---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525205450696
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md
reviewed:
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - research/_staging/tasks/conversion-review-note-chunk-b8f4f0490a36-p0001-01-entry-172-image-reread.md
  - wiki/people/dario-arturo-pulgar-smith.md
  - wiki/people/dar-o-pulgar-arriagada.md
  - wiki/people/jose-del-carmen-pulgar.md
  - wiki/people/juana-arriagada-de-pulgar.md
  - wiki/people/juana-de-dios-amagada-de-pulgar.md
  - wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md
  - wiki/people/dario-pulgar-adult-passenger-age-64.md
  - wiki/people/dario-pulgar-child-passenger-age-11.md
conflict_type: conversion_row_conflict
subject: "Register page 58 entry 172"
identity_confidence_score: 0.56
conflict_severity_score: 0.92
evidence_quality_score: 0.74
conversion_confidence_score: 0.30
claim_probability: 0.62
relevance_score: 0.86
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Identity And Conflict Analysis: Entry 172 Row Conflict

This note reviews the exact staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md`.

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The assigned chunk and source packet describe entry 172 as a Pulgar/Arriagada birth registration, while the current converted Markdown describes entry 172 as a Burgos/de la Cruz birth registration. This is a row-level conflict, not a same-person, spelling, or name-variant conflict.
- No child identity, birth event, parent-name claim, child-parent relationship, parent-pair clue, duplicate-person decision, canonical merge, or Dario-line comparison should be promoted from this draft.
- The father field in the Pulgar/Arriagada reading is unresolved at proof-review precision. The assigned chunk reads `Jose del Carmen Pulgar S.`; the image-reread note says the visible field is readable as `Jose del Carmen Pulgar` and that a final `S.` is not clearly visible.
- Existing canonical Pulgar context contains multiple unresolved or distinct Dario/Pulgar clusters. This entry does not name Dario, Arturo, Smith, Dario Jose, or any later-life Dario context, so it cannot bridge `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or passenger-list Dario Pulgar candidates.
- Existing wiki pages for `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` show possible parent-name context, but the entry-172 row conflict and father-field uncertainty block any parent merge or silent correction.

## Literal Evidence

The assigned chunk transcribes entry 172 on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.

The current converted Markdown transcribes entry 172 as `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`, with father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

The reviewed image-reread note supports the Pulgar/Arriagada row for child name, sex, registration date, birth date/time, birthplace, mother, informant, and official, but keeps the father suffix after `Pulgar` unresolved.

## Hypotheses

| Rank | Hypothesis | Probability | Identity confidence | Evidence supporting | Evidence against / limits |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | Entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.62 | 0.56 | Assigned chunk, source packet, and prior image-reread note align on the Pulgar/Arriagada child, mother, birth details, and informant. | Current converted Markdown gives a wholly different entry 172; father suffix unresolved; no canonical promotion until QA. |
| 2 | Entry 172 is the converted Markdown row for `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. | 0.28 | 0.28 | Current converted Markdown directly states this row under entry 172. | It conflicts with the assigned chunk, source packet, and image-reread note; no Pulgar/Arriagada family relevance if controlling. |
| 3 | The two readings represent adjacent or mismatched source/conversion assignments, not a single person. | 0.76 | 0.72 | Names, parents, dates, places, and informants are materially different; the conflict behaves like a row/source assignment problem. | Requires targeted conversion QA to identify the controlling image/row and whether any file or chunk assignment is stale. |
| 4 | `Jose del Carmen Pulgar S.` is the same canonical person as `Jose del Carmen Pulgar`. | 0.50 | 0.42 | Same base name; existing wiki page `jose-del-carmen-pulgar.md` has local Pulgar parent context. | The `S.` suffix is not certified; existing context does not prove this specific entry-172 father is the same person as the canonical stub. |
| 5 | `Juana Arriagada de Pulgar` in entry 172 is the same person as canonical `Juana Arriagada de Pulgar`. | 0.58 | 0.46 | Exact name match between the Pulgar/Arriagada row and existing wiki page; page already has staged entry-172 evidence snapshot. | Row-level conflict and existing low confidence block promotion; do not merge with `Juana de Dios Amagada de Pulgar` by name similarity or spouse context. |
| 6 | Entry-172 Pulgar/Arriagada evidence bridges to `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. | 0.08 | 0.05 | Only broad Pulgar/Arriagada family-context relevance. | The entry does not name Dario, Arturo, Smith, Jose as a Dario middle name, medical/Geneva/passenger contexts, spouse, child, grandchild, or any direct Dario-line bridge. |

## Conflict Analysis

- Same-person conflict: unresolved only for the local parent candidates `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` versus existing Juana stubs. The source does not support merging any Dario identities.
- Duplicate-person risk: high if the Pulgar/Arriagada row is treated as proof of existing canonical people before conversion QA; high if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar` without a separate parent/spouse proof review.
- Name-variant conflict: `Jose del Carmen Pulgar S.` may be a suffix/name component or conversion artifact. It must be certified as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Relationship conflict: the child-parent relationships are blocked because the controlling entry-172 row has not been certified. If the Pulgar/Arriagada row controls, the mother relationship is stronger than the father identity normalization because the mother name has less field-level uncertainty.
- Chronology conflict: no chronology conflict is established within the Pulgar/Arriagada row itself. The conflict is between two incompatible entry-172 birth events: 8 March 1888 at 3 p.m. versus 6 April 1888 at 10 p.m.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| identity_confidence_score | 0.56 | Moderate confidence that the Pulgar/Arriagada row is the intended family-relevant row, but low readiness for canonical identity attachment. |
| conflict_severity_score | 0.92 | The derivative records disagree on child, parents, birth date/time, place, and informant. |
| evidence_quality_score | 0.74 | Civil birth register image and local reread are strong source types, but this note does not perform new conversion or image QA. |
| conversion_confidence_score | 0.30 | The current converted Markdown and assigned chunk disagree at row level. |
| claim_probability | 0.62 | Pulgar/Arriagada is more probable from staged evidence, but not certified. |
| relevance_score | 0.86 | High relevance to Pulgar/Arriagada research and parent candidates; low direct relevance to Dario identity bridging. |
| canonical_readiness | hold_for_conversion_qa | Targeted conversion QA and rerun proof review are required before promotion. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, current converted Markdown, and source packet. The QA output must decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row and, if Pulgar/Arriagada controls, certify the father field only as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that QA, rerun proof review on child identity, birth facts, father-name claim, mother-name claim, child-parent relationships, parent-pair clue, and anti-conflation checks for `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
