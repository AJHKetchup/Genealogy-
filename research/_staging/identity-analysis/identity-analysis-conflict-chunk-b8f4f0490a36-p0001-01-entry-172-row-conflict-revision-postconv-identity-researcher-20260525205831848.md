---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525205831848
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md
reviewed:
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-proof-review-postconv-proof-review-20260525204415696.md
  - wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md
  - wiki/people/jose-del-carmen-pulgar.md
  - wiki/people/juana-arriagada-de-pulgar.md
  - wiki/people/juana-de-dios-amagada-de-pulgar.md
  - wiki/people/tulio-cesar-luis-jose.md
  - wiki/people/dario-arturo-pulgar-smith.md
  - wiki/people/dario-pulgar-child-passenger-age-11.md
  - wiki/people/dar-o-pulgar-arriagada.md
  - research/_staging/source-packets/chunk-0c7431cd7d77-p0002-01-r3578-jacket5-chile-dario-pulgar-arriagada.md
conflict_type: conversion_row_conflict
subject: "Register page 58 entry 172"
identity_confidence_score: 0.56
conflict_severity_score: 0.93
evidence_quality_score: 0.74
conversion_confidence_score: 0.30
claim_probability: 0.62
relevance_score: 0.88
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Identity And Conflict Analysis: Entry 172 Row Conflict

This note analyzes the exact staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md`.

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The assigned chunk/source packet and current converted Markdown disagree on the controlling row for entry 172.
2. The assigned chunk/source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
3. The current converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
4. These are incompatible row identities, not spelling variants, name-order variants, or duplicate-person candidates.
5. The father field in the Pulgar/Arriagada row remains unresolved at proof-review precision: targeted QA must certify `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
6. No Dario-line attachment is supported by this entry. The reviewed entry does not name Dario, Arturo, Smith, Dario Jose, Darío J., or any Dario parent, spouse, child, grandchild, medical, passenger, CV, or expropriation bridge.

## Literal Evidence

From the assigned chunk and revised source packet:

- Entry: `172`, register page 58.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, `a las tres de la tarde`, `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.`; Chilean; employee; resident at `Calle de Colipí`.
- Mother field: `Juana Arriagada de Pulgar`; Chilean; `Su sexo`; resident at `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employee, resident at `Calle de Valdivia`.

From the current converted Markdown:

- Entry: `172`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: 6 April 1888 at 10 p.m.; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

Interpretation: the derivative readings cannot both describe the same entry 172 row. Identity analysis cannot resolve the controlling row without conversion QA.

## Hypotheses

| Rank | Hypothesis | Probability | Identity confidence | Evidence supporting | Conflicts / limits |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth-registration row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.62 | 0.56 | Assigned chunk, revised source packet, and prior proof review all support a coherent Pulgar/Arriagada row. | Current converted Markdown gives a different entry 172; father suffix unresolved; no promotion until QA. |
| 2 | Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.28 | 0.28 | Current converted Markdown directly states this row under entry 172. | It conflicts with the assigned chunk/source packet and has no Pulgar relevance. |
| 3 | The conflict reflects a stale, mismatched, or misassigned derivative conversion state. | 0.76 | 0.72 | Same entry number is tied to materially different child, parent, birth, place, and informant data across derivatives. | Requires targeted conversion QA; not a person-merge question. |
| 4 | `Jose del Carmen Pulgar S.` is the same person as existing `Jose del Carmen Pulgar`. | 0.50 | 0.42 | Same base name and local Pulgar parent context. | `S.` is not certified; existing wiki context does not prove this entry-172 father is the same canonical stub. |
| 5 | `Juana Arriagada de Pulgar` in entry 172 is the existing `Juana Arriagada de Pulgar` stub. | 0.58 | 0.46 | Exact name match and existing low-confidence entry-172 evidence snapshot. | Row conflict blocks promotion; do not merge with `Juana de Dios Amagada de Pulgar` by spouse/family context alone. |
| 6 | Entry 172 supports `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío Pulgar Arriagada`. | 0.03 | 0.03 | Broad Pulgar/Arriagada surname context only. | No Dario name or identity bridge appears in this source. |

## Conflict Analysis

- Same-person conflict: `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` are competing row readings, not the same person.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is merged into `Jose del Carmen Pulgar` before the suffix/mark and other Jose parent evidence are reviewed.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` remains unresolved; preserve literal uncertainty.
- Relationship conflict: high. Under one reading, the child-parent pair is Pulgar/Arriagada; under the other, it is Burgos/de la Cruz.
- Chronology conflict: high between the derivative readings: 8 March 1888 at 3 p.m. versus 6 April 1888 at 10 p.m.
- Dario-line conflict: no positive bridge. Keep all Dario candidates separate or unresolved for this task.

