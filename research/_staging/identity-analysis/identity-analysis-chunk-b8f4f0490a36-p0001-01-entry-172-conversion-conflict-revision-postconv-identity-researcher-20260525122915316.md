---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525122915316
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Conversion Conflict

## Blockers First

- Material row-level blocker: the referenced staged conflict draft says the current chunk supports entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, while the assigned converted Markdown records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`.
- This is not a name variant, spelling variant, or relationship nuance. It is a controlling conversion/file-assignment conflict, so no identity, parent, relationship, or chronology claim from this draft is canonically ready.
- Father-name blocker: even under the Pulgar/Arriagada reading, the father field must remain unresolved among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies the literal reading.
- Dario-line blocker: this entry does not name `Dario`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`. It cannot bridge any Dario identity cluster to the child or parents by surname context alone.
- Jose/Juana blocker: `Juana Arriagada de Pulgar` is not silently equivalent to `Juana de Dios Amagada de Pulgar` or other `Juana de Dios ... de Pulgar` readings in existing wiki context.

## Literal Evidence Under Review

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md`.
- Current chunk reading: entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, parents at `Calle de Colipi`, informant `Ernesto Herrera L.`
- Assigned converted Markdown reading: entry 172 records `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En esta`.
- Reviewed task context for this exact worker timestamp repeats the same required QA decision: decide whether the controlling source row is the Pulgar/Arriagada row or the Gomez/de la Cruz row, and settle the father suffix.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Hypothesis: if the current chunk/source-packet reading controls, entry 172 records the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar S.` or an uncertain suffix form and mother `Juana Arriagada de Pulgar`.

Supporting evidence:

- The referenced source packet explicitly preserves a Pulgar/Arriagada row for entry 172.
- The current chunk contains a full table row for entry 172 naming the child, father, mother, birth date/time, birth place, parent residence, and informant.
- Existing canonical stub pages already contain generated evidence snapshots for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` from prior entry-172 staging, but those should not be treated as resolving this current derivative conflict.

Conflicts and limits:

- The assigned converted Markdown is materially inconsistent and names a different child and parents.
- The father suffix is not settled.
- The source packet itself sets `conversion_confidence: mixed` and `promotion_recommendation: hold_for_conversion_qa`.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Strong within the current chunk, but blocked by the assigned converted Markdown conflict. |
| conflict_severity | 0.95 | Entire entry identity and parent set differ. |
| evidence_quality | 0.62 | Staged chunk/source-packet detail is rich, but derivative disagreement prevents proof-ready use. |
| conversion_confidence | 0.40 | Explicitly mixed until targeted QA reconciles source, converted Markdown, and chunk. |
| claim_probability | 0.68 | Plausible if chunk is confirmed; not promotable now. |
| relevance | 1.00 | Direct subject of the staged conflict draft. |
| canonical_readiness | 0.10 | Hold for conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Hypothesis: the assigned converted Markdown is controlling, and entry 172 concerns `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`.

Supporting evidence:

- The assigned converted Markdown literally transcribes entry 172 with the Gomez/de la Cruz family.

Conflicts and limits:

- The staged conflict draft and source packet identify this as the conflicting derivative reading, not a confirmed family-relevant row.
- This hypothesis would sever the staged Pulgar/Arriagada child and parent claims from this entry.
- No local identity work should promote Gomez/de la Cruz claims from this conflict draft until QA determines whether this converted Markdown belongs to a different row, page, or source assignment.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.35 | Present in converted Markdown, but contradicted by current chunk/source packet. |
| conflict_severity | 0.95 | Mutually exclusive with the Pulgar/Arriagada reading. |
| evidence_quality | 0.45 | Literal derivative text exists, but context flags it as suspect. |
| conversion_confidence | 0.35 | Needs file/row assignment QA. |
| claim_probability | 0.30 | Possible only if converted Markdown is confirmed as controlling. |
| relevance | 0.95 | Central competing reading. |
| canonical_readiness | 0.05 | No promotion until QA. |

## Hypothesis 3: Father Candidate Is Jose del Carmen Pulgar / Jose del Carmen Pulgar S.

Hypothesis: under the Pulgar/Arriagada reading, the father is a Jose del Carmen Pulgar candidate, but the exact name form is unresolved.

Supporting evidence:

- Current chunk reads `Jose del Carmen Pulgar S.`
- Source packet and conflict draft preserve three father-name QA outcomes: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` is a local Jose Pulgar stub with other draft Pulgar-line parent context, so duplicate-person risk is real.

Conflicts and limits:

