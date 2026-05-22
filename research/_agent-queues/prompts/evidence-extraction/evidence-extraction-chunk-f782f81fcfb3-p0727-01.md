# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca221159bd-c-mara-de-senadores-de-l-p0704-0728-c-mara-de-senadores-de-la-naci-n-1936-fbca9c2302/page-0727-chunk-01.md`
- Converted source: `raw/converted/ca221159bd-c-mara-de-senadores-de-l-p0704-0728-c-mara-de-senadores-de-la-naci-n-1936-pages-704-728.codex.md`
- Chunk manifest: `raw/chunks/ca221159bd-c-mara-de-senadores-de-l-p0704-0728-c-mara-de-senadores-de-la-naci-n-1936-fbca9c2302/manifest.json`
- Original source: `raw/sources/Cámara de Senadores de la Nación, 1936.pdf`
- Page range: 727-727
- Staging area: `research/_staging`


## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
