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
- Matched family terms: Arriagada, Pulgar
- Narrative cues: birth
- Evidence priority: `-49` (family_relevance:high, qc:pass, matched_terms, person_linked_narrative_context, proof_review_revision)


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-identity-candidates-proof-review-postconv-proof-review-20260523122056350.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-identity-candidates-20260522150707183.md` | `hold` | Revise the staged identity analysis and source packet to reflect that the source image is now available and supports the Pulgar/Arriagada row. Keep canonical readiness at hold until conversion QA corrects or supersedes the converted Markdown entry-172 transcript and records whether the father field has no suffix, a clear `S.`, or an uncertain suffix. |
| `research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-identity-candidates-proof-review-postconv-proof-review-20260523182729229.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-identity-candidates-20260522150707183.md` | `hold_for_conversion_qa` | Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the page image and reconcile or supersede `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`. The QA result should explicitly decide whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form. After that, rerun proof review for the individual birth facts and child-parent relationships before any canonical promotion or parent-candidate merge. |
| `research/_staging/reviews/proof-review-rel-chunk-b8f4f0490a36-p0001-01-004-child-father-postconv-proof-review-20260522120356549.md` | `research/_staging/relationships/chunk-b8f4f0490a36-p0001-01-004-child-father.md` | `hold_for_conversion_qa` | Run or await targeted conversion QA on entry 172's father-name line. If QA confirms the visible source supports `Jose del Carmen Pulgar` without the suffix, the relationship can be reconsidered for scoped promotion as a child-father relationship only, separate from any father-identity merge or attribute claims. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-b8f4f0490a36-p0001-01-001-child-birth-name-postconv-proof-review-20260522112919722.md` | `research/_staging/claims/chunk-b8f4f0490a36-p0001-01-001-child-birth-name.md` | `hold` | Keep the claim on hold for conversion QA. Restore or locate the referenced page image, reread entry 172 against the image, and then rerun proof review or update this review status before any canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-b8f4f0490a36-p0001-01-001-child-birth-name-postconv-proof-review-20260522222759757.md` | `research/_staging/claims/chunk-b8f4f0490a36-p0001-01-001-child-birth-name.md` | `hold_for_conversion_qa` | Hold for conversion QA. Reconcile or regenerate the referenced converted Markdown/page Markdown so entry 172 matches the image-reread Pulgar/Arriagada row, or restore the source/page image at the manifest path for direct verification. After that, rerun proof review for canonical readiness. |
| `research/_staging/reviews/proof-review-research-staging-claims-chunk-b8f4f0490a36-p0001-01-006-father-attributes-postconv-proof-review-20260522123003255.md` | `research/_staging/claims/chunk-b8f4f0490a36-p0001-01-006-father-attributes.md` | `hold_for_conversion_qa` | Hold this combined father-attributes claim for conversion QA. After QA, either promote a corrected combined claim if the father name and residence spelling are resolved, or split the supported attributes into narrower claims for `Chileno` and `Empleado` while keeping suffix and residence questions in review. |
| `research/_staging/reviews/proof-review-research-staging-identity-analysis-identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-proof-review-20260523121840908.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict.md` | `hold` | Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the present source image. Correct or supersede the assigned converted Markdown so entry 172 matches the visible Pulgar/Arriagada row, and explicitly mark the father field as `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar [?]` with any suffix uncertainty documented. After that, rerun proof review for the child birth-name, child-mother, child-father, birth-event, and parent-attribute claims before any further canonical promotion or merge. |
| `research/_staging/reviews/proof-review-research-staging-identity-analysis-identity-analysis-chunk-b8f4f0490a36-p0001-01-identity-candidates-postconv-proof-review-20260523122309853.md` | `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-identity-candidates.md` | `hold` | Revise the staged identity analysis and source packet to reflect the current review state: the source image is available and supports the Pulgar/Arriagada row, while the converted Markdown currently gives a conflicting Gomez/de la Cruz row. Then run targeted conversion QA to reconcile or retire the conflicting converted transcript and record whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an explicitly uncertain form. Keep all dependent identity and relationship claims on hold until that QA is complete. |

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
