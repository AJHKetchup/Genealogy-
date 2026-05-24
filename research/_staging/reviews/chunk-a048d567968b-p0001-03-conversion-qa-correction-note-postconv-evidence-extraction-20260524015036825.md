---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524015036825
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260524015036825.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; support is in embedded converted text and rendered/source images for printed/source pages 7 and 8"
literal_support: "page 7 text names Dario Pulgar and supports the Chilean descriptor, Chile state-film distribution role, and 1973 flight context; page 8 text supports Spanish mother tongue, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium-high
conversion_qa_concern: "The source images page-0007.jpg and page-0008.jpg are present in the conversion job page-images directory, but the authoritative citation remains blocked by the page-1 chunk assignment and multi-page embedded text. This is a page-boundary/citation issue rather than a disagreement in the Dario Pulgar wording."
uncertainty: "The claims are memoir-derived contextual evidence and should not be treated as vital-record or official employment proof. No kinship relationship is stated in this chunk."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker reviewed the proof-review follow-up for `CHUNK-a048d567968b-P0001-03`. No raw source, converted Markdown, chunk Markdown, or page Markdown was edited.

## Current Evidence State

The Dario Pulgar passages are family-relevant and already represented by staged atomic claims. The existing claim set should remain in staging:

- `chunk-a048d567968b-p0001-03-001-dario-pulgar-chilean-descriptor.md`
- `chunk-a048d567968b-p0001-03-002-dario-pulgar-chile-film-distribution.md`
- `chunk-a048d567968b-p0001-03-003-dario-pulgar-fled-after-1973-coup.md`
- `chunk-a048d567968b-p0001-03-004-dario-pulgar-mother-tongue-spanish.md`
- `chunk-a048d567968b-p0001-03-005-dario-pulgar-english-french.md`
- `chunk-a048d567968b-p0001-03-006-dario-pulgar-vision-habitat-distribution-rights.md`

The negative relationship note remains appropriate because this chunk states no family relationship for Dario Pulgar.

## Blocker To Preserve

The derivative sources still disagree about page control. The task assignment, chunk frontmatter, and chunk manifest place the chunk on page 1. The family-relevant Dario Pulgar text appears in embedded converted sections for printed/source pages 7 and 8, and the chunk continues into later converted page text. Until conversion QA reconciles or formally documents that discrepancy, keep related claim drafts on `promotion_recommendation: hold_for_conversion_qa`.

## Recommendation

Do not promote these claims canonically yet. After page-boundary/citation QA, the claims may be reconsidered as memoir-attributed contextual evidence for Dario Pulgar's identity, language background, Chile/1973 displacement context, and Vision Habitat work.
