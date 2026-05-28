---
type: source_packet
status: draft
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, entry 172"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row entry 172"
source_type: "civil_birth_registration"
source_location: "Los Angeles, La Laja, Chile"
source_date: "1888-04-07"
family_relevance: high
matched_terms: ["Arriagada", "Pulgar"]
conversion_confidence: "low_derivative_conflict_image_reviewed"
conversion_qa_concern: "The source image and assigned chunk support the Pulgar/Arriagada row as physical entry 172 on register page 58, while the assigned converted Markdown records a different Burgos/de la Cruz entry 172. Father field is preserved only as Jose del Carmen Pulgar; the trailing S. in the chunk is not certified here."
promotion_recommendation: "hold_for_conversion_qa"
worker: "postconv-evidence-extraction-20260528133324374"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration Revision

This packet stages the family-relevant evidence for physical row `172` on register page 58. The family narrative value is high because the row names Pulgar and Arriagada persons in a birth registration.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

## Image-Reviewed Row Control

Visual review of the original image shows entry number `172` in the middle row of page 58. That physical row contains the Pulgar/Arriagada family, not the Burgos/de la Cruz family in the assigned converted Markdown. The visible father field supports `Jose del Carmen Pulgar`; this revision does not certify a terminal `S.` or other suffix.

## Derivative Conflict

The assigned converted Markdown records entry 172 as child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. That is inconsistent with the original image and current assigned chunk for this task. This packet preserves the conflict rather than normalizing the converted Markdown.

## Promotion Recommendation

Hold for conversion QA and proof review. Do not promote child identity, birth facts, parent-child relationships, identity merges, Dario-line attachments, or wiki updates until the row-control QA is accepted and proof review is rerun.