- This draft does not prove that the entry-172 father is the same person as the Jose del Carmen Pulgar candidate linked to Tulio Cesar Luis Jose.
- The final suffix may be a surname initial, abbreviation, or uncertain mark; it must not be normalized silently.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.55 | Candidate father is likely in the chunk reading, but exact form and duplicate status are unresolved. |
| conflict_severity | 0.70 | Father identity affects parent linkage and possible duplicate-person work. |
| evidence_quality | 0.58 | Good row context, weak suffix certainty. |
| conversion_confidence | 0.38 | Blocked by row conflict plus suffix uncertainty. |
| claim_probability | 0.55 | Parent claim is plausible if the Pulgar row is confirmed. |
| relevance | 0.96 | Direct parent candidate. |
| canonical_readiness | 0.08 | Requires conversion QA then parent-identity proof review. |

## Hypothesis 4: Mother Candidate Is Juana Arriagada de Pulgar

Hypothesis: under the Pulgar/Arriagada reading, the mother is `Juana Arriagada de Pulgar`.

Supporting evidence:

- Current chunk and source packet name `Juana Arriagada de Pulgar`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` contains a generated probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from prior entry-172 staging.

Conflicts and limits:

- The assigned converted Markdown names `Emilia de la Cruz`, not Juana.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate local stub tied to a different draft child context; this draft does not prove equivalence with `Juana Arriagada de Pulgar`.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Clear in the chunk reading, but blocked by row conflict. |
| conflict_severity | 0.82 | Mother identity differs entirely between derivative readings. |
| evidence_quality | 0.60 | Name is explicit in chunk/source packet, but not conversion-QA settled. |
| conversion_confidence | 0.40 | Mixed. |
| claim_probability | 0.62 | Plausible if Pulgar row controls. |
| relevance | 0.96 | Direct parent candidate. |
| canonical_readiness | 0.08 | Hold. |

## Pulgar-Line Anti-Conflation Comparison

The required Dario/Pulgar comparison is context only for this staged draft.

| Candidate | Evidence In This Draft | Assessment |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | None. Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns not to auto-merge similarly named records. | No bridge from entry 172. Probability 0.02. |
| `Dario Arturo Pulgar` | None. Existing staged CV context concerns a document-level Dario Arturo Pulgar, but this birth entry names no Dario. | No bridge. Probability 0.02. |
| `Dario Jose Pulgar-Arriagada` | None. Shared `Pulgar`/`Arriagada` surname elements are not identity proof. | Do not merge with `Jose del Carmen Segundo Pulgar Arriagada`. Probability 0.01. |
| `Dario/Dario Pulgar Arriagada` / `Dario J. Pulgar Arriagada` | None in this entry. Existing medical/Geneva/passenger clusters have separate chronology and occupation anchors. | No same-person support here. Probability 0.01. |
| Jose/Juana parent candidates | Entry may name `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` if Pulgar row controls. | Direct relevance only for entry-172 parents; not a bridge to Dario candidates. Probability for direct parent-context relevance 0.60, for Dario bridge 0.02. |

Ranked hypotheses:

| Rank | Hypothesis | Probability | Required Next Step |
| ---: | --- | ---: | --- |
| 1 | Current chunk/source-packet Pulgar/Arriagada row is the intended entry-172 evidence. | 0.68 | Targeted conversion QA against source image, converted Markdown, and chunk. |
| 2 | Assigned converted Markdown Gomez/de la Cruz row is the intended entry-172 evidence. | 0.30 | Same targeted conversion QA; determine if chunk/source assignment is wrong. |
| 3 | Entry-172 father is the same as an existing `Jose del Carmen Pulgar` parent candidate elsewhere. | 0.28 | Only after QA, run parent-identity proof review comparing names, dates, residences, spouses, and child contexts. |
| 4 | `Juana Arriagada de Pulgar` is the same as `Juana de Dios Amagada de Pulgar` or another Juana candidate. | 0.12 | Separate Juana proof review; do not treat as a variant from this draft alone. |
| 5 | Any Dario identity cluster is same person as, or directly connected to, the entry-172 child or parents. | 0.02 | No action from this draft except preserving anti-conflation warnings. |

## Conflict Summary

- Same-person conflict: unresolved for entry 172 because the controlling row is unresolved.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is merged into `Jose del Carmen Pulgar` without suffix QA and parent-identity proof review.
- Name-variant risk: moderate for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`; moderate for `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar`; minimal for Dario within this draft because no Dario appears.
- Relationship conflict: high for child-parent claims because competing readings name entirely different parents.
- Chronology conflict: the Pulgar row birth date is 1888-03-08 at 3 p.m.; the Gomez/de la Cruz row birth date is 1888-03-26 at 10 p.m. These cannot both describe the same entry/person.

## Recommended Next Action

Keep the staged conflict draft and all dependent claims, relationships, parent candidates, and canonical snapshots at `hold_for_conversion_qa`.

Exact next proof-review/promotion step: run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned converted Markdown, current chunk, and source packet. The QA note must decide whether the controlling source row for register page 58, entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row, or whether the converted Markdown/chunk assignment must be superseded. It must also certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review for child identity, birth facts, father and mother claims, child-parent relationships, and any parent-candidate or Dario-line bridge question.
