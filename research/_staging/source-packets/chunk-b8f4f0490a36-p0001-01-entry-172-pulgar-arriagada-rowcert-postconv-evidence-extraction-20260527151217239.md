---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527151217239"
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
conversion_confidence: "mixed_derivative_conflict_image_reviewed"
conversion_qa_concern: "Original image and assigned chunk support the Pulgar/Arriagada row for entry 172; current converted Markdown instead gives a Burgos/de la Cruz row. Father field is certified only as Jose del Carmen Pulgar, without promoting a terminal suffix."
uncertainty: "Low that physical row 172 is the Pulgar/Arriagada row; moderate for any father-name suffix after Pulgar; high for promotion readiness until proof review accepts this row-control correction."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages person-first evidence for the birth registration of Jose del Carmen Segundo Pulgar Arriagada. Direct review of the original source image shows entry `172` on register page 58 as the Pulgar/Arriagada row. The row states the child's name and sex, birth date/time and place, parents, and informant.

## Literal Support

Assigned chunk:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipí Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipí | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis años Prof Empleado Dom Calle de Valdivia | ... |
```

Current converted Markdown conflict:

```text
Entry 172 ... Nombres. José Miguel ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz
```

## Image-Reviewed Evidence Boundary

The source image controls over the derivative conflict for this staging pass. It supports `Jose del Carmen Segundo Pulgar Arriagada`, `Hombre`, birth on 8 March 1888 at 3 p.m. at Calle de Valdivia, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`. The father field is not certified beyond `Jose del Carmen Pulgar`; do not promote the chunk's `S.` suffix without focused proof review.

## Promotion Boundary

Keep all claims and relationship candidates from this packet at `hold_for_conversion_qa` until a proof reviewer accepts the targeted conversion QA note and decides whether the converted Markdown must be corrected or superseded.
