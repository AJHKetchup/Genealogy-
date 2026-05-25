---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525172756135
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Conversion Conflict

## Blockers First

- Material row-level blocker: the staged conflict draft says the assigned chunk and source-image review support entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` with an unresolved final suffix or mark, and mother `Juana Arriagada de Pulgar`; the assigned converted Markdown instead records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En Pellin`.
- This is not a same-person spelling variant. It is a controlling conversion/file-assignment conflict affecting the child, parents, birth date, birth place, and informant context.
- Father-name blocker: if the Pulgar/Arriagada row is confirmed, the exact father field must remain unresolved among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies the source reading.
- Canonical-readiness blocker: existing wiki stubs already contain generated snapshots for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`, but those snapshots do not resolve this current row conflict and should not be used as promotion authority.
- Dario-line blocker: this staged draft does not name `Dario`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario Pulgar Arriagada`. Shared `Pulgar`/`Arriagada` surname context can only justify later double-checking, not a bridge or merge.

## Literal Evidence Under Review

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md`.
- Current chunk reading: entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, parents at `Calle de Colipi`, informant `Ernesto Herrera L.`
- Assigned converted Markdown reading: entry 172 records `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En Pellin`.
- Reviewed canonical context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, `wiki/people/dario-arturo-pulgar-smith.md`, and `wiki/people/dar-o-pulgar-arriagada.md`.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Hypothesis: if the chunk/source-packet reading controls, entry 172 records the birth of `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S./[?]` and `Juana Arriagada de Pulgar`.

Supporting evidence:

- The staged conflict draft and source packet both state that chunk/source-image review supports the Pulgar/Arriagada row.
- The chunk contains a full row for entry 172 with child name, sex, birth date/time, birth place, father, mother, residences, and informant.
- Existing canonical stubs for the child and mother reflect earlier entry-172 staging, so the names are already tracked locally as held Pulgar-line candidates.

Conflicts and limits:

- The assigned converted Markdown gives a different child-parent cluster for the same entry number.
- The father suffix is unresolved and cannot be normalized silently.
- The source packet says `conversion_confidence: mixed` and `promotion_recommendation: hold_for_conversion_qa`.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Strong within the chunk/source-packet reading, but blocked by the assigned converted Markdown conflict. |
| conflict_severity | 0.95 | Entire child-parent row differs. |
| evidence_quality | 0.62 | Detailed local staged evidence exists, but derivative disagreement prevents proof-ready use. |
| conversion_confidence | 0.40 | Explicitly mixed until source, chunk, and converted Markdown are reconciled. |
| claim_probability | 0.68 | Plausible if the chunk/source-image review is confirmed. |
| relevance | 1.00 | Direct subject of the staged draft. |
| canonical_readiness | 0.10 | Hold for conversion QA and renewed proof review. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz de la Maza Birth Registration

Hypothesis: the assigned converted Markdown is controlling, and entry 172 concerns `Jose Francisco`, son of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`.

Supporting evidence:

- The assigned converted Markdown literally transcribes entry 172 with the Gomez/de la Cruz de la Maza family, a February 1888 birth date, and `Pellin` as place.

Conflicts and limits:

- The staged conflict draft treats this as the conflicting derivative reading, not as confirmed family-relevant evidence.
- This hypothesis is mutually exclusive with the Pulgar/Arriagada child and parent claims.
- No Gomez/de la Cruz de la Maza claim should be promoted from this conflict note until QA determines whether the converted Markdown belongs to a different row, page, or file assignment.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.35 | Present in converted Markdown, but contradicted by current chunk/source-packet staging. |
| conflict_severity | 0.95 | Mutually exclusive with the Pulgar/Arriagada reading. |
| evidence_quality | 0.45 | Literal derivative text exists, but local review flags it as suspect. |
| conversion_confidence | 0.35 | Requires row/file assignment QA. |
| claim_probability | 0.30 | Possible only if the converted Markdown is confirmed as controlling. |
| relevance | 0.95 | Central competing reading. |
| canonical_readiness | 0.05 | No promotion until QA. |

## Hypothesis 3: Father Candidate Is Jose del Carmen Pulgar / Jose del Carmen Pulgar S.

Hypothesis: under the Pulgar/Arriagada reading, the father is a `Jose del Carmen Pulgar` candidate, but the exact name form and duplicate-person status are unresolved.

Supporting evidence:

- The staged conflict draft preserves the father field as `Jose del Carmen Pulgar` with an unresolved final suffix or mark.
- The chunk reads `Jose del Carmen Pulgar S.`
- Existing `wiki/people/jose-del-carmen-pulgar.md` is a separate local stub with a generated draft child link to `Tulio Cesar Luis Jose`, creating a real duplicate-person and parent-candidate review need.

Conflicts and limits:

