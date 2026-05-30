---
type: proof_review
status: reviewed
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110953508.md"
worker: "postconv-proof-review-20260530115951389"
role: claim_reviewer
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110953508.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: not_ready
recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

This review covers only the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110953508.md` and its referenced derivative verification context.

## Blockers First

- Row-control is unresolved. The assigned chunk and source packet identify entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the current converted Markdown identifies entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The original source image cannot be used for this review. `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` is absent locally, and the referenced `extracted-images` directory is also absent.
- The disagreement is identity-controlling, not a minor transcription variance. Child name, parents, birth date/time/place, informant, and page/register context differ.
- The father-field suffix in the Pulgar reading is not settled beyond the derivative transcription `Jose del Carmen Pulgar S.`; the source packet correctly bounds this as `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar [?]` until image QA.
- No Dario identity claim is supported by this staged draft. The record does not name Dario, Arturo, Smith, Dario Jose, Dario Pulgar Arriagada, or Dario Pulgar A.
- Canonical promotion is blocked. No birth fact, parent-child relationship, spousal clue, identity merge, or wiki update should be promoted from this draft.

## Evidence Strengths

- A civil birth registration would be a strong source type if the controlling row were certified.
- The assigned chunk and revised source packet agree with each other on the Pulgar/Arriagada reading for entry `172`.
- The current converted Markdown is available and gives a clear alternate Burgos/de la Cruz reading, which supports the conclusion that this is a real derivative conflict requiring row-control QA.
- The staged identity analysis appropriately treats the Dario comparisons as anti-conflation checks rather than promotion evidence.

## Scored Judgment

| Dimension | Score / value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.72 | Civil registration is high-value evidence, but the review cannot inspect the source image. |
| conversion_confidence_score | 0.30 | Existing derivative layers materially disagree on the same entry number. |
| evidence_quantity_score | 0.45 | Two derivative readings and a source packet are available, but no full image or row crop confirms the controlling row. |
| agreement_score | 0.25 | Chunk/source packet agree with each other, but they conflict with the converted Markdown. |
| identity_confidence_score | 0.28 | Identity confidence is low because the controlling row has not been certified. |
| claim_probability | 0.62 | Probability that the staged draft's hold-for-QA conclusion is correct; probability of any specific parent-child claim is lower until QA. |
| relevance_level | high_if_pulgar_row_certified | The Pulgar reading is relevant, but the Burgos reading would remove Pulgar-line relevance. |
| relevance_confidence | 0.58 | Relevance depends on row-control certification. |
| canonical_readiness | not_ready | Hold for conversion QA; do not promote. |

## Claim-Level Assessment

| Claim or inference | Support | Probability | Readiness |
| --- | --- | ---: | --- |
| Entry `172` is currently in row-control conflict. | Directly supported by the chunk/source packet versus converted Markdown disagreement. | 0.90 | hold_for_conversion_qa |
| Entry `172` is the Pulgar/Arriagada row. | Supported by assigned chunk and source packet; contradicted by converted Markdown; source image absent. | 0.62 | not_ready |
| Entry `172` is the Burgos/de la Cruz row. | Supported by converted Markdown; contradicted by chunk/source packet. | 0.24 | not_ready |
| `Jose del Carmen Pulgar` is the father in the certified entry. | Supported only if the Pulgar row is certified; suffix remains unresolved. | 0.40 | not_ready |
| `Juana Arriagada de Pulgar` is the mother in the certified entry. | Supported only if the Pulgar row is certified. | 0.48 | not_ready |
| The entry supports a Dario Pulgar identity bridge. | No literal name or relationship bridge in the reviewed context. | 0.02 | not_ready |

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. The next worker should restore or locate the original full-page image, certify which physical row controls entry `172`, and re-check the father field suffix before any proof review considers claims or relationships for promotion.

Do not edit canonical pages, promote claims, attach relationships, or merge Jose/Juana/Dario candidates from this staged draft.
