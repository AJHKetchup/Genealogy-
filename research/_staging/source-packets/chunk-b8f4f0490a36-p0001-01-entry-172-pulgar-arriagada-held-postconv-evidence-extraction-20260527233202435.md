---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527233106550"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
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
conversion_qa_concern: "The image and assigned chunk support a Pulgar/Arriagada row for entry 172, but the current converted Markdown gives an incompatible Burgos/de la Cruz row."
uncertainty: "Low for the controlling image row and core Pulgar/Arriagada names; moderate for the father's trailing suffix; not promotion-ready until proof review accepts the row-control reconciliation."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages family-relevant evidence for `Jose del Carmen Segundo Pulgar Arriagada`, a child recorded in birth-registration entry `172` on register page 58.

## Literal Support

Assigned chunk:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia |
```

Current converted Markdown conflict:

```text
Entry 172 ... Nombres. Jose Miguel ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz
```

## Row-Control Boundary

Image review confirms that physical row `172` is the Pulgar/Arriagada row. The father field is staged only as `Jose del Carmen Pulgar` plus an unresolved possible suffix or terminal mark. The chunk's `S.` reading is preserved as derivative text, not as a certified name element.

## Extraction Boundary

The source supports held claims for the child's recorded name and sex, birth date/time/place, registration date, father field, mother field, and informant. All dependent claims and relationship candidates remain `hold_for_conversion_qa` pending proof review of the image-versus-converted-file conflict.
