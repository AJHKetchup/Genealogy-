# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Converted source: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Chunk manifest: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json`
- Original source: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`
- Page range: 1-1
- Staging area: `research/_staging`
- Family relevance: `high`
- Matched family terms: Arriagada, Carmen, Entries, Juana, Pulgar, Riquelme, Segundo
- Evidence priority: `301` (family_relevance:high, qc:pass, matched_terms, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/proof-review-rel-chunk-b8f4f0490a36-p0001-01-004-child-father-postconv-proof-review-20260522120356549.md` | `research/_staging/relationships/chunk-b8f4f0490a36-p0001-01-004-child-father.md` | `hold_for_conversion_qa` | Run or await targeted conversion QA on entry 172's father-name line. If QA confirms the visible source supports `Jose del Carmen Pulgar` without the suffix, the relationship can be reconsidered for scoped promotion as a child-father relationship only, separate from any father-identity merge or attribute claims. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-b8f4f0490a36-p0001-01-001-child-birth-name-postconv-proof-review-20260522112919722.md` | `research/_staging/claims/chunk-b8f4f0490a36-p0001-01-001-child-birth-name.md` | `hold` | Keep the claim on hold for conversion QA. Restore or locate the referenced page image, reread entry 172 against the image, and then rerun proof review or update this review status before any canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-b8f4f0490a36-p0001-01-001-child-birth-name-postconv-proof-review-20260522222759757.md` | `research/_staging/claims/chunk-b8f4f0490a36-p0001-01-001-child-birth-name.md` | `hold_for_conversion_qa` | Hold for conversion QA. Reconcile or regenerate the referenced converted Markdown/page Markdown so entry 172 matches the image-reread Pulgar/Arriagada row, or restore the source/page image at the manifest path for direct verification. After that, rerun proof review for canonical readiness. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-b8f4f0490a36-p0001-01-006-father-attributes-postconv-proof-review-20260522123003255.md` | `research/_staging/claims/chunk-b8f4f0490a36-p0001-01-006-father-attributes.md` | `hold_for_conversion_qa` | Hold this combined father-attributes claim for conversion QA. After QA, either promote a corrected combined claim if the father name and residence spelling are resolved, or split the supported attributes into narrower claims for `Chileno` and `Empleado` while keeping suffix and residence questions in review. |
| `research/_staging/reviews/proof-review-update-research-staging-relationships-chunk-b8f4f0490a36-p0001-01-001-child-parents-20260522-image-reread.md` | `research/_staging/relationships/chunk-b8f4f0490a36-p0001-01-001-child-parents.md` | `partial` |  type: proof_review_update status: draft role: evidence_extractor task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01 prior_review: "research/_staging/reviews/proof-review-research-staging-relationships-chunk-b8f4f0490a36-p0001-01-001-child-parents-postconv-proof-review-20260522112528091.md" |
| `research/_staging/reviews/proof-review-update-research-staging-relationships-chunk-b8f4f0490a36-p0001-01-002-parents-spousal-clue-20260522-image-reread.md` | `research/_staging/relationships/chunk-b8f4f0490a36-p0001-01-002-parents-spousal-clue.md` | `hold` |  type: proof_review_update status: draft role: evidence_extractor task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01 prior_review: "research/_staging/reviews/proof-review-research-staging-relationships-chunk-b8f4f0490a36-p0001-01-002-parents-spousal-clue-postconv-proof-review-20260522112724533.md" |

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
