---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260527203255281"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
reviewed_claim_type: identity_conflict_analysis
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Row Conflict

## Blockers

1. The raw source image cited by the draft is not present at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and the expected conversion-job page image is also absent. This review cannot independently certify the physical row for entry `172`.
2. The assigned chunk and source packet conflict materially with the current converted Markdown. The chunk/source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted Markdown reads entry `172` as `José Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.
3. The father suffix remains unresolved. The chunk has `Jose del Carmen Pulgar S.`, while an earlier image-reviewed note preserved only `Jose del Carmen Pulgar` and required targeted confirmation for any suffix or additional name component.
4. No reviewed entry-172 material names Dario, Arturo, Smith, or a Dario-line relationship. Any Dario/Pulgar-Smith attachment remains unsupported from this draft.
5. Claims in the staged draft that rely on existing canonical pages were not needed to verify this hold decision and should not be treated as promotion support.

## Evidence Strengths

- The staged draft accurately identifies the central derivative conflict: two current derivative layers assign incompatible families, dates, and parents to the same entry number.
- The held source packet repeats the Pulgar/Arriagada reading and explicitly flags the conversion-control problem instead of promoting the row.
- The current converted Markdown directly supports the competing Burgos/de la Cruz reading, making this a real row-control conflict rather than a spelling or name-variant issue.
- Prior staged conversion-review notes support the caution that the Pulgar/Arriagada row may be the correct physical row, but those notes also keep the father suffix and final conversion reconciliation unresolved.

## Scores

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration would be strong source material, but the source image is absent in this checkout for this review. |
| conversion_confidence_score | 0.30 | The chunk and converted Markdown disagree on the entire entry-172 family. |
| evidence_quantity_score | 0.55 | Several derivative/staged materials exist, but independent image verification is unavailable here. |
| agreement_score | 0.25 | Agreement is low across the current derivative layers; agreement is higher only within the held Pulgar/Arriagada packet family. |
| identity_confidence_score | 0.58 | Moderate for treating the Pulgar/Arriagada row as a plausible held hypothesis; insufficient for canonical identity or relationship promotion. |
| claim_probability | 0.84 | High probability that the staged draft's hold recommendation is correct. Lower probability for any specific row conclusion until image QA is restored. |
| relevance_level | high | The conflict directly affects Pulgar/Arriagada identity and parent-child claims. |
| relevance_confidence | 0.88 | The names in the chunk/source packet are clearly Pulgar/Arriagada-relevant, even though canonical use is blocked. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, merges, page updates, or Dario-line attachments from this draft. |

## Claim Judgment

The staged identity-analysis draft is supported as a cautious hold. Its strongest supported claim is not that entry `172` is definitively the Pulgar/Arriagada birth row, but that the derivative layers are in serious conflict and must stay out of canonical promotion until targeted conversion QA reconciles the source image, chunk, and converted Markdown.

The draft's anti-conflation guidance is also supported. Entry `172` as reviewed here does not name Dario or Arturo and does not provide a relationship bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or any Dario/Darío Pulgar cluster.

## Next Action

Keep the staged draft at `hold_for_conversion_qa`. The next action is targeted conversion QA with the source image restored: decide whether physical entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row, then certify the father field only to the visible level of certainty. After that, rerun proof review before any canonical claim, relationship, merge, wiki-page update, or Dario-line comparison.
