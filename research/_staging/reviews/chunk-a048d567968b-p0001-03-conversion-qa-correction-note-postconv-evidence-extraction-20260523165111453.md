---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523165111453
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
literal_support: "Rendered page-0007.jpg visibly supports the Dario Pulgar Chilean/Chile state film distribution/fleeing-1973 paragraph. Rendered page-0008.jpg visibly supports `His mother tongue was Spanish`, the English/French language passage, and `Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were`."
conversion_confidence: medium
conversion_qa_concern: "The earlier missing page-0008.jpg concern is not reproduced in this checkout: page-0008.jpg is present and visually supports the relevant passage. The unresolved blocker is still the derivative page-boundary/citation conflict: the chunk manifest assigns CHUNK-a048d567968b-P0001-03 to page 1 while the family-relevant evidence is on rendered/printed pages 7 and 8 inside the chunk body."
uncertainty: "This correction note does not alter raw sources, converted Markdown, chunks, or page Markdown. It preserves the disagreement between assigned chunk metadata and image-reviewed evidence, so related Dario Pulgar claims should remain staged until authoritative conversion/page QA resolves the citation."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision reviewed the staged Dario Pulgar outputs for `CHUNK-a048d567968b-P0001-03` after proof review requested conversion-QA reconciliation.

## Visual Check

The local checkout contains the two rendered page images needed for the family-relevant Dario Pulgar passages:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

The rendered page 7 image supports the paragraph naming Dario Pulgar, describing him as Chilean, stating his Chile state film distribution role under Allende, and stating that he fled after Pinochet's 1973 overthrow of the Allende government. The rendered page 8 image supports the mother-tongue sentence, the English/French language context, and the Vision Habitat distribution-rights/off-shore printing-materials work sentence.

## Staged Output State

The existing source packet, six Dario Pulgar atomic claims, negative relationship candidate, and page-boundary research task already preserve the disagreement and keep promotable claims on `hold_for_conversion_qa`. No new canonical claims are being promoted from this task.

No kinship relationship is stated in the chunk. The existing negative relationship candidate remains appropriate with `promotion_recommendation: do_not_promote`.

## Remaining Blocker

The missing-image blocker for page 8 is cleared for this checkout, but the authoritative citation/page-boundary problem remains unresolved. The chunk manifest and assigned chunk path identify page 1, while the image-reviewed family-relevant text belongs to rendered/printed pages 7 and 8. Keep the Dario Pulgar claims from this chunk in staging until conversion QA corrects or formally documents the page reference to use for promotion.

No external research was performed.
