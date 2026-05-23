---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523181145771
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1 in chunk frontmatter/manifest; converted chunk body contains later page metadata/text and family-relevant support reported on rendered/printed pages 7 and 8"
literal_support: "Converted chunk text supports Dario Pulgar as a Chilean colleague, his Chile state film distribution role under Allende, his flight after Pinochet's 1973 overthrow, his Spanish mother tongue, his English/French language context, and his Vision Habitat distribution-rights/off-shore printing-materials work."
conversion_confidence: medium
conversion_qa_concern: "The converted text is internally readable and prior staged notes report image review on page-0007.jpg and page-0008.jpg, but this checkout lacks the conversion job page-images directory, so the page-8 mother-tongue sentence cannot be independently reverified here. The larger unresolved blocker remains derivative page control: the chunk manifest assigns page 1 while the evidence belongs to later embedded converted pages."
uncertainty: "This note preserves disagreement between derivative transcript metadata and previously image-reviewed evidence. It does not alter raw sources, converted Markdown, chunks, page Markdown, or canonical wiki pages."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision rechecks the proof-review blockers for `CHUNK-a048d567968b-P0001-03` from the current filesystem state and existing staging trail.

## Current State

- The assigned chunk and chunk manifest still identify `page-0001-chunk-03.md`, with `page_start: 1` and `page_end: 1`.
- The chunk body contains later converted page metadata and text, including printed/source page 8 language material and following page text.
- The conversion job manifest lists rendered image paths for `page-0007.jpg` and `page-0008.jpg`, but the `page-images` directory is not present in this checkout. `Test-Path` returned false for the directory and for both expected image files.
- Earlier staged correction notes report that `page-0007.jpg` visually supported the Dario Pulgar full-name/Chile-film/fleeing-1973 paragraph and that `page-0008.jpg` visually supported `His mother tongue was Spanish` and the Vision Habitat distribution-rights passage. This revision preserves those notes as prior image-review evidence but cannot independently repeat the check.

## Extraction Judgment

The existing source packet, Dario Pulgar atomic claim drafts, and negative relationship note remain useful staged evidence, but the promotable Dario claims should stay on `hold_for_conversion_qa`.

The active blocker is not the substance of the converted Dario text; it is citation and conversion control. The chunk metadata assigns page 1, the body includes later printed/source pages, and the rendered images needed for direct recheck are absent from this checkout. Conversion QA should restore or regenerate the rendered images and reconcile the authoritative page references before any Dario Pulgar claims from this chunk are promoted.

No family relationship is stated in the chunk. The existing negative-evidence relationship draft remains `do_not_promote`.
