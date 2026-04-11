from __future__ import annotations

import importlib.util
import logging
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

from .models import Page, Site

LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class LoadedPlugin:
    name: str
    module: ModuleType
    instance: object


def load_plugins(plugin_dir: Path) -> list[LoadedPlugin]:
    plugins: list[LoadedPlugin] = []
    if not plugin_dir.exists():
        return plugins

    for path in sorted(plugin_dir.glob("*.py")):
        if path.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"mobius_plugin_{path.stem}", path)
        if spec is None or spec.loader is None:
            continue
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        factory = getattr(module, "register", None)
        if callable(factory):
            instance = factory()
            plugins.append(LoadedPlugin(name=path.stem, module=module, instance=instance))
            LOGGER.debug("Loaded plugin %s", path.stem)
    return plugins


def apply_page_hooks(plugins: list[LoadedPlugin], page: Page, site: Site) -> Page:
    for plugin in plugins:
        hook = getattr(plugin.instance, "on_page", None)
        if callable(hook):
            result = hook(page, site)
            if result is not None:
                page = result
    return page


def apply_site_hooks(plugins: list[LoadedPlugin], site: Site) -> Site:
    for plugin in plugins:
        hook = getattr(plugin.instance, "on_site", None)
        if callable(hook):
            result = hook(site)
            if result is not None:
                site = result
    return site
