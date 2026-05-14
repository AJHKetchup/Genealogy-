# Conversion Quality Contract

Use this checklist when converting or reviewing page work orders.

## Transcription

- Preserve original spelling, punctuation, line breaks that carry meaning, table structure, printed labels, handwritten labels, captions, stamps, seals, signatures, marginalia, and page numbers.
- Use `[?]` immediately after uncertain words or phrases.
- Use `[illegible]` only when no plausible reading is possible.
- Do not modernize names, places, grammar, abbreviations, or dates in literal transcription.
- Keep translation and interpretation out of the literal transcription section.

## Images

- Crop every meaningful non-text visual region into the page's assigned `extracted-images/page-####/` folder.
- Keep crop filenames stable: `page-####-image-01.png`, `page-####-image-02.png`.
- Insert each crop inline near its source position in `## Images, Captions, And Visual Notes`.
- Use visible captions literally. If no caption exists, write a descriptive caption and label it as supplied by the converter.
- Record uncertainty when a crop boundary, identity, or caption is unclear.

## Chunking

- Use one page per work order.
- Chunk assembled Markdown with `genealogy-wiki prep-chunk`.
- Keep page boundaries stable. Split oversized pages inside the same page, by Markdown section and paragraph boundaries.
- Do not merge unrelated pages into one chunk for convenience.

## Provenance

Each derivative must point back to:

- original raw source path
- source SHA-256 when available
- conversion job manifest
- page image path
- page Markdown path
- extracted-image folder when images were present
- chunk manifest after chunking

## Completeness Review

Check:

- every visible text region is represented or marked unresolved
- all tables/forms preserve labels and row order
- image regions and captions are accounted for
- page numbers and stamped/handwritten numbers are represented
- uncertain or illegible areas are listed
- missing pages are explicit in the assembled document
