#!/usr/bin/env python3
"""research30days-cn CLI - 中文多源近30天调研引擎."""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

if os.name == "nt":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SCRIPT_DIR))

from lib.render import render_compact, render_json, render_markdown_report  # noqa: E402
from lib.schema import Report  # noqa: E402
from lib.sources import DEFAULT_SOURCES, SOURCE_CONFIG, run_searches  # noqa: E402

VERSION = "0.1.0"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value.lower()).strip("-")
    return slug or "research"


def parse_sources(raw: str | None) -> list[str]:
    if not raw:
        return list(DEFAULT_SOURCES)
    keys: list[str] = []
    for part in raw.split(","):
        key = part.strip().lower()
        if not key:
            continue
        if key not in SOURCE_CONFIG:
            valid = ", ".join(sorted(SOURCE_CONFIG))
            raise SystemExit(f"未知来源: {key}。可选: {valid}")
        if key not in keys:
            keys.append(key)
    if not keys:
        raise SystemExit("至少指定一个来源。")
    return keys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="research30days-cn",
        description="调研某个话题在中文互联网近 N 天的讨论与内容。",
    )
    parser.add_argument("topic", help="调研主题，如: AI Agent 工具")
    parser.add_argument(
        "--days",
        type=int,
        default=30,
        help="回溯天数，默认 30",
    )
    parser.add_argument(
        "--sources",
        default=",".join(DEFAULT_SOURCES),
        help="逗号分隔来源: web,zhihu,bilibili,sspai",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=8,
        help="每个来源最多返回条数，默认 8",
    )
    parser.add_argument(
        "--emit",
        choices=["compact", "json", "md"],
        default="compact",
        help="输出格式，默认 compact（供 Agent 综合）",
    )
    parser.add_argument(
        "--save",
        metavar="DIR",
        help="保存完整报告到目录",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    topic = args.topic.strip()
    if not topic:
        print("主题不能为空。", file=sys.stderr)
        return 2

    source_keys = parse_sources(args.sources)
    queried_at = datetime.now(timezone.utc)

    source_results = run_searches(
        topic,
        source_keys,
        max_results=args.max_results,
        days=args.days,
    )

    report = Report(
        topic=topic,
        days=args.days,
        queried_at=queried_at,
        sources=source_results,
    )

    if args.emit == "json":
        output = render_json(report)
    elif args.emit == "md":
        output = render_markdown_report(report)
    else:
        output = render_compact(report)

    print(output)

    if args.save:
        out_dir = Path(args.save).expanduser().resolve()
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{slugify(topic)}-raw.md"
        out_path.write_text(render_markdown_report(report), encoding="utf-8")
        print(f"\n已保存: {out_path}", file=sys.stderr)

    if report.total_items == 0:
        print(
            "\n⚠️ 未检索到结果。可尝试: 缩短主题词、增加 --sources、或稍后重试。",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
