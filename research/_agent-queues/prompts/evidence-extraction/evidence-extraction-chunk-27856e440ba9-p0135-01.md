# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca24f561d6-r3577-50-5569-5569-jacke-p0126-0150-r3577-50-5569-5569-jacket3-pages-126-150-codex/page-0135-chunk-01.md`
- Converted source: `raw/converted/ca24f561d6-r3577-50-5569-5569-jacke-p0126-0150-r3577-50-5569-5569-jacket3-pages-126-150.codex.md`
- Chunk manifest: `raw/chunks/ca24f561d6-r3577-50-5569-5569-jacke-p0126-0150-r3577-50-5569-5569-jacket3-pages-126-150-codex/manifest.json`
- Original source: `raw/sources/R3577-50-5569-5569-Jacket3.pdf`
- Page range: 135-135
- Staging area: `research/_staging`
- Family relevance: `high`
- Matched family terms: Arriagada, Pulgar
- Narrative cues: convention
- Evidence priority: `85` (family_relevance:high, qc:pass, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/identity-analysis-id-stage-chunk-27856e440ba9-p0135-01-pulgar-arriagada-postconv-identity-analysis-20260530032230860-proof-review-postconv-proof-review-20260530175416524.md` | `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-27856e440ba9-p0135-01-pulgar-arriagada-postconv-identity-analysis-20260530032230860.md` | `hold_for_page_image_qa_and_identity_bridge_review` | Keep this item on hold. First, perform page-image QA for page 135, including the speaker heading and the `jjas`/likely `pas` reading. Then run a separate identity-bridge proof review comparing this page-local speaker with identity-bearing convention listings, especially any record that explicitly names `M. Dario Pulgar-Arriagada` with Chile and health-service context. Only after that bridge is accepted should claims from page 135 attach to a fuller Dario/Jose candidate or any canonical person page. |
| `research/_staging/reviews/identity-analysis-id-stage-chunk-27856e440ba9-p0135-01-pulgar-arriagada-postconv-identity-analysis-20260530032230860-proof-review-postconv-proof-review-20260530180038601.md` | `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-27856e440ba9-p0135-01-pulgar-arriagada-postconv-identity-analysis-20260530032230860.md` | `hold_for_conversion_qa_and_identity_bridge` | Hold for targeted conversion QA. The next action is to make the deferred page image available or otherwise visually inspect source page 135, confirm the speaker heading and the `jjas`/`pas` reading, then run a separate identity-bridge proof review against identity-bearing convention-list records before attaching this intervention to a fuller Dario Pulgar-Arriagada candidate. |
| `research/_staging/reviews/identity-analysis-id-stage-chunk-27856e440ba9-p0135-01-pulgar-arriagada-postconv-identity-analysis-20260530032703013-proof-review-postconv-proof-review-20260530180843690.md` | `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-27856e440ba9-p0135-01-pulgar-arriagada-postconv-identity-analysis-20260530032703013.md` | `hold` | Keep the staged draft on hold. First, locate or regenerate the rendered page image through the normal conversion QA workflow and verify the heading plus the `jjas` artifact against the visible page. After that, run a separate identity-bridge review using identity-bearing convention records before attaching this page-local intervention to any fuller Pulgar-Arriagada identity. |
| `research/_staging/reviews/identity-analysis-id-stage-chunk-27856e440ba9-p0135-01-pulgar-arriagada-postconv-identity-analysis-20260530032703013-proof-review-postconv-proof-review-20260530181512993.md` | `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-27856e440ba9-p0135-01-pulgar-arriagada-postconv-identity-analysis-20260530032703013.md` | `hold` | Hold from canonical promotion. The next action is page-image QA for source page 135, specifically confirming the speaker heading and resolving the `jjas` reading in the French sentence. After that, run a separate identity-bridge proof review against identity-bearing convention delegate lists before attaching this page-local intervention to a fuller Dario Pulgar-Arriagada identity. |

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
