---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525091344655
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525081514407.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: blocked
---

# Identity And Conflict Analysis: Entry 172 Conversion Conflict

## Blockers

1. The exact staged draft under review is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md`.
2. The controlling entry-172 row is not stable. The current chunk/source packet reads a Pulgar/Arriagada birth registration, while the assigned converted Markdown reads a different Gomez/de la Cruz birth registration.
3. The father-name ending is unresolved. Keep `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as separate literal-reading possibilities until targeted conversion QA certifies the source-visible form.
4. No same-person merge, duplicate-person merge, parent relationship, Dario-line bridge, or canonical wiki promotion is ready from this staged draft.

## Literal Evidence

Current chunk and source packet literal reading:

- Entry: `172`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date and place: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; `Calle de Valdivia`.
- Father: chunk reads `Jose del Carmen Pulgar S.`.
- Mother: `Juana Arriagada de Pulgar`.
- Parent residence: `Calle de Colipi`.
- Informant: `Ernesto Herrera L.`, present at the birth.

Assigned converted Markdown literal reading for entry 172:

- Child: `Jose Francisco`.
- Birth date and place: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`; `En esta`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.

Interpretation kept separate: these are mutually exclusive row identities for the same assigned entry number and source path. This is not a spelling variant.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Evidence supporting:

- The current chunk and staged source packet agree on `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
- The source packet explicitly treats this as family-relevant Pulgar/Arriagada evidence while holding promotion for conversion QA.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` contain low-confidence/probable evidence snapshots from this same local evidence cluster, which supports relevance but does not independently resolve the conversion conflict.

Evidence against or limiting:

- The assigned converted Markdown gives a different family for entry 172.
- The father suffix/final mark remains unresolved.

Scores:

| Metric | Score | Reason |
| --- | ---: | --- |
| identity_confidence | 0.64 | Coherent chunk/source-packet cluster, weakened by the converted-file disagreement. |
| conflict_severity | 0.95 | Different child, parents, birth date/place, and likely row identity. |
| evidence_quality | 0.62 | Civil registration would be strong, but present evidence is derivative-conflicted. |
| conversion_confidence | 0.35 | Chunk and converted Markdown materially disagree. |
| claim_probability | 0.66 | Probable only if targeted QA confirms the Pulgar row. |
| relevance | 0.96 | Directly relevant to Pulgar/Arriagada parent candidates. |
| canonical_readiness | 0.10 | Blocked pending conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Evidence supporting:

- The assigned converted Markdown literally records entry 172 as `Jose Francisco`, child of `Oswaldo Gomez` and `Emilia de la Cruz`.

Evidence against or limiting:

- The current chunk and staged source packet record the Pulgar/Arriagada row for the same entry number, source, converted hash, and chunk id.
- The staged conflict draft classifies the issue as row-level conversion or file-assignment conflict.

Scores:

| Metric | Score | Reason |
| --- | ---: | --- |
| identity_confidence | 0.40 | Supported by one derivative transcript and contradicted by the chunk/source packet. |
| conflict_severity | 0.95 | Mutually exclusive entry-172 identity. |
| evidence_quality | 0.48 | Single derivative support in direct conflict. |
| conversion_confidence | 0.30 | Cannot be trusted without row reconciliation. |
| claim_probability | 0.34 | Possible as the true row, not promotion-ready. |
| relevance | 0.88 | Directly relevant as the conflicting identity cluster. |
| canonical_readiness | 0.05 | Blocked. |

## Hypothesis 3: Father Candidate Equals Canonical Jose del Carmen Pulgar

Evidence supporting:

- The chunk/source packet father line overlaps with canonical `wiki/people/jose-del-carmen-pulgar.md` by the name `Jose del Carmen Pulgar`.
- The canonical page already has a separate draft child link to `Tulio Cesar Luis Jose`, so this name exists in local Pulgar-line context.

Evidence against or limiting:

- The entry-172 father line may include `S.` or an uncertain final mark; the exact literal form is not settled.
- The canonical page does not prove that the entry-172 father and the Tulio-related father candidate are the same person.
- Name overlap alone cannot support a duplicate-person merge or parent merge.

Scores:

| Metric | Score | Reason |
| --- | ---: | --- |
| identity_confidence | 0.42 | Plausible local name overlap, but no independent identity bridge. |
| conflict_severity | 0.60 | Main risk is a premature parent or duplicate merge. |
| evidence_quality | 0.45 | Conflicted entry plus separate draft wiki context. |
| conversion_confidence | 0.35 | Father line depends on row QA. |
| claim_probability | 0.40 | Possible, unproved. |
| relevance | 0.82 | Relevant if the Pulgar row is confirmed. |
| canonical_readiness | 0.08 | Blocked. |

## Hypothesis 4: Juana Arriagada de Pulgar Is A Distinct Mother Candidate

Evidence supporting:

- The current chunk/source packet literally names `Juana Arriagada de Pulgar` as mother.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` carries a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from this same local evidence cluster.

