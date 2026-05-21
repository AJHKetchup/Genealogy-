import json

import pytest

from historic_doc_ingest import genealogy_wiki
from historic_doc_ingest.genealogy_wiki import source_prep_gemini_run


def write_docling_unusable_entries(root, entries: list[dict[str, object]]) -> None:
    queue_dir = root / "research" / "_agent-queues"
    discovery_dir = root / "raw" / "discovery" / "docling" / "job-one"
    queue_dir.mkdir(parents=True, exist_ok=True)
    discovery_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": 1,
        "purpose": "Test Docling discovery state for Gemini fallback routing.",
        "entries": {},
    }
    for entry in entries:
        task_id = str(entry["task_id"])
        source_sha256 = str(entry["source_sha256"])
        page = int(entry["page"])
        discovery_path = f"raw/discovery/docling/job-one/page-{page:04d}.md"
        (root / discovery_path).write_text(
            "# Rough Docling Discovery\n\nDiscovery status: `rough_unusable`\n",
            encoding="utf-8",
        )
        payload["entries"][genealogy_wiki.source_prep_discovery_key(task_id, source_sha256)] = {
            "status": "rough_unusable",
            "task_id": task_id,
            "source": str(entry.get("source", "raw/sources/source.png")),
            "source_sha256": source_sha256,
            "page": page,
            "discovery_path": discovery_path,
            "readability_flags": ["test_docling_unusable"],
        }
    (queue_dir / "source-prep-discovery.json").write_text(json.dumps(payload), encoding="utf-8")


def complete_gemini_markdown(visual_manifest: str) -> str:
    return f"""# Page 1

## Page Metadata

Page converted from the prepared page image.

## Layout And Reading Order

Single-page source read top to bottom.

## Literal Transcription

DARIO PULGAR SMITH

## Images, Captions, And Visual Notes

The page contains a portrait photograph.

## Uncertain Or Illegible

None noted.

## Completeness Audit

The visible page was reviewed against the page image.

## Visual Region Manifest

```json
{visual_manifest}
```
"""


def write_test_batch(root, *, requested_treatment: str = "") -> None:
    queue_dir = root / "research" / "_agent-queues"
    queue_dir.mkdir(parents=True, exist_ok=True)
    page_dir = root / "raw" / "codex-conversion-jobs" / "job-one"
    page_image = page_dir / "page-images" / "page-0001.png"
    image_output_dir = page_dir / "extracted-images" / "page-0001"
    output_path = page_dir / "page-markdown" / "page-0001.md"
    page_image.parent.mkdir(parents=True, exist_ok=True)
    image_output_dir.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pil_image = pytest.importorskip("PIL.Image")
    image = pil_image.new("RGB", (200, 100), color="white")
    for x in range(20, 80):
        for y in range(20, 70):
            image.putpixel((x, y), (20, 20, 20))
    image.save(page_image)

    page = {
        "page": 1,
        "task_id": "source-prep:job-one:p0001",
        "page_image": "raw/codex-conversion-jobs/job-one/page-images/page-0001.png",
        "work_order": "raw/codex-conversion-jobs/job-one/work-orders/page-0001.md",
        "output_path": "raw/codex-conversion-jobs/job-one/page-markdown/page-0001.md",
        "image_output_dir": "raw/codex-conversion-jobs/job-one/extracted-images/page-0001",
    }
    if requested_treatment:
        page.update(
            {
                "research_relevance": "high",
                "requested_treatment": requested_treatment,
                "research_relevance_reasons": ["family portrait reference"],
            }
        )
    queue = {
        "tasks": [
            {
                "task_id": "source-prep-batch:job-one:p0001",
                "queue": "source-prep-batches",
                "status": "todo",
                "source": "raw/sources/source.png",
                "source_sha256": "abc123",
                "job_manifest": "raw/codex-conversion-jobs/job-one/manifest.json",
                "job_id": "job-one",
                "title": "Named portrait source",
                "first_page": 1,
                "last_page": 1,
                "page_count": 1,
                "task_ids": ["source-prep:job-one:p0001"],
                "pages": [page],
            }
        ]
    }
    (queue_dir / "source-prep-batches.json").write_text(json.dumps(queue), encoding="utf-8")
    write_docling_unusable_entries(
        root,
        [
            {
                "task_id": "source-prep:job-one:p0001",
                "source_sha256": "abc123",
                "page": 1,
                "source": "raw/sources/source.png",
            }
        ],
    )


