# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0014-chunk-01.md`
- Converted source: `raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md`
- Chunk manifest: `raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/manifest.json`
- Original source: `raw/sources/El Aguila Nombre Grande Scan.pdf`
- Page range: 14-14
- Staging area: `research/_staging`
- Family relevance: `critical`
- Matched family terms: Dario, Dario Pulgar, Pulgar
- Narrative cues: none
- Evidence priority: `-686` (family_relevance:critical, qc:reread-page, matched_terms, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-postconv-identity-analysis-20260524193138285-proof-review-postconv-proof-review-20260524203058480.md` | `research/_staging/identity-analysis/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-postconv-identity-analysis-20260524193138285.md` | `hold_for_conversion_qa` | Hold the staged identity analysis in review until conversion QA restores or regenerates the page 14 rendered image and reconciles the chunk/converted SHA mismatch. The next reviewer should visually reread only the page-local forms: typed `DR DARIO PULGAR A` versus any `PULGARA` reading, the handwritten signature, whether `A.` is visibly separated, and whether the page itself names parents or expands the abbreviation. Do not attach this item to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or any Jose/Juana parent candidates without a |
| `research/_staging/reviews/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-postconv-identity-analysis-20260524193138285-proof-review-postconv-proof-review-20260524203444206.md` | `research/_staging/identity-analysis/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-postconv-identity-analysis-20260524193138285.md` | `not_ready` | Hold for targeted conversion QA and page-image reread. The next reviewer should inspect the actual page image/source page for the typed name, handwritten signature, and any visible context that might expand `A.` or identify parents. After that, review only narrow page-local claims first; any same-person bridge to `Arriagada`, `Arturo`, `Smith`, `Jose`, or parent candidates needs a separate proof review with its own cited evidence. |
| `research/_staging/reviews/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-postconv-identity-analysis-20260524193138285-proof-review.md` | `research/_staging/identity-analysis/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-postconv-identity-analysis-20260524193138285.md` | `hold` | Keep the staged analysis on hold for conversion QA. The next proof step should be a targeted visual reread of page 14 from the source PDF or recovered page image, focused only on the typed name, the handwritten signature, any expansion of `A.`, and whether the article names parents or other identity anchors. Do not promote or attach the identity until that reread and a separate identity-bridge review are complete. |
| `research/_staging/reviews/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-postconv-proof-review-20260524204317872.md` | `research/_staging/identity-analysis/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-postconv-identity-analysis-20260524193138285.md` | `hold_for_conversion_qa` | Hold the staged identity analysis. Restore or generate the referenced page image and perform a targeted visual proof review of page 14, limited to the typed `DR DARIO PULGAR A` line, the handwritten signature, any visible date/context, and whether any visible text expands `A.` or names parents. After that, review only narrow page-local claims before considering any separate identity-bridge task. |
| `research/_staging/reviews/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-proof-review.md` | `research/_staging/identity-analysis/identity-analysis-chunk-dfc1ae4668c1-p0014-01-pulgar-a-pulgara-name-watch-postconv-identity-analysis-20260524193138285.md` | `hold` | Keep the staged identity analysis at `hold_for_conversion_qa`. Restore or regenerate the page-14 image from `El Aguila Nombre Grande Scan.pdf`, then perform a targeted visual reread of the typed article name and handwritten signature. Only after that reread should any narrow page-local claim be promoted, and identity-bridge or parent-link claims should remain separate proof-review tasks. |

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
