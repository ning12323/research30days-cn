"""Data models for research30days-cn."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SearchItem:
    title: str
    url: str
    snippet: str
    source: str
    published: str | None = None
    score: float = 0.0


@dataclass
class SourceResult:
    source: str
    label: str
    items: list[SearchItem] = field(default_factory=list)
    error: str | None = None


@dataclass
class Report:
    topic: str
    days: int
    queried_at: datetime
    sources: list[SourceResult] = field(default_factory=list)

    @property
    def total_items(self) -> int:
        return sum(len(s.items) for s in self.sources)

    @property
    def successful_sources(self) -> list[SourceResult]:
        return [s for s in self.sources if s.items]
