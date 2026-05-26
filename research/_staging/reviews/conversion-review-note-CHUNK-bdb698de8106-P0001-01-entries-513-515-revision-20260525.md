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
page_reference: page 1; register page 172; entries 513-515
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entries 513-515 Revision

## Purpose

This revision responds to proof-review requests for the bdb698de chunk. It does not edit the raw source, converted Markdown, chunk Markdown, source packet page text, or canonical wiki pages.

## Citation Status

The assigned chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is present and matches manifest chunk `CHUNK-bdb698de8106-P0001-01`. The remaining blocker is not a missing bdb citation; it is the unresolved field-level conflict between the derivative transcript and image-reviewed evidence.

## Literal Support From Converted/Chunk Transcript

```text
513 ... Nombre. Isolina del Carmen José ... Sexo. Masculino ... Nombre del padre. José del Carmen Pulgar ... Nombre de la madre. Juana de Dios Amador de Pulgar ... José del C. Pulgar Padre ... Edad. Cuarenta i siete Años ... Prof. Agricultor ... Dom. Calle Colon
514 ... Nombre. Riquelme Juan Teodoro ... Nombre del padre. Belisario Riquelme ... Nombre de la madre. Mercedes Riquelme ... Mercedes Riquelme Madre Esposa de Juan Soler
515 ... Nombre. Rosa Elvira del Carmen ... Nombre del padre. Pedro Pablo Leiva ... Pedro Pablo Leiva Padre
```

## Image-Reviewed Conflict Indicators

Existing staged review notes report the following image-reviewed alternatives. These are conflict indicators only and should not replace the transcript without targeted conversion QA:

- Entry 513: child-name field appears closer to a `Pulgar...` / `... José` reading than to converted `Isolina del Carmen José`; mother surname appears closer to `Amagada` than converted `Amador`; birth date/time may differ from the converted line.
- Entry 513: father/declarant line has stronger support for `José del Carmen Pulgar` / `José del C. Pulgar`, father, age forty-seven, agriculturist, Calle Colon, but remains part of the disputed row.
- Entry 514: father field may read `Se ignora` rather than `Belisario Riquelme`; child name, street, and witnesses require direct rereading.
- Entry 515: only the upper portion is visible in the image-reviewed notes; visible child text appears to begin `Rosa Elvira` but the following line is unresolved and appears closer to `Laura de Car...`/`Laura de la Cruz...` than converted `del Carmen`; father/declarant surname appears closer to `Neira` than converted `Leiva`.

## Promotion Recommendation

`hold_for_conversion_qa`: keep the source packet, entry-level claims, relationship candidates, and identity candidates staged. Do not promote, merge, rename, or attach any Pulgar/Juana/Dario identity from this chunk until a targeted conversion-QA note settles entries 513-515 from the source image.
