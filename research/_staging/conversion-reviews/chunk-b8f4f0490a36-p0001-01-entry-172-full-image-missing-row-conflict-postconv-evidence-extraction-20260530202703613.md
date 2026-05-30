---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530202703613"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-held-conflict-postconv-evidence-extraction-20260530202703613.md"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
literal_support: "Assigned chunk entry 172 gives Jose del Carmen Segundo Pulgar Arriagada, son of Jose del Carmen Pulgar S. and Juana Arriagada de Pulgar. Current converted Markdown entry 172 gives Jose Miguel, son of Oswaldo Burgos and Concepcion de la Cruz."
conversion_confidence: "blocked_original_full_source_image_missing"
conversion_qa_concern: "The proof-review requested row-control QA cannot be completed in this task because the original full PNG is absent from raw/sources in this checkout. Available crop assets support Pulgar/Arriagada parent and informant fields, but they do not certify the full physical row, entry number, or row alignment against the conflicting converted Markdown."
uncertainty: "Father field should be preserved only as Jose del Carmen Pulgar for staged extraction; do not promote the chunk's trailing S. or any parent-child relationship until full-image QA and proof review."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row Conflict Remains Held

The assigned chunk and chunk manifest identify `CHUNK-b8f4f0490a36-P0001-01` as the only chunk for the converted source. The assigned chunk transcribes register page 58, entry `172`, as the Pulgar/Arriagada birth registration. The current converted Markdown for the same converted file transcribes entry `172` as a different Burgos/de la Cruz birth registration.

The expected original source image with SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2` is not present under `raw/sources` in this checkout. The conversion job directory contains work order and page Markdown files but no full page image. Two staged crop assets are available and show parent/informant fields consistent with the Pulgar/Arriagada row, but those crops are insufficient to certify the complete physical row and entry number.

Result: keep all dependent source packets, claims, relationships, identity analysis, and wiki work at `hold_for_conversion_qa`. A later QA worker should restore or locate the full source image, compare it to the assigned chunk and converted Markdown, certify which physical row controls entry `172`, and record the father field only to the visible level of certainty.
