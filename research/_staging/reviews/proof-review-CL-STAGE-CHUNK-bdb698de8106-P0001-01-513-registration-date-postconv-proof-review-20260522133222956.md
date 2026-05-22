---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522133222956
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-registration-date.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-registration-date.md
reviewed_at: 2026-05-22T13:33:22Z
decision: hold_for_conversion_qa
canonical_readiness: not_ready_conversion_conflict
source_quality_score: 0.92
conversion_confidence_score: 0.45
evidence_quantity_score: 0.66
agreement_score: 0.62
identity_confidence_score: 0.80
claim_probability: 0.92
relevance_level: direct
relevance_confidence: 0.97
next_action: reconcile_stale_chunk_reference_and_conversion_conflicts_before_canonical_promotion
---

# Proof Review: Entry 513 Registration Date

## Blockers

- The staged draft references chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, but that exact file is unavailable in the workspace. A nearby chunk exists as `page-0172-chunk-01.md`, and another derivative chunk exists under the `-codex` chunk folder, but the assigned staged reference is stale or incorrect.
- The source packet explicitly recommends `hold_for_conversion_qa` because the assigned converted/chunk transcript materially conflicts with visible source-image readings for names, relationships, witnesses, streets, official signature, and record completeness. This date claim should not be promoted while the entry context is still under conversion reconciliation.
- The date field itself is comparatively stable: the visible image, the assigned converted file, and the available related chunks all support entry 513's registration date as `Julio veinte/veintidos de mil ochocientos ochenta i nueve`, normalized as `1889-07-22`. The blocker is provenance and conversion-context reliability, not the date value.
- Do not use this review to alter the transcript, normalize source spelling beyond the staged date claim, or promote this claim to any canonical folder.

## Scores

| Factor | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.92 | The source is a civil birth register image with a direct registration-date column for entry 513. |
| conversion_confidence_score | 0.45 | The date reading is supported, but the source packet documents broad conversion conflicts and the staged draft's exact chunk path is missing. |
| evidence_quantity_score | 0.66 | One direct source image plus derivative transcription layers support the date; no independent corroborating source was reviewed. |
| agreement_score | 0.62 | The date value agrees across the visible image, converted file, and available related chunks, but the surrounding entry transcription and assigned chunk reference do not fully agree. |
| identity_confidence_score | 0.80 | The claim subject is only `entry 513`, and the row number is visible; canonical person identity remains risky because surrounding name and relationship fields are under QA dispute. |
| claim_probability | 0.92 | High probability that entry 513 was registered on 22 July 1889. The visible date column reads `Julio ... veintidos ... de mil ochocientos ochenta i nueve`, and the derivative text preserves the same date. |
| relevance_level | direct | The registration-date column directly records the date of registration for the entry. |
| relevance_confidence | 0.97 | The field, row number, and date relationship are clear even though other fields require conversion QA. |
| canonical_readiness | not_ready_conversion_conflict | Hold for conversion QA; do not promote until the stale chunk reference and source-image/derivative conflicts are reconciled. |

## Evidence Strengths

- The staged draft quotes `Julio veintidos de mil ochocientos ochenta i nueve`, directly matching the registration-date field asserted for entry 513.
- The converted file transcribes entry 513's `Fecha de la Inscripcion` as `Julio / veintidos / de mil ochocientos ochenta / i nueve`.
- The visible source image shows entry number `513` with the registration-date column beginning `Julio`, continuing `veintidos`, and ending `de mil ochocientos ochenta i nueve`.
- The source type is a primary civil birth register page, so a registration-date claim for an entry does not require a relationship inference.

## Review Judgment

This staged claim has strong direct support for the normalized registration date `1889-07-22`, but it is not canonically ready. The assigned chunk path is unavailable, and the source packet documents material conflicts between the derivative transcription and visible image evidence for the same page.

Treat the registration date as likely correct at the staged-evidence level, while keeping the claim on hold until conversion QA reconciles the chunk reference and entry 513 transcription context.

## Next Action

Repair or formally supersede the stale chunk reference, then run targeted conversion QA for entry 513 against the source image. Re-review the claim after the conversion layer is stable before any canonical promotion.
