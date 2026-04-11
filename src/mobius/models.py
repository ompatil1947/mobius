from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class Page:
    source_path: Path
    output_path: Path
    slug: str
    title: str
    metadata: dict[str, Any]
    body: str
    html: str = ""
    url: str = ""
    template: str = "page.html"
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Site:
    title: str
    description: str
    pages: list[Page]
    output_dir: Path
    theme_dir: Path
    plugin_dir: Path
