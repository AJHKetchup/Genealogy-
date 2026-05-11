from __future__ import annotations

import argparse
from pathlib import Path

from historic_doc_ingest.pipeline import IngestOptions, ingest_pdf


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert image-based historical PDFs into Markdown plus an audit manifest."
    )
    parser.add_argument("pdf", type=Path, help="Path to a PDF document.")
    parser.add_argument("--out", type=Path, required=True, help="Output directory.")
    parser.add_argument("--dpi", type=int, default=400, help="Page render DPI. Default: 400.")
    parser.add_argument("--ocr-lang", default="eng", help="Tesseract language code. Default: eng.")
    parser.add_argument("--no-ocr", action="store_true", help="Render and extract PDF layer data without OCR.")
    parser.add_argument(
        "--ignore-pdf-text-layer",
        action="store_true",
        help="Force OCR even when a PDF text layer exists.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    options = IngestOptions(
        dpi=args.dpi,
        ocr_language=args.ocr_lang,
        use_ocr=not args.no_ocr,
        prefer_pdf_text_layer=not args.ignore_pdf_text_layer,
    )
    document = ingest_pdf(args.pdf, args.out, options)
    print(f"Wrote {args.out / 'document.md'}")
    print(f"Wrote {args.out / 'manifest.json'}")
    warnings = document.metadata.get("warnings", [])
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
