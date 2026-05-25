# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0007-chunk-01.md`
- Converted source: `raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md`
- Chunk manifest: `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/manifest.json`
- Original source: `raw/sources/Habitat Revisited, Jim Carney, 2006.pdf`
- Page range: 7-7
- Staging area: `research/_staging`
- Family relevance: `high`
- Matched family terms: Dario, Dario Pulgar, Pulgar
- Narrative cues: conference
- Evidence priority: `-43` (family_relevance:high, qc:reread-page, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/identity-analysis-conflict-chunk-8791cef1980e-p0007-01-no-genealogical-conflict-identified-postconv-identity-analysis-20260524224614092-proof-review.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-8791cef1980e-p0007-01-no-genealogical-conflict-identified-postconv-identity-analysis-20260524224614092.md` | `hold_for_conversion_qa` | Keep the staged identity analysis out of canonical promotion. Reconcile the referenced chunk metadata with the staged draft/source packet identifiers and clear or update the reread-page/page-image QA hold. After QA reconciliation, the page may support a narrow contextual note about page-local `Dario Pulgar` in the Vision Habitat narrative, but it still should not be used by itself to merge or attach claims to `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or Jose/Juana parent candidates. |
| `research/_staging/reviews/proof-review-identity-analysis-conflict-chunk-8791cef1980e-p0007-01-no-genealogical-conflict-identified-postconv-identity-analysis-20260524224614092-postconv-proof-review-20260524232219860.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-8791cef1980e-p0007-01-no-genealogical-conflict-identified-postconv-identity-analysis-20260524224614092.md` | `hold` | Resolve the conversion QA and metadata mismatch first: confirm which converted SHA and chunk id are current for page 7, verify the rendered page image against the converted transcription, and then rerun or update conversion QA before any canonical claim extraction. After that, compare this reviewed Habitat evidence with a separately proof-reviewed identity bridge for `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith` before attaching facts to a canonical person. |

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
