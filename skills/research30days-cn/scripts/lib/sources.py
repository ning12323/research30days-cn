"""Search adapters for Chinese web sources."""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from typing import Callable
from urllib.parse import urlparse

import httpx

from .schema import SearchItem, SourceResult

try:
    from ddgs import DDGS
except ImportError:  # pragma: no cover - legacy package name
    from duckduckgo_search import DDGS  # type: ignore[no-redef]

SOURCE_CONFIG: dict[str, dict[str, str]] = {
    "web": {
        "label": "全网",
        "query_suffix": "",
        "region": "cn-zh",
    },
    "zhihu": {
        "label": "知乎",
        "query_suffix": " site:zhihu.com",
        "region": "cn-zh",
    },
    "bilibili": {
        "label": "B站",
        "query_suffix": " site:bilibili.com",
        "region": "cn-zh",
    },
    "sspai": {
        "label": "少数派",
        "query_suffix": " site:sspai.com",
        "region": "cn-zh",
    },
}

DEFAULT_SOURCES = ["web", "zhihu", "bilibili"]


def _normalize_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip("/")


def _dedupe_items(items: list[SearchItem]) -> list[SearchItem]:
    seen: set[str] = set()
    unique: list[SearchItem] = []
    for item in items:
        key = _normalize_url(item.url)
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def _score_item(item: SearchItem, topic: str) -> float:
    topic_terms = [t for t in re.split(r"\s+", topic.lower()) if t]
    haystack = f"{item.title} {item.snippet}".lower()
    hits = sum(1 for term in topic_terms if term in haystack)
    source_boost = {"zhihu": 1.2, "bilibili": 1.1, "sspai": 1.05}.get(item.source, 1.0)
    return hits * source_boost


def search_ddg(
    topic: str,
    source_key: str,
    *,
    max_results: int = 8,
    timelimit: str = "m",
) -> SourceResult:
    cfg = SOURCE_CONFIG[source_key]
    query = f"{topic}{cfg['query_suffix']}".strip()
    label = cfg["label"]

    try:
        ddgs = DDGS()
        raw = list(
            ddgs.text(
                query,
                region=cfg["region"],
                safesearch="moderate",
                timelimit=timelimit,
                max_results=max_results,
            )
        )
    except Exception as exc:  # noqa: BLE001 - surface source errors to caller
        return SourceResult(source=source_key, label=label, error=str(exc))

    items: list[SearchItem] = []
    for row in raw:
        title = (row.get("title") or "").strip()
        url = (row.get("href") or row.get("url") or "").strip()
        snippet = (row.get("body") or row.get("snippet") or "").strip()
        if not title or not url:
            continue
        item = SearchItem(
            title=title,
            url=url,
            snippet=snippet,
            source=source_key,
            published=row.get("date"),
        )
        item.score = _score_item(item, topic)
        items.append(item)

    items = _dedupe_items(items)
    items.sort(key=lambda x: x.score, reverse=True)
    return SourceResult(source=source_key, label=label, items=items)


def search_bilibili_api(topic: str, *, max_results: int = 8) -> SourceResult:
    """Fallback B站 search via public API when DDG results are thin."""
    url = "https://api.bilibili.com/x/web-interface/search/type"
    params = {
        "search_type": "video",
        "keyword": topic,
        "page": 1,
        "order": "totalrank",
        "page_size": max_results,
    }
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Referer": "https://www.bilibili.com",
    }

    try:
        with httpx.Client(timeout=15.0, headers=headers) as client:
            resp = client.get(url, params=params)
            resp.raise_for_status()
            payload = resp.json()
    except Exception as exc:  # noqa: BLE001
        return SourceResult(source="bilibili", label="B站", error=str(exc))

    if payload.get("code") != 0:
        return SourceResult(
            source="bilibili",
            label="B站",
            error=payload.get("message") or "bilibili api error",
        )

    result = payload.get("data", {}).get("result", []) or []
    items: list[SearchItem] = []
    for row in result[:max_results]:
        title = re.sub(r"<[^>]+>", "", row.get("title") or "").strip()
        bvid = row.get("bvid") or ""
        aid = row.get("aid")
        if bvid:
            link = f"https://www.bilibili.com/video/{bvid}"
        elif aid:
            link = f"https://www.bilibili.com/video/av{aid}"
        else:
            continue
        desc = re.sub(r"<[^>]+>", "", row.get("description") or "").strip()
        pubdate = row.get("pubdate")
        published = None
        if pubdate:
            published = datetime.fromtimestamp(int(pubdate), tz=timezone.utc).strftime(
                "%Y-%m-%d"
            )
        item = SearchItem(
            title=title,
            url=link,
            snippet=desc,
            source="bilibili",
            published=published,
        )
        item.score = _score_item(item, topic)
        items.append(item)

    return SourceResult(source="bilibili", label="B站", items=items)


SearchFn = Callable[..., SourceResult]


def run_searches(
    topic: str,
    source_keys: list[str],
    *,
    max_results: int = 8,
    days: int = 30,
) -> list[SourceResult]:
    timelimit = "m" if days >= 28 else "w" if days >= 7 else "d"
    results: list[SourceResult] = []

    for key in source_keys:
        if key not in SOURCE_CONFIG:
            continue
        result = search_ddg(topic, key, max_results=max_results, timelimit=timelimit)
        if key == "bilibili" and len(result.items) < 3:
            api_result = search_bilibili_api(topic, max_results=max_results)
            if api_result.items:
                merged = _dedupe_items(result.items + api_result.items)
                merged.sort(key=lambda x: x.score, reverse=True)
                result.items = merged[:max_results]
                result.error = None
        results.append(result)

    return results


def cutoff_date(days: int) -> datetime:
    return datetime.now(timezone.utc) - timedelta(days=days)
