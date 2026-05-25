---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525210248504
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
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

This note analyzes the exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md`.

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The assigned chunk/source packet and current converted Markdown disagree about the controlling row for register page 58, entry 172.
2. The assigned chunk/source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
3. The current converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
4. These readings are incompatible row identities, not same-person evidence, duplicate-person evidence, or a name-variant problem.
5. The Pulgar father field remains unresolved at proof-review precision. Targeted QA must certify the field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
6. This entry does not name or bridge `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or `Darío Pulgar Arriagada`. Dario-line comparison here is anti-conflation context only.

## Literal Evidence

From the assigned chunk and staged source packet:

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

Interpretation: identity analysis cannot certify either row as controlling. The conflict must be resolved as conversion/source-assignment QA before any identity, parent, or relationship conclusion is promoted.

## Hypotheses

| Rank | Hypothesis | Probability | Identity confidence | Evidence supporting | Conflicts / limits |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth-registration row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.62 | 0.56 | Assigned chunk and revised source packet give a coherent Pulgar/Arriagada row; existing local wiki stubs already reflect low-confidence context from this cluster. | Current converted Markdown gives a different row; father suffix unresolved; no promotion until QA and proof review. |
| 2 | Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.28 | 0.28 | Current converted Markdown directly places this row under entry 172. | Contradicts assigned chunk/source packet and carries no Pulgar relevance unless QA shows the Pulgar row belongs elsewhere. |
| 3 | The conflict reflects stale, mismatched, or misassigned derivative conversion state. | 0.76 | 0.72 | Same entry number is tied to different child, parent, birth, place, residence, and informant data. | Requires targeted conversion QA; not a person-merge question. |
| 4 | `Jose del Carmen Pulgar S.` is the same person as existing `Jose del Carmen Pulgar`. | 0.50 | 0.42 | Same base name and local Jose parent-candidate context. | `S.` is not certified; spouse/child/residence chronology comparison is still needed. |
| 5 | `Juana Arriagada de Pulgar` in entry 172 is the existing `Juana Arriagada de Pulgar` stub. | 0.58 | 0.46 | Exact name match and existing entry-172 evidence snapshot. | Row conflict blocks promotion; do not merge with other Juana candidates by family context alone. |
| 6 | Entry 172 supports any Dario-line identity bridge. | 0.03 | 0.03 | Broad Pulgar/Arriagada surname context only. | No Dario name, parentage, spouse, child, CV, passenger, Geneva, medical, or expropriation bridge appears here. |

## Conflict Analysis

- Same-person conflict: `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` are competing row readings, not variants of one person.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is merged into `Jose del Carmen Pulgar` before father-field QA and parent-candidate comparison.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` remains unresolved; preserve the literal uncertainty.
- Relationship conflict: high. One reading gives Pulgar/Arriagada parents; the other gives Burgos/de la Cruz parents.
- Chronology conflict: high. The derivative readings differ between birth on 1888-03-08 at 3 p.m. and birth on 1888-04-06 at 10 p.m.
- Conversion conflict: severe. The current converted Markdown and assigned chunk/source packet cannot both be correct for the same entry-172 row.

## Pulgar-Line And Parent-Candidate Comparison

| Candidate / cluster | Relationship to this draft | Attachment probability | Required proof-review or promotion step |
| --- | --- | ---: | --- |
| `Jose del Carmen Segundo Pulgar Arriagada` | Direct child candidate if Pulgar/Arriagada row controls. | 0.62 | Targeted conversion QA, then proof review of child name, sex, birth date/time/place, and registration date. |
| `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` | Direct father candidate only if Pulgar/Arriagada row controls. | 0.50 | QA-certified father-field reading, then Jose parent-candidate identity comparison across reviewed records. |
| `Juana Arriagada de Pulgar` | Direct mother candidate only if Pulgar/Arriagada row controls. | 0.58 | Conversion QA, then parent-candidate proof review; preserve the literal married-name form. |
| `Juana de Dios Amagada de Pulgar` | Separate Juana parent candidate from Tulio/entry-513 context. | 0.12 | Separate Jose/Juana comparison using reviewed entry-513 evidence; do not merge by spouse or broad family context alone. |
| `Dario Arturo Pulgar-Smith` | Existing family-supplied maternal-grandfather page. | 0.02 | Separate identity-bridge proof review explicitly connecting a Dario source to Pulgar-Smith; do not attach entry 172. |
| `Dario Arturo Pulgar` | CV document-level subject in staging. | 0.02 | Separate CV identity-bridge proof review; do not attach entry 172. |
| `Dario Jose Pulgar-Arriagada` | Separate staged/title/photo or name-form cluster. | 0.03 | Separate proof review comparing full name, initials, profession, dates, and family anchors. |
| `Dario/Dario Pulgar Arriagada` / `Darío Pulgar Arriagada` | Separate legal, medical, Geneva, or expropriation contexts. | 0.02 | Separate identity bridge with vital, residence, occupation, or relationship continuity. |

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| identity_confidence_score | 0.56 | Pulgar/Arriagada is the stronger family-relevant reading from the assigned chunk/source packet, but row control is not certified. |
| conflict_severity_score | 0.93 | The conflict changes child, parents, birth date/time, birth place, parent residence, and informant. |
| evidence_quality_score | 0.74 | Civil birth-register evidence is potentially strong, but this task relies on staged derivatives and existing wiki context rather than new conversion QA. |
| conversion_confidence_score | 0.30 | The current converted Markdown and assigned chunk/source packet disagree at row level. |
| claim_probability | 0.62 | The Pulgar/Arriagada row is probable from local staged evidence but not promotion-ready. |
| relevance_score | 0.88 | Directly relevant to Pulgar/Arriagada parent candidates; only anti-conflation relevance for Dario candidates. |
| canonical_readiness | hold_for_conversion_qa | No canonical promotion, merge, relationship claim, or Dario-line attachment should proceed before QA and rerun proof review. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, current converted Markdown, staged source packet, and staged conflict note. The QA note must decide the controlling entry-172 row and certify the father field only to the extent visible: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth fact, parent-name claim, parent-child relationship, parent-pair clue, duplicate-person decision, or canonical attachment. Keep `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and other Jose/Juana candidates separate unless a later proof-reviewed bridge explicitly connects them.
