---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-515-registration-date.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-515-registration-date.md
reviewer: postconv-proof-review-20260522185919905
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: Entry 515 Registration Date

## Blockers

- Canonical readiness is `hold` because the staged draft and source packet already carry `hold_for_conversion_qa` for entry 515, and related entry-515 reviews document a lower-row crop concern and conversion-version conflicts.
- The chunk path named in the staged draft and source packet, `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md`, is unavailable at that exact path. The workspace contains related same-source `page-0001-chunk-01.md` chunks instead, so this is a conversion-control issue.
- Same-source chunk variants materially disagree on entry 515 identity. One available variant gives `Rosa Elvira del Carmen`, while another gives `Neira Ulloa / Laura de la Cruz`; the visible source image only partially supports the entry-515 name area. The registration-date cell is stronger than the identity field, but the staged claim should not be promoted as a personal event for `Rosa Elvira del Carmen` until entry 515 is reconciled.
- The visible source image is cropped at the bottom of entry 515. The registration-date cell is visible near the left edge, but the crop concern remains relevant to row integrity and identity confidence.

## Scores

| source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
|---:|---:|---:|---:|---:|---:|---|---:|---|
| 0.88 | 0.46 | 0.62 | 0.55 | 0.44 | 0.66 | high | 0.88 | hold |

## Evidence Strengths

- The cited source is an original civil birth-register page, a strong source type for the date an entry was registered.
- The staged draft, source packet, converted file, related chunks, and source image all refer to page 172, entry 515 of the 1889 Los Anjeles birth register.
- Direct image review supports the entry-515 registration-date reading as `Julio veinte i tres ...`, corresponding to 23 July 1889.
- The converted file and available same-source chunks agree that the entry-515 registration date is 23 July 1889, even while they disagree on other fields in the row.
- The claim is highly relevant to the cited row because it concerns the `Fecha de la Inscripcion` column for entry 515.

## Review Judgment

The row-level registration date is probably supported: the image and derivative transcriptions agree that entry 515 was registered on 23 July 1889.

The claim is not canonical-ready because it attaches that date to `Rosa Elvira del Carmen` in a conversion context with unresolved entry-515 identity conflicts and an unavailable referenced chunk path. Treat this as a held, moderately probable claim pending conversion QA, not as a rejected registration-date reading.

## Next Action

Keep this claim out of canonical folders. Reconcile entry 515 against a complete lower-row image or formal conversion QA note, then revise or promote the registration-date claim only after the row identity and referenced conversion path are stable.
