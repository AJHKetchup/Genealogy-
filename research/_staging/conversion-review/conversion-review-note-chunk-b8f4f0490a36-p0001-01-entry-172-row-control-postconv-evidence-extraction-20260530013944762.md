---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530013944762"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260530013944762.md"
conversion_confidence: image_reviewed_row_control_with_converted_markdown_conflict
conversion_qa_concern: "The current converted Markdown assigns entry 172 to Jose Miguel, son of Oswaldo Burgos and Concepcion de la Cruz; the assigned chunk and prior image-reviewed staging identify physical row 172 as the Pulgar/Arriagada birth row."
literal_support: "Assigned chunk row 172 names Jose del Carmen Segundo Pulgar Arriagada, sex Hombre, born 8 March 1888 at Calle de Valdivia, father Jose del Carmen Pulgar S. in the derivative chunk, mother Juana Arriagada de Pulgar, and informant Ernesto Herrera L."
uncertainty: "For promotable staging, father is bounded to Jose del Carmen Pulgar only; the trailing S. or mark after Pulgar remains uncertified pending proof review."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row Control

This revision preserves the disagreement between the assigned chunk and the current converted Markdown. The assigned chunk for `CHUNK-b8f4f0490a36-P0001-01` places physical row `172` on register page `58` as the Pulgar/Arriagada birth row:

```text
Nombre. Jose del Carmen Segundo Pulgar Arriagada
Sexo. Hombre
Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde
Lugar. Calle de Valdivia
Nombre del padre Jose del Carmen Pulgar S.
Nombre de la madre Juana Arriagada de Pulgar
Ernesto Herrera L. Presente al nacimiento
```

The current converted Markdown instead records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. Treat that as a stale, row-shifted, or wrong-page derivative conflict until conversion QA/proof review resolves it.

For staged family evidence, use the Pulgar/Arriagada row only as held evidence. Bound the father field to `Jose del Carmen Pulgar`; do not promote `Jose del Carmen Pulgar S.` or a suffix expansion until the mark after `Pulgar` is independently certified.

