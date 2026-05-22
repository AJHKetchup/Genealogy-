---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-515-child-name-sex.md
staged_draft: research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-515-child-name-sex.md
reviewer: postconv-proof-review-20260522071912776
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: claim-chunk-3d3ab761209f-p0001-01-515-child-name-sex

## Blockers

- Hold for conversion QA: the assigned chunk and the assembled converted Markdown materially disagree on entry 515's child identity. The assigned chunk reads `Neira Ulloa / Laura de la Cruz / Femenino`, while the assembled converted file reads `Rosa Elvira del Carmen / Femenino`.
- Do not promote from the assembled converted Markdown for this claim. It appears to describe a different entry-515 child name than the image-visible and chunk-supported reading.
- Do not treat the sex field as independently image-confirmed from the available page image in this review. The page image is bottom-cropped around entry 515; the child-name area is visible, but the lower sex line is not clear enough for me to verify directly from the image.
- Keep the `Neira=emendado=` note as a QA concern. It supports that a correction/emendation exists for entry 515, but it also raises transcription sensitivity for the surname.

## Scoring

| source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
|---:|---:|---:|---:|---:|---:|---|---:|---|
| 0.88 | 0.50 | 0.68 | 0.34 | 0.72 | 0.70 | high | 0.95 | hold |

## Evidence Strengths

- The cited source is a civil birth register page, a strong primary source type for a child's registered name and sex when the entry is correctly read.
- The staged draft references the relevant source image, assigned chunk, source packet, and page reference for register page 172, entry 515.
- The assigned chunk directly supports the staged wording: `Nombre. / Neira Ulloa / Laura de la Cruz / Sexo. / Femenino`.
- Direct page-image inspection supports the major child-name reading in the assigned chunk: entry 515 visibly begins with `Neira Ulloa` and `Laura de la Cruz` in the `Nombre i sexo` column.
- The source packet records the same material QA issue and recommends `hold_for_conversion_qa`; it also notes the entry 515 emendation text `Neira=emendado=` and `vale=`.

## Review Judgment

The claim is highly relevant to the staged subject and makes no relationship jump. For the name portion, the best available evidence favors the assigned chunk over the assembled converted Markdown: the visible entry 515 name field appears consistent with `Neira Ulloa / Laura de la Cruz`, not `Rosa Elvira del Carmen`.

The full claim is still not canonically ready. The conversion layers disagree materially, and the sex value is supported by the assigned chunk but was not clearly verifiable from the available image crop/page view during this review. Because the staged claim combines name and sex, the scored judgment is `hold` rather than ready.

## Next Action

Keep this claim on hold for targeted conversion QA of entry 515's `Nombre i sexo` column. A corrected transcription or targeted crop should confirm both the visible child-name reading and the sex value before canonical promotion. If the sex line cannot be confirmed, split or revise the staged claim so that only the image-supported name portion proceeds.
