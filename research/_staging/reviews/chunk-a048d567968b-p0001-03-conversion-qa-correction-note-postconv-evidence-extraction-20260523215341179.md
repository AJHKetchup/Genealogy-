---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523215341179
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; family-relevant Dario Pulgar support is staged against rendered/printed pages 7 and 8"
literal_support: "Existing staged claims quote Dario Pulgar as a Chilean colleague, his Chile state film distribution role under Allende, his flight after Pinochet's 1973 overthrow, his Spanish mother tongue and English/French language context, and his Vision Habitat distribution-rights/off-shore printing-materials work."
conversion_confidence: medium-high
conversion_qa_concern: "This dispatch found the staged source packet, six atomic Dario Pulgar claims, negative relationship note, and page-boundary research task already revised to preserve the evidence disagreement. Rendered page images page-0007.jpg and page-0008.jpg are present in the conversion job. The remaining blocker is authoritative page/chunk citation reconciliation because the manifest assigns the chunk to page 1 while the family-relevant support belongs to printed/rendered pages 7 and 8."
uncertainty: "No raw source, converted Markdown, chunk, or page Markdown was edited. This note does not resolve the page-boundary conflict; it documents that claim promotion remains blocked until conversion QA corrects or explicitly documents the authoritative page reference."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision rechecked `CHUNK-a048d567968b-P0001-03` after proof review held two Dario Pulgar claims for conversion QA.

Existing staged outputs are sufficient for the current evidence state:

- `research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md` records the Dario Pulgar source packet and keeps `promotion_recommendation: hold_for_conversion_qa`.
- Six atomic Dario Pulgar claim drafts in `research/_staging/claims/` remain staged with `promotion_recommendation: hold_for_conversion_qa`.
- `research/_staging/relationships/chunk-a048d567968b-p0001-03-no-family-relationship-stated.md` records that this chunk states no family relationship and remains `do_not_promote`.
- `research/_staging/research-tasks/chunk-a048d567968b-p0001-03-conversion-qa-page-boundary.md` keeps the unresolved page-boundary task open.

The rendered page images cited by the revised staged materials are present in this checkout:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

The blocker remains citation/page-boundary QA, not absence of staged evidence. The assignment and chunk manifest identify the chunk as page 1, while the Dario Pulgar support is documented in staged materials against rendered/printed pages 7 and 8. Keep the Dario Pulgar claims on `hold_for_conversion_qa` until conversion QA reconciles or explicitly documents the authoritative page reference.
