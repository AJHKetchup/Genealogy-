---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527220554472"
source_title: "Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172"
source_type: "civil_registration_birth"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row entry 172"
entry_number: "172"
jurisdiction: "Los Angeles, Circunscripcion de La Laja, Chile"
family_relevance: high
matched_terms:
  - "Arriagada"
  - "Pulgar"
conversion_confidence: "image_reviewed_row_control"
conversion_qa_concern: "Current converted Markdown gives a conflicting Burgos/de la Cruz reading for entry 172; source image and assigned chunk support the Pulgar/Arriagada physical row. Father field is certified only as Jose del Carmen Pulgar."
uncertainty: "Low for row control, child name, mother name, birth facts, registration date, and informant facts; moderate for any suffix after the father's surname."
promotion_recommendation: "promote_after_review"
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This source packet stages image-reviewed evidence for the birth registration of Jose del Carmen Segundo Pulgar Arriagada. It is family-relevant through the matched `Pulgar` and `Arriagada` names.

## Literal Support

Assigned chunk:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia | ... |
```

Current converted Markdown conflict:

```text
Entry 172 ... Nombres. Jose Miguel ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz
```

## Image-Reviewed Row Control

The original image controls this staging pass. It shows entry `172` on register page 58 as the Pulgar/Arriagada row. The current converted Markdown is stale, row-shifted, or sourced from another page/image for entry `172`.

## Father-Field Boundary

The father field is certified only to the visible reading `Jose del Carmen Pulgar`. The chunk's trailing `S.` is not clearly visible enough for promotion.

## Extractable Evidence

This row supports claims for the child's recorded name and sex, birth date/time and place, registration date, father name, mother name, parental residence/occupation fields, and informant details. All downstream drafts must preserve the converted-Markdown conflict and proceed through proof review before canonical promotion.
