---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527200920411"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register pages 58-59; derivative chunk places entry 172 on register page 58"
entry_number: "172"
jurisdiction: "Los Angeles, Circunscripcion de La Laja, Chile"
family_relevance: high
matched_terms:
  - Arriagada
  - Pulgar
conversion_confidence: "blocked_source_image_missing_derivative_conflict"
conversion_qa_concern: "This worker could not locate the original 1888 entry 172 image in raw/sources under the expected path. The assigned chunk supports the Pulgar/Arriagada row, while the current converted Markdown supports a Burgos/de la Cruz row. Do not promote until targeted conversion QA restores/opens the image and certifies physical row control."
uncertainty: "High for promotion readiness because the original image was unavailable in this pass and the derivative transcripts materially disagree. Father field is no safer than the chunk text and must not be promoted beyond visible/certified support."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages family-relevant evidence for the possible birth registration of Jose del Carmen Segundo Pulgar Arriagada. It preserves a material conflict between the assigned chunk and the current converted Markdown. This worker did not alter raw sources, converted Markdown, chunk files, or page Markdown.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia | Por los testigos: --- Conocido del oficial. | [signature] Emilio Riquelme V. | |
```

## Conflicting Converted Markdown

The current converted Markdown records entry `172` as a different child and parent set:

```text
Entry 172 ... Nombres. Jose Miguel ... Fecha. El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz ... compareciente: Oswaldo Burgos
```

## Evidence Boundary

If the assigned chunk is confirmed against the source image, the row would support the child's recorded name and sex, birth date/time and place, registration date, stated father, stated mother, parents' stated residence/occupation, and informant details. Because the original image was not available in this pass and the converted Markdown conflicts, every dependent claim remains `hold_for_conversion_qa`.

The father field must be preserved only to the level later certified from the visible image. The assigned chunk says `Jose del Carmen Pulgar S.`, but this packet does not promote the suffix.

## Promotion Boundary

Do not promote any canonical claim, relationship, identity merge, Dario-line attachment, or wiki update from this packet until targeted conversion QA opens the original page image, certifies which physical row controls entry `172`, resolves whether the converted Markdown is stale/row-shifted/different-page, and records the father field only to the visible level of certainty.
