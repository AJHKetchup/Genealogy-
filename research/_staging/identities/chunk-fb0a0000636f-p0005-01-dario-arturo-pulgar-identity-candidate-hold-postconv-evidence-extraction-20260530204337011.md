---
type: identity_candidate
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530204246348
subject: Dario Arturo Pulgar
identity_basis: source_title_and_document_continuity
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_reference: page 5
confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Identity Candidate: Dario Arturo Pulgar

## Literal Support

The aggregate converted file title identifies the source as `CV of Dario Arturo Pulgar pages 4-9`, and the source file is `raw/sources/CV of Dario Arturo Pulgar.pdf`.

The page-5 chunk body reviewed here contains CV work-history entries but does not repeat the name `Dario Arturo Pulgar`.

## Identity Assessment

This chunk can only support a tentative, document-continuity identity candidate for the CV subject. It should not by itself bridge the page-5 work-history entries to a canonical person page.

## QA Concern

Promotion is blocked because page control is unresolved. The current chunk and aggregate converted file section for page 5 contain 1979-1970 work-history entries, while the conversion job page Markdown for `page-0005.md` contains different 1999/1998 entries. The chunk manifest lists the same page-5 chunk id twice with different character counts and hashes, and no rendered `page-0005.jpg` was found in the checked conversion-job image paths.

## Required Follow-Up

After conversion QA reconciles page 5, perform a separate identity-bridge proof review using a title page, front matter, contact/signature page, or other identity-bearing CV page before attaching any page-5 work-history claims to a canonical Dario Pulgar person page.
