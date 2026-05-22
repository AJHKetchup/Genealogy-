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


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/proof-review-research-staging-relationships-rel-stage-chunk-4127185dc97c-p0172-01-513-child-parents-postconv-proof-review-20260522074501392.md` | `research/_staging/relationships/REL-STAGE-CHUNK-4127185dc97c-P0172-01-513-child-parents.md` | `hold` | Keep this staged relationship on hold. Run conversion QA on entry 513 against the source image, focusing on the child name/surname and the mother's full name. After the corrected transcription is available, revise or replace this relationship candidate rather than promoting the current draft. |
| `research/_staging/reviews/proof-review-research-staging-relationships-rel-stage-chunk-4127185dc97c-p0172-01-514-child-mother-and-father-conflict-postconv-proof-review-20260522074633403.md` | `research/_staging/relationships/REL-STAGE-CHUNK-4127185dc97c-P0172-01-514-child-mother-and-father-conflict.md` | `hold` | Run conversion QA against the source image for entry 514, focusing on the father field, the child name, and the compareciente note. After QA, revise the staged relationship to preserve only the mother-child claim if the visible-source reading remains stable. |
| `research/_staging/reviews/proof-review-research-staging-relationships-rel-stage-chunk-4127185dc97c-p0172-01-515-child-parents-postconv-proof-review-20260522074851382.md` | `research/_staging/relationships/REL-STAGE-CHUNK-4127185dc97c-P0172-01-515-child-parents.md` | `hold` | Hold this staged relationship for conversion QA. Re-transcribe entry 515 from the image, focusing on the child full name, the father surname, the mother surname, and the father-as-declarant line. Do not promote the combined child-parents relationship until the names are reconciled against visible source evidence. |

When revising, do not edit raw sources, converted Markdown, chunks, or page Markdown. Write new or updated staged drafts and/or conversion-review correction notes that preserve the disagreement between derivative transcripts and image-reviewed evidence. If the evidence remains blocked, keep `promotion_recommendation: hold_for_conversion_qa` and make the blocker explicit.


## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
