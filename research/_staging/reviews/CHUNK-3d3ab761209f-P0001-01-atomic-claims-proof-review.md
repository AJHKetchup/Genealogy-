---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/CHUNK-3d3ab761209f-P0001-01-atomic-claims.md
staged_draft: research/_staging/claims/CHUNK-3d3ab761209f-P0001-01-atomic-claims.md
reviewer: postconv-proof-review-20260522025927189
review_date: 2026-05-22
canonical_readiness: revise
---

# Proof Review: CHUNK-3d3ab761209f-P0001-01 Atomic Claims

## Blockers

- Revise before canonical promotion: the staged draft cites `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, but that exact referenced chunk file is unavailable. The same directory contains `page-0172-chunk-01.md`, which carries a different chunk id and different facts.
- Revise before canonical promotion: the referenced converted file `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`, the conversion job page Markdown, and the restored page image do not support many core staged claims.
- Do not promote the staged child-name and birth-event claims for entries 513-515 as written. The available conversion/page image conflict with the staged draft on principal names, birth dates/times, places, and some parent facts.
- Do not promote the record 514 negative-father claim ca514-005. The referenced conversion and visible image support a named father field, not `Se ignora`.
- Do not promote image-sensitive claims ca514-004, ca514-007, ca514-010, ca514-011, ca515-011, and ca515-012 from this staged draft. The visible source does not support `Calle Sanegueso`, `Benjamin Utiera`, `Ignacio Soto`, or the staged record 515 witness/emendation set as written.
- A separate chunk file at `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md` carries `chunk_id: CHUNK-3d3ab761209f-P0001-01` and matches the staged draft more closely, but it conflicts with the referenced converted file and restored page image. Treat it as a provenance conflict, not as sufficient support for canonical promotion.

## Scores

- source_quality_score: 0.86
- conversion_confidence_score: 0.42
- evidence_quantity_score: 0.70
- agreement_score: 0.28
- identity_confidence_score: 0.38
- claim_probability: 0.36
- relevance_level: high
- relevance_confidence: 0.90
- canonical_readiness: revise

## Claim Review

| Claim id(s) | Judgment | Claim probability | Notes |
| --- | --- | ---: | --- |
| ca513-001 | revise | 0.35 | The staged name `Jose Luis Pulgar Amagada` is not supported by the referenced converted file. The restored image does support a Pulgar child entry, but the given names and surname reading need a fresh transcription decision. |
| ca513-002 | supported_limited | 0.86 | Entry 513 registration date of 22 July 1889 is supported by the referenced conversion and image. |
| ca513-003 | revise | 0.30 | The staged birth date/time, 26 June 1889 at 4:30 p.m., conflicts with the referenced conversion and visible image, which support a different June date/time reading. |
| ca513-004 through ca513-010 | mixed_revise | 0.58 | Calle Colon, Jose del Carmen Pulgar, Juana de Dios Amagada de Pulgar, and Jose del C. Pulgar are broadly visible/supported, but the staged mother occupation wording and some same-entry identity uses should be revised against the supported conversion/image before promotion. |
| ca513-011 | supported_low_genealogical_value | 0.80 | The compareciente identity note is supported as a source note, not as a substantive genealogical claim. |
| ca514-001 through ca514-004 | revise | 0.28 | The staged Riquelme Aviles/Sanegueso claims conflict with the referenced conversion and page image, which show different name/place readings. |
| ca514-005 | not_supported | 0.08 | The staged `Se ignora` father claim is not supported by the referenced conversion or restored image. |
| ca514-006 through ca514-010 | revise | 0.34 | Mercedes Riquelme as mother/declarant, age 21, and seamstress are supported, but the staged legal phrase, no-signature phrasing, and Sanegueso domicile conflict with the referenced conversion/image. |
| ca514-011 | not_supported_as_written | 0.20 | The restored image and referenced conversion support different witness readings than `Benjamin Utiera` and `Ignacio Soto`. |
| ca515-001 through ca515-010 | revise | 0.30 | The staged Neira Ulloa/Laura de la Cruz claims conflict with the referenced conversion and restored image, which support different principal names, birth date/time/place, parents, occupations, and declarant details. |
| ca515-011 | not_supported_as_written | 0.20 | The staged witness names are not supported by the referenced conversion/page image. |
| ca515-012 | not_supported_as_written | 0.22 | The staged `Neira=emendado=vale=` note is not supported as written by the referenced conversion/page image for the displayed record 515. |

## Evidence Strengths

- The source itself is a civil birth register page, which is a strong source type for birth-registration facts when the transcription is stable.
- The restored page image is now available at `raw/codex-conversion-jobs/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513/page-images/page-0001.png`, so the earlier image-availability blocker is resolved.
- A few staged details have partial support in the visible source, especially entry 513's registration date, Calle Colon, Jose del Carmen/Jose del C. Pulgar, Juana de Dios Amagada de Pulgar, and entry 514's Mercedes Riquelme age/occupation/declarant role.

## Review Judgment

The staged atomic-claims draft is relevant to the cited source, but it is not canonically ready. The main problem is not a narrow handwriting uncertainty; it is a provenance and agreement failure among the staged draft, its cited chunk path, the referenced converted file, the conversion job page Markdown, and the restored source image.

canonical_readiness: revise

## Next Action

Revise the staged draft from the restored page image and the authoritative converted/page Markdown, or repair the provenance chain if a different image/transcription was intended. After that, rerun claim extraction/review rather than promoting selected claims from this draft.
