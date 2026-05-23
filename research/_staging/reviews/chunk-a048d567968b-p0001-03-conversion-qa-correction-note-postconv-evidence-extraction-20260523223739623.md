---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523223739623
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; image-reviewed support is on rendered source images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
reviewed_claims:
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-001-dario-pulgar-chilean-descriptor.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-002-dario-pulgar-chile-film-distribution.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-003-dario-pulgar-fled-after-1973-coup.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-004-dario-pulgar-mother-tongue-spanish.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-005-dario-pulgar-english-french.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-006-dario-pulgar-vision-habitat-distribution-rights.md"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
relationship_note: "research/_staging/relationships/chunk-a048d567968b-p0001-03-no-family-relationship-stated.md"
conversion_confidence: medium-high
conversion_qa_concern: "Rendered images page-0007.jpg and page-0008.jpg are present in this checkout and visually support the Dario Pulgar passages, including the Chile state-film role, the 1973 flight context, the sentence 'His mother tongue was Spanish,' the English/French language statement, and the Vision Habitat distribution-rights work statement. The unresolved blocker is page/chunk reconciliation: the task and chunk manifest assign this evidence to page 1, while the visible printed pages are 7 and 8 and the chunk body includes later converted page metadata."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: Dario Pulgar Evidence

This evidence-extraction revision does not alter raw sources, converted Markdown, chunk Markdown, page Markdown, or canonical wiki pages. It preserves the disagreement between derivative chunk metadata and image-reviewed support.

## Image-Reviewed Support

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present and visually contains the passage naming Dario Pulgar, describing him as Chilean, stating his Chile state film distribution role under Allende, and stating that he fetched up at "The Board" after fleeing Pinochet's overthrow of the Allende government in 1973.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and visually contains the sentence "His mother tongue was Spanish," the surrounding English/French language passage, and the later sentence that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

## Remaining Blocker

The image availability and literal wording concerns are improved, but the proof-review blocker is not fully resolved for canonical promotion. The task and chunk manifest identify this as assigned page 1 / `CHUNK-a048d567968b-P0001-03`; the visible support is on printed/source pages 7 and 8; and the chunk body continues with converted page metadata for later pages. Conversion QA still needs to correct or explicitly document the page-boundary/citation-metadata discrepancy before any Dario Pulgar claims from this chunk are promoted.

## Staging Decision

Keep the source packet and individual Dario Pulgar claim drafts in staging with `promotion_recommendation: hold_for_conversion_qa`. Keep the negative family-relationship note as `promotion_recommendation: do_not_promote`, because this chunk provides contextual biographical and work evidence for Dario Pulgar but does not state a parent, spouse, child, sibling, or other genealogical relationship.
