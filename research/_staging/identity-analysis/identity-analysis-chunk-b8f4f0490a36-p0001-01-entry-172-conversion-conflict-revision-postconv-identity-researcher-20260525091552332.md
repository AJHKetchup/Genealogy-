---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525091552332
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity And Conflict Analysis: Entry 172 Conversion Conflict

## Blockers First

1. Material row-level conversion conflict blocks canonical use. The staged conflict draft, source packet, and current chunk treat entry 172 as a Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`; the assigned converted Markdown treats entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`.
2. The father field is not proof-ready. The chunk/source packet preserve `Jose del Carmen Pulgar S.`, while the conflict draft requires keeping three QA outcomes open: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. Existing canonical pages already contain low-confidence or draft Pulgar/Juana/Jose evidence. Do not use this staged conflict to merge parent candidates, rename pages, or promote relationships.
4. No Dario identity is named in this entry. Dario-line context is only an anti-conflation check until a separate proof-reviewed identity bridge connects the clusters.

## Literal Evidence Under Review

- Current staged conflict draft: says the current chunk supports entry 172 as the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Referenced current chunk: entry 172 reads `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, parents domiciled at `Calle de Colipí`, informant `Ernesto Herrera L.`, official `Emilio Riquelme V.`
- Assigned converted Markdown: entry 172 reads `José Francisco`, male, born 26 March 1888 at 10 p.m. in `En esta`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, informant `Oswaldo Gomez`, official `Camilo Henriquez`.
- Existing canonical context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has staged/probable evidence from an entry-172 source packet, including a probable mother link to `Juana Arriagada de Pulgar`; `wiki/people/juana-arriagada-de-pulgar.md` mirrors that probable child link with confidence 1; `wiki/people/jose-del-carmen-pulgar.md` currently has a draft child link to a different entry/person, `Tulio Cesar Luis Jose`; `wiki/people/juana-de-dios-amagada-de-pulgar.md` has a draft child link to `Tulio Cesar Luis Jose`.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Interpretation: the controlling entry 172 row is for `Jose del Carmen Segundo Pulgar Arriagada`, with parents `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`.

Supporting evidence:

- The current chunk and source packet agree on the Pulgar/Arriagada row and preserve a detailed row-level transcription.
- The staged conflict draft identifies the converted Markdown's Gomez/de la Cruz row as a row-level conversion or file-assignment conflict, not a spelling variant.
- Existing canonical pages already show the Pulgar/Arriagada entry-172 cluster as staged/probable rather than final, which fits a hold-for-QA analysis.

Conflicts and limits:

- The assigned converted Markdown directly contradicts the child, parents, birth date/place, informant, and official.
- Father exactness remains unresolved because `Pulgar S.` may be a suffix, a transcription artifact, or uncertain.
- This hypothesis supports the row identity only after conversion QA; it does not prove broader same-person relationships with other Jose/Juana candidates.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Strong local chunk/source-packet agreement, reduced by derivative conversion conflict. |
| conflict_severity | 0.95 | Different child and parents; material row-level conflict. |
| evidence_quality | 0.68 | Civil-registration row is high-value if confirmed, but the active derivative set disagrees. |
| conversion_confidence | 0.42 | Current chunk is coherent; assigned converted Markdown is incompatible. |
| claim_probability | 0.76 | Pulgar/Arriagada is more probable within the staged conflict set, but not promotion-ready. |
| relevance | 0.96 | Directly relevant to the Pulgar/Arriagada parent-child cluster. |
| canonical_readiness | 0.18 | Hold until targeted conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Interpretation: the assigned converted Markdown is the controlling transcript for entry 172, and the current chunk/source packet are assigned to the wrong row or wrong source.

Supporting evidence:

- The assigned converted Markdown explicitly labels its row as entry 172 and gives a complete Gomez/de la Cruz birth registration.

Conflicts and limits:

- The staged conflict draft and source packet were created specifically because the current chunk supports a different Pulgar/Arriagada row.
- The Gomez/de la Cruz row has no Pulgar/Arriagada family relevance and cannot support the Jose/Juana parent cluster.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | Supported only by the assigned converted Markdown in this staged set. |
| conflict_severity | 0.95 | Mutually exclusive with the Pulgar/Arriagada row. |
| evidence_quality | 0.38 | Complete transcript, but contradicted by the staged chunk/source-packet chain. |
| conversion_confidence | 0.30 | The conflict itself makes the converted file unreliable for this task. |
| claim_probability | 0.22 | Possible assignment problem, not the leading identity hypothesis. |
| relevance | 0.05 | Not relevant to the Pulgar line except as a conversion blocker. |
| canonical_readiness | 0.00 | Do not promote into Pulgar/Jose/Juana pages. |

## Hypothesis 3: Jose/Juana Parent Candidate Link

Interpretation: if the Pulgar/Arriagada row is confirmed, entry 172 may support a child-parent relationship between `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar [?]`, and `Juana Arriagada de Pulgar`.

Supporting evidence:

- Literal row reading in the current chunk names the child and names father and mother in the parent column.
- Existing canonical pages already stage `Juana Arriagada de Pulgar` as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`, with low confidence.

