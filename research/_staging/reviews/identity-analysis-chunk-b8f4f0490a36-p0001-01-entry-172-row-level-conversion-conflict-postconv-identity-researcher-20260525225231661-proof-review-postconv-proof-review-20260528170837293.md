---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260528170837293"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225231661.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225231661.md"
output_area: "research/_staging/reviews/"
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.90
conversion_confidence_score: 0.45
evidence_quantity_score: 0.55
agreement_score: 0.62
identity_confidence_score: 0.54
claim_probability: 0.74
relevance_level: high
relevance_confidence: 0.95
---

# Proof Review: Entry 172 Row-Level Conversion Conflict Identity Analysis

Review of staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225231661.md`.

## Blockers First

1. Canonical promotion remains blocked because the assigned chunk/source packet and the current converted Markdown still disagree materially for entry 172.
2. The current converted Markdown gives entry 172 as a Burgos/de la Cruz birth, while the chunk, source packet, conflict draft, and visible source image support a Pulgar/Arriagada row for entry 172 on page 58.
3. The father-name suffix or final mark after `Jose del Carmen Pulgar` is not safe to normalize from the review context alone. It should remain uncertain until targeted conversion QA certifies the visible father field.
4. The staged identity analysis correctly rejects any Dario-line attachment from this row. This source names no Dario, Arturo, Smith, CV, medical-title, passenger, photograph, legal-notice, or lineage bridge.
5. No child identity, birth fact, parent fact, parent-child relationship, duplicate merge, or canonical wiki update should be promoted from this draft until the converted Markdown conflict is resolved or superseded by targeted QA.

## Evidence Checked

- Staged identity analysis: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225231661.md`.
- Staged conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

The source image visibly places entry 172 on page 58 in the Pulgar/Arriagada row. The assigned chunk and source packet agree with that visible row on the child, sex, registration date, birth date and time, birthplace, mother, informant, and overall family context.

The staged identity analysis is well supported in treating the Burgos/de la Cruz text as a row-control or conversion-control conflict, not as an identity variant. The names, parents, birth dates, places, and informants are too different to reconcile as one child or one parent set.

The draft also handles identity risk appropriately. It keeps `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and Dario-line candidates separated pending later proof work.

## Scored Judgment

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth register image is a strong direct source for the row, though image legibility is not perfect for every name detail. |
| conversion_confidence_score | 0.45 | The chunk/source packet align with the image, but the current converted Markdown is materially wrong or mis-controlled for this row. |
| evidence_quantity_score | 0.55 | One direct source image plus derivative artifacts; no independent corroborating record reviewed for identity bridges. |
| agreement_score | 0.62 | Source image, chunk, packet, and conflict draft agree on Pulgar/Arriagada; converted Markdown strongly disagrees. |
| identity_confidence_score | 0.54 | Moderate confidence for the row-level Pulgar/Arriagada reading; low confidence for attaching the people to canonical identities. |
| claim_probability | 0.74 | The claim that the staged draft correctly identifies a conversion-control conflict is likely. Specific canonical claims remain blocked. |
| relevance_level | high | This row directly controls Pulgar/Arriagada child and parent claims. |
| relevance_confidence | 0.95 | The row is plainly relevant to the staged Pulgar/Arriagada analysis. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until targeted QA resolves or replaces the conflicting converted Markdown and certifies the father field. |

## Claim Probability Notes

| Claim or hypothesis | Probability | Disposition |
| --- | ---: | --- |
| The staged identity analysis correctly identifies a row-level conversion conflict. | 0.86 | Supported. |
| Entry 172 in the visible source image is the Pulgar/Arriagada row described by the chunk/source packet. | 0.82 | Supported, with father suffix still uncertain. |
| The current converted Markdown's Burgos/de la Cruz row is the controlling reading for this source image's entry 172. | 0.08 | Not supported by the visible image reviewed here. |
| The Pulgar/Arriagada row is ready for canonical promotion as person or relationship claims. | 0.10 | Hold. Conversion conflict and father-field uncertainty remain. |
| This row supports a Dario Arturo Pulgar-Smith or Dario Pulgar Arriagada attachment. | 0.03 | Not supported in this source context. |

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`. The QA note should explicitly state that the source image's entry 172 on page 58 is the Pulgar/Arriagada row if confirmed, identify the converted Markdown conflict as a conversion error or row-control mismatch, and certify the father field only to the visible extent. After that, create separate proof-review tasks for child identity, birth facts, parent claims, and parent-child relationships before any canonical promotion.
