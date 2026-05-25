---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525165723772
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.82
conversion_confidence_score: 0.42
evidence_quantity_score: 0.62
agreement_score: 0.58
identity_confidence_score: 0.64
claim_probability: 0.66
relevance_level: high
relevance_confidence: 0.92
---

# Proof Review: Entry 172 Identity/Conflict Analysis

## Blockers First

1. The staged identity analysis is correct to hold this item because the referenced converted Markdown and the current chunk/source-packet layer assign different families to entry 172.
2. The visible source image, current chunk, and source packet support an entry-172 Pulgar/Arriagada row, but the converted Markdown records a different Jose Francisco/Gomez/de la Cruz cluster. This is a row-level conversion or assignment conflict, not a spelling issue.
3. The father field remains transcription-sensitive. The visible row appears consistent with `Jose del Carmen Pulgar`, with an ending/mark after Pulgar that should not be normalized beyond the reviewed forms `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` without targeted QA.
4. No Dario, Arturo, Smith, Geneva, passenger, occupation, spouse, child, or later-life identity bridge is present in the reviewed source context. Any Dario-line attachment must remain unsupported by this entry.
5. Canonical promotion is not ready. Parent-child relationships, same-person merges, and Pulgar/Juana candidate merges must wait for conversion QA and a later claim-level proof review.

## Evidence Strengths

- The source class is strong: a civil birth register with a visible entry number, date, child field, parent fields, compareciente field, and official signature area.
- The source image visibly supports the broad Pulgar/Arriagada row assignment for entry 172 on page 58: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar...`, mother `Juana Arriagada de Pulgar`, and compareciente `Ernesto Herrera L.`.
- The current chunk and source packet agree with the visible source at the row-identity level and preserve the father-ending uncertainty.
- The staged draft appropriately separates the row-level conversion conflict from identity conclusions and correctly treats existing canonical pages as non-independent if they depend on this disputed entry.
- The staged draft appropriately rejects Dario-line attachment from this entry alone.

## Scored Judgment

| Metric | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration is a high-value source class, and the relevant entry is visible, though handwriting and image contrast reduce field-level certainty. |
| conversion_confidence_score | 0.42 | The source image/current chunk support the Pulgar row, but the referenced converted Markdown conflicts substantially. |
| evidence_quantity_score | 0.62 | One primary source image plus derivative chunk/source packet support the assessment; no independent corroborating source was reviewed or needed for this hold decision. |
| agreement_score | 0.58 | Image, chunk, source packet, and conflict note broadly agree on Pulgar/Arriagada; converted Markdown disagrees on names, dates, places, parents, and informant. |
| identity_confidence_score | 0.64 | Pulgar/Arriagada is the better-supported row identity under reviewed evidence, but confidence is capped by the derivative conflict and father-ending uncertainty. |
| claim_probability | 0.66 | Probability that the underlying row is the Pulgar/Arriagada birth registration, not yet a promotable claim. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child candidates. |
| relevance_confidence | 0.92 | Relevance is high if the Pulgar row is certified; Dario-line relevance is not supported by this source. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims or relationships until conversion QA certifies the controlling row and exact father-field reading. |

## Claim Review

The staged draft's main conclusion is supported: this item should remain `hold_for_conversion_qa`. The draft's blockers, conflict severity, Pulgar/Arriagada probability cap, and anti-conflation warning are consistent with the reviewed evidence.

The draft slightly overstates certainty only if read as final proof of the Pulgar/Arriagada row. As a conflict analysis, however, it keeps the correct boundary: it treats Pulgar/Arriagada as the stronger hypothesis while withholding canonical promotion.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, the current chunk, and the converted Markdown. The QA note should certify the controlling entry-172 row and record the father field exactly, including whether the visible ending after Pulgar is an `S.`, another mark, or unresolved.

After QA, proof-review the certified row-level claims before any promotion: child name, sex, registration date, birth date/time, birth place, father candidate, mother candidate, residence, informant, and parent-child relationships.
