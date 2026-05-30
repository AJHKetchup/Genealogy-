---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530015328497"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_path: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530015328497.md"
literal_support: "Assigned chunk row 172 names Jose del Carmen Segundo Pulgar Arriagada with father Jose del Carmen Pulgar S. in the derivative chunk transcription and mother Juana Arriagada de Pulgar; current converted Markdown names Jose Miguel with parents Oswaldo Burgos and Concepcion de la Cruz."
conversion_confidence: "image_review_context_available_with_derivative_conversion_conflict"
conversion_qa_concern: "Prior proof review requested targeted row-control QA. This revision preserves the row-control conflict and bounds the father field to Jose del Carmen Pulgar only; it does not certify the trailing S. as visible."
uncertainty: "The repository contains prior staged image-review notes and parent-field crop assets supporting the Pulgar/Arriagada row, but the raw source image path was not directly openable under the task filename in this worker session. Proof review should use the existing image-review note and/or the original image to decide final promotion."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row-Control Conflict

The assigned chunk and prior staged image-review material support treating physical row `172` on register page `58` as the Pulgar/Arriagada birth row:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `tres de la tarde`, at `Calle de Valdivia`.
- Father: bounded here to `Jose del Carmen Pulgar`; the possible suffix after `Pulgar` remains uncertified.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

The current converted Markdown conflicts materially by assigning entry `172` to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. Preserve that as a conversion conflict.

Because proof review explicitly required conversion QA followed by proof review, this worker's dependent packet, claims, and relationship candidates remain at `hold_for_conversion_qa`. No canonical claim, parent relationship, identity merge, Dario-line attachment, or wiki update should be promoted from this extraction alone.
