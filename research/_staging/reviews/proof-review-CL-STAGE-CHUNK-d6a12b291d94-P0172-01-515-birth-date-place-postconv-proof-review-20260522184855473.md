---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-515-birth-date-place.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-515-birth-date-place.md
reviewer: postconv-proof-review-20260522184855473
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: Entry 515 Birth Date, Time, And Place

## Blockers

- Canonical readiness is `hold`. The staged draft's own `promotion_recommendation` is `hold_for_conversion_qa`, and the cited source packet also recommends holding entry 515 claims pending conversion QA.
- The staged claim object, `16 July 1889, 10:00 p.m.; Calle San Joaquin`, is not literally supported by the referenced converted file or the available chunk text reviewed for this source.
- The staged literal support says `Fecha. Julio diez i seis de mil ochocientos ochenta i nueve, a las diez de la noche` and `Lugar. Calle San Joaquin`, but that wording is not present in the referenced converted file. The converted file instead has entry 515 as `El mismo veinte tres ... a las diez de la mañana` with no place transcribed.
- The chunk path named in the staged draft and source packet, `raw/chunks/.../page-0172-chunk-01.md`, is unavailable in the workspace. The available chunk for the same shortened directory is `page-0001-chunk-01.md`, and it also does not support the staged literal.
- A second available chunk for the same source has entry 515 as `Neira Ulloa / Laura de la Cruz`, with birth date `Julio diez i ocho ... a las diez de la mañana` and place `Calle Santiago`, which materially conflicts with the staged subject and staged claim.
- Direct review of the source PNG shows the entry 515 row is partly cropped at the bottom. The visible birth-date cell appears consistent with an opening like `Julio diez i ocho`, not the staged `Julio diez i seis`; the time and place require targeted image QA before any canonical use.
- Identity risk is high because the staged subject `Rosa Elvira del Carmen` conflicts with image-reviewed and alternate-chunk evidence for entry 515 as `Neira Ulloa / Laura de la Cruz`. This birth-date/place claim should not be used to anchor a canonical person or family.

## Scores

| source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
|---:|---:|---:|---:|---:|---:|---|---:|---|
| 0.88 | 0.20 | 0.42 | 0.10 | 0.18 | 0.12 | high | 0.82 | hold |

## Evidence Strengths

- The cited source is a civil birth register, a strong source type for a birth date, time, and place when the entry reading and identity are settled.
- The staged draft, source packet, converted file, and source image all point to page 172 and entry 515 of the 1889 Los Anjeles birth register.
- The claim is directly relevant to the intended evidence field because it concerns the `Fecha i lugar del nacimiento` column for entry 515.
- The visible image does show an entry 515 row and a birth-date/time/place cell, so this is a conversion-QA problem rather than an entirely absent source context.

## Review Judgment

The claim should be held and revised after conversion QA. Current support is insufficient for the exact staged assertion. The literal support quoted in the staged draft is not found in the referenced converted file, the named chunk path is missing, available chunk variants conflict materially, and the visible source image does not corroborate the staged date, time, place, or subject identity.

This is not a promoted/rejected binary judgment: the source type is reliable and the field is relevant, but the present claim probability is low because the transcription and identity alignment are unstable.

## Next Action

Keep this staged claim out of canonical folders. Perform targeted conversion QA on entry 515 using a complete lower-row image or continuation image, focusing on the child name/sex and the full `Fecha i lugar del nacimiento` cell. After QA, revise the staged claim to the visible source-supported reading or retire this staged draft if it belongs to a different row or conversion version.
