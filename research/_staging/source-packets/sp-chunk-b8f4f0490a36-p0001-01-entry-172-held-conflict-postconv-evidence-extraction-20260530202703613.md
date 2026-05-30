---
type: source_packet
status: draft
source_id: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; entry 172"
entry_number: "172"
jurisdiction: "Los Angeles, Chile"
registration_date: "1888-04-07"
family_relevance: high
matched_terms:
  - "Arriagada"
  - "Pulgar"
literal_support: "Assigned chunk row 172 states: Nombre Jose del Carmen Segundo Pulgar Arriagada; Sexo Hombre; Fecha Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde; Lugar Calle de Valdivia; Nombre del padre Jose del Carmen Pulgar S.; Nombre de la madre Juana Arriagada de Pulgar. Current converted Markdown instead gives entry 172 as Jose Miguel, child of Oswaldo Burgos and Concepcion de la Cruz."
conversion_confidence: "blocked_full_source_image_absent_crop_supported_parent_fields"
conversion_qa_concern: "The full original PNG is absent from raw/sources. Available crop assets support parent and informant fields consistent with Pulgar/Arriagada, but they do not certify the whole physical row, child-name field, inscription number, or row alignment against the current converted Markdown."
uncertainty: "Preserve the father only as Jose del Carmen Pulgar for staged extraction. Do not promote father suffix, parent-child relationships, identity merge, Dario-line attachment, or wiki update until full-image row-control QA and proof review are completed."
promotion_recommendation: hold_for_conversion_qa
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530202703613"
---

# Source Packet: Entry 172 Held Pulgar/Arriagada Birth Evidence

This source packet stages the family-relevant evidence for a possible birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, while preserving the unresolved row conflict.

## Held Reading

The assigned chunk records entry `172` as a male child named `Jose del Carmen Segundo Pulgar Arriagada`, registered on `Siete de Abril de mil ochocientos ochenta i ocho`, born on `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, at `Calle de Valdivia`.

The assigned chunk gives the father as `Jose del Carmen Pulgar S.` and the mother as `Juana Arriagada de Pulgar`. Available staged crop assets support the parent field as `Jose del Carmen Pulgar` with an uncertain trailing mark and support `Juana Arriagada de Pulgar`; they do not certify the complete row or entry number because the full source image is missing.

## Conflict Preserved

The current converted Markdown for the same converted file gives entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. Treat this as a conversion or row-control conflict, not as an identity variant.

## Promotion

Keep this packet and all dependent claims and relationships at `hold_for_conversion_qa` until the original full source image is restored or located, targeted row-control QA certifies the physical row for entry `172`, and proof review accepts the result.
