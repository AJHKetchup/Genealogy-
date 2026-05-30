---
type: conversion_review
status: draft
task_id: evidence-extraction:CHUNK-27856e440ba9-P0135-01
worker: postconv-evidence-extraction-20260530202705234
subject: "M. Pulgar-Arriagada (Chili), source page 135"
source: raw/sources/R3577-50-5569-5569-Jacket3.pdf
source_sha256: 24f561d67a2d9ea1cf27814f4f0bb894ff6132a0b2fe0cbe2c03e133d862bc91
converted_file: raw/converted/ca24f561d6-r3577-50-5569-5569-jacke-p0126-0150-r3577-50-5569-5569-jacket3-pages-126-150.codex.md
converted_sha256: 27856e440ba94ce6653ceb8ce1869010182c957b1776badb3afc388022cfc695
chunk: raw/chunks/ca24f561d6-r3577-50-5569-5569-jacke-p0126-0150-r3577-50-5569-5569-jacket3-pages-126-150-codex/page-0135-chunk-01.md
chunk_id: CHUNK-27856e440ba9-P0135-01
page_reference: "source page 135; chunk page_start 135-page_end 135"
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-27856e440ba9-P0135-01-pulgar-arriagada-convention-intervention.md
conversion_confidence: low_to_medium_pending_page_image_qa
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Hold: Page 135 Image Unavailable

## Revision Context

Proof review requested targeted page-image QA before any canonical promotion of the page-135 Pulgar-Arriagada evidence. The specific items needing visual confirmation are:

- speaker heading: `M. Pulgar-Arriagada (Chili) ;`
- intervention text, especially the derivative `jjas` reading in `les brancardiers n'ont jjas partout la meme fonction`
- sentence attributed to the speaker: `dans mon pays, les brancardiers sont combattants...`

## Current Workspace Finding

The conversion metadata references a rendered page image at:

`raw/codex-conversion-jobs/ca24f561d6-r3577-50-5569-5569-jacke-p0126-0150-r3577-50-5569-5569-jacket3-pages-126-150/page-images/page-0135.jpg`

That path is not present in the current workspace. The available local files for page 135 are derivative text/metadata files:

- `raw/codex-conversion-jobs/ca24f561d6-r3577-50-5569-5569-jacke-p0126-0150-r3577-50-5569-5569-jacket3-pages-126-150/page-markdown/page-0135.md`
- `raw/codex-conversion-jobs/ca24f561d6-r3577-50-5569-5569-jacke-p0126-0150-r3577-50-5569-5569-jacket3-pages-126-150/page-markdown/page-0135.visuals.json`
- `raw/codex-conversion-jobs/ca24f561d6-r3577-50-5569-5569-jacke-p0126-0150-r3577-50-5569-5569-jacket3-pages-126-150/work-orders/page-0135.md`

No source-preparation or document-conversion command was run during this extraction revision.

## Evidence Handling

The existing source packet and two atomic claims have been revised to `promotion_recommendation: hold_for_conversion_qa`. Their literal support remains derivative transcript evidence only. The disagreement between derivative transcript and unverified image evidence is preserved: `jjas` is retained as the derivative reading, while `pas` remains only a likely correction to be checked visually.

## Required Next Action

Recover or regenerate the rendered page image through the normal conversion QA workflow, then visually inspect source page 135. After the page-local heading and intervention text are accepted, run a separate identity-bridge proof review against identity-bearing convention records, especially any record that explicitly names `M. Dario Pulgar-Arriagada` with Chile and health-service context.

Until both steps are complete, do not attach these claims to a fuller Dario/Jose candidate or any canonical person page.
