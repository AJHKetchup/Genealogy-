import json

import pytest

from historic_doc_ingest import genealogy_wiki
from historic_doc_ingest.genealogy_wiki import source_prep_gemini_run


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
    assert route["use_crops"] is False
    assert route["relevant"] is False


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
