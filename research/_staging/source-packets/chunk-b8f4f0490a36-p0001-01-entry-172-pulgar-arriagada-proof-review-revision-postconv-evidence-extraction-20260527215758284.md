---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527215758284"
source_title: "Registro de Nacimientos, Circunscripción de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
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
  - Arriagada
  - Pulgar
conversion_confidence: "image_reviewed_row_control_with_derivative_conflict"
conversion_qa_concern: "The assigned chunk and original image identify entry 172 as the Pulgar/Arriagada row, while the current converted Markdown identifies entry 172 as a Burgos/de la Cruz row. The father field should be preserved only as Jose del Carmen Pulgar plus an unresolved trailing mark/possible suffix until targeted conversion QA and proof review accept a controlled reading."
uncertainty: "Low for controlling physical row and core Pulgar/Arriagada family identity from the image; moderate for the father's trailing suffix; high for canonical promotion while the converted Markdown conflict remains unresolved."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages family-relevant evidence for the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`. It is a proof-review revision packet and does not replace or edit the converted Markdown.

## Literal Support

Assigned chunk:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipí Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipí | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis años Prof Empleado Dom Calle de Valdivia | ... |
```

Current converted Markdown conflict:

```text
Entry 172 ... Nombres. José Miguel ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz
```

## Image-Reviewed Row Control

The original image shows register page 58, entry `172`, as the second physical row on the left page. That row is the Pulgar/Arriagada birth registration, not the Burgos/de la Cruz row found in the current converted Markdown.

The father field is visible as `Jose del Carmen Pulgar` followed by an unresolved trailing mark or possible suffix. This packet does not promote the chunk's `S.` reading as certain.

## Extractable Evidence Held For Review

The row supports draft claims for the child's recorded birth name and sex, registration date, birth date/time/place, named father, named mother, and informant. Because the converted Markdown remains materially conflicting, all dependent claims and relationship candidates from this packet remain `hold_for_conversion_qa`.
