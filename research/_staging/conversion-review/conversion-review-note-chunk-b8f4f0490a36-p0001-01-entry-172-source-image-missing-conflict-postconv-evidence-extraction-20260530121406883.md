---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530121406883"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; disputed entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-held-conflict-postconv-evidence-extraction-20260530121406883.md"
conversion_confidence: "derivative_conflict_unresolved_source_image_missing"
conversion_qa_concern: "Original source image is absent from raw/sources and no conversion-job page image is present, so this worker cannot certify the physical row controlling entry 172."
literal_support: "Assigned chunk row 172 names Jose del Carmen Segundo Pulgar Arriagada, sex Hombre, born 8 March 1888 at Calle de Valdivia, father Jose del Carmen Pulgar S. in the derivative chunk, mother Juana Arriagada de Pulgar, and informant Ernesto Herrera L."
uncertainty: "The current converted Markdown instead assigns entry 172 to Jose Miguel, son of Oswaldo Burgos and Concepcion de la Cruz. Father field for the Pulgar row is bounded to Jose del Carmen Pulgar until the trailing mark/suffix is image-certified."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Image QA Blocked

The requested targeted conversion QA cannot be completed in this worker run because the source PNG named by the chunk metadata is not present in `raw/sources`, and the conversion-job directory has no page image to inspect.

The evidence layers remain in material conflict:

- Assigned chunk: entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Current converted Markdown: entry `172` is `Jose Miguel`, with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`.

Do not treat either derivative layer as row-control-certified. Keep claims and relationships on `hold_for_conversion_qa` until the original page image is restored or located and proof review accepts the row-control finding.
