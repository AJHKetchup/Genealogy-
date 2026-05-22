---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/source-packets/sp-chunk-3d3ab761209f-p0001-01-los-angeles-birth-register-page-172.md
staged_draft: research/_staging/source-packets/sp-chunk-3d3ab761209f-p0001-01-los-angeles-birth-register-page-172.md
reviewer: postconv-proof-review-20260522045721618
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: sp-chunk-3d3ab761209f-p0001-01-los-angeles-birth-register-page-172

## Blockers

- Hold for conversion QA: the staged packet correctly flags a material conflict between the assigned chunk and the converted file, and the conflict affects core identifying details for entries 513-515.
- Revise literal support before any canonical promotion: the staged packet quotes the page heading as `Los Angeles, num. 1o de Julio`, but the visible source image and converted file support `Los Anjeles, num. 1o de La Laja`. This is a literal-support error, not a normalization choice.
- Hold entry-level claims for records 513-515: the assigned chunk and converted file disagree on names, dates, places, parent fields, witnesses, and the officer signature. The visible image supports some converted-file readings and some chunk-like readings, but this review should not rewrite the transcription from the image.
- Treat record 515 as higher risk: the lower portion of the visible page is cropped, so completeness and signature claims for entry 515 are not fully verifiable from this image alone.

## Scores

- source_quality_score: 0.86
- conversion_confidence_score: 0.48
- evidence_quantity_score: 0.62
- agreement_score: 0.36
- identity_confidence_score: 0.52
- claim_probability: 0.58
- relevance_level: high
- relevance_confidence: 0.91
- canonical_readiness: hold

## Evidence Strengths

- The cited source image, converted file, and assigned chunk are available in the workspace, and the source SHA-256 in the staged packet matches the referenced source image metadata.
- The source type is strong for genealogy once accurately transcribed: a civil birth register page is primary evidence for birth registrations, declared parent fields, compareciente details, and official registration context.
- The broad source identity is supported: the page is a Chilean civil birth register page for 1889, page 172, with visible entries numbered 513, 514, and 515.
- The staged packet appropriately warns against normalizing names, streets, and surname parsing until the chunk-versus-converted conflict is resolved.

## Review Judgment

The staged source packet is relevant and useful as a QA warning, but it is not ready for canonical use. Its strongest supported claim is the process claim: this packet should remain held because the cited conversion artifacts disagree materially. Its weaker claims are the literal quoted support lines, especially the jurisdiction/date heading and any assertion that all details for entries 513-515 are settled.

Identity risk is moderate to high for person-level promotion. Multiple people are named in each registration, and the conflicting transcriptions would alter child names, parent names, witnesses, places, occupations, and official-signature readings. No relationship or identity merge should be promoted from this packet until a corrected transcription is reviewed against the visible source and any missing/cropped area is accounted for.

## Next Action

Keep this source packet on hold and route it to conversion QA. The next pass should reconcile the assigned chunk, converted file, and source image; correct the page heading; explicitly mark any cropped or unavailable fields for entry 515; and then regenerate or revise downstream claim packets before proof review is rerun.
