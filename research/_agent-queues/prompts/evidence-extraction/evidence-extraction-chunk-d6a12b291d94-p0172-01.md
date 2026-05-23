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
- Family relevance: `high`
- Matched family terms: Pulgar
- Narrative cues: birth, witness
- Evidence priority: `122` (family_relevance:high, qc:pass, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-514-child-name-sex-proof-review.md` | `research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-514-child-name-sex.md` | `hold` | Hold this staged claim. Perform conversion QA on entry 514 and the missing chunk path. If the visible source reading is confirmed, create a revised claim for entry 514 using the supported child name and sex; do not promote the current `Rigoberto Juan Bautista` claim. |
| `research/_staging/reviews/identity-analysis-conflict-stage-chunk-d6a12b291d94-p0172-01-qa-candidates-proof-review.md` | `research/_staging/identity-analysis/identity-analysis-conflict-stage-chunk-d6a12b291d94-p0172-01-qa-candidates-postconv-identity-analysis-20260523063958802.md` | `hold` | Keep the staged identity analysis on hold and route the underlying page through conversion QA. The next reviewer should obtain or generate a complete source view for page 172, then perform targeted rereads of entry 515's lower row and entry 513's maternal surname. After those two items are resolved, entries 513 and 514 can be reviewed as individual child, parent, informant, and relationship claims; no canonical Dario-line attachment should be made from this draft. |
| `research/_staging/reviews/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates-proof-review-postconv-proof-review-20260523144712217.md` | `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md` | `hold_for_conversion_qa` | Revise or supersede the staged draft to match the restored chunk and current metadata, then run targeted field-level conversion QA against the source image for entry 513 child name and maternal surname, entry 514 father field, and entry 515 father/declarant surname. After those readings are settled, review separate atomic claims before any canonical person or relationship promotion. |
| `research/_staging/reviews/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates-proof-review-postconv-proof-review-20260523190116852.md` | `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md` | `hold` | Keep the staged draft and all person/relationship claims from page 172 on `hold_for_conversion_qa`. The next action is targeted conversion QA against the source image for entries 513-515, starting with the chunk/version mismatch (`CHUNK-4127185dc97c-P0172-01` versus `CHUNK-d6a12b291d94-P0172-01`). Then verify entry 513 child name and maternal surname, entry 514 father field, and entry 515 surname/emendation before any proof review attempts canonical identity linkage. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-date-time-postconv-proof-review-20260522154003468.md` | `research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-date-time.md` | `hold` | Hold for conversion QA. Reconcile the source image, converted file, and missing/stale chunk reference for entry 513, specifically the child identity and the birth time phrase. If the Tulio row is intended, revise the claim to the correct entry number and only use wording visibly supported by that row or by a corrected conversion. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-place-postconv-proof-review-20260522154231372.md` | `research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-place.md` | `hold` | Hold for conversion QA or revise after targeted image review. Reconcile entry 513's child name and the missing chunk reference against the source image, then create or update the staged claim so the stable `Calle Colon` birth-place evidence is attached only to the confirmed entry-513 subject. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-child-name-sex-postconv-proof-review-20260522154503628.md` | `research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-child-name-sex.md` | `hold` | Hold for targeted conversion QA. Reconcile entry 513's child-name field and the missing chunk reference directly against the source image; preserve `Sexo. Masculino` as supported, but do not create or normalize a canonical child identity from `Tulio Cesar Luis Jose`, `Isolina del Carmen Jose`, or any alternate reading until the visible-source transcription is resolved. |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-declarant-postconv-proof-review-20260522154732359.md` | `research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-declarant.md` | `revise` | Revise the staged claim or its support metadata to cite an available reviewed chunk or source-image-backed evidence note, preserving the visible-source wording `José del C. Pulgar` and the separate father expansion `José del Carmen Pulgar`. After provenance is corrected, the declarant claim is a strong candidate for promotion. |

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
