---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530072501797"
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
literal_support: "Assigned chunk row 172 records Jose del Carmen Segundo Pulgar Arriagada, male, born 8 March 1888 at three in the afternoon at Calle de Valdivia; father field transcribed as Jose del Carmen Pulgar S.; mother Juana Arriagada de Pulgar; informant Ernesto Herrera L., present at the birth."
conversion_confidence: "assigned_chunk_and_existing_staged_crop_assets_reviewed_original_source_missing"
conversion_qa_concern: "The current converted Markdown records a different Burgos/de la Cruz entry 172. The original source PNG is not present in raw/sources in this checkout, so this packet preserves the disagreement and does not certify the row for promotion."
uncertainty: "High for promotion readiness because the derivative row-control conflict remains unresolved. Medium for the father-field suffix after Jose del Carmen Pulgar. Low for family relevance if the Pulgar/Arriagada row is confirmed as controlling."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages family-relevant evidence from the assigned chunk for entry `172`, while preserving the conflict between the assigned chunk and the current converted Markdown.

## Family-Relevant Row

The assigned chunk identifies physical row `172` on register page `58` as a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`.

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at `tres de la tarde`, at `Calle de Valdivia`.
- Father: preserve only as `Jose del Carmen Pulgar`; do not promote the possible suffix after `Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, resident at `Calle de Valdivia`.

## Literal Support

Assigned chunk row 172:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

Existing staged crop assets under `research/_staging/conversion-review-assets/` support the Pulgar/Arriagada parent and informant fields at a local crop level. They do not certify a trailing suffix after `Pulgar`, and they do not replace review of the missing original full-page PNG.

## Conversion Conflict

The current converted Markdown records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. That is a row-control conflict, not a spelling variant.

## Promotion Recommendation

Keep this packet and dependent staged claims and relationships at `hold_for_conversion_qa`. Rerun proof review before any canonical claim, relationship, identity merge, Dario-line attachment, or wiki update.
