from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

from historic_doc_ingest.genealogy_wiki import init_genealogy_wiki
from historic_doc_ingest.wiki_site import build_wiki_site


def test_build_wiki_site_worker_embeds_generated_site(tmp_path: Path) -> None:
    node = shutil.which("node")
    if not node:
        pytest.skip("node is required to build the embedded Cloudflare Worker")

    init_genealogy_wiki(tmp_path)
    person = tmp_path / "wiki" / "people" / "dario-arturo-pulgar-smith.md"
    person.write_text(
        """---
type: person
display_name: Dario Arturo Pulgar-Smith
---
# Dario Arturo Pulgar-Smith

Evidence-backed person page.
""",
        encoding="utf-8",
    )
    site_dir = build_wiki_site(tmp_path, tmp_path / "site", include_research=False)
    worker_path = tmp_path / "site-worker" / "index.mjs"
    script_path = Path(__file__).resolve().parents[1] / "scripts" / "build-wiki-site-worker.mjs"

    result = subprocess.run(
        [node, str(script_path), str(site_dir), str(worker_path)],
        check=True,
        capture_output=True,
        text=True,
    )

    worker_source = worker_path.read_text(encoding="utf-8")
    assert "Embedded" in result.stdout
    assert "export default" in worker_source
    assert "/index.html" in worker_source
    assert "dario-arturo-pulgar-smith.html" in worker_source
    assert "bytesFromBase64" in worker_source
