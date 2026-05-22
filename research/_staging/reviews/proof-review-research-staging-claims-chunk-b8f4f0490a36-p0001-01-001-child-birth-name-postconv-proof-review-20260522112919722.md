---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/chunk-b8f4f0490a36-p0001-01-001-child-birth-name.md
staged_draft: research/_staging/claims/chunk-b8f4f0490a36-p0001-01-001-child-birth-name.md
reviewer: postconv-proof-review-20260522112919722
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: chunk-b8f4f0490a36-p0001-01-001-child-birth-name

## Blockers

- Hold for conversion QA: the staged draft and source packet both note a controller/requested `reread-page` concern before canonical promotion.
- The referenced raw source image was not available at `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` during this review, and the manifest's page image path under the conversion job was also not present. I could not independently verify the handwriting against the image.
- Do not normalize the recorded name to accented or modernized spelling before image review. The staged claim uses `Jose del Carmen Segundo Pulgar Arriagada`, which matches the available conversion text.

## Scores

- source_quality_score: 0.90
- conversion_confidence_score: 0.72
- evidence_quantity_score: 0.65
- agreement_score: 0.88
- identity_confidence_score: 0.84
- claim_probability: 0.82
- relevance_level: critical
- relevance_confidence: 0.93
- canonical_readiness: hold

## Evidence Strengths

- The staged claim, source packet, assigned chunk, and converted Markdown all agree on the literal child-name field for entry 172: `Nombre. Jose del Carmen Segundo Pulgar Arriagada`.
- The evidence is directly relevant to the claim type. A civil birth registration is a strong source for the child's recorded birth name when the transcription is verified.
- The claim is narrow and does not require a relationship jump. It asserts only the recorded birth name of the named child in entry 172.
- Identity risk is limited within this claim because the subject and object are the same full recorded name and are tied to a numbered birth-register entry.

## Review Judgment

The available derivative evidence supports the staged birth-name claim, but the review cannot clear it for canonical promotion because the required image reread could not be completed. The converted file and chunk are internally consistent, and there is no conflict among the accessible transcription artifacts for this specific name field.

Source reliability is high in principle because this is a civil birth register, but conversion confidence is held below high-final because the original image was unavailable to confirm the handwriting, diacritics, and exact spelling. The claim probability is therefore strong but not final.

## Next Action

Keep the claim on hold for conversion QA. Restore or locate the referenced page image, reread entry 172 against the image, and then rerun proof review or update this review status before any canonical promotion.
