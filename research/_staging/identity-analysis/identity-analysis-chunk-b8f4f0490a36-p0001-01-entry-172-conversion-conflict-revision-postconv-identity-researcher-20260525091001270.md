---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525091001270
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: blocked
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conflict

## Blockers

1. The exact staged draft under review is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md`.
2. The controlling row is unresolved. The current chunk/source packet reads entry 172 as the Pulgar/Arriagada birth registration, while the assigned converted Markdown reads entry 172 as a different Gomez/de la Cruz family.
3. The father-name ending is unresolved. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as open readings until targeted conversion QA certifies the source-visible form.
4. No canonical fact, relationship, parent merge, duplicate-person merge, or Dario-line attachment is ready. All dependent claims and relationships should remain `hold_for_conversion_qa`.

## Literal Evidence

Current chunk and source packet:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/place: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; `Calle de Valdivia`.
- Father: chunk reads `Jose del Carmen Pulgar S.`.
- Mother: `Juana Arriagada de Pulgar`.
- Parents' residence: `Calle de Colipi`.
- Informant: `Ernesto Herrera L.`, present at the birth.

Assigned converted Markdown:

- Child: `Jose Francisco`.
- Birth date/place: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho`; `En esta`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.

Interpretation: this is a material row-level conversion or file-assignment conflict, not a name variant.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Evidence supporting:

- The current chunk and source packet agree on `Jose del Carmen Segundo Pulgar Arriagada` as child, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The staged claims and relationships from the same `20260525082133967` extraction consistently hold the child, father, mother, and parental-pair candidates for conversion QA rather than promotion.
- Existing wiki pages already contain a low-confidence/probable snapshot for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, but those pages are not enough to resolve this row-level conflict by themselves.

Evidence against or limiting:

- The assigned converted Markdown for the same source path and chunk id records a different entry-172 family.
- The father suffix/final mark remains unresolved.

Scores:

| Metric | Score | Reason |
| --- | ---: | --- |
| identity_confidence | 0.64 | Moderately supports the Pulgar/Arriagada row as the intended identity cluster, weakened by converted-file disagreement. |
| conflict_severity | 0.94 | Different child, father, mother, birth date/place, and family cluster. |
| evidence_quality | 0.62 | Civil-registration evidence would be strong, but current support is split between derivative artifacts. |
| conversion_confidence | 0.35 | Current chunk is coherent, but assigned converted Markdown materially conflicts. |
| claim_probability | 0.66 | Probable only if the chunk/source-packet row is confirmed by QA. |
| relevance | 0.96 | Directly relevant to entry 172 Pulgar/Arriagada identity and parent candidates. |
| canonical_readiness | 0.10 | Blocked pending conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Evidence supporting:

- The assigned converted Markdown literally records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`.

Evidence against or limiting:

- The current chunk and staged source packet record the Pulgar/Arriagada row for the same entry number and source path.
- The staged conflict draft identifies this as a conversion/file-assignment problem, not a family identity variant.

Scores:

| Metric | Score | Reason |
| --- | ---: | --- |
| identity_confidence | 0.40 | Supported by the converted Markdown only, contradicted by the current chunk/source packet. |
| conflict_severity | 0.94 | Mutually exclusive row identity for entry 172. |
| evidence_quality | 0.48 | Single derivative transcript support in conflict with another derivative artifact. |
| conversion_confidence | 0.30 | Cannot be trusted without targeted row reconciliation. |
| claim_probability | 0.34 | Possible as the true assigned converted row, not promotion-ready. |
| relevance | 0.88 | Directly relevant as the conflicting identity cluster. |
| canonical_readiness | 0.05 | Do not promote from this staged conflict. |

## Hypothesis 3: `Jose del Carmen Pulgar S.` Is The Same Person As Canonical `Jose del Carmen Pulgar`

Evidence supporting:

- The chunk/source packet father line overlaps strongly with canonical `wiki/people/jose-del-carmen-pulgar.md` by name.
- The existing canonical page has a separate draft child relationship for `Tulio Cesar Luis Jose`, showing the name already exists as a candidate in local context.

Evidence against or limiting:

- This entry's father suffix is unresolved and may be `S.`, no suffix, or an uncertain mark.
- The existing canonical `Jose del Carmen Pulgar` page does not itself prove that the entry-172 father is the same person as the Tulio-related candidate.
- Name overlap alone is insufficient for a parent merge.

Scores:

| Metric | Score | Reason |
| --- | ---: | --- |
| identity_confidence | 0.42 | Plausible name overlap, but no independent bridge and unresolved suffix. |
| conflict_severity | 0.60 | Main risk is duplicate-person/parent merge by name alone. |
| evidence_quality | 0.45 | One conflicted birth-entry cluster plus separate wiki context. |
| conversion_confidence | 0.35 | Father line depends on row QA. |
| claim_probability | 0.40 | Possible, not proved. |
| relevance | 0.82 | Relevant father candidate if the Pulgar row is confirmed. |
| canonical_readiness | 0.08 | Blocked. |

## Hypothesis 4: `Juana Arriagada de Pulgar` Is A Distinct Mother Candidate, Not Automatically Other Juana Candidates

Evidence supporting:

- The current chunk/source packet literally names `Juana Arriagada de Pulgar` as mother.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` carries a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from the same local evidence cluster.

