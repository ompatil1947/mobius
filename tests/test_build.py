from filecmp import cmp
from pathlib import Path

from mobius.builder import build_site


def _collect_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def test_generated_site_matches_reference(project_root: Path, tmp_path: Path):
    output_dir = tmp_path / "site"
    build_site(
        project_root / "content",
        output_dir,
        project_root / "themes/default",
        project_root / "plugins",
    )

    expected_root = project_root / "expected_site"
    generated_files = _collect_files(output_dir)
    expected_files = _collect_files(expected_root)

    assert [path.relative_to(output_dir) for path in generated_files] == [
        path.relative_to(expected_root) for path in expected_files
    ]

    for generated in generated_files:
        expected = expected_root / generated.relative_to(output_dir)
        assert cmp(generated, expected, shallow=False)
