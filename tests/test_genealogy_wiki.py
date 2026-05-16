import json
from pathlib import Path

import pytest

from historic_doc_ingest import genealogy_wiki
from historic_doc_ingest.genealogy_wiki import (
    build_static_site,
    build_source_prep_batch_agent_tasks,
    build_claim_index,
    build_relationship_index,
    chunk_converted_markdown,
    cloud_source_prep_heartbeat,
    compile_narrative,
    assemble_codex_conversion_job,
    create_claim,
    create_codex_conversion_job,
    create_material_packet,
    create_relationship,
    create_source_packet,
    ensure_source_prep_page_image,
    generate_tree,
    find_suspicious_name_readings,
    init_genealogy_wiki,
    lint_genealogy_wiki,
    mark_source_relevance_feedback,
    monitor_r2_source_intake,
    release_stale_agent_tasks,
    research_analyzer_run,
    write_claim_index,
    write_relationship_graph,
    write_relationship_index,
    write_source_prep_index,
    write_source_usability_report,
    write_storage_lifecycle_report,
    write_system_status_dashboard,
    write_agent_queues,
    write_source_prep_batches,
    write_post_conversion_qc,
    next_codex_conversion_work_order,
    prepare_raw_sources,
    promote_staged_drafts,
    source_prep_page_cache_path,
    source_prep_fastlane_run,
    source_relevance_hint_matches_task,
    review_source_prep_page_output,
    sync_vault_transcriptions,
    sync_github_database,
    update_agent_task_state,
    update_agent_task_states,
)


def complete_page_markdown(transcription: str = "Converted by Codex.") -> str:
    return f"""# Page 1

## Page Metadata

Page converted from the prepared page image.

## Layout And Reading Order

Single-page source read top to bottom.

## Literal Transcription

{transcription}

## Images, Captions, And Visual Notes

No separate visual regions identified.

## Uncertain Or Illegible

None noted.

## Completeness Audit

The visible page was reviewed against the page image.
"""


def complete_gemini_page_markdown(transcription: str = "Converted by Gemini.") -> str:
    return (
        complete_page_markdown(transcription)
        + """

## Visual Region Manifest

```json
{"visual_regions": [], "no_visual_regions_reason": "No substantial standalone visual evidence."}
```
"""
    )


