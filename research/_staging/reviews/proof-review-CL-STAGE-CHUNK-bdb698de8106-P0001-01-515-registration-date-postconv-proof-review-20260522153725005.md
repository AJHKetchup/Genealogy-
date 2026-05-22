---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522153725005
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-registration-date.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-registration-date.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: event
subject_claimed: entry 515
predicate_claimed: registration_date
object_claimed: 1889-07-23
source_quality_score: 0.92
conversion_confidence_score: 0.62
evidence_quantity_score: 0.55
agreement_score: 0.78
identity_confidence_score: 0.70
claim_probability: 0.80
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-registration-date

## Blockers

- Canonical readiness is `hold` because the source packet carries an entry-level `hold_for_conversion_qa` recommendation for this page and specifically warns that record 515 is only partially visible in the source image.
- The date field itself is supported, but entry 515 has material name and parent/declarant conflicts between the converted transcript and image-reviewed packet notes. Those conflicts do not directly overturn the registration-date claim, but they block promotion from this conversion layer without QA reconciliation.
- The visible source image shows only the upper portion of entry 515. The registration-date area is available enough for review, but the incomplete row reduces confidence in using the surrounding converted entry as canonical context.

## Evidence Strengths

- The staged claim cites a contemporaneous civil birth-register page, page 172, with entries 513, 514, and 515.
- The staged literal support, `Julio veintitres de mil ochocientos ochenta i nueve`, matches the entry 515 registration-date cell in both the referenced converted file and referenced chunk.
- Direct image review also supports the visible registration-date reading for entry 515 as `Julio veinte i tres`, equivalent to 1889-07-23 in the page's 1889 register context.
- The claim is limited to the registration date for entry 515, so the broader person-name conflicts affect readiness more than the probability of this particular date assertion.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is direct, contemporaneous evidence for a registration-date field.
- `conversion_confidence_score`: 0.62. The date transcription is consistent, but the same converted row has unresolved conflicts for names and relationships.
- `evidence_quantity_score`: 0.55. There is one direct source entry; no independent corroborating source was reviewed for this claim.
- `agreement_score`: 0.78. The staged draft, converted file, chunk, and visible image agree on the date field, while the surrounding entry-level QA conflict lowers the score.
- `identity_confidence_score`: 0.70. The row is identifiable as entry 515, but the incomplete image and conflicting person readings keep identity confidence below high.
- `claim_probability`: 0.80. The exact registration-date claim is probably correct, subject to conversion QA for the partial entry.
- `relevance_level`: high. The source field is directly relevant to entry 515's registration date.
- `relevance_confidence`: 0.90. The claim and source field align closely.
- `canonical_readiness`: hold. Do not promote until conversion QA reconciles record 515 against the source image and confirms that this date belongs to the corrected entry 515 transcription.

## Next Action

Hold for conversion QA. Ask QA to reconcile record 515's partial image visibility and name/declarant conflicts while preserving the currently supported registration-date reading if the corrected row still verifies `Julio veinte/veintitres de mil ochocientos ochenta i nueve`.
