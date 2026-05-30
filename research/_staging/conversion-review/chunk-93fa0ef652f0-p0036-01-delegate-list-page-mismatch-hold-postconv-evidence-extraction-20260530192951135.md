---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-93fa0ef652f0-P0036-01
worker: postconv-evidence-extraction-20260530192951135
source: "raw/sources/R3578-50-5569-5569-Jacket5.pdf"
source_sha256: "09a9828166381d0dbd9fe5fbfebb432548bf6f216d51556bdf77fe23dcce018f"
converted_file: "raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50.codex.md"
converted_sha256: "93fa0ef652f02312ad94cc90d7e82cab2796be38005ce430dad53337580df475"
chunk: "raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50-codex/page-0036-chunk-01.md"
chunk_id: "CHUNK-93fa0ef652f0-P0036-01"
chunk_manifest: "raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50-codex/manifest.json"
page_reference: "source page 36; task page range 36-36"
page_markdown: "raw/codex-conversion-jobs/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50/page-markdown/page-0036.md"
page_image: "raw/codex-conversion-jobs/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50/page-images/page-0036.jpg"
source_packet: "research/_staging/source-packets/chunk-93fa0ef652f0-p0036-01-r3578-jacket5-chile-dario-pulgar-arriagada.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 36 Delegate-List Mismatch

## Review Scope

This note responds to the proof-review revision context for the Dario Pulgar-Arriagada convention evidence. It preserves disagreement between derivative transcripts and does not edit raw sources, converted Markdown, chunks, or page Markdown.

## Derivative Evidence In Conflict

The assigned chunk and converted aggregate contain an English delegate-list page. The family-relevant literal support in those derivatives is:

```text
THE PRESIDENT OF THE REPUBLIC OF CHILE:

 Colonel Guillermo Novoa-Sepulveda, Military Attaché to the
Legation of Chile at Berlin,
 Captain Dario Pulgar-Arriagada, Medical Corps;
```

However, the conversion-job page Markdown for page 36 contains unrelated French medical/prisoner text beginning with impairment and prisoner-of-war medical categories, not the Chile delegate list. It also says conversion QA must compare the output with the rendered page image before research extraction.

The chunk manifest contains duplicate entries for `CHUNK-93fa0ef652f0-P0036-01` with different recorded character counts and sha256 values. The current chunk file hash is `3bb42e33e16f222c28cc474b32e036869eec9ad3825e64eed3a5e8ac09accb04`, which differs from both recorded manifest chunk hashes observed in this worker run.

## Missing Image Blocker

The job manifest references `raw/codex-conversion-jobs/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50/page-images/page-0036.jpg` and marks the page image as deferred. That image path was absent locally during this extraction task, so this worker could not visually resolve whether source page 36 is the delegate list or the French medical/prisoner page.

## Required QA

A conversion-QA worker should locate or regenerate the rendered image for source page 36, compare it against the assigned chunk, aggregate converted Markdown, page Markdown, and manifest, then certify the correct page alignment and literal text.

If the image confirms the delegate list, the staged claims may proceed to proof review as narrow public-role evidence for `Dario Pulgar-Arriagada`, with no family relationship or canonical same-person merge inferred from this page alone.

If the image confirms the French medical/prisoner text or another page, the staged Dario delegate-list claims for this chunk should remain unpromoted and be reassigned to the correct source page/chunk.

## Decision

Keep the page-36 source packet, atomic claims, and identity-support note on `hold_for_conversion_qa`.
