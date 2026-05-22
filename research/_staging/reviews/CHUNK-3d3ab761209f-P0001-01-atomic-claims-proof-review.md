---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/CHUNK-3d3ab761209f-P0001-01-atomic-claims.md
staged_draft: research/_staging/claims/CHUNK-3d3ab761209f-P0001-01-atomic-claims.md
reviewer: postconv-proof-review-20260522004058403
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: CHUNK-3d3ab761209f-P0001-01 Atomic Claims

## Blockers

- Raw source image is not available at the path cited by the staged draft and conversion: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`. The `raw/sources` directory currently contains only `.gitkeep`.
- No page-image cache is available in the cited conversion job directory; it contains `page-markdown`, `work-orders`, `manifest.json`, and `README.md`, but no `page-images` directory. Image-only review of handwriting, crop completeness, and marginal/emendation text could not be performed.
- Hold image-sensitive claims pending restored source/page image: ca514-004 (`Calle Sanegueso`), ca514-007 and ca514-010 where that street recurs, ca514-011 (`Benjamin Utiera`), and ca515-012 (`Neira=emendado= vale=`).
- Hold canonical identity merges for named parents/declarants. The same-entry links are plausible, but the draft provides only this register page and no external identity reconciliation for Jose del Carmen/Jose del C. Pulgar, Mercedes Riquelme, Pedro Pablo Neira, Juana de Dios Amagada de Pulgar, or Carmen Ulloa.
- Do not promote the negative-father claim ca514-005 beyond the scope of this registration. The conversion supports that the father field says `Se ignora`, but this is not wider evidence that the father was unknown in all contexts.

## Scores

- source_quality_score: 0.82
- conversion_confidence_score: 0.74
- evidence_quantity_score: 0.78
- agreement_score: 0.96
- identity_confidence_score: 0.64
- claim_probability: 0.80
- relevance_level: high
- relevance_confidence: 0.92
- canonical_readiness: hold

## Claim Review

| Claim id(s) | Judgment | Claim probability | Notes |
| --- | --- | ---: | --- |
| ca513-001 through ca513-008 | supported_from_conversion | 0.86 | The converted file and chunk directly contain entry number, child name/sex, registration date, birth date/time/place, father, mother, nationality, occupation, and domicile facts. Ready for claim drafting after image restoration; identity merges remain separate. |
| ca513-009 and ca513-010 | revise_before_canonical | 0.78 | The conversion supports `Jose del C. Pulgar` as compareciente/father with age, occupation, and domicile. Treat equivalence to `Jose del Carmen Pulgar` as a same-entry inference, not a resolved identity merge. |
| ca513-011 | supported_low_genealogical_value | 0.82 | The conversion supports that the compareciente was known to the officer. This is better as a source note than a canonical genealogical claim. |
| ca514-001 through ca514-003 | supported_from_conversion | 0.86 | The converted file and chunk directly support child name/sex, registration date, and birth date/time. |
| ca514-004, ca514-007, ca514-010 | hold_image_check | 0.68 | `Sanegueso` is present in the conversion, but the conversion itself flags the street name as unusual. Do not normalize or promote this street reading until the page image is available. |
| ca514-005 | supported_limited_scope | 0.84 | The father field is transcribed as `Se ignora`. Promote only as a statement about this registration, not as a broader biological or legal conclusion. |
| ca514-006, ca514-008, ca514-009 | supported_from_conversion | 0.82 | The conversion supports Mercedes Riquelme as mother/declarant, her request that her name be recorded, and the no-signature statement. Maintain literal wording for the legal phrase. |
| ca514-011 | hold_image_check | 0.58 | Ignacio Soto is plainly supported by the conversion, but `Benjamin Utiera` is explicitly flagged as difficult. Hold the witness surname until image review. |
| ca515-001 through ca515-008 | supported_from_conversion | 0.86 | The converted file and chunk directly support child name/sex, registration date, birth date/time/place, named father and mother, nationality, occupation, and domicile facts. Avoid expanding `Santiago` beyond the literal place/domicile wording. |
| ca515-009 and ca515-010 | revise_before_canonical | 0.80 | Pedro Pablo Neira is listed as father and compareciente with age, occupation, and domicile. Same-entry equivalence is likely, but age-derived identity conclusions should wait for canonical identity review. |
| ca515-011 | supported_low_genealogical_value | 0.78 | Witness names are supported by the conversion, but witness tracking should only be promoted if relevant to the research objective. |
| ca515-012 | hold_image_check | 0.62 | The emendation note is transcribed in the conversion, but it is exactly the kind of marginal/official text that should be checked against the image before promotion. |

## Evidence Strengths

- The staged draft, converted file, and chunk agree on the shared source metadata: Los Angeles, Chile civil birth register, page 172, entries 513-515, dated July 1889.
- The draft's literal-support excerpts are present in the converted Markdown and assigned chunk, with no detected mismatch between the staged claims and the available transcription.
- The source type is strong for birth-event facts and for declared parent/declarant information because it is a civil birth register entry close in time to each birth.
- The draft preserves uncertainty appropriately for record 514's unusual street name, difficult witness surname, identity reconciliation, and record 515's emendation note.

## Review Judgment

The atomic claims are mostly well supported by the converted Markdown and chunk. Core registration, birth-event, parent-name, declarant, occupation, nationality, domicile, and witness facts can be treated as high-probability staged claims from the conversion.

Canonical readiness remains `hold` because the visible source image is unavailable. This prevents independent review of difficult handwriting, marginal/emendation text, and crop completeness. Claims requiring identity reconciliation should also be revised or held before canonical promotion so same-entry name variants and declarant/parent equivalence are not overextended into merged identities.

## Next Action

Restore or regenerate the page image, then re-check `Sanegueso`, `Benjamin Utiera`, the record 515 `Neira` emendation, and bottom-crop completeness. After image review, promote only literal registration-scoped claims first; send identity-linking claims for separate person/relationship review.
