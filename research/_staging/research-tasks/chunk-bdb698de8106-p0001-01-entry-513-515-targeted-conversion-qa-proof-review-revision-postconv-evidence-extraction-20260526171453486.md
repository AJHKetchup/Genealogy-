---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526171453486
task_type: conversion_qa
priority: high
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entries 513 and 515
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526171453486.md
promotion_recommendation: hold_for_conversion_qa
---

# Research Task: Targeted Conversion QA For Entries 513 And 515

## Question

Reconcile the assigned converted transcript against the source image for entry 513 and the partial entry 515 before any canonical promotion.

## Fields To Reconcile

- Entry 513 child-name field: converted transcript reads `Isolina del Carmen` plus `José`; image-review notes report a conflicting Pulgar-style child-name field and a `José` line.
- Entry 513 birth date/time/place: confirm whether the converted `El mismo veinte dos ... a las cuatro de la mañana` and `Calle Colon` are accurate.
- Entry 513 parents: confirm father `José del Carmen Pulgar`; reconcile mother surname currently converted as `Juana de Dios Amador de Pulgar` against image-review alternatives.
- Entry 513 declarant: verify `José del C. Pulgar`, `Padre`, age forty-seven, occupation `Agricultor`, and `Calle Colon`.
- Entry 515 child name: reconcile converted `Rosa Elvira del Carmen` against the partial visible row without replacing the transcript by inference.
- Entry 515 father/declarant surname: verify whether converted `Pedro Pablo Leiva` is supported by the visible source image.

## Expected Output

Produce a corrected conversion-review note or corrected derivative transcription with uncertain letters marked. Keep existing claims and relationships on `hold_for_conversion_qa` until proof review can evaluate the reconciled text.
