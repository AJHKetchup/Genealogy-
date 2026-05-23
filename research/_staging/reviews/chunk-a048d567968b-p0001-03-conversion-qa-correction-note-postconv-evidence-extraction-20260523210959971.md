---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523210959971
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260523210959971.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1 in controller chunk manifest; Dario Pulgar support appears in derivative text for printed/source pages 7 and 8 and in separate legacy page-7/page-8 chunks"
literal_support: "The derivative text names `Dario Pulgar`, describes him as Chilean, states he was the number two man in Chile's state film distribution system under Allende, states he fled after Pinochet's 1973 overthrow, states `His mother tongue was Spanish`, and states Dario worked on distribution rights and off-shore printing materials."
conversion_confidence: low-to-medium
conversion_qa_concern: "Earlier staged correction notes report visual support from Habitat page-0007.jpg and page-0008.jpg, but this worker could not find those Habitat rendered images in the current checkout. The manifest still references them, and page-level Markdown exists, but the authoritative source-image/page citation is not reconciled."
uncertainty: "Do not alter the source text. Preserve both layers: derivative transcripts and prior staged image-review reports support the Dario passages, while current filesystem state prevents independent image verification by this worker."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision addresses the proof-review follow-up for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunks, or page Markdown.

## Current Revision Finding

The Dario Pulgar passages remain family-relevant and should stay staged, but not promoted. The controller-assigned chunk is still `page-0001-chunk-03.md`, while its body contains later converted page metadata and text. The Dario full-name and Chile film-distribution paragraph appears in the printed/source page 7 portion; the mother-tongue, English/French, and Vision Habitat distribution-rights passages appear in the printed/source page 8 portion.

This worker found derivative support in:

- `raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-markdown/page-0007.md`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-markdown/page-0008.md`
- `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0007-chunk-01.md`
- `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0008-chunk-01.md`

## Preserved Disagreement

Earlier staged correction notes report that Habitat rendered images `page-0007.jpg` and `page-0008.jpg` were present and visually supported the Dario Pulgar passages, including the previously blocked sentence `His mother tongue was Spanish`. In this current checkout, a recursive search under `raw/` did not find those Habitat image files; it found `page-0007.jpg` and `page-0008.jpg` only in an unrelated CV conversion job. The Habitat conversion manifest still lists the images, so the disagreement is between the manifest/prior staged visual-review notes and the current filesystem state available to this worker.

The substantive derivative transcript and prior visual-review notes agree on the Dario Pulgar claim substance. The unresolved blocker is authoritative citation/page control and current availability of source images for independent verification.

## Staging Recommendation

Keep the existing source packet and Dario Pulgar atomic claims on `promotion_recommendation: hold_for_conversion_qa`. The existing negative relationship note remains appropriate with `promotion_recommendation: do_not_promote` because the chunk states colleague/work context and no parent, spouse, child, sibling, or other kinship relationship.

After conversion QA reconciles the assigned page-1 chunk, printed/source pages 7 and 8, and the rendered image availability, the occupation/role, migration-context, language, and Vision Habitat work claims can be reconsidered for proof review with memoir-source attribution.
