---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527221218880"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
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
conversion_qa_concern: "Current converted Markdown assigns entry 172 to a Burgos/de la Cruz row. The original image and assigned chunk support the Pulgar/Arriagada physical row. The father field is certified only as Jose del Carmen Pulgar; any trailing suffix or mark is not promoted."
uncertainty: "Low for row control and core Pulgar/Arriagada birth evidence; moderate for any suffix after the father's surname; proof review is still required before canonical promotion."
promotion_recommendation: "promote_after_review"
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages family-relevant evidence for the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`.

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

The original source image is available and controls this staging pass. On register page 58, physical row `172` is the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the current converted Markdown.

## Father-Field Boundary

The father field is staged only as `Jose del Carmen Pulgar`. The assigned chunk's trailing `S.` is treated as an unresolved possible suffix and is not promoted from this packet.

## Extractable Evidence

This row supports atomic drafts for the child's recorded name and sex, birth date/time/place, registration date, father name, mother name, and informant details. The row-control conflict with the converted Markdown is preserved in every dependent draft; canonical use requires proof review.
