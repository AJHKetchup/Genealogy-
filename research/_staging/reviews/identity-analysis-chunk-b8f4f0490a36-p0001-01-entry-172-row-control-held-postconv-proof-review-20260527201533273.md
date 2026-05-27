---
type: proof_review
status: complete
role: claim_reviewer
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md"
reviewer: "postconv-proof-review-20260527201533273"
review_date: "2026-05-27"
canonical_readiness: "hold_for_conversion_qa"
source_quality_score: 0.78
conversion_confidence_score: 0.35
evidence_quantity_score: 0.55
agreement_score: 0.25
identity_confidence_score: 0.45
claim_probability: 0.55
relevance_level: "high"
relevance_confidence: 0.70
---

# Proof Review: Entry 172 Row-Control Conflict

Review of staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md`.

## Blockers

- The same source is represented by two conflicting conversion layers. The converted file `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` records entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the referenced chunk `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md` records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The primary source image path recorded in the draft and source packet, `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, is not present in this workspace. The manifest also points to `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`, but that page image is also absent. This reviewer therefore cannot independently certify the visible row from the image.
- The source packet states that direct image review supports the Pulgar/Arriagada row, but that assertion cannot be rechecked here because the source image is unavailable. Treat it as useful review context, not as newly verified transcription.
- The father suffix after `Pulgar` remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, while the staged draft correctly avoids certifying the suffix beyond `Jose del Carmen Pulgar` plus an uncertain trailing mark.
- No identity bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada is supported by the reviewed materials. Any Dario-line merge or relationship inference remains blocked.

## Evidence Strengths

- The draft accurately reports a material row-control conflict and does not over-promote the Pulgar/Arriagada reading into canonical claims.
- The referenced chunk and source packet agree on the Pulgar/Arriagada row for entry 172, including registration date, child name, male sex, birth date and place, named parents, and declarant context.
- The converted file is internally available and clearly contradicts the chunk for the same entry number, so the hold recommendation is literally supported even without primary-image verification.
- The source type, if the image is restored and confirmed, would be a strong primary civil birth registration source for the child identity and parent names stated in the row.

## Scored Judgment

- `source_quality_score`: 0.78. Civil birth registration is a strong source class, but local primary-image unavailability prevents full proof review.
- `conversion_confidence_score`: 0.35. Confidence is low because the converted file and chunk materially disagree for the same entry number.
- `evidence_quantity_score`: 0.55. There are multiple derivative references, but only one underlying source and no accessible image for this review.
- `agreement_score`: 0.25. Agreement is poor across conversion products; the chunk and source packet agree with each other, but the converted file conflicts.
- `identity_confidence_score`: 0.45. The Pulgar/Arriagada row is plausible from the chunk/source-packet layer, but not certifiable while row control and image access are unresolved.
- `claim_probability`: 0.55. More likely than not that the staged draft correctly identifies a real conversion conflict, but not high enough to certify the Pulgar row canonically from this review alone.
- `relevance_level`: high. If certified, entry 172 is directly relevant to Pulgar/Arriagada identity and parent-child claims.
- `relevance_confidence`: 0.70. Relevance is clear for the Pulgar/Arriagada line, but depends on row-control certification.
- `canonical_readiness`: hold_for_conversion_qa.

## Next Action

Run targeted conversion QA after restoring or locating the source image/page image. QA should compare the image, converted file, chunk, and source packet; certify whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row; and record the father field only as far as visibly supported. Do not promote child identity, birth facts, parent-child relationships, parent identity merges, or Dario-line comparisons until that QA is complete and a renewed proof review confirms the row.
