---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523183125851
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; converted page-markdown/page-0007.md and page-0008.md contain the Dario Pulgar support; manifest lists page-images/page-0007.jpg and page-0008.jpg, but the page-images directory is absent in the current checkout"
literal_support: "page-0007.md states Dario Pulgar was a dynamic Chilean, had been the number two man in Chile's state film distribution system under Allende, and fled after Pinochet's 1973 overthrow; page-0008.md states `His mother tongue was Spanish` and that Dario worked on distribution rights and off-shore printing materials."
conversion_confidence: medium
conversion_qa_concern: "The family-relevant text agrees between the assigned chunk and the page Markdown for printed pages 7-8, and prior staged notes report visual checks on rendered page images. This worker could not independently repeat the image check because the conversion job has manifest entries for page-0007.jpg/page-0008.jpg but no page-images directory in this checkout. The chunk manifest still assigns the combined chunk to page 1."
uncertainty: "The source text is usable for staged memoir-source claims about Dario Pulgar, but canonical promotion remains blocked until conversion QA restores/regenerates or documents the missing rendered page images and resolves the authoritative page citation."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision preserves the disagreement between derivative transcripts and image-reviewed evidence for `CHUNK-a048d567968b-P0001-03`. I did not edit raw sources, converted Markdown, chunk files, page Markdown, or conversion job files.

## Current Evidence State

- The assigned chunk path is `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md`, and the chunk manifest assigns it to page 1.
- The chunk body includes later page metadata and text for printed/source pages 7, 8, 9, and 10.
- `page-markdown/page-0007.md` contains the full-name Dario Pulgar paragraph, including the Chilean descriptor, Chile state film distribution role, and fleeing after the 1973 Pinochet overthrow.
- `page-markdown/page-0008.md` contains the mother-tongue sentence, English/French language context, Vision Habitat distribution-rights work, and Geneva regional-office context.
- The conversion job manifest lists rendered image paths for `page-images/page-0007.jpg` and `page-images/page-0008.jpg`, but the `page-images` directory is absent in this checkout. Therefore this worker could not independently visually verify those images.

## Revision Applied

Updated the two proof-reviewed claim drafts for Dario Pulgar's Chile film distribution role and Spanish mother tongue so their QA concern explicitly states that current image recheck is blocked by the missing `page-images` directory, while preserving prior notes that reported visual checks.

## Remaining Blocker

Keep related Dario Pulgar claim drafts on `hold_for_conversion_qa`. The blocker is not the substance of the family-relevant text; it is unresolved conversion QA: missing rendered source images in the current checkout plus the page-reference discrepancy between assigned page 1 and support on printed/source pages 7-8.
