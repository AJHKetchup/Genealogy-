---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524152417501
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; entry 172"
entry_number: "172"
family_relevance: high
matched_terms:
  - Pulgar
  - Arriagada
literal_support: "The source image and assigned chunk support entry 172 as the birth registration of Jose del Carmen Segundo Pulgar Arriagada, male, registered 7 April 1888, born 8 March 1888 about 3 p.m. at Calle de Valdivia, with father Jose del Carmen Pulgar and mother Juana Arriagada de Pulgar."
conversion_confidence: mixed
conversion_qa_concern: "The assigned converted Markdown transcribes entry 172 as an unrelated Jose Francisco / Oswaldo Gomez / Emilia de la Cruz registration. The source image and assigned chunk instead support the Pulgar/Arriagada row. The father field after Pulgar still requires targeted QA to decide whether it has no suffix, a clear S., or an uncertain final mark."
uncertainty: "Low for the Pulgar/Arriagada row identity in the image and assigned chunk; medium for the father's exact ending/suffix and some parent-attribute/residence spellings; high for canonical readiness until conversion QA reconciles or supersedes the converted Markdown."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This source packet concerns the family-relevant birth registration recorded as entry 172 on register page 58. The family cluster supported by the image and assigned chunk is:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father: `Jose del Carmen Pulgar`, with unresolved possible suffix/final mark after `Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, recorded as present at the birth.

## Literal Support

Assigned chunk support:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

Source-image review in this extraction pass supports that entry 172 is the Pulgar/Arriagada row, not the Gomez/de la Cruz row shown in the assigned converted Markdown. The image supports the child name, sex, registration date, birth date and approximate time, birth place, mother, broad father reading, and informant. The exact father-field ending after `Pulgar` is not settled enough for canonical use in this evidence extraction pass.

## Derivative Transcript Conflict

The assigned converted Markdown records entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born on `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`, at `En esta`. That is a row-level conflict with the source image and assigned chunk, not a spelling variant.

## Promotion Blocker

Keep this source packet and all dependent claims at `hold_for_conversion_qa` until targeted conversion QA corrects or supersedes the converted Markdown and explicitly records the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form such as `Jose del Carmen Pulgar [?]`. After that, rerun proof review on the child identity, birth facts, father claim, mother claim, child-parent relationships, parent attributes, and any parent-candidate merge before canonical promotion.
