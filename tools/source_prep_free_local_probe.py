"""Isolated no-API probe for source-prep baseline conversion quality.

This tool intentionally avoids the live source-prep queues and Gemini routes.
It compares free/local extractors on synthetic pages and, when present, restored
page images from conversion jobs. It writes only the requested report files.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
import time
from pathlib import Path


DEFAULT_DOC_TIMEOUT_SECONDS = 45.0
PREVIEW_CHARS = 500


def repo_imports(root: Path) -> None:
    src = root / "src"
    if str(src) not in sys.path:
        sys.path.insert(0, str(src))


def dependency_report() -> dict[str, object]:
    report: dict[str, object] = {}
    for module in ("fitz", "PIL", "docling", "easyocr", "pdfplumber", "pytesseract"):
        try:
            __import__(module)
            report[module] = True
        except Exception:
            report[module] = False
    report["tesseract_binary"] = bool(shutil.which("tesseract"))
    return report


def profile_markdown(root: Path, markdown: str) -> dict[str, object]:
    repo_imports(root)
    from historic_doc_ingest.genealogy_wiki import profile_source_prep_discovery_markdown

    return profile_source_prep_discovery_markdown(markdown)


def text_result(
    *,
    root: Path,
    method: str,
    seconds: float,
    text: str,
    error: str | None = None,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    profile = profile_markdown(root, text)
    result: dict[str, object] = {
        "method": method,
        "seconds": round(seconds, 3),
        "status": profile.get("status"),
        "text_chars": profile.get("text_chars"),
        "alpha_chars": profile.get("alpha_chars"),
        "word_count": profile.get("word_count"),
        "line_count": profile.get("line_count"),
        "short_line_ratio": profile.get("short_line_ratio"),
        "readability_flags": profile.get("readability_flags", []),
        "error": error or "",
        "preview": text.strip()[:PREVIEW_CHARS],
    }
    if extra:
        result.update(extra)
    return result


def error_result(*, root: Path, method: str, seconds: float, error: str) -> dict[str, object]:
    result = text_result(root=root, method=method, seconds=seconds, text="", error=error)
    result["status"] = "error"
    return result


def run_pymupdf_text(root: Path, pdf_path: Path) -> dict[str, object]:
    start = time.perf_counter()
    try:
        import fitz

        page_count = 0
        image_count = 0
        parts: list[str] = []
        with fitz.open(pdf_path) as doc:
            page_count = len(doc)
            for page in doc:
                parts.append(page.get_text("text") or "")
                image_count += len(page.get_images(full=True))
        seconds = time.perf_counter() - start
        return text_result(
            root=root,
            method="pymupdf_text",
            seconds=seconds,
            text="\n\n".join(parts),
            extra={"page_count": page_count, "embedded_image_count": image_count},
        )
    except Exception as exc:
        return error_result(root=root, method="pymupdf_text", seconds=time.perf_counter() - start, error=str(exc))


def run_pdfplumber_text(root: Path, pdf_path: Path) -> dict[str, object]:
    start = time.perf_counter()
    try:
        import pdfplumber

        parts: list[str] = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                parts.append(page.extract_text(x_tolerance=1, y_tolerance=3) or "")
        seconds = time.perf_counter() - start
        return text_result(root=root, method="pdfplumber_text", seconds=seconds, text="\n\n".join(parts))
    except Exception as exc:
        return error_result(root=root, method="pdfplumber_text", seconds=time.perf_counter() - start, error=str(exc))


def run_docling_pdf(
    root: Path,
    pdf_path: Path,
    *,
    use_ocr: bool,
    table_structure: bool,
    document_timeout: float,
) -> dict[str, object]:
    start = time.perf_counter()
    method = f"docling_ocr_{'on' if use_ocr else 'off'}_tables_{'on' if table_structure else 'off'}"
    try:
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions
        from docling.document_converter import DocumentConverter, PdfFormatOption

        pipeline_options = PdfPipelineOptions()
        pipeline_options.document_timeout = document_timeout
        if hasattr(pipeline_options, "do_ocr"):
            pipeline_options.do_ocr = use_ocr
        pipeline_options.do_table_structure = table_structure
        pipeline_options.do_picture_description = False
        pipeline_options.do_picture_classification = False
        pipeline_options.do_formula_enrichment = False
        pipeline_options.do_code_enrichment = False
        pipeline_options.generate_page_images = True
        pipeline_options.generate_picture_images = True
        pipeline_options.images_scale = 2.0
        if hasattr(pipeline_options, "do_chart_extraction"):
            pipeline_options.do_chart_extraction = False

        converter = DocumentConverter(
            format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
        )
        result = converter.convert(str(pdf_path), max_num_pages=1)
        document = getattr(result, "document", None)
        if document is None:
            raise RuntimeError("Docling returned no document.")
        markdown = str(document.export_to_markdown()).strip()
        seconds = time.perf_counter() - start
        return text_result(
            root=root,
            method=method,
            seconds=seconds,
            text=markdown,
            extra={
                "picture_count": len(getattr(document, "pictures", []) or []),
                "table_count": len(getattr(document, "tables", []) or []),
            },
        )
    except Exception as exc:
        return error_result(root=root, method=method, seconds=time.perf_counter() - start, error=str(exc))


def create_native_pdf(path: Path) -> None:
    import fitz

    doc = fitz.open()
    page = doc.new_page(width=612, height=792)
    title = "Dario Arturo Pulgar - native text source-prep sample"
    body = (
        "This born-digital page has selectable text, dates, places, and a small table. "
        "A free native-text extractor should accept it without OCR or any Gemini call."
    )
    page.insert_textbox(fitz.Rect(54, 54, 558, 90), title, fontsize=14)
    page.insert_textbox(fitz.Rect(54, 105, 558, 165), body, fontsize=11)
    y = 205
    headers = ["Year", "Place", "Role"]
    rows = [
        ["1972", "Santiago, Chile", "Producer"],
        ["1978", "Montreal, Canada", "Audio Visual Consultant"],
        ["1982", "Nairobi, Kenya", "Development Support Communications Officer"],
    ]
    xs = [54, 130, 300, 558]
    for x in xs:
        page.draw_line(fitz.Point(x, y), fitz.Point(x, y + 96))
    for row_y in (y, y + 24, y + 48, y + 72, y + 96):
        page.draw_line(fitz.Point(54, row_y), fitz.Point(558, row_y))
    for index, header in enumerate(headers):
        page.insert_text((xs[index] + 6, y + 17), header, fontsize=10)
    for row_index, row in enumerate(rows, start=1):
        for col_index, cell in enumerate(row):
            page.insert_text((xs[col_index] + 6, y + 24 * row_index + 17), cell, fontsize=9)
    doc.save(path)
    doc.close()


def create_scanned_pdf(path: Path) -> None:
    import fitz
    from PIL import Image, ImageDraw, ImageFont

    image = Image.new("RGB", (1400, 1800), "white")
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 44)
        small = ImageFont.truetype("arial.ttf", 34)
    except Exception:
        font = ImageFont.load_default()
        small = font
    draw.text((110, 90), "Scanned page source-prep sample", fill="black", font=font)
    lines = [
        "Dario Arturo Pulgar appears in a printed paragraph.",
        "The page includes a date, a place, and a non-text visual block.",
        "This sample should require local OCR before any Gemini fallback.",
        "If the OCR layer is weak, the pipeline can hold it for later review.",
    ]
    y = 210
    for line in lines:
        draw.text((110, y), line, fill="black", font=small)
        y += 72
    draw.rectangle((110, 610, 610, 1000), outline="black", width=5, fill=(225, 225, 225))
    draw.text((165, 775), "embedded photo area", fill="black", font=small)
    png_path = path.with_suffix(".png")
    image.save(png_path)
    doc = fitz.open()
    page = doc.new_page(width=612, height=792)
    page.insert_image(page.rect, filename=str(png_path))
    doc.save(path)
    doc.close()


def wrap_image_as_pdf(image_path: Path, pdf_path: Path) -> None:
    import fitz
    from PIL import Image

    with Image.open(image_path) as image:
        width, height = image.size
    doc = fitz.open()
    page = doc.new_page(width=width, height=height)
    page.insert_image(page.rect, filename=str(image_path))
    doc.save(pdf_path)
    doc.close()


def restored_page_image_samples(root: Path, limit: int) -> list[dict[str, object]]:
    if limit <= 0:
        return []
    samples: list[dict[str, object]] = []
    job_root = root / "raw" / "codex-conversion-jobs"
    if not job_root.exists():
        return samples
    patterns = ("*/page-images/page-*.jpg", "*/page-images/page-*.jpeg", "*/page-images/page-*.png")
    for pattern in patterns:
        for image_path in sorted(job_root.glob(pattern)):
            samples.append({"sample_id": f"restored:{image_path.parent.parent.name}:{image_path.stem}", "image_path": image_path})
            if len(samples) >= limit:
                return samples
    return samples


def run_sample(
    root: Path,
    sample: dict[str, object],
    *,
    work_dir: Path,
    document_timeout: float,
    skip_docling: bool,
) -> dict[str, object]:
    sample_id = str(sample["sample_id"])
    pdf_path = sample.get("pdf_path")
    if pdf_path is None:
        image_path = Path(str(sample["image_path"]))
        pdf_path = work_dir / f"{sample_id.replace(':', '_')}.pdf"
        wrap_image_as_pdf(image_path, pdf_path)
    pdf = Path(str(pdf_path))
    methods = [run_pymupdf_text(root, pdf), run_pdfplumber_text(root, pdf)]
    if not skip_docling:
        methods.extend(
            [
                run_docling_pdf(
                    root,
                    pdf,
                    use_ocr=False,
                    table_structure=False,
                    document_timeout=document_timeout,
                ),
                run_docling_pdf(
                    root,
                    pdf,
                    use_ocr=True,
                    table_structure=False,
                    document_timeout=document_timeout,
                ),
                run_docling_pdf(
                    root,
                    pdf,
                    use_ocr=True,
                    table_structure=True,
                    document_timeout=document_timeout,
                ),
            ]
        )
    return {
        "sample_id": sample_id,
        "kind": sample.get("kind", "restored_page_image"),
        "source": str(sample.get("source", sample.get("image_path", ""))),
        "methods": methods,
    }


def build_report(
    *,
    root: Path,
    sample_limit: int,
    document_timeout: float,
    skip_docling: bool,
) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="source-prep-free-probe-") as temp:
        work_dir = Path(temp)
        native_pdf = work_dir / "synthetic-native.pdf"
        scanned_pdf = work_dir / "synthetic-scanned.pdf"
        create_native_pdf(native_pdf)
        create_scanned_pdf(scanned_pdf)
        samples: list[dict[str, object]] = [
            {
                "sample_id": "synthetic_native_pdf",
                "kind": "synthetic_native_pdf",
                "source": "generated locally",
                "pdf_path": native_pdf,
            },
            {
                "sample_id": "synthetic_scanned_pdf",
                "kind": "synthetic_scanned_pdf",
                "source": "generated locally",
                "pdf_path": scanned_pdf,
            },
        ]
        samples.extend(restored_page_image_samples(root, sample_limit))
        results = [
            run_sample(root, sample, work_dir=work_dir, document_timeout=document_timeout, skip_docling=skip_docling)
            for sample in samples
        ]
    return {
        "purpose": "isolated no-api comparison of free/local source-prep extraction layers",
        "mutates_live_pipeline": False,
        "api_credit_usage": "none",
        "dependencies": dependency_report(),
        "settings": {
            "sample_limit": sample_limit,
            "document_timeout": document_timeout,
            "skip_docling": skip_docling,
        },
        "samples": results,
        "recommendations": summarize_recommendations(results),
    }


def summarize_recommendations(samples: list[dict[str, object]]) -> list[str]:
    recs: list[str] = []
    native = next((sample for sample in samples if sample.get("sample_id") == "synthetic_native_pdf"), None)
    scanned = next((sample for sample in samples if sample.get("sample_id") == "synthetic_scanned_pdf"), None)
    if native and any(
        method.get("method") == "pymupdf_text" and method.get("status") == "rough_ok"
        for method in native.get("methods", [])
    ):
        recs.append("Use PyMuPDF native-text extraction as a zero-token fastlane before OCR for born-digital PDFs.")
    if scanned and any(
        str(method.get("method", "")).startswith("docling_ocr_on") and method.get("status") == "rough_ok"
        for method in scanned.get("methods", [])
    ):
        recs.append("Use Docling OCR as the main free scanned-page layer before any Gemini fallback.")
    if scanned and not any(
        str(method.get("method", "")).startswith("docling_ocr_on") and method.get("status") == "rough_ok"
        for method in scanned.get("methods", [])
    ):
        recs.append("Treat Docling OCR failures as technical uncertainty, not automatic Pro escalation; route simple blanks and low-content scans to cheap validation first.")
    table_wins = False
    for sample in samples:
        methods = {method.get("method"): method for method in sample.get("methods", [])}
        plain = methods.get("docling_ocr_on_tables_off")
        tables = methods.get("docling_ocr_on_tables_on")
        if plain and tables and tables.get("status") == "rough_ok":
            if int(tables.get("word_count") or 0) >= int(plain.get("word_count") or 0):
                table_wins = True
    if table_wins:
        recs.append("Keep a measured table-structure Docling variant available for tabular pages before spending Gemini tokens.")
    return recs


def write_markdown(report: dict[str, object], path: Path) -> None:
    lines = [
        "# Free Local Source-Prep Probe",
        "",
        "This report is generated by `tools/source_prep_free_local_probe.py`.",
        "It does not mutate source-prep queues and does not call Gemini or any paid API.",
        "",
        "## Dependencies",
        "",
    ]
    for key, value in sorted(dict(report.get("dependencies", {})).items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Recommendations", ""])
    for rec in report.get("recommendations", []):
        lines.append(f"- {rec}")
    lines.extend(["", "## Samples", ""])
    for sample in report.get("samples", []):
        lines.append(f"### {sample.get('sample_id')}")
        lines.append("")
        lines.append(f"- Kind: `{sample.get('kind')}`")
        lines.append(f"- Source: `{sample.get('source')}`")
        lines.append("")
        lines.append("| Method | Status | Words | Text chars | Flags | Seconds | Pictures | Tables | Error |")
        lines.append("| --- | --- | ---: | ---: | --- | ---: | ---: | ---: | --- |")
        for method in sample.get("methods", []):
            flags = ", ".join(str(flag) for flag in method.get("readability_flags", []))
            error = str(method.get("error", "")).replace("|", "\\|")
            lines.append(
                "| {method} | {status} | {words} | {chars} | {flags} | {seconds} | {pictures} | {tables} | {error} |".format(
                    method=method.get("method"),
                    status=method.get("status"),
                    words=method.get("word_count"),
                    chars=method.get("text_chars"),
                    flags=flags or "none",
                    seconds=method.get("seconds"),
                    pictures=method.get("picture_count", method.get("embedded_image_count", "")),
                    tables=method.get("table_count", ""),
                    error=error,
                )
            )
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Repository root.")
    parser.add_argument("--sample-limit", type=int, default=3, help="Restored page images to include when present.")
    parser.add_argument("--document-timeout", type=float, default=DEFAULT_DOC_TIMEOUT_SECONDS)
    parser.add_argument("--skip-docling", action="store_true", help="Skip Docling runs for fast unit/smoke tests.")
    parser.add_argument("--out-json", type=Path, default=Path("docs/source-prep-free-local-probe.json"))
    parser.add_argument("--out-md", type=Path, default=Path("docs/source-prep-free-local-probe.md"))
    args = parser.parse_args(argv)

    root = args.root.resolve()
    report = build_report(
        root=root,
        sample_limit=max(args.sample_limit, 0),
        document_timeout=args.document_timeout,
        skip_docling=args.skip_docling,
    )
    out_json = (root / args.out_json).resolve() if not args.out_json.is_absolute() else args.out_json
    out_md = (root / args.out_md).resolve() if not args.out_md.is_absolute() else args.out_md
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(report, out_md)
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
