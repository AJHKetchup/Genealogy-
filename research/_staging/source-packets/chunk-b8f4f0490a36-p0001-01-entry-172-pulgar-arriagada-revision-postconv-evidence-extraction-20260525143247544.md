---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260525143247544
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
literal_support: "Current chunk entry 172 records Jose del Carmen Segundo Pulgar Arriagada, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with father read in the chunk as Jose del Carmen Pulgar S. and mother Juana Arriagada de Pulgar."
conversion_confidence: mixed
conversion_qa_concern: "The assigned converted Markdown records entry 172 as Jose Francisco, child of Oswaldo Gomez and Emilia de la Cruz, born veinte i seis de Marzo at En esta. This conflicts with the current chunk and requires targeted conversion QA before promotion."
uncertainty: "High for canonical readiness because the derivative transcript and chunk disagree. The father-field ending after Pulgar also remains unresolved until image-level QA."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages family-relevant Pulgar/Arriagada evidence while preserving the unresolved conflict between the current chunk and the assigned converted Markdown. No raw source, converted Markdown, chunk, or page Markdown was edited.

## Current Chunk Reading

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth date and time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: chunk reads `Jose del Carmen Pulgar S.`; exact ending requires QA.
- Mother: `Juana Arriagada de Pulgar`.
- Parent residence: `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, recorded as present at the birth.

## Literal Support

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipí Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipí | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis años Prof Empleado Dom Calle de Valdivia |
```

## Conversion Conflict

The assigned converted Markdown records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born `El veinte i seis de Marzo de mil ochocientos ochenta i ocho` at `En esta`. This is a mutually exclusive entry-172 identity, not a spelling variant.

## Promotion Recommendation

Keep this packet and all dependent claims, relationship candidates, parent candidates, identity comparisons, and Dario-line comparisons at `hold_for_conversion_qa`. Targeted conversion QA must decide whether the controlling entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row, and must record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review after QA before promotion.
