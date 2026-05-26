---
type: conversion_review_request
status: draft
review_type: targeted_conversion_qa
subject: "CHUNK-b8f4f0490a36-P0001-01 entry 172"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md"
page_reference: "page 1; register page 58; entry 172"
priority: high
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526170931232"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Targeted Conversion QA Request: Entry 172

## QA Question

Decide whether register page 58, entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and certify the father field only to the extent visible.

## Materials To Reconcile

- Original image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Held source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md`

## Current Extraction Finding

Image review during evidence extraction supports the Pulgar/Arriagada row as entry 172, matching the current chunk. The current converted Markdown conflicts by recording a Burgos/de la Cruz row for entry 172. The father field visibly reads `Jose del Carmen Pulgar` with a trailing mark that appears compatible with `S.`, but this evidence extraction does not certify whether the field should be transcribed as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Required Output

Record the controlling transcription for entry 172 and explicitly classify the father field as one of:

- `Jose del Carmen Pulgar`
- `Jose del Carmen Pulgar S.`
- `Jose del Carmen Pulgar [?]`

After QA, rerun proof review before any canonical child identity, birth facts, parent-child relationships, parent merge, or Dario-line comparison is promoted.
