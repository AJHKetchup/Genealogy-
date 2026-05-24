---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260524141725293
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
review_status: hold
canonical_readiness: hold
reviewed:
  - research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.86
conversion_confidence_score: 0.38
evidence_quantity_score: 0.64
agreement_score: 0.46
identity_confidence_score: 0.80
claim_probability: 0.82
relevance_level: critical
relevance_confidence: 0.98
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- Canonical readiness is `hold`. The staged draft is supportable as an identity-conflict analysis, but not as a promotion-ready claim source, because the assigned converted Markdown transcribes entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, and mother `Rosario de la Cruz de la Maza`, while the chunk, source packet, and visible source image support a Pulgar/Arriagada row.
- The conversion conflict is material. The reviewed files disagree on child name, parents, birth date, birth place, residence, informant, and broader row context. No person identity, birth fact, parent-child relationship, or family relationship should be promoted from this staged draft until conversion QA reconciles or supersedes the conflicting converted Markdown.
- The father-name suffix remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, while the image/source-packet discussion preserves uncertainty around whether the source visibly supports a final suffix. Keep `Jose del Carmen Pulgar` and `Jose del Carmen Pulgar S.` as transcription hypotheses until targeted QA resolves the field.
- The record does not name Dario. The staged draft correctly warns against merging the child, father, or mother into any Dario Pulgar identity by surname or family context alone.

## Evidence Strengths

- The source class is strong: a civil birth registration image for Los Angeles/La Laja, 1888, page 58, entry 172.
- The source image visibly supports entry 172 as a Pulgar/Arriagada birth row. It is materially consistent with the chunk and source packet for `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The staged draft handles uncertainty appropriately. It treats the Gomez/de la Cruz converted Markdown as a row-level conflict, preserves the unresolved father suffix, and recommends `hold_for_conversion_qa` instead of silently promoting the chunk reading.
- Relationship-jump risk is explicitly controlled. The draft does not assert that this entry proves a Dario identity or a broader Pulgar lineage connection.

## Scores

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Direct civil registration image; relevant row is visible, though handwriting and row density require careful QA. |
| conversion_confidence_score | 0.38 | The chunk aligns with the image, but the assigned converted Markdown carries a materially different entry 172. |
| evidence_quantity_score | 0.64 | One direct image, one chunk, one source packet, and one conflicting converted file were reviewed; no independent corroborating source was reviewed. |
| agreement_score | 0.46 | Image, chunk, source packet, and staged analysis mostly agree, but the controlling converted Markdown sharply disagrees. |
| identity_confidence_score | 0.80 | High that the visible entry belongs to the Pulgar/Arriagada cluster; reduced by the unresolved derivative conflict and father suffix. |
| claim_probability | 0.82 | The staged draft is probably correct as a conflict/hold analysis, not as canonical proof. |
| relevance_level | critical | The conflict controls whether child identity and parent-child relationships can safely proceed. |
| relevance_confidence | 0.98 | All reviewed materials point to the assigned entry 172/source image and the same staged draft. |
| canonical_readiness | hold | Requires conversion QA correction or supersession before canonical use. |

## Judgment

Hold the staged draft for conversion QA. The Pulgar/Arriagada identity cluster has direct support from the page image and the current chunk, but the assigned converted Markdown is inconsistent enough to block canonical promotion. The staged draft's uncertainty handling and Dario guardrail are appropriate.

## Next Action

Run targeted conversion QA on entry 172 against the source image and update or supersede the assigned converted Markdown. QA should decide the controlling row identity, document whether the father field includes a final suffix, and preserve source-visible spelling for residence and names. After that, rerun proof review for the child identity, birth-event facts, father claim, mother claim, and parent-child relationships before any canonical promotion.
