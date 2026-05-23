---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523144712824
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_path: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; visually verified support is on rendered images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
literal_support: "page-0007.jpg supports `Dario Pulgar`, the Chilean descriptor, Chile state film distribution role, and the fleeing-after-1973 passage; page-0008.jpg supports `His mother tongue was Spanish`, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium
conversion_qa_concern: "The earlier missing rendered-image concern for page-0008.jpg is resolved in this checkout, and the family-relevant text agrees with the rendered images. The remaining blocker is the authoritative citation/page-boundary mismatch: the manifest assigns the chunk to page 1 while the verified support is on rendered/printed pages 7 and 8 and the chunk body continues into later page metadata."
uncertainty: "This correction note documents visual support but does not resolve which page reference should be canonical. Related claims should stay staged until conversion/page-boundary QA decides whether citation should follow assigned page 1, rendered image numbers, printed page numbers, or regenerated chunk metadata."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This current-worker revision responds to the proof-review follow-up for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunk Markdown, or conversion job page Markdown.

## Visual Verification

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present and visually supports the Dario Pulgar paragraph near the bottom of printed page 7, including the Chilean descriptor, the Chile state film distribution role under Allende, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and visually supports the sentence `His mother tongue was Spanish`, the English/French language context, and the sentence that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

## Staged Draft Status

The staged source packet, claims, identity candidate, conflict candidate, relationship negative-evidence note, and QA task preserve the derivative/source disagreement and keep promotable Dario Pulgar claims on `hold_for_conversion_qa`. The active blocker is no longer missing rendered image `page-0008.jpg`; it is the unresolved page-boundary/citation mismatch between:

- controller assignment and chunk manifest: `page_start: 1` / `page_end: 1`;
- rendered image and printed page evidence: `page-0007.jpg` / printed page 7 and `page-0008.jpg` / printed page 8;
- chunk body content: later converted page metadata and transcription embedded in a page-1 assigned chunk.

## Promotion Recommendation

Keep related Dario Pulgar claims, the source packet, identity/conflict candidates, and QA task on `hold_for_conversion_qa` until the authoritative page reference is corrected or explicitly documented. The relationship note remains `do_not_promote` because this chunk states no family relationship.
