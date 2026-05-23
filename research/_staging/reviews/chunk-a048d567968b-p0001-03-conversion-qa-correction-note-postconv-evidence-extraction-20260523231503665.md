---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523231503665
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; visually checked support appears on rendered/printed pages 7 and 8"
literal_support: "Rendered page-0007.jpg supports the Dario Pulgar Chilean/Chile film distribution/fled-after-1973 paragraph; rendered page-0008.jpg supports `His mother tongue was Spanish` and Dario's Vision Habitat distribution-rights work."
conversion_confidence: medium-high
conversion_qa_concern: "The relevant Dario Pulgar passages agree between derivative transcript and rendered page images, but the chunk/page metadata remains inconsistent: the manifest assigns page 1 while the support is on printed/source pages 7-8 and the chunk body continues through later page metadata."
uncertainty: "This note does not resolve the authoritative citation boundary. It documents image-reviewed support for the literal passages while preserving the derivative page-reference disagreement."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker-specific revision addresses the proof-review follow-up for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunks, or page Markdown.

## Visual Check Results

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present and visually supports the Dario Pulgar paragraph on printed page 7. The image names Dario Pulgar, describes him as Chilean, states that under Allende he had been the number two man in Chile's state film distribution system while still in his twenties, and says he fetched up at "The Board" after fleeing Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and visually supports the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario was primarily occupied with acquiring distribution rights and determining where off-shore printing materials were.

## Remaining Blocker

The image-reviewed evidence supports the literal Dario Pulgar passages, but the citation/page boundary is still not promotion-ready. The controller assignment and chunk manifest identify the chunk as page 1, while the source images and printed page numbers place the family-relevant passages on pages 7 and 8. The chunk body also includes converted metadata/text for later pages, so the disagreement should remain explicit in staged claims and packets.

## Staging Decision

Keep the Dario Pulgar source packet and related atomic claims on `hold_for_conversion_qa` until a conversion/page-boundary reviewer either corrects the chunk/page metadata or documents the intended citation scheme. The existing negative relationship note remains `do_not_promote` because this chunk states no family relationship.