## Pulgar-Line Comparison

| Candidate / cluster | Relationship to this draft | Attachment probability | Required proof-review or promotion step |
| --- | --- | ---: | --- |
| `Jose del Carmen Segundo Pulgar Arriagada` | Direct child candidate if Pulgar/Arriagada row controls. | 0.62 | Targeted conversion QA, then proof review for child name, birth, and parent claims. |
| `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` | Direct father candidate only if Pulgar/Arriagada row controls. | 0.50 | QA-certified father-field reading, then Jose parent-candidate identity comparison across reviewed records. |
| `Juana Arriagada de Pulgar` | Direct mother candidate only if Pulgar/Arriagada row controls. | 0.58 | Conversion QA, then parent-candidate proof review; preserve literal married-name form. |
| `Juana de Dios Amagada de Pulgar` | Separate Juana parent candidate from entry-513/Tulio context. | 0.12 | Separate Jose/Juana comparison using reviewed entry-513 evidence; do not merge by spouse context alone. |
| `Dario Arturo Pulgar-Smith` | Existing family-supplied maternal-grandfather page. | 0.02 | Separate identity bridge source; do not attach entry 172. |
| `Dario Arturo Pulgar` | CV document-level subject in staging; no page-local bridge here. | 0.02 | Separate CV identity-bridge proof review; do not attach entry 172. |
| `Dario Jose Pulgar-Arriagada` / `Darío J. Pulgar Arriagada` | Separate staged medical/title or name-form cluster. | 0.03 | Separate proof review comparing full name, initials, profession, dates, and family anchors. |
| `Darío Pulgar Arriagada` / `Dario Pulgar Arriagada` | Separate legal/Geneva/expropriation contexts. | 0.02 | Separate identity bridge with vital, residence, occupation, or relationship continuity. |

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| identity_confidence_score | 0.56 | Pulgar/Arriagada is the stronger family-relevant reading, but row control is not certified. |
| conflict_severity_score | 0.93 | The conflict changes child, parents, birth date/time, place, and informant. |
| evidence_quality_score | 0.74 | Civil birth-register evidence is strong, but this task relies on staged derivatives and prior review rather than new conversion QA. |
| conversion_confidence_score | 0.30 | The converted Markdown and assigned chunk disagree at row level. |
| claim_probability | 0.62 | The Pulgar/Arriagada row is probable from local staged evidence but not promotion-ready. |
| relevance_score | 0.88 | Directly relevant to Pulgar/Arriagada parent candidates; only anti-conflation relevance for Dario candidates. |
| canonical_readiness | hold_for_conversion_qa | No canonical promotion, merge, or relationship claim should proceed before QA and proof review. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, current converted Markdown, source packet, and conflict note. The QA note must decide the controlling entry-172 row and certify the father field only as far as visible: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting child identity, birth facts, father-name claim, mother-name claim, child-parent relationships, parent-pair clues, or any Jose/Juana parent merge. Do not attach this entry to any Dario-line person without a later proof-reviewed bridge source.
