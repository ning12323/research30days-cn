"""Tests for research30days-cn."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "skills" / "research30days-cn" / "scripts"
sys.path.insert(0, str(SCRIPTS))

from lib.render import render_compact  # noqa: E402
from lib.schema import Report, SearchItem, SourceResult  # noqa: E402


def test_render_compact_includes_badge():
    from datetime import datetime, timezone

    report = Report(
        topic="测试",
        days=30,
        queried_at=datetime(2026, 6, 19, tzinfo=timezone.utc),
        sources=[
            SourceResult(
                source="web",
                label="全网",
                items=[
                    SearchItem(
                        title="示例",
                        url="https://example.com",
                        snippet="snippet",
                        source="web",
                        score=1.0,
                    )
                ],
            )
        ],
    )
    text = render_compact(report)
    assert "research30days-cn" in text
    assert "测试" in text
    assert "示例" in text
