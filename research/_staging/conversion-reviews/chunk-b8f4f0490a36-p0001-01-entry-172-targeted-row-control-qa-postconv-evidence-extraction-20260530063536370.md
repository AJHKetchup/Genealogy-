---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530063536370"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530063536370.md"
literal_support: "Assigned chunk row 172 gives the Pulgar/Arriagada birth; current converted Markdown gives a Burgos/de la Cruz row for entry 172."
conversion_confidence: "partial_row_control_from_assigned_chunk_and_existing_crop_assets"
conversion_qa_concern: "Original source PNG was not located in raw/sources in this checkout, so this note cannot certify the full physical row from the original image."
uncertainty: "Father field suffix after Pulgar remains unresolved; preserve father only as Jose del Carmen Pulgar until original-image QA certifies more."
promotion_recommendation: hold_for_conversion_qa
---

# Targeted Row-Control QA Note: Entry 172

## Scope

Compared the assigned chunk, current converted Markdown, chunk manifest, and staged crop assets. The original source PNG identified by SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2` was not located under `raw/sources/` during this revision, so the requested original-image certification cannot be completed here.

## Row-Control Finding

The assigned chunk identifies row `172` on register page `58` as the Pulgar/Arriagada birth registration:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, `a las tres de la tarde`, at `Calle de Valdivia`.
- Father: preserve as `Jose del Carmen Pulgar`; the possible suffix after `Pulgar` is not certified.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

The staged crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-bottom-postconv-evidence-extraction-20260529000036877.png` supports the lower parent/informant fields for the Pulgar/Arriagada row. It does not certify the full physical row or the father suffix.

## Derivative Conflict

The current converted Markdown materially conflicts by recording entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. Treat this as a row-control conversion conflict, not as a promoted alternate reading.

## Required Follow-Up

Restore or locate the original PNG and rerun targeted conversion QA against the original image, assigned chunk, current converted Markdown, and this source packet. After that, rerun proof review before any canonical claim, relationship, identity merge, Dario-line attachment, or wiki update.
