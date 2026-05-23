---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523232821787
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260523232821787.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; reviewed support appears on rendered source images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
literal_support: "page-0007.jpg supports the Dario Pulgar Chilean descriptor, Chile state-film distribution role, and 1973 flight context; page-0008.jpg supports `His mother tongue was Spanish`, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium-high
conversion_qa_concern: "Rendered source images page-0007.jpg and page-0008.jpg are present and support the family-relevant text. The remaining blocker is the unresolved disagreement between the assigned page-1 chunk metadata and printed/source page 7-8 evidence."
uncertainty: "Evidence wording is supported, but canonical citation remains unsafe until page-boundary QA reconciles the manifest assignment, chunk body page metadata, and rendered source images."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision responds to the proof-review hold for `CHUNK-a048d567968b-P0001-03`.

## Current Findings

- The controller-assigned chunk path is `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md`.
- The chunk frontmatter and manifest assign the chunk to page 1.
- The family-relevant Dario Pulgar text in the chunk is not page-1 evidence. It appears in the chunk body with later page metadata and is visually supported by rendered/printed pages 7 and 8.
- `page-0007.jpg` visibly supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, Chile state-film distribution role, and 1973 flight context.
- `page-0008.jpg` visibly supports `His mother tongue was Spanish`, the related English/French language passage, and Dario's Vision Habitat distribution-rights work.

## Effect On Staged Claims

The staged claim drafts for Dario Pulgar remain useful but not promotion-ready. Keep them on `hold_for_conversion_qa` until an authoritative citation/page-boundary correction is made or the conversion record explicitly documents why this page-1 chunk contains printed pages 7 and 8.

No relationship candidate should be promoted from this chunk. The chunk gives person-linked narrative context for Dario Pulgar but states no kinship relationship.

## Promotion Recommendation

Keep `promotion_recommendation: hold_for_conversion_qa` for Dario Pulgar claims from this chunk. The blocker is now specifically page-reference/chunk-boundary reconciliation, not missing rendered page-8 image evidence.