Evidence against or limiting:

- The assigned converted Markdown names `Emilia de la Cruz` as mother.
- Other local Juana candidates exist, including `Juana de Dios Amagada de Pulgar`; this draft does not prove that any Juana candidates are the same person.

Scores:

| Metric | Score | Reason |
| --- | ---: | --- |
| identity_confidence | 0.60 | Coherent in the Pulgar row, but row QA is unresolved. |
| conflict_severity | 0.72 | Risk includes row conflict and wrong Juana merge. |
| evidence_quality | 0.58 | Direct civil-register style evidence if confirmed, currently derivative-conflicted. |
| conversion_confidence | 0.35 | Same row-level conversion blocker. |
| claim_probability | 0.62 | Probable only if the Pulgar row is confirmed. |
| relevance | 0.94 | Direct mother candidate for entry 172. |
| canonical_readiness | 0.10 | Blocked. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: canonical family-supplied maternal grandfather of Alexander John Heinz. Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, or a grandchild relationship.
- `Dario Arturo Pulgar`: staged CV/work-history context identifies a document-level CV subject by source title and document continuity; entry 172 does not bridge to that CV subject.
- `Dario Jose Pulgar-Arriagada`: this exact full form is not established by entry 172. The local Dario/Pulgar-Arriagada context must remain separate unless a proof-reviewed source supplies matching identity anchors.
- `Dario J. Pulgar Arriagada`: separate staged medical-title context lists this name under `Medicos-Cirujanos` in a 2 September 1918 university session; entry 172 does not expand or connect to that `J.` initial.
- `Dario/Dario Pulgar Arriagada` and `Dario Pulgar-Arriagada`: separate official/convention and canonical contexts name a Chile-related public/medical-service figure, but they do not state parents, birth date, or a relationship to this entry-172 child.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Jose del Carmen Pulgar [?]`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` must remain separate or unresolved until conversion QA and proof review provide exact bridges.

Ranked Dario-line hypotheses:

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is not direct evidence for any Dario identity; it is only a possible Pulgar/Juana parent-candidate clue after QA. | 0.90 | Complete targeted conversion QA, then proof-review the entry-172 child and parent readings before lineage comparison. |
| 2 | Entry 172 may later become an ancestor or collateral-line clue for a Dario Pulgar-Arriagada or Pulgar-Smith cluster. | 0.18 | Require a separate proof-reviewed bridge from the entry-172 child or parents to a Dario candidate. |
| 3 | Entry 172 directly identifies `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. | 0.02 | No promotion path from this draft; needs direct identity-bearing evidence in another source. |

## Conflicts

- Same-person conflict: unresolved for `Jose del Carmen Pulgar [?]` versus canonical `Jose del Carmen Pulgar`.
- Duplicate-person conflict: high risk if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar` or other Juana candidates without a bridge.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` are literal-reading alternatives, not settled variants.
- Relationship conflict: child-father, child-mother, and parental-pair candidates depend on whether the Pulgar row is the controlling entry-172 row.
- Chronology conflict: no internal chronology conflict is established in the Pulgar row, but the birth chronology is not canonically usable until the row is confirmed.
- Dario-line conflict: no direct Dario evidence appears in entry 172; merging by Pulgar/Arriagada name context alone is unsupported.

## Recommended Next Action

Keep the staged draft and all dependent evidence at `hold_for_conversion_qa`. The exact next step is targeted conversion QA against the source image, assigned converted Markdown, current chunk, and source packet, explicitly deciding whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row and certifying the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review before any canonical claim, relationship, parent merge, Dario-line comparison, or wiki promotion.
