---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527180532740"
subject: "Entry 172 row-control conflict remains held in this worker because source image is unavailable"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; entry 172"
conversion_confidence: "blocked_missing_source_image"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Hold: Entry 172

This worker could not complete the requested targeted image QA because the source image named in the task and manifest was not available at `raw/sources/...Entry No. 172;.png`, and the manifest's page image `raw/codex-conversion-jobs/.../page-images/page-0001.png` was also absent.

The derivative materials remain in conflict:

- Assigned chunk `CHUNK-b8f4f0490a36-P0001-01` reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- Current converted Markdown reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Earlier staged QA note `research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527151217239.md` reports an image-reviewed Pulgar/Arriagada row and limits the father reading to `Jose del Carmen Pulgar`; this worker could not independently verify that note because the image is unavailable.

Recommendation: keep all newly staged evidence from this worker at `hold_for_conversion_qa`. The next proof review should either inspect an available source image directly or explicitly accept a prior image-reviewed QA note before any canonical promotion.
