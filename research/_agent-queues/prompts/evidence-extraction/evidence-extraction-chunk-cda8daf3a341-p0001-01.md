# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a-codex/page-0001-chunk-01.md`
- Converted source: `raw/converted/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a.codex.md`
- Chunk manifest: `raw/chunks/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a-codex/manifest.json`
- Original source: `raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG`
- Page range: 1-1
- Staging area: `research/_staging`
- Family relevance: `high`
- Matched family terms: Arriagada, Dario, Pulgar
- Narrative cues: convention, geneva, photograph
- Evidence priority: `-49` (family_relevance:high, qc:pass, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493-proof-review-postconv-proof-review-20260526100317893.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md` | `hold_for_conversion_qa` | Keep the staged identity analysis on hold and route `CHUNK-b8f4f0490a36-P0001-01` to targeted conversion QA. QA should reconcile the source image, assigned chunk, held source packet, and current converted Markdown, then certify the controlling row and father-field ending before any proof-reviewed promotion is attempted. |
| `research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493-proof-review-postconv-proof-review-20260526101722223.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md` | `` | Keep the staged identity analysis on hold for targeted conversion QA. QA should compare the source image, converted Markdown, chunk, and held source packet; decide which row controls entry `172`; and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, identity, or Dario-line bridge is promoted. |
| `research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-proof-review-20260526100752339.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md` | `hold` | Keep the staged draft on `hold_for_conversion_qa`. Targeted QA should compare the page image, converted Markdown, chunk, and source packet; decide the controlling transcription for entry `172`; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting any identity, birth fact, parent-child relationship, parent merge, or Dario-line bridge. |
| `research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-proof-review-postconv-proof-review-20260526095544407.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md` | `hold` | Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, chunk, and held source packet. The QA outcome must decide the controlling entry-172 row and certify the father field before this material can return to proof review for canonical readiness. |
| `research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-proof-review-postconv-proof-review-20260526095846903.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md` | `0.08` | Keep the staged draft on `hold_for_conversion_qa`. The next required action is targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`: compare the source image, current converted Markdown, current chunk, and held source packet; decide the controlling entry-172 row; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical claim, relationship, identity merge, or Dario-line bridge is promoted. |
| `research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-proof-review.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md` | `hold_for_conversion_qa` | Send `CHUNK-b8f4f0490a36-P0001-01` to targeted conversion QA. Reconcile the converted Markdown, chunk, held source packet, and source image for page 58, entry `172`; certify the controlling row; and explicitly decide the father-field ending. After QA, rerun proof review before any promotion to `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or other canonical folders. |

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
