# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md`
- Converted source: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk manifest: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/manifest.json`
- Original source: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Page range: 172-172
- Staging area: `research/_staging`
- Family relevance: `critical`
- Matched family terms: Birth, Carmen, Dios, Juan, Juana, Mercedes, Pulgar, Registration, Riquelme, chunk, mercedes riquelme
- Evidence priority: `99472` (family_relevance:critical, qc:reread-page, matched_terms, proof_review_revision, blocked_by_conversion_qc)

## QC Hold

- Status: `blocked_needs_reread`
- Blocked pages: 172
- Page reread queue: `research/_conversion-review/page-queues/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63.md`
- Suspected readings: `research/_conversion-review/corrections/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63.md`

Do not extract claims from this chunk until the blocked page reread is resolved or the chunk is re-queued.


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant-postconv-proof-review-20260522132543215.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md` | `hold` | Hold for conversion QA. Ask QA to verify entry 513 against the page image, repair the cited chunk path/id, and reconcile whether the declarant profession should be read as `Agricultor` or `Jornalero`. The name `José del C. Pulgar`, role `Padre`, age 47, and domicile `Calle Colon` have direct visible support, but the complete atomic claim should remain staged until the conversion conflict is resolved. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-birth-date-place-postconv-proof-review-20260522133432835.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-birth-date-place.md` | `hold_for_conversion_qa` | Run targeted conversion QA against the source image for entry 514's `Fecha i lugar del nacimiento` field. After QA, replace this staged claim with an image-supported, registration-scoped birth date/time/place claim before any canonical promotion. |

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
