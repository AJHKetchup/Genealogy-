---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523165539856
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; image-reviewed support appears on rendered/printed pages 7 and 8"
literal_support: "Rendered page-0007.jpg visibly supports the paragraph naming Dario Pulgar, describing him as Chilean, stating that he had been the number two man in Chile's state film distribution system under Allende, and stating that he fled after Pinochet's 1973 overthrow of the Allende government. Rendered page-0008.jpg visibly supports `His mother tongue was Spanish`, the English/French language passage, and `Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were`."
conversion_confidence: medium
conversion_qa_concern: "The prior missing-rendered-image blocker for page-0008.jpg is not present in this checkout: page-0008.jpg exists and visually supports the mother-tongue/language and Vision Habitat work passages. The remaining blocker is the derivative page-boundary/citation conflict: the chunk manifest assigns CHUNK-a048d567968b-P0001-03 to page 1 while the family-relevant text belongs to rendered/printed pages 7 and 8 embedded in the chunk body."
uncertainty: "This note does not alter source text, converted Markdown, chunks, or page Markdown. It preserves the disagreement between derivative chunk metadata and image-reviewed evidence, so related Dario Pulgar claims should remain staged until authoritative conversion/page QA establishes the correct citation."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision reviewed `CHUNK-a048d567968b-P0001-03` in response to proof-review requests for conversion-QA reconciliation.

## Visual Check

The local checkout contains:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

The rendered page 7 image supports the paragraph naming Dario Pulgar, describing him as Chilean, stating his Chile state film distribution role under Allende, and stating that he fled after Pinochet's 1973 overthrow of the Allende government.

The rendered page 8 image supports the sentence `His mother tongue was Spanish`, the English/French language context, and the sentence that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

## Staged Output State

The existing source packet, six Dario Pulgar atomic claim drafts, negative relationship candidate, and conversion-QA identity-review task already carry the controller-assigned chunk path and keep the relevant Dario Pulgar claims on `hold_for_conversion_qa`. No canonical wiki pages were edited, and no new relationship claim is supported by this chunk.

## Remaining Blocker

The page-8 rendered-image availability issue is cleared in this checkout, but the authoritative page reference remains unresolved. The chunk manifest assigns this evidence to page 1, while the image-reviewed Dario Pulgar passages are on rendered/printed pages 7 and 8 inside the chunk body. Keep related claims in staging until conversion QA corrects or formally documents the page reference to use for promotion.

No external research was performed.
