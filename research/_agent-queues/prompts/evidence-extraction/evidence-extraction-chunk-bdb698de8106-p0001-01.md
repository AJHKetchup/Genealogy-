# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`
- Converted source: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk manifest: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/manifest.json`
- Original source: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Page range: 1-1
- Staging area: `research/_staging`
- Family relevance: `critical`
- Matched family terms: Carmen, Entries, Juana, Mercedes, Pulgar, Riquelme, Soler, juan soler, mercedes riquelme
- Evidence priority: `-699` (family_relevance:critical, qc:reread-page, matched_terms, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant-proof-review.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md` | `hold_for_conversion_qa` | Keep the staged claim on hold pending conversion QA for entry 513. After QA resolves the row-level transcription conflict, this specific declarant appearance claim can be reconsidered for promotion with a high probability score if the declarant column remains unchanged. |
| `research/_staging/reviews/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name-proof-review.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name.md` | `hold_for_conversion_qa` | Hold this claim for targeted conversion QA on entry 515. The QA task should reconcile the partial source image against the converted `Rosa Elvira del Carmen` reading without replacing the transcription from inference alone. |
| `research/_staging/reviews/conversion-review-note-CHUNK-bdb698de8106-P0001-01-entry-513-image-reconciliation.md` | `` | `` |  type: conversion_review_note status: draft task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01 source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place-postconv-proof-review-20260522105816426.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md` | `hold` | Hold for conversion QA. Ask QA to reconcile entry 513's child identity, sex, birth date, birth time, and chunk id/path directly against the source image. After QA, revise or replace the staged claim from the corrected transcription; retain `Calle Colon` only if the corrected entry still supports that place for the confirmed subject. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place-postconv-proof-review-20260522231104509.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md` | `hold_for_conversion_qa` | Send to targeted conversion QA/image reread before any canonical promotion. The next reviewer should reconcile the entry 513 birth-date field against the image, especially `Junio veinte i dos` versus the converted `Julio veintidos`, and keep the child identity unresolved unless the visible source itself supports a stable reading. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place-postconv-proof-review-20260522235121450.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md` | `hold_for_conversion_qa` | Send to targeted conversion QA/image reread before promotion. QA should reconcile entry 513's child identity and the birth-date/time field directly against the restored page image, then revise or replace the staged claim from the corrected transcription. Retain `Calle Colon` only as a provisional entry-513 place reading until that QA pass is complete. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-name-sex-postconv-proof-review-20260522110007051.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-name-sex.md` | `hold` | Hold for conversion QA. Ask QA to reconcile entry 513's child name and the correct chunk id/path against the source image. Preserve `Sexo. Masculino` as supported, but do not create or normalize a canonical child identity from `Isolina del Carmen Jose` or from any alternate reading until the visible-source transcription is resolved. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant-postconv-proof-review-20260522132543215.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md` | `hold` | Hold for conversion QA. Ask QA to verify entry 513 against the page image, repair the cited chunk path/id, and reconcile whether the declarant profession should be read as `Agricultor` or `Jornalero`. The name `José del C. Pulgar`, role `Padre`, age 47, and domicile `Calle Colon` have direct visible support, but the complete atomic claim should remain staged until the conversion conflict is resolved. |

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