- This staged draft does not prove the entry-172 father is the same person as the Jose del Carmen Pulgar candidate attached to Tulio Cesar Luis Jose.
- The final suffix could be a surname initial, abbreviation, or uncertain mark; it must remain literal/uncertain until QA.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.55 | Candidate father is likely if the Pulgar row controls, but exact form is unresolved. |
| conflict_severity | 0.70 | Father identity affects parent linkage and possible duplicate-person handling. |
| evidence_quality | 0.58 | Good row context, weak suffix certainty. |
| conversion_confidence | 0.38 | Blocked by row conflict and suffix uncertainty. |
| claim_probability | 0.55 | Plausible only if the Pulgar row is confirmed. |
| relevance | 0.96 | Direct parent candidate. |
| canonical_readiness | 0.08 | Requires conversion QA, then parent-identity proof review. |

## Hypothesis 4: Mother Candidate Is Juana Arriagada de Pulgar

Hypothesis: under the Pulgar/Arriagada reading, the mother is `Juana Arriagada de Pulgar`.

Supporting evidence:

- The staged conflict draft, source packet, and chunk all name `Juana Arriagada de Pulgar` under the Pulgar/Arriagada reading.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` contains a generated probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from prior entry-172 staging.

Conflicts and limits:

- The assigned converted Markdown names `Rosario de la Cruz de la Maza`, not Juana.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate local stub tied to a different draft child context. This staged draft does not prove `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person or variants.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Clear in the chunk/source-packet reading, but blocked by row conflict. |
| conflict_severity | 0.82 | Mother identity differs entirely between derivative readings. |
| evidence_quality | 0.60 | Name is explicit in local staged evidence, but not conversion-QA settled. |
| conversion_confidence | 0.40 | Mixed. |
| claim_probability | 0.62 | Plausible if the Pulgar row controls. |
| relevance | 0.96 | Direct parent candidate. |
| canonical_readiness | 0.08 | Hold. |

## Pulgar-Line Anti-Conflation Comparison

| Candidate | Evidence In This Staged Draft | Assessment |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | None. Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly cautions against automatic merges with similarly named source clusters. | No bridge from entry 172. Probability 0.02. |
| `Dario Arturo Pulgar` | None. Existing staged CV contexts are document-level `Dario Arturo Pulgar` evidence, but this birth entry names no Dario and no Smith/Pulgar-Smith marker. | No bridge. Probability 0.02. |
| `Dario Jose Pulgar-Arriagada` | None. Shared `Pulgar`/`Arriagada` elements are surname context only. | Do not merge with the child, father, mother, or other Dario clusters by name alone. Probability 0.01. |
| `Dario J. Pulgar Arriagada` / `Dario Pulgar Arriagada` | None in this entry. Existing medical, passenger, or later legal clusters have separate chronology and occupation anchors. | No same-person support here. Probability 0.01. |
| Jose/Juana parent candidates | Entry may name `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` if the Pulgar row controls. | Direct relevance only for entry-172 parent review; not a bridge to Dario candidates. Probability for direct parent-context relevance 0.60, for Dario bridge 0.02. |

Ranked hypotheses:

| Rank | Hypothesis | Probability | Required Next Step |
| ---: | --- | ---: | --- |
| 1 | Current chunk/source-packet Pulgar/Arriagada row is the intended entry-172 evidence. | 0.68 | Targeted conversion QA against source image, assigned converted Markdown, current chunk, and source packet. |
| 2 | Assigned converted Markdown Gomez/de la Cruz de la Maza row is the intended entry-172 evidence. | 0.30 | Same targeted conversion QA; determine whether chunk/source assignment is wrong or converted Markdown is wrong/misassigned. |
| 3 | Entry-172 father is the same as existing `Jose del Carmen Pulgar` parent candidate elsewhere. | 0.28 | Only after QA, run parent-identity proof review comparing names, suffixes, dates, residences, spouses, and child contexts. |
| 4 | `Juana Arriagada de Pulgar` is the same as `Juana de Dios Amagada de Pulgar` or another Juana candidate. | 0.12 | Separate Juana proof review; do not treat as a variant from this draft alone. |
| 5 | Any Dario identity cluster is same person as, or directly connected to, the entry-172 child or parents. | 0.02 | No action from this draft except preserving anti-conflation warnings. |

## Conflict Summary

- Same-person conflict: unresolved for entry 172 because the controlling row is unresolved.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is merged into `Jose del Carmen Pulgar` without suffix QA and parent-identity proof review.
- Name-variant risk: moderate for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`; moderate for `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar`; minimal for Dario within this draft because no Dario appears.
- Relationship conflict: high for child-parent claims because competing readings name entirely different parents.
- Chronology conflict: the Pulgar row birth date/time is 1888-03-08 at 3 p.m.; the converted Markdown row birth date/time is 1888-02-20 at 10 p.m. These cannot both describe the same child/event.

## Recommended Next Action

Keep the staged conflict draft and all dependent claims, relationships, parent candidates, Dario-line comparisons, and canonical snapshots at `hold_for_conversion_qa`.

Exact next proof-review/promotion step: run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned converted Markdown, current chunk, and source packet. The QA note must decide whether register page 58, entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz de la Maza row, or whether the converted Markdown/chunk assignment must be superseded. It must also certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review for child identity, birth facts, father and mother claims, child-parent relationships, duplicate parent candidates, and any later Dario-line bridge question.
