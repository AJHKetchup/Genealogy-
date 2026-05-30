# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0401-0425-r3578-50-5569-5569-jacket5-pages-401-425-codex/page-0411-chunk-01.md`
- Converted source: `raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0401-0425-r3578-50-5569-5569-jacket5-pages-401-425.codex.md`
- Chunk manifest: `raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0401-0425-r3578-50-5569-5569-jacket5-pages-401-425-codex/manifest.json`
- Original source: `raw/sources/R3578-50-5569-5569-Jacket5.pdf`
- Page range: 411-411
- Staging area: `research/_staging`
- Family relevance: `high`
- Matched family terms: Pulgar
- Narrative cues: convention
- Evidence priority: `361` (family_relevance:high, qc:pass, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/chunk-2faa60e38062-p0411-01-initialed-pulgar-identity-watch-postconv-identity-analysis-20260530175415492-proof-review-postconv-proof-review-20260530190148761.md` | `research/_staging/identity-analysis/chunk-2faa60e38062-p0411-01-initialed-pulgar-identity-watch-postconv-identity-analysis-20260530175415492.md` | `hold` | Keep the staged draft on hold. Restore or retrieve the missing rendered page image or source PDF, then verify the Chile block directly against the source image. If the image confirms the line, promote only a narrow source-local claim that a person rendered as `D. Pulgar` appears under the Chile signature/list block on page 411. Any same-person merge requires separate identity-bearing evidence with a full name or strong bridge facts. |
| `research/_staging/reviews/chunk-2faa60e38062-p0411-01-initialed-pulgar-identity-watch-postconv-identity-analysis-20260530175415492-proof-review-postconv-proof-review-20260530190945103.md` | `research/_staging/identity-analysis/chunk-2faa60e38062-p0411-01-initialed-pulgar-identity-watch-postconv-identity-analysis-20260530175415492.md` | `hold` | Hold the staged draft from canonical promotion. Retrieve or generate the deferred page image through the normal conversion/QA workflow, then compare `page-0411.jpg` against the text-layer reading. If the image confirms the line, a downstream worker may stage only the narrow `D. Pulgar` Chile signatory claim and should keep all same-person merges or relationship conclusions pending separate full-name identity-bridge evidence. |

When revising, do not edit raw sources, converted Markdown, chunks, or page Markdown. Write new or updated staged drafts and/or conversion-review correction notes that preserve the disagreement between derivative transcripts and image-reviewed evidence. If the evidence remains blocked, keep `promotion_recommendation: hold_for_conversion_qa` and make the blocker explicit.


## Person-First Narrative Contract

- Start with known family members and reviewed family relationships, not source chunks as the main object.
- Extract claims only when they can support a family member, family relationship, life event, place in a family story, photograph, or narrative question.
- High-value narrative claims include where a family member stayed, traveled, lived, worked, studied, appeared in a photo, attended a meeting, served as a delegate, spoke, signed, witnessed, or was present for a discussion.
- Context about a hotel, institution, place, co-delegate, meeting, or historical setting is useful only when it directly explains a family member's experience or a specific family record. Keep broad background as a staged context/research note with an explicit linked family entity, or mark it low relevance.
- Do not fan out generic claims about all delegates, all places, or all official proceedings unless the chunk ties them to the family member's narrative.

## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- If the chunk has low or no family relevance and no explicit family clue, do not fan out broad historical or official-name claims. Write at most a concise source-scope or negative-evidence note, then stop.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
