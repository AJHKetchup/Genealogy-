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
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: promote_after_review
worker: "postconv-evidence-extraction-20260526230112215"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Targeted Conversion QA: Entry 172

## Materials Compared

- Original source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Chunk manifest: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json`
- Prior staged source packets and proof-review revision requests for this chunk.

## Finding

The controlling physical row for entry `172` is the middle row on the left page, register page 58. The row is the Pulgar/Arriagada birth registration, not the Burgos/de la Cruz row in the current converted Markdown.

The current converted Markdown is stale, row-shifted, or from a different image/page set for this source. It records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the source image and assigned chunk instead show entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

## Certified Reading

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
- Declarant: `Ernesto Herrera L.`, present at the birth; age twenty-six; employed; domiciled on `Calle de Valdivia`

## Father-Field Certification

The father field is certified only as `Jose del Carmen Pulgar`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the visible mark after `Pulgar` is not clear enough to promote as a definite `S.` from this extraction. Preserve the suffix question in notes and do not attach it to the father name in canonical claims without proof-review acceptance.

## Promotion Gate

Use the image-reviewed Pulgar/Arriagada row for staged evidence from this task and preserve the derivative-transcript conflict. Proof review is still required before any canonical claim, relationship, identity merge, parent merge, Dario-line attachment, or wiki update.
