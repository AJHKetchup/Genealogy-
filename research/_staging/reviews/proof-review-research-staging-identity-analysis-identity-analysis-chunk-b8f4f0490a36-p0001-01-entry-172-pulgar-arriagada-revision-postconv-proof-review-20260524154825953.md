---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260524154825953
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524145409450.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524145409450.md
reviewed_sources:
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524145409450.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.88
conversion_confidence_score: 0.55
evidence_quantity_score: 0.70
agreement_score: 0.45
identity_confidence_score: 0.78
claim_probability: 0.74
relevance_level: high
relevance_confidence: 0.92
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- The assigned converted Markdown and assigned chunk conflict at the row level. The converted Markdown gives entry 172 as `José Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`, while the chunk and visible source image support entry 172 as a Pulgar/Arriagada birth entry.
- Because the canonical conversion file remains contradictory, the staged draft is not ready for canonical promotion even though the image supports the Pulgar/Arriagada identity cluster.
- The father's exact terminal mark after `Pulgar` remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, but the image does not support treating the suffix as settled for canonical identity use without targeted conversion QA.
- The staged draft correctly excludes Dario attachments. The visible entry does not name Dario, and surname or family context alone would be an identity-risk jump.

## Evidence Strengths

- The source image is a primary civil birth register page and visibly places entry 172 on page 58, dated 7 April 1888, in the Los Angeles birth register.
- The source image supports the central identity cluster in the staged draft: child `Jose del Carmen Segundo Pulgar Arriagada`, male; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`; and broad father reading `Jose del Carmen Pulgar` with an unresolved final mark.
- The assigned chunk agrees with the image on the Pulgar/Arriagada row and gives coherent supporting details: birth date 8 March 1888, about 3 p.m., Calle de Valdivia; parents domiciled Calle de Colipi; informant present at birth.
- The draft's recommendation, `hold_for_conversion_qa`, is proportionate to the evidence. It preserves the supported image reading while preventing promotion from a conflicted conversion set.

## Scored Judgment

- `source_quality_score`: 0.88. Primary civil registration image, relevant and legible enough for the identity cluster, though some handwriting details remain uncertain.
- `conversion_confidence_score`: 0.55. The chunk is useful, but the canonical converted Markdown contradicts it materially.
- `evidence_quantity_score`: 0.70. One directly relevant primary source image plus derivative chunk support; no independent corroborating source reviewed for this task.
- `agreement_score`: 0.45. Image and chunk agree with each other, but the referenced converted Markdown disagrees at the identity level.
- `identity_confidence_score`: 0.78. The child-mother-informant cluster is reasonably supported; the father suffix and conversion conflict lower confidence.
- `claim_probability`: 0.74. The staged analysis is probably correct as a cautionary identity analysis and hold recommendation, but dependent identity claims should not be promoted before QA reconciliation.
- `relevance_level`: high.
- `relevance_confidence`: 0.92. The entry is directly relevant to Pulgar/Arriagada research and directly relevant as negative evidence against Dario attachment.
- `canonical_readiness`: hold_for_conversion_qa.

## Next Action

Run targeted conversion QA for the source image and conversion set. Reconcile or supersede the converted Markdown row for entry 172, and explicitly record whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form such as `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical promotion.