def write_audio_media_batch(root) -> None:
    queue_dir = root / "research" / "_agent-queues"
    queue_dir.mkdir(parents=True, exist_ok=True)
    page_dir = root / "raw" / "codex-conversion-jobs" / "audio-job"
    media_path = page_dir / "page-images" / "interview.m4a"
    media_path.parent.mkdir(parents=True, exist_ok=True)
    media_path.write_bytes(b"not real audio")
    queue = {
        "tasks": [
            {
                "task_id": "source-prep-batch:audio-job:p0001",
                "queue": "source-prep-batches",
                "status": "todo",
                "source": "raw/sources/interview.m4a",
                "source_sha256": "audio123",
                "job_manifest": "raw/codex-conversion-jobs/audio-job/manifest.json",
                "job_id": "audio-job",
                "title": "Oral history interview",
                "first_page": 1,
                "last_page": 1,
                "page_count": 1,
                "task_ids": ["source-prep:audio-job:p0001"],
                "pages": [
                    {
                        "page": 1,
                        "task_id": "source-prep:audio-job:p0001",
                        "page_image": "raw/codex-conversion-jobs/audio-job/page-images/interview.m4a",
                        "work_order": "raw/codex-conversion-jobs/audio-job/work-orders/page-0001.md",
                        "output_path": "raw/codex-conversion-jobs/audio-job/page-markdown/page-0001.md",
                        "image_output_dir": "raw/codex-conversion-jobs/audio-job/extracted-images/page-0001",
                    }
                ],
            }
        ]
    }
    (queue_dir / "source-prep-batches.json").write_text(json.dumps(queue), encoding="utf-8")


def write_parallel_test_batches(root, page_count: int = 2) -> None:
    queue_dir = root / "research" / "_agent-queues"
    queue_dir.mkdir(parents=True, exist_ok=True)
    page_dir = root / "raw" / "codex-conversion-jobs" / "job-one"
    pil_image = pytest.importorskip("PIL.Image")
    tasks = []
    for page_number in range(1, page_count + 1):
        page_image = page_dir / "page-images" / f"page-{page_number:04d}.png"
        image_output_dir = page_dir / "extracted-images" / f"page-{page_number:04d}"
        output_path = page_dir / "page-markdown" / f"page-{page_number:04d}.md"
        page_image.parent.mkdir(parents=True, exist_ok=True)
        image_output_dir.mkdir(parents=True, exist_ok=True)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        pil_image.new("RGB", (120, 80), color="white").save(page_image)
        page = {
            "page": page_number,
            "task_id": f"source-prep:job-one:p{page_number:04d}",
            "page_image": f"raw/codex-conversion-jobs/job-one/page-images/page-{page_number:04d}.png",
            "work_order": f"raw/codex-conversion-jobs/job-one/work-orders/page-{page_number:04d}.md",
            "output_path": f"raw/codex-conversion-jobs/job-one/page-markdown/page-{page_number:04d}.md",
            "image_output_dir": f"raw/codex-conversion-jobs/job-one/extracted-images/page-{page_number:04d}",
        }
        tasks.append(
            {
                "task_id": f"source-prep-batch:job-one:p{page_number:04d}",
                "queue": "source-prep-batches",
                "status": "todo",
                "source": "raw/sources/source.png",
                "source_sha256": f"abc123-{page_number}",
                "job_manifest": "raw/codex-conversion-jobs/job-one/manifest.json",
                "job_id": "job-one",
                "title": "Parallel source",
                "first_page": page_number,
                "last_page": page_number,
                "page_count": 1,
                "task_ids": [f"source-prep:job-one:p{page_number:04d}"],
                "pages": [page],
            }
        )
    (queue_dir / "source-prep-batches.json").write_text(json.dumps({"tasks": tasks}), encoding="utf-8")
    write_docling_unusable_entries(
        root,
        [
            {
                "task_id": f"source-prep:job-one:p{page_number:04d}",
                "source_sha256": f"abc123-{page_number}",
                "page": page_number,
                "source": "raw/sources/source.png",
            }
            for page_number in range(1, page_count + 1)
        ],
    )


