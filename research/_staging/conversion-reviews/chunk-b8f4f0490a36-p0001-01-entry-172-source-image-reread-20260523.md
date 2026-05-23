---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260523181508215
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-jose-del-carmen-segundo-pulgar-arriagada.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Source-Image Reread

## Current Finding

The source image is available at the expected raw source path and was inspected directly in this revision. The visible row for entry 172 on register page 58 supports the Pulgar/Arriagada row, not the entry-172 row in the assigned converted Markdown.

## Source-Image Reread

- Entry number: `172`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`
- Birth place: `Calle de Valdivia`
- Father: visible as `Jose del Carmen Pulgar`; no clear final `S.` suffix was seen in this image reread
- Father's nationality/occupation/residence: `Chileno`; `Empleado`; residence appears to be `Calle de Colipi/Colipí` but exact accent/lettering should remain a QA normalization issue
- Mother: `Juana Arriagada de Pulgar`
- Mother's nationality/occupation/residence: `Chilena`; `Su sexo`; same residence line as father
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at `Calle de Valdivia`

## Derivative Transcript Conflict

The assigned chunk supports the same Pulgar/Arriagada row, but records the father as `Jose del Carmen Pulgar S.`. The assigned converted Markdown file instead reads entry 172 as:

```text
Jose Francisco; father Oswaldo Gomez; mother Emilia de la Cruz; informant Oswaldo Gomez
```

This is a material conflict between the visible source/assigned chunk and the assigned converted Markdown. The conversion QA record should correct or supersede the converted Markdown so the controlling transcript for this task matches the visible source image, and it must explicitly record whether the father field has no suffix, a clear `S.`, or an uncertain suffix.

## Promotion Guidance

Keep all dependent claims, relationship candidates, and identity candidates at `hold_for_conversion_qa` until the converted Markdown conflict is reconciled and the father-name suffix issue is recorded. After QA, rerun proof review for the child birth-name, child-mother, child-father, birth-event, and parent-attribute claims before any canonical promotion or identity merge.