def test_init_genealogy_wiki_creates_operating_files(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    assert (tmp_path / "GENEALOGY_WIKI.md").exists()
    assert (tmp_path / "wiki" / "Family Tree.md").exists()
    assert (tmp_path / "wiki" / "index.md").exists()
    assert (tmp_path / "research" / "00 Research Start.md").exists()
    assert (tmp_path / "research" / "index.md").exists()
    assert (tmp_path / "research" / "log.md").exists()
    assert (tmp_path / "research" / "research-plan.md").exists()
    assert (tmp_path / "research" / "questions").exists()
    assert (tmp_path / "research" / "tasks").exists()
    assert (tmp_path / "research" / "_templates" / "person.md").exists()
    assert (tmp_path / "research" / "_templates" / "claim.md").exists()
    source_template = (tmp_path / "research" / "_templates" / "source.md").read_text(encoding="utf-8")
    packet_template = (tmp_path / "research" / "_templates" / "source-packet.md").read_text(encoding="utf-8")
    claim_template = (tmp_path / "research" / "_templates" / "claim.md").read_text(encoding="utf-8")
    assert "source_reliability_score: 0.0" in source_template
    assert "## Source Reliability" in packet_template
    assert "## Conversion Confidence" in claim_template
    assert not (tmp_path / "wiki" / "relationships").exists()
    assert not (tmp_path / "wiki" / "claims").exists()
    assert not (tmp_path / "wiki" / "evidence").exists()
    assert not (tmp_path / "wiki" / "tasks").exists()
    assert not (tmp_path / "wiki" / "questions").exists()
    assert not (tmp_path / "wiki" / "research-plan.md").exists()
    assert not (tmp_path / "wiki" / "00 Start Here.md").exists()
    assert not (tmp_path / "wiki" / "log.md").exists()
    assert (tmp_path / "research" / "source-packets").exists()
    assert (tmp_path / "research" / "_conversion-review").exists()
    assert (tmp_path / "research" / "_conversion-review" / "page-queues").exists()
    assert (tmp_path / "research" / "_conversion-review" / "corrections").exists()
    assert (tmp_path / "research" / "_staging").exists()
    assert (tmp_path / "research" / "_staging" / "photos").exists()
    assert (tmp_path / "research" / "_indexes").exists()
    assert (tmp_path / "research" / "claims").exists()
    assert (tmp_path / "research" / "relationships").exists()
    assert (tmp_path / "research" / "evidence").exists()
    assert (tmp_path / "raw" / "converted").exists()
    assert (tmp_path / "raw" / "chunks").exists()


def test_lint_genealogy_wiki_passes_fresh_scaffold(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    assert lint_genealogy_wiki(tmp_path) == []


def test_lint_flags_research_workflow_language_in_public_wiki(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    person = tmp_path / "wiki" / "people" / "process-leak.md"
    person.write_text(
        """---
type: person
status: stub
---

# Process Leak

This public page still talks about the proof-layer and research vault.

## See Also

- [[Family Tree]]
""",
        encoding="utf-8",
    )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(index.read_text(encoding="utf-8") + "\n- [[people/process-leak]]\n", encoding="utf-8")

    issues = lint_genealogy_wiki(tmp_path)

    assert "wiki product page uses research workflow language 'research vault': people/process-leak.md" in issues
    assert "wiki product page uses research workflow language 'proof-layer': people/process-leak.md" in issues


def test_lint_accepts_aliased_wiki_index_links(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    person = tmp_path / "wiki" / "people" / "dario-pulgar-adult-passenger.md"
    person.write_text(
        """---
type: person
status: stub
---

# Dario Pulgar (1953 passenger)

See [[Family Tree]].
""",
        encoding="utf-8",
    )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        index.read_text(encoding="utf-8")
        + "\n- [[people/dario-pulgar-adult-passenger|Dario Pulgar (1953 passenger)]]\n",
        encoding="utf-8",
    )

    assert "page not referenced from index: people/dario-pulgar-adult-passenger.md" not in lint_genealogy_wiki(tmp_path)


def test_lint_genealogy_wiki_ignores_system_staging_drafts(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    staged_claim = tmp_path / "research" / "_staging" / "claims" / "CLD001-draft.md"
    staged_claim.parent.mkdir(parents=True, exist_ok=True)
    staged_claim.write_text(
        """---
type: claim
status: draft
---

# Draft Claim

This draft is intentionally incomplete and not linked from the canonical index.
""",
        encoding="utf-8",
    )

    assert lint_genealogy_wiki(tmp_path) == []


def test_promote_staged_drafts_updates_visible_wiki_product(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    staged_packets = tmp_path / "research" / "_staging" / "source-packets"
    staged_claims = tmp_path / "research" / "_staging" / "claims"
    staged_packets.mkdir(parents=True, exist_ok=True)
    staged_claims.mkdir(parents=True, exist_ok=True)
    staged_packet = staged_packets / "SP-STAGE-Test-Source.md"
    staged_packet.write_text(
        """---
type: source_packet
status: draft
source_id: SP-STAGE-TEST
source_kind: civil_register
raw_file: raw/sources/test-source.png
converted_file: raw/converted/test-source.codex.md
created: 2026-05-15
tags: [source-packet, staging]
---

# Source Packet: Test Source

## Source Identity

- Source path: `raw/sources/test-source.png`

## Source Reliability

- Reliability class: original.

## Page And Image Map

## Literal Transcription

The register names Test Person.

## Translation

Not needed.

## Interpretation

The record supports one claim.

## Uncertain Or Illegible

None.

## Extracted Atomic Claims

| Claim | Status | Confidence | Claim Page |
| --- | --- | ---: | --- |
| Test Person was recorded. | draft | 8.0 | [[claims/CL-STAGE-Test-Person-Name]] |
""",
        encoding="utf-8",
    )
    (staged_claims / "CL-STAGE-Test-Person-Name.md").write_text(
        """---
type: claim
status: draft
claim_type: name
confidence: 8.0
subject: Test Person
predicate: recorded_name
object: Test Person
date: 1900-01-01
place: Test Place
source: raw/converted/test-source.codex.md
source_packet: research/_staging/source-packets/SP-STAGE-Test-Source.md
promotion_recommendation: promote
tags: [claim, staging]
---

# Atomic Claim: Test Person Name

## Claim

The record names Test Person.

## Status

Draft.

## Confidence

8.0/10.

## Source Reliability

- Reliability class: original.

## Conversion Confidence

- Reading confidence: high.

## Literal Source Support

```text
Test Person
```

## Translation

Not needed.

## Interpretation

This is a name claim.

## Uncertainty

No uncertainty.

## Supports

## Conflicts With
""",
        encoding="utf-8",
    )

    summary = promote_staged_drafts(tmp_path)

    claim_path = tmp_path / "research" / "claims" / "cl-stage-test-person-name.md"
    packet_path = tmp_path / "research" / "source-packets" / "sp-stage-test-source.md"
    person_path = tmp_path / "wiki" / "people" / "test-person.md"
    assert claim_path.exists()
    assert packet_path.exists()
    assert person_path.exists()
    claim_text = claim_path.read_text(encoding="utf-8")
    assert "subject: [[people/test-person]]" in claim_text
    assert "source: [[sources/" in claim_text
    assert "source_packet: [[source-packets/sp-stage-test-source]]" in claim_text
    assert "[[claims/cl-stage-test-person-name]]" in (tmp_path / "research" / "index.md").read_text(encoding="utf-8")
    assert "[[people/test-person]]" in (tmp_path / "wiki" / "index.md").read_text(encoding="utf-8")
    assert "[[claims/cl-stage-test-person-name]]" not in (tmp_path / "wiki" / "index.md").read_text(encoding="utf-8")
    person_text = person_path.read_text(encoding="utf-8").lower()
    assert "research vault" not in person_text
    assert "proof-layer" not in person_text
    assert "family tree view" not in person_text
    assert summary["manifest"]
    assert lint_genealogy_wiki(tmp_path) == []


def test_promote_staged_parent_candidate_updates_tree(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    staged_packets = tmp_path / "research" / "_staging" / "source-packets"
    staged_claims = tmp_path / "research" / "_staging" / "claims"
    staged_relationships = tmp_path / "research" / "_staging" / "relationships"
    staged_packets.mkdir(parents=True, exist_ok=True)
    staged_claims.mkdir(parents=True, exist_ok=True)
    staged_relationships.mkdir(parents=True, exist_ok=True)
    (staged_packets / "SP-STAGE-Parentage.md").write_text(
        """---
type: source_packet
status: draft
source_id: SP-STAGE-PARENTAGE
source_kind: birth_register
raw_file: raw/sources/parentage.png
created: 2026-05-15
---

# Source Packet: Parentage

## Literal Transcription

Child: Child Person. Father: Parent Person.

## Translation

Not needed.

## Interpretation

The entry supports parentage.

## Uncertain Or Illegible

None.
""",
        encoding="utf-8",
    )
    (staged_claims / "CL-STAGE-Child-Father.md").write_text(
        """---
type: claim
status: draft
claim_type: parentage
confidence: 8.5
subject: Child Person
predicate: recorded_father
object: Parent Person
source: raw/converted/parentage.codex.md
source_packet: research/_staging/source-packets/SP-STAGE-Parentage.md
promotion_recommendation: promote
---

# Atomic Claim: Child Father

## Claim

The register names Parent Person as father of Child Person.

## Status

Draft.

## Confidence

8.5/10.

## Source Reliability

- Reliability class: original.

## Conversion Confidence

- Reading confidence: high.

## Literal Source Support

```text
Father: Parent Person
```

## Translation

Not needed.

## Interpretation

This supports a parent-child relationship.

## Uncertainty

No uncertainty.

## Supports

## Conflicts With
""",
        encoding="utf-8",
    )
    (staged_relationships / "REL-STAGE-Child-Parent.md").write_text(
        """---
type: relationship_candidate
status: draft
relationship_type: recorded_parent_child
confidence: 8.5
child: Child Person
parents: [Parent Person]
source_packet: research/_staging/source-packets/SP-STAGE-Parentage.md
promotion_recommendation: promote
---

# Relationship Candidate: Child Parent

## Candidate Relationship

The entry records Child Person as child of Parent Person.

## Literal Support

Father: Parent Person.

## Interpretation

The source supports probable parentage.

## Uncertainty

No uncertainty.
""",
        encoding="utf-8",
    )

    promote_staged_drafts(tmp_path)

    relationship_path = tmp_path / "research" / "relationships" / "rel-stage-child-parent-parent-person-parent.md"
    assert relationship_path.exists()
    relationship_text = relationship_path.read_text(encoding="utf-8")
    assert "relationship_type: probable_parent" in relationship_text
    assert "person_a: [[people/parent-person]]" in relationship_text
    assert "person_b: [[people/child-person]]" in relationship_text
    assert "[[claims/cl-stage-child-father]]" in relationship_text
    tree_text = (tmp_path / "wiki" / "Family Tree.md").read_text(encoding="utf-8")
    assert "Parent Person" in tree_text
    assert "probable parent of" in tree_text
    assert "draft" not in tree_text
    assert lint_genealogy_wiki(tmp_path) == []


def test_source_packet_preserves_transcription_translation_interpretation_sections(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    raw_file = tmp_path / "raw" / "converted" / "record.md"
    raw_file.write_text("# Record\n", encoding="utf-8")

    packet = create_source_packet(tmp_path, raw_file, "SP001", "Geneva Record", "archive_pdf")
    packet_text = packet.read_text(encoding="utf-8")

    assert "## Literal Transcription" in packet_text
    assert "## Translation" in packet_text
    assert "## Interpretation" in packet_text
    assert "## Uncertain Or Illegible" in packet_text


def test_material_packet_is_document_agnostic_and_stages_source(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    source_file = tmp_path / "downloaded-record.bin"
    source_file.write_bytes(b"historical source bytes")

    packet = create_material_packet(
        tmp_path,
        source_file,
        "SP900",
        "Any Source Material",
        source_kind="mixed_source",
        features=["handwriting", "table/grid", "marginalia"],
    )
    packet_text = packet.read_text(encoding="utf-8")

    assert (tmp_path / "raw" / "sources" / "sp900-any-source-material" / "downloaded-record.bin").exists()
    assert (tmp_path / "research" / "sources" / "sp900-any-source-material.md").exists()
    assert "## Verbatim Extraction Contract" in packet_text
    assert "## Dynamic Material Profile" in packet_text
    assert "## Printed Header And Label Inventory" in packet_text
    assert "## Layout Inventory" in packet_text
    assert "## Reading Order" in packet_text
    assert "## Literal Transcription" in packet_text
    assert "## Structured Transcription Tables" in packet_text
    assert "## Translation" in packet_text
    assert "## Interpretation" in packet_text
    assert "## Uncertain Or Illegible" in packet_text
    assert "## Relationship Evidence Candidates" in packet_text
    assert "## Conflict Candidates" in packet_text
    assert "## Research Tasks Suggested" in packet_text
    assert "## Completeness Audit" in packet_text
    assert "Do not summarize, shorten, modernize, or paraphrase" in packet_text
    assert "Missing, shortened, or uncertain items" in packet_text
    assert "handwriting" in packet_text
    assert "table/grid" in packet_text
    assert "source-type agnostic" in packet_text
    assert "1930" not in packet_text
    assert lint_genealogy_wiki(tmp_path) == []


def test_codex_conversion_job_prepares_image_work_order_and_assembles(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    image = tmp_path / "source-page.jpg"
    Image.new("RGB", (20, 10), "white").save(image)

    manifest = create_codex_conversion_job(
        tmp_path,
        image,
        job_id="CJ001",
        title="Codex Source",
    )
    manifest_text = manifest.read_text(encoding="utf-8")
    assert "codex-thread-vision" in manifest_text
    assert "source_sha256" in manifest_text
    assert "extracted_images_dir" in manifest_text
    assert "max_pages_per_work_order" in manifest_text
    assert (manifest.parent / "page-images" / "page-0001.jpg").exists()
    assert (manifest.parent / "extracted-images" / "page-0001").exists()
    work_order = next_codex_conversion_work_order(tmp_path, manifest)
    assert work_order is not None
    assert "View the source image" in work_order.read_text(encoding="utf-8")
    assert "Extracted image output folder" in work_order.read_text(encoding="utf-8")

    page_output = manifest.parent / "page-markdown" / "page-0001.md"
    page_output.write_text(complete_page_markdown(), encoding="utf-8")
    assert next_codex_conversion_work_order(tmp_path, manifest) is None

    assembled = assemble_codex_conversion_job(tmp_path, manifest)
    assembled_text = assembled.read_text(encoding="utf-8")
    assert "Converted by Codex." in assembled_text
    assert "Source SHA-256" in assembled_text
    assert lint_genealogy_wiki(tmp_path) == []


def test_source_prep_page_image_regenerates_from_raw_source(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    doc = fitz.open()
    for page_number in range(1, 3):
        page = doc.new_page(width=72, height=72)
        page.insert_text((8, 36), f"Page {page_number}")
    doc.save(source)

    manifest_path = create_codex_conversion_job(
        tmp_path,
        source,
        job_id="CJ002",
        title="Regenerate Page Image",
        page_range="2",
    )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    page = manifest["pages"][0]
    page_image = tmp_path / page["image_path"]
    staged_source = tmp_path / manifest["local_staged_source_file"]
    page_image.unlink()
    staged_source.unlink()

    batch = {
        "job_manifest": manifest_path.relative_to(tmp_path).as_posix(),
        "first_page": 2,
        "pages": [
            {
                "page": 2,
                "page_image": page["image_path"],
            }
        ],
    }

    regenerated = ensure_source_prep_page_image(tmp_path, batch)

    assert regenerated == page_image
    assert page_image.exists()
    updated = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert updated["pages"][0]["image_path"] == page["image_path"]
    assert updated["pages"][0]["image_bytes"] == page_image.stat().st_size


def test_prepare_raw_sources_queues_agent_conversion_jobs(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "source-page.jpg"
    Image.new("RGB", (20, 10), "white").save(source)

    results = prepare_raw_sources(tmp_path)

    assert len(results) == 1
    assert results[0].status == "queued_for_agent_conversion"
    assert results[0].converted_file == ""
    assert (tmp_path / "raw" / "source-prep-manifest.json").exists()
    jobs = list((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    assert len(jobs) == 1
    assert next_codex_conversion_work_order(tmp_path, jobs[0]) is not None


def test_source_prep_index_registers_cloud_only_r2_sources(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    (tmp_path / "raw" / "r2-raw-sources.json").write_text(
        json.dumps(
            {
                "version": 1,
                "files": [
                    {
                        "path": "raw/sources/cloud-only.pdf",
                        "key": "archive/raw/sources/cloud-only.pdf",
                        "bytes": 42,
                        "sha256": "abc123",
                        "media_type": "application/pdf",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    write_source_prep_index(tmp_path)

    manifest = json.loads((tmp_path / "raw" / "source-prep-manifest.json").read_text(encoding="utf-8"))
    assert manifest["sources"][0]["raw_path"] == "raw/sources/cloud-only.pdf"
    assert manifest["sources"][0]["status"] == "cloud_registered"
    assert manifest["sources"][0]["local_cache"] == "missing"
    assert manifest["sources"][0]["media_type"] == "pdf"
    assert manifest["sources"][0]["cloud"]["key"] == "archive/raw/sources/cloud-only.pdf"


def test_r2_source_intake_monitor_writes_remote_manifest_and_registers_sources(monkeypatch, tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    (tmp_path / "raw" / "r2-raw-sources.json").write_text(
        json.dumps(
            {
                "version": 1,
                "files": [
                    {
                        "path": "raw/sources/existing.pdf",
                        "key": "raw/sources/existing.pdf",
                        "bytes": 1,
                        "sha256": "old-sha",
                        "media_type": "application/pdf",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("R2_BUCKET", "genealogy")
    monkeypatch.setenv("R2_ACCESS_KEY_ID", "test")
    monkeypatch.setenv("R2_SECRET_ACCESS_KEY", "test")

    def fake_remote_manifest(root, config, limit=None):
        assert limit == 10
        return {
            "version": 1,
            "created": "2026-05-16T00:00:00+00:00",
            "purpose": "Cloud object inventory for immutable raw genealogy source originals.",
            "storage": {
                "provider": "cloudflare-r2",
                "account_id": config.account_id,
                "endpoint_url": config.endpoint_url,
                "bucket": config.bucket,
                "prefix": config.prefix,
            },
            "manifest_path": "raw/r2-raw-sources.json",
            "raw_source_root": "raw/sources",
            "source": "remote-r2-list",
            "files": [
                {
                    "path": "raw/sources/cloud-new.jpg",
                    "key": "raw/sources/cloud-new.jpg",
                    "bytes": 42,
                    "sha256": "new-sha",
                    "media_type": "image/jpeg",
                },
                {
                    "path": "raw/sources/existing.pdf",
                    "key": "raw/sources/existing.pdf",
                    "bytes": 2,
                    "sha256": "new-sha-existing",
                    "media_type": "application/pdf",
                },
            ],
        }

    monkeypatch.setattr(genealogy_wiki, "build_raw_cloud_manifest_from_remote", fake_remote_manifest)

    summary = monitor_r2_source_intake(tmp_path, limit=10)

    assert summary["remote_file_count"] == 2
    assert summary["new_file_count"] == 1
    assert summary["changed_file_count"] == 1
    assert summary["removed_file_count"] == 0
    assert (tmp_path / "research" / "_automation" / "r2-source-intake-state.json").exists()
    r2_manifest = json.loads((tmp_path / "raw" / "r2-raw-sources.json").read_text(encoding="utf-8"))
    assert [item["path"] for item in r2_manifest["files"]] == [
        "raw/sources/cloud-new.jpg",
        "raw/sources/existing.pdf",
    ]
    source_manifest = json.loads((tmp_path / "raw" / "source-prep-manifest.json").read_text(encoding="utf-8"))
    sources_by_path = {source["raw_path"]: source for source in source_manifest["sources"]}
    assert sources_by_path["raw/sources/cloud-new.jpg"]["status"] == "cloud_registered"
    assert sources_by_path["raw/sources/cloud-new.jpg"]["media_type"] == "image"
    assert sources_by_path["raw/sources/existing.pdf"]["cloud"]["sha256"] == "new-sha-existing"


def test_prepare_raw_sources_splits_large_pdfs_into_agent_page_ranges(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    doc = fitz.open()
    for page_number in range(1, 6):
        page = doc.new_page(width=72, height=72)
        page.insert_text((8, 36), f"Page {page_number}")
    doc.save(source)

    results = prepare_raw_sources(tmp_path, pages_per_job=2)

    assert len(results) == 1
    assert results[0].status == "queued_for_agent_conversion"
    assert len(results[0].conversion_jobs) == 3
    manifests = sorted((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    assert len(manifests) == 3
    page_ranges = [json.loads(path.read_text(encoding="utf-8"))["chunking"]["page_range"] for path in manifests]
    assert page_ranges == ["1-2", "3-4", "5"]
    page_counts = [len(json.loads(path.read_text(encoding="utf-8"))["pages"]) for path in manifests]
    assert page_counts == [2, 2, 1]

    index = json.loads((tmp_path / "raw" / "source-prep-manifest.json").read_text(encoding="utf-8"))
    assert index["sources"][0]["status"] == "queued_for_agent_conversion"
    assert len(index["sources"][0]["conversion_jobs"]) == 3


def test_prepare_raw_sources_adds_requested_pdf_page_range_when_source_has_existing_jobs(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    doc = fitz.open()
    for page_number in range(1, 6):
        page = doc.new_page(width=72, height=72)
        page.insert_text((8, 36), f"Page {page_number}")
    doc.save(source)

    first = prepare_raw_sources(tmp_path, page_range="1-2", pages_per_job=25)
    second = prepare_raw_sources(tmp_path, page_range="4-5", pages_per_job=25)

    assert len(first[0].conversion_jobs) == 1
    assert len(second[0].conversion_jobs) == 2
    manifests = sorted((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    page_ranges = sorted(json.loads(path.read_text(encoding="utf-8"))["chunking"]["page_range"] for path in manifests)
    assert page_ranges == ["1-2", "4-5"]


def test_source_prep_tasks_collapse_overlapping_pdf_jobs_to_one_task_per_source_page(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    doc = fitz.open()
    for page_number in range(1, 4):
        page = doc.new_page(width=72, height=72)
        page.insert_text((8, 36), f"Page {page_number}")
    doc.save(source)

    create_codex_conversion_job(
        tmp_path,
        source,
        job_id="ARCHIVE-P001-002",
        title="Archive pages 1-2",
        page_range="1-2",
    )
    create_codex_conversion_job(
        tmp_path,
        source,
        job_id="ARCHIVE-P001-003",
        title="Archive pages 1-3",
        page_range="1-3",
    )

    tasks = genealogy_wiki.build_source_prep_agent_tasks(tmp_path)

    assert len(tasks) == 3
    assert sorted(int(task["source_page"]) for task in tasks) == [1, 2, 3]
    assert len({(task["source_sha256"], task["source_page"]) for task in tasks}) == 3


def test_prepare_raw_sources_adds_next_missing_pdf_pages_with_limit(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    doc = fitz.open()
    for page_number in range(1, 7):
        page = doc.new_page(width=72, height=72)
        page.insert_text((8, 36), f"Page {page_number}")
    doc.save(source)

    prepare_raw_sources(tmp_path, page_range="1-2", pages_per_job=25)
    result = prepare_raw_sources(tmp_path, pages_per_job=2, new_pages_limit=3)[0]

    manifests = sorted((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    page_ranges = sorted(json.loads(path.read_text(encoding="utf-8"))["chunking"]["page_range"] for path in manifests)

    assert len(result.conversion_jobs) == 3
    assert page_ranges == ["1-2", "3-4", "5"]


def test_prepare_raw_sources_limits_new_pdf_initial_jobs(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    doc = fitz.open()
    for page_number in range(1, 7):
        page = doc.new_page(width=72, height=72)
        page.insert_text((8, 36), f"Page {page_number}")
    doc.save(source)

    result = prepare_raw_sources(tmp_path, pages_per_job=2, new_pages_limit=3)[0]

    manifests = sorted((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    page_ranges = sorted(json.loads(path.read_text(encoding="utf-8"))["chunking"]["page_range"] for path in manifests)

    assert len(result.conversion_jobs) == 2
    assert page_ranges == ["1-2", "3"]


def test_write_agent_queues_creates_conversion_qa_and_extraction_tasks(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "source-page.jpg"
    Image.new("RGB", (20, 10), "white").save(source)
    prepare_raw_sources(tmp_path)
    manifest = next((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))

    written = write_agent_queues(tmp_path)
    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    assert source_queue["task_count"] == 1
    assert source_queue["tasks"][0]["role"] == "source_converter"
    assert source_queue["tasks"][0]["status"] == "todo"
    assert (tmp_path / source_queue["tasks"][0]["prompt_path"]).exists()

    page_output = manifest.parent / "page-markdown" / "page-0001.md"
    page_output.write_text(complete_page_markdown(), encoding="utf-8")
    assembled = assemble_codex_conversion_job(tmp_path, manifest)
    chunk_converted_markdown(tmp_path, assembled)

    written = write_agent_queues(tmp_path)
    assert len(written) == 3
    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    assert source_queue["tasks"][0]["status"] == "done"
    qa_queue = json.loads((tmp_path / "research" / "_agent-queues" / "conversion-qa.json").read_text(encoding="utf-8"))
    extraction_queue = json.loads(
        (tmp_path / "research" / "_agent-queues" / "evidence-extraction.json").read_text(encoding="utf-8")
    )
    assert qa_queue["task_count"] == 1
    assert qa_queue["tasks"][0]["role"] == "conversion_qa_reviewer"
    assert extraction_queue["task_count"] >= 1
    assert extraction_queue["tasks"][0]["role"] == "evidence_extractor"
    assert extraction_queue["tasks"][0]["status"] == "blocked_pending_conversion_qa"
    assert extraction_queue["tasks"][0]["block_reason"] == "pending_conversion_qa"
    prompt_text = (tmp_path / extraction_queue["tasks"][0]["prompt_path"]).read_text(encoding="utf-8")
    assert "Conversion QA Gate" in prompt_text
    assert "Do not extract claims" in prompt_text

    update_agent_task_state(tmp_path, qa_queue["tasks"][0]["task_id"], "done", agent="qa-1")
    write_agent_queues(tmp_path)
    extraction_queue = json.loads(
        (tmp_path / "research" / "_agent-queues" / "evidence-extraction.json").read_text(encoding="utf-8")
    )
    assert extraction_queue["tasks"][0]["status"] == "todo"
    assert "block_reason" not in extraction_queue["tasks"][0]


def test_agent_task_state_claims_and_releases_queue_tasks(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "source-page.jpg"
    Image.new("RGB", (20, 10), "white").save(source)
    prepare_raw_sources(tmp_path)

    write_agent_queues(tmp_path)
    queue_path = tmp_path / "research" / "_agent-queues" / "source-prep.json"
    source_queue = json.loads(queue_path.read_text(encoding="utf-8"))
    task_id = source_queue["tasks"][0]["task_id"]

    update_agent_task_state(tmp_path, task_id, "claimed", agent="worker-1", note="reading page image")
    write_agent_queues(tmp_path)
    source_queue = json.loads(queue_path.read_text(encoding="utf-8"))
    assert source_queue["tasks"][0]["status"] == "claimed"
    assert source_queue["tasks"][0]["agent"] == "worker-1"
    assert source_queue["tasks"][0]["note"] == "reading page image"

    update_agent_task_state(tmp_path, task_id, "released", agent="worker-1")
    write_agent_queues(tmp_path)
    source_queue = json.loads(queue_path.read_text(encoding="utf-8"))
    assert source_queue["tasks"][0]["status"] == "todo"
    assert source_queue["tasks"][0]["task_state_status"] == "released"
    assert "agent" not in source_queue["tasks"][0]
    assert source_queue["tasks"][0]["released_by"] == "worker-1"


def test_agent_task_state_updates_multiple_tasks_in_one_write(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    state_path = update_agent_task_states(
        tmp_path,
        ["source-prep:job:p0001", "source-prep:job:p0002"],
        "claimed",
        agent="worker-1",
        note="batch claim",
    )
    payload = json.loads(state_path.read_text(encoding="utf-8"))

    assert payload["tasks"]["source-prep:job:p0001"]["status"] == "claimed"
    assert payload["tasks"]["source-prep:job:p0002"]["status"] == "claimed"
    assert payload["tasks"]["source-prep:job:p0001"]["agent"] == "worker-1"
    assert payload["tasks"]["source-prep:job:p0002"]["note"] == "batch claim"


def test_write_agent_queue_removes_stale_prompt_packets(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    queue_dir = tmp_path / "research" / "_agent-queues"
    stale_dir = queue_dir / "prompts" / "demo"
    stale_dir.mkdir(parents=True)
    stale_prompt = stale_dir / "old-task.md"
    stale_prompt.write_text("stale prompt", encoding="utf-8")

    queue_path = genealogy_wiki.write_agent_queue(
        tmp_path,
        queue_dir,
        "demo",
        [
            {
                "task_id": "demo:new-task",
                "status": "todo",
                "prompt": "fresh prompt",
            }
        ],
    )

    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    prompt_path = tmp_path / queue["tasks"][0]["prompt_path"]
    assert not stale_prompt.exists()
    assert prompt_path.exists()
    assert prompt_path.read_text(encoding="utf-8") == "fresh prompt"


def test_source_prep_batches_emit_one_page_per_worker(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    doc = fitz.open()
    for page_number in range(1, 6):
        page = doc.new_page(width=72, height=72)
        page.insert_text((8, 36), f"Page {page_number}")
    doc.save(source)
    prepare_raw_sources(tmp_path, pages_per_job=5)
    write_agent_queues(tmp_path)

    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    page_three_task = next(task["task_id"] for task in source_queue["tasks"] if task["page"] == 3)
    update_agent_task_state(tmp_path, page_three_task, "claimed", agent="worker-1")

    batch_path = write_source_prep_batches(tmp_path, max_pages=3, limit=10)
    batch_queue = json.loads(batch_path.read_text(encoding="utf-8"))
    batches = batch_queue["tasks"]

    assert [batch["page_count"] for batch in batches] == [1, 1, 1, 1]
    assert batches[0]["first_page"] == 1
    assert batches[0]["last_page"] == 1
    assert batches[1]["first_page"] == 2
    assert batches[1]["last_page"] == 2
    assert batches[2]["first_page"] == 4
    assert batches[2]["last_page"] == 4
    assert page_three_task not in batches[0]["task_ids"]
    prompt_text = (tmp_path / batches[0]["prompt_path"]).read_text(encoding="utf-8")
    assert "not a quality shortcut" in prompt_text
    assert "agent-task claim" in prompt_text


def test_source_relevance_expensive_document_mark_expands_to_page_hints(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    doc = fitz.open()
    for page_number in range(1, 4):
        page = doc.new_page(width=72, height=72)
        page.insert_text((8, 36), f"Page {page_number}")
    doc.save(source)

    manifest_path = create_codex_conversion_job(
        tmp_path,
        source,
        job_id="CJ003",
        title="Important Archive Section",
        page_range="1-3",
    )

    path, summary = mark_source_relevance_feedback(
        tmp_path,
        job_manifest=manifest_path.relative_to(tmp_path).as_posix(),
        page=0,
        relevance="high",
        treatment="pro_with_crops",
        reason="Research agent identified this section as relevant.",
        agent="researcher",
    )

    payload = json.loads(path.read_text(encoding="utf-8"))
    assert summary["expanded"] is True
    assert summary["pages"] == [1, 2, 3]
    assert [hint["page"] for hint in payload["hints"]] == [1, 2, 3]
    assert {hint["requested_treatment"] for hint in payload["hints"]} == {"pro_with_crops"}


def test_source_relevance_page_hint_matches_only_that_page() -> None:
    hint = {
        "source": "raw/sources/archive.pdf",
        "page": 20,
    }

    assert source_relevance_hint_matches_task(hint, {"source": "raw/sources/archive.pdf", "page": 20}) is True
    assert source_relevance_hint_matches_task(hint, {"source": "raw/sources/archive.pdf", "page": 21}) is False
    assert source_relevance_hint_matches_task(hint, {"source": "raw/sources/archive.pdf"}) is False


def test_source_relevance_infers_page_from_page_scoped_task_id(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    path, hint = mark_source_relevance_feedback(
        tmp_path,
        task_id="source-prep:archive:p0020",
        relevance="critical",
        treatment="pro",
        reason="Research agent wants an evidence-grade reread.",
    )

    payload = json.loads(path.read_text(encoding="utf-8"))
    assert hint["page"] == 20
    assert payload["hints"][0]["page"] == 20


def test_source_relevance_rejects_unexpanded_expensive_source_scope(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    with pytest.raises(ValueError, match="page-level orders"):
        mark_source_relevance_feedback(
            tmp_path,
            source="raw/sources/not-prepared.pdf",
            relevance="high",
            treatment="pro",
        )


def test_source_prep_fastlane_completes_born_digital_pdf_pages(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "minutes.pdf"
    doc = fitz.open()
    repeated_text = (
        "Dario Pulgar Smith attended the committee meeting in Geneva on 12 March 1934. "
        "The minutes list delegates, offices, places, correspondence, and archival references. "
    )
    for page_number in range(1, 3):
        page = doc.new_page(width=360, height=500)
        page.insert_textbox((36, 36, 324, 460), f"Page {page_number}\n\n" + repeated_text * 4, fontsize=11)
    doc.save(source)

    prepare_raw_sources(tmp_path, pages_per_job=2)
    write_agent_queues(tmp_path)

    summary = source_prep_fastlane_run(tmp_path, limit=10, scan_limit=10, agent="fast-test")

    assert summary["converted"] == 2
    queue_path = tmp_path / "research" / "_agent-queues" / "source-prep.json"
    write_agent_queues(tmp_path)
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    assert queue["status_counts"]["done"] == 2
    task_state = json.loads((tmp_path / "research" / "_agent-queues" / "task-state.json").read_text(encoding="utf-8"))
    assert {state["status"] for state in task_state["tasks"].values()} == {"done"}
    page_output = next((tmp_path / "raw" / "codex-conversion-jobs").glob("*/page-markdown/page-0001.md"))
    page_text = page_output.read_text(encoding="utf-8")
    assert "deterministic PDF-native fast lane" in page_text
    assert "## Completeness Audit" in page_text
    assert (page_output.parent.parent / "extracted-images" / "page-0001").exists()


def test_source_prep_fastlane_skips_full_page_scan_pdf(tmp_path) -> None:
    fitz = pytest.importorskip("fitz")
    Image = pytest.importorskip("PIL.Image")
    init_genealogy_wiki(tmp_path)
    scan = tmp_path / "scan.jpg"
    Image.new("RGB", (300, 420), "white").save(scan)
    source = tmp_path / "raw" / "sources" / "scan.pdf"
    doc = fitz.open()
    page = doc.new_page(width=300, height=420)
    page.insert_image(page.rect, filename=scan)
    doc.save(source)

    prepare_raw_sources(tmp_path)
    write_agent_queues(tmp_path)

    summary = source_prep_fastlane_run(tmp_path, limit=10, scan_limit=10, agent="fast-test")

    assert summary["converted"] == 0
    assert summary["skipped"]["full_page_image_scan"] == 1
    write_agent_queues(tmp_path)
    queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    assert queue["status_counts"]["todo"] == 1


def test_source_prep_review_ignores_empty_reread_metadata(tmp_path) -> None:
    page_output = tmp_path / "page.md"
    page_output.write_text(
        complete_gemini_page_markdown("Transmettons à M. Ratzenberger du Département politique Fédéral.")
        .replace("Page converted from the prepared page image.", "Page converted from the prepared page image.\n- Technical reread clues: none"),
        encoding="utf-8",
    )

    review = review_source_prep_page_output(page_output)

    assert review["status"] == "done"
    assert "explicit_reread_needed" not in review["quality_flags"]
    assert "encoding_mojibake" not in review["quality_flags"]


def test_docling_discovery_writes_rough_output_and_removes_page_from_batches(tmp_path, monkeypatch) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "printed-minutes.pdf"
    doc = fitz.open()
    page = doc.new_page(width=360, height=500)
    text = (
        "Dario Pulgar Smith attended the meeting in Geneva. "
        "The printed minutes list offices, dates, correspondents, places, and archive references. "
    )
    page.insert_textbox((36, 36, 324, 460), text * 4, fontsize=11)
    doc.save(source)

    prepare_raw_sources(tmp_path)
    monkeypatch.setattr(
        genealogy_wiki,
        "convert_source_with_docling",
        lambda input_path: "# Printed Minutes\n\n" + text * 4,
    )

    summary = genealogy_wiki.source_prep_docling_discovery_run(tmp_path, limit=1, scan_limit=10)

    assert summary["accepted"] == 1
    discovery_path = next((tmp_path / "raw" / "discovery" / "docling").glob("*/page-0001.md"))
    discovery_text = discovery_path.read_text(encoding="utf-8")
    assert "not evidence-grade transcription" in discovery_text
    assert "Printed Minutes" in discovery_text
    manifest_path = next((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    page_output = tmp_path / manifest["pages"][0]["output_path"]
    assert not page_output.exists()

    write_agent_queues(tmp_path)
    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    assert source_queue["status_counts"]["rough_discovery"] == 1
    batch_path = write_source_prep_batches(tmp_path, limit=10)
    batch_queue = json.loads(batch_path.read_text(encoding="utf-8"))
    assert batch_queue["tasks"] == []


def test_docling_discovery_unusable_page_falls_through_to_gemini(tmp_path, monkeypatch) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "bad-scan.pdf"
    doc = fitz.open()
    page = doc.new_page(width=360, height=500)
    page.insert_text((36, 100), "x")
    doc.save(source)

    prepare_raw_sources(tmp_path)
    monkeypatch.setattr(genealogy_wiki, "convert_source_with_docling", lambda input_path: "???")

    discovery = genealogy_wiki.source_prep_docling_discovery_run(tmp_path, limit=1, scan_limit=10)

    assert discovery["unusable"] == 1
    batch_path = write_source_prep_batches(tmp_path, limit=10)
    batch_queue = json.loads(batch_path.read_text(encoding="utf-8"))
    assert len(batch_queue["tasks"]) == 1

    def fake_gemini(**kwargs):
        return {
            "text": complete_gemini_page_markdown("DARIO PULGAR SMITH"),
            "finish_reason": "STOP",
            "usage": {"promptTokenCount": 5, "candidatesTokenCount": 10, "totalTokenCount": 15},
        }

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fake_gemini)

    gemini = genealogy_wiki.source_prep_gemini_run(tmp_path, limit=1, api_key="test-key")

    assert gemini["completed"] == 1
    task_state = json.loads((tmp_path / "research" / "_agent-queues" / "task-state.json").read_text(encoding="utf-8"))
    assert {state["status"] for state in task_state["tasks"].values()} == {"done"}


def test_relevance_feedback_overrides_rough_docling_discovery(tmp_path, monkeypatch) -> None:
    fitz = pytest.importorskip("fitz")
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "browse-first.pdf"
    doc = fitz.open()
    page = doc.new_page(width=360, height=500)
    text = "This printed page has enough words for rough discovery and later page-level upgrade. "
    page.insert_textbox((36, 36, 324, 460), text * 5, fontsize=11)
    doc.save(source)

    prepare_raw_sources(tmp_path)
    write_agent_queues(tmp_path)
    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    task_id = source_queue["tasks"][0]["task_id"]
    monkeypatch.setattr(genealogy_wiki, "convert_source_with_docling", lambda input_path: text * 5)

    genealogy_wiki.source_prep_docling_discovery_run(tmp_path, limit=1, scan_limit=10)
    mark_source_relevance_feedback(
        tmp_path,
        task_id=task_id,
        relevance="high",
        treatment="pro",
        reason="Research agent found this exact page relevant.",
        agent="researcher",
    )

    batch_path = write_source_prep_batches(tmp_path, limit=10)
    batch_queue = json.loads(batch_path.read_text(encoding="utf-8"))

    assert len(batch_queue["tasks"]) == 1
    assert batch_queue["tasks"][0]["pages"][0]["requested_treatment"] == "pro"
    gemini_plan = genealogy_wiki.source_prep_gemini_run(tmp_path, limit=1, dry_run=True)
    assert gemini_plan["processed"] == 1
    assert gemini_plan["tasks"][0]["route"]["tier"] == "pro_with_crops"


def test_research_analyzer_marks_family_relevant_chunk_pages_for_upgrade(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    person_dir = tmp_path / "wiki" / "people"
    person_dir.mkdir(parents=True, exist_ok=True)
    (person_dir / "pulgar-dario.md").write_text(
        """---
type: person
status: stub
---

# Dario Pulgar Smith
""",
        encoding="utf-8",
    )
    converted = tmp_path / "raw" / "converted" / "dario-record.codex.md"
    converted.write_text(
        complete_gemini_page_markdown(
            "Dario Pulgar Smith appears as son of Maria Smith and signed the register."
        )
        + """
## Extracted Genealogy Leads

- **Dario Pulgar Smith**

## Visual Region Manifest

```json
{"visual_regions": [{"kind": "signature", "caption_literal": "Dario Pulgar Smith"}]}
```
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)

    summary = research_analyzer_run(tmp_path, limit=3)

    assert summary["upgrade_requests_written"] == 1
    feedback = json.loads((tmp_path / "research" / "_agent-queues" / "source-relevance-feedback.json").read_text())
    hint = feedback["hints"][0]
    assert hint["converted_file"] == "raw/converted/dario-record.codex.md"
    assert hint["page"] == 1
    assert hint["relevance"] == "critical"
    assert hint["requested_treatment"] == "pro_with_crops"
    assert "Dario Pulgar Smith" in hint["matched_terms"]
    index = json.loads((tmp_path / "research" / "_indexes" / "research-analyzer.json").read_text())
    assert index["pages"][0]["recommended_action"] == "request_page_upgrade"

    second_summary = research_analyzer_run(tmp_path, limit=3)

    assert second_summary["upgrade_requests_written"] == 0
    assert second_summary["upgrade_requests_existing"] == 1
    feedback_after_second_run = json.loads(
        (tmp_path / "research" / "_agent-queues" / "source-relevance-feedback.json").read_text()
    )
    assert len(feedback_after_second_run["hints"]) == 1


def test_research_analyzer_records_generic_genealogy_leads_without_upgrade_request(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    converted = tmp_path / "raw" / "converted" / "generic-record.codex.md"
    converted.write_text(
        complete_gemini_page_markdown("M. Werner appears in a professional list.")
        + """
## Extracted Genealogy Leads

- **M. Werner**
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)

    summary = research_analyzer_run(tmp_path, limit=3)

    assert summary["upgrade_candidates"] == 0
    assert summary["upgrade_requests_written"] == 0
    index = json.loads((tmp_path / "research" / "_indexes" / "research-analyzer.json").read_text())
    assert index["pages"][0]["recommended_action"] == "record_signal"
    assert not (tmp_path / "research" / "_agent-queues" / "source-relevance-feedback.json").exists()
    queue = json.loads((tmp_path / "research" / "_agent-queues" / "research-questions.json").read_text())
    assert queue["task_count"] == 1
    assert queue["tasks"][0]["status"] == "todo"
    assert (tmp_path / queue["tasks"][0]["question_path"]).exists()
    assert (tmp_path / queue["tasks"][0]["prompt_path"]).exists()
    assert "prompt" not in queue["tasks"][0]
    research_index = (tmp_path / "research" / "index.md").read_text(encoding="utf-8")
    assert f"[[questions/{Path(queue['tasks'][0]['question_path']).stem}]]" in research_index


def test_research_analyzer_blocks_question_tasks_for_qc_held_pages(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    converted = tmp_path / "raw" / "converted" / "held-record.codex.md"
    converted.write_text(
        complete_gemini_page_markdown("M. Werner appears in a professional list.")
        + """
## Extracted Genealogy Leads

- **M. Werner**
""",
        encoding="utf-8",
    )
    chunk_manifest = chunk_converted_markdown(tmp_path, converted)
    qc_dir = tmp_path / "research" / "_conversion-review"
    qc_dir.mkdir(parents=True, exist_ok=True)
    qc_dir.joinpath("qc-pages.json").write_text(
        json.dumps(
            {
                "pages": [
                    {
                        "page": 1,
                        "recommended_action": "reread-page",
                        "conversion_confidence": "low",
                        "family_relevance": "medium",
                        "quality_flags": ["possible_name_drift"],
                        "matched_terms": ["Werner"],
                        "converted_file": converted.relative_to(tmp_path).as_posix(),
                        "chunk_manifest": chunk_manifest.relative_to(tmp_path).as_posix(),
                    }
                ]
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    summary = research_analyzer_run(tmp_path, limit=3)

    assert summary["research_questions_written"] == 1
    queue = json.loads((tmp_path / "research" / "_agent-queues" / "research-questions.json").read_text())
    task = queue["tasks"][0]
    assert queue["task_count"] == 1
    assert task["status"] == "blocked_needs_reread"
    assert task["block_reason"] == "post_conversion_qc_hold"
    assert task["blocked_pages"] == [1]
    assert task["qc_recommended_action"] == "reread-page"
    assert task["qc_quality_flags"] == ["possible_name_drift"]
    prompt_text = (tmp_path / task["prompt_path"]).read_text(encoding="utf-8")
    assert "QC Hold" in prompt_text
    assert "Do not extract claims" in prompt_text


def test_research_analyzer_refreshes_existing_todo_question_pages(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    converted = tmp_path / "raw" / "converted" / "refresh-record.codex.md"
    converted.write_text(
        complete_gemini_page_markdown("M. Werner appears in a professional list.")
        + """
## Extracted Genealogy Leads

- **M. Werner**
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)
    first_summary = research_analyzer_run(tmp_path, limit=3)
    queue = json.loads((tmp_path / "research" / "_agent-queues" / "research-questions.json").read_text())
    question_path = tmp_path / queue["tasks"][0]["question_path"]
    assert first_summary["research_questions_written"] == 1
    assert "M. Werner" in question_path.read_text(encoding="utf-8")

    converted.write_text(
        complete_gemini_page_markdown("M. Huber appears in a professional list.")
        + """
## Extracted Genealogy Leads

- **M. Huber**
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)
    second_summary = research_analyzer_run(tmp_path, limit=3)

    assert second_summary["research_questions_written"] == 0
    assert second_summary["research_questions_existing"] == 1
    assert second_summary["research_questions_refreshed"] == 1
    refreshed_text = question_path.read_text(encoding="utf-8")
    assert "M. Huber" in refreshed_text
    assert "M. Werner" not in refreshed_text


def test_research_analyzer_removes_stale_todo_question_pages(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    converted = tmp_path / "raw" / "converted" / "stale-question.codex.md"
    converted.write_text(
        """# Stale Question

## Conversion Metadata

- Source: `raw/sources/source.pdf`
- Source SHA-256: `abc123`
- Manifest: `raw/codex-conversion-jobs/job/manifest.json`

## Page Metadata
- Page: 1

## Literal Transcription

M. Werner appears in a professional list.

## Extracted Genealogy Leads

- **M. Werner**

## Page Metadata
- Page: 2

## Literal Transcription

M. Huber appears in a professional list.

## Extracted Genealogy Leads

- **M. Huber**
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)
    research_analyzer_run(tmp_path, limit=3, question_limit=10)
    queue = json.loads((tmp_path / "research" / "_agent-queues" / "research-questions.json").read_text())
    stale_task = next(task for task in queue["tasks"] if task["page"] == 2)
    stale_question_path = tmp_path / stale_task["question_path"]
    stale_question_link = f"[[questions/{stale_question_path.stem}]]"
    assert stale_question_path.exists()

    converted.write_text(
        """# Stale Question

## Conversion Metadata

- Source: `raw/sources/source.pdf`
- Source SHA-256: `abc123`
- Manifest: `raw/codex-conversion-jobs/job/manifest.json`

## Page Metadata
- Page: 1

## Literal Transcription

M. Werner appears in a professional list.

## Extracted Genealogy Leads

- **M. Werner**

## Page Metadata
- Page: 2

## Literal Transcription

No genealogy signal on this page.
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)
    research_analyzer_run(tmp_path, limit=3, question_limit=10)

    queue = json.loads((tmp_path / "research" / "_agent-queues" / "research-questions.json").read_text())
    assert [task["page"] for task in queue["tasks"]] == [1]
    assert not stale_question_path.exists()
    research_index = (tmp_path / "research" / "index.md").read_text(encoding="utf-8")
    assert stale_question_link not in research_index


def test_research_analyzer_recovers_original_pages_for_question_queue(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    source.write_bytes(b"%PDF-1.4 placeholder")
    digest = genealogy_wiki.file_sha256(source)
    manifest_path = tmp_path / "raw" / "codex-conversion-jobs" / "archive-pages-4-5" / "manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(
            {
                "job_id": "archive-pages-4-5",
                "source_file": source.relative_to(tmp_path).as_posix(),
                "source_sha256": digest,
                "media_type": "pdf",
                "pages": [{"page": 4, "source_page": 4}, {"page": 5, "source_page": 5}],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    converted = tmp_path / "raw" / "converted" / "archive-pages-4-5.codex.md"
    converted.write_text(
        f"""# Archive Pages 4-5

## Conversion Metadata

- Source: `{source.relative_to(tmp_path).as_posix()}`
- Source SHA-256: `{digest}`
- Manifest: `{manifest_path.relative_to(tmp_path).as_posix()}`

## Page Metadata

- Task id: `source-prep:archive-pages-4-5:p0004`
- **Page number**: 4

## Literal Transcription

M. Werner appears in a professional list.

## Extracted Genealogy Leads

- **M. Werner**

## Page Metadata

- Task id: `source-prep:archive-pages-4-5:p0005`

## Literal Transcription

M. Huber appears in a professional list.

## Extracted Genealogy Leads

- **M. Huber**
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)

    summary = research_analyzer_run(tmp_path, limit=0, question_limit=10)

    assert summary["research_questions_written"] == 2
    index = json.loads((tmp_path / "research" / "_indexes" / "research-analyzer.json").read_text(encoding="utf-8"))
    assert [page["page"] for page in index["pages"]] == [4, 5]
    queue = json.loads((tmp_path / "research" / "_agent-queues" / "research-questions.json").read_text(encoding="utf-8"))
    assert [task["page"] for task in queue["tasks"]] == [4, 5]
    assert all((tmp_path / task["prompt_path"]).exists() for task in queue["tasks"])


def test_cloud_source_prep_heartbeat_runs_research_analyzer(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    converted = tmp_path / "raw" / "converted" / "heartbeat-record.codex.md"
    converted.write_text(
        complete_gemini_page_markdown("M. Werner appears in a professional list.")
        + """
## Extracted Genealogy Leads

- **M. Werner**
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)

    summary = cloud_source_prep_heartbeat(
        tmp_path,
        restore_raw=False,
        upload_assets=False,
        research_analyzer_limit=1,
        research_question_limit=1,
    )

    analyzer_step = next(step for step in summary["steps"] if step["name"] == "research-analyzer")
    assert analyzer_step["status"] == "ran"
    assert summary["queues"]["research_questions"]["path"] == "research/_agent-queues/research-questions.json"
    assert summary["queues"]["research_questions"]["task_count"] == 1
    queue = json.loads((tmp_path / "research" / "_agent-queues" / "research-questions.json").read_text(encoding="utf-8"))
    assert queue["task_count"] == 1
    assert (tmp_path / queue["tasks"][0]["prompt_path"]).exists()


def test_agent_queue_releases_stale_claims(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "source-page.jpg"
    Image.new("RGB", (20, 10), "white").save(source)
    prepare_raw_sources(tmp_path)
    write_agent_queues(tmp_path, stale_minutes=60)
    queue_path = tmp_path / "research" / "_agent-queues" / "source-prep.json"
    source_queue = json.loads(queue_path.read_text(encoding="utf-8"))
    task_id = source_queue["tasks"][0]["task_id"]

    state_path = update_agent_task_state(tmp_path, task_id, "claimed", agent="worker-1")
    state_payload = json.loads(state_path.read_text(encoding="utf-8"))
    state_payload["tasks"][task_id]["claimed_at"] = "2000-01-01T00:00:00Z"
    state_payload["tasks"][task_id]["updated_at"] = "2000-01-01T00:00:00Z"
    state_path.write_text(json.dumps(state_payload, indent=2), encoding="utf-8")

    assert release_stale_agent_tasks(tmp_path, stale_minutes=60) == 1
    write_agent_queues(tmp_path, stale_minutes=60)
    source_queue = json.loads(queue_path.read_text(encoding="utf-8"))
    assert source_queue["tasks"][0]["status"] == "todo"
    assert source_queue["tasks"][0]["task_state_status"] == "released"
    assert "agent" not in source_queue["tasks"][0]
    assert source_queue["tasks"][0]["released_by"] == "worker-1"


def test_source_prep_page_review_cache_is_used_for_unchanged_outputs(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "source-page.jpg"
    Image.new("RGB", (20, 10), "white").save(source)
    prepare_raw_sources(tmp_path)
    manifest = next((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    page_output = manifest.parent / "page-markdown" / "page-0001.md"
    page_output.write_text(complete_page_markdown(), encoding="utf-8")

    write_agent_queues(tmp_path)
    cache_path = source_prep_page_cache_path(tmp_path)
    assert cache_path.exists()
    cache = json.loads(cache_path.read_text(encoding="utf-8"))
    cache_key = page_output.relative_to(tmp_path).as_posix()
    stat = page_output.stat()
    cache["entries"][cache_key] = {
        "mtime_ns": stat.st_mtime_ns,
        "size": stat.st_size,
        "review": {"status": "needs_reread", "quality_flags": ["cached_marker"], "missing_sections": []},
    }
    cache_path.write_text(json.dumps(cache, indent=2), encoding="utf-8")

    write_agent_queues(tmp_path)
    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    assert source_queue["tasks"][0]["status"] == "needs_reread"
    assert source_queue["tasks"][0]["quality_flags"] == ["cached_marker"]


def test_legacy_page_output_is_not_treated_as_done(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "legacy-scan.jpg"
    Image.new("RGB", (20, 10), "white").save(source)
    prepare_raw_sources(tmp_path)
    manifest = next((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    page_output = manifest.parent / "page-markdown" / "page-0001.md"
    page_output.write_text("# Page 1\n\nOCR-ish text exists, but no conversion contract sections.\n", encoding="utf-8")

    write_agent_queues(tmp_path)

    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    task = source_queue["tasks"][0]
    assert task["status"] == "needs_reread"
    assert "missing_conversion_contract_sections" in task["quality_flags"]
    prompt_text = (tmp_path / task["prompt_path"]).read_text(encoding="utf-8")
    assert "Repair Context" in prompt_text
    assert "not trusted by the current source-prep contract" in prompt_text


def test_qc_holds_block_only_affected_extraction_chunks_and_source_status(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "scan.jpg"
    Image.new("RGB", (20, 10), "white").save(source)
    prepare_raw_sources(tmp_path)
    manifest = next((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    page_output = manifest.parent / "page-markdown" / "page-0001.md"
    page_output.write_text(
        """# Page 1

## Literal Transcription

[No visible text transcribed in this batch pass.]
""",
        encoding="utf-8",
    )
    assembled = assemble_codex_conversion_job(tmp_path, manifest)
    chunk_converted_markdown(tmp_path, assembled)
    write_post_conversion_qc(tmp_path)

    write_agent_queues(tmp_path)
    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    assert source_queue["tasks"][0]["status"] == "needs_reread"
    assert source_queue["tasks"][0]["repair_reason"] == "post_conversion_qc_hold"
    extraction_queue = json.loads(
        (tmp_path / "research" / "_agent-queues" / "evidence-extraction.json").read_text(encoding="utf-8")
    )
    task = extraction_queue["tasks"][0]
    assert task["status"] == "blocked_needs_reread"
    assert task["blocked_pages"] == [1]
    prompt_text = (tmp_path / task["prompt_path"]).read_text(encoding="utf-8")
    assert "QC Hold" in prompt_text
    assert "Do not extract claims" in prompt_text

    write_source_usability_report(tmp_path)
    usability = json.loads((tmp_path / "research" / "_indexes" / "source-usability.json").read_text(encoding="utf-8"))
    assert usability["summary"]["status_counts"]["usable_with_page_repairs"] == 1
    assert usability["sources"][0]["qc_hold_count"] == 1
    assert usability["sources"][0]["page_repair_count"] == 1


def test_completed_qc_reread_hold_is_unblocked_when_page_passes_contract(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "scan.jpg"
    Image.new("RGB", (20, 10), "white").save(source)
    prepare_raw_sources(tmp_path)
    manifest = next((tmp_path / "raw" / "codex-conversion-jobs").glob("*/manifest.json"))
    page_output = manifest.parent / "page-markdown" / "page-0001.md"
    page_output.write_text(complete_page_markdown("Dario Pulgar visually reread."), encoding="utf-8")
    assembled = assemble_codex_conversion_job(tmp_path, manifest)
    chunk_manifest = chunk_converted_markdown(tmp_path, assembled)

    qc_dir = tmp_path / "research" / "_conversion-review"
    qc_dir.mkdir(parents=True, exist_ok=True)
    qc_dir.joinpath("qc-pages.json").write_text(
        json.dumps(
            {
                "pages": [
                    {
                        "page": 1,
                        "recommended_action": "reread-region",
                        "conversion_confidence": "medium",
                        "family_relevance": "medium",
                        "quality_flags": [],
                        "matched_terms": ["Dario", "Pulgar"],
                        "converted_file": assembled.relative_to(tmp_path).as_posix(),
                        "chunk_manifest": chunk_manifest.relative_to(tmp_path).as_posix(),
                        "source_manifest": manifest.relative_to(tmp_path).as_posix(),
                    }
                ]
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    write_agent_queues(tmp_path)
    queue_path = tmp_path / "research" / "_agent-queues" / "source-prep.json"
    source_queue = json.loads(queue_path.read_text(encoding="utf-8"))
    task_id = source_queue["tasks"][0]["task_id"]
    assert source_queue["tasks"][0]["status"] == "needs_reread"

    update_agent_task_state(tmp_path, task_id, "done", agent="worker-1")
    write_agent_queues(tmp_path)
    source_queue = json.loads(queue_path.read_text(encoding="utf-8"))
    assert source_queue["tasks"][0]["status"] == "done"
    assert source_queue["tasks"][0]["task_state_status"] == "done"
    qa_queue = json.loads((tmp_path / "research" / "_agent-queues" / "conversion-qa.json").read_text(encoding="utf-8"))
    update_agent_task_state(tmp_path, qa_queue["tasks"][0]["task_id"], "done", agent="qa-1")
    write_agent_queues(tmp_path)

    extraction_queue = json.loads(
        (tmp_path / "research" / "_agent-queues" / "evidence-extraction.json").read_text(encoding="utf-8")
    )
    assert extraction_queue["tasks"][0]["status"] == "todo"

    write_source_usability_report(tmp_path)
    usability = json.loads((tmp_path / "research" / "_indexes" / "source-usability.json").read_text(encoding="utf-8"))
    assert usability["summary"]["status_counts"]["usable_for_extraction"] == 1
    assert usability["sources"][0]["qc_hold_count"] == 0
    assert usability["sources"][0]["page_repair_count"] == 0


def test_system_status_dashboard_summarizes_pipeline_artifacts(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "scan.jpg"
    Image.new("RGB", (20, 10), "white").save(source)
    prepare_raw_sources(tmp_path)
    write_agent_queues(tmp_path)
    write_source_prep_batches(tmp_path)
    (tmp_path / "raw" / "r2-derived-assets.json").write_text(
        json.dumps(
            {
                "files": [
                    {
                        "path": "raw/codex-conversion-jobs/job/extracted-images/page-0001/signature.png",
                        "bytes": 12,
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    written = write_system_status_dashboard(tmp_path)

    assert {path.name for path in written} == {"system-status.json", "System Dashboard.md"}
    payload = json.loads((tmp_path / "research" / "_indexes" / "system-status.json").read_text(encoding="utf-8"))
    assert payload["source_conversion"]["source_count"] == 1
    assert payload["source_conversion"]["conversion_job_count"] == 1
    assert payload["source_conversion"]["usability_status_counts"]["conversion_in_progress"] == 1
    assert payload["queues"]["source_prep"]["task_count"] == 1
    assert payload["queues"]["source_prep"]["path"] == "research/_agent-queues/source-prep.json"
    assert payload["storage"]["r2_derived_asset_count"] == 1
    assert payload["storage_lifecycle"]["status"] == "not_started"
    dashboard_text = (tmp_path / "research" / "System Dashboard.md").read_text(encoding="utf-8")
    assert "## Source Conversion" in dashboard_text
    assert "## Storage" in dashboard_text
    assert "## Final Site" in dashboard_text
    research_index = (tmp_path / "research" / "index.md").read_text(encoding="utf-8")
    assert "[[System Dashboard]]" in research_index


def test_storage_lifecycle_report_writes_page_level_deaccession_candidate(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "neutral-page.png"
    Image.new("RGB", (20, 10), "white").save(source)
    digest = genealogy_wiki.file_sha256(source)
    manifest_path = tmp_path / "raw" / "codex-conversion-jobs" / "neutral-page" / "manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(
            {
                "job_id": "neutral-page",
                "source_file": source.relative_to(tmp_path).as_posix(),
                "source_sha256": digest,
                "media_type": "image",
                "pages": [{"page": 1}],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    converted = tmp_path / "raw" / "converted" / "neutral-page.codex.md"
    neutral_text = "Office supply inventory lists paper, ink, envelopes, shelves, and repair notes. " * 20
    converted.write_text(
        f"""# Neutral Page

## Conversion Metadata

- Source: `{source.relative_to(tmp_path).as_posix()}`
- Source SHA-256: `{digest}`
- Manifest: `{manifest_path.relative_to(tmp_path).as_posix()}`

{complete_gemini_page_markdown(neutral_text)}
""",
        encoding="utf-8",
    )
    (tmp_path / "raw" / "source-prep-manifest.json").write_text(
        json.dumps(
            {
                "sources": [
                    {
                        "id": "SRC-neutral",
                        "title": "Neutral Page",
                        "raw_path": source.relative_to(tmp_path).as_posix(),
                        "media_type": "image",
                        "bytes": source.stat().st_size,
                        "sha256": digest,
                        "status": "converted",
                        "conversion_jobs": [{"manifest": manifest_path.relative_to(tmp_path).as_posix()}],
                        "converted_sources": [
                            {
                                "path": converted.relative_to(tmp_path).as_posix(),
                                "source": source.relative_to(tmp_path).as_posix(),
                                "source_manifest": manifest_path.relative_to(tmp_path).as_posix(),
                                "sha256": genealogy_wiki.file_sha256(converted),
                            }
                        ],
                    }
                ]
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)

    written = write_storage_lifecycle_report(tmp_path)

    assert {path.name for path in written} >= {"storage-lifecycle.json", "storage-lifecycle.md"}
    payload = json.loads((tmp_path / "research" / "_indexes" / "storage-lifecycle.json").read_text(encoding="utf-8"))
    page = payload["pages"][0]
    assert payload["summary"]["page_count"] == 1
    assert payload["summary"]["deaccession_candidate_count"] == 1
    assert page["retention_status"] == "deaccession_candidate"
    assert page["deaccession_allowed"] is True
    assert page["page_storage_unit"] == "page_level_raw_object"
    record_path = tmp_path / payload["deaccession_records"][0]
    assert record_path.exists()
    assert "No R2 object was deleted" in record_path.read_text(encoding="utf-8")

    write_system_status_dashboard(tmp_path, refresh_source_status=False)
    status = json.loads((tmp_path / "research" / "_indexes" / "system-status.json").read_text(encoding="utf-8"))
    assert status["storage_lifecycle"]["status"] == "active"
    assert status["storage_lifecycle"]["deaccession_record_count"] == 1


def test_storage_lifecycle_recovers_original_pages_from_metadata(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "archive.pdf"
    source.write_bytes(b"%PDF-1.4 placeholder")
    digest = genealogy_wiki.file_sha256(source)
    manifest_path = tmp_path / "raw" / "codex-conversion-jobs" / "archive-pages-4-5" / "manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(
            {
                "job_id": "archive-pages-4-5",
                "source_file": source.relative_to(tmp_path).as_posix(),
                "source_sha256": digest,
                "media_type": "pdf",
                "pages": [{"page": 4, "source_page": 4}, {"page": 5, "source_page": 5}],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    converted = tmp_path / "raw" / "converted" / "archive-pages-4-5.codex.md"
    neutral_page_text = "Office inventory, meeting logistics, supply notes, shelf counts, and envelope labels. " * 12
    converted.write_text(
        f"""# Archive Pages 4-5

## Conversion Metadata

- Source: `{source.relative_to(tmp_path).as_posix()}`
- Source SHA-256: `{digest}`
- Manifest: `{manifest_path.relative_to(tmp_path).as_posix()}`

## Page Metadata

- Task id: `source-prep:archive-pages-4-5:p0004`
- **Page number**: 4

## Literal Transcription

{neutral_page_text}

## Page Metadata

- Task id: `source-prep:archive-pages-4-5:p0005`

## Literal Transcription

{neutral_page_text}
""",
        encoding="utf-8",
    )
    (tmp_path / "raw" / "source-prep-manifest.json").write_text(
        json.dumps(
            {
                "sources": [
                    {
                        "id": "SRC-archive",
                        "title": "Archive",
                        "raw_path": source.relative_to(tmp_path).as_posix(),
                        "media_type": "pdf",
                        "sha256": digest,
                        "status": "converted",
                        "conversion_jobs": [{"manifest": manifest_path.relative_to(tmp_path).as_posix()}],
                        "converted_sources": [{"path": converted.relative_to(tmp_path).as_posix()}],
                    }
                ]
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)

    write_storage_lifecycle_report(tmp_path)

    payload = json.loads((tmp_path / "research" / "_indexes" / "storage-lifecycle.json").read_text(encoding="utf-8"))
    assert [page["page"] for page in payload["pages"]] == [4, 5]
    assert {page["page_storage_unit"] for page in payload["pages"]} == {"whole_source_object"}
    assert all("raw_source_is_not_page_level" in page["deaccession_blockers"] for page in payload["pages"])


def test_write_post_conversion_qc_flags_bad_and_suspicious_pages(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    person = tmp_path / "wiki" / "people" / "dario-pulgar.md"
    person.write_text("# Dario Pulgar\n", encoding="utf-8")
    converted = tmp_path / "raw" / "converted" / "sample.codex.md"
    converted.write_text(
        """# Sample

## Conversion Metadata

- Source: `raw/sources/sample.pdf`
- Source SHA-256: `abc123`
- Manifest: `raw/codex-conversion-jobs/sample/manifest.json`

# Page 1

![Source page](../codex-conversion-jobs/sample/page-images/page-0001.jpg)

## Literal Transcription

[No visible text transcribed in this batch pass.]

# Page 2

## Literal Transcription

The record names David Pulgar as a delegate.
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)

    written = write_post_conversion_qc(tmp_path)

    assert (tmp_path / "research" / "_conversion-review" / "qc-index.json") in written
    queue_text = (tmp_path / "research" / "_conversion-review" / "page-queues" / "sample-codex.md").read_text(
        encoding="utf-8"
    )
    corrections_text = (tmp_path / "research" / "_conversion-review" / "corrections" / "sample-codex.md").read_text(
        encoding="utf-8"
    )
    assert "Page 1" in queue_text
    assert "placeholder_transcription" in queue_text
    assert "Page 2" in queue_text
    assert "David" in corrections_text
    assert "Dario" in corrections_text
    assert "reread-page" in queue_text
    qc_pages = json.loads((tmp_path / "research" / "_conversion-review" / "qc-pages.json").read_text(encoding="utf-8"))
    page_two = next(page for page in qc_pages["pages"] if page["page"] == 2)
    assert page_two["recommended_action"] == "reread-page"
    assert page_two["conversion_confidence"] == "low"


def test_suspicious_name_readings_ignore_common_lowercase_near_matches() -> None:
    terms = {"dario": "Dario", "smith": "Smith"}

    assert find_suspicious_name_readings("The dark dais is visible with papers.", terms) == []

    readings = find_suspicious_name_readings("The record names David Pulgar.", terms)
    assert readings[0]["literal"] == "David"
    assert readings[0]["suspected"] == "Dario"


def test_source_prep_batches_keep_suspicious_name_pages_single() -> None:
    base_task = {
        "queue": "source-prep",
        "role": "source_converter",
        "status": "needs_reread",
        "source": "raw/sources/archive.pdf",
        "source_sha256": "abc123",
        "job_manifest": "raw/codex-conversion-jobs/archive/manifest.json",
        "job_id": "ARCHIVE",
        "title": "Archive",
        "work_order": "raw/codex-conversion-jobs/archive/work-orders/page-0001.md",
        "page_image": "raw/codex-conversion-jobs/archive/page-images/page-0001.jpg",
        "output_path": "raw/codex-conversion-jobs/archive/page-markdown/page-0001.md",
        "image_output_dir": "raw/codex-conversion-jobs/archive/extracted-images/page-0001",
        "repair_reason": "post_conversion_qc_hold",
        "recommended_action": "reread-page",
        "family_relevance": "medium",
        "matched_terms": ["Pulgar"],
    }
    tasks = []
    for page in range(1, 5):
        task = dict(base_task)
        task["task_id"] = f"source-prep:archive:p{page:04d}"
        task["page"] = page
        if page == 2:
            task["suspicious_readings"] = [{"literal": "David", "suspected": "Dario"}]
        tasks.append(task)

    batches = build_source_prep_batch_agent_tasks(tasks, max_pages=4, limit=10)

    assert [batch["page_count"] for batch in batches] == [1, 1, 1, 1]
    assert batches[1]["task_ids"] == ["source-prep:archive:p0002"]
    assert "David -> Dario" in batches[1]["prompt"]


def test_suspicious_name_readings_ignore_publication_words() -> None:
    terms = {"dario": "Dario", "pulgar": "Pulgar"}

    assert find_suspicious_name_readings("En el Diario El Sur se publicó el aviso.", terms) == []

    readings = find_suspicious_name_readings("En el Diario El Sur, the record names David Pulgar.", terms)
    assert [reading["literal"] for reading in readings] == ["David"]
    assert readings[0]["suspected"] == "Dario"


def test_text_layer_only_pages_are_queued_for_visual_reread(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    converted = tmp_path / "raw" / "converted" / "text-layer.codex.md"
    converted.write_text(
        """# Text Layer Source

## Conversion Metadata

- Source: `raw/sources/text-layer.pdf`
- Source SHA-256: `abc123`
- Manifest: `raw/codex-conversion-jobs/text-layer/manifest.json`

# Page 1

## Page Metadata

PDF text-layer extraction may omit handwriting and layout.

## Layout And Reading Order

Automated text-layer batch pass.

## Literal Transcription

This is a plausible text layer with no obvious family names.

## Images, Captions, And Visual Notes

No image crop was extracted.

## Translation

Not needed.

## Interpretation

No interpretation added.

## Uncertain Or Illegible

None marked.

## Extracted Genealogy Leads

None.

## Completeness Audit

Text layer only.
""",
        encoding="utf-8",
    )
    chunk_converted_markdown(tmp_path, converted)

    write_post_conversion_qc(tmp_path)

    pages = json.loads((tmp_path / "research" / "_conversion-review" / "qc-pages.json").read_text(encoding="utf-8"))[
        "pages"
    ]
    page = pages[0]
    assert page["recommended_action"] == "reread-page"
    assert "text_layer_only" in page["quality_flags"]


def test_write_source_prep_index_inventories_raw_sources_and_links_jobs(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "record.txt"
    source.write_text("historical source", encoding="utf-8")

    manifest = create_codex_conversion_job(
        tmp_path,
        source,
        job_id="CJ002",
        title="Record",
    )
    index_path = write_source_prep_index(tmp_path)
    text = index_path.read_text(encoding="utf-8")

    assert "raw/sources/record.txt" in text
    assert '"media_type": "text"' in text
    assert "CJ002" in text
    assert manifest.relative_to(tmp_path).as_posix() in text


def test_chunk_converted_markdown_writes_page_scoped_chunks(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    converted = tmp_path / "raw" / "converted" / "sample.codex.md"
    converted.write_text(
        """# Sample Source

## Conversion Metadata

- Source: `raw/codex-conversion-jobs/cj/source/source.pdf`
- Source SHA-256: `abc123`
- Manifest: `raw/codex-conversion-jobs/cj/manifest.json`

# Page 1

## Literal Transcription

Short page.

# Page 2

## Literal Transcription

Long line one.

Long line two.
""",
        encoding="utf-8",
    )

    manifest = chunk_converted_markdown(tmp_path, converted, max_chars=1000)
    text = manifest.read_text(encoding="utf-8")

    assert '"converted_file": "raw/converted/sample.codex.md"' in text
    assert '"source": "raw/codex-conversion-jobs/cj/source/source.pdf"' in text
    assert '"source_sha256": "abc123"' in text
    assert (manifest.parent / "page-0001-chunk-01.md").exists()
    assert (manifest.parent / "page-0002-chunk-01.md").exists()
    chunk_text = (manifest.parent / "page-0001-chunk-01.md").read_text(encoding="utf-8")
    assert "type: source_prep_chunk" in chunk_text
    assert "Short page." in chunk_text


def test_chunk_converted_markdown_splits_page_metadata_sections(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    converted = tmp_path / "raw" / "converted" / "sample-metadata.codex.md"
    converted.write_text(
        """# Sample Source

## Conversion Metadata

- Source: `raw/sources/source.pdf`
- Source SHA-256: `abc123`
- Manifest: `raw/codex-conversion-jobs/job/manifest.json`

## Page Metadata
- **task_id**: `source-prep:job:p0001`
- **page_number**: 1

## Literal Transcription

First page text.

## Page Metadata
- Task id: `source-prep:job:p0002`
- Page: 2

## Literal Transcription

Second page text.

## Page Metadata
- Task id: `source-prep:job:p0003`

## Literal Transcription

Third page text.
""",
        encoding="utf-8",
    )
    output_dir = tmp_path / "raw" / "chunks" / "sample-metadata"
    output_dir.mkdir(parents=True)
    stale_chunk = output_dir / "page-0001-chunk-99.md"
    stale_chunk.write_text("stale generated chunk", encoding="utf-8")

    manifest_path = chunk_converted_markdown(tmp_path, converted, output_dir=output_dir, max_chars=1000)

    assert not stale_chunk.exists()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert [chunk["page_start"] for chunk in manifest["chunks"]] == [1, 2, 3]
    assert [Path(chunk["path"]).name for chunk in manifest["chunks"]] == [
        "page-0001-chunk-01.md",
        "page-0002-chunk-01.md",
        "page-0003-chunk-01.md",
    ]
    assert "Second page text." in (output_dir / "page-0002-chunk-01.md").read_text(encoding="utf-8")
    assert "Third page text." in (output_dir / "page-0003-chunk-01.md").read_text(encoding="utf-8")


def test_sync_vault_transcriptions_writes_editable_notes_and_preserves_manual_edits(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    source = tmp_path / "raw" / "sources" / "record.txt"
    source.write_text("historical source", encoding="utf-8")

    manifest = create_codex_conversion_job(
        tmp_path,
        source,
        job_id="CJ003",
        title="Record",
    )
    job_dir = manifest.parent
    crop = job_dir / "extracted-images" / "page-0001" / "page-0001-image-01.png"
    crop.parent.mkdir(parents=True, exist_ok=True)
    crop.write_bytes(b"not a real image")
    page_output = job_dir / "page-markdown" / "page-0001.md"
    page_output.write_text(
        """# Page 1

## Literal Transcription

Converted text.

## Images, Captions, And Visual Notes

![Seal](../extracted-images/page-0001/page-0001-image-01.png)
""",
        encoding="utf-8",
    )
    converted = assemble_codex_conversion_job(tmp_path, manifest)
    chunk_converted_markdown(tmp_path, converted)
    write_source_prep_index(tmp_path)

    source_page = tmp_path / "research" / "sources" / "src-5c8b314eb484-record.md"
    source_page.write_text(
        """---
type: source
source_id: SRC-5c8b314eb484
---

# Record

## Source Identity

## Obsidian Inspection

## Conversion Artifacts

## Transcription Or Abstract

Use the converted Markdown and chunk manifest above as the prepared source text. Do not create claims directly from this page without checking the converted source and original image/file evidence.

## Extracted Claims
""",
        encoding="utf-8",
    )

    written = sync_vault_transcriptions(tmp_path)

    transcription = tmp_path / "research" / "sources" / "transcriptions" / "src-5c8b314eb484-record.md"
    page_note = tmp_path / "research" / "sources" / "transcriptions" / "src-5c8b314eb484-record" / "page-0001.md"
    assert transcription in written
    assert page_note in written
    index_text = transcription.read_text(encoding="utf-8")
    page_text = page_note.read_text(encoding="utf-8")
    assert "type: source_transcription_index" in index_text
    assert "[[sources/transcriptions/src-5c8b314eb484-record/page-0001|Page 1]]" in index_text
    assert "type: source_transcription_page" in page_text
    assert "Converted text." in page_text
    assert "../../../_assets/conversions/src-5c8b314eb484-record/extracted-images/page-0001/page-0001-image-01.png" in page_text
    assert (tmp_path / "research" / "_assets" / "conversions" / "src-5c8b314eb484-record" / "extracted-images" / "page-0001" / "page-0001-image-01.png").exists()
    assert "[[sources/transcriptions/src-5c8b314eb484-record|Open transcription index]]" in source_page.read_text(encoding="utf-8")
    assert "[[sources/transcriptions/src-5c8b314eb484-record|record]]" in (tmp_path / "research" / "index.md").read_text(encoding="utf-8")

    page_note.write_text(page_text + "\nManual correction.\n", encoding="utf-8")
    sync_vault_transcriptions(tmp_path)
    assert "Manual correction." in page_note.read_text(encoding="utf-8")


def test_sync_vault_transcriptions_flags_placeholder_conversions(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    from PIL import Image

    source = tmp_path / "raw" / "sources" / "scan.png"
    Image.new("RGB", (20, 10), "white").save(source)

    manifest = create_codex_conversion_job(
        tmp_path,
        source,
        job_id="CJ004",
        title="Scan",
    )
    page_output = manifest.parent / "page-markdown" / "page-0001.md"
    page_output.write_text(
        """# Page 1

## Literal Transcription

[No visible text transcribed in this batch pass.]

## Images, Captions, And Visual Notes

Full standalone image copied as extracted visual evidence.
""",
        encoding="utf-8",
    )
    converted = assemble_codex_conversion_job(tmp_path, manifest)
    chunk_converted_markdown(tmp_path, converted)
    write_source_prep_index(tmp_path)

    sync_vault_transcriptions(tmp_path)

    page_note = next((tmp_path / "research" / "sources" / "transcriptions").glob("src-*-scan/page-0001.md"))
    transcription = page_note.parent.with_suffix(".md")
    page_text = page_note.read_text(encoding="utf-8")
    index_text = transcription.read_text(encoding="utf-8")
    dashboard_text = (tmp_path / "research" / "Conversion Dashboard.md").read_text(encoding="utf-8")

    assert "status: needs_visual_conversion" in page_text
    assert 'quality_flags: ["placeholder_transcription", "image_preserved_not_transcribed"]' in page_text
    assert "`placeholder_transcription`" in page_text
    assert "status: needs_visual_conversion" in index_text
    assert "needs_visual_conversion" in dashboard_text


def test_lint_flags_detached_claim(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    claim = tmp_path / "research" / "claims" / "CL001-test.md"
    claim.write_text(
        """---
type: claim
status: accepted
confidence: 9.5
source:
---

# Claim

## Claim

Dario attended an event.

## Literal Source Support

## Interpretation

## Uncertainty
""",
        encoding="utf-8",
    )

    issues = lint_genealogy_wiki(tmp_path)

    assert "claim page missing source: research/claims/CL001-test.md" in issues


def test_generate_tree_uses_relationship_pages(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    relationship = tmp_path / "research" / "relationships" / "R001-parent.md"
    relationship.write_text(
        """---
type: relationship
status: accepted
relationship_type: proven_parent
confidence: 9.0
person_a: [[people/parent]]
person_b: [[people/child]]
---

# Relationship

## Evidence For

## Evidence Against
""",
        encoding="utf-8",
    )

    output = generate_tree(tmp_path)

    tree_text = output.read_text(encoding="utf-8")
    assert 'n_people_parent["Parent"] -->|parent of| n_people_child["Child"]' in tree_text
    assert "accepted 9.0" not in tree_text


def test_build_static_site_renders_public_wiki_pages(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    (tmp_path / "wiki" / "people").mkdir(parents=True, exist_ok=True)
    (tmp_path / "wiki" / "people" / "dario-pulgar.md").write_text(
        """---
type: person
status: draft
---

# Dario Pulgar

See [[Family Tree]] and [[people/relative|a relative]].
""",
        encoding="utf-8",
    )
    (tmp_path / "wiki" / "people" / "relative.md").write_text("# Relative\n", encoding="utf-8")
    (tmp_path / "wiki" / "_templates").mkdir(parents=True, exist_ok=True)
    (tmp_path / "wiki" / "_templates" / "hidden.md").write_text("# Hidden Template\n", encoding="utf-8")
    (tmp_path / "wiki" / "log.md").write_text("# Internal Log\n", encoding="utf-8")

    written = build_static_site(tmp_path)

    written_names = {path.relative_to(tmp_path).as_posix() for path in written}
    assert "site/index.html" in written_names
    assert "site/family-tree.html" in written_names
    assert "site/people/dario-pulgar.html" in written_names
    assert "site/people/relative.html" in written_names
    assert "site/assets/site.css" in written_names
    assert "site/site-manifest.json" in written_names
    assert not (tmp_path / "site" / "_templates" / "hidden.html").exists()
    assert not (tmp_path / "site" / "log.html").exists()

    person_html = (tmp_path / "site" / "people" / "dario-pulgar.html").read_text(encoding="utf-8")
    assert '<a href="../family-tree.html">Family Tree</a>' in person_html
    assert '<a href="relative.html">a relative</a>' in person_html
    assert "Generated from wiki/people/dario-pulgar.md" in person_html
    manifest = json.loads((tmp_path / "site" / "site-manifest.json").read_text(encoding="utf-8"))
    assert manifest["page_count"] == 4
    assert manifest["storage_contract"].startswith("HTML, CSS, and build manifests are GitHub files")


def test_compile_narrative_uses_only_accepted_or_probable_claims(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    accepted = tmp_path / "research" / "claims" / "CL001-accepted.md"
    accepted.write_text(
        """---
type: claim
status: accepted
confidence: 9.5
subject: Dario
source: [[sources/S001]]
---

# Claim

## Claim

Dario attended the conference.
""",
        encoding="utf-8",
    )
    rejected = tmp_path / "research" / "claims" / "CL002-rejected.md"
    rejected.write_text(
        """---
type: claim
status: rejected
confidence: 1.0
subject: Dario
source: [[sources/S002]]
---

# Claim

## Claim

Dario lived on the Moon.
""",
        encoding="utf-8",
    )

    narrative = compile_narrative(tmp_path, "Dario")
    text = narrative.read_text(encoding="utf-8")

    assert "Dario attended the conference." in text
    assert "Moon" not in text
    assert "narrative_type: individual_biography" in text
    assert "## Family-Relevant Historical Context" in text


def test_lint_flags_parent_born_after_child(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    (tmp_path / "wiki" / "people" / "parent.md").write_text(
        """---
type: person
birth_year: 1900
death_year:
---

# Parent

See [[Family Tree]].
""",
        encoding="utf-8",
    )
    (tmp_path / "wiki" / "people" / "child.md").write_text(
        """---
type: person
birth_year: 1890
death_year:
---

# Child

See [[Family Tree]].
""",
        encoding="utf-8",
    )
    (tmp_path / "research" / "relationships" / "R001-parent.md").write_text(
        """---
type: relationship
status: accepted
relationship_type: parent_child
confidence: 9.0
person_a: [[people/parent]]
person_b: [[people/child]]
---

# Relationship

## Evidence For

## Evidence Against
""",
        encoding="utf-8",
    )

    issues = lint_genealogy_wiki(tmp_path)

    assert "chronology impossible, parent born after child: relationships/R001-parent.md" in issues


def test_create_claim_and_build_claim_index(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    (tmp_path / "wiki" / "people" / "dario.md").write_text(
        """---
type: person
---

# Dario
""",
        encoding="utf-8",
    )
    (tmp_path / "research" / "sources" / "S001-record.md").write_text(
        """---
type: source
---

# Source

## Extracted Claims
""",
        encoding="utf-8",
    )

    claim_path = create_claim(
        root=tmp_path,
        claim_id="CL001",
        claim_text="Dario attended the 1929 Geneva Conventions.",
        claim_type="event",
        subject="[[people/dario]]",
        source="[[sources/S001-record]]",
        status="accepted",
        confidence=9.5,
    )

    claims = build_claim_index(tmp_path)

    assert claim_path.exists()
    assert len(claims) == 1
    assert claims[0].status == "accepted"
    assert claims[0].confidence == 9.5
    assert claims[0].text == "Dario attended the 1929 Geneva Conventions."


def test_write_claim_index(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_claim(
        root=tmp_path,
        claim_id="CL001",
        claim_text="Dario attended the conference.",
        claim_type="event",
        subject="[[people/dario]]",
        source="[[sources/S001-record]]",
    )

    index_path = write_claim_index(tmp_path)
    text = index_path.read_text(encoding="utf-8")

    assert index_path == tmp_path / "research" / "_indexes" / "claims.json"
    assert '"claims"' in text
    assert "Dario attended the conference." in text


def test_lint_flags_missing_claim_reference_target(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_claim(
        root=tmp_path,
        claim_id="CL001",
        claim_text="Dario attended the conference.",
        claim_type="event",
        subject="[[people/missing-dario]]",
        source="[[sources/missing-source]]",
    )

    issues = lint_genealogy_wiki(tmp_path)

    assert "claim research/claims/cl001-dario-attended-the-conference.md subject target missing: [[people/missing-dario]]" in issues
    assert "claim research/claims/cl001-dario-attended-the-conference.md source target missing: [[sources/missing-source]]" in issues


def test_create_relationship_and_calculate_confidence_from_claims(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    (tmp_path / "wiki" / "people" / "parent.md").write_text("---\ntype: person\n---\n# Parent\n", encoding="utf-8")
    (tmp_path / "wiki" / "people" / "child.md").write_text("---\ntype: person\n---\n# Child\n", encoding="utf-8")
    (tmp_path / "research" / "sources" / "S001-record.md").write_text(
        "---\ntype: source\n---\n# Source\n\n## Extracted Claims\n",
        encoding="utf-8",
    )
    claim_path = create_claim(
        root=tmp_path,
        claim_id="CL001",
        claim_text="The record names Parent as Child's parent.",
        claim_type="relationship",
        subject="[[people/child]]",
        source="[[sources/S001-record]]",
        status="accepted",
        confidence=8.5,
    )
    claim_link = f"[[claims/{claim_path.stem}]]"

    create_relationship(
        root=tmp_path,
        relationship_id="R001",
        relationship_type="proven_parent",
        person_a="[[people/parent]]",
        person_b="[[people/child]]",
        status="accepted",
        supporting_claims=[claim_link],
    )

    relationships = build_relationship_index(tmp_path)

    assert len(relationships) == 1
    assert relationships[0].supporting_claims == [claim_link]
    assert relationships[0].calculated_confidence == 8.5


def test_write_relationship_index(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_relationship(
        root=tmp_path,
        relationship_id="R001",
        relationship_type="possible_sibling",
        person_a="[[people/a]]",
        person_b="[[people/b]]",
    )

    index_path = write_relationship_index(tmp_path)
    text = index_path.read_text(encoding="utf-8")

    assert index_path == tmp_path / "research" / "_indexes" / "relationships.json"
    assert '"relationships"' in text
    assert "possible_sibling" in text


def test_lint_flags_missing_relationship_targets_and_claims(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_relationship(
        root=tmp_path,
        relationship_id="R001",
        relationship_type="possible_sibling",
        person_a="[[people/missing-a]]",
        person_b="[[people/missing-b]]",
        supporting_claims=["[[claims/missing-claim]]"],
    )

    issues = lint_genealogy_wiki(tmp_path)

    assert "relationship research/relationships/r001-people-missing-a-people-missing-b-possible-sibling.md person_a target missing: [[people/missing-a]]" in issues
    assert "relationship research/relationships/r001-people-missing-a-people-missing-b-possible-sibling.md references missing claim: [[claims/missing-claim]]" in issues


def test_write_relationship_graph(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_relationship(
        root=tmp_path,
        relationship_id="R001",
        relationship_type="spouse",
        person_a="[[people/a]]",
        person_b="[[people/b]]",
        status="probable",
        confidence=7.5,
    )

    graph_path = write_relationship_graph(tmp_path)
    text = graph_path.read_text(encoding="utf-8")

    assert graph_path == tmp_path / "research" / "_indexes" / "relationship-graph.json"
    assert '"nodes"' in text
    assert '"edges"' in text
    assert '"type": "spouse"' in text


def test_sync_github_database_source_conversion_only_limits_scope(tmp_path, monkeypatch) -> None:
    class GitResult:
        def __init__(self, stdout: str = "", returncode: int = 0) -> None:
            self.stdout = stdout
            self.stderr = ""
            self.returncode = returncode

    for relative_path in [
        "raw/source-prep-manifest.json",
        "raw/codex-conversion-jobs/job-001/manifest.json",
        "raw/converted/job-001.codex.md",
        "raw/chunks/job-001/manifest.json",
        "research/_agent-queues/source-prep-batches.json",
        "research/_agent-queues/task-state.json",
        "research/_automation/gemini-source-prep-state.json",
        "research/log.md",
        "research/claims/unrelated.md",
        "wiki/index.md",
    ]:
        path = tmp_path / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}", encoding="utf-8")

    calls: list[list[str]] = []

    def fake_run_git(root, args, check=True):
        calls.append(args)
        if args == ["diff", "--cached", "--quiet"]:
            return GitResult(returncode=0)
        return GitResult()

    monkeypatch.setattr(genealogy_wiki, "run_git", fake_run_git)

    summary = sync_github_database(tmp_path, dry_run=True, source_conversion_only=True)

    assert summary["source_conversion_only"] is True
    assert "research/claims/unrelated.md" not in summary["included"]
    assert "wiki/index.md" not in summary["included"]
    dry_run_add = next(args for args in calls if args[:3] == ["add", "--dry-run", "-A"])
    assert "-f" in dry_run_add
    assert "raw/converted" in dry_run_add
    assert "research/_agent-queues/task-state.json" in dry_run_add
    assert "research" not in dry_run_add
    assert "wiki" not in dry_run_add
