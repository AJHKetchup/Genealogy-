---
type: source_packet
status: draft
source_id: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register pages 58-59; disputed entry 172"
entry_number: "172"
jurisdiction: "Los Angeles, Chile"
registration_date: "1888-04-07"
matched_terms:
  - "Arriagada"
  - "Pulgar"
family_relevance: high
literal_support: "Assigned chunk entry 172 reads: Nombre. Jose del Carmen Segundo Pulgar Arriagada; Sexo. Hombre; Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde; Lugar. Calle de Valdivia; Nombre del padre Jose del Carmen Pulgar S.; Nombre de la madre Juana Arriagada de Pulgar; Ernesto Herrera L. Presente al nacimiento."
conversion_confidence: "derivative_conflict_unresolved_source_image_missing"
conversion_qa_concern: "The assigned chunk and current converted Markdown disagree over the same entry number. The chunk gives the Pulgar/Arriagada row, but the converted Markdown gives Jose Miguel, father Oswaldo Burgos, mother Concepcion de la Cruz. The original source image is not present under raw/sources in this checkout, so this worker cannot certify the controlling physical row."
uncertainty: "Treat the Pulgar/Arriagada facts as derivative-supported but not image-certified. Preserve the father field only as Jose del Carmen Pulgar with an uncertified trailing S./mark in the chunk. Do not attach this evidence to a canonical person, relationship, Dario line, identity merge, or wiki page before targeted image QA and proof review."
promotion_recommendation: hold_for_conversion_qa
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530120435692"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-unresolved-row-conflict-postconv-evidence-extraction-20260530120435692.md"
---

# Source Packet: Disputed Entry 172 Pulgar/Arriagada Birth Candidate

## Family-Relevant Summary

The assigned chunk contains high-relevance Pulgar/Arriagada birth evidence. It identifies entry `172` as the birth registration of a male child named `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.

This packet is not promotion-ready. The current converted Markdown for the same converted source assigns entry `172` to a different child and parents: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`. The original source PNG needed for row-control QA is absent from `raw/sources` in this checkout.

## Literal Support From Assigned Chunk

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

## Conflict Preserved

The row-control conflict is material. It is not a spelling difference or a minor transcription uncertainty. Until the original image for SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2` is restored or otherwise available for targeted QA, every dependent claim and relationship must stay on `hold_for_conversion_qa`.

