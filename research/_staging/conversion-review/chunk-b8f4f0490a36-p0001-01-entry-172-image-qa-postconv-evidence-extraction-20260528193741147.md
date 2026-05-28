---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260528193741147
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "image page 1; register pages 58-59; entry 172 on page 58"
promotion_recommendation: promote_after_review
---

# Conversion Review Note: Entry 172 Image QA

## Controlling Physical Row

The controlling row for entry `172` is the middle row on the left-hand page, register page `Páj. 58`. The image row begins with printed entry number `172` and contains the Pulgar/Arriagada birth registration, not the Burgos/de la Cruz registration.

## Image-Reviewed Evidence To Preserve

- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child name and sex: visible as `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth date/time/place: visible as `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place appears as `Calle de Valdivia`.
- Father field: visible as `Jose del Carmen Pulgar`; any trailing suffix after `Pulgar` is not safely certified from this image review.
- Father details: Chilean; occupation appears `Empleado`; domicile line appears to begin `Calle de Col...`, consistent with the assigned chunk's `Calle de Colipí`, but the final letters are not independently certified here.
- Mother field: visible as `Juana Arriagada de Pulgar`; Chilean; profession `Su sexo`; domicile line appears to match the father's domicile line.
- Declarant/compareciente: visible as `Ernesto Herrera L.`, `Presente al nacimiento`, age `Veintiseis años`, occupation `Empleado`, domicile `Calle de Valdivia`.
- Identity check/signature: row uses the printed `Conocido del oficial` path and shows the official signature at right.

## Derivative Transcript Conflict

The current converted Markdown file identifies entry `172` as a different registration: `José Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`. That converted text does not match the source image for this source path and appears stale, row-shifted, or sourced from a different page/image.

The assigned chunk's entry `172` is broadly aligned with the image-reviewed Pulgar/Arriagada row. The only material caution from this QA pass is the father field: preserve it as `Jose del Carmen Pulgar` with an uncertain possible suffix, rather than as the fully certified `Jose del Carmen Pulgar S.`.

## Recommendation

Use this note as targeted conversion QA for entry `172`. Source packets, claims, and relationship candidates may proceed to proof review using the image-reviewed row, but the converted-file conflict and father-suffix uncertainty must remain explicit. Do not edit the raw source, converted Markdown, chunk Markdown, or page Markdown from this evidence-extraction task.
