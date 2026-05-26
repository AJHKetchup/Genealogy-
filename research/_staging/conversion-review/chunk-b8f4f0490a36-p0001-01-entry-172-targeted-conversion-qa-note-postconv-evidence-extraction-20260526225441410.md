---
type: conversion_review_note
status: draft
review_type: targeted_conversion_qa
subject: "Entry 172 row control and father-field reading"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: promote_after_review
worker: "postconv-evidence-extraction-20260526225338422"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Targeted Conversion QA: Entry 172

## Materials Compared

- Original source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Chunk manifest: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json`
- Prior proof-review revision requests listed for this task.

## Finding

The controlling physical row for entry `172` is the middle row on the left page, register page 58. The visible row is the Pulgar/Arriagada birth registration, not the Burgos/de la Cruz row currently recorded in the converted Markdown.

The current converted Markdown is stale, mismatched, or otherwise sourced from a different row set for this image. It gives entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the source image and assigned chunk show entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

## Certified Entry 172 Reading

- Registration number: `172`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`
- Birth place: `Calle de Valdivia`
- Father: `Jose del Carmen Pulgar`
- Father details: `Chileno`; `Empleado`; `Calle de Colipi`
- Mother: `Juana Arriagada de Pulgar`
- Mother details: `Chilena`; `Su sexo`; `Calle de Colipi`
- Declarant/informant: `Ernesto Herrera L.`, present at the birth; age twenty-six; employed; domiciled on `Calle de Valdivia`.

## Father-Field Certification

The father field is certified only as `Jose del Carmen Pulgar`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the image does not support promotion of the trailing mark as a definite `S.`. Preserve the suffix question in notes; do not promote it as part of the father's name from this extraction.

## Promotion Gate

Use the image-reviewed Pulgar/Arriagada row for staged evidence from this task. Preserve the conflict with the current converted Markdown in dependent drafts. Rerun proof review before any canonical claim, relationship, identity merge, parent merge, Dario-line attachment, or wiki update.
