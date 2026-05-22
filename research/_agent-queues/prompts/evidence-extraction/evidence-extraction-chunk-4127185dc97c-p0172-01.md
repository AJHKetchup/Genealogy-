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
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-4127185dc97c-P0172-01-513-declarant.md` | `research/_staging/claims/CL-STAGE-CHUNK-4127185dc97c-P0172-01-513-declarant.md` | `hold` | Re-transcribe or QA-reconcile entry 513 from the source image, especially the child-name field and heading/jurisdiction wording. If the declarant and father-name readings remain confirmed after QA, revise/promote only the registration-scoped declarant claim and keep any broader identity linkage for separate identity review. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-4127185dc97c-P0172-01-514-registration-date-postconv-proof-review-20260522091619206.md` | `research/_staging/claims/CL-STAGE-CHUNK-4127185dc97c-P0172-01-514-registration-date.md` | `hold` | Keep the claim held pending conversion QA for entry 514. After the row is re-transcribed or QA-reconciled against the source image, promote or revise only the registration-date claim if the date cell remains confirmed as July 23, 1889. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-4127185dc97c-P0172-01-515-birth-date-place-postconv-proof-review-20260522091806930.md` | `research/_staging/claims/CL-STAGE-CHUNK-4127185dc97c-P0172-01-515-birth-date-place.md` | `hold` | Re-transcribe or QA-reconcile entry 515 directly from the source image, focusing on the birth date/time/place cell and row alignment. After QA, revise the staged claim if the image supports a different reading, or promote only if the exact date, time, and place are confirmed. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-4127185dc97c-P0172-01-515-child-name-sex-postconv-proof-review-20260522091953334.md` | `research/_staging/claims/CL-STAGE-CHUNK-4127185dc97c-P0172-01-515-child-name-sex.md` | `hold` | Re-transcribe or QA-reconcile entry 515 directly from the source image, focusing first on the child-name cell and then on whether the sex field is visible and supports `Femenino`. After QA, revise the staged claim to the image-supported reading or promote only if the exact registered name and sex are confirmed. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-4127185dc97c-P0172-01-515-declarant-postconv-proof-review-20260522092142001.md` | `research/_staging/claims/CL-STAGE-CHUNK-4127185dc97c-P0172-01-515-declarant.md` | `hold` | Re-transcribe or QA-reconcile entry 515 directly from the source image, focusing on the father/declarant surname, then the declarant's role, age, occupation, and domicile. After QA, revise the staged claim to the image-supported reading or promote only if the exact declarant identity and details are confirmed. |
| `research/_staging/reviews/proof-review-research-staging-claims-cl-stage-chunk-4127185dc97c-p0172-01-513-birth-date-place-postconv-proof-review-20260522081049052.md` | `research/_staging/claims/CL-STAGE-CHUNK-4127185dc97c-P0172-01-513-birth-date-place.md` | `hold` | Keep the claim on hold for conversion QA. Reconcile entry 513's child-name field against the source image, then revise or rerun staged claims so the supported birth date/time/place is attached only to the person named in the visible source. |
| `research/_staging/reviews/proof-review-research-staging-claims-cl-stage-chunk-4127185dc97c-p0172-01-513-child-name-sex-postconv-proof-review-20260522081240882.md` | `research/_staging/claims/CL-STAGE-CHUNK-4127185dc97c-P0172-01-513-child-name-sex.md` | `hold` | Keep the claim on hold for conversion QA. Reconcile entry 513's child-name field against the source image, then revise or rerun the staged claim so `Masculino` is attached only to the person actually named in the visible register entry. |
| `research/_staging/reviews/proof-review-research-staging-claims-cl-stage-chunk-4127185dc97c-p0172-01-513-father-postconv-proof-review-20260522083924075.md` | `research/_staging/claims/CL-STAGE-CHUNK-4127185dc97c-P0172-01-513-father.md` | `hold` | Keep this claim on hold. Run targeted conversion QA for entry 513's child-name field, then revise or replace the father claim so `José del Carmen Pulgar` is linked only to the child actually named in the visible register entry. |

When revising, do not edit raw sources, converted Markdown, chunks, or page Markdown. Write new or updated staged drafts and/or conversion-review correction notes that preserve the disagreement between derivative transcripts and image-reviewed evidence. If the evidence remains blocked, keep `promotion_recommendation: hold_for_conversion_qa` and make the blocker explicit.


## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
