---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524012752081
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
assigned_page_reference: "page_start 1 / page_end 1 in controller assignment, chunk frontmatter, and chunk manifest"
image_reviewed:
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg"
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg"
staged_source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
staged_source_packet_supplement: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260524012752081.md"
staged_claims_reviewed:
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-001-dario-pulgar-chilean-descriptor.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-002-dario-pulgar-chile-film-distribution.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-003-dario-pulgar-fled-after-1973-coup.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-004-dario-pulgar-mother-tongue-spanish.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-005-dario-pulgar-english-french.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-006-dario-pulgar-vision-habitat-distribution-rights.md"
relationship_note: "research/_staging/relationships/chunk-a048d567968b-p0001-03-no-family-relationship-stated.md"
conversion_confidence: medium-high
conversion_qa_concern: "The staged Dario Pulgar claims preserve the discrepancy between assigned page 1 and image-reviewed printed/source pages 7-8. Promotion remains blocked until conversion QA reconciles or formally documents the authoritative page/chunk citation."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: Dario Pulgar Claims Remain Held

This revision responds to proof-review requests for `CHUNK-a048d567968b-P0001-03` without changing raw or converted source material.

## Findings

The family-relevant Dario Pulgar evidence remains useful but not promotion-ready. The derivative chunk transcript names Dario Pulgar and supports staged claims about:

- Chilean identity descriptor.
- Chile state film-distribution role under Allende.
- Displacement after Pinochet's 1973 overthrow of the Allende government.
- Spanish as mother tongue.
- English/French language context.
- Vision Habitat distribution-rights and off-shore printing-materials work.

Prior image-reviewed staging identifies `page-0007.jpg` as support for the full-name, Chilean descriptor, Chile film-distribution, and 1973 displacement passages, and `page-0008.jpg` as support for the mother-tongue, English/French, and Vision Habitat role passages.

## Blocker

The blocker is still conversion/page-reference QA:

- The controller task, chunk frontmatter, and chunk manifest assign the chunk to page `1`.
- The chunk body embeds later converted page sections and Dario Pulgar support from printed/source pages `7` and `8`.
- Canonical promotion would require a stable citation target, so the staged claims should not flow to the tree yet.

## Recommendation

Keep all Dario Pulgar claims from this chunk at `promotion_recommendation: hold_for_conversion_qa`. After conversion QA corrects or documents the page/chunk discrepancy, the claims can be reconsidered individually by proof review as memoir-attributed contextual claims.

No kinship relationship is stated in this chunk; the staged negative-evidence relationship note remains appropriate with `promotion_recommendation: do_not_promote`.
