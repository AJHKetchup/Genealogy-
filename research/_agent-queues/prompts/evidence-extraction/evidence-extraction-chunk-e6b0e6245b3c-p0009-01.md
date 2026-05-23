# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0009-chunk-01.md`
- Converted source: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`
- Chunk manifest: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json`
- Original source: `raw/sources/CV of Dario Arturo Pulgar.pdf`
- Page range: 9-9
- Staging area: `research/_staging`
- Family relevance: `high`
- Matched family terms: Dario, Pulgar
- Narrative cues: education
- Evidence priority: `-41` (family_relevance:high, qc:reread-page, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/identity-analysis-id-stage-chunk-e6b0e6245b3c-p0009-01-dario-cv-subject-proof-review-postconv-proof-review-20260523185732970.md` | `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-e6b0e6245b3c-p0009-01-dario-cv-subject.md` | `hold_for_identity_bridge` | Keep the staged draft on hold for canonical use. Reconcile the source packet's stale missing-page-image QA note with the now-present page image, then review an identity-bearing CV page or another accepted local source that explicitly connects `Dario Arturo Pulgar` with the intended canonical `Dario Arturo Pulgar-Smith` identity before any promotion, merge, or relationship attachment. |
| `research/_staging/reviews/proof-review-research-staging-identity-analysis-identity-analysis-chunk-e6b0e6245b3c-p0009-01-evidence-revision-hold-postconv-proof-review-20260523185923822.md` | `research/_staging/identity-analysis/identity-analysis-chunk-e6b0e6245b3c-p0009-01-evidence-revision-hold.md` | `hold_for_identity_bridge_and_source_packet_qa_reconciliation` | Reconcile the stale source-packet/conversion-QA missing-image note with the now-present `page-0009.jpg`, then run or rely on a separate identity-bridge proof review that explicitly connects the CV subject `Dario Arturo Pulgar` to any intended canonical person before promotion. |
| `research/_staging/reviews/proof-review-research-staging-identity-analysis-identity-analysis-conf-stage-chunk-e6b0e6245b3c-p0009-01-page-image-qa-postconv-proof-review-20260523185352116.md` | `research/_staging/identity-analysis/identity-analysis-conf-stage-chunk-e6b0e6245b3c-p0009-01-page-image-qa.md` | `hold_for_conversion_qa_and_identity_bridge` | Keep this staged draft on hold. Restore or generate the rendered page image for page 9, compare the converted education and language text against the PDF/page image, and then run a separate identity-bridge proof review before any canonical promotion or merge. |

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
