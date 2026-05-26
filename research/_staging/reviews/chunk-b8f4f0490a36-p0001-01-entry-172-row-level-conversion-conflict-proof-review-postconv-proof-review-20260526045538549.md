---
type: proof_review
status: reviewed_hold
role: claim_reviewer
worker: postconv-proof-review-20260526045538549
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015729976.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015729976.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: 0.00
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- The staged draft is supported as a conflict diagnosis, but it is not ready for canonical promotion because the current converted Markdown and the assigned chunk give incompatible entry-172 readings.
- The visible source image supports the assigned chunk's Pulgar/Arriagada row for entry 172 on page 58, not the Burgos/de la Cruz row currently recorded in the converted Markdown for entry 172.
- This review must not correct the converted Markdown, chunk, source packet, or wiki pages. A targeted conversion QA worker should reconcile the derivative transcription files against the source image.
- No child identity, birth fact, parent-child relationship, same-person merge, or Dario-line bridge should be promoted from this staged draft while the derivative source control conflict remains unresolved.
- The father field is visibly consistent with `Jose del Carmen Pulgar` plus a terminal mark or abbreviation, but this proof review does not certify whether that terminal reading is `S.`, another mark, or uncertain notation.

## Scored Judgment

| Field | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.92 | Civil birth register image is a direct record image with entry number, date, child, parents, and informant visible. |
| conversion_confidence_score | 0.35 | The assigned chunk matches the source image for entry 172, but the current converted Markdown gives a different row for the same entry number. |
| evidence_quantity_score | 0.55 | One direct source image plus two derivative readings; enough to diagnose the conflict, not enough to resolve downstream identity bridges. |
| agreement_score | 0.45 | Source image, chunk, and source packet agree on the Pulgar/Arriagada row; current converted Markdown materially disagrees. |
| identity_confidence_score | 0.78 | The source image supports a distinct Pulgar/Arriagada child in entry 172, but canonical identity work must wait for conversion QA. |
| claim_probability | 0.95 | The staged draft's central claim, that entry 172 has a row-level conversion conflict requiring hold, is strongly supported. |
| relevance_level | high | The visible row names Pulgar and Arriagada and is directly relevant to the Pulgar/Arriagada family cluster. |
| relevance_confidence | 0.98 | Family relevance is explicit in the visible names and the assigned chunk. |
| canonical_readiness | 0.00 | Canonical promotion is blocked until conversion QA reconciles the converted Markdown and chunk. |

## Evidence Strengths

- The source image visibly shows entry `172` on page 58 with child name consistent with `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registration date `Siete de Abril`, birth date `Ocho de Marzo`, birthplace `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The assigned chunk preserves the same Pulgar/Arriagada row and supplies a coherent set of related fields for entry 172.
- The source packet correctly identifies the current converted Markdown conflict and recommends `hold_for_conversion_qa`.
- The identity-analysis draft properly separates the Pulgar/Arriagada reading from the Burgos/de la Cruz reading and correctly blocks Dario-line attachment from this record.

## Review Findings

- Literal support: The draft's statement that the chunk/source-packet reading conflicts with the current converted Markdown is supported. The source image further supports that the chunk's entry-172 row is the visible row for this source image.
- Source reliability: High for direct civil registration evidence, but the derivative conversion layer is unreliable for this row until reconciled.
- Conversion confidence: Mixed. The chunk is visually plausible and substantially supported; the current converted Markdown appears misaligned for this source image.
- Claim confidence: High for the hold/conflict recommendation; moderate for any specific normalized parent or child identity claim until conversion QA certifies the exact transcription.
- Identity risk: High if promoted now, because the same entry number is attached to two incompatible child-parent clusters in derivative files.
- Relationship jumps: No parent-child relationship should be promoted yet. The record may support Jose del Carmen Pulgar and Juana Arriagada de Pulgar as parents only after row-control QA.
- Dario relevance: This record does not name Dario, Dario Arturo, Dario Jose, Pulgar-Smith, Alexander John Heinz, spouse, child, or grandchild. Any Dario-line bridge has probability `0.00` from this source alone.
- Conflict handling: The staged draft's `hold_for_conversion_qa` recommendation is the correct canonical posture.

## Next Action

Targeted conversion QA should reconcile the source image, converted Markdown, assigned chunk, and source packet for entry 172. That QA should certify the controlling row and father-field reading only to the visible extent, then return the corrected derivative source for a new proof review before any canonical claim or relationship promotion.
