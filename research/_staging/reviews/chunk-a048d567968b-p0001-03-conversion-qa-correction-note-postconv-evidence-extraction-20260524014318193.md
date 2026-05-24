---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524014318193
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
source_packet_supplement: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260524014318193.md"
page_reference: "assigned page 1 in controller/chunk/manifest; Dario Pulgar support visually verified on rendered/printed pages 7 and 8"
literal_support: "Page-0007.jpg supports the Dario Pulgar Chilean/Chile state film distribution/fleeing-1973 paragraph. Page-0008.jpg supports `His mother tongue was Spanish`, the English/French language passage, and the Vision Habitat distribution-rights/off-shore printing-materials passage."
conversion_confidence: medium-high
conversion_qa_concern: "The rendered images are present and support the Dario Pulgar wording, but promotion remains blocked by the unresolved page-boundary/citation conflict between assigned page 1 and printed/source pages 7-8."
uncertainty: "This correction note does not edit raw sources, converted Markdown, chunk files, page Markdown, or canonical wiki pages. The source is memoir evidence and supplies no formal job dates, birth date, exact title, or kinship relationship."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This correction note responds to the proof-review revision requests for `CHUNK-a048d567968b-P0001-03`.

## Finding

The relevant rendered source images are present in the checkout and were visually checked:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

Printed/source page 7 supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, the statement that he had been the number two man in Chile's state film distribution system under Allende while still in his twenties, and the statement that he fetched up at "The Board" after fleeing Pinochet's 1973 overthrow of the Allende government.

Printed/source page 8 supports the statement that Dario's mother tongue was Spanish, that he was fluent in English and had learned French in Montreal, and that he was primarily occupied with acquiring distribution rights and determining where off-shore printing materials were.

## Remaining Blocker

The substantive text is image-supported, but this extraction task cannot repair conversion outputs or chunk metadata. The controller assignment, chunk frontmatter, and chunk manifest identify the material as page 1, while the visually checked family-relevant support is on printed/source pages 7 and 8. That disagreement must remain visible in staging.

## Recommendation

Keep the source packet and atomic Dario Pulgar claim drafts at `promotion_recommendation: hold_for_conversion_qa` until conversion QA reconciles or formally documents the authoritative citation/page boundary. Keep the negative relationship note at `promotion_recommendation: do_not_promote`, because no kinship relationship is stated in this chunk.
