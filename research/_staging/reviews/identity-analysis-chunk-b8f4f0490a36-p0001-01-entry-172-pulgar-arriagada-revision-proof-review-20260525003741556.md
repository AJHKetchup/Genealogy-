---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525003741556
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524231550559.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524231550559.md
reviewed_sources:
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524231550559.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.88
conversion_confidence_score: 0.45
evidence_quantity_score: 0.62
agreement_score: 0.42
identity_confidence_score: 0.72
claim_probability: 0.68
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- The staged draft should remain on hold. The source image and current chunk support entry 172 as a Pulgar/Arriagada birth registration, but the assigned converted Markdown contains a materially different entry 172 transcription with a different child, parents, dates, and location. This is a row-level conversion or file-assignment conflict, not a minor reading variant.
- The exact final mark after the father's name is not ready for canonical use. The chunk reads `Jose del Carmen Pulgar S.`, while the image supports the core name `Jose del Carmen Pulgar` but leaves the suffix or final mark uncertain enough to require targeted conversion QA.
- No Dario identity claim is supported by this entry. The staged draft correctly warns against attaching this record to any Dario candidate by surname or family context alone.

## Evidence Strengths

- The visible source image supports the controlling row as entry 172 on page 58 and shows a child named Jose del Carmen Segundo Pulgar Arriagada, male, with registration date 7 April 1888 and birth date 8 March 1888.
- The image and chunk agree on the mother as Juana Arriagada de Pulgar and the informant as Ernesto Herrera L., present at the birth.
- The record is a civil birth registration, so the source type is strong for a child's birth identity and named parent-child relationships once the conversion conflict is resolved.

## Scored Judgment

- `source_quality_score`: 0.88. Civil registration image is a strong original-type source, though handwriting and image quality leave some narrow uncertainty.
- `conversion_confidence_score`: 0.45. The current chunk matches the image for the Pulgar/Arriagada row, but the assigned converted Markdown conflicts materially with both.
- `evidence_quantity_score`: 0.62. One direct source supports the identity cluster; no independent corroborating source was reviewed for this task.
- `agreement_score`: 0.42. Image and chunk agree, but the converted Markdown disagrees at the row level.
- `identity_confidence_score`: 0.72. The child-parent identity cluster is probably correct for this image row, but not ready for canonical linkage until conversion QA resolves the derivative conflict.
- `claim_probability`: 0.68. The staged draft's hold-and-warning position is well supported; the full positive identity claim should remain provisional.
- `relevance_level`: high.
- `relevance_confidence`: 0.90.
- `canonical_readiness`: hold_for_conversion_qa.

## Next Action

Run targeted conversion QA on the assigned converted Markdown and page image. The QA note should reconcile or supersede the conflicting entry 172 transcription and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form such as `Jose del Carmen Pulgar [?]`. After that, rerun proof review before promoting child identity, birth facts, parent-child relationships, or any Jose/Juana parent-candidate merge.
