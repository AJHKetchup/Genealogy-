---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-515-child-name-sex.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-515-child-name-sex.md
reviewer: postconv-proof-review-20260522185241101
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: Entry 515 Child Name And Sex

## Blockers

- Canonical readiness is `hold`. The staged draft and cited source packet both recommend `hold_for_conversion_qa` for entry 515 because the available source image is cropped at the lower row.
- The staged literal support includes `Sexo. Femenino`, but the referenced converted file's entry 515 cell reads `**Sexo.**` with no value after it. The available source PNG cuts off the lower part of entry 515, so the sex value is not directly verifiable from the image.
- The chunk path named in the staged draft and source packet, `raw/chunks/.../page-0172-chunk-01.md`, is unavailable in the workspace. The available chunks for the same source are `page-0001-chunk-01.md` variants, not the referenced page-0172 chunk.
- The available same-source chunks materially disagree on entry 515 identity: one variant has `Rosa Elvira del Carmen` but no sex value, while another has `Neira Ulloa / Laura de la Cruz` and `Femenino`. This creates identity and conversion-version risk that must be resolved before canonical use.
- Direct image review shows the entry 515 name area is partially visible and appears broadly consistent with a `Rosa Elvira...` reading, but the lower name continuation and sex field are not cleanly visible enough to verify the full staged claim.

## Scores

| source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
|---:|---:|---:|---:|---:|---:|---|---:|---|
| 0.88 | 0.30 | 0.35 | 0.25 | 0.42 | 0.38 | high | 0.90 | hold |

## Evidence Strengths

- The cited source is a civil birth register, a strong source type for a child's registered name and sex when the row is complete and the transcription is stable.
- The staged draft, source packet, converted file, and image all point to page 172, entry 515 of the 1889 Los Anjeles birth register.
- The visible image area does show the start of entry 515 and the name column, giving partial support for the claim's relevance and for a possible `Rosa Elvira...` name reading.
- The claim is directly relevant to the intended field because it concerns the `Nombre i sexo` column for entry 515.

## Review Judgment

Hold the staged claim. The source type is reliable and the claim is relevant, but the exact combined assertion is not sufficiently supported. The full registered name is only partially image-verifiable, the sex value is absent from the referenced converted file, the named chunk path is missing, and available same-source chunk variants conflict on the entry 515 identity.

This is a scored proof judgment rather than a binary rejection. A child-name claim may become usable after targeted conversion QA, but the present staged claim should not be promoted as `Rosa Elvira del Carmen` with sex `Femenino`.

## Next Action

Keep this claim out of canonical folders. Perform targeted conversion QA against a complete lower-row image or continuation image for entry 515, focusing on the full `Nombre i sexo` cell. After QA, revise the staged claim to the visible source-supported reading, including whether the sex field is actually stated, or retire this draft if it belongs to a different conversion version.
