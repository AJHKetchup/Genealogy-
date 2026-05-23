---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523154110589
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
page_reference: "assigned page 1; current visual check confirms support on rendered images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
literal_support: "page-0007.jpg supports the full-name `Dario Pulgar` paragraph, Chilean descriptor, Chile state film distribution role under Allende, and fleeing-after-1973 passage; page-0008.jpg supports `His mother tongue was Spanish`, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium
conversion_qa_concern: "The family-relevant text is visually supported in rendered page images, including the previously questioned page-0008.jpg. The unresolved blocker is still the authoritative page-boundary/citation mismatch: the controller assignment and chunk manifest identify this as page 1, while the visible support is on printed/rendered pages 7 and 8 and the chunk body includes later page metadata."
uncertainty: "This note documents visual support and the remaining derivative-page disagreement only. It does not decide whether the canonical citation should follow assigned page 1, rendered image numbers, printed page numbers, or regenerated chunk metadata."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This current-worker revision addresses the proof-review follow-up for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunk Markdown, or conversion job page Markdown.

## Current Visual Check

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present. It visually supports the paragraph naming `Dario Pulgar`, describing him as Chilean, stating that he had been the number two man in Chile's state film distribution system under Allende while still in his twenties, and stating that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present. It visually supports the sentence `His mother tongue was Spanish`, the English/French language passage, and the sentence that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

## Staged Draft Status

The existing staged source packet, six atomic claim drafts, conflict candidate, identity-analysis hold note, negative relationship note, and conversion-QA task already preserve the derivative/source disagreement. They correctly keep promotable Dario Pulgar facts on `hold_for_conversion_qa`, while the negative relationship note remains `do_not_promote` because this chunk states no kinship relationship.

The missing-rendered-image blocker for `page-0008.jpg` is not reproduced in this checkout. The active blocker is the page-boundary and citation mismatch:

- controller assignment and chunk manifest: `page_start: 1` / `page_end: 1`;
- visually checked support: rendered `page-0007.jpg` and `page-0008.jpg`, visible printed pages 7 and 8;
- chunk body: later converted page metadata and transcribed text are embedded inside the assigned page-1 chunk.

## Promotion Recommendation

Keep all promotable Dario Pulgar claims from this chunk on `hold_for_conversion_qa` until conversion/page-boundary QA either corrects the chunk metadata or explicitly documents the authoritative page citation policy for this source packet. Do not promote claims, relationships, identity merges, or canonical attachments from this chunk on the current page-1 citation alone.
