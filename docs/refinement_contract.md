# Page Refinement Contract

Use this contract for a vision-capable LLM, HTR system, or document AI service that reviews rendered page images and the first-pass manifest.

## Input

Send the provider:

- The rendered page image from `assets/pages/page-0001.png`.
- The matching page object from `manifest.json`.
- Any extracted image-region assets from `assets/images/`.

## Instruction Template

```text
You are correcting a historical document transcription.

Preserve the page's reading order, section hierarchy, page number, image positions, and captions.
Do not modernize spelling, punctuation, capitalization, or typography unless it is clearly an OCR artifact.
Mark unreadable text as [illegible] rather than guessing.
Keep all bounding boxes and block ordinals from the input unless a block must be split or merged.
When you change text, add a concise provenance note explaining why.

Return JSON that matches the page object shape in manifest.json:
- number
- width
- height
- image_path
- blocks
- metadata
```

## Review Rules

- Prefer source image evidence over OCR text.
- Compare headings, marginalia, footers, page numbers, captions, and body text separately.
- Keep captions attached to their nearest image region.
- Preserve line breaks only when they carry document meaning, such as poetry, tables, lists, forms, or indexes.
- Do not hallucinate missing words, dates, names, or places.

## Output Expectations

The returned page object can be substituted for the original page in `manifest.json`, then `historic_doc_ingest.markdown.write_markdown` can be run again to regenerate `document.md`.
