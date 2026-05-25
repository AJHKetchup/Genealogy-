---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525173055107
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525171911545.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525171911545.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525171911545.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Conversion Conflict

## Blockers

- Controlling-row blocker: the staged conflict draft says the assigned chunk supports entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` or unresolved `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`; the assigned converted Markdown says entry `172` is `Jose Francisco`, child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`, born at `En Pellin`.
- This is a row-level or file-assignment conflict, not a spelling variant. The competing readings have different child names, parents, birth date, birth place, and informant context.
- Father-field blocker: the final element after `Jose del Carmen Pulgar` is not proof-review certified. Preserve the possible readings `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- Canonical-readiness blocker: existing wiki pages already contain low-confidence or draft evidence for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`. This draft must not strengthen, merge, rename, or promote those pages.
- Dario-line blocker: this entry does not name Dario. It cannot bridge `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar Arriagada`, or passenger-list Dario candidates.

## Literal Evidence

From the staged conflict draft, revised source packet, and assigned chunk:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father field by chunk reading: `Jose del Carmen Pulgar S.`; proof-review context still requires targeted QA for the exact ending.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age `Veintiseis años`, profession `Empleado`, residence `Calle de Valdivia`.

Contrary literal evidence from the assigned converted Markdown:

- Entry `172` is transcribed as child `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`.
- Birth is transcribed as `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En Pellin`.

Interpretation kept separate: the Pulgar/Arriagada reading is the family-relevant staged target and is supported by the assigned chunk/source packet, but the converted Markdown conflict blocks promotion until targeted conversion QA decides the controlling row.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Interpretation: the controlling row for this task is the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, with parents `Jose del Carmen Pulgar [ending unresolved]` and `Juana Arriagada de Pulgar`.

Supporting evidence:

- The staged conflict draft explicitly identifies the Pulgar/Arriagada row as the chunk-supported entry `172`.
- The revised source packet gives the same child, date, place, father, mother, and informant fields.
- The assigned chunk contains the Pulgar/Arriagada row for entry `172`.
- Existing canonical wiki pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` already point to earlier entry-172 evidence, but those entries remain probable/draft and must not be upgraded from this held draft.

Conflicts and limits:

- The assigned converted Markdown gives a different entry `172`.
- The father suffix is unresolved.
- Parent-candidate matches to existing `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` pages require proof review after conversion QA.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Strong staged/chunk support, reduced by direct converted-file disagreement. |
| conflict_severity | 0.94 | Competing rows identify different children, parents, dates, and places. |
| evidence_quality | 0.68 | Detailed staged packet and chunk, but derivative outputs disagree. |
| conversion_confidence | 0.45 | Mixed; controlling row is not certified. |
| claim_probability | 0.70 | Probable as staged evidence, not promotion-ready. |
| relevance | 0.98 | Directly addresses the assigned staged conflict draft. |
| canonical_readiness | 0.18 | Hold for conversion QA and proof-review rerun. |

## Hypothesis 2: Converted Markdown Entry 172 Is The Controlling Row

Interpretation: the current converted Markdown may describe the controlling entry `172`, making the record about `Jose Francisco`, child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`.

Supporting evidence:

- The assigned converted Markdown explicitly labels that row as entry `172`.
- It provides a complete alternative child-parent-birth-place cluster.

Conflicts and limits:

- The staged conflict draft and revised source packet were created because the chunk/source-image review supports a different Pulgar/Arriagada row.
- The converted Markdown conflicts with the chunk on every identity-bearing field.
- This Gomez/de la Cruz de la Maza cluster has no demonstrated Pulgar-line relevance in the staged draft.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.36 | Present in the converted output but contradicted by the revised staged packet/chunk. |
| conflict_severity | 0.94 | Mutually exclusive row/person cluster. |
| evidence_quality | 0.42 | Single derivative conversion reading under active QA challenge. |
| conversion_confidence | 0.35 | Converted text is not reliable enough for promotion here. |
| claim_probability | 0.30 | Possible file/row assignment issue, not the stronger staged conclusion. |
| relevance | 0.72 | Relevant as the competing row only. |
| canonical_readiness | 0.02 | Do not promote from this conflict draft. |

## Hypothesis 3: Father Candidate Is Existing Jose Del Carmen Pulgar

Interpretation: the father named in the Pulgar/Arriagada row may be the same person as canonical `wiki/people/jose-del-carmen-pulgar.md`.

Supporting evidence:

- The row names a father read as `Jose del Carmen Pulgar` with an unresolved final element.
- The existing canonical page uses the same preferred name.
- The wiki already contains a separate draft child relationship from a Tulio-related birth-register task, so this is a plausible parent-candidate cluster requiring comparison.

Conflicts and limits:

- The exact father-name ending remains unresolved.
- Name overlap alone is insufficient to merge Jose parent candidates across separate records.
- The existing Jose page does not yet provide a settled relationship to `Jose del Carmen Segundo Pulgar Arriagada`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Plausible same-name parent candidate, blocked by suffix and row conflict. |
| conflict_severity | 0.70 | Meaningful risk of merging separate Jose del Carmen Pulgar candidates. |
| evidence_quality | 0.52 | Direct name evidence, but not fully certified. |
| conversion_confidence | 0.45 | Dependent on controlling-row QA. |
| claim_probability | 0.46 | Possible, not proved. |
| relevance | 0.88 | Direct parent-candidate issue. |
| canonical_readiness | 0.12 | Hold for father-field certification and parent-candidate proof review. |