Conflicts and limits:

- The father exact name cannot be normalized until QA certifies the final suffix.
- This entry does not prove that `Jose del Carmen Pulgar [?]` is the same person as existing `wiki/people/jose-del-carmen-pulgar.md`, which currently carries a draft link to a different child cluster.
- This entry does not prove that `Juana Arriagada de Pulgar` is the same person as `Juana de Dios Amagada de Pulgar` or any `Juana de Dios Amador de Pulgar` reading from entry 513 contexts.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Parent names are direct in the chunk but blocked by conversion conflict and father-name uncertainty. |
| conflict_severity | 0.80 | Risk of conflating separate Jose/Juana candidates is significant. |
| evidence_quality | 0.62 | Potential direct birth-register evidence, not yet clean. |
| conversion_confidence | 0.42 | Same row-level blocker controls the relationship evidence. |
| claim_probability | 0.64 | Probable if QA confirms the Pulgar row; not yet canonical. |
| relevance | 0.94 | Directly relevant to parent-candidate review. |
| canonical_readiness | 0.16 | Hold for QA and proof review. |

## Required Pulgar-Line Comparison

| Candidate | Comparison To This Entry | Rank | Probability | Required next step |
| --- | --- | ---: | ---: | --- |
| `Jose del Carmen Segundo Pulgar Arriagada` | Directly named by the current chunk/source packet as the entry-172 child. | 1 | 0.76 | Targeted conversion QA for entry 172, then proof review of child identity and birth facts. |
| `Juana Arriagada de Pulgar` | Directly named by the current chunk/source packet as mother if the Pulgar row controls. | 2 | 0.64 | QA-confirm row and then proof-review the mother-child relationship before canonical update. |
| `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` / `Jose del Carmen Pulgar [?]` | Directly named as father in the current chunk, but exact suffix is unresolved. | 3 | 0.56 | QA must certify exact father field before any parent-candidate merge. |
| `Dario Arturo Pulgar-Smith` | Existing canonical family-supplied maternal-grandfather page; this entry does not name Dario, Arturo, or Smith. | 4 | 0.03 | Separate identity-bridge proof review; do not attach this entry by surname/family context alone. |
| `Dario Arturo Pulgar` | Existing staged CV subject cluster; no shared given name, date, role, or source context with entry 172. | 5 | 0.02 | Keep separate unless a proof-reviewed lineage source bridges the CV subject to this 1888 child or parents. |
| `Dario Jose Pulgar-Arriagada` | Existing staged photo/Geneva context uses Dario Jose/Pulgar-Arriagada, but entry 172 names Jose del Carmen Segundo, not Dario Jose. | 6 | 0.02 | Require explicit proof-reviewed bridge between names before any same-person or lineage claim. |
| `Darío/Dario Pulgar Arriagada` | Existing Pulgar-Arriagada contexts may share surname elements only; entry 172 has no Dario reading. | 7 | 0.02 | Maintain as separate name cluster; do not merge by surname alone. |
| `Juana de Dios Amagada de Pulgar` / `Juana de Dios Amador de Pulgar` | Existing entry-513 parent candidate differs from `Juana Arriagada de Pulgar`; this entry does not settle that variant. | 8 | 0.08 | Compare only in a later parent-candidate proof review after both entry 172 and entry 513 readings are QA-stable. |

## Conflict Findings

- Same-person conflict: unresolved for all Dario clusters. This entry supplies no bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Darío/Dario Pulgar Arriagada.
- Duplicate-person risk: high if the father `Jose del Carmen Pulgar [?]` is silently merged into the existing `Jose del Carmen Pulgar` page before suffix and cross-entry evidence are reviewed.
- Name-variant conflict: `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada/Amador de Pulgar` is not resolved by this source. Treat as separate parent-candidate review, not a correction.
- Relationship conflict: current canonical snapshots show low-confidence or draft relationships; this staged conflict cannot raise them to canonical status while the conversion conflict remains active.
- Chronology conflict: none proved inside this entry. Chronology comparison to Dario clusters is negative evidence only because this is an 1888 birth registration and no Dario identity is named.

## Recommended Next Action

Keep this staged draft and all dependent person, claim, relationship, and parent-candidate materials at `hold_for_conversion_qa`.

Exact next proof-review/promotion step: run targeted conversion QA on register page 58, entry 172 using the source image, assigned converted Markdown, current chunk, and source packet. The QA note must decide the controlling row and record the father field as exactly one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review for the child birth facts and parent-child relationships before any canonical promotion, merge, or Dario-line identity bridge.
