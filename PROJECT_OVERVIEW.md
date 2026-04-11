# Project overview

Mobius is a static documentation site generator built around a simple pipeline:

1. Markdown content is read from `content/`.
2. YAML front matter is parsed by `osmium`.
3. Metadata and body text are converted into page objects.
4. Jinja2 templates in `themes/default/` render the HTML.
5. The local plugin in `plugins/` adds page decoration from metadata.
6. The generated site is written to `site/` and compared with `expected_site/`.

The result is a small but complete documentation site generator with a stable
output structure and a straightforward build flow.

## Summary of the implementation

- `mobius.cli` exposes the command line interface
- `mobius.builder` coordinates loading, rendering, and writing files
- `mobius.content` scans Markdown sources and prepares page data
- `mobius.plugins` loads local extensions
- `mobius.theme` wraps Jinja2 environment setup and rendering

This structure keeps metadata handling, rendering, and plugin behavior separate
enough to remain easy to maintain.
