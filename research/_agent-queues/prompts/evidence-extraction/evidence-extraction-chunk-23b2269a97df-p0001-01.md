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
- Family relevance: `medium`
- Matched family terms: Carmen
- Evidence priority: `1301` (family_relevance:medium, qc:pass, matched_terms, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-001-child-birth-name-postconv-proof-review-20260522130511490.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-001-child-birth-name.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the birth-name claim using the verified source-visible name form before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-002-child-sex-postconv-proof-review-20260522130719068.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-002-child-sex.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the sex claim using the verified source-visible child and sex fields before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-003-birth-date-time-postconv-proof-review-20260522131158369.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-003-birth-date-time.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the birth-date/time claim using the verified source-visible child and birth fields before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-004-birth-place-postconv-proof-review-20260522131453055.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-004-birth-place.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the birth-place claim using the verified source-visible child and birth-place fields before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-005-registration-date-postconv-proof-review-20260522131659712.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-005-registration-date.md` | `not_ready_conversion_conflict` | Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the registration-date claim using the verified source-visible child identity and registration-date field before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-006-father-name-postconv-proof-review-20260522131906480.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-006-father-name.md` | `not_ready_conversion_conflict` | Run targeted conversion QA for page 58, entry 172 against the source image. Confirm the exact father-name reading and either correct/regenerate the converted text and chunk or explicitly document the image reread as the controlling transcript before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-007-mother-name-postconv-proof-review-20260522132119234.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-007-mother-name.md` | `not_ready_conversion_conflict` | Run targeted conversion QA for page 58, entry 172 against the source image. Confirm the exact mother-name reading, including whether `de Pulgar` is part of the recorded name, and either correct/regenerate the converted text and chunk or explicitly document the image reread as the controlling transcript before any canonical promotion. |
| `research/_staging/reviews/proof-review-claim-chunk-23b2269a97df-p0001-01-008-informant-postconv-proof-review-20260522132330653.md` | `research/_staging/claims/chunk-23b2269a97df-p0001-01-008-informant.md` | `not_ready_conversion_conflict` | Run targeted conversion QA for page 58, entry 172 against the source image. Confirm the exact compareciente/informant name, including whether the given name should be read as `Oswaldo` or another spelling, and either correct/regenerate the converted text and chunk or explicitly document the image reread as the controlling transcript before any canonical promotion. |

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
