---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523182729813
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; converted chunk body includes later printed/source page metadata and text, with prior staged notes locating Dario Pulgar support on rendered page-0007.jpg and page-0008.jpg"
literal_support: "Converted text includes `Dario Pulgar`, `the number two man in Chile's state film distribution system`, `after fleeing Pinochet's overthrow of the Allende government in 1973`, `His mother tongue was Spanish`, and `Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were`."
conversion_confidence: medium
conversion_qa_concern: "The transcript text is clear enough for staged extraction, but the page control problem remains unresolved. The chunk manifest assigns this chunk to page 1 while the chunk body contains converted metadata/text for later printed pages. The conversion job manifest lists rendered image paths for page-0007.jpg and page-0008.jpg, but those image files were not present in the current checkout for this worker to independently verify the prior image-reviewed evidence."
uncertainty: "This note preserves the disagreement between derivative transcripts, page/chunk metadata, and prior image-reviewed evidence. It does not correct raw source text, converted Markdown, chunk Markdown, or page Markdown."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision keeps the Dario Pulgar evidence staged but not promotion-ready.

## Current Evidence State

The converted chunk contains family-relevant Dario Pulgar passages. Existing staged drafts cover the Chilean descriptor, Chile state film-distribution role under Allende, displacement after the 1973 Pinochet overthrow, Spanish mother tongue, English/French language context, and Vision Habitat distribution-rights/off-shore printing-materials work.

The source packet and six atomic claim drafts already carry `promotion_recommendation: hold_for_conversion_qa`. The negative relationship candidate correctly remains `do_not_promote` because this chunk states no kinship relationship.

## QA Blocker

The blocker remains conversion/page control, not the semantic relevance of the Dario passages:

- `CHUNK-a048d567968b-P0001-03` is assigned to page 1 in the chunk manifest.
- The chunk body contains later converted page metadata and text, including printed/source page 8.
- Prior staged correction notes report visual checks against rendered `page-0007.jpg` and `page-0008.jpg`.
- The conversion job manifest lists those rendered image paths and hashes, but the image files themselves are absent in this checkout, so this worker could not independently repeat visual verification.

## Staging Decision

Do not promote the Dario Pulgar claims from this chunk until conversion QA restores or regenerates the missing rendered page images, visually verifies the family-relevant sentences, and documents the authoritative page citation. Existing staged drafts should remain in staging with `hold_for_conversion_qa`.

No external research was performed, and no raw sources, converted Markdown, chunks, or page Markdown were edited.
