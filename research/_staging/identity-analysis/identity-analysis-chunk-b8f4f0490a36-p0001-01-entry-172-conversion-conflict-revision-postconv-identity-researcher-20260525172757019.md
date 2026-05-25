---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525172757019
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170607416.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170607416.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Conversion Conflict

## Blockers

- Controlling-row blocker: the staged conflict draft and revised source packet say entry `172` is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`; the assigned converted Markdown says entry `172` is `Jose Francisco`, child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`, born at `En Pellin`. This is a row-level or file-assignment conflict, not a name-variant conflict.
- Father-field blocker: the chunk reads the father as `Jose del Carmen Pulgar S.`, while source-image review leaves the final mark after `Pulgar` unresolved. Preserve the proof-review outcomes `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Canonical-promotion blocker: existing canonical wiki pages already contain low-confidence or draft evidence for some related Pulgar/Juana/Jose candidates. Do not strengthen or merge those profiles from this draft until conversion QA identifies the controlling row and proof review reruns.
- Dario-line blocker: this entry does not name Dario. It supplies only possible older Pulgar-line context and cannot bridge `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, passenger-list Dario Pulgar candidates, or any Jose/Juana parent clusters.

## Literal Evidence

From the revised staged source packet and chunk:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father field in the chunk: `Jose del Carmen Pulgar S.`; the staged conflict draft marks the ending after `Pulgar` unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age `Veintiseis años`, profession `Empleado`, domicile `Calle de Valdivia`.

Contrary literal evidence from the assigned converted Markdown:

- Entry `172` is transcribed as child `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`.
- Birth is transcribed as `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En Pellin`.

Interpretation kept separate: the Pulgar/Arriagada row is the stronger family-relevant staged target in the revised packet, but the derivative conversion conflict prevents canonical promotion.

## Hypothesis 1: Entry 172 Is Jose Del Carmen Segundo Pulgar Arriagada

Interpretation: the controlling source row for this staged task is the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar [ending unresolved]` and `Juana Arriagada de Pulgar`.

Supporting evidence:

- The staged conflict draft states that the assigned chunk and source-image review support the Pulgar/Arriagada birth registration.
- The revised source packet lists the child, birth date/place, father, mother, and informant fields for the Pulgar/Arriagada row.
- The chunk itself contains a row for entry `172` with the Pulgar/Arriagada readings.
- Existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` already contain auto-generated evidence snapshots pointing back to the earlier entry-172 source packet, but they remain low-confidence/probable rather than final proof.

Conflicts and limits:

- The assigned converted Markdown points to a different `172` row.
- The father suffix is not certified.
- The father relationship to existing `Jose del Carmen Pulgar` is not ready to promote, because the current canonical page for `Jose del Carmen Pulgar` contains a separate draft child relationship to `Tulio Cesar Luis Jose`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Strong staged/chunk support, reduced by direct converted-file disagreement. |
| conflict_severity | 0.94 | Different child, parents, place, date, and likely source row. |
| evidence_quality | 0.68 | Source packet and chunk are detailed; conversion disagreement remains unresolved. |
| conversion_confidence | 0.45 | Mixed by staged packet; cannot certify controlling row yet. |
| claim_probability | 0.70 | Probable staged identity after image review, not promotion-ready. |
| relevance | 0.98 | Directly addresses the assigned staged conflict draft. |
| canonical_readiness | 0.18 | Hold until conversion QA and proof review rerun. |

## Hypothesis 2: Converted Markdown Entry 172 Is The Controlling Person

