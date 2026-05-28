---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528221606420"
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
conversion_qa_concern: "Original image and assigned chunk support physical row 172 as the Pulgar/Arriagada birth registration. Current converted Markdown records a different Burgos/de la Cruz entry 172."
literal_support: "Row 172 records Jose del Carmen Segundo Pulgar Arriagada, male, born 8 March 1888 at about three in the afternoon at Calle de Valdivia, father Jose del Carmen Pulgar, mother Juana Arriagada de Pulgar, registered 7 April 1888."
uncertainty: "Low for row control and core birth details; moderate for any father-name suffix after Pulgar. Canonical use still requires proof review."
promotion_recommendation: "promote_after_review"
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages family-relevant evidence for the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`.

## Literal Support

Assigned chunk:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. ... Nombre de la madre Juana Arriagada de Pulgar ... | Ernesto Herrera L. Presente al nacimiento ... |
```

Current converted Markdown conflict:

```text
Entry 172 ... Nombres. Jose Miguel ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz
```

## Image-Reviewed Row Control

The original source image supports the assigned chunk's physical row numbering: entry `172` on register page 58 is the Pulgar/Arriagada row. The Burgos/de la Cruz text in the converted Markdown is preserved as a conversion conflict and is not used for the staged family claims.

## Father-Field Boundary

The father field is staged only as `Jose del Carmen Pulgar`. The possible terminal suffix after `Pulgar`, including the assigned chunk's `S.`, remains unresolved and should not be promoted without proof review.
