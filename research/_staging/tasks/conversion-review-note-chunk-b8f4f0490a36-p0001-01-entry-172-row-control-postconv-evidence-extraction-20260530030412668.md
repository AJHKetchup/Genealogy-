---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530030412668"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_path: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530030412668.md"
literal_support: "Assigned chunk row 172 names Jose del Carmen Segundo Pulgar Arriagada with father Jose del Carmen Pulgar S. in the derivative chunk transcription and mother Juana Arriagada de Pulgar; current converted Markdown names Jose Miguel with parents Oswaldo Burgos and Concepcion de la Cruz."
conversion_confidence: "image_crop_reviewed_with_missing_original_source_file"
conversion_qa_concern: "The raw source image path did not resolve on disk in this worker session. Existing staged crop assets support the Pulgar/Arriagada parent-field row, but this note therefore remains a staged correction note rather than final canonical QA."
uncertainty: "Father-field suffix after Pulgar remains uncertified. Current converted Markdown appears stale, row-shifted, or sourced from a different image/page relative to the assigned chunk."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row-Control Conflict

The assigned chunk supports treating entry `172` on register page `58` as the Pulgar/Arriagada birth row:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father: `Jose del Carmen Pulgar`; do not certify the trailing suffix after `Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

Existing staged crop assets in `research/_staging/conversion-review-assets/` show the Pulgar/Arriagada parent and informant fields. In this worker session the original source image named in the manifest did not resolve on disk, so this note preserves the crop-supported correction while keeping promotion blocked.

The current converted Markdown conflicts materially by assigning entry `172` to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. Treat that as a conversion/row-control conflict, not an identity variant.

No canonical claim, relationship, identity merge, Dario-line attachment, or wiki update should be promoted before proof review accepts a corrected row-control note.
