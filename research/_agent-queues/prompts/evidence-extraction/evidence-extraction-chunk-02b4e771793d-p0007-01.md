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
- Evidence priority: `-43` (family_relevance:high, qc:pass, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-identity-analysis-20260525002829666-proof-review-postconv-proof-review-20260525020804650.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-identity-analysis-20260525002829666.md` | `hold_for_conversion_qa_and_identity_bridge` | Keep the staged draft on hold. Reconcile the authoritative page-7 chunk ID and converted SHA, then review bridge evidence before attaching this page to any canonical Dario/Pulgar person page or relationship. No canonical files, raw sources, converted files, chunks, or source packets were edited in this review. |
| `research/_staging/reviews/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-identity-analysis-20260525002829666-proof-review-postconv-proof-review-20260525021150516.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-identity-analysis-20260525002829666.md` | `hold` | Keep the staged identity-analysis draft and underlying conflict candidate on hold. First reconcile conversion QA for page 7 of `Habitat Revisited`, including the authoritative chunk id and converted SHA. After that, review an identity-bearing bridge before attaching this memoir evidence to any canonical Dario Pulgar page or merging it with Pulgar-Smith, Pulgar-Arriagada, medical, Geneva/ICRC, property, passenger, or Jose/Juana family clusters. |
| `research/_staging/reviews/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-identity-analysis-20260525002829666-proof-review-postconv-proof-review-20260525021629630.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-identity-analysis-20260525002829666.md` | `hold` | Keep the staged draft on hold. Reconcile the authoritative converted-file hash, chunk id, and manifest state for page 7 before any canonical use. After conversion QA, evaluate this Habitat/Vision Habitat evidence alongside separately proof-reviewed CV or identity-bearing records; only a distinct bridge should decide whether this page-local `Dario Pulgar` belongs on a canonical person page. |
| `research/_staging/reviews/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-identity-analysis-20260525002829666-proof-review.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-identity-analysis-20260525002829666.md` | `not_ready` | Keep the item on hold for conversion QA. Reconcile the authoritative page-7 chunk id, converted SHA, and the minor `UNAVCHS`/`UNAVHS` transcription issue, then require a separate proof-reviewed identity bridge before any canonical attachment or merge. |
| `research/_staging/reviews/proof-review-identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-proof-review-20260525020001195.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-identity-analysis-20260525002829666.md` | `not_ready` | Reconcile the authoritative converted Markdown hash, chunk id, and manifest state for `Habitat Revisited` page 7. After that, run a separate identity-bridge proof review comparing this page-local `Dario Pulgar` evidence to proof-reviewed CV or family evidence before any canonical attachment to `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or Pulgar-Arriagada variants. |
| `research/_staging/reviews/proof-review-identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold-postconv-proof-review-20260525021416456.md` | `research/_staging/identity-analysis/identity-analysis-conflict-chunk-dd2b66f37e49-p0007-01-metadata-and-identity-hold.md` | `hold` | Keep this staged draft on hold. The next required action is conversion QA to reconcile the authoritative page-7 chunk id and converted SHA, followed by a separate identity-bridge review comparing the proof-reviewed Habitat evidence to proof-reviewed CV or family identity evidence. Do not promote claims, merge identities, rename pages, or attach this memoir paragraph to canonical Dario/Pulgar pages from this review alone. |

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