## Hypothesis 4: Mother Candidate Is Existing Juana Arriagada De Pulgar

Interpretation: the mother named in the Pulgar/Arriagada row may be the same person as canonical `wiki/people/juana-arriagada-de-pulgar.md`.

Supporting evidence:

- The row and source packet read the mother as `Juana Arriagada de Pulgar`.
- The existing canonical page uses the same preferred name and has an auto-generated probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts and limits:

- The main row-level conversion conflict still blocks promotion.
- The separate canonical `Juana de Dios Amagada de Pulgar` page is a different Juana candidate linked in draft to `Tulio Cesar Luis Jose`; do not silently normalize `Arriagada` and `Amagada`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Strong exact-name support within the held row, reduced by conversion hold. |
| conflict_severity | 0.62 | Main risk is row conflict plus Juana-candidate conflation. |
| evidence_quality | 0.63 | Direct row reading, but still staged. |
| conversion_confidence | 0.45 | Dependent on controlling-row QA. |
| claim_probability | 0.64 | Probable if Pulgar/Arriagada row is accepted. |
| relevance | 0.90 | Direct parent-candidate issue. |
| canonical_readiness | 0.16 | Hold until conversion QA and relationship proof review. |

## Dario-Line Anti-Conflation Comparison

This staged draft and its referenced row do not name `Dario`, `Dario Arturo`, `Dario Jose`, `Dario J.`, `Pulgar-Smith`, or any Dario parent/child relationship.

| Candidate | Local evidence context | Effect of this draft | Probability from this draft |
| --- | --- | --- | ---: |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal grandfather of Alexander John Heinz; page warns against automatic attachment of similarly named records. | No direct bridge; at most a possible future lineage context after separate proof. | 0.01 |
| `Dario Arturo Pulgar` | Staged CV materials elsewhere use this document-level name and require identity-bridge review to attach to `Pulgar-Smith`. | No CV, Arturo, Dario, occupation, or family bridge appears here. | 0.01 |
| `Dario Jose Pulgar-Arriagada` | Other local staged contexts mention this full name. | No support; do not infer from Pulgar/Arriagada surname pattern. | 0.01 |
| `Dario J. Pulgar Arriagada` | Other staged tasks cite a 1918 medical-title context. | No Dario, initial, medical title, or chronology bridge appears here. | 0.01 |
| `Dario Pulgar Arriagada` / `Darío Pulgar Arriagada` | Existing canonical stub has a 2000 expropriation event. | No same-person evidence or chronology bridge. | 0.01 |
| Jose/Juana parent candidates | This draft directly involves Jose del Carmen Pulgar and Juana Arriagada de Pulgar, with a separate Juana de Dios Amagada candidate in wiki context. | Relevant only as parent-candidate anti-conflation and proof-review targets. | Jose 0.46; Juana Arriagada 0.64; Juana de Dios Amagada 0.05 |

Ranked hypotheses:

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Entry `172` supports a non-Dario Pulgar/Arriagada birth-registration cluster for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | Complete targeted conversion QA and certify the controlling row. |
| 2 | The row supplies parent-candidate context for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. | 0.55 | After row QA, run parent-candidate proof review against existing Jose/Juana pages. |
| 3 | The row is indirect ancestral context for a later Dario-line person. | 0.08 | Require a separately reviewed lineage bridge from this child or parents to the relevant Dario candidate. |
| 4 | Same-person evidence for `Dario Arturo Pulgar-Smith` and `Dario Arturo Pulgar`. | 0.01 | Use identity-bearing CV or family evidence; this draft cannot decide it. |
| 5 | Same-person evidence for `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario Pulgar Arriagada`. | 0.01 | Use full-name/date/occupation/residence/family-continuity evidence from those source packets; do not merge by surname. |

## Conflict Summary

- Same-person conflicts: unresolved for father `Jose del Carmen Pulgar` versus existing `Jose del Carmen Pulgar`; unresolved for mother `Juana Arriagada de Pulgar` only because the controlling row is held.
- Duplicate-person risks: high if Jose parent candidates are merged across entry-172 and Tulio-related drafts before proof review; high if Juana Arriagada and Juana de Dios Amagada are normalized silently.
- Name-variant conflicts: the father suffix after `Pulgar` is unresolved; `Arriagada` versus `Amagada` is not a silent correction.
- Relationship conflicts: the Pulgar/Arriagada row would support child-parent relationships for `Jose del Carmen Segundo Pulgar Arriagada`, but the converted Markdown supports unrelated Gomez/de la Cruz parents for entry `172`.
- Chronology conflicts: none proved among Pulgar-line people from this entry alone; the date conflict is between competing row readings for the same entry number.

## Recommended Next Action

Keep this staged draft and all dependent identity, claim, relationship, parent-candidate, and Dario-line comparison work at `hold_for_conversion_qa`.

Exact next step: targeted conversion QA must compare the source image, assigned converted Markdown, chunk, and revised source packet for entry `172`; identify the controlling row; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Only after that should proof review rerun child identity, birth claims, child-parent relationships, and parent-candidate comparisons against existing `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` pages. No Dario-line merge or canonical attachment is supported by this draft.
