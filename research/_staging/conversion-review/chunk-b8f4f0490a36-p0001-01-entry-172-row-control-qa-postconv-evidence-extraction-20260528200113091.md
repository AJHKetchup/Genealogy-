---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528200113091"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528200113091.md"
conversion_confidence: "image_reviewed_row_control_with_converted_markdown_conflict"
conversion_qa_concern: "Current converted Markdown assigns entry 172 to a Burgos/de la Cruz birth; source image and assigned chunk control entry 172 as the Pulgar/Arriagada row."
literal_support: "Physical row 172 on register page 58 contains Jose del Carmen Segundo Pulgar Arriagada; father bounded to Jose del Carmen Pulgar; mother Juana Arriagada de Pulgar; informant Ernesto Herrera L."
uncertainty: "A possible trailing suffix or mark after Pulgar is visible in derivative readings but is not certified from this task's image review."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row Control

Targeted review compared the original page image, assigned chunk, current converted Markdown, and staged source-packet context.

The controlling physical row for entry `172` is the middle row on the left-hand page, register page `Paj. 58`. That row is the Pulgar/Arriagada birth registration, not the Burgos/de la Cruz registration found in the current converted Markdown.

## Certified Boundary

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at about `tres de la tarde`, at `Calle de Valdivia`.
- Father: bounded to `Jose del Carmen Pulgar`; do not certify `S.` or any other suffix from this extraction.
- Father details: Chilean, employed, domiciled at `Calle de Colipi` per the assigned chunk; final domicile letters are lower confidence on the image alone.
- Mother: `Juana Arriagada de Pulgar`; Chilean, `Su sexo`, domiciled at the same `Calle de Colipi` reading from the assigned chunk.
- Informant/compareciente: `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, domiciled at `Calle de Valdivia`.

## Preserved Conflict

The current converted Markdown records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. That derivative text conflicts with the original image for this source and should be treated as stale, row-shifted, or sourced from a different page/image until conversion QA resolves it.

Because proof review specifically requested QA followed by rerun proof review before canonical promotion, all dependent claims and relationship candidates from this worker remain `hold_for_conversion_qa`.