def test_gemini_source_prep_skips_audio_for_media_pipeline(tmp_path, monkeypatch) -> None:
    write_audio_media_batch(tmp_path)

    def fail_gemini(**kwargs):
        raise AssertionError("audio/video media must not enter the document Gemini fallback")

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fail_gemini)

    summary = source_prep_gemini_run(tmp_path, limit=1, api_key="test-key", refresh_queue=False)

    assert summary["processed"] == 0
    assert summary["completed"] == 0
    assert summary["released"] == 0
    assert summary["skipped"] == 1
    assert summary["media_skipped"] == 1
    assert summary["tasks"][0]["reason"] == "audio_media_pipeline"


def test_gemini_source_prep_stops_on_fatal_dependency_blocker(tmp_path, monkeypatch) -> None:
    write_parallel_test_batches(tmp_path, page_count=3)
    calls = 0

    def fail_gemini(**kwargs):
        nonlocal calls
        calls += 1
        raise genealogy_wiki.GeminiSourcePrepFatalError(
            "Gemini HTTP 429: RESOURCE_EXHAUSTED prepayment credits are depleted"
        )

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fail_gemini)

    with pytest.raises(RuntimeError, match="Gemini source-prep fatal blocker"):
        source_prep_gemini_run(tmp_path, limit=3, parallelism=3, api_key="test-key", refresh_queue=False)

    state = json.loads(
        (tmp_path / "research" / "_automation" / "gemini-source-prep-state.json").read_text(encoding="utf-8")
    )
    task_state = json.loads(
        (tmp_path / "research" / "_agent-queues" / "task-state.json").read_text(encoding="utf-8")
    )

    assert calls == 1
    assert state["processed"] == 1
    assert state["released"] == 1
    assert state["skipped"] == 2
    assert "prepayment credits are depleted" in state["fatal_error"]
    assert state["tasks"][0]["reason"] == "fatal_gemini_dependency"
    assert [task["reason"] for task in state["tasks"][1:]] == [
        "gemini_fatal_dependency_unattempted",
        "gemini_fatal_dependency_unattempted",
    ]
    assert {task["status"] for task in task_state["tasks"].values()} == {"released"}


def test_gemini_source_prep_preflight_stops_before_page_claims(tmp_path, monkeypatch) -> None:
    write_parallel_test_batches(tmp_path, page_count=3)

    def fail_preflight(**kwargs):
        raise genealogy_wiki.GeminiSourcePrepFatalError(
            "Gemini HTTP 429: RESOURCE_EXHAUSTED prepayment credits are depleted"
        )

    def fail_page_call(**kwargs):
        raise AssertionError("page conversion should not run after fatal Gemini preflight")

    monkeypatch.setattr(genealogy_wiki, "preflight_gemini_source_prep_api", fail_preflight)
    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fail_page_call)

    with pytest.raises(RuntimeError, match="Gemini source-prep fatal blocker"):
        source_prep_gemini_run(
            tmp_path,
            limit=3,
            parallelism=3,
            api_key="test-key",
            refresh_queue=False,
            preflight_api=True,
        )

    state = json.loads(
        (tmp_path / "research" / "_automation" / "gemini-source-prep-state.json").read_text(encoding="utf-8")
    )
    task_state_path = tmp_path / "research" / "_agent-queues" / "task-state.json"

    assert state["processed"] == 0
    assert state["released"] == 0
    assert state["skipped"] == 0
    assert "prepayment credits are depleted" in state["fatal_error"]
    assert not task_state_path.exists()


