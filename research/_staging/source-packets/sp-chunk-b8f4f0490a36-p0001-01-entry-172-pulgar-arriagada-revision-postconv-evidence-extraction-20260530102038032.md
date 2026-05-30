---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530102038032"
source_id: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_path_reported: "raw/sources/Registro de Nacimientos, CircunscripciÃ³n de Los Ãngeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; claimed physical row entry 172"
entry_number: "172"
source_identity: "Held Pulgar/Arriagada birth registration lead for Jose del Carmen Segundo Pulgar Arriagada"
jurisdiction: "Los Angeles, Chile"
registration_date: "1888-04-07"
family_relevance: high
matched_terms:
  - "Arriagada"
  - "Pulgar"
literal_support: "Assigned chunk entry 172 names Jose del Carmen Segundo Pulgar Arriagada, sex Hombre, born Ocho de Marzo de mil ochocientos ochenta i ocho at about three in the afternoon at Calle de Valdivia, with father Jose del Carmen Pulgar S. in the derivative chunk transcript and mother Juana Arriagada de Pulgar."
conversion_confidence: "assigned_chunk_and_parent-field_crop_support_but_full_source_image_absent"
conversion_qa_concern: "Current converted Markdown assigns entry 172 to Jose Miguel, child of Oswaldo Burgos and Concepcion de la Cruz. The original full source image is absent from raw/sources in this checkout, so this pass cannot newly certify which physical row controls entry 172."
uncertainty: "Preserve the father only as Jose del Carmen Pulgar in dependent drafts. The possible suffix or mark after Pulgar is not certified. No canonical claim, relationship, identity merge, Dario-line attachment, or wiki update is warranted before targeted full-image QA and proof review."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Hold

## Person-First Summary

The family-relevant people in the assigned chunk's entry `172` are the child `Jose del Carmen Segundo Pulgar Arriagada`, stated father `Jose del Carmen Pulgar`, and stated mother `Juana Arriagada de Pulgar`.

## Literal Support From Assigned Chunk

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

## Conversion Conflict

The current converted Markdown for the same source identity records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. That is a row-control conflict, not a name variant.

Two staged crop assets under `research/_staging/conversion-review-assets/` show parent-field handwriting consistent with `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, but they do not show enough of the page to certify the entry number or full physical row in this pass.

## Promotion Boundary

Hold this packet and dependent claims at `hold_for_conversion_qa` until the full source image is restored or located, row `172` is visually certified, and proof review accepts the bounded father-field reading.
