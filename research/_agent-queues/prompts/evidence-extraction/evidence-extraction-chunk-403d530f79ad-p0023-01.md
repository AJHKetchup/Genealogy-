# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca9010aa1a-s495-2-2-p0026-0050-s495-2-2-pages-26-50-codex/page-0023-chunk-01.md`
- Converted source: `raw/converted/ca9010aa1a-s495-2-2-p0026-0050-s495-2-2-pages-26-50.codex.md`
- Chunk manifest: `raw/chunks/ca9010aa1a-s495-2-2-p0026-0050-s495-2-2-pages-26-50-codex/manifest.json`
- Original source: `raw/sources/S495-2-2.pdf`
- Page range: 23-23
- Staging area: `research/_staging`


## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- If the source states parent-child, spouse, household, sibling, grandparent, or same-person evidence, write the relationship candidate files before producing a long list of routine event/detail claims. Tree-building relationships are the highest-value extraction output.
- For dense register or table chunks, prefer a complete source packet plus relationship candidates and the most important identity/date/place claims over an exhaustive claim dump that risks timing out before relationships are staged.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
