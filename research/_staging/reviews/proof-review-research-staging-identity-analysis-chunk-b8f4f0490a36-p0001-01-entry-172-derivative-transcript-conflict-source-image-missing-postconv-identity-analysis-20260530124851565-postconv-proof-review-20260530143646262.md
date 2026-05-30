---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260530143646262"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.56
conversion_confidence_score: 0.34
evidence_quantity_score: 0.44
agreement_score: 0.24
identity_confidence_score: 0.56
claim_probability: 0.62
relevance_level: conditional_high
relevance_confidence: 0.60
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Transcript Conflict

This review covers staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md`.

## Blockers First

- Canonical readiness is `not_ready`; keep the item on `hold_for_conversion_qa`.
- The expected source image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` is absent in this workspace.
- The expected page image `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` is absent in this workspace.
- The assigned chunk/source packet and the current converted Markdown materially disagree for entry `172`. The conflict covers child name, sex wording, parents, birth date/time/place, and informant/declarant.
- The father reading `Jose del Carmen Pulgar S.` is derivative-only. Do not normalize, expand, or canonically attach the terminal `S.` without a visible source reread.
- No Dario identity bridge is supported by the reviewed files. The staged draft correctly treats Dario attachment as very low probability and not promotion-ready.

## Evidence Strengths

- The assigned chunk and source packet internally agree on a Pulgar/Arriagada reading: entry `172`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth `Ocho de Marzo de mil ochocientos ochenta i ocho` at about three in the afternoon at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The current converted Markdown internally supports a different entry `172`: child `José Miguel`, sex `Varon`, birth `El seis de Abril de mil ochocientos ochenta i ocho` at ten at night in `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and declarant `Oswaldo Burgos`.
- The conversion review note explicitly identifies this as unresolved row control because the source/page image was unavailable.
- The staged identity analysis preserves uncertainty and does not attempt a canonical merge, relationship promotion, or Dario-line attachment.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.56 | A civil birth register is a strong source class, but this review had only conflicting derivative text, not the image. |
| conversion_confidence_score | 0.34 | Conversion confidence is low because the chunk and converted Markdown disagree on nearly every identity-bearing field. |
| evidence_quantity_score | 0.44 | Several derivative artifacts exist, but they all point back to one unresolved source target and no image-controlled reread. |
| agreement_score | 0.24 | Internal agreement exists within the Pulgar/Arriagada layer and within the Burgos/de la Cruz layer; cross-layer agreement is poor. |
| identity_confidence_score | 0.56 | Moderate derivative confidence for the Pulgar/Arriagada staged candidate; very low confidence for Dario or canonical parent attachment. |
| claim_probability | 0.62 | The Pulgar/Arriagada row plausibly reflects the intended staged candidate, but it cannot be certified over the converted Markdown conflict. |
| relevance_level | conditional_high | High relevance only if later image-controlled QA certifies the Pulgar/Arriagada row; otherwise low. |
| relevance_confidence | 0.60 | Relevance is plausible but depends entirely on unresolved row control. |
| canonical_readiness | not_ready | No canonical claim, relationship, merge, rename, or wiki update is supported now. |

## Claim Probability Detail

| Claim or hypothesis | Probability | Review finding |
| --- | ---: | --- |
| Entry `172` is the Pulgar/Arriagada row described by the assigned chunk and source packet. | 0.62 | Supported by two internally consistent derivative artifacts; not image-certified. |
| Entry `172` is the Burgos/de la Cruz row described by the current converted Markdown. | 0.24 | Supported by the converted Markdown; contradicted by the assigned chunk and source packet. |
| The conflict reflects different physical rows or images under one entry target. | 0.88 | The breadth of disagreement across names, parents, dates, places, and informants makes row/image misalignment likely. |
| `Jose del Carmen Segundo Pulgar Arriagada` is a Dario candidate. | 0.03 | The reviewed files do not literally name Dario or provide a bridge by occupation, spouse, child, later event, or family cluster. |
| Existing Jose/Juana parent candidates can be attached canonically now. | 0.16 | Parent attachment is possible only after row control and parent-name readings are certified from the visible source. |

## Next Action

Keep this staged draft on `hold_for_conversion_qa`. The next action is targeted conversion QA: restore or locate the original source image or certified page image, then compare physical entry `172` against the assigned chunk, source packet, conversion review note, and current converted Markdown. After physical row control is certified, rerun proof review on the child, sex, birth event, father, mother, informant, and any proposed parent-child or identity-bridge claims.
