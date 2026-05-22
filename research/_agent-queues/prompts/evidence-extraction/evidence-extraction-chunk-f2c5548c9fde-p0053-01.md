# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dic-8fbd29c654/page-0053-chunk-01.md`
- Converted source: `raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-41-60.codex.md`
- Chunk manifest: `raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dic-8fbd29c654/manifest.json`
- Original source: `raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf`
- Page range: 53-53
- Staging area: `research/_staging`
- Family relevance: `critical`
- Matched family terms: Arturo, Gallegos, García, Larraín, Lavín
- Evidence priority: `-647` (family_relevance:critical, qc:reread-page, matched_terms, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/proof-review-chunk-f2c5548c9fde-p0053-01-003-arturo-larrain-garcia-locality-postconv-proof-review-20260522210734131.md` | `research/_staging/claims/chunk-f2c5548c9fde-p0053-01-003-arturo-larrain-garcia-locality.md` | `hold_for_conversion_qa` | Keep the claim in staging. Perform conversion QA or restore/render `page-0053.jpg` and visually reread the `Larraín García, Arturo` row to confirm the name, row alignment, address, and locality before any canonical promotion. |
| `research/_staging/reviews/proof-review-chunk-f2c5548c9fde-p0053-01-006-arturo-lavin-gallegos-locality-postconv-proof-review-20260522210944929.md` | `research/_staging/claims/chunk-f2c5548c9fde-p0053-01-006-arturo-lavin-gallegos-locality.md` | `revise_literal_support_before_promotion` | Keep the claim in staging until the literal-support quote or conversion QA note handles the `Merced 250 B` address character. After that limited cleanup, the locality claim can be considered for canonical promotion only as a scoped 1959 medical-directory locality listing for `Arturo Lavín Gallegos` in `Santiago`. |

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
