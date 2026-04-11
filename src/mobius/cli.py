from __future__ import annotations

import logging
from pathlib import Path

import click

from .builder import build_site
from .server import serve_directory, watch_sources


DEFAULT_CONTENT = Path("content")
DEFAULT_OUTPUT = Path("site")
DEFAULT_THEME = Path("themes/default")
DEFAULT_PLUGINS = Path("plugins")


def _setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s %(name)s: %(message)s")


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--verbose", is_flag=True, help="Enable debug logging.")
def main(verbose: bool) -> None:
    _setup_logging(verbose)


@main.command()
@click.option("--content-dir", type=click.Path(path_type=Path), default=DEFAULT_CONTENT)
@click.option("--output-dir", type=click.Path(path_type=Path), default=DEFAULT_OUTPUT)
@click.option("--theme-dir", type=click.Path(path_type=Path), default=DEFAULT_THEME)
@click.option("--plugin-dir", type=click.Path(path_type=Path), default=DEFAULT_PLUGINS)
def build(content_dir: Path, output_dir: Path, theme_dir: Path, plugin_dir: Path) -> None:
    build_site(content_dir, output_dir, theme_dir, plugin_dir)
    click.echo(f"Built site in {output_dir}")


@main.command()
@click.option("--content-dir", type=click.Path(path_type=Path), default=DEFAULT_CONTENT)
@click.option("--output-dir", type=click.Path(path_type=Path), default=DEFAULT_OUTPUT)
@click.option("--theme-dir", type=click.Path(path_type=Path), default=DEFAULT_THEME)
@click.option("--plugin-dir", type=click.Path(path_type=Path), default=DEFAULT_PLUGINS)
@click.option("--host", default="127.0.0.1")
@click.option("--port", default=8000, type=int)
@click.option("--watch/--no-watch", default=False)
def serve(
    content_dir: Path,
    output_dir: Path,
    theme_dir: Path,
    plugin_dir: Path,
    host: str,
    port: int,
    watch: bool,
) -> None:
    def rebuild() -> None:
        build_site(content_dir, output_dir, theme_dir, plugin_dir)

    rebuild()
    observer = None
    if watch:
        observer = watch_sources([content_dir, theme_dir, plugin_dir], rebuild)

    server = serve_directory(output_dir, host, port)
    try:
        server.serve_forever()
    finally:
        server.server_close()
        if observer is not None:
            observer.stop()
            observer.join()


if __name__ == "__main__":
    main()
