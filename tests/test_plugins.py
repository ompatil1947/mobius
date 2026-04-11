from pathlib import Path

from mobius.builder import build_site


def test_feature_plugin_adds_markup(project_root: Path, tmp_path: Path):
    output_dir = tmp_path / "site"
    build_site(
        project_root / "content",
        output_dir,
        project_root / "themes/default",
        project_root / "plugins",
    )

    index_html = (output_dir / "index.html").read_text(encoding="utf-8")
    assert "Featured" in index_html
    assert "page--featured" in index_html
