---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523202753338
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; derivative page-markdown and chunk body place Dario Pulgar support on source/printed pages 7 and 8"
literal_support: "Page-markdown page-0007.md and the chunk text support the Dario Pulgar Chilean/Chile film-distribution/fleeing-1973 paragraph; page-markdown page-0008.md and the chunk text support `His mother tongue was Spanish`, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium
conversion_qa_concern: "The current checkout contains page-markdown for pages 7 and 8 and the conversion manifest lists page-images/page-0007.jpg and page-images/page-0008.jpg, but the page-images directory is absent, so this worker cannot independently repeat the visual verification requested by proof review. Earlier staged notes report visual checks, including one note that page-0008.jpg was present, but the current filesystem state does not allow confirmation. The chunk manifest still assigns CHUNK-a048d567968b-P0001-03 to page 1 while the family-relevant support belongs to later source/printed pages."
uncertainty: "The derivative transcripts agree on the Dario Pulgar wording, but canonical citation remains blocked until the rendered images or PDF page references are reconciled and the page-boundary issue is resolved by conversion QA."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision preserves the proof-review disagreement for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunks, page Markdown, or canonical wiki pages.

## Current Filesystem Check

- The assigned chunk path is `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md`.
- The chunk manifest assigns this chunk to `page_start: 1` and `page_end: 1`.
- The conversion job manifest lists rendered images for source pages 7 and 8 at `page-images/page-0007.jpg` and `page-images/page-0008.jpg`.
- The `page-images` directory is not present in the current checkout, so no fresh image reread was performed in this revision.
- The derivative page Markdown files `page-markdown/page-0007.md` and `page-markdown/page-0008.md` are present and agree with the Dario Pulgar passages staged in the source packet and claim drafts.

## Evidence State

The derivative text supports the same family-relevant Dario Pulgar cluster already staged:

- `page-0007.md` names `Dario Pulgar`, describes him as Chilean, states that he had been the number two man in Chile's state film distribution system under Allende, and says he arrived after fleeing Pinochet's 1973 overthrow of the Allende government.
- `page-0008.md` states that Dario's mother tongue was Spanish, that he was fluent in English, that he had learned French in Montreal, and that he was primarily occupied with acquiring distribution rights and locating off-shore printing materials.

## Disagreement Preserved

Earlier proof review and staged correction notes report visual support on rendered `page-0007.jpg` and `page-0008.jpg`, including one later correction note saying `page-0008.jpg` was present at that time. This worker cannot confirm those image checks because the rendered images are absent now. The disagreement is therefore not resolved; it is narrowed to repository-state/page-boundary QA rather than a new contradiction in the Dario Pulgar wording.

## Promotion Recommendation

Keep the related source packet, identity candidate, relationship negative-evidence note, conflict note, and Dario Pulgar claim drafts on `hold_for_conversion_qa`, except the negative relationship note which remains `do_not_promote`. The next reviewer should restore or regenerate the rendered source images, verify pages 7 and 8 visually, and reconcile the authoritative citation/page boundary before any canonical promotion.
