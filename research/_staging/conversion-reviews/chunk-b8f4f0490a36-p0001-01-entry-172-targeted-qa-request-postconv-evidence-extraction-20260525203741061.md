---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260525203741061
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Targeted QA Request

## Finding

The assigned chunk and source image context support a Pulgar/Arriagada birth row for register page 58, entry 172. The current assigned converted Markdown records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.

This is a material row-level conflict. The current converted Markdown should not be used to promote the Pulgar/Arriagada claims, and the Pulgar/Arriagada chunk should not be promoted until conversion QA reconciles or supersedes the converted file.

## Row To Certify

The assigned chunk gives the entry-172 row as:

- Entry number: `172`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Birth date/time/place: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; `Calle de Valdivia`
- Father: `Jose del Carmen Pulgar S.` in the assigned chunk
- Mother: `Juana Arriagada de Pulgar`
- Informant: `Ernesto Herrera L.`, present at the birth

## Required QA Decision

The conversion QA result should:

1. Identify whether the controlling source row for entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row now in the converted Markdown.
2. If the Pulgar/Arriagada row controls, certify the father field only to the extent visible: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. Record whether the assigned converted Markdown should be corrected, superseded, or treated as a mismatched conversion state.

## Promotion Guidance

Keep all dependent staged evidence at `hold_for_conversion_qa`. After QA, rerun proof review for the child identity, birth facts, parent names, parent-child relationships, and any proposed Pulgar-line comparison.
