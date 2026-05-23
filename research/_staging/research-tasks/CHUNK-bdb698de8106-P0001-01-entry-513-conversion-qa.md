---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
task_type: conversion_qa
priority: high
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entry 513
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
promotion_recommendation: hold_for_conversion_qa
---

# Research Task: Entry 513 Conversion QA

## Question

Reread entry 513 directly from the source image and reconcile the converted transcript against the visible row.

## Fields To Reconcile

- Child name field: converted transcript reads `Isolina del Carmen José`; image review appears closer to `Pulgar Ama... / ... Dami... / José`.
- Birth date/time: converted transcript reads `El mismo veinte dos ... a las cuatro de la mañana`; image review appears closer to `Junio veinte i dos ... a las cuatro i media de la tarde`.
- Mother field: converted transcript reads `Juana de Dios Amador de Pulgar`; image review appears closer to `Juana de Dios Amagada de Pulgar`.
- Declarant profession: verify `Agricultor` against any alternate `Jornalero` reading.

## Expected Output

Produce a corrected conversion-review note or corrected derivative transcription for entry 513, preserving original spelling and marking uncertain letters. Do not promote any child identity, birth event, or parent-child relationship until this QA task is resolved.
