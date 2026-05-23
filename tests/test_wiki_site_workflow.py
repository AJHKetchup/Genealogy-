from __future__ import annotations

from pathlib import Path


def test_wiki_site_workflow_fails_if_pages_cannot_be_enabled() -> None:
    workflow = (Path(__file__).resolve().parents[1] / ".github" / "workflows" / "wiki-site.yml").read_text(
        encoding="utf-8"
    )

    assert "pages: write" in workflow
    assert "id-token: write" in workflow
    assert "GitHub Pages is not enabled" in workflow
    assert "exit 1" in workflow
    assert "Published gh-pages, but this token cannot enable Pages" not in workflow
