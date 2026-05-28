---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260528220118497"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md"
output_area: "research/_staging/reviews/"
review_decision: hold
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.86
conversion_confidence_score: 0.38
evidence_quantity_score: 0.62
agreement_score: 0.44
identity_confidence_score: 0.52
claim_probability: 0.58
relevance_level: high
relevance_confidence: 0.95
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md`.

## Blockers First

1. Canonical promotion remains blocked because the referenced converted Markdown and the assigned chunk do not transcribe the same entry-172 row.
2. The source image and assigned chunk support a Pulgar/Arriagada entry 172, while the current converted file reports a Burgos/de la Cruz entry 172. These cannot be treated as name variants or a same-person conflict.
3. The father field in the Pulgar/Arriagada row is not safe for canonical normalization beyond the visible/derivative reading `Jose del Carmen Pulgar S.` unless targeted conversion QA certifies the exact mark after `Pulgar`.
4. No Dario-line attachment, parent merge, duplicate merge, child identity claim, birth fact, or parent-child relationship should be promoted from this draft.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

The source image visibly places entry 172 on page 58 as a Pulgar/Arriagada row. It supports the staged draft's central claim that the current converted Markdown is not aligned with the controlling source image for this task. The assigned chunk and source packet agree with the image on the child name, registration date, birth date, birthplace, parents, and informant at a row-control level.

The staged draft correctly treats this as a conversion-control problem rather than a genealogical identity resolution. Its warnings against Dario-line attachment and Jose/Juana parent merging are supported by the reviewed evidence.

## Scored Judgment

| Dimension | Score / value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth-register image is a strong source, and the relevant row is visible enough to verify the broad Pulgar/Arriagada control. |
| conversion_confidence_score | 0.38 | Current converted Markdown materially disagrees with the source image and assigned chunk; chunk confidence is higher than converted-file confidence, but the conversion set is conflicted. |
| evidence_quantity_score | 0.62 | One source image plus derivative chunk/source packet are enough to identify the row-control conflict, not enough for canonical family attachment. |
| agreement_score | 0.44 | Source image, chunk, and source packet agree with each other; converted Markdown disagrees on every major identity field. |
| identity_confidence_score | 0.52 | Moderate confidence that the draft identifies the competing row problem; low confidence for attaching the row to canonical persons. |
| claim_probability | 0.58 | The claim that Pulgar/Arriagada is the intended entry-172 row is more likely than not after image review, but still needs formal conversion QA before reuse. |
| relevance_level | high | Directly affects Pulgar/Arriagada identity, birth, and parent relationship claims. |
| relevance_confidence | 0.95 | The row-level conflict is directly relevant to the staged draft's subject. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until conversion QA reconciles the converted file/chunk/source image conflict. |

## Claim-Level Review

| Claim | Review result | Probability | Notes |
| --- | --- | ---: | --- |
| The staged draft correctly identifies a row-level conversion conflict. | supported | 0.95 | The current converted Markdown gives `José Miguel`, `Oswaldo Burgos`, and `Concepcion de la Cruz`; the source image/chunk/source packet give a Pulgar/Arriagada row. |
| Entry 172 in the source image is a Pulgar/Arriagada birth-registration row. | likely_supported_pending_qa | 0.82 | The visible image supports this at row-control level, but this proof review should not rewrite the conversion. |
| `Jose del Carmen Segundo Pulgar Arriagada` can be promoted as a canonical child identity from this draft. | hold | 0.55 | The row looks plausible, but canonical promotion is blocked by conversion conflict and needs separate claim review. |
| `Jose del Carmen Pulgar S.` can be promoted as the father exactly. | hold | 0.48 | The source/chunk support a Pulgar father, but the suffix/mark still needs targeted reread. |
| `Juana Arriagada de Pulgar` can be promoted as the mother exactly. | hold | 0.58 | Supported by the image/chunk at row level, but still dependent on conversion QA and later relationship review. |
| This row supports Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario J. Pulgar Arriagada. | not_supported | 0.04 | No Dario/Arturo/Smith identity bridge appears in the reviewed row. |

## Next Action

Hold the staged draft for targeted conversion QA. The next worker should reconcile the source image, assigned chunk, source packet, and current converted Markdown; certify the controlling entry-172 row; and separately reread the father field. After QA, create separate proof-reviewed claims for the child, birth event, mother, father, and parent-child relationships before any canonical promotion.
