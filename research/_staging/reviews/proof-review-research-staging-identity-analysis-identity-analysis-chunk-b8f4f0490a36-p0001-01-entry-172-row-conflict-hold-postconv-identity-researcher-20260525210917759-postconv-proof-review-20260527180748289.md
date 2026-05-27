---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527180748289
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210917759.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210917759.md"
reviewed_files:
  - "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210917759.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_image_attempted: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_image_available_for_review: false
source_quality_score: 0.82
conversion_confidence_score: 0.30
evidence_quantity_score: 0.55
agreement_score: 0.20
identity_confidence_score: 0.38
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict Hold

## Blockers

- The staged draft is correctly not promotion-ready. The assigned chunk and source packet identify entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown identifies entry 172 as a Burgos/de la Cruz birth row. These are incompatible whole-row readings, not minor spelling variants.
- The referenced source image path was not available at the exact filename during this review, so I could not independently certify the visible manuscript row. This review is limited to the staged draft, conflict draft, source packet, chunk, and converted Markdown.
- The father field in the Pulgar/Arriagada reading remains uncertified. The review cannot choose between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` without targeted image QA.
- The draft's Dario-line caution is supported: none of the reviewed evidence names Dario, Darío, Arturo, Smith, Dario Jose, or Dario Arturo Pulgar-Smith.
- No canonical claim, relationship, merge, or wiki update should be made from this staged draft until row-control QA resolves which entry-172 transcription controls.

## Evidence Strengths

- The staged draft accurately represents the conflict between the assigned chunk/source packet and the current converted Markdown.
- The chunk and source packet agree internally on the Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, and informant `Ernesto Herrera L.`
- The converted Markdown clearly preserves the opposing Burgos/de la Cruz reading: child `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth date `El seis de Abril de mil ochocientos ochenta i ocho`, and informant `Oswaldo Burgos`.
- Because the conflict is explicit and material, the staged draft's hold recommendation is the most defensible review outcome.

## Scoring

| category | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registration is a strong source type for birth and parent fields, but the image was unavailable for this review. |
| conversion_confidence_score | 0.30 | Two derivative transcriptions disagree on the whole row and material identity fields. |
| evidence_quantity_score | 0.55 | There is one source event with multiple derivative references, but no independent confirming source reviewed here. |
| agreement_score | 0.20 | The chunk/source packet agree with each other, but they conflict sharply with the converted Markdown. |
| identity_confidence_score | 0.38 | Identity cannot be certified until the controlling row is confirmed. |
| claim_probability | 0.62 | The claim that the staged item should remain held for conversion QA is likely; the underlying Pulgar identity claim is not promotion-ready. |
| relevance_level | high | If the Pulgar row is confirmed, it is directly relevant to Pulgar/Arriagada family reconstruction. |
| relevance_confidence | 0.85 | The reviewed staged materials consistently flag Pulgar and Arriagada relevance, while excluding Dario-line proof from this record. |
| canonical_readiness | hold_for_conversion_qa | The row-level conflict blocks canonical use. |

## Claim Probability By Proposed Use

| proposed use | probability | readiness |
| --- | ---: | --- |
| Keep this staged draft on hold for conversion QA. | 0.92 | ready as review disposition |
| Treat entry 172 as the Pulgar/Arriagada birth row. | 0.62 | hold |
| Treat entry 172 as the Burgos/de la Cruz birth row. | 0.28 | hold |
| Promote `Juana Arriagada de Pulgar` as mother from this entry. | 0.58 | hold |
| Merge or equate the father with canonical `Jose del Carmen Pulgar`. | 0.20 | not ready |
| Use this entry as evidence for any Dario/Darío Pulgar identity. | 0.02 | blocked |

## Next Action

Run targeted conversion QA for page 58, entry 172 using the source image and the two conflicting derivative readings. QA should decide the controlling row and certify the father-field reading before this item is rerun through proof review.
