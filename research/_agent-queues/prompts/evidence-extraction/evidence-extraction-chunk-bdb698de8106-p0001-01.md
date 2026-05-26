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
- Family relevance: `high`
- Matched family terms: Pulgar
- Narrative cues: birth, father, mother
- Evidence priority: `-49` (family_relevance:high, qc:pass, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant-proof-review.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md` | `hold_for_conversion_qa` | Keep the staged claim on hold pending conversion QA for entry 513. After QA resolves the row-level transcription conflict, this specific declarant appearance claim can be reconsidered for promotion with a high probability score if the declarant column remains unchanged. |
| `research/_staging/reviews/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name-proof-review.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name.md` | `hold_for_conversion_qa` | Hold this claim for targeted conversion QA on entry 515. The QA task should reconcile the partial source image against the converted `Rosa Elvira del Carmen` reading without replacing the transcription from inference alone. |
| `research/_staging/reviews/conversion-review-note-CHUNK-bdb698de8106-P0001-01-entries-513-515-revision-20260525.md` | `` | `` |  type: conversion_review_note status: draft task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01 source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png |
| `research/_staging/reviews/conversion-review-note-CHUNK-bdb698de8106-P0001-01-entry-513-image-reconciliation.md` | `` | `` |  type: conversion_review_note status: draft task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01 source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png |
| `research/_staging/reviews/conversion-review-note-CHUNK-bdb698de8106-P0001-01-task-revision-20260526.md` | `` | `` |  type: conversion_review_note status: draft task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01 source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png |
| `research/_staging/reviews/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts-proof-review-postconv-proof-review-20260523180329671.md` | `research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md` | `hold` | Keep `research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md` on hold for conversion QA. Create or regenerate the correct page chunk for `CHUNK-4127185dc97c-P0172-01`, then perform a targeted corrected transcription of entries 513-515 from the source image. Only after that should any proof-review worker evaluate whether entry 513 connects to existing Pulgar/Juana wiki identities. Do not promote, merge, rename, or attach any Dario/Pulgar/Pulgar-Smith/Arriagada identity from this staged draft. |
| `research/_staging/reviews/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates-proof-review-postconv-proof-review-20260523144712217.md` | `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md` | `hold_for_conversion_qa` | Revise or supersede the staged draft to match the restored chunk and current metadata, then run targeted field-level conversion QA against the source image for entry 513 child name and maternal surname, entry 514 father field, and entry 515 father/declarant surname. After those readings are settled, review separate atomic claims before any canonical person or relationship promotion. |
| `research/_staging/reviews/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates-proof-review-postconv-proof-review-20260523165754854.md` | `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md` | `hold` | Keep the staged draft on hold. The next action is targeted conversion QA against the restored source image, starting with the chunk citation mismatch and then resolving these fields in order: entry 513 child name/surname and mother surname; entry 514 child name and father field; entry 515 child name and father/declarant surname. Do not promote, merge, rename, or attach any canonical person or relationship from this staged draft until those field-level readings are resolved. |

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
