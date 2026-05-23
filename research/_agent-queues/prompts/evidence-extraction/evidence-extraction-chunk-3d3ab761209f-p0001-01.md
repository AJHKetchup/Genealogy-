# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md`
- Converted source: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk manifest: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/manifest.json`
- Original source: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Page range: 1-1
- Staging area: `research/_staging`
- Family relevance: `high`
- Matched family terms: Pulgar
- Narrative cues: birth, witness
- Evidence priority: `-49` (family_relevance:high, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/proof-review-CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-registration-date-postconv-proof-review-20260522151013138.md` | `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-registration-date.md` | `hold` | Hold this claim for conversion QA/provenance cleanup. After the source packet and staged draft point to the correct current chunk path and chunk id, this registration-date claim can likely be promoted with high confidence, provided the corrected derivative layer still preserves the visible date reading. |
| `research/_staging/reviews/proof-review-claim-chunk-3d3ab761209f-p0001-01-514-registration-date-postconv-proof-review-20260522153441992.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-514-registration-date.md` | `hold` | Keep the claim held pending conversion QA for entry 514. After the page/row transcription is reconciled against the source image, the registration-date claim can be promoted or restaged as `22 July 1889` if the date cell remains confirmed. |
| `research/_staging/reviews/proof-review-REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents-postconv-proof-review-20260522112159176.md` | `research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md` | `not_ready` | Hold this staged relationship and run conversion QA against the restored page image for entry 513. Reconcile the child name, sex, surname sequence, father field, and mother field from the visible source; then revise or replace this staged relationship from the corrected transcription. Preserve the boundary between verification and transcription: do not change the child to a different reading unless the visible source supports that reading. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-3d3ab761209f-p0001-01-atomic-claims-postconv-proof-review-20260522205428497.md` | `research/_staging/claims/CHUNK-3d3ab761209f-P0001-01-atomic-claims.md` | `hold` | Keep this staged atomic-claims draft on hold. Request targeted conversion QA/crops for entry 513 child name, birth date/time, and mother surname; entry 514 street and witness names; and the lower part of entry 515, especially the mother field. After QA, revise the staged claims before any promotion, and send relationship/identity conclusions through separate review rather than deriving them from this claim draft. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-birth-date-time-postconv-proof-review-20260522062707498.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-birth-date-time.md` | `hold` | Keep this claim on hold for conversion QA. Reconcile the source image, assigned chunk, and assembled converted Markdown for entry 513, then rerun proof review or revise the staged claim from the corrected transcription before any canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-birth-place-postconv-proof-review-20260522063058226.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-birth-place.md` | `hold` | Keep this claim on hold until conversion QA reconciles entry 513 across the source image, assigned chunk, and assembled converted Markdown. After that QA pass, this birth-place claim can likely be promoted or revised with the same literal place spelling if the corrected entry still identifies the subject as Jose Luis Pulgar Amagada. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-child-name-sex-postconv-proof-review-20260522063230567.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-child-name-sex.md` | `hold` | Keep this claim on hold for conversion QA. Reconcile entry 513's child-name field against the source image and corrected transcription, then rerun proof review or revise the staged claim before any canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-father-name-postconv-proof-review-20260522063401351.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-father-name.md` | `hold` | Keep this claim on hold for conversion QA. Reconcile entry 513 in the assembled converted Markdown against the source image and assigned chunk, then rerun proof review or revise the staged claim before canonical promotion. |

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
