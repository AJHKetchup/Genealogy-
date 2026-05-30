---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530203527240
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

# Conversion Review Note: Page 5 Control Blocker

## Finding

The staged evidence for `CHUNK-fb0a0000636f-P0005-01` should remain on hold. The chunk file and the aggregate converted file section for page 5 contain 1979-1970 work-history entries beginning with `United Nations Centre for Human Settlements (HABITAT)`, while the conversion job page Markdown for `page-0005.md` contains different 1999/1998 work-history entries beginning with `National Trust Fund for Protected Areas in Peru (PROFONANPE)`.

## Additional QA Concerns

- The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice, with different character counts and sha256 values.
- Checked image locations did not contain `page-0005.jpg`, so this extraction could not rerun proof review against a visible page image.
- The page body reviewed in the chunk does not restate `Dario Arturo Pulgar`; subject attachment depends on the CV title and document continuity after page control is fixed.

## Required Follow-Up

Reconcile the aggregate converted file, conversion job page Markdown, current chunk file, source packet, and chunk manifest so page 5 has one controlling transcription, one chunk id, and a current hash. Restore or regenerate the page image for proof review. After provenance is clean, use this page only for narrow CV work-history claims unless a separate identity-bearing page bridges the CV subject to a canonical person.
