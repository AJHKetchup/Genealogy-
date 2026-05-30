---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530064417547"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530064417547.md"
literal_support: "Assigned chunk row 172 records Jose del Carmen Segundo Pulgar Arriagada, father Jose del Carmen Pulgar S. in the chunk transcript, and mother Juana Arriagada de Pulgar; current converted Markdown records a Burgos/de la Cruz entry for 172."
conversion_confidence: "partial_from_assigned_chunk_and_existing_crop_assets_original_source_png_not_found"
conversion_qa_concern: "The requested original source PNG is not present under raw/sources in this checkout, so this worker cannot certify the full physical row from the original image."
uncertainty: "The father field is preserved only as Jose del Carmen Pulgar; the possible suffix after Pulgar is not certified."
promotion_recommendation: hold_for_conversion_qa
---

# Targeted Row-Control QA Note: Entry 172

## Scope

Compared the assigned chunk, current converted Markdown, chunk manifest, and existing staged crop assets for `CHUNK-b8f4f0490a36-P0001-01`. The original source PNG with SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2` was not found under `raw/sources/`, so this note cannot satisfy the proof-review request for original-image certification.

## Row-Control Status

The assigned chunk identifies entry `172` on register page `58` as the Pulgar/Arriagada birth registration:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `a las tres de la tarde`, at `Calle de Valdivia`.
- Father: preserve as `Jose del Carmen Pulgar`; the chunk has `Jose del Carmen Pulgar S.`, but the suffix is not certified here.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

Existing crop assets at `research/_staging/conversion-review-assets/` support the Pulgar/Arriagada parent and informant fields, but they are not a substitute for the full original-page row-control check requested by proof review.

## Derivative Conflict

The current converted Markdown materially conflicts with the assigned chunk by recording entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. Preserve this as a row-control conversion conflict. Do not promote either the father suffix or any canonical family relationship until the original-image QA and proof review are complete.
