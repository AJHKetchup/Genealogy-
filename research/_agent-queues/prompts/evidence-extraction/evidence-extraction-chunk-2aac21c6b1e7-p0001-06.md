# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca47b759d1-historia-del-hospital-cl-p0041-0060-historia-del-hospital-cl-nico-regional-de-concepci-n-carlos-p-rez-arrau-september-2013-pp-45-48-appendix-directors-of-hospital-cl-nico-regional-pages-41-60-codex/page-0001-chunk-06.md`
- Converted source: `raw/converted/ca47b759d1-historia-del-hospital-cl-p0041-0060-historia-del-hospital-cl-nico-regional-de-concepci-n-carlos-p-rez-arrau-september-2013-pp-45-48-appendix-directors-of-hospital-cl-nico-regional-pages-41-60.codex.md`
- Chunk manifest: `raw/chunks/ca47b759d1-historia-del-hospital-cl-p0041-0060-historia-del-hospital-cl-nico-regional-de-concepci-n-carlos-p-rez-arrau-september-2013-pp-45-48-appendix-directors-of-hospital-cl-nico-regional-pages-41-60-codex/manifest.json`
- Original source: `raw/sources/Historia del Hospital Clínico Regional de Concepción, Carlos Pérez Arrau, September 2013, pp. 45–48, Appendix Directors of Hospital Clínico Regional.pdf`
- Page range: 1-1
- Staging area: `research/_staging`
- Family relevance: `critical`
- Matched family terms: Article, Segundo, Virginio, concepcion
- Evidence priority: `100001` (family_relevance:critical, qc:reread-page, matched_terms, blocked_by_conversion_qc)

## QC Hold

- Status: `blocked_needs_reread`
- Blocked pages: 1
- Page reread queue: `research/_conversion-review/page-queues/ca47b759d1-historia-del-hospital-cl-p0041-0060-historia-del-hospital-cl-nico-regional-a64bacd7fc.md`
- Suspected readings: `research/_conversion-review/corrections/ca47b759d1-historia-del-hospital-cl-p0041-0060-historia-del-hospital-cl-nico-regional-a64bacd7fc.md`

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
