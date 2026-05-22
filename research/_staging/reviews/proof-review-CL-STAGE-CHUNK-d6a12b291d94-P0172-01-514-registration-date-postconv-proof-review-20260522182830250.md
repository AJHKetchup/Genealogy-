---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522182830250
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-514-registration-date.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-514-registration-date.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_quality_score: 0.90
conversion_confidence_score: 0.88
evidence_quantity_score: 0.70
agreement_score: 0.55
identity_confidence_score: 0.20
claim_probability: 0.40
relevance_level: medium
relevance_confidence: 0.65
canonical_readiness: hold_for_revision
---

# Proof Review: Entry 514 Registration Date

## Blockers

- The staged draft's subject is `Rigoberto Juan Bautista`, but the reviewed converted page and visible source image for entry 514 do not support that identity. The converted file reads the entry 514 child as `Riquelme Juan Teodoro`; the source image visibly begins `Riquelme` and does not show `Rigoberto Juan Bautista` in the entry 514 name field.
- Because the subject identity is unsupported, the claim as drafted cannot be promoted as a registration date for `Rigoberto Juan Bautista`, even though the date field itself is well supported for entry 514.
- The staged draft's literal-support line preserves only the entry number and registration date, so it does not resolve the identity mismatch.

## Evidence Strengths

- The source is a civil birth register page image for Los Anjeles, Chile, 1889, page 172, containing entries 513-515. This is a strong direct source for registration dates recorded in the table.
- Entry 514's registration-date cell is visible in the source image and reads `Julio veinte i dos de mil ochocientos ochenta i nueve`, equivalent to 22 July 1889.
- The converted file gives the same date for entry 514 as `Julio veintidos de mil ochocientos ochenta i nueve`. The difference between `veinte i dos` and `veintidos` is a normalization/transcription variation and does not materially change the date.
- No relationship inference is required for the date field itself. The issue is identity assignment, not date extraction.

## Scored Judgment

- `source_quality_score`: 0.90. Original register image is available and legible enough for the entry 514 date field.
- `conversion_confidence_score`: 0.88. The converted date agrees with the visible image, with minor spelling normalization.
- `evidence_quantity_score`: 0.70. One direct civil-register source supports the date, but there is no independent corroborating evidence in this review.
- `agreement_score`: 0.55. Agreement is high for the date field but low for the staged subject identity.
- `identity_confidence_score`: 0.20. The named subject in the staged claim is not supported by the reviewed entry.
- `claim_probability`: 0.40. The statement is probable only if reframed as the registration date of entry 514; as drafted for `Rigoberto Juan Bautista`, it is not adequately supported.
- `relevance_level`: medium.
- `relevance_confidence`: 0.65. The evidence is relevant to entry 514's registration date, but relevance to the staged subject is weak.
- `canonical_readiness`: hold_for_revision.

## Next Action

Revise or regenerate the staged claim so the subject matches the visible entry 514 identity before canonical promotion. If a separate source supports `Rigoberto Juan Bautista`, review that source separately rather than transferring this entry 514 date to that person.
