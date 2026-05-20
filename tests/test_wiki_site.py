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
    assert (output / "tree.html").exists()
    assert (output / "people.html").exists()
    assert (output / "research.html").exists()
    assert (output / "graph.html").exists()
    assert (output / "timeline.html").exists()
    people_html = (output / "people.html").read_text(encoding="utf-8")
    parent_html = (output / "wiki" / "people" / "parent.html").read_text(encoding="utf-8")
    data_js = (output / "assets" / "site-data.js").read_text(encoding="utf-8")
    assert "Child Person" in parent_html
    assert "Parent Person" in people_html
    assert "../../wiki/people/child.html" in parent_html
    assert "Parent Person" in data_js
    assert '"familyWiki"' in data_js
    assert '"type": "wikilink"' in data_js
    assert "1888" in data_js


def test_wiki_site_surfaces_converted_sources_and_filters_ops_timeline(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    converted = tmp_path / "raw" / "converted"
    converted.mkdir(parents=True, exist_ok=True)
    source = converted / "ca12345678-registro-de-nacimientos-1889.codex.md"
    source.write_text(
        """# Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1889

## Conversion Metadata

- Source: `raw/sources/register.png`
- Manifest: `raw/codex-conversion-jobs/manifest.json`

## Page Metadata

- **Document Type:** Birth Register
- **Year:** 1889
- **Location:** Los Angeles, Chile

## Layout And Reading Order

The page records the birth of a Pulgar child in a handwritten civil register.
""",
        encoding="utf-8",
    )
    research_dashboard = tmp_path / "research" / "Post-Conversion Dashboard.md"
    research_dashboard.write_text("# Post-Conversion Dashboard\n\nUpdated 2026-05-19.\n", encoding="utf-8")

    output = build_wiki_site(tmp_path, tmp_path / "site")

    data_js = (output / "assets" / "site-data.js").read_text(encoding="utf-8")
    index_html = (output / "index.html").read_text(encoding="utf-8")
    research_html = (output / "research.html").read_text(encoding="utf-8")
    sources_html = (output / "sources.html").read_text(encoding="utf-8")
    assert '"Converted sources"' in data_js
    assert '"displayTitle"' in data_js
    assert "Registro de Nacimientos" in data_js
    timeline_blob = data_js.split('"timeline":', 1)[1].split('"dashboard":', 1)[0]
    assert "Post-Conversion Dashboard" not in timeline_blob
    assert "Registro de Nacimientos" not in timeline_blob
    assert "Alexander John Heinz Family History" in index_html
    assert "Agent Queues" not in index_html
    assert "Internal Research Operations" in research_html
    assert "Agent Queues" in research_html
    assert "Source Library" in sources_html
    assert any((output / "sources").glob("ca12345678-registro-de-nacimientos-1889*.html"))


def test_genealogy_wiki_site_cli(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    exit_code = genealogy_wiki.main(["site", "--root", str(tmp_path), "--out", str(tmp_path / "public"), "--wiki-only"])

    assert exit_code == 0
    assert (tmp_path / "public" / "index.html").exists()
    assert (tmp_path / "public" / "assets" / "app.js").exists()
