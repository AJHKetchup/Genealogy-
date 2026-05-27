---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527203428889"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; derivative entry 172"
entry_number: "172"
family_relevance: high
matched_terms:
  - Arriagada
  - Pulgar
conversion_confidence: "blocked_no_source_image_available"
conversion_qa_concern: "The source image path and the conversion job page image are absent in this checkout. The assigned chunk reads entry 172 as the Pulgar/Arriagada row, while the current converted Markdown reads entry 172 as a Burgos/de la Cruz row."
uncertainty: "High for physical row control and father suffix. The chunk supports a family-relevant Pulgar/Arriagada extraction, but the derivative conflict prevents promotion until targeted conversion QA can inspect the image."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration Hold

This packet stages the family-relevant Pulgar/Arriagada reading from the assigned chunk, but does not promote it. The expected raw source image and the page image named in the conversion manifest were not present in this checkout, so this worker could not certify the physical row controlling entry `172`.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia | ... |
```

## Conflicting Converted Markdown

```text
Entry 172 ... Nombres. Jose Miguel ... Fecha. El seis de Abril de mil ochocientos ochenta i ocho ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz ... [Name]: Oswaldo Burgos
```

## Extraction Boundary

The chunk's Pulgar/Arriagada row is family-relevant and supports held claim drafts for the child, birth event, registration date, parents, and informant. However, the current converted Markdown is incompatible with that row. The father field must not be normalized beyond the derivative reading `Jose del Carmen Pulgar S.` until the image is restored or another image-backed QA note is accepted by proof review.

