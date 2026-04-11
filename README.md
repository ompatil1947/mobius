# Mobius

Mobius is a compact static documentation site generator for Markdown-based
projects.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## What it does

- converts Markdown content into a static HTML site
- reads YAML front matter for page metadata
- renders pages with Jinja2 themes
- loads small plugins from the local `plugins/` directory
- rebuilds content while files change

## Layout

- `content/` contains source Markdown files
- `themes/default/` provides the built-in templates
- `plugins/` holds local extensions
- `expected_site/` stores the reference HTML output

## Documentation

- [Installation](INSTALLATION.md)
- [Contributing](CONTRIBUTING.md)
- [Project overview](PROJECT_OVERVIEW.md)
- [Maintainer flow](MAINTAINER_FLOW.md)

## Usage

```bash
mobius build
mobius serve --watch
```

The default build writes to `site/`.