Evidence against or limiting:

- The assigned converted Markdown gives a different mother, `Emilia de la Cruz`.
- Other local Juana candidates exist, including `Juana de Dios Amagada de Pulgar`; this entry does not prove they are the same person.

Scores:

| Metric | Score | Reason |
| --- | ---: | --- |
| identity_confidence | 0.60 | The mother reading is coherent in the Pulgar chunk, but row QA is unresolved. |
| conflict_severity | 0.72 | Risk is both row conflict and wrong Juana merge. |
| evidence_quality | 0.58 | Direct civil-register row reading if confirmed, currently derivative-conflicted. |
| conversion_confidence | 0.35 | Same row-level conversion blocker. |
| claim_probability | 0.62 | Probable if Pulgar row is confirmed. |
| relevance | 0.94 | Direct mother candidate for entry 172. |
| canonical_readiness | 0.10 | Hold. |

## Dario-Line Comparison

The staged draft and local wiki context require anti-conflation with Dario-line candidates:

- `Dario Arturo Pulgar-Smith`: canonical family-supplied maternal grandfather of Alexander John Heinz. Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, or a grandchild relationship.
- `Dario Arturo Pulgar`: appears in separate CV/work-history staging. Entry 172 does not provide a direct bridge to that CV subject.
- `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, and `Dario/Dario Pulgar Arriagada`: separate staged/canonical clusters appear in medical, photo, passenger, property, expropriation, or other contexts. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.
- Jose/Juana parent candidates: entry 172 may become useful as older Pulgar/Arriagada parent evidence only after conversion QA and proof review; it cannot silently correct or merge Jose/Juana candidates from other entries.

Ranked Dario-line hypotheses:

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is unrelated direct evidence for any Dario identity and should serve only as a Pulgar/Juana parent-candidate check. | 0.90 | Complete targeted conversion QA, then proof-review the entry-172 parent readings before any later lineage comparison. |
| 2 | Entry 172 is an ancestor/lineage clue that may later connect to a Dario Pulgar-Arriagada/Pulgar-Smith cluster. | 0.18 | Require a separate proof-reviewed bridge from `Jose del Carmen Segundo Pulgar Arriagada` or the named parents to a Dario candidate. |
| 3 | Entry 172 directly identifies `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. | 0.02 | No promotion path from this draft; needs direct identity-bearing evidence in another source. |

## Conflicts

- Same-person conflict: unresolved for the father candidate `Jose del Carmen Pulgar [?]` versus existing `Jose del Carmen Pulgar`.
- Duplicate-person conflict: high risk if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar` or other Juana candidates without a bridge.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` must remain separate readings until QA.
- Relationship conflict: child-father, child-mother, and parental-pair candidates depend on whether the Pulgar row is the controlling entry 172 row.
- Chronology conflict: none internal to the Pulgar row, but chronology cannot be used canonically until the row is confirmed.
- Dario-line conflict: no direct Dario evidence; merging by Pulgar/Arriagada name alone would be unsupported.

## Recommended Next Action

Keep the staged draft and dependent evidence on `hold_for_conversion_qa`. The exact next step is targeted conversion QA against the source image, assigned converted Markdown, current chunk, and source packet, explicitly deciding whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row and certifying the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, parent merge, Dario-line comparison, or wiki promotion.
