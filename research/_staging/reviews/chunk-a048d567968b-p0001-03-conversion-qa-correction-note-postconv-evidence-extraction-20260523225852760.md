---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523225852760
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
related_source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260523225852760.md"
related_claims:
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-001-dario-pulgar-chilean-descriptor.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-002-dario-pulgar-chile-film-distribution.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-003-dario-pulgar-fled-after-1973-coup.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-004-dario-pulgar-mother-tongue-spanish.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-005-dario-pulgar-english-french.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-006-dario-pulgar-vision-habitat-distribution-rights.md"
source_page_images_checked:
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg"
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg"
conversion_confidence: medium-high
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This note addresses the proof-review follow-up for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunks, or page Markdown.

## Correction

The previously reported missing rendered image for converted/printed page 8 is no longer a blocker in this checkout. `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` exists and was visually checked.

Visual review confirms:

- `page-0007.jpg` supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, Chile state-film-distribution role under Allende, and 1973 displacement context.
- `page-0008.jpg` supports `His mother tongue was Spanish`, the related English/French language passage, and the Vision Habitat distribution-rights/off-shore printing-materials role passage.

## Remaining Disagreement

The page-reference discrepancy remains. The assignment and chunk manifest identify the chunk as page 1, but the family-relevant support appears in the chunk body under converted page metadata for printed/source pages 7 and 8. The staged claims should therefore retain `promotion_recommendation: hold_for_conversion_qa` until the conversion/chunk boundary and citation target are reconciled or explicitly documented as a known multi-page chunking artifact.

## Staging Recommendation

Do not promote the Dario Pulgar claims from this chunk yet. The wording is visually supported, but canonical citation should wait for conversion QA to resolve the page-reference mismatch.
