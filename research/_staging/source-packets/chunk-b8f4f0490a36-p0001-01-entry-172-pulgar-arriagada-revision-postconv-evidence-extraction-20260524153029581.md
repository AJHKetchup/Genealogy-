---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524153029581
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
literal_support: "The assigned chunk records entry 172 as the birth registration of Jose del Carmen Segundo Pulgar Arriagada, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with father Jose del Carmen Pulgar S. and mother Juana Arriagada de Pulgar."
conversion_confidence: mixed
conversion_qa_concern: "The assigned converted Markdown transcribes entry 172 as an unrelated Jose Francisco / Oswaldo Gomez / Emilia de la Cruz registration. The current assigned chunk and source image review support the Pulgar/Arriagada row. The father field after Pulgar still requires targeted conversion QA to decide whether the source supports no suffix, a clear S., or an uncertain final mark."
uncertainty: "Low for the row-level Pulgar/Arriagada association in the assigned chunk and image; medium for the father's exact final suffix/mark; high for canonical readiness until conversion QA reconciles or supersedes the converted Markdown."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages the family-relevant evidence for the birth registration recorded as entry 172 on register page 58.

## Family Cluster

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father: `Jose del Carmen Pulgar`, with a possible `S.` or unresolved final mark after `Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, recorded as present at the birth.

## Literal Support

Assigned chunk support:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

Source-image review in this extraction pass supports the controlling row as the Pulgar/Arriagada entry rather than the Gomez/de la Cruz row currently present in the assigned converted Markdown. The image is sufficient to keep family-relevant staged evidence, but not sufficient in this task to settle the father-name suffix for canonical use.

## Derivative Transcript Conflict

The assigned converted Markdown records entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born on `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`, at `En esta`. That is a material row-level conflict with the assigned chunk and image-reviewed evidence, not a spelling variant.

## Promotion Blocker

Keep this source packet and all dependent claim and relationship drafts at `hold_for_conversion_qa`. Targeted conversion QA should reconcile or supersede the converted Markdown and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form such as `Jose del Carmen Pulgar [?]`. After that, rerun proof review on child identity, birth facts, parent-child relationships, parent attributes, and any proposed parent merge.
