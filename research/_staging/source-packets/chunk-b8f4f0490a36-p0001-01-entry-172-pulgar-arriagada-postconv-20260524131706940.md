---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524131706940
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
jurisdiction: "Los Angeles, Circunscripcion de La Laja, Chile"
registration_date: "1888-04-07"
family_relevance: high
matched_terms:
  - Pulgar
  - Arriagada
conversion_confidence: mixed
conversion_qa_concern: "The source image and current assigned chunk support the Pulgar/Arriagada row for entry 172, but the assigned converted Markdown still gives a conflicting Gomez/de la Cruz row for entry 172. The father-name field also requires targeted QA: the current chunk reads Jose del Carmen Pulgar S.; the image appears consistent with Jose del Carmen Pulgar, with any final suffix not clearly resolved in this extraction."
uncertainty: "Low that the visible image and current chunk concern a Pulgar/Arriagada birth entry; high for canonical promotion while the converted Markdown conflict remains unresolved; moderate for whether the father's recorded name includes a final S. suffix."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

Known family-relevant names in this entry are the Pulgar/Arriagada child-parent cluster. The image and the current chunk support a birth registration for Jose del Carmen Segundo Pulgar Arriagada, son of Jose del Carmen Pulgar or Jose del Carmen Pulgar S. and Juana Arriagada de Pulgar. This packet preserves the blocker: the assigned converted Markdown file still transcribes entry 172 as a different Gomez/de la Cruz registration and cannot be used as promotion-ready literal support.

## Literal Support From Current Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

## Conflicting Assigned Converted Markdown

The assigned converted Markdown currently gives entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born in Pellin. That derivative row conflicts materially with the source image and the current chunk.

## Evidence Scope

If conversion QA reconciles the derivative conflict, this source can support the child's recorded name, sex, birth date and time, birth place, registration date, stated father, stated mother, parents' stated nationality/occupation/residence, informant details, and official registration context.

## Current Promotion Blocker

Keep dependent claims and relationship candidates at `hold_for_conversion_qa` until a conversion-review note or corrected/superseding converted Markdown explicitly resolves:

- whether entry 172's controlling transcript is the Pulgar/Arriagada row rather than the Gomez/de la Cruz row;
- whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form;
- whether residence spelling should be cited as `Calle de Colipí` or kept with source orthography from the image/chunk.
