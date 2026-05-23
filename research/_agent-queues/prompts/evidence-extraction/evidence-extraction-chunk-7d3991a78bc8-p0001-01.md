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
- Family relevance: `critical`
- Matched family terms: Carmen, Entries, Osorio
- Evidence priority: `-699` (family_relevance:critical, qc:reread-page, matched_terms, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/chunk-7d3991a78bc8-p0001-01-001-child-birth-name-proof-review.md` | `research/_staging/claims/chunk-7d3991a78bc8-p0001-01-001-child-birth-name.md` | `hold_for_conversion_qa` | Send to conversion QA to reconcile `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and its chunk against the source image for page 58, entry 172. Do not promote this birth-name claim until that reconciliation is recorded. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-7d3991a78bc8-p0001-01-002-child-sex-postconv-proof-review-20260523002215327.md` | `research/_staging/claims/chunk-7d3991a78bc8-p0001-01-002-child-sex.md` | `hold_for_conversion_qa` | Send to conversion QA to reconcile `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md` against the source image for page 58, entry 172. Keep this sex claim staged on hold until that reconciliation is recorded. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-7d3991a78bc8-p0001-01-003-birth-date-time-postconv-proof-review-20260523002508736.md` | `research/_staging/claims/chunk-7d3991a78bc8-p0001-01-003-birth-date-time.md` | `hold_for_conversion_qa` | Send to conversion QA to reconcile `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md` against the original image for page 58, entry 172. Do not promote this birth-date/time claim until that reconciliation is recorded. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-7d3991a78bc8-p0001-01-004-birth-place-postconv-proof-review-20260523002806777.md` | `research/_staging/claims/chunk-7d3991a78bc8-p0001-01-004-birth-place.md` | `hold_for_conversion_qa` | Send to conversion QA to reconcile `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md` against the original image for page 58, entry 172. Do not promote this birth-place claim until that reconciliation is recorded. |
| `research/_staging/reviews/proof-review-research-staging-relationships-chunk-7d3991a78bc8-p0001-01-001-child-father-postconv-proof-review-20260523001103477.md` | `research/_staging/relationships/chunk-7d3991a78bc8-p0001-01-001-child-father.md` | `hold` | Hold for conversion QA. Restore or locate the original source image or manifest page image, reread entry 172 on register page 58, and reconcile the Bunster/de la Maza derivative against the Pulgar/Arriagada staging before promoting, revising, or retiring this relationship candidate. |
| `research/_staging/reviews/proof-review-research-staging-relationships-chunk-7d3991a78bc8-p0001-01-002-child-mother-postconv-proof-review-20260523001356614.md` | `research/_staging/relationships/chunk-7d3991a78bc8-p0001-01-002-child-mother.md` | `revise` | Send the assigned converted file and chunk through targeted conversion QA for entry 172, page 58. Revise or retire this staged candidate so it no longer asserts the unsupported `Jose Miguel` to `Amelia de la Maza` relationship, then rerun proof review only after the derivative transcript matches the source-visible entry. |
| `research/_staging/reviews/proof-review-research-staging-relationships-chunk-7d3991a78bc8-p0001-01-003-child-parents-postconv-proof-review-20260523001643173.md` | `research/_staging/relationships/chunk-7d3991a78bc8-p0001-01-003-child-parents.md` | `revise` | Hold for targeted conversion QA on entry 172, register page 58. Reconcile the assigned converted Markdown and chunk with the source image, then revise or retire this staged candidate before any canonical relationship promotion is considered. |

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
