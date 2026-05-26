# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md`
- Converted source: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Chunk manifest: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/manifest.json`
- Original source: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`
- Page range: 1-1
- Staging area: `research/_staging`
- Family relevance: `none`
- Matched family terms: none
- Narrative cues: birth, father, witness
- Evidence priority: `3301` (family_relevance:none, qc:pass, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-postconv-proof-review-20260526233240501.md` | `research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-researcher-20260526230757479.md` | `hold_for_conversion_qa` | Run targeted conversion QA against the source image for entries 513 and 515, then re-run proof review on atomic claims only after the child-name, mother-surname, birth-date/time, and entry-515 row conflicts are reconciled. Keep this staged draft as a blocker/correction map, not a canonical evidence packet. |
| `research/_staging/reviews/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-postconv-proof-review-20260526234137676.md` | `research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-researcher-20260526230757479.md` | `hold` | Keep the staged draft on `hold_for_conversion_qa`. The next action is targeted row-level conversion QA against the original page image for entries 513 and 515, especially entry 513 child name, mother surname, birth date/time, and entry 515 child/father/mother fields. After QA-certified transcription exists, rerun proof review for atomic identity, birth-event, and parent-child relationship claims before any canonical promotion. |
| `research/_staging/reviews/proof-review-chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-proof-review-20260526233711772.md` | `research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-researcher-20260526230757479.md` | `hold_for_conversion_qa` | Keep this staged draft on `hold_for_conversion_qa`. The next action should be targeted page-image QA for entries 513 and 515, focused on entry 513 child-name lines, birth date/time, father/declarant details, mother surname, and the visible extent of entry 515 child/father/mother fields. After that QA exists, rerun proof review for separate atomic claims and relationship candidates before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-001-child-birth-name-postconv-proof-review-20260522130511490.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-001-child-birth-name.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the birth-name claim using the verified source-visible name form before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-002-child-sex-postconv-proof-review-20260522130719068.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-002-child-sex.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the sex claim using the verified source-visible child and sex fields before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-003-birth-date-time-postconv-proof-review-20260522131158369.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-003-birth-date-time.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the birth-date/time claim using the verified source-visible child and birth fields before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-004-birth-place-postconv-proof-review-20260522131453055.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-004-birth-place.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the birth-place claim using the verified source-visible child and birth-place fields before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-005-registration-date-postconv-proof-review-20260522131659712.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-005-registration-date.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the registration-date claim using the verified source-visible child identity and registration-date field before any canonical promotion. |

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
