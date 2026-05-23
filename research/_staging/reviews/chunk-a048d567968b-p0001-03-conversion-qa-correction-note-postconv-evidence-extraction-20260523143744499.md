---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523143744499
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
literal_support: "page-0007.jpg shows `Dario Pulgar` and the Chile film distribution/fled-after-1973 passage; page-0008.jpg shows `His mother tongue was Spanish` and the Vision Habitat distribution-rights passage."
conversion_confidence: medium
conversion_qa_concern: "The rendered images verify the family-relevant text, but the chunk manifest still assigns this part to page 1 while the visible evidence is on printed/rendered pages 7 and 8 and the chunk body continues into later page metadata."
uncertainty: "This note does not resolve the authoritative page citation. Claims from this chunk should remain staged until conversion/page-boundary QA decides whether citation should follow the chunk assignment, rendered image number, printed page number, or regenerated chunk metadata."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This current-worker revision rechecked the proof-review blockers for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunk Markdown, or conversion job page Markdown.

## Visual Verification

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present and visually supports the Dario Pulgar paragraph near the bottom of printed page 7, including the statements that Dario Pulgar stayed on, was described as Chilean, had been the number two man in Chile's state film distribution system under Allende while still in his twenties, and had fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and visually supports the page-top sentence `His mother tongue was Spanish`, the English/French language passage, and the later sentence that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

## Staged Draft Status

The staged source packet and claim drafts for this chunk already preserve the problem by using `promotion_recommendation: hold_for_conversion_qa`. The evidence substance is readable in the converted chunk and visually supported by the rendered images, but the authoritative citation remains unresolved because:

- the controller assignment and chunk manifest identify `CHUNK-a048d567968b-P0001-03` as `page_start: 1` / `page_end: 1`;
- the source images carrying the Dario Pulgar evidence are rendered images `page-0007.jpg` and `page-0008.jpg`, with visible printed page numbers 7 and 8;
- the chunk body includes multiple later page metadata/transcription sections after the assigned page-1 frontmatter.

## Promotion Recommendation

Keep the related Dario Pulgar claims, identity candidate, source packet, and conflict candidate on `hold_for_conversion_qa`. The negative relationship note remains `do_not_promote` because this chunk states no kinship relationship.
