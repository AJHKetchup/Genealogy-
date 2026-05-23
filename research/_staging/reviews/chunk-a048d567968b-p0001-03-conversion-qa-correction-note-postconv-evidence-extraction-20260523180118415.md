---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523180118415
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
affected_claims:
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-001-dario-pulgar-chilean-descriptor.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-002-dario-pulgar-chile-film-distribution.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-003-dario-pulgar-fled-after-1973-coup.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-004-dario-pulgar-mother-tongue-spanish.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-005-dario-pulgar-english-french.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-006-dario-pulgar-vision-habitat-distribution-rights.md"
page_reference: "assigned page 1 in chunk manifest; visually checked support is on rendered page images page-0007.jpg and page-0008.jpg, printed pages 7 and 8"
conversion_confidence: medium
conversion_qa_concern: "The Dario Pulgar passages are readable in both the converted chunk and current rendered page images, including page-0008.jpg. The unresolved blocker is the derivative chunk/manifest page assignment: CHUNK-a048d567968b-P0001-03 is assigned to page 1 while its body contains later printed/source pages 7-10. Do not promote claims until the authoritative page citation/boundary is corrected or formally accepted by conversion QA."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: CHUNK-a048d567968b-P0001-03

This revision documents, but does not repair, the page-reference disagreement for the Dario Pulgar evidence in `CHUNK-a048d567968b-P0001-03`.

## Current Visual Check

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present. It visually supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, Chile state film distribution role under Allende, and flight after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present in this checkout. It visually supports the converted sentence `His mother tongue was Spanish, but he was fluent in English and had learned French in Montreal in six weeks, he said.` It also visually supports `Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.`

## Preserved Disagreement

The local images clear the prior missing-rendered-image blocker for the page-8 language passage. They do not clear the page-boundary/citation blocker:

- the assigned chunk path and chunk manifest identify this as `page-0001-chunk-03.md`, with `page_start: 1` and `page_end: 1`;
- the chunk body contains multiple embedded converted page sections, including page metadata for printed/source pages 8, 9, and 10;
- the family-relevant support for Dario Pulgar appears visually on rendered pages `page-0007.jpg` and `page-0008.jpg`, not on assigned page 1.

## Extraction Judgment

The existing staged Dario Pulgar claims and source packet may remain useful as draft evidence, but their promotion recommendation should stay `hold_for_conversion_qa`. The evidence is textually and visually supported as memoir-source context, while the authoritative citation/page reference remains unresolved.

No kinship relationship is stated in the checked Dario passages; the existing negative-evidence relationship note remains appropriate for this chunk only.
