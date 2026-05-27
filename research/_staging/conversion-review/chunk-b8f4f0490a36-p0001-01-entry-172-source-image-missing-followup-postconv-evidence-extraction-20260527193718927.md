---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527193718927"
subject: "Entry 172 Pulgar/Arriagada vs Burgos/de la Cruz row conflict"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260527193718927.md"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row numbered 172"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172

## Result

Fresh targeted source-image certification could not be completed in this pass. The source file named by the chunk/task was not present under `raw/sources`, and a local SHA-256 scan of image files under `raw` found no file matching `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`.

## Preserved Disagreement

- Assigned chunk: entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888 at Calle de Valdivia.
- Current converted Markdown: entry `172` is `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888.

## Follow-Up Required

Conversion-control should restore or locate the original page image by source SHA-256, compare it against the assigned chunk and current converted Markdown, and certify:

- whether physical entry `172` is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row;
- whether the current converted Markdown is stale, row-shifted, or sourced from another page/image;
- whether the father field is visibly `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

Until that certification exists and proof review is rerun, all dependent evidence remains `hold_for_conversion_qa`.