def test_gemini_source_prep_preflight_only_does_not_process_pages(tmp_path, monkeypatch) -> None:
    write_parallel_test_batches(tmp_path, page_count=3)
    preflight_calls = 0

    def ok_preflight(**kwargs):
        nonlocal preflight_calls
        preflight_calls += 1
        return {"text": "OK", "finish_reason": "STOP", "usage": {}}

    def fail_page_call(**kwargs):
        raise AssertionError("preflight-only should not process queued pages")

    monkeypatch.setattr(genealogy_wiki, "preflight_gemini_source_prep_api", ok_preflight)
    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fail_page_call)

    summary = source_prep_gemini_run(
        tmp_path,
        limit=3,
        parallelism=3,
        api_key="test-key",
        refresh_queue=False,
        preflight_api=True,
        preflight_only=True,
    )

    task_state_path = tmp_path / "research" / "_agent-queues" / "task-state.json"

    assert preflight_calls == 1
    assert summary["processed"] == 0
    assert summary["completed"] == 0
    assert summary["released"] == 0
    assert summary["skipped"] == 0
    assert summary["preflight_only"] is True
    assert not task_state_path.exists()


def test_gemini_source_prep_preflight_falls_back_to_second_env_key(tmp_path, monkeypatch) -> None:
    write_parallel_test_batches(tmp_path, page_count=1)
    monkeypatch.setenv("GEMINI_API_KEY", "depleted-key")
    monkeypatch.setenv("GOOGLE_API_KEY", "funded-key")
    calls: list[str] = []

    def selective_preflight(**kwargs):
        calls.append(kwargs["api_key"])
        if kwargs["api_key"] == "depleted-key":
            raise genealogy_wiki.GeminiSourcePrepFatalError(
                "Gemini HTTP 429: RESOURCE_EXHAUSTED prepayment credits are depleted"
            )
        return {"text": "OK", "finish_reason": "STOP", "usage": {}}

    monkeypatch.setattr(genealogy_wiki, "preflight_gemini_source_prep_api", selective_preflight)

    summary = source_prep_gemini_run(
        tmp_path,
        limit=1,
        refresh_queue=False,
        preflight_api=True,
        preflight_only=True,
        preflight_success_state=False,
    )

    assert calls == ["depleted-key", "funded-key"]
    assert summary["api_key_source"] == "GOOGLE_API_KEY"
    assert summary["api_key_candidates"] == ["GEMINI_API_KEY", "GOOGLE_API_KEY"]
    assert summary["preflight_only"] is True


def test_gemini_source_prep_conversion_uses_working_env_key_after_preflight(tmp_path, monkeypatch) -> None:
    write_test_batch(tmp_path)
    monkeypatch.setenv("GEMINI_API_KEY", "depleted-key")
    monkeypatch.setenv("GOOGLE_API_KEY", "funded-key")

    def selective_preflight(**kwargs):
        if kwargs["api_key"] == "depleted-key":
            raise genealogy_wiki.GeminiSourcePrepFatalError(
                "Gemini HTTP 429: RESOURCE_EXHAUSTED prepayment credits are depleted"
            )
        return {"text": "OK", "finish_reason": "STOP", "usage": {}}

    def fake_gemini(**kwargs):
        assert kwargs["api_key"] == "funded-key"
        return {
            "text": complete_gemini_markdown(json.dumps({"visual_regions": []})),
            "finish_reason": "STOP",
            "usage": {},
        }

    monkeypatch.setattr(genealogy_wiki, "preflight_gemini_source_prep_api", selective_preflight)
    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fake_gemini)

    summary = source_prep_gemini_run(tmp_path, limit=1, refresh_queue=False)

    assert summary["api_key_source"] == "GOOGLE_API_KEY"
    assert summary["completed"] == 1
    assert summary["released"] == 0


