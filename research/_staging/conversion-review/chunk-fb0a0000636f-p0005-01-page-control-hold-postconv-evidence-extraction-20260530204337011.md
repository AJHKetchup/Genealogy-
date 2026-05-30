---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530204246348
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
page_reference: page 5
conversion_confidence: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 5 Still Blocked

## Finding

This revision preserves the disagreement between derivative transcripts. The current chunk file and the later aggregate converted-file section for page 5 contain 1979-1970 work-history entries beginning with `United Nations Centre for Human Settlements (HABITAT)`, while the conversion job page Markdown for `page-0005.md` contains different 1999/1998 work-history entries beginning with `National Trust Fund for Protected Areas in Peru (PROFONANPE)`.

## Current Manifest Problem

The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice:

- chunk number 2: `chars` 3731, `sha256` `8665c9a052228707fcc12e17639f8c24771df15fcd8ce7f5c1c64d7858d56329`
- chunk number 5: `chars` 4025, `sha256` `6e1e9af82d55037a291205bb43099a8807647f608b47d7658dc5a1270badc1a0`

The current chunk file frontmatter reports converted SHA-256 `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`; the source PDF SHA-256 is `07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424`.

## Image Blocker

No `page-0005.jpg`, `page-0005.jpeg`, or `page-0005.png` was found under `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/` during this extraction pass. Proof review cannot verify the visible page from the rendered image until that asset is restored or regenerated through the approved conversion QA workflow.

## Required Follow-Up

Reconcile the aggregate converted file, conversion job page Markdown, chunk file, source packet, and chunk manifest so page 5 has one controlling transcription, one chunk id, and one current hash. Restore or regenerate the rendered page image, then rerun targeted proof review against the visible page. After provenance is clean, use this page only for narrow occupational/work-history claims unless a separate identity-bearing CV page bridges `Dario Arturo Pulgar` to a canonical person page.
