---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530044358861"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_confidence: "assigned_chunk_and_existing_staged_crop_assets_reviewed_original_source_missing"
conversion_qa_concern: "The original source PNG is not present under raw/sources in this checkout. The assigned chunk and existing staged crop assets support the Pulgar/Arriagada row, while the current converted Markdown records a different Burgos/de la Cruz entry 172."
promotion_recommendation: hold_for_conversion_qa
---

# Targeted Row-Control QA Note: Entry 172

This worker could not complete a fresh original-image certification because the referenced PNG is not present in `raw/sources/` in this checkout. The review therefore compares the assigned chunk, the current converted Markdown, the chunk manifest, and existing staged crop assets.

## Row-Control Finding

The assigned chunk identifies physical row `172` on register page `58` as the Pulgar/Arriagada birth registration:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at `tres de la tarde`, at `Calle de Valdivia`.
- Father field: preserve only as `Jose del Carmen Pulgar`; the possible trailing suffix after `Pulgar` is not certified here.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

The staged crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png` visibly supports the lower parent/informant fields for the Pulgar/Arriagada row, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`. It does not make the trailing suffix after `Pulgar` promotion-ready.

## Derivative Conflict

The current converted Markdown materially conflicts with the assigned chunk by recording entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. Treat that as a derivative row-control conflict, not as an alternate reading of the Pulgar/Arriagada row.

## Promotion Recommendation

Keep all dependent claims, relationships, identity attachments, and wiki updates at `hold_for_conversion_qa` until a worker with the original page image available certifies the physical row and proof review accepts the row-control resolution.
