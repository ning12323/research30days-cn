"""Output renderers for research30days-cn."""

from __future__ import annotations

import json
from datetime import datetime

from .schema import Report, SearchItem


def _format_item(idx: int, item: SearchItem) -> str:
    date_part = f" | {item.published}" if item.published else ""
    snippet = item.snippet.replace("\n", " ").strip()
    if len(snippet) > 160:
        snippet = snippet[:157] + "..."
    return (
        f"{idx}. [{item.source}] {item.title}{date_part}\n"
        f"   {snippet}\n"
        f"   {item.url}"
    )


def render_compact(report: Report) -> str:
    synced = report.queried_at.strftime("%Y-%m-%d")
    lines = [
        f"🇨🇳 research30days-cn v0.1.0 · synced {synced}",
        "",
        f"主题: {report.topic}",
        f"时间范围: 近 {report.days} 天",
        f"命中: {report.total_items} 条 · 来源: {len(report.successful_sources)}/{len(report.sources)}",
        "",
        "## 证据簇（供 Agent 综合，勿原样输出给用户）",
        "",
    ]

    cluster_idx = 1
    for source in report.sources:
        if source.error and not source.items:
            lines.append(f"### {cluster_idx}. {source.label}（失败: {source.error}）")
            lines.append("")
            cluster_idx += 1
            continue
        if not source.items:
            continue
        lines.append(
            f"### {cluster_idx}. {source.label} "
            f"(score {sum(i.score for i in source.items):.1f}, "
            f"{len(source.items)} 条)"
        )
        lines.append("")
        for i, item in enumerate(source.items, 1):
            lines.append(_format_item(i, item))
            lines.append("")
        cluster_idx += 1

    lines.extend(
        [
            "---",
            "<!-- END EVIDENCE -->",
            "",
            "## Agent 输出指引",
            "",
            "请根据上方证据综合成中文报告，格式见 references/output-template.md。",
            "禁止原样粘贴证据簇；必须提炼共识、争议与可跟进链接。",
        ]
    )
    return "\n".join(lines)


def render_json(report: Report) -> str:
    payload = {
        "topic": report.topic,
        "days": report.days,
        "queried_at": report.queried_at.isoformat(),
        "sources": [
            {
                "source": s.source,
                "label": s.label,
                "error": s.error,
                "items": [
                    {
                        "title": i.title,
                        "url": i.url,
                        "snippet": i.snippet,
                        "published": i.published,
                        "score": i.score,
                    }
                    for i in s.items
                ],
            }
            for s in report.sources
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def render_markdown_report(report: Report) -> str:
    """Full markdown artifact for saving to disk."""
    header = render_compact(report)
    footer = [
        "",
        "## 元数据",
        "",
        f"- 查询时间: {report.queried_at.isoformat()}",
        f"- 总条目: {report.total_items}",
    ]
    return header + "\n".join(footer)
