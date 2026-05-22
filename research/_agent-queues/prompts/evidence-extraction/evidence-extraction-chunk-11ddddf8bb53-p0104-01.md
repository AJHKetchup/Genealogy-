# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca3e1a8684-r3016-11a-2905-950-p0101-0125-r3016-11a-2905-950-pages-101-125-codex/page-0104-chunk-01.md`
- Converted source: `raw/converted/ca3e1a8684-r3016-11a-2905-950-p0101-0125-r3016-11a-2905-950-pages-101-125.codex.md`
- Chunk manifest: `raw/chunks/ca3e1a8684-r3016-11a-2905-950-p0101-0125-r3016-11a-2905-950-pages-101-125-codex/manifest.json`
- Original source: `raw/sources/R3016-11A-2905-950.pdf`
- Page range: 104-104
- Staging area: `research/_staging`
- Family relevance: `medium`
- Matched family terms: Entry, chunk
- Evidence priority: `102104` (family_relevance:medium, qc:spot-check, matched_terms, blocked_by_conversion_qc)

## QC Hold

- Status: `blocked_needs_reread`
- Blocked pages: 104
- Page reread queue: `research/_conversion-review/page-queues/ca3e1a8684-r3016-11a-2905-950-p0101-0125-r3016-11a-2905-950-pages-101-125-codex.md`
- Suspected readings: `research/_conversion-review/corrections/ca3e1a8684-r3016-11a-2905-950-p0101-0125-r3016-11a-2905-950-pages-101-125-codex.md`

Do not extract claims from this chunk until the blocked page reread is resolved or the chunk is re-queued.



## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- If the chunk has low or no family relevance and no explicit family clue, do not fan out broad historical or official-name claims. Write at most a concise source-scope or negative-evidence note, then stop.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
