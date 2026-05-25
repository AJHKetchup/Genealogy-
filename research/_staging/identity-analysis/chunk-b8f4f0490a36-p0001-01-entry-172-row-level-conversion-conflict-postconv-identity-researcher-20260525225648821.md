---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525225648821
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The assigned staged conflict draft, source packet, and chunk do not agree with the assigned converted Markdown for entry 172. This is a row-control conflict, not a name variant.
- The Pulgar/Arriagada reading cannot be promoted until targeted conversion QA certifies whether entry 172 is the `Jose del Carmen Segundo Pulgar Arriagada` row or the `Jose Miguel` / Burgos-de la Cruz row.
- The father field must remain uncertified until QA decides whether the visible form is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No same-person merge, duplicate-person cleanup, canonical name change, parent-child relationship promotion, or Dario-line bridge is ready from this draft.
- Family-context hints involving Dario/Pulgar can justify a later double-check only. The literal entry-172 evidence does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Darío Pulgar Arriagada, or any Dario candidate.

## Literal Evidence From Assigned Materials

- Staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md` states that the assigned chunk/source-packet reading is `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- The same staged draft states that the current converted Markdown reading is `José Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.
- The referenced source packet repeats the Pulgar/Arriagada row and explicitly recommends `hold_for_conversion_qa`.
- The referenced chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The referenced converted file transcribes entry 172 as `José Miguel`, with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`.

## Existing Wiki Context Considered

- Canonical `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` already contains staged/promoted-looking evidence snapshot material for a child named `Jose del Carmen Segundo Pulgar Arriagada`, including birth on 1888-03-08 at Calle de Valdivia and mother `Juana Arriagada de Pulgar`, but the current assignment's draft still flags a later row-level conversion conflict.
- Canonical `wiki/people/juana-arriagada-de-pulgar.md` records a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from the same chunk family, with very low displayed relationship confidence in the person snapshot.
- Canonical `wiki/people/jose-del-carmen-pulgar.md` records a separate reviewed child link to `Tulio Cesar Luis Jose` from an 1889 Los Anjeles birth-register entry naming father `Jose del Carmen Pulgar`.
- Existing relationship pages for the 1889 entry name `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` as parents of `Tulio Cesar Luis Jose`. That may be a parent-candidate comparison target, but it is not proof that the 1888 `Juana Arriagada de Pulgar` and 1889 `Juana de Dios Amagada de Pulgar` are the same person.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to merge similarly named source clusters without identity review.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` contains a scoped 2000 expropriation-notice event for `Darío Pulgar Arriagada`; it has no stated kinship, birth, death, or bridge to entry 172.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Evidence supporting:

- The assigned chunk and referenced source packet agree on `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
- The staged conflict draft is explicit that the Pulgar/Arriagada row is the assigned chunk/source-packet reading and that promotion should be held only because the converted Markdown disagrees.
- A civil birth registration would be strong direct evidence for the child identity, birth facts, and named parents if row control is certified.

Conflicts and limits:

- The assigned converted Markdown gives a different child, parents, birth date, birth time, place wording, and informant for the same entry number.
- The father suffix `S.` is not safe to expand or drop without targeted field QA.
- This entry does not supply a Dario identity bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Better-supported by the assigned chunk and source packet, but blocked by the converted-file conflict. |
| conflict_severity | 0.95 | Mutually incompatible row readings affect every core identity and relationship field. |
| evidence_quality | 0.84 | Civil registration evidence is high quality once the row is certified; current derivative disagreement lowers usable quality. |
| conversion_confidence | 0.30 | The conversion layer conflicts with the chunk/source-packet layer for the same entry number. |
| claim_probability | 0.70 | Probable but not promotion-grade before conversion QA. |
| relevance | 0.90 | Directly relevant to Pulgar/Arriagada parent-child identity if certified. |
| canonical_readiness | 0.10 | Hold; not ready for promotion or merge. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Evidence supporting:

- The assigned converted Markdown literally records entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.

Conflicts and limits:

- This reading is contradicted by the assigned chunk, source packet, and staged conflict draft.
- It contains no Pulgar, Arriagada, Jose/Juana parent-candidate, or Dario-line relevance.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.28 | Present in the converted Markdown but isolated against the assigned chunk/source packet. |
| conflict_severity | 0.95 | If controlling, it invalidates the Pulgar/Arriagada extraction for this entry. |
| evidence_quality | 0.45 | Derivative transcription only in the current comparison; needs image-level QA. |
| conversion_confidence | 0.30 | The converted layer is internally usable text but conflicts with other assigned derivatives. |
| claim_probability | 0.25 | Possible row-control outcome but weaker in the staged evidence set. |
| relevance | 0.05 | Not relevant to Pulgar-line identity except as a blocker. |
| canonical_readiness | 0.00 | Not ready; no canonical action. |

## Hypothesis 3: Jose del Carmen Pulgar In Entry 172 Is The Same Parent As Jose del Carmen Pulgar In The 1889 Tulio Entry

Evidence supporting:

- Both local contexts use the name `Jose del Carmen Pulgar`.
- The 1889 relationship page records father/declarant `Jose del Carmen Pulgar` for `Tulio Cesar Luis Jose`, age forty-seven.
- If the 1888 Pulgar row is certified, the two records may represent a plausible repeated father candidate in Los Anjeles-area civil registrations.

Conflicts and limits:

- The 1888 father may read `Jose del Carmen Pulgar S.` or uncertain suffix; the exact field is not certified.
- The 1888 mother is staged as `Juana Arriagada de Pulgar`; the 1889 mother is recorded as `Juana de Dios Amagada de Pulgar`. That is a material name-form conflict, not a silent correction.
- No age is given for the 1888 father in the assigned Pulgar row excerpt. Chronology cannot be reconciled from this draft alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Plausible candidate comparison by name and context, but underproved and row-blocked. |
| conflict_severity | 0.70 | Potential parent-identity merge risk if handled by name alone. |
| evidence_quality | 0.62 | One 1889 reviewed relationship is stronger than the unresolved 1888 row. |
| conversion_confidence | 0.50 | Mixed: 1889 reviewed evidence appears stronger; 1888 remains conflicted. |
| claim_probability | 0.42 | Possible, not ready. |
| relevance | 0.75 | Relevant to Jose/Juana parent-candidate comparison if entry 172 is certified. |
| canonical_readiness | 0.05 | Hold for conversion QA and separate parent identity proof review. |

## Hypothesis 4: Juana Arriagada de Pulgar In Entry 172 Is The Same Parent As Juana de Dios Amagada de Pulgar In The 1889 Tulio Entry

Evidence supporting:

- Both names include a Juana married-name form ending `de Pulgar`.
- Existing local pages place both names in Pulgar parent contexts from Los Anjeles civil birth registrations.

Conflicts and limits:

- `Arriagada` and `Amagada`/`de Dios Amagada` are different literal readings in the existing local evidence.
- The 1888 row is not conversion-certified under this assignment.
- No independent identity anchors in this draft establish that these Juana names are variants of one person.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Name and spouse-context hints exist, but the surname conflict is material. |
| conflict_severity | 0.80 | High risk of an incorrect mother merge if normalized silently. |
| evidence_quality | 0.56 | Existing local evidence is useful for comparison but not sufficient for identity resolution. |
| conversion_confidence | 0.45 | The 1888 row is blocked; the 1889 mother form must be preserved literally. |
| claim_probability | 0.30 | Possible variant, not proved. |
| relevance | 0.72 | Relevant if entry 172 is certified and a parent-identity review is opened. |
| canonical_readiness | 0.00 | Not ready; preserve separate hypotheses. |

## Hypothesis 5: Entry 172 Connects To Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Evidence supporting:

- The surname `Pulgar` appears in the Pulgar/Arriagada hypothesis.
- Existing canonical context includes `Dario Arturo Pulgar-Smith` as a family-supplied maternal-line person, and staged CV materials elsewhere use `Dario Arturo Pulgar`.

Conflicts and limits:

- Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, a grandchild, Alexander John Heinz, or any modern identifying event.
- Existing Dario CV and family-supplied contexts require separate identity-bridge proof review before canonical attachment.
- A surname-only connection is not identity evidence.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Surname overlap only; no direct bridge. |
| conflict_severity | 0.85 | High merge risk if used to attach a child or parents to the Dario-Smith cluster. |
| evidence_quality | 0.20 | No direct evidence for this hypothesis in the assigned entry. |
| conversion_confidence | 0.30 | Even the Pulgar row is unresolved. |
| claim_probability | 0.05 | Not supported from this draft. |
| relevance | 0.25 | Low direct relevance; only a future comparison hint. |
| canonical_readiness | 0.00 | Reject/hold from this source alone. |

## Hypothesis 6: Entry 172 Connects To Dario Jose Pulgar-Arriagada, Dario/Darío Pulgar Arriagada, Or The 2000 Darío Pulgar Arriagada Notice

Evidence supporting:

- The Pulgar/Arriagada hypothesis contains the surnames `Pulgar Arriagada`.
- Existing canonical `Darío Pulgar Arriagada` has a scoped 2000 expropriation-notice event.

Conflicts and limits:

- Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose, Dario Arturo, or Darío Pulgar Arriagada.
- The 2000 notice provides no kinship, vital dates, or parentage; it cannot bridge to an 1888 birth entry by name pattern alone.
- If `Jose del Carmen Segundo Pulgar Arriagada` was born in 1888, he is chronologically unlikely to be the same person as a 2000 apparent property holder unless supported by strong additional proof, which is absent here.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | No same-person evidence; name-pattern overlap only. |
| conflict_severity | 0.80 | High risk of false merge across generations and source types. |
| evidence_quality | 0.18 | No direct bridge evidence in the assigned materials. |
| conversion_confidence | 0.30 | Entry 172 row remains unresolved. |
| claim_probability | 0.03 | Not supported from this draft. |
| relevance | 0.20 | Only useful as a warning not to merge Pulgar-Arriagada names by pattern. |
| canonical_readiness | 0.00 | Reject/hold from this source alone. |

## Conflict Summary

- Same-person conflict: unresolved for the entry-172 child because two different row readings identify two different children.
- Duplicate-person risk: high if `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and the 1889 `Jose del Carmen Pulgar` parent are merged without suffix and parent-cluster review.
- Name-variant conflict: material for `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar`; preserve both readings.
- Relationship conflict: no entry-172 parent-child relationship should be promoted while the row-control conflict remains.
- Chronology conflict: no direct Dario chronology can be inferred; the 1888 birth child should not be merged into modern Dario/Darío Pulgar contexts.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | Targeted conversion QA comparing source image, converted file, chunk, and source packet; certify row and father field. |
| 2 | Entry 172 is the Burgos/de la Cruz birth row for `José Miguel`. | 0.25 | Same targeted conversion QA; if certified, retire the Pulgar/Arriagada staged extraction for this entry. |
| 3 | 1888 `Jose del Carmen Pulgar S.` is the same as 1889 `Jose del Carmen Pulgar`. | 0.42 | After row QA, run a parent-identity proof review comparing exact names, ages, residences, spouse/mother names, and chronology. |
| 4 | 1888 `Juana Arriagada de Pulgar` is the same as 1889 `Juana de Dios Amagada de Pulgar`. | 0.30 | After row QA, run a separate mother-identity proof review preserving literal surname variants. |
| 5 | Entry 172 supports Dario Arturo Pulgar-Smith or Dario Arturo Pulgar. | 0.05 | No promotion; only a later identity-bridge review using identity-bearing Dario sources can test this. |
| 6 | Entry 172 supports Dario Jose Pulgar-Arriagada or Dario/Darío Pulgar Arriagada. | 0.03 | No merge; preserve as unrelated or unproved unless future proof-reviewed bridge evidence appears. |

## Recommended Next Action

Keep this staged conflict at `hold_for_conversion_qa`. The exact next step is targeted conversion QA for `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, comparing the current converted Markdown, assigned chunk, and staged source packet. QA must certify the controlling entry-172 row and the father-field reading before any proof review, promotion, parent merge, or Dario-line identity comparison proceeds.