def test_gemini_source_prep_preflight_success_can_skip_state_write(tmp_path, monkeypatch) -> None:
    write_parallel_test_batches(tmp_path, page_count=1)

    def ok_preflight(**kwargs):
        return {"text": "OK", "finish_reason": "STOP", "usage": {}}

    monkeypatch.setattr(genealogy_wiki, "preflight_gemini_source_prep_api", ok_preflight)

    summary = source_prep_gemini_run(
        tmp_path,
        limit=1,
        api_key="test-key",
        refresh_queue=False,
        preflight_api=True,
        preflight_only=True,
        preflight_success_state=False,
    )

    assert summary["preflight_only"] is True
    assert "state_path" not in summary
    assert "preflight_state_path" in summary
    assert not (tmp_path / "research" / "_automation" / "gemini-source-prep-state.json").exists()
    preflight_state = json.loads(
        (tmp_path / "research" / "_automation" / "gemini-source-prep-preflight-state.json").read_text(
            encoding="utf-8"
        )
    )
    assert preflight_state["preflight_only"] is True
    assert preflight_state["fatal_error"] == ""


def test_gemini_source_prep_dry_run_does_not_write_state_or_log(tmp_path) -> None:
    write_test_batch(tmp_path)

    summary = source_prep_gemini_run(tmp_path, limit=1, dry_run=True, refresh_queue=False)

    assert summary["dry_run"] is True
    assert summary["processed"] == 1
    assert "state_path" not in summary
    assert not (tmp_path / "research" / "_automation" / "gemini-source-prep-state.json").exists()
    assert not (tmp_path / "research" / "log.md").exists()


def test_gemini_preflight_only_fatal_preserves_last_conversion_state(tmp_path, monkeypatch) -> None:
    write_parallel_test_batches(tmp_path, page_count=1)
    automation = tmp_path / "research" / "_automation"
    automation.mkdir(parents=True, exist_ok=True)
    main_state_path = automation / "gemini-source-prep-state.json"
    main_state_path.write_text(
        json.dumps({"completed": 2233, "fatal_error": "", "mode": "gemini-source-prep"}),
        encoding="utf-8",
    )
    original_state = main_state_path.read_text(encoding="utf-8")

    def fail_preflight(**kwargs):
        raise genealogy_wiki.GeminiSourcePrepFatalError(
            "Gemini HTTP 429: RESOURCE_EXHAUSTED prepayment credits are depleted"
        )

    monkeypatch.setattr(genealogy_wiki, "preflight_gemini_source_prep_api", fail_preflight)

    with pytest.raises(genealogy_wiki.GeminiSourcePrepFatalError):
        source_prep_gemini_run(
            tmp_path,
            limit=1,
            api_key="test-key",
            refresh_queue=False,
            preflight_api=True,
            preflight_only=True,
            preflight_success_state=False,
        )

    assert main_state_path.read_text(encoding="utf-8") == original_state
    preflight_state = json.loads((automation / "gemini-source-prep-preflight-state.json").read_text(encoding="utf-8"))
    assert preflight_state["preflight_only"] is True
    assert "prepayment credits are depleted" in preflight_state["fatal_error"]


def test_gemini_visual_manifest_creates_crop_and_metadata(tmp_path, monkeypatch) -> None:
    write_test_batch(tmp_path)

    def fake_gemini(**kwargs):
        assert "Visual Region Manifest" in kwargs["prompt"]
        assert "Do not create crop boxes for marginal numbers" in kwargs["prompt"]
        return {
            "text": complete_gemini_markdown(
                json.dumps(
                    {
                        "visual_regions": [
                            {
                                "region_id": "portrait-1",
                                "kind": "portrait",
                                "bbox_pct": [10, 20, 40, 70],
                                "caption_literal": "DARIO PULGAR SMITH",
                                "caption_type": "source-field",
                                "identity_basis": "named identity card field",
                                "source_context": "The same card names DARIO PULGAR SMITH.",
                                "confidence": "high",
                                "suggested_filename": "portrait-dario-pulgar-smith.png",
                                "inline_anchor": "Images, Captions, And Visual Notes",
                            }
                        ]
                    }
                )
            ),
            "finish_reason": "STOP",
            "usage": {"promptTokenCount": 10, "candidatesTokenCount": 20, "totalTokenCount": 30},
        }

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fake_gemini)

    summary = source_prep_gemini_run(tmp_path, limit=1, api_key="test-key", refresh_queue=False)

    output_path = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "page-markdown" / "page-0001.md"
    visuals_path = output_path.with_suffix(".visuals.json")
    crop_path = (
        tmp_path
        / "raw"
        / "codex-conversion-jobs"
        / "job-one"
        / "extracted-images"
        / "page-0001"
        / "page-0001-image-01-portrait-dario-pulgar-smith.png"
    )

    assert summary["completed"] == 1
    assert summary["visual_regions"]["cropped"] == 1
    assert visuals_path.exists()
    assert crop_path.exists()
    assert "Pipeline-extracted visual crops" in output_path.read_text(encoding="utf-8")
    manifest = json.loads(visuals_path.read_text(encoding="utf-8"))
    assert manifest["visual_regions"][0]["caption_type"] == "source-field"
    assert manifest["visual_regions"][0]["crop_path_rel"] == (
        "raw/codex-conversion-jobs/job-one/extracted-images/page-0001/"
        "page-0001-image-01-portrait-dario-pulgar-smith.png"
    )


