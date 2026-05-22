# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca221159bd-c-mara-de-senadores-de-l-p0479-0503-c-mara-de-senadores-de-la-naci-n-1936-0d3d48efc7/page-0003-chunk-01.md`
- Converted source: `raw/converted/ca221159bd-c-mara-de-senadores-de-l-p0479-0503-c-mara-de-senadores-de-la-naci-n-1936-pages-479-503.codex.md`
- Chunk manifest: `raw/chunks/ca221159bd-c-mara-de-senadores-de-l-p0479-0503-c-mara-de-senadores-de-la-naci-n-1936-0d3d48efc7/manifest.json`
- Original source: `raw/sources/Cámara de Senadores de la Nación, 1936.pdf`
- Page range: 3-3
- Staging area: `research/_staging`

## QC Hold

- Status: `blocked_needs_reread`
- Blocked pages: 3
- Page reread queue: `research/_conversion-review/page-queues/ca221159bd-c-mara-de-senadores-de-l-p0479-0503-c-mara-de-senadores-de-la-naci-n-1936-0d3d48efc7.md`
- Suspected readings: `research/_conversion-review/corrections/ca221159bd-c-mara-de-senadores-de-l-p0479-0503-c-mara-de-senadores-de-la-naci-n-1936-0d3d48efc7.md`

Do not extract claims from this chunk until the blocked page reread is resolved or the chunk is re-queued.


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
