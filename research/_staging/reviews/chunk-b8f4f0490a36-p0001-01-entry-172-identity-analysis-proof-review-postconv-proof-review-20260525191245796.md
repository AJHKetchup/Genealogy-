---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525191245796
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
reviewed_sources:
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

- Canonical readiness remains `hold_for_conversion_qa`. The staged identity analysis correctly treats this as a row-level conversion or assignment conflict, not a promotable person, relationship, or name-variant conclusion.
- The assigned converted Markdown and the assigned chunk do not agree for entry 172. The converted Markdown gives a different child, parents, date/place details, and informant from the chunk and source packet.
- The source image visually supports the chunk-side Pulgar/Arriagada row for entry 172, but this proof-review note should not rewrite the converted file or promote a corrected transcription. A targeted conversion QA/correction note is still needed to reconcile the canonical converted Markdown, chunk, and source packet.
- The father field ending after `Pulgar` remains a literal-reading uncertainty. Keep the alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` open until conversion QA certifies the source-visible reading.
- No Dario-line identity bridge is supported by this item. The staged draft correctly rejects jumps to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada from this entry alone.

## Evidence Strengths

- The source type is a civil birth registration, which is strong direct evidence for a birth event when the row is securely transcribed.
- The chunk and source packet agree that entry 172 is a Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, with father recorded as `Jose del Carmen Pulgar S.` and mother as `Juana Arriagada de Pulgar`.
- The reviewed page image aligns with the chunk's row placement and Pulgar/Arriagada identity cluster for entry 172, increasing confidence that the staged analysis is identifying a real conversion conflict rather than inventing one.
- The staged analysis preserves uncertainty and avoids promoting parent-child relationships, parent merges, or Dario-line comparisons.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration is high-quality original evidence in principle; image visibility is usable for row-level confirmation. |
| conversion_confidence_score | 0.38 | The chunk/source-packet reading is stronger than the converted-file reading for this assignment, but the official converted Markdown remains materially inconsistent. |
| evidence_quantity_score | 0.55 | One directly relevant source image plus conflicting derivative layers; enough to identify the problem, not enough for canonical promotion. |
| agreement_score | 0.42 | Chunk, source packet, conflict draft, and image broadly agree; converted Markdown sharply disagrees. |
| identity_confidence_score | 0.66 | Moderate confidence for the Pulgar/Arriagada row as a source-visible identity cluster, reduced by unresolved conversion state and father-name ending. |
| claim_probability | 0.72 | The staged draft's probability for the Pulgar/Arriagada row is reasonable pending QA. |
| relevance_level | 0.90 | Highly relevant to Pulgar/Arriagada parent-candidate work if the row is formally reconciled. |
| relevance_confidence | 0.86 | The row contains Pulgar and Arriagada names and direct parent-child birth-registration details. |
| canonical_readiness | 0.10 | Hold; do not promote until conversion QA resolves the conflicting derivative transcript and father-field reading. |

## Review Judgment

The staged identity analysis is supported as a conflict analysis and should remain in staging. Its main conclusion is sound: the entry should not be used for canonical identity, claim, relationship, or merge work until targeted conversion QA reconciles the converted Markdown with the chunk/source image.

The draft slightly understates that the source image itself appears to support the chunk-side Pulgar/Arriagada row, but that does not remove the blocker because the assigned converted Markdown is still inconsistent and should be corrected or superseded through the conversion QA process rather than by proof review.

## Next Action

Create or route to targeted conversion QA for the assigned converted Markdown, chunk, source packet, and source image. The QA output should explicitly decide the controlling entry 172 transcription and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical promotion.
