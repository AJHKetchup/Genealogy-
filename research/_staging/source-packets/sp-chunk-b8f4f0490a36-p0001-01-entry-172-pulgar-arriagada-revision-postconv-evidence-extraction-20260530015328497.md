---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530015328497"
source_id: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_path: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row entry 172"
entry_number: "172"
jurisdiction: "Los Angeles, Chile"
family_relevance: high
matched_terms:
  - "Pulgar"
  - "Arriagada"
literal_support: "Assigned chunk row 172 records Jose del Carmen Segundo Pulgar Arriagada, male, born 8 March 1888 at three in the afternoon at Calle de Valdivia; father field as transcribed in the chunk is Jose del Carmen Pulgar S.; mother is Juana Arriagada de Pulgar; informant is Ernesto Herrera L., present at the birth."
conversion_confidence: "image_review_context_available_with_derivative_conversion_conflict"
conversion_qa_concern: "Current converted Markdown materially conflicts with the assigned chunk and prior image-review notes by recording entry 172 as Jose Miguel, child of Oswaldo Burgos and Concepcion de la Cruz, born 6 April 1888. The father field for the Pulgar row is staged only to the visible/certified base name Jose del Carmen Pulgar; do not certify a trailing S. from this extraction."
uncertainty: "High for canonical readiness because proof review requested targeted QA followed by proof review before promotion. Medium for the exact father-field ending after Pulgar. Low for family relevance if the Pulgar/Arriagada row remains controlling."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages the family-relevant Pulgar/Arriagada evidence while preserving the unresolved derivative-transcript conflict.

## Image-Reviewed Row Summary

The assigned chunk and prior staged image-review material identify physical row `172` on register page `58` as a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`.

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at about `tres de la tarde`, at `Calle de Valdivia`.
- Father: preserve as `Jose del Carmen Pulgar`; the possible trailing `S.` is not certified here.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, resident at `Calle de Valdivia`.

## Literal Support From Assigned Chunk

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

## Conversion Conflict

The current converted Markdown records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. That is a material row-control conflict, not a spelling variant.

## Promotion Recommendation

Keep this packet and all dependent claims and relationships at `hold_for_conversion_qa`. Rerun proof review before any canonical claim, relationship, identity merge, Dario-line attachment, or wiki update.
