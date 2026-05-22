---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-registration-date.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-registration-date.md
reviewer: postconv-proof-review-20260522171504013
review_date: 2026-05-22
canonical_readiness: revise
---

# Proof Review: Entry 513 Registration Date

## Blockers

- Canonical readiness is `revise` because the staged draft assigns the claim to `Tulio Cesar Luis Jose`, but the reviewed conversion/image context does not support that exact subject label. The available derivative transcriptions conflict on entry 513's child-name field, and the source image supports only a provisional row association, not the staged normalized name.
- The referenced chunk path in the staged draft and source packet, `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md`, is unavailable at that exact path. Related chunks for the same source exist under `page-0001-chunk-01.md`, but this review treats the missing referenced chunk as a conversion-control issue.
- The registration-date cell itself is supported for entry 513, but the claim should not be promoted as a personal event for `Tulio Cesar Luis Jose` until the entry 513 child identity is reconciled through conversion QA.

## Scores

| source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
|---:|---:|---:|---:|---:|---:|---|---:|---|
| 0.88 | 0.58 | 0.74 | 0.62 | 0.34 | 0.64 | medium | 0.61 | revise |

## Evidence Strengths

- The source is an original civil birth-register page, a strong source type for the narrow fact of the registration date recorded in a register row.
- The staged draft and source packet both point to page 172, entry 513, and the source image visibly shows row number `513` aligned with the registration-date column.
- Direct image review supports the registration-date reading for entry 513 as `Julio veinte i dos de mil ochocientos ochenta i nueve`, i.e. 22 July 1889.
- The converted Markdown and available related chunks also support 22 July 1889 as the entry 513 registration date, despite disagreeing on other fields in the same row.

## Review Judgment

The date portion of the claim is likely supported for register entry 513: the image and derivative transcriptions agree that entry 513 was registered on 22 July 1889.

The staged claim is not canonical-ready because it attaches that date to `Tulio Cesar Luis Jose`. The reviewed image and derivative evidence do not establish that subject label, and related conversion notes show unresolved conflict in entry 513's child-name field. This should be revised to a row-level or provisional-subject claim after conversion QA, rather than promoted as a claim about the named person.

## Next Action

Revise or hold the staged draft pending entry 513 identity reconciliation. A safe next draft would preserve the confirmed date as an entry-level registration-date fact for entry 513 while keeping the child name provisional until the visible source itself supports a final reading.
