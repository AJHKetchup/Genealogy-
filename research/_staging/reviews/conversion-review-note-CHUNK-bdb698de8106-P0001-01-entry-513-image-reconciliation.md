---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entry 513
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 513 Image Reconciliation

## Purpose

This note records the targeted bdb698de entry-513 blocker requested by proof review. It does not edit the raw source, converted Markdown, chunk Markdown, or page Markdown.

## Literal Support

Converted/chunk transcript:

```text
513 | Julio veintidos de mil ochocientos ochenta i nueve | Nombre. Isolina del Carmen José | Sexo. Masculino | Fecha. El mismo veinte dos ... a las cuatro de la mañana | Lugar. Calle Colon | Nombre del padre. José del Carmen Pulgar | Nombre de la madre. Juana de Dios Amador de Pulgar | José del C. Pulgar Padre ... Prof. Agricultor Dom. Calle Colon
```

Direct image-review conflict indicators:

```text
Nombre. [Pulgar Ama... / ... Dami... / José]
Sexo. Masculino
Fecha. Junio veinte i dos ... a las cuatro i media de la tarde [date/time reading uncertain]
Lugar. Calle Colon
Nombre del padre. José del Carmen Pulgar
Nombre de la madre. Juana de Dios Amagada de Pulgar [surname reading uncertain]
José del C. Pulgar / Padre / Edad. Cuarenta i siete Años / Prof. Agricultor / Dom. Calle Colon
```

## Conversion Confidence And QA Concern

The correct chunk path and chunk id are now cited in the staged bdb drafts, but the conversion layer remains unstable for entry 513. The most important conflicts are the child identity, birth date, birth time, and mother surname. The declarant/father name, father role, age, profession, and domicile have stronger image support, but they are still part of the same disputed row.

## Uncertainty

Do not normalize a child name from either `Isolina del Carmen José` or the image-reviewed `Pulgar Ama... / José` reading. Do not promote the parent-child relationship until QA supplies a stable literal transcription for the child field and mother field.

## Promotion Recommendation

`hold_for_conversion_qa`: keep all entry 513 claims and relationship candidates staged until targeted conversion QA resolves the row-level transcription conflict.
