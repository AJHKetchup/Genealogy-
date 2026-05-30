# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0005-chunk-01.md`
- Converted source: `raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md`
- Chunk manifest: `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/manifest.json`
- Original source: `raw/sources/Habitat Revisited, Jim Carney, 2006.pdf`
- Page range: 5-5
- Staging area: `research/_staging`
- Family relevance: `high`
- Matched family terms: Pulgar
- Narrative cues: conference, delegate, delegation, discussion, hotel
- Evidence priority: `-45` (family_relevance:high, qc:pass, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121-proof-review-20260530152916674.md` | `research/_staging/identity-analysis/identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121.md` | `not_ready` | Keep the staged draft on hold and do not promote any page-5 facts to canonical claims or relationships. The next required action is provenance and conversion QA: restore or regenerate the missing page-5 image, verify the page-5 text visually, and reconcile the converted-file SHA mismatch. After that, a separate identity-bridge review can compare verified page-5 `Pulgar` with same-source `Dario Pulgar` and any candidate CV or canonical Pulgar identities. |
| `research/_staging/reviews/identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121-proof-review-postconv-proof-review-20260530152131494.md` | `research/_staging/identity-analysis/identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121.md` | `not_ready` | Keep this staged identity analysis as `hold` / `not_ready`. Reconcile the converted-file SHA mismatch, restore or regenerate the missing page-5 image for conversion QA, and then run a targeted identity-bridge review comparing proof-reviewed page 5 with the same-source `Dario Pulgar` references before any claim, relationship, or canonical wiki promotion. |
| `research/_staging/reviews/identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121-proof-review-postconv-proof-review-20260530153346952.md` | `research/_staging/identity-analysis/identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121.md` | `hold` | Keep this staged draft as a non-canonical identity-risk aid. Reconcile the converted-file SHA mismatch and restore or regenerate the missing page 5 image through the normal source-prep/conversion QA workflow, then proof-review page 5 visually. After that, a separate identity-bridge review can compare page 5 with the same-source `Dario Pulgar` references and any CV/canonical Pulgar-Smith bridge evidence. |
| `research/_staging/reviews/identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121-proof-review-postconv-proof-review-20260530153816819.md` | `research/_staging/identity-analysis/identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121.md` | `hold` | Keep the staged identity analysis on hold and do not promote any page-5 claim to `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or other canonical locations. The next required action is conversion/provenance QA: restore or regenerate the page 5 image for visual proofing and reconcile the converted-file SHA mismatch. After that, perform a targeted identity bridge review comparing page 5 with the same-source `Dario Pulgar` references before any broader canonical attachment is considered. |
| `research/_staging/reviews/proof-review-identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121.md` | `research/_staging/identity-analysis/identity-analysis-chunk-ff8bc4b91301-p0005-01-no-material-conflict-postconv-identity-analysis-20260530144112121.md` | `not_ready` | Hold the staged identity analysis as a review aid only. Reconcile the converted-file SHA mismatch and restore or locate the referenced page image for page 5, then proof-review the page visually against the source page. After that, a separate identity-bridge review can compare proof-reviewed page-5 `Pulgar` with same-source `Dario Pulgar` evidence from other Habitat pages and any CV/canonical `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith` bridge evidence. |

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
