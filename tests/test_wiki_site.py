from __future__ import annotations

from historic_doc_ingest import genealogy_wiki
from historic_doc_ingest.genealogy_wiki import init_genealogy_wiki
from historic_doc_ingest.wiki_site import build_wiki_site


def test_build_wiki_site_renders_pages_search_data_and_graph(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    parent = tmp_path / "wiki" / "people" / "parent.md"
    child = tmp_path / "wiki" / "people" / "child.md"
    parent.write_text(
        """---
type: person
display_name: Parent Person
birth: 1888
---
# Parent Person

Connected to [[people/child|Child Person]] through a sourced family clue.
""",
        encoding="utf-8",
    )
    child.write_text(
        """---
type: person
display_name: Child Person
birth: 1912
---
# Child Person

See [[people/parent|Parent Person]].
""",
        encoding="utf-8",
    )

    output = build_wiki_site(tmp_path, tmp_path / "site")

    assert (output / "index.html").exists()
    assert (output / "graph.html").exists()
    assert (output / "timeline.html").exists()
    parent_html = (output / "wiki" / "people" / "parent.html").read_text(encoding="utf-8")
    data_js = (output / "assets" / "site-data.js").read_text(encoding="utf-8")
    assert "Child Person" in parent_html
    assert "../../wiki/people/child.html" in parent_html
    assert "Parent Person" in data_js
    assert '"type": "wikilink"' in data_js
    assert "1888" in data_js


def test_genealogy_wiki_site_cli(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    exit_code = genealogy_wiki.main(["site", "--root", str(tmp_path), "--out", str(tmp_path / "public"), "--wiki-only"])

    assert exit_code == 0
    assert (tmp_path / "public" / "index.html").exists()
    assert (tmp_path / "public" / "assets" / "app.js").exists()