Interpretation: the assigned converted Markdown may be reading the true controlling row, making this task about `Jose Francisco`, child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`.

Supporting evidence:

- The converted Markdown explicitly assigns entry `172` to `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`.
- The converted Markdown is the current assigned conversion output for the referenced converted file.

Conflicts and limits:

- The revised staged conflict draft and source packet were created specifically because source-image/chunk review supports the Pulgar/Arriagada row instead.
- The converted Markdown conflicts with the chunk row on every identity-bearing field.
- The Gomez/de la Cruz cluster has no direct Pulgar-line relevance in the staged draft.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.36 | It is present in the converted output but contradicted by the revised packet/chunk review. |
| conflict_severity | 0.94 | Mutually exclusive row/person cluster. |
| evidence_quality | 0.42 | Single derivative conversion reading under active QA challenge. |
| conversion_confidence | 0.35 | Converted text is not reliable enough for promotion in this conflict. |
| claim_probability | 0.30 | Possible file/row assignment issue, not the stronger staged conclusion. |
| relevance | 0.72 | Relevant as the competing row, not as a family identity candidate. |
| canonical_readiness | 0.02 | Do not promote from this conflict draft. |

## Hypothesis 3: Father Candidate Is Existing Jose Del Carmen Pulgar

Interpretation: the father field in the Pulgar/Arriagada row may identify the same person as canonical `wiki/people/jose-del-carmen-pulgar.md`.

Supporting evidence:

- The row names a father read as `Jose del Carmen Pulgar` plus an unresolved ending or suffix.
- The existing canonical page uses the preferred name `Jose del Carmen Pulgar`.
- The same broader Pulgar-line context includes child and parent candidates with Jose/Juana names.

Conflicts and limits:

- The row may read `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]`, so the exact name form is not certified.
- The existing `Jose del Carmen Pulgar` page currently shows a draft child relationship to `Tulio Cesar Luis Jose`, not a settled relationship to `Jose del Carmen Segundo Pulgar Arriagada`.
- Name overlap alone cannot merge parent candidates across separate birth-register tasks.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Plausible same-name parent candidate, but father suffix and row conflict block proof. |
| conflict_severity | 0.70 | Risk of merging separate Jose del Carmen Pulgar candidates. |
| evidence_quality | 0.52 | Direct name in row, but unresolved mark and derivative conflict. |
| conversion_confidence | 0.45 | Same conversion hold as the main row. |
| claim_probability | 0.46 | Possible, not proved. |
| relevance | 0.88 | Direct parent-candidate issue. |
| canonical_readiness | 0.12 | Hold for father-field certification and parent-candidate proof review. |

## Hypothesis 4: Mother Candidate Is Existing Juana Arriagada De Pulgar

Interpretation: the mother field identifies the same person as canonical `wiki/people/juana-arriagada-de-pulgar.md`.

Supporting evidence:

- The row and source packet read the mother as `Juana Arriagada de Pulgar`.
- The existing canonical page uses the same preferred name and already has an auto-generated probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts and limits:

- The main row-level conversion conflict still blocks promotion.
- The separate canonical `Juana de Dios Amagada de Pulgar` page is a different Juana candidate linked in draft to `Tulio Cesar Luis Jose`; do not normalize `Arriagada` and `Amagada` or merge Juana candidates from this draft.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Strong exact-name support within the held row, reduced by conversion QA hold. |
| conflict_severity | 0.62 | Main risk is Juana-candidate conflation and row conflict. |
| evidence_quality | 0.63 | Direct row reading, but still derivative/staged. |
| conversion_confidence | 0.45 | Dependent on controlling-row QA. |
| claim_probability | 0.64 | Probable if Pulgar/Arriagada row is accepted. |
| relevance | 0.90 | Direct parent-candidate issue. |
| canonical_readiness | 0.16 | Hold until conversion QA and relationship proof review. |

## Dario-Line Anti-Conflation Comparison

This staged draft and its referenced row do not name `Dario`, `Dario Arturo`, `Dario Jose`, `Dario J.`, `Darío`, `Pulgar-Smith`, or `Dario Pulgar Arriagada`.

Candidate comparison:

| Candidate | Local evidence context | Effect of this draft | Identity probability from this draft |
| --- | --- | --- | ---: |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal grandfather of Alexander John Heinz; page warns against automatic attachment of Dario/Pulgar records. | No direct bridge. Entry 172 may be older Pulgar-line context only after proof review. | 0.01 |
| `Dario Arturo Pulgar` | Staged CV materials elsewhere use this document-level name and require identity-bridge review before linking to `Pulgar-Smith`. | No CV, Arturo, Dario, occupation, or family bridge appears here. | 0.01 |
| `Dario Jose Pulgar-Arriagada` | Mentioned in other staged Pulgar-line contexts, not in this entry. | No support. Do not infer from `Pulgar Arriagada` surname pattern. | 0.01 |
| `Dario J. Pulgar Arriagada` | Other staged tasks cite a 1918 medical-title context. | No medical title, initial, or Dario name appears here. | 0.01 |
| `Darío Pulgar Arriagada` / `Dario Pulgar Arriagada` | Existing canonical stub has a 2000 expropriation event. | No date/age/property bridge; no same-person evidence. | 0.01 |
| Passenger-list Dario Pulgar candidates | Existing child age-11 and adult age-64 stubs are separate passenger-list identities. | No passenger, age, residence, or travel evidence here. | 0.00 |
| Jose/Juana parent candidates | This draft directly involves Jose del Carmen Pulgar and Juana Arriagada de Pulgar, plus separate Juana de Dios Amagada de Pulgar context in the wiki. | Relevant only as parent-candidate anti-conflation and proof-review targets. | 0.46 for Jose candidate; 0.64 for Juana Arriagada candidate; 0.05 for Juana de Dios Amagada. |

Ranked Dario/Pulgar hypotheses:

| Rank | Hypothesis | Probability | Required next proof-review step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 supports a non-Dario Pulgar/Arriagada birth-registration cluster for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | Complete targeted conversion QA and certify the controlling row. |
| 2 | The row supplies parent-candidate context for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. | 0.55 | After row QA, run parent-candidate proof review comparing existing Jose/Juana pages and relationship evidence. |
| 3 | The row is indirect ancestral context for a later Dario-line person. | 0.08 | Require a separate reviewed lineage bridge from `Jose del Carmen Segundo Pulgar Arriagada` or his parents to the relevant Dario candidate. |
| 4 | Same-person or duplicate-person evidence for `Dario Arturo Pulgar-Smith` and `Dario Arturo Pulgar`. | 0.01 | Use identity-bearing CV/family evidence; this draft cannot decide it. |
| 5 | Same-person evidence for `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Darío Pulgar Arriagada`. | 0.01 | Use full-name/date/occupation/residence/family-continuity evidence from those source packets; do not merge by surname. |

## Conflict Summary

- Same-person conflicts: unresolved for father `Jose del Carmen Pulgar` versus existing `Jose del Carmen Pulgar`; unresolved for mother `Juana Arriagada de Pulgar` only because the controlling row is held.
- Duplicate-person risks: high if `Jose del Carmen Pulgar` parent candidates are merged across entry-172 and Tulio-related drafts before proof review; high if Juana Arriagada and Juana de Dios Amagada are normalized silently.
- Name-variant conflicts: father suffix after `Pulgar` is unresolved; `Arriagada` versus `Amagada` is not a silent correction.
- Relationship conflicts: the Pulgar/Arriagada row would support child-parent relationships for `Jose del Carmen Segundo Pulgar Arriagada`, but the converted Markdown supports unrelated Gomez/de la Cruz parents for entry `172`.
- Chronology conflicts: none proved between Pulgar-line people from this entry alone; the date conflict is between two competing row readings for the same entry number.

## Recommended Next Action

Keep this staged draft and all dependent identity, claim, relationship, parent-candidate, and Dario-line comparison work at `hold_for_conversion_qa`.

Exact next step: targeted conversion QA must compare the source image, assigned converted Markdown, chunk, and revised source packet for entry `172`; identify the controlling row; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Only after that should proof review rerun child identity and parent relationships, followed by a separate parent-candidate comparison against existing `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` pages. No Dario-line merge or canonical attachment is supported by this draft.
