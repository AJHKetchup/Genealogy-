---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523224111061
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
page_reference: "assigned page 1 in chunk manifest/frontmatter; family-relevant Dario Pulgar support is documented against rendered/printed pages 7 and 8"
literal_support: "The staged Dario Pulgar evidence includes the Chilean descriptor, Chile state film-distribution role under Allende, flight after Pinochet's 1973 overthrow, Spanish mother tongue, English/French language context, and Vision Habitat distribution-rights/off-shore printing-materials work."
conversion_confidence: medium-high
conversion_qa_concern: "Rendered page images page-0007.jpg and page-0008.jpg are present in this checkout, and prior staged revisions document visual support for the relevant Dario Pulgar passages. The remaining blocker is authoritative page/chunk citation integrity: this derivative chunk is assigned to page 1 while the family-relevant support belongs to printed/rendered pages 7 and 8 and the chunk body includes later converted page metadata."
uncertainty: "This note does not alter raw sources, converted Markdown, chunks, or page Markdown. It preserves the disagreement between derivative chunk metadata and image-reviewed evidence. Identity linkage to a canonical Dario Pulgar person remains for proof review after citation QA."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision found the required staged outputs already present for `CHUNK-a048d567968b-P0001-03`:

- Source packet: `research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md`
- Six atomic Dario Pulgar claim drafts in `research/_staging/claims/`, all kept on `hold_for_conversion_qa`
- Negative relationship note: `research/_staging/relationships/chunk-a048d567968b-p0001-03-no-family-relationship-stated.md`
- Conversion/page-boundary task: `research/_staging/tasks/TASK-STAGE-CHUNK-a048d567968b-P0001-03-conversion-qa-page-boundary.md`

The current checkout contains both rendered source images referenced by prior revisions:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

The earlier missing-image blocker for page 8 is not active in this checkout. The active blocker is still citation/page-boundary QA: the assignment and chunk manifest identify this as page 1, while the Dario Pulgar support is preserved in the converted chunk body and prior image-reviewed staging as printed/rendered pages 7 and 8.

Keep the Dario Pulgar source packet and claim drafts on `promotion_recommendation: hold_for_conversion_qa` until conversion QA corrects or formally documents the authoritative page references. No canonical wiki pages should be edited from this extraction task.