def test_gemini_visual_manifest_skips_low_value_crop_regions(tmp_path, monkeypatch) -> None:
    write_test_batch(tmp_path)

    def fake_gemini(**kwargs):
        return {
            "text": complete_gemini_markdown(
                json.dumps(
                    {
                        "visual_regions": [
                            {
                                "region_id": "margin-1",
                                "kind": "handwritten_marginalia",
                                "bbox_pct": [1, 1, 8, 20],
                                "caption_literal": "2",
                                "caption_type": "converter-description",
                                "source_context": "Small marginal filing number.",
                                "confidence": "high",
                                "suggested_filename": "page-0001-margin-number.png",
                            }
                        ]
                    }
                )
            ),
            "finish_reason": "STOP",
            "usage": {},
        }

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fake_gemini)

    summary = source_prep_gemini_run(tmp_path, limit=1, api_key="test-key", refresh_queue=False)

    output_path = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "page-markdown" / "page-0001.md"
    visuals_path = output_path.with_suffix(".visuals.json")
    crop_dir = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "extracted-images" / "page-0001"

    assert summary["completed"] == 1
    assert summary["visual_regions"]["declared"] == 1
    assert summary["visual_regions"]["cropped"] == 0
    assert summary["visual_regions"]["skipped"] == 1
    assert not list(crop_dir.glob("page-0001-image-*.png"))
    assert "Pipeline-extracted visual crops" not in output_path.read_text(encoding="utf-8")
    manifest = json.loads(visuals_path.read_text(encoding="utf-8"))
    assert manifest["visual_regions"] == []
    assert manifest["skipped_regions"][0]["reason"] == "low_value_visual_region_not_saved"


def test_pro_with_crops_releases_when_visual_manifest_missing(tmp_path, monkeypatch) -> None:
    write_test_batch(tmp_path, requested_treatment="pro_with_crops")

    def fake_gemini(**kwargs):
        return {
            "text": complete_gemini_markdown('{"not_visual_regions": []}').replace("## Visual Region Manifest", "## Gemini Notes"),
            "finish_reason": "STOP",
            "usage": {},
        }

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fake_gemini)

    summary = source_prep_gemini_run(tmp_path, limit=1, api_key="test-key", refresh_queue=False)

    assert summary["completed"] == 0
    assert summary["released"] == 1
    assert summary["tasks"][0]["reason"] == "visual_crop_extraction_failed"
    assert "visual_region_manifest_missing" in summary["tasks"][0]["error"]


