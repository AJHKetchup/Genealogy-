---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524212140194
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
literal_support: "The assigned chunk records entry 172 as Jose del Carmen Segundo Pulgar Arriagada, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with father Jose del Carmen Pulgar S. and mother Juana Arriagada de Pulgar."
conversion_confidence: mixed
conversion_qa_concern: "Material row-level conflict: the assigned converted Markdown transcribes entry 172 as Jose Miguel, father Oswaldo Burgos, mother Concepcion de la Cruz, born 6 April 1888 at En esta. The assigned chunk and source image support the Pulgar/Arriagada row. Targeted conversion QA must reconcile or supersede the converted Markdown and explicitly record whether the father field reads Jose del Carmen Pulgar, Jose del Carmen Pulgar S., or Jose del Carmen Pulgar [?]."
uncertainty: "Low for the controlling Pulgar/Arriagada row identity in the source image and current chunk; medium for exact father-name suffix and residence spelling; high for canonical readiness until conversion QA and proof review are complete."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

Known family evidence in this entry centers on the Pulgar/Arriagada child-parent cluster:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father: `Jose del Carmen Pulgar`, with possible final `S.` or unresolved mark after `Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, recorded as present at the birth.

## Literal Support

Assigned chunk support:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

Source-image review in this evidence-extraction pass supports the controlling row as the Pulgar/Arriagada row on register page 58, entry 172. It supports the broad father reading `Jose del Carmen Pulgar`, but this pass does not settle whether a final `S.` or other mark after `Pulgar` is present.

## Derivative Transcript Conflict

The assigned converted Markdown records entry 172 as an unrelated `José Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz` birth at `En esta`. That is a material row-level conflict with the assigned chunk and source-image evidence, not a spelling variant.

## Promotion Blocker

Keep this packet and all dependent claim, identity, relationship, and parent-candidate drafts at `hold_for_conversion_qa`. Targeted conversion QA should reconcile or supersede the converted Markdown, confirm the controlling row, preserve source-visible spellings for names and residences, and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before canonical promotion or any parent-candidate merge.
