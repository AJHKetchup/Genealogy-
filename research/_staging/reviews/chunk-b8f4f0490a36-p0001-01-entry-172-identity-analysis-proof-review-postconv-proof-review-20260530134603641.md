---
type: proof_review
status: completed
role: claim_reviewer
worker: "postconv-proof-review-20260530134603641"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_reference: "page 1; register page 58; entry 172"
source_quality_score: 0.72
conversion_confidence_score: 0.34
evidence_quantity_score: 0.46
agreement_score: 0.18
identity_confidence_score: 0.58
claim_probability: 0.64
relevance_level: "conditional_high"
relevance_confidence: 0.55
canonical_readiness: "not_ready"
promotion_recommendation: "hold_for_conversion_qa"
---

# Proof Review: Entry 172 Identity/Conflict Analysis

This review covers only the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md` and the referenced verification files listed in the front matter.

## Blockers First

- The source image is unavailable at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.
- The conversion-job page image is unavailable at `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`.
- The assigned chunk and current converted Markdown give materially different entry-172 identities. The chunk records `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted file records `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Because row control cannot be checked against the visible source, no child identity, parent-child relationship, Dario-line attachment, merge, rename, or canonical wiki update is proof-ready from this draft.
- The father field `Jose del Carmen Pulgar S.` remains a derivative reading only. The terminal `S.` must not be normalized or promoted without image-controlled review.

## Evidence Strengths

- The staged identity analysis accurately preserves the main derivative conflict found in the conflict draft, source packet, conversion QA note, chunk, and converted Markdown.
- The source type, if certified, would be strong: a civil birth-registration table with direct statements of child, date, place, parents, and informant.
- The assigned chunk and source packet agree internally on the Pulgar/Arriagada row details for entry `172`.
- The converted Markdown also gives an explicit entry `172`, which makes the conflict concrete rather than speculative.
- The staged draft correctly avoids converting the Pulgar/Arriagada evidence into a same-person conclusion for any Dario candidate.

## Scored Judgment

| Dimension | Score / value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.72 | Civil registration would be a high-quality source, but the actual image is missing for this review. |
| conversion_confidence_score | 0.34 | Conversion confidence is low because the two derivative transcript layers disagree on core row content. |
| evidence_quantity_score | 0.46 | There are several derivative layers, but only one unavailable underlying image. |
| agreement_score | 0.18 | Agreement is limited to entry number and broad document context; names, parents, dates, places, and informants conflict. |
| identity_confidence_score | 0.58 | Moderate confidence that the staged conflict analysis describes a real row-control problem; low confidence for promoting either identity. |
| claim_probability | 0.64 | Probability that the Pulgar/Arriagada row is the intended row for this staged task, based on chunk/source-packet agreement; not source-certified. |
| relevance_level | conditional_high | High for Pulgar/Arriagada research only if the chunk row is later certified; low if the converted Burgos/de la Cruz row controls. |
| relevance_confidence | 0.55 | Relevance depends on unresolved row control. |
| canonical_readiness | not_ready | Hold for conversion QA; no canonical promotion or relationship assertion. |

## Claim Probability Detail

| Claim | Probability | Review result |
| --- | ---: | --- |
| Entry `172` is the Pulgar/Arriagada row described in the assigned chunk. | 0.64 | Plausible but held; supported by chunk and source packet, contradicted by converted Markdown, not image-certified. |
| Entry `172` is the Burgos/de la Cruz row described in the converted Markdown. | 0.24 | Plausible but held; supported by converted Markdown, contradicted by chunk and source packet. |
| The two derivative layers describe different physical rows or substituted page content under one target. | 0.88 | Strong conflict explanation, but exact cause remains unproved without the source image. |
| Any Dario identity is supported by this entry. | 0.02 | Not supported; no Dario, Arturo, Smith, or Dario-specific bridge appears in the checked files. |

## Next Action

Keep this staged draft and all dependent claims on `hold_for_conversion_qa`. The next worker must restore or locate the original source image or certified page image and compare physical entry `172` directly against both derivative readings. Only after row control is certified should a proof reviewer score the child identity, father-field reading, mother-field reading, birth event, informant, and any parent-child relationship for canonical use.
