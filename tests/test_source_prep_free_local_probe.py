from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


def load_probe_module():
    repo_root = Path(__file__).resolve().parents[1]
    probe_path = repo_root / "tools" / "source_prep_free_local_probe.py"
    spec = importlib.util.spec_from_file_location("source_prep_free_local_probe", probe_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_free_local_probe_smoke_accepts_native_text_and_rejects_image_without_ocr() -> None:
    pytest.importorskip("fitz")
    pytest.importorskip("PIL")
    pytest.importorskip("pdfplumber")
    probe = load_probe_module()
    repo_root = Path(__file__).resolve().parents[1]

    report = probe.build_report(
        root=repo_root,
        sample_limit=0,
        document_timeout=5,
        skip_docling=True,
    )

    assert report["api_credit_usage"] == "none"
    assert report["mutates_live_pipeline"] is False
    samples = {sample["sample_id"]: sample for sample in report["samples"]}
    native_methods = {method["method"]: method for method in samples["synthetic_native_pdf"]["methods"]}
    scanned_methods = {method["method"]: method for method in samples["synthetic_scanned_pdf"]["methods"]}
    assert native_methods["pymupdf_text"]["status"] == "rough_ok"
    assert native_methods["pdfplumber_text"]["status"] == "rough_ok"
    assert scanned_methods["pymupdf_text"]["status"] == "rough_unusable"
    assert scanned_methods["pdfplumber_text"]["status"] == "rough_unusable"
