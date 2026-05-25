---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260525115123585
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; entry 172"
entry_number: "172"
family_relevance: high
matched_terms:
  - Pulgar
  - Arriagada
literal_support: "Current chunk entry 172 records Jose del Carmen Segundo Pulgar Arriagada, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with father Jose del Carmen Pulgar S. and mother Juana Arriagada de Pulgar."
conversion_confidence: mixed
conversion_qa_concern: "Material row-level conflict: the assigned converted Markdown transcribes entry 172 as Jose Francisco, father Oswaldo Gomez, mother Emilia de la Cruz, born veinte i seis de Marzo in En esta. The current chunk transcribes entry 172 as the Pulgar/Arriagada row. Targeted conversion QA must reconcile the source image, converted Markdown, and chunk and explicitly record whether the father field reads Jose del Carmen Pulgar, Jose del Carmen Pulgar S., or Jose del Carmen Pulgar [?]."
uncertainty: "High for canonical readiness because derivative transcripts disagree on the controlling entry-172 row. Medium for the exact father-name ending after Pulgar. Low for family relevance if the current chunk's Pulgar/Arriagada row is confirmed by QA."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet preserves the family-relevant Pulgar/Arriagada evidence from the current chunk while keeping the derivative-transcript conflict explicit.

## Family-Relevant Reading From Current Chunk

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date and time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: chunk reads `Jose del Carmen Pulgar S.`; do not promote an exact father-name form until QA certifies it.
- Mother: `Juana Arriagada de Pulgar`.
- Parent residence: `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, recorded as present at the birth.

## Literal Support

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipí Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipí | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis años Prof Empleado Dom Calle de Valdivia |
```

## Derivative Transcript Conflict

The assigned converted Markdown records a different entry 172: `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born `veinte i seis de Marzo` in `En esta`. The converted file also uses `En esta` for the relevant place/residence fields. This is not a spelling variant; it is a row-level conversion or assignment conflict.

## Promotion Blocker

Keep this packet, all dependent atomic claims, relationships, and identity candidates at `hold_for_conversion_qa`. Targeted conversion QA must reconcile or supersede the converted Markdown, preserve source-visible spellings, and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review before any canonical claim, relationship, parent merge, or Dario-line comparison is promoted.

