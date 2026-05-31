---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530235954849
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded_in_chunk: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_reference: page 5
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 5 Control Blocker

This evidence extraction pass did not edit raw sources, converted Markdown, chunks, source-prep page Markdown, or canonical wiki files.

## Blocker

Physical page 5 is not under reliable page control. The assigned chunk currently preserves a 1979-1970 work-history page, while another page-5 derivative transcription in the aggregate converted file preserves a 1999-1997 consulting-work page. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice with different character counts and hashes. Observed hashes for the aggregate converted file and current chunk do not match the metadata recorded in the chunk frontmatter or manifest.

No rendered `page-0005.jpg`, `.jpeg`, or `.png` was found under the conversion job path during this pass.

## Required Next Action

Run conversion QA outside this evidence-extraction task:

- Restore or regenerate the authoritative physical page-5 image from `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- Compare the physical page image against both derivative readings.
- Repair the duplicate manifest/chunk metadata and recorded hash drift through the conversion workflow.
- Certify the controlling page-5 transcription before proof review promotes any page-5 occupational or identity claim.

After page control is certified, run a separate identity-bridge proof review before attaching the accepted CV subject to `Dario Arturo Pulgar-Smith` or to any Pulgar-Arriagada/Jose/Juana cluster.
