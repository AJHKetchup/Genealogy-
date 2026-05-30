---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530102722394"
source_id: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source: "raw/sources/Registro de Nacimientos, CircunscripciÃ³n de Los Ãngeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; claimed physical row entry 172"
entry_number: "172"
family_relevance: high
matched_terms:
  - "Arriagada"
  - "Pulgar"
literal_support: "Assigned chunk entry 172 names Jose del Carmen Segundo Pulgar Arriagada, sex Hombre, born Ocho de Marzo de mil ochocientos ochenta i ocho at about three in the afternoon at Calle de Valdivia, with father transcribed in the chunk as Jose del Carmen Pulgar S. and mother Juana Arriagada de Pulgar."
conversion_confidence: "derivative_conflict_full_image_unavailable"
conversion_qa_concern: "The current converted Markdown assigns entry 172 to Jose Miguel, child of Oswaldo Burgos and Concepcion de la Cruz. The full source PNG for SHA-256 aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2 was not present in raw/sources in this checkout, and the conversion job directory has no page image. Existing crop assets show only parent-field portions and cannot certify the physical row number."
uncertainty: "Do not promote child identity, birth event, parent-child relationships, identity merges, Dario-line attachments, or wiki updates until full-image conversion QA certifies which physical row controls entry 172. Preserve the father field only as Jose del Carmen Pulgar or Jose del Carmen Pulgar [?] until the suffix is visible and certified."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Revision: Entry 172 Pulgar/Arriagada Hold

## Person-First Summary

The family-relevant lead in the assigned chunk is a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, with stated parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

## Assigned Chunk Support

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

## Derivative Conflict

The current converted Markdown for the same source identity records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at `En esta`. This is a row-control conflict, not a name spelling issue.

This pass could not inspect the full original source image because the reported PNG path is absent from `raw/sources`, and the conversion job has no page image directory. Prior crop assets under `research/_staging/conversion-review-assets/` support only portions of the parent field; they do not show enough page context to certify row `172`.

## Promotion Boundary

Keep this packet at `hold_for_conversion_qa`. A conversion-QA worker must restore or locate the full source image, certify the physical row controlling entry `172`, and bound the father-field suffix before proof review considers any canonical claim or relationship.
