---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528045502562"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, entry 172"
source_type: "civil_birth_registration"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row entry 172"
source_location: "Los Angeles, Circunscripcion de La Laja, Chile"
source_date: "1888-04-07"
family_relevance: "high"
matched_terms: ["Arriagada", "Pulgar"]
conversion_confidence: "image_reviewed_row_control_with_converted_markdown_conflict"
conversion_qa_concern: "Original image and assigned chunk identify physical entry 172 as the Pulgar/Arriagada row; current converted Markdown gives a conflicting Burgos/de la Cruz row."
uncertainty: "Low for row control and core Pulgar/Arriagada birth facts; moderate for any terminal suffix after the father's surname Pulgar."
promotion_recommendation: "promote_after_review"
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

## Person-First Relevance

This birth registration directly supports the Pulgar/Arriagada family narrative by recording a male child's birth, both stated parents, the family domicile, and the compareciente who was present at the birth.

## Literal Support

Assigned chunk:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipi **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipi | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

## Image-Controlled Reading

Direct image review confirms physical row `172` on register page 58 as the Pulgar/Arriagada row. The image supports the child, sex, registration date, birth date/time/place, mother, parent domicile, and compareciente. The father is staged only as `Jose del Carmen Pulgar`; the possible suffix after `Pulgar` is not certified.

## Converted Markdown Conflict

The current converted Markdown describes entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. That derivative transcript conflicts with the original image and assigned chunk for the physical row numbered `172`.

## Promotion Recommendation

`promote_after_review`: promote only after proof review accepts the row-control QA and the limited father-field reading.
