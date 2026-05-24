---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524231550559
source_title: "Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172"
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
literal_support: "Current chunk entry 172 names Jose del Carmen Segundo Pulgar Arriagada, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with father Jose del Carmen Pulgar S. and mother Juana Arriagada de Pulgar. Source image review confirms the controlling row is the Pulgar/Arriagada row on register page 58."
conversion_confidence: mixed
conversion_qa_concern: "Material row-level conflict: assigned converted Markdown transcribes entry 172 as Jose Francisco, father Oswaldo Gomez, mother Rosario de la Cruz de la Maza, born 20 February 1888 in Pellin. Current chunk and source image support the Pulgar/Arriagada row. Targeted conversion QA must reconcile or supersede the converted Markdown and explicitly record whether the father field reads Jose del Carmen Pulgar, Jose del Carmen Pulgar S., or Jose del Carmen Pulgar [?]."
uncertainty: "Low for controlling row identity as Pulgar/Arriagada; medium for exact father-name suffix and some residence spelling details; high for canonical readiness until conversion QA and proof review are complete."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This family-relevant birth registration concerns the Pulgar/Arriagada child-parent cluster:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father: `Jose del Carmen Pulgar`, with final suffix or mark after `Pulgar` unresolved for canonical use.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, recorded as present at the birth.

## Literal Support

Assigned chunk support:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia |
```

Source-image review for this extraction pass confirms that register page 58, entry 172 is the Pulgar/Arriagada row. The image supports the child name, mother name, birth date, birth place, registration date, and the core father name `Jose del Carmen Pulgar`; it does not conclusively settle whether a final `S.` or other mark follows the father's surname.

## Derivative Transcript Conflict

The assigned converted Markdown gives a materially different entry 172: `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 20 February 1888 in `Pellin`. This is a row-level conversion or file-assignment conflict, not a spelling variant.

## Promotion Blocker

Keep this source packet and dependent claim, relationship, and identity-analysis drafts at `hold_for_conversion_qa`. Conversion QA should reconcile or supersede the assigned converted Markdown, confirm the controlling entry 172 row from the image, preserve source-visible name and residence spellings, and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical promotion or parent-candidate merge.
