---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523213558105
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; Dario Pulgar support is visually verified on rendered page images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
literal_support: "page-0007.jpg supports the Dario Pulgar full-name, Chilean descriptor, Chile state film distribution role, and 1973 flight context. page-0008.jpg supports `His mother tongue was Spanish`, the English/French language passage, and the Vision Habitat distribution-rights/off-shore printing-materials passage."
conversion_confidence: medium-high
conversion_qa_concern: "The previously reported page-0008.jpg missing-image blocker is not present in this checkout; page-0007.jpg and page-0008.jpg are available and visually support the staged passages. The remaining blocker is the derivative page-boundary/citation conflict: the chunk manifest assigns this material to page 1 while the supporting evidence is on rendered/printed pages 7 and 8."
uncertainty: "This note does not alter raw sources, converted Markdown, chunk text, or page Markdown. The image-reviewed evidence and derivative transcript agree on the Dario passages, but authoritative page citation/chunk-boundary reconciliation is still unresolved."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker reviewed `CHUNK-a048d567968b-P0001-03` after proof review requested conversion-QA reconciliation for the Dario Pulgar claims.

## Findings

- The rendered page images are present in this checkout:
  - `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
  - `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`
- Visual check of `page-0007.jpg` verifies the full-name Dario Pulgar paragraph, including the Chilean descriptor, Chile state-film distribution role under Allende, and flight after Pinochet's 1973 overthrow.
- Visual check of `page-0008.jpg` verifies the sentence `His mother tongue was Spanish`, the English/French language context, and Dario's Vision Habitat work acquiring distribution rights and locating off-shore printing materials.
- The staged claim drafts should remain on `hold_for_conversion_qa` because the chunk manifest still assigns this material to page 1 while the verified support is on rendered/printed pages 7 and 8.

## Staged Output Updates

I updated the stale image-availability wording in:

- `research/_staging/identities/chunk-a048d567968b-p0001-03-dario-pulgar-identity-candidate.md`
- `research/_staging/research-tasks/chunk-a048d567968b-p0001-03-conversion-qa-page-boundary.md`

The source packet, six atomic Dario Pulgar claims, negative relationship candidate, identity candidate, and page-boundary research task all keep promotion blocked or non-promotable as appropriate. No canonical wiki pages were edited.

## Promotion Recommendation

Keep all promotable Dario Pulgar drafts from this chunk on `hold_for_conversion_qa` until the conversion/page-boundary issue is corrected or explicitly documented by the conversion QA process. After that, the occupation/role, language, migration-context, and Vision Habitat work claims can be reconsidered for proof review with memoir-source attribution.
