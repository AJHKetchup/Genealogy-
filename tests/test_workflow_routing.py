from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_site_generator_changes_do_not_wake_internal_research_or_conversion() -> None:
    internal = (ROOT / ".github" / "workflows" / "internal-research-agents.yml").read_text(encoding="utf-8")
    conversion = (ROOT / ".github" / "workflows" / "cloud-source-prep.yml").read_text(encoding="utf-8")
    site = (ROOT / ".github" / "workflows" / "wiki-site.yml").read_text(encoding="utf-8")

    assert '"src/historic_doc_ingest/**"' in site
    assert '"src/historic_doc_ingest/**"' in internal
    assert '"!src/historic_doc_ingest/wiki_site.py"' in internal
    assert '"src/historic_doc_ingest/**"' in conversion
    assert '"!src/historic_doc_ingest/wiki_site.py"' in conversion
    assert "cancel-in-progress: false" in internal
    assert "cancel-in-progress: false" in conversion


def test_scheduled_internal_runs_do_not_skip_waiting_promotion() -> None:
    internal = (ROOT / ".github" / "workflows" / "internal-research-agents.yml").read_text(encoding="utf-8")

    assert "disabled_requires_allow_promotion" in internal
    assert "$promotionWaiting" in internal
    assert "$ageMinutes -lt $freshMinutes -and -not $promotionWaiting" in internal
    assert "scheduled promotion-capable run will proceed" in internal
