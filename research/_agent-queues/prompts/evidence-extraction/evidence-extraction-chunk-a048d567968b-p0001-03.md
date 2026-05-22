# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0001-chunk-03.md`
- Converted source: `raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md`
- Chunk manifest: `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/manifest.json`
- Original source: `raw/sources/Habitat Revisited, Jim Carney, 2006.pdf`
- Page range: 1-1
- Staging area: `research/_staging`
- Family relevance: `critical`
- Matched family terms: Dario, Pulgar, chile, chunk, last, mother, name, parents, supplied, time
- Evidence priority: `-699` (family_relevance:critical, qc:reread-page, matched_terms, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/chunk-a048d567968b-p0001-03-002-dario-pulgar-chile-film-distribution-proof-review.md` | `research/_staging/claims/chunk-a048d567968b-p0001-03-002-dario-pulgar-chile-film-distribution.md` | `hold_for_conversion_qa` | Complete conversion QA for `CHUNK-a048d567968b-P0001-03`: correct or document the page reference discrepancy between assigned page 1, converted page metadata/page 8, and the visually checked printed page 7. After that, this claim can be reconsidered for canonical promotion as a contextual occupation/role claim with memoir-source attribution. |
| `research/_staging/reviews/chunk-a048d567968b-p0001-03-004-dario-pulgar-mother-tongue-spanish-proof-review.md` | `research/_staging/claims/chunk-a048d567968b-p0001-03-004-dario-pulgar-mother-tongue-spanish.md` | `hold_for_conversion_qa` | Complete conversion QA for `CHUNK-a048d567968b-P0001-03`: restore or regenerate the missing rendered source image for the converted page 8 passage, visually verify the sentence "His mother tongue was Spanish", and correct or document the page reference discrepancy. Keep this claim in staging until that QA is complete. |
| `research/_staging/reviews/chunk-a048d567968b-p0001-03-conversion-qa-correction-note.md` | `` | `` |  type: conversion_review_correction status: draft role: evidence_extractor worker: postconv-evidence-extraction-20260522174958565 task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03 |

When revising, do not edit raw sources, converted Markdown, chunks, or page Markdown. Write new or updated staged drafts and/or conversion-review correction notes that preserve the disagreement between derivative transcripts and image-reviewed evidence. If the evidence remains blocked, keep `promotion_recommendation: hold_for_conversion_qa` and make the blocker explicit.


## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- If the chunk has low or no family relevance and no explicit family clue, do not fan out broad historical or official-name claims. Write at most a concise source-scope or negative-evidence note, then stop.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