def test_gemini_source_prep_parallelism_completes_independent_pages(tmp_path, monkeypatch) -> None:
    write_parallel_test_batches(tmp_path, page_count=2)

    def fake_gemini(**kwargs):
        return {
            "text": complete_gemini_markdown('{"visual_regions": [], "no_visual_regions_reason": "text only"}'),
            "finish_reason": "STOP",
            "usage": {"promptTokenCount": 1, "candidatesTokenCount": 2, "totalTokenCount": 3},
        }

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fake_gemini)

    summary = source_prep_gemini_run(tmp_path, limit=2, parallelism=2, api_key="test-key", refresh_queue=False)

    assert summary["parallelism"] == 2
    assert summary["processed"] == 2
    assert summary["completed"] == 2
    assert summary["usage"]["total_tokens"] == 6
    for page_number in (1, 2):
        assert (
            tmp_path
            / "raw"
            / "codex-conversion-jobs"
            / "job-one"
            / "page-markdown"
            / f"page-{page_number:04d}.md"
        ).exists()
    task_state = json.loads((tmp_path / "research" / "_agent-queues" / "task-state.json").read_text(encoding="utf-8"))
    assert task_state["tasks"]["source-prep:job-one:p0001"]["status"] == "done"
    assert task_state["tasks"]["source-prep:job-one:p0002"]["status"] == "done"


def test_gemini_flash_max_tokens_retries_next_as_pro(tmp_path, monkeypatch) -> None:
    write_test_batch(tmp_path)

    def fake_gemini(**kwargs):
        assert kwargs["model"] == "gemini-2.5-flash"
        assert kwargs["max_output_tokens"] == 65536
        assert kwargs["thinking_budget"] == 0
        return {
            "text": "",
            "finish_reason": "MAX_TOKENS",
            "usage": {
                "promptTokenCount": 1000,
                "candidatesTokenCount": 64000,
                "thoughtsTokenCount": 500,
                "totalTokenCount": 65500,
            },
        }

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fake_gemini)

    summary = source_prep_gemini_run(tmp_path, limit=1, api_key="test-key", refresh_queue=False)

    assert summary["completed"] == 0
    assert summary["released"] == 1
    assert summary["failed"] == 0
    assert summary["usage"]["thoughts_tokens"] == 500
    assert summary["tasks"][0]["reason"] == "max_tokens_retry_pro"
    task_state = json.loads((tmp_path / "research" / "_agent-queues" / "task-state.json").read_text(encoding="utf-8"))
    state = task_state["tasks"]["source-prep:job-one:p0001"]
    assert state["status"] == "released"
    assert "Flash hit max tokens" in state["note"]

    plan = source_prep_gemini_run(tmp_path, limit=1, dry_run=True, refresh_queue=False)

    assert plan["processed"] == 1
    assert plan["tasks"][0]["route"]["tier"] == "pro"
    assert plan["tasks"][0]["route"]["model"] == "gemini-2.5-pro"
    assert "prior_max_tokens" in plan["tasks"][0]["route"]["reasons"]


def test_gemini_pro_max_tokens_holds_for_region_split(tmp_path, monkeypatch) -> None:
    write_test_batch(tmp_path)
    genealogy_wiki.update_agent_task_state(
        tmp_path,
        "source-prep:job-one:p0001",
        "released",
        agent="gemini-source-prep",
        note="Gemini Flash hit max tokens; retry once with Pro and the full output budget.",
    )

    def fake_gemini(**kwargs):
        assert kwargs["model"] == "gemini-2.5-pro"
        assert kwargs["max_output_tokens"] == 65536
        assert kwargs["thinking_budget"] is None
        return {
            "text": "",
            "finish_reason": "MAX_TOKENS",
            "usage": {
                "promptTokenCount": 1000,
                "candidatesTokenCount": 64000,
                "thoughtsTokenCount": 500,
                "totalTokenCount": 65500,
            },
        }

    monkeypatch.setattr(genealogy_wiki, "call_gemini_generate_content", fake_gemini)

    summary = source_prep_gemini_run(tmp_path, limit=1, api_key="test-key", refresh_queue=False)

    assert summary["completed"] == 0
    assert summary["released"] == 0
    assert summary["failed"] == 1
    assert summary["tasks"][0]["route"]["tier"] == "pro"
    assert summary["tasks"][0]["reason"] == "max_tokens_requires_region_split"
    task_state = json.loads((tmp_path / "research" / "_agent-queues" / "task-state.json").read_text(encoding="utf-8"))
    state = task_state["tasks"]["source-prep:job-one:p0001"]
    assert state["status"] == "failed"
    assert "page-region splitting" in state["note"]


