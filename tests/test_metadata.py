from pathlib import Path

from mobius.content import load_pages


def test_metadata_is_loaded_as_lists_and_strings(project_root: Path, tmp_path: Path):
    pages = load_pages(project_root / "content", tmp_path)
    index = next(page for page in pages if page.slug == "index")

    assert index.metadata["title"] == "Mobius"
    assert index.metadata["featured"] is True
    assert index.metadata["tags"] == ["docs", "home"]
