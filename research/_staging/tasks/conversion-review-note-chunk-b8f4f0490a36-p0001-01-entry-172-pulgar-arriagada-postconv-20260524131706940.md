---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524131706940
task_type: conversion_qa
subject: "Entry 172 Pulgar/Arriagada conversion conflict"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172

Run targeted conversion QA against the source image for entry 172. The current chunk supports a Pulgar/Arriagada row, but the assigned converted Markdown supports a conflicting Gomez/de la Cruz row.

QA should explicitly decide:

- whether the controlling entry 172 transcript is the Pulgar/Arriagada row visible in the source image/current chunk;
- whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form;
- whether the father and mother domicile should be cited as `Calle de Colipí` or another source-visible spelling;
- whether the assigned converted Markdown should be corrected, superseded, or marked as assigned to the wrong row.

Until this is done, keep all staged claims and relationships from this entry at `hold_for_conversion_qa`.
