---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523223322532
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; support visually appears on rendered source images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
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
conversion_qa_concern: "Rendered images page-0007.jpg and page-0008.jpg are now present and visually support the Dario Pulgar passages, including the Chile state-film role and the sentence 'His mother tongue was Spanish.' The unresolved blocker is page/chunk reconciliation: the task and manifest assign this evidence to page 1, while the visible printed pages are 7 and 8 and the chunk continues with later converted page metadata."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: Dario Pulgar Passages

This revision keeps the Dario Pulgar evidence in staging and preserves the disagreement between derivative chunk metadata and image-reviewed evidence.

## Image-Reviewed Support

- Rendered image `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` visibly contains the paragraph naming Dario Pulgar, describing him as Chilean, stating that he had been the number two man in Chile's state film distribution system under Allende, and stating that he fetched up at "The Board" after fleeing Pinochet's overthrow of the Allende government in 1973.
- Rendered image `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` visibly contains the sentence "His mother tongue was Spanish" and the surrounding language passage, plus the later sentence that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

## Remaining Blocker

The proof-review blocker is not resolved for canonical promotion. The chunk manifest and task identify the assigned material as page 1 / `CHUNK-a048d567968b-P0001-03`, but the visually checked support is on printed/source pages 7 and 8, and the chunk body also embeds converted page metadata for later pages. This indicates a page-boundary or citation-metadata discrepancy that should be corrected or explicitly documented by conversion QA before any staged Dario Pulgar claims are promoted.

## Staging Decision

Keep the source packet, individual Dario Pulgar claim drafts, and negative relationship note in staging with `promotion_recommendation: hold_for_conversion_qa` for promotable claims and `promotion_recommendation: do_not_promote` for the negative relationship note. No raw source, converted Markdown, chunk Markdown, or canonical wiki pages were edited by this evidence-extraction revision.
