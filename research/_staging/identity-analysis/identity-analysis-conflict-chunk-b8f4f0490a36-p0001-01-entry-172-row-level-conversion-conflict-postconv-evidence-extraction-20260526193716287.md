---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: evidence_extractor
worker: postconv-evidence-extraction-20260526193716287
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
subject: "Entry 172, Los Angeles birth register, 1888"
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526193716287.md
conversion_review_note: research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526193716287.md
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-26
---

# Identity Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blocker

The assigned chunk and current converted Markdown give incompatible identities for the same entry number. The assigned chunk reads entry 172 as Jose del Carmen Segundo Pulgar Arriagada, child of Jose del Carmen Pulgar and Juana Arriagada de Pulgar. The current converted Markdown reads entry 172 as Jose Miguel, child of Oswaldo Burgos and Concepcion de la Cruz.

This is not a name variant. It changes child identity, birth date, birth time, birthplace, father, mother, and informant.

## Readings Kept Separate

Assigned chunk reading:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.` in the assigned chunk.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

Current converted Markdown reading:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, about `diez de la noche`.
- Birthplace: `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Identity Assessment

The Pulgar/Arriagada row is family-relevant and supports extractable claims only as held drafts. No same-person or duplicate-person hypothesis should be promoted between the Pulgar/Arriagada child and the Burgos/de la Cruz child.

The father field remains specifically unresolved. Do not promote `Jose del Carmen Pulgar S.` as a certified father name until targeted conversion QA confirms the final mark.

## Promotion Recommendation

`hold_for_conversion_qa`. Targeted conversion QA must certify the physical row controlling entry 172 and the father-field reading before renewed proof review. No canonical claim, relationship, parent merge, identity merge, or Dario-line comparison should be promoted from this extraction before that gate.
