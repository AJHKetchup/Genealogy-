---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527151911781"
source_title: "Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172"
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
conversion_confidence: "image_reviewed_row_control"
conversion_qa_concern: "Current converted Markdown gives a conflicting Burgos/de la Cruz reading for entry 172; source image and assigned chunk support the Pulgar/Arriagada row. Father field is certified only as Jose del Carmen Pulgar."
uncertainty: "Low for row control and core child/parent facts; moderate for any suffix after the father's surname; high for canonical use until proof review accepts the QA note."
promotion_recommendation: promote_after_review
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages evidence for the birth registration of Jose del Carmen Segundo Pulgar Arriagada. The known family-relevant terms are `Pulgar` and `Arriagada`.

## Literal Support

Assigned chunk:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipí Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipí | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis años Prof Empleado Dom Calle de Valdivia | ... |
```

Current converted Markdown conflict:

```text
Entry 172 ... Nombres. José Miguel ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz
```

## Image-Reviewed Boundary

The original image controls this staging pass. It shows entry `172` on register page 58 as the Pulgar/Arriagada row. The father field is only certified to `Jose del Carmen Pulgar`; the chunk's trailing `S.` is not promoted from this packet.

## Extractable Evidence

The row supports the child's name and sex, birth date/time and place, registration date, father, mother, parental residence, and informant details. Dependent claims and relationship candidates must preserve the derivative-transcript conflict and proceed only through proof review.
