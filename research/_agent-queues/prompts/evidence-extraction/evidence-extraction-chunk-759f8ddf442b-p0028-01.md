# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/page-0028-chunk-01.md`
- Converted source: `raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-21-40.codex.md`
- Chunk manifest: `raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/manifest.json`
- Original source: `raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf`
- Page range: 28-28
- Staging area: `research/_staging`
- Family relevance: `none`
- Matched family terms: none
- Narrative cues: none
- Evidence priority: `3328` (family_relevance:none, qc:pass, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-proof-review-postconv-proof-review-20260523213139227.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz.md` | `hold_for_conversion_qa` | Complete `research/_staging/research-tasks/chunk-759f8ddf442b-p0028-01-reread-page.md`: locate or regenerate the rendered page image for source page 28, compare the printed page against the converted row, and verify exact diacritics, address spelling, row alignment, and column headings. If the row is confirmed, route only the directory listing/contact/locality claims for proof review; do not promote any relationship or same-person merge from this draft. |
| `research/_staging/reviews/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-proof-review-postconv-proof-review-20260523213557496.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz.md` | `hold_for_conversion_qa` | Complete `research/_staging/research-tasks/chunk-759f8ddf442b-p0028-01-reread-page.md`: locate or regenerate the rendered page image for source page 28, compare the printed page against the converted row, and verify exact diacritics, address spelling, row alignment, and column headings. If confirmed, route only the directory listing/contact/locality claims for proof review; do not promote a relationship, merge, or canonical identity from this draft. |
| `research/_staging/reviews/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-proof-review-postconv-proof-review-20260523214857765.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz.md` | `hold_for_conversion_qa` | Keep the staged draft on `hold_for_conversion_qa`. The next action is to locate or regenerate the page 28 image and visually reread the printed source against the converted row, including name diacritics, `Darío Urzúa 1660`, `Santiago`, row alignment, and column headings. After that, the narrow directory listing/contact/locality claims can be proof-reviewed again; do not promote this draft to canonical folders now. |
| `research/_staging/reviews/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-proof-review-postconv-proof-review-20260523215340586.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz.md` | `hold_for_conversion_qa` | Keep the staged draft on `hold_for_conversion_qa`. The next required action is a page-28 visual reread against the original source page or regenerated page image, checking the name, diacritics, `Darío Urzúa 1660`, `Santiago`, column headings, and row alignment. After that, rerun proof review for only the narrow directory listing/contact claims; do not create canonical relationships or same-person merges from this row. |
| `research/_staging/reviews/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-proof-review.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz.md` | `hold_for_conversion_qa` | Keep `research/_staging/identity-analysis/identity-analysis-conflict-chunk-759f8ddf442b-p0028-01-juana-diaz-munoz.md` on hold. The next action is a page reread of source page 28 against the rendered page image or original PDF to confirm the exact name, accents, address, locality, row alignment, and column headings. Do not promote a canonical claim, relationship, merge, or conflict until that visual QA is complete. |

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