def test_gemini_source_prep_ignores_local_env_file(tmp_path, monkeypatch) -> None:
    write_test_batch(tmp_path)
    (tmp_path / ".env").write_text("GEMINI_API_KEY=local-only-key\n", encoding="utf-8")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="cloud automation environment"):
        source_prep_gemini_run(tmp_path, limit=1, refresh_queue=False)


def test_gemini_route_ignores_converter_family_relevance_without_research_feedback(tmp_path) -> None:
    batch = {
        "source": "raw/sources/source.pdf",
        "title": "Simple printed page",
        "first_page": 1,
        "family_relevance": "critical",
        "matched_terms": ["Pulgar"],
        "pages": [
            {
                "page": 1,
                "family_relevance": "critical",
                "matched_terms": ["Pulgar"],
                "page_image": "raw/codex-conversion-jobs/job-one/page-images/page-0001.jpg",
            }
        ],
    }

    route = genealogy_wiki.classify_gemini_source_prep_batch(tmp_path, batch)

    assert route["tier"] == "lite"
    assert route["model"] == "gemini-2.5-flash"
    assert route["use_crops"] is False
    assert route["relevant"] is False


def test_gemini_route_starts_blank_or_encoding_failures_on_flash(tmp_path) -> None:
    batch = {
        "source": "raw/sources/source.pdf",
        "title": "Blank separator page",
        "first_page": 1,
        "rough_discovery_flags": [
            "insufficient_text",
            "insufficient_alpha_text",
            "insufficient_words",
            "encoding_mojibake",
        ],
        "pages": [
            {
                "page": 1,
                "page_image": "raw/codex-conversion-jobs/job-one/page-images/page-0001.jpg",
            }
        ],
    }

    route = genealogy_wiki.classify_gemini_source_prep_batch(tmp_path, batch)

    assert route["tier"] == "lite"
    assert route["model"] == "gemini-2.5-flash"
    assert route["use_crops"] is False
    assert route["complex"] is False


def test_gemini_route_uses_explicit_research_feedback_for_expensive_treatment(tmp_path) -> None:
    batch = {
        "source": "raw/sources/source.pdf",
        "title": "Simple printed page",
        "first_page": 1,
        "pages": [
            {
                "page": 1,
                "research_relevance": "high",
                "requested_treatment": "pro_with_crops",
                "page_image": "raw/codex-conversion-jobs/job-one/page-images/page-0001.jpg",
            }
        ],
    }

    route = genealogy_wiki.classify_gemini_source_prep_batch(tmp_path, batch)

    assert route["tier"] == "pro_with_crops"
    assert route["use_crops"] is True
    assert route["relevant"] is True


def test_gemini_route_honors_explicit_pro_without_crops(tmp_path) -> None:
    batch = {
        "source": "raw/sources/source.pdf",
        "title": "Simple printed page",
        "first_page": 1,
        "pages": [
            {
                "page": 1,
                "research_relevance": "high",
                "requested_treatment": "pro",
                "page_image": "raw/codex-conversion-jobs/job-one/page-images/page-0001.jpg",
            }
        ],
    }

    route = genealogy_wiki.classify_gemini_source_prep_batch(tmp_path, batch)

    assert route["tier"] == "pro"
    assert route["model"] == "gemini-2.5-pro"
    assert route["use_crops"] is False
    assert route["complex"] is True


def test_gemini_route_uses_technical_failure_for_pro_without_crops(tmp_path) -> None:
    batch = {
        "source": "raw/sources/source.pdf",
        "title": "Simple printed page",
        "first_page": 1,
        "quality_flags": ["ocr_garbage"],
        "pages": [
            {
                "page": 1,
                "page_image": "raw/codex-conversion-jobs/job-one/page-images/page-0001.jpg",
            }
        ],
    }

    route = genealogy_wiki.classify_gemini_source_prep_batch(tmp_path, batch)

    assert route["tier"] == "pro"
    assert route["use_crops"] is False
    assert route["complex"] is True
