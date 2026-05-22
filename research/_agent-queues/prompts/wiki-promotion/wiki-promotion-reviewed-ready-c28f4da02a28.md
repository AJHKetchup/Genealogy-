# Reviewed Promotion Task

Use $genealogy-proof-review as the review contract and act as the wiki_promoter only for items already reviewed as promotion-ready.

You are a promotion worker for this exact workspace:

$Root = "D:\a\Genealogy-\Genealogy-"

## Assignment

- Role: wiki_promoter
- Review folder: research/_staging/reviews/
- Promotion command: python -m historic_doc_ingest.genealogy_wiki promote-staged --root "D:\a\Genealogy-\Genealogy-"

## Review-Ready Inputs

- research/_staging/claims/chunk-bdfcf4d3256f-p0002-01-002-virginio-gomez-birth-place.md (ready_for_scoped_secondary_birthplace_claim; review: research/_staging/reviews/proof-review-chunk-bdfcf4d3256f-p0002-01-002-virginio-gomez-birth-place-postconv-proof-review-20260522222529414.md)

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
