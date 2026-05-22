# Reviewed Promotion Task

Use $genealogy-proof-review as the review contract and act as the wiki_promoter only for items already reviewed as promotion-ready.

You are a promotion worker for this exact workspace:

$Root = "D:\a\Genealogy-\Genealogy-"

## Assignment

- Role: wiki_promoter
- Review folder: research/_staging/reviews/
- Promotion command: python -m historic_doc_ingest.genealogy_wiki promote-staged --root "D:\a\Genealogy-\Genealogy-"

## Review-Ready Inputs

- research/_staging/claims/cl-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-age.md (ready_with_scope_note; review: research/_staging/reviews/proof-review-claim-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-age-postconv-proof-review-20260522124638203.md)
- research/_staging/claims/cl-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-citizenship-chile.md (ready_with_scope_note; review: research/_staging/reviews/proof-review-claim-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-citizenship-chile-postconv-proof-review-20260522125249780.md)
- research/_staging/claims/cl-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-intended-future-residence-chile.md (ready_with_scope_note; review: research/_staging/reviews/proof-review-claim-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-intended-future-residence-chile-postconv-proof-review-20260522125452404.md)
- research/_staging/claims/cl-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-last-permanent-residence-england.md (ready_for_canonical_claim; review: research/_staging/reviews/proof-review-claim-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-last-permanent-residence-england-postconv-proof-review-20260522125656205.md)
- research/_staging/claims/cl-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-passenger-andes.md (ready_with_scope_note; review: research/_staging/reviews/proof-review-claim-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-passenger-andes-postconv-proof-review-20260522124839768.md)
- research/_staging/claims/cl-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-student.md (ready_for_canonical_claim; review: research/_staging/reviews/proof-review-claim-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-child-student-postconv-proof-review-20260522125045647.md)
- research/_staging/claims/chunk-b8f4f0490a36-p0001-01-005-registration-date.md (promote_after_review_for_registration_date_only; review: research/_staging/reviews/proof-review-claim-chunk-b8f4f0490a36-p0001-01-005-registration-date-postconv-proof-review-20260522115913855.md)
- research/_staging/claims/chunk-b8f4f0490a36-p0001-01-007-mother-attributes.md (promote_after_review; review: research/_staging/reviews/proof-review-claim-chunk-b8f4f0490a36-p0001-01-007-mother-attributes-postconv-proof-review-20260522123209997.md)
- research/_staging/relationships/chunk-b8f4f0490a36-p0001-01-003-child-mother.md (ready_for_scoped_promotion; review: research/_staging/reviews/proof-review-relationship-chunk-b8f4f0490a36-p0001-01-003-child-mother-postconv-proof-review-20260522120159415.md)
- research/_staging/claims/chunk-b8f4f0490a36-p0001-01-002-child-sex.md (ready_after_review; review: research/_staging/reviews/proof-review-research-staging-claims-chunk-b8f4f0490a36-p0001-01-002-child-sex-postconv-proof-review-20260522113117296.md)
- research/_staging/claims/chunk-b8f4f0490a36-p0001-01-001-child-birth-name.md (ready_after_review; review: research/_staging/reviews/proof-review-update-research-staging-claims-chunk-b8f4f0490a36-p0001-01-001-child-birth-name-20260522-image-reread.md)

## Rules

- Promote only staged material with explicit review notes showing strong source support, conservative scores, and promotion-ready canonical_readiness, such as ready, ready_with_caveats, ready_for_canonical_claim, ready_with_scope_note, ready_after_review, or ready_for_scoped_promotion.
- Preserve probability, source quality, conflicts, and uncertainty in canonical pages; promotion is an operational state, not a truth binary.
- Preserve the distinction between literal transcription and interpretation. Do not convert a suspected reading into canonical fact unless the review says the visible source supports it.
- Living-family privacy is not a standalone hold for this internal family project; user approval was recorded in research/_automation/post-conversion-architecture.json. Still require reviewed evidence, source support, and conservative confidence/status labels.
- Do not promote drafts with missing converted/chunk evidence, open conversion QA holds, unresolved identity conflicts, low claim probability, or canonical_readiness below ready.
- Run a dry run first and inspect skipped items before any real promotion.
- After promotion, run python -m historic_doc_ingest.genealogy_wiki lint --root "D:\a\Genealogy-\Genealogy-" and update research/log.md.

## Done When

- A promotion manifest exists under research/_staging/promotions/, or the task writes a review note explaining why nothing was safe to promote.
