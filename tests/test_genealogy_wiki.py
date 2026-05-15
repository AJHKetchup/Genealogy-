import json

import pytest

import historic_doc_ingest.genealogy_wiki as genealogy_wiki

from historic_doc_ingest.genealogy_wiki import (
    build_claim_index,
    build_relationship_index,
    classify_gemini_source_prep_batch,
    chunk_converted_markdown,
    compile_narrative,
    assemble_codex_conversion_job,
    create_claim,
    create_codex_conversion_job,
    create_material_packet,
    create_relationship,
    create_source_packet,
    generate_tree,
    find_suspicious_name_readings,
    init_genealogy_wiki,
    lint_genealogy_wiki,
    mark_source_relevance_feedback,
    release_stale_agent_tasks,
    write_claim_index,
    write_relationship_graph,
    write_relationship_index,
    write_source_prep_index,
    write_source_usability_report,
    write_agent_queues,
    write_source_prep_batches,
    write_post_conversion_qc,
    next_codex_conversion_work_order,
    prepare_raw_sources,
    source_prep_page_cache_path,
    source_prep_fastlane_run,
    source_prep_gemini_run,
    sync_vault_transcriptions,
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

## Translation

Not needed.

## Interpretation

No interpretation added.

## Uncertain Or Illegible

None noted.

## Extracted Genealogy Leads

None.

## Completeness Audit

The visible page was reviewed against the page image.
"""


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
    assert (tmp_path / "wiki" / "relationships").exists()
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
    assert (tmp_path / "research" / "_indexes").exists()
    assert (tmp_path / "raw" / "converted").exists()
    assert (tmp_path / "raw" / "chunks").exists()


def test_lint_genealogy_wiki_passes_fresh_scaffold(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    assert lint_genealogy_wiki(tmp_path) == []


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


def test_gemini_source_prep_routes_simple_complex_and_relevant_pages(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    base_batch = {
        "task_id": "source-prep-batch:job:p0001",
        "page_count": 1,
        "status": "todo",
        "source": "raw/sources/minutes.pdf",
        "title": "Committee minutes",
        "first_page": 1,
        "task_ids": ["source-prep:job:p0001"],
        "pages": [
            {
                "page": 1,
                "page_image": "raw/codex-conversion-jobs/job/page-images/page-0001.jpg",
                "output_path": "raw/codex-conversion-jobs/job/page-markdown/page-0001.md",
                "image_output_dir": "raw/codex-conversion-jobs/job/extracted-images/page-0001",
            }
        ],
    }

    simple = classify_gemini_source_prep_batch(tmp_path, base_batch, lite_model="lite", pro_model="pro")
    assert simple["tier"] == "lite"
    assert simple["model"] == "lite"

    complex_batch = dict(base_batch)
    complex_batch["title"] = "Passenger list"
    complex_batch["pages"] = [dict(base_batch["pages"][0], quality_flags=["possible_table_layout_loss"])]
    complex_route = classify_gemini_source_prep_batch(tmp_path, complex_batch, lite_model="lite", pro_model="pro")
    assert complex_route["tier"] == "pro"
    assert complex_route["model"] == "pro"

    relevant_batch = dict(base_batch)
    relevant_batch["pages"] = [
        dict(base_batch["pages"][0], family_relevance="critical", matched_terms=["Pulgar"], suspicious_readings=[])
    ]
    relevant_route = classify_gemini_source_prep_batch(tmp_path, relevant_batch, lite_model="lite", pro_model="pro")
    assert relevant_route["tier"] == "pro_with_crops"
    assert relevant_route["model"] == "pro"
    assert relevant_route["use_crops"] is True


def test_source_relevance_feedback_requeues_done_page_for_pro_crops(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    Image = pytest.importorskip("PIL.Image")
    source = tmp_path / "raw" / "sources" / "source-page.jpg"
    Image.new("RGB", (100, 120), "white").save(source)
    prepare_raw_sources(tmp_path)

    write_agent_queues(tmp_path)
    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    task = source_queue["tasks"][0]
    output_path = tmp_path / task["output_path"]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(complete_page_markdown("Already converted cheaply."), encoding="utf-8")
    update_agent_task_state(tmp_path, task["task_id"], "done", agent="lite")

    mark_source_relevance_feedback(
        tmp_path,
        source=task["source"],
        page=task["page"],
        relevance="critical",
        treatment="pro_with_crops",
        reason="Research agent found this page may identify a direct ancestor.",
        entities=["Dario Pulgar"],
        terms=["Pulgar"],
        agent="evidence-extractor",
    )
    write_agent_queues(tmp_path)
    source_queue = json.loads((tmp_path / "research" / "_agent-queues" / "source-prep.json").read_text(encoding="utf-8"))
    task = source_queue["tasks"][0]

    assert task["status"] == "needs_reread"
    assert task["research_relevance"] == "critical"
    assert task["requested_treatment"] == "pro_with_crops"
    assert task["research_entities"] == ["Dario Pulgar"]
    assert task["matched_terms"] == ["Pulgar"]


def test_gemini_source_prep_run_writes_valid_page_output(tmp_path, monkeypatch) -> None:
    init_genealogy_wiki(tmp_path)
    Image = pytest.importorskip("PIL.Image")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    (tmp_path / ".env").write_text("GEMINI_API_KEY=test-key\n", encoding="utf-8")
    source = tmp_path / "raw" / "sources" / "source-page.jpg"
    Image.new("RGB", (100, 120), "white").save(source)
    prepare_raw_sources(tmp_path)
    write_agent_queues(tmp_path)
    write_source_prep_batches(tmp_path, max_pages=1, limit=5)

    def fake_gemini(**kwargs):
        assert kwargs["api_key"] == "test-key"
        assert kwargs["model"] == "gemini-2.5-flash-lite"
        assert len(kwargs["media_paths"]) == 1
        return {
            "text": complete_page_markdown("Converted by Gemini."),
            "finish_reason": "STOP",
            "usage": {"promptTokenCount": 10, "candidatesTokenCount": 20, "totalTokenCount": 30},
        }

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fake_gemini)
    summary = source_prep_gemini_run(tmp_path, limit=1)

    assert summary["completed"] == 1
    assert summary["route_counts"]["lite"] == 1
    output_path = next((tmp_path / "raw" / "codex-conversion-jobs").glob("*/page-markdown/page-0001.md"))
    assert "Converted by Gemini." in output_path.read_text(encoding="utf-8")
    task_state = json.loads((tmp_path / "research" / "_agent-queues" / "task-state.json").read_text(encoding="utf-8"))
    assert {state["status"] for state in task_state["tasks"].values()} == {"done"}


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

    extraction_queue = json.loads(
        (tmp_path / "research" / "_agent-queues" / "evidence-extraction.json").read_text(encoding="utf-8")
    )
    assert extraction_queue["tasks"][0]["status"] == "todo"

    write_source_usability_report(tmp_path)
    usability = json.loads((tmp_path / "research" / "_indexes" / "source-usability.json").read_text(encoding="utf-8"))
    assert usability["summary"]["status_counts"]["usable_for_extraction"] == 1
    assert usability["sources"][0]["qc_hold_count"] == 0
    assert usability["sources"][0]["page_repair_count"] == 0


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


def test_suspicious_name_readings_ignore_common_lowercase_near_matches() -> None:
    terms = {"dario": "Dario", "smith": "Smith"}

    assert find_suspicious_name_readings("The dark dais is visible with papers.", terms) == []

    readings = find_suspicious_name_readings("The record names David Pulgar.", terms)
    assert readings[0]["literal"] == "David"
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
    claim = tmp_path / "wiki" / "claims" / "CL001-test.md"
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

    assert "claim page missing source: claims/CL001-test.md" in issues


def test_generate_tree_uses_relationship_pages(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    relationship = tmp_path / "wiki" / "relationships" / "R001-parent.md"
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

    assert "proven_parent accepted 9.0" in output.read_text(encoding="utf-8")


def test_compile_narrative_uses_only_accepted_or_probable_claims(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    accepted = tmp_path / "wiki" / "claims" / "CL001-accepted.md"
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
    rejected = tmp_path / "wiki" / "claims" / "CL002-rejected.md"
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

[[relationships/R001-parent]]
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

[[relationships/R001-parent]]
""",
        encoding="utf-8",
    )
    (tmp_path / "wiki" / "relationships" / "R001-parent.md").write_text(
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

    assert "claim wiki/claims/cl001-dario-attended-the-conference.md subject target missing: [[people/missing-dario]]" in issues
    assert "claim wiki/claims/cl001-dario-attended-the-conference.md source target missing: [[sources/missing-source]]" in issues


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

    assert "relationship wiki/relationships/r001-people-missing-a-people-missing-b-possible-sibling.md person_a target missing: [[people/missing-a]]" in issues
    assert "relationship wiki/relationships/r001-people-missing-a-people-missing-b-possible-sibling.md references missing claim: [[claims/missing-claim]]" in issues


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
