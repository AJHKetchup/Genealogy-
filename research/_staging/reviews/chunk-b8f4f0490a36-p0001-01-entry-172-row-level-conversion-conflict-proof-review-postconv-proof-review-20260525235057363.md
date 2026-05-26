---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525235057363
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
reviewed_sources:
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-25
canonical_readiness: hold_for_conversion_control_correction
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. **Converted-file control conflict:** the assigned converted Markdown does not match the visible source image for this task's entry 172. It transcribes a different family, including `José Miguel`, `Oswaldo Burgos`, and `Concepcion de la Cruz`, while the visible source image and assigned chunk show `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
2. **Canonical promotion blocker:** no claim should be promoted from the converted Markdown until the conversion-control mismatch is corrected or superseded by QA. The chunk/source packet/source image support the Pulgar row, but the canonical conversion artifact is materially inconsistent.
3. **Father-name precision blocker:** the father can be reviewed only to the visible extent. The image supports `Jose del Carmen Pulgar` with a following mark/initial that is plausibly `S.`, but that final element should remain uncertain unless QA certifies it.
4. **Identity-bridge blocker:** this record names no Dario/Dario Arturo/Dario Jose person. It is not direct evidence for a Dario identity merge or Pulgar-Smith bridge.

## Evidence Strengths

- The source image visibly places entry `172` on page 58 and shows the child name as `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`.
- The source image supports the registration date as 7 April 1888 and the birth date as 8 March 1888, with place `Calle de Valdivia`.
- The source image supports the parents as `Jose del Carmen Pulgar` with an uncertain final `S.`/mark and `Juana Arriagada de Pulgar`.
- The source image supports the compareciente as `Ernesto Herrera L.`, present at the birth, age 26, employed, domiciled at `Calle de Valdivia`.
- The assigned chunk and source packet agree with the visible source image on the Pulgar/Arriagada row-level reading.
- The staged identity analysis correctly treats the Burgos/de la Cruz and Pulgar/Arriagada readings as a row-control conflict, not as a same-person variant.

## Scored Judgment

- **source_quality_score:** 0.88
- **conversion_confidence_score:** 0.40 overall; 0.82 for the assigned chunk against the image; 0.10 for the current converted Markdown as the controlling entry-172 artifact.
- **evidence_quantity_score:** 0.70
- **agreement_score:** 0.55 overall because the chunk/source packet/image agree but the converted Markdown conflicts completely.
- **identity_confidence_score:** 0.78 for the Pulgar/Arriagada row as visible entry 172; 0.05 for any Dario attachment.
- **claim_probability:** 0.82 that visible entry 172 is the Pulgar/Arriagada birth row; 0.45 that the father field should be promoted exactly as `Jose del Carmen Pulgar S.` without further QA; 0.05 that this record directly supports any Dario identity claim.
- **relevance_level:** high for Pulgar/Arriagada family reconstruction; low for Dario identity work.
- **relevance_confidence:** 0.86 for Pulgar/Arriagada relevance; 0.20 for Dario relevance.
- **canonical_readiness:** hold_for_conversion_control_correction.

## Review Determination

The staged draft is substantially supported in its main caution: this is a conversion-control conflict and should not be promoted while the converted Markdown contradicts the chunk and image. The review should be treated as **hold/revise**, not reject. The Pulgar/Arriagada row is visibly present in the source image, but the repository's assigned converted Markdown currently points to an incompatible Burgos/de la Cruz row, so canonical claims must wait for correction or targeted QA.

The draft's Dario caution is also supported. The visible entry contains no Dario name and provides no direct identity bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.

## Next Action

Run targeted conversion QA or correction for the converted Markdown controlling this source. Preserve the Pulgar/Arriagada reading as staged evidence only until the conversion-control mismatch is resolved, and keep the father's final `S.`/mark uncertain unless the visible image is specifically certified.
