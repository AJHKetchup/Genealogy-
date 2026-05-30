---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260530141605588"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.56
conversion_confidence_score: 0.38
evidence_quantity_score: 0.42
agreement_score: 0.22
identity_confidence_score: 0.58
claim_probability: 0.64
relevance_level: conditional_high
relevance_confidence: 0.62
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Transcript Conflict

This review covers only the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md` and its referenced verification files.

## Blockers First

- Row control is not certified. The referenced source image path and conversion-job page image path are absent in this workspace, so I could not verify the physical entry from an image.
- The assigned chunk/source packet and current converted Markdown materially disagree for entry `172`: child, parents, birth date/time/place, and informant differ.
- No canonical claim, parent-child relationship, identity merge, Dario-line attachment, or wiki update is ready from this staged draft.
- The father-name suffix in `Jose del Carmen Pulgar S.` remains derivative-only; the terminal mark should not be normalized or promoted without image-controlled QA.

## Evidence Strengths

- The assigned chunk and source packet internally agree that entry `172` is a Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The current converted Markdown internally supports a different entry `172` for `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The staged identity analysis accurately treats this as a derivative transcript conflict rather than a harmless name variant.
- A civil birth register would be a strong source class if row control were restored, but this review only has conflicting derivative text.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.56 | Civil birth registration is a strong record type, but the source image is unavailable here. |
| conversion_confidence_score | 0.38 | The chunk and converted Markdown disagree on core identity fields, and image reread is unavailable. |
| evidence_quantity_score | 0.42 | There are multiple derivative layers, but only one conflicted event and no image-controlled confirmation. |
| agreement_score | 0.22 | Agreement exists within each derivative layer, but the two derivative layers sharply conflict with each other. |
| identity_confidence_score | 0.58 | Moderate confidence for the Pulgar/Arriagada candidate as a staged derivative reading; very low confidence for any Dario attachment. |
| claim_probability | 0.64 | The Pulgar/Arriagada row is plausible because the assigned chunk and packet agree, but it cannot be certified over the converted Markdown conflict. |
| relevance_level | conditional_high | High only if later row-control QA certifies the Pulgar/Arriagada row; low if the Burgos/de la Cruz reading controls. |
| relevance_confidence | 0.62 | Family relevance depends on unresolved row control. |
| canonical_readiness | not_ready | Hold for conversion QA; no promotion or canonical update is supported. |

## Claim Probability Detail

| Claim or hypothesis | Probability | Review finding |
| --- | ---: | --- |
| Entry `172` is the Pulgar/Arriagada row described by the assigned chunk. | 0.64 | Supported by the assigned chunk and source packet; not image-certified. |
| Entry `172` is the Burgos/de la Cruz row described by the current converted Markdown. | 0.24 | Supported by the converted Markdown; contradicted by the chunk and source packet. |
| The conflict reflects different physical rows or images under one entry target. | 0.88 | Best explanation for the breadth of disagreement across names, dates, places, and informants. |
| The child is a Dario Pulgar candidate. | 0.03 | The reviewed files do not literally name Dario or provide an identity bridge. |
| Existing Jose/Juana parent candidates can be canonically attached now. | 0.18 | Possible only after row control and parent-field readings are certified. |

## Next Action

Keep this item on `hold_for_conversion_qa`. A conversion-QA worker must locate or restore the original source image or certified page image and compare physical entry `172` against the assigned chunk, source packet, and current converted Markdown. After row control is resolved, proof review should be rerun on the certified child, parents, birth event, informant, and any proposed parent-child or identity-bridge claims.
