---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260528133117335"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224813411.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224813411.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.90
conversion_confidence_score: 0.40
evidence_quantity_score: 0.70
agreement_score: 0.52
identity_confidence_score: 0.58
claim_probability: 0.64
relevance_level: high
relevance_confidence: 0.95
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224813411.md`.

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The assigned chunk/source packet and current converted Markdown do not describe the same entry 172 row.
2. The disagreement changes the child, parent set, birth date, birthplace, and informant. This is not a same-person question or a normal spelling/name-variant conflict.
3. The source image view supports the Pulgar/Arriagada row at page 58 entry 172, but this review is not a conversion-repair task and does not modify the converted Markdown.
4. The father field should not be silently normalized. The visible row supports `Jose del Carmen Pulgar` with an unresolved trailing mark or suffix, so targeted QA must decide whether the source supports `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain reading.
5. No child identity, parent identity, parent-child relationship, parent merge, Dario-line bridge, or canonical wiki update is ready from this draft while row control remains unresolved.

## Evidence Strengths

- The underlying source is a civil birth-register image, a strong primary source type for birth and parent facts once the row is controlled.
- The assigned chunk and source packet consistently read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with parents `Jose del Carmen Pulgar ...` and `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The page image is consistent with the Pulgar/Arriagada row in the entry 172 position on page 58.
- The staged identity analysis correctly treats the Burgos/de la Cruz converted-file reading as a row-control conflict rather than proof of an alternate identity or relationship.

## Scoring

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth-register image is a high-quality primary source for the event class. |
| conversion_confidence_score | 0.40 | The chunk/source packet align with the image, but the current converted Markdown gives a different row. |
| evidence_quantity_score | 0.70 | Source image, source packet, assigned chunk, converted Markdown, conflict draft, and staged analysis were available; all derive from one underlying source. |
| agreement_score | 0.52 | Image, chunk, and source packet favor Pulgar/Arriagada, while converted Markdown conflicts materially. |
| identity_confidence_score | 0.58 | Moderate for identifying the visible Pulgar/Arriagada row; low for attaching canonical persons before QA. |
| claim_probability | 0.64 | The staged draft's hold-for-QA conclusion is well supported; individual identity/relationship claims remain unready. |
| relevance_level | high | The row controls family identity, parentage, and anti-conflation handling. |
| relevance_confidence | 0.95 | The evidence directly concerns the assigned staged draft and entry 172. |
| canonical_readiness | hold_for_conversion_qa | Hold until targeted QA reconciles the conversion and certifies the father field. |

## Claim Probability Notes

- Probability that the staged draft correctly identifies a row-level conversion-control conflict: 0.86.
- Probability that the Pulgar/Arriagada row is the visible page 58 entry 172 in the source image: 0.74.
- Probability that the Burgos/de la Cruz reading in the current converted Markdown is the correct controlling row for this source image: 0.12.
- Probability that this draft can support immediate canonical identity or relationship promotion: 0.05.
- Probability that this row supports any Dario identity bridge without separate bridge evidence: 0.03.

## Identity And Relationship Risk

The identity risk is high if any canonical claim is promoted before row-control QA. `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` are not plausible variants of one child, and the parent sets are mutually exclusive for a single controlled entry. The Pulgar surname and Arriagada context do not prove a connection to any Dario Pulgar candidate without a separate source-supported bridge.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, source packet, and current converted Markdown. The QA note should explicitly decide the controlling entry 172 row and certify the father field only to the visible source-supported form before any separate proof review of child identity, birth facts, parent attributes, or parent-child relationships.
