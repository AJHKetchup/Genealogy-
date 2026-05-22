# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md`
- Converted source: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Chunk manifest: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/manifest.json`
- Original source: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`
- Page range: 1-1
- Staging area: `research/_staging`
- Family relevance: `critical`
- Matched family terms: Birth, Carmen, Entry, Juan, Luis, Registration, chunk
- Evidence priority: `-699` (family_relevance:critical, qc:reread-page, matched_terms, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-001-child-birth-name-postconv-proof-review-20260522130511490.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-001-child-birth-name.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the birth-name claim using the verified source-visible name form before any canonical promotion. |
| `research/_staging/reviews/proof-review-relationship-chunk-23b2269a97df-p0001-01-001-child-mother-postconv-proof-review-20260522125900173.md` | `research/_staging/relationships/chunk-23b2269a97df-p0001-01-001-child-mother.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After the assigned conversion/chunk are reconciled with the page image, re-review the child-mother relationship for scoped promotion using the recorded mother name or an already-established canonical identity mapping. |
| `research/_staging/reviews/proof-review-relationship-chunk-23b2269a97df-p0001-01-002-child-father-postconv-proof-review-20260522130103057.md` | `research/_staging/relationships/chunk-23b2269a97df-p0001-01-002-child-father.md` | `hold_for_conversion_qa` | Run targeted conversion QA for page 58, entry 172 against the source image. Confirm the child name and exact father-name form from the visible record, then revise or regenerate the converted text/chunk before considering canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-relationships-chunk-23b2269a97df-p0001-01-003-parental-pair-postconv-proof-review-20260522130308689.md` | `research/_staging/relationships/chunk-23b2269a97df-p0001-01-003-parental-pair.md` | `not_ready` | Complete the conversion QA reconciliation for entry 172. After the converted file/chunk are corrected or an explicit controlling image-reread note is approved, restage or revise this relationship as a parent-pair claim with any spousal inference kept indirect. |

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
