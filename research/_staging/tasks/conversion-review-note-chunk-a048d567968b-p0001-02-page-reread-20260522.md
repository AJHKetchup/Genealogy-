---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-02
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-02.md"
chunk_id: CHUNK-a048d567968b-P0001-02
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
corrected_chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/manifest.json"
page_reference: "assigned manifest says page 1; evidence support belongs to source pages 4 and 5"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: CHUNK-a048d567968b-P0001-02 Page Reread

The assigned chunk is still page-boundary contaminated. Its frontmatter and manifest assign it to page 1, but the body contains later converted page text.

## Reread Findings

- Original PDF text extraction places the Saturna passage on source page 4 and confirms `at my sainted mother's little cottage on Saturna Island (Andreas, Dario, Bo-Eric and I)`.
- Corrected per-page chunk `CHUNK-56159bc5510f-P0004-01` also places the Saturna passage on page 4.
- Original PDF text extraction places the Vancouver group passage on source page 5 and confirms `including Pulgar , Gyborg, Jane Weiner, and Barbara Janes ... and myself`.
- Corrected per-page chunk `CHUNK-56159bc5510f-P0005-01` also places the Vancouver group passage on page 5.
- Same-source identity context appears on source page 2 (`Chiliean/Canadian Dario Pulgar`) and source page 7 (`Dario Pulgar`).
- The local job directory currently contains rendered page images only for pages 7 and 8, so this note does not claim a local page-image reread for pages 4 or 5.

## Recommendation

Do not promote canonical claims from this chunk until conversion QA reconciles the chunk/page assignment. The staged evidence now preserves the disagreement: literal name evidence is supported by original-PDF text extraction and corrected per-page chunks, but the derivative assigned chunk manifest page reference remains wrong.
