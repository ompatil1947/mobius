from __future__ import annotations

import logging
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

LOGGER = logging.getLogger(__name__)


class _ReloadHandler(FileSystemEventHandler):
    def __init__(self, rebuild) -> None:
        self.rebuild = rebuild

    def on_any_event(self, event):  # type: ignore[override]
        if event.is_directory:
            return
        LOGGER.info("Change detected: %s", event.src_path)
        self.rebuild()


def serve_directory(directory: Path, host: str, port: int) -> ThreadingHTTPServer:
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    server = ThreadingHTTPServer((host, port), handler)
    LOGGER.info("Serving %s at http://%s:%s", directory, host, port)
    return server


def watch_sources(paths: list[Path], rebuild) -> Observer:
    observer = Observer()
    handler = _ReloadHandler(rebuild)
    for path in paths:
        observer.schedule(handler, str(path), recursive=True)
    observer.start()
    return observer
