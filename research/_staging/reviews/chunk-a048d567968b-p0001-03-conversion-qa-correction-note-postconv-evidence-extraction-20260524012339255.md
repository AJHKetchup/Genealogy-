---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524012339255
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
assigned_page_reference: "page_start 1 / page_end 1 in chunk and manifest"
image_reviewed:
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg"
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg"
staged_source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
staged_claims_reviewed:
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-002-dario-pulgar-chile-film-distribution.md"
  - "research/_staging/claims/chunk-a048d567968b-p0001-03-004-dario-pulgar-mother-tongue-spanish.md"
conversion_confidence: medium-high
conversion_qa_concern: "Rendered images verify the disputed Dario Pulgar wording, but chunk and manifest page metadata still assign the mixed later-page text to page 1. Do not promote until authoritative page/chunk citation handling is reconciled or explicitly accepted."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: Dario Pulgar Page Boundary Disagreement

This revision preserves the disagreement identified by proof review rather than resolving it in the raw or converted files. No raw source, converted Markdown, chunk Markdown, page Markdown, or canonical wiki page was edited.

## Image Review

- `page-0007.jpg` visibly carries printed page number `7` and contains the full-name Dario Pulgar paragraph: `A couple of my UN Habitat Secretariat confreres stayed on, notably Dario Pulgar...` followed by the Chile/Allende state film distribution and 1973 displacement wording.
- `page-0008.jpg` visibly carries printed page number `8` and contains the sentence `His mother tongue was Spanish`, the English/French language passage, and the Vision Habitat distribution-rights/off-shore printing materials passage.

## Staged Evidence Status

The existing staged source packet and Dario Pulgar claim drafts now correctly identify the proof-review blocker as a page/chunk citation problem:

- The chunk manifest and chunk frontmatter assign `CHUNK-a048d567968b-P0001-03` to page 1.
- The chunk body embeds converted text from printed/source pages 7, 8, 9, and 10.
- The two proof-reviewed claims have visually supported wording, but their canonical citation target remains uncertain because their support belongs to printed/source pages 7 and 8 inside an assigned page-1 chunk.

## Recommendation

Keep `promotion_recommendation: hold_for_conversion_qa` for the Dario Pulgar claims from this chunk until conversion QA either:

1. corrects the chunk/page metadata and citation references, or
2. documents that this chunk intentionally contains later printed/source pages and defines the canonical citation format for claims drawn from the embedded page 7 and page 8 text.

After that QA step, the Chile film distribution role and mother-tongue Spanish claims can be reconsidered for proof review as memoir-attributed contextual claims.
