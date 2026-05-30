---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530115723059
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
reviewed_source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.78
conversion_confidence_score: 0.35
evidence_quantity_score: 0.45
agreement_score: 0.28
identity_confidence_score: 0.30
claim_probability: 0.64
relevance_level: high
relevance_confidence: 0.82
canonical_readiness: not_ready
recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict Identity Analysis

This review covers staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md`.

## Blockers First

- Row-control remains unresolved. The assigned chunk/source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, while the converted file and job page Markdown read entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Full-image verification is unavailable in this checkout. The referenced source PNG path and job page image path both tested absent, so this review cannot certify which physical row controls entry `172`.
- The father-field suffix is not promotion-ready. The chunk has `Jose del Carmen Pulgar S.`, but the source packet correctly limits promotion to `Jose del Carmen Pulgar` or an unresolved marked suffix until the image is visible.
- No Dario identity bridge is supported by the reviewed local evidence. The Pulgar/Arriagada row, if later certified, names Jose del Carmen Segundo, not Dario Arturo, Dario Jose, or a Smith-linked identity.
- Canonical readiness is `not_ready`. No person merge, parent-child relationship, birth event, Dario-line attachment, or wiki update should be promoted from this staged draft until targeted conversion QA resolves row control.

## Evidence Strengths

- The staged draft accurately identifies the central conflict between the assigned chunk/source packet and the converted Markdown for the same entry number.
- The source type is strong in principle: a Chilean civil birth registration, if certified from the image, would be direct evidence for the child name, birth event, parents, and informant.
- The assigned chunk and source packet internally agree on the Pulgar/Arriagada reading: registration date 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; birth 8 March 1888 around 3 p.m. at `Calle de Valdivia`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- The converted file and job page Markdown internally agree on the conflicting Burgos/de la Cruz reading: child `Jose Miguel`; birth 6 April 1888 at 10 p.m.; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`.
- The staged draft's hold recommendation is well supported by the available verification context.

## Scored Judgment

| Dimension | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil registration is a high-quality source type, but the actual image is unavailable for this review. |
| conversion_confidence_score | 0.35 | The derivative materials materially disagree on the same entry number. |
| evidence_quantity_score | 0.45 | There are multiple local derivative texts, but no accessible full-page image in this checkout. |
| agreement_score | 0.28 | Agreement exists within each derivative branch, but the branches conflict directly. |
| identity_confidence_score | 0.30 | The Pulgar/Arriagada cluster is plausible only as a held candidate until row control is certified. |
| claim_probability | 0.64 | The draft's claim that this is a row-control conflict requiring hold is more likely than not and is supported by the reviewed files. |
| relevance_level | high | Pulgar/Arriagada relevance is high if the assigned row is certified. |
| relevance_confidence | 0.82 | The family relevance terms and identities are clear in the assigned chunk/source packet. |
| canonical_readiness | not_ready | Hold; no canonical claim or relationship should be promoted. |

## Claim-Level Review

| Claim | Probability | Disposition | Rationale |
| --- | ---: | --- | --- |
| The staged draft correctly treats the material as a row-control conflict. | 0.88 | support | The reviewed chunk/source packet and converted Markdown assign incompatible children, parents, dates, places, and informants to entry `172`. |
| The Pulgar/Arriagada row controls entry `172`. | 0.62 | hold | Supported by the assigned chunk/source packet, but blocked by the absent full source image and conflicting conversion. |
| The Burgos/de la Cruz row controls entry `172`. | 0.24 | hold | Supported by the converted file/job page Markdown, but contradicted by the assigned chunk/source packet. |
| The father can be promoted as exactly `Jose del Carmen Pulgar S.`. | 0.22 | revise/hold | The chunk reads this way, but the source packet correctly warns that the suffix is not certified. |
| The packet supports any Dario same-person attachment. | 0.03 | reject for now | No reviewed text supplies a Dario name, Smith surname, later-life bridge, or relationship path. |
| Existing canonical Jose/Juana facts can be strengthened now from this packet. | 0.12 | hold | Same-name or family-context evidence is insufficient while row control is unresolved. |

## Next Action

Keep the staged identity analysis on `hold_for_conversion_qa`. The next worker should restore or locate the full original page image and perform targeted row-control QA against the source image, assigned chunk, source packet, converted Markdown, and job page Markdown. The QA note should explicitly decide which physical row controls entry `172` and separately bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that QA result exists, rerun proof review before any canonical promotion, relationship attachment, identity merge, Dario-line comparison, or wiki update.
