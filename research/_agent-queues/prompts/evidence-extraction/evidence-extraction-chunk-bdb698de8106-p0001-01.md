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
| `research/_staging/reviews/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916-proof-review-20260526220809497.md` | `research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md` | `hold` | Run targeted conversion QA against the source image for entry 513 child name/sex, mother surname, father/declarant profession, and entry 515 child-name/father-declarant fields. After QA, rerun proof review on atomic claims and relationship candidates before any canonical edit. |
| `research/_staging/reviews/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916-proof-review.md` | `research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md` | `hold` | Run targeted conversion QA against the source image for entry 513 child name/sex, mother surname, father/declarant occupation, and entry 515 child/father-declarant fields. After QA, rerun proof review on atomic claims and relationship candidates before any canonical edit. |
| `research/_staging/reviews/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-proof-review-20260526215418546.md` | `research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md` | `hold` | Run targeted conversion QA against the original image for entry 513 child full name, sex, birth details, father/declarant details, and mother full name, plus entry 515 child-name and father/declarant surname only enough to prevent row spillover. After that correction or uncertainty note exists, rerun proof review on atomic identity and relationship candidates before any canonical promotion. |
| `research/_staging/reviews/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-proof-review-20260526215839027.md` | `research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md` | `hold` | Run targeted conversion QA against the original page image for entry 513 child full name, sex, birth date/time/place, father/declarant details, and mother full name. Also reconcile entry 515 child-name and father/declarant surname only enough to prevent row spillover. After QA produces a stable transcription or explicit uncertainty markers, rerun proof review on each atomic claim and relationship candidate before any canonical promotion. |
| `research/_staging/reviews/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant-proof-review.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md` | `hold_for_conversion_qa` | Keep the staged claim on hold pending conversion QA for entry 513. After QA resolves the row-level transcription conflict, this specific declarant appearance claim can be reconsidered for promotion with a high probability score if the declarant column remains unchanged. |
| `research/_staging/reviews/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name-proof-review.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name.md` | `hold_for_conversion_qa` | Hold this claim for targeted conversion QA on entry 515. The QA task should reconcile the partial source image against the converted `Rosa Elvira del Carmen` reading without replacing the transcription from inference alone. |
| `research/_staging/reviews/conversion-review-note-CHUNK-bdb698de8106-P0001-01-current-worker-revision-20260526-165034575.md` | `` | `` |  type: conversion_review_note status: draft task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01 worker: postconv-evidence-extraction-20260526165034575 source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md |
| `research/_staging/reviews/conversion-review-note-CHUNK-bdb698de8106-P0001-01-current-worker-revision-20260526-171453486.md` | `` | `` |  type: conversion_review_note status: draft task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01 worker: postconv-evidence-extraction-20260526171453486 source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526171453486.md |

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
