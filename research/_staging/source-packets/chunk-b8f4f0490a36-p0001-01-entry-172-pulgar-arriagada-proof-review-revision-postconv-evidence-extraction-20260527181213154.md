---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527181213154"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register pages 58-59; entry 172 on page 58 per assigned chunk"
entry_number: "172"
family_relevance: high
matched_terms:
  - Pulgar
  - Arriagada
literal_support: "Assigned chunk entry 172 names Jose del Carmen Segundo Pulgar Arriagada, male, born 8 March 1888 at Calle de Valdivia, with father Jose del Carmen Pulgar S. and mother Juana Arriagada de Pulgar."
conversion_confidence: "derivative_conflict_with_prior_image_review_context"
conversion_qa_concern: "Assigned chunk gives the Pulgar/Arriagada row; current converted Markdown gives a Burgos/de la Cruz row. Prior staged conversion QA says the image controls as Pulgar/Arriagada, but this worker cannot independently recertify the absent image."
uncertainty: "Canonical promotion remains blocked until proof review accepts an image-reviewed row-control note or the converted Markdown is corrected. The father field should be limited to Jose del Carmen Pulgar unless the terminal suffix is separately certified."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Revision Hold

This packet stages the family-relevant Pulgar/Arriagada reading for entry `172` while preserving the derivative-source conflict that caused the prior proof-review hold.

## Family-Relevant Reading From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia |
```

## Conflicting Converted Markdown

The current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. That is a different family row from the assigned chunk.

## QA Boundary

The original source image and page image are absent from this checkout, so this worker cannot independently certify the physical row. Earlier staged image-reviewed QA notes report that the image controls as the Pulgar/Arriagada row and limit the father field to visible `Jose del Carmen Pulgar`; those notes should be proof-reviewed before any canonical promotion.

No claim, relationship, identity merge, or wiki update should be promoted from this packet until row control and the father-field boundary are accepted by proof review.
