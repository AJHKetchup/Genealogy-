---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528131154111
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
source_quality_score: 0.88
conversion_confidence_score: 0.42
evidence_quantity_score: 0.72
agreement_score: 0.48
identity_confidence_score: 0.50
claim_probability: 0.57
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical promotion remains blocked because the assigned converted Markdown and assigned chunk do not identify the same entry-172 row.
2. The source image and assigned chunk support the Pulgar/Arriagada reading for entry 172, but the current converted Markdown gives a Burgos/de la Cruz reading. This derivative conflict must be resolved by targeted conversion QA before any claim, relationship, identity merge, or Pulgar-to-Dario bridge can be promoted.
3. The father name suffix in the Pulgar/Arriagada row remains a literal-reading issue. It must not be normalized beyond the visible source; acceptable review language is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until QA certifies the reading.
4. The staged draft's Dario comparison is correctly treated as anti-conflation context only. This source does not name Dario, Arturo, Smith, Dario Jose, or any later Pulgar-Arriagada public-role identity.

## Evidence Checked

- Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md`.
- Referenced current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image was visually checked for entry 172.

## Judgment

The staged draft is supported as a conflict/hold analysis. The visible source image shows entry 172 on page 58 as the Pulgar/Arriagada birth row, consistent with the current chunk and source packet. The current converted Markdown instead describes an incompatible Burgos/de la Cruz entry 172, with different child, parents, birth date, birthplace, and informant.

This means the claim under review is not ready for canonical use, even though the conflict diagnosis is well supported. The review should remain a scored hold, not a promotion or rejection of the Pulgar/Arriagada family facts. If later conversion QA certifies the image/chunk reading as controlling, a separate narrow proof review can score the child birth-name, birth date/time, birthplace, father, mother, informant, and parent-child relationships.

## Scores

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong primary source, and the relevant row is visible enough to support the conflict review. |
| conversion_confidence_score | 0.42 | Image/chunk/source packet agree, but the current converted Markdown is materially wrong or misaligned for entry 172. |
| evidence_quantity_score | 0.72 | Draft cites the staged conflict note, packet, chunk, converted file, and source image; enough to assess the row-control conflict. |
| agreement_score | 0.48 | Agreement is strong among image/chunk/source packet, but the converted Markdown directly conflicts. |
| identity_confidence_score | 0.50 | Moderate for identifying the competing row candidates; insufficient for canonical identity attachment. |
| claim_probability | 0.57 | The Pulgar/Arriagada row is probable from the visible image and chunk, but derivative conflict lowers promotable probability. |
| relevance_level | high | The row is directly relevant to Pulgar/Arriagada family review if certified. |
| relevance_confidence | 0.90 | Relevance is clear from the Pulgar and Arriagada names in the source-supported row. |
| canonical_readiness | hold_for_conversion_qa | No canonical claim, relationship, merge, or Dario bridge should be promoted until row-control QA is complete. |

## Evidence Strengths

- The staged draft correctly separates literal source verification from interpretation.
- It correctly treats Reading A and Reading B as incompatible row-control candidates rather than name variants or same-person evidence.
- It correctly blocks relationship jumps to Dario candidates and preserves the father suffix uncertainty.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, current chunk, and source packet. The QA note should identify the controlling entry-172 row and certify the father field only to the visible level before any downstream proof review or canonical promotion.
