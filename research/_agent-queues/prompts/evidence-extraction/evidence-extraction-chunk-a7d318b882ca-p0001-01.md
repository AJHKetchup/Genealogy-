# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/cadb21f94f-r3577-50-5569-5569-jacke-p0026-0050-r3577-50-5569-5569-jacket1-pages-26-50-codex/page-0001-chunk-01.md`
- Converted source: `raw/converted/cadb21f94f-r3577-50-5569-5569-jacke-p0026-0050-r3577-50-5569-5569-jacket1-pages-26-50.codex.md`
- Chunk manifest: `raw/chunks/cadb21f94f-r3577-50-5569-5569-jacke-p0026-0050-r3577-50-5569-5569-jacket1-pages-26-50-codex/manifest.json`
- Original source: `raw/sources/R3577-50-5569-5569-Jacket1.pdf`
- Page range: 1-1
- Staging area: `research/_staging`
- Family relevance: `medium`
- Matched family terms: Article
- Evidence priority: `2001` (family_relevance:medium, qc:pass, matched_terms)



## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- If the chunk has low or no family relevance and no explicit family clue, do not fan out broad historical or official-name claims. Write at most a concise source-scope or negative-evidence note, then stop.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
