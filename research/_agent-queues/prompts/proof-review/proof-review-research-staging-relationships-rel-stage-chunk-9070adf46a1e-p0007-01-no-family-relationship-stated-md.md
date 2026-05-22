# Proof Review Task

Use $genealogy-proof-review.

You are a proof-review worker for this exact workspace:

$Root = "D:\a\Genealogy-\Genealogy-"

You are not alone in the codebase. Other workers may be handling separate staged drafts. Own only this staged draft and do not edit raw sources, converted Markdown, chunks, or canonical wiki pages.

## Assignment

- Role: claim_reviewer
- Staged draft: research/_staging/relationships/REL-STAGE-CHUNK-9070adf46a1e-P0007-01-no-family-relationship-stated.md
- Output area: research/_staging/reviews/

## Rules

- Read the staged draft and only the referenced converted file, chunk, page image, source packet, QA note, or source page needed to verify it.
- Check literal support, uncertainty, source reliability, conversion confidence, claim confidence, identity risk, relationship jumps, conflicts, relevance, and claim probability.
- Treat proof as a scored judgment, not a promoted/not-promoted binary. Include source_quality_score, conversion_confidence_score, evidence_quantity_score, agreement_score, identity_confidence_score, claim_probability, relevance_level, relevance_confidence, and canonical_readiness.
- Maintain the hard boundary between verification context and source transcription. "Please double-check whether this is Dario" is allowed; "change this to Dario" is forbidden unless the visible source itself supports that reading.
- If support is missing or the referenced conversion/chunk is unavailable, mark the item hold or revise; do not guess.
- Write a review note under research/_staging/reviews/ that references this exact staged draft.
- Do not promote to research/claims, research/relationships, wiki/people, wiki/families, or other canonical folders.

## Done When

- A review note exists under research/_staging/reviews/.
- The note includes probability/evidence scoring plus canonical_readiness.
- The note lists blockers first, then evidence strengths and next action.
