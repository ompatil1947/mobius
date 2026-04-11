from __future__ import annotations

import logging
import shutil
from dataclasses import asdict
from pathlib import Path

from .content import load_pages, sort_pages
from .models import Site
from .plugins import apply_page_hooks, apply_site_hooks, load_plugins
from .theme import create_environment, render_template

LOGGER = logging.getLogger(__name__)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _clear_output(output_dir: Path) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)


def build_site(
    content_dir: Path,
    output_dir: Path,
    theme_dir: Path,
    plugin_dir: Path,
    *,
    site_title: str = "Mobius",
    site_description: str = "A small static documentation site generator.",
) -> Site:
    _clear_output(output_dir)
    env = create_environment(theme_dir)
    pages = sort_pages(load_pages(content_dir, output_dir))
    site = Site(
        title=site_title,
        description=site_description,
        pages=pages,
        output_dir=output_dir,
        theme_dir=theme_dir,
        plugin_dir=plugin_dir,
    )
    plugins = load_plugins(plugin_dir)
    site = apply_site_hooks(plugins, site)

    for page in pages:
        page.extra.setdefault("site_title", site.title)
        page.extra.setdefault("site_description", site.description)
        page = apply_page_hooks(plugins, page, site)
        template_name = "index.html" if page.slug == "index" else "page.html"
        context = {
            "site": site,
            "page": page,
            "pages": pages,
            "navigation": pages,
            "page_data": asdict(page),
        }
        rendered = render_template(env, template_name, context)
        _write_text(page.output_path, rendered)
        LOGGER.info("Rendered %s", page.output_path)

    return site
