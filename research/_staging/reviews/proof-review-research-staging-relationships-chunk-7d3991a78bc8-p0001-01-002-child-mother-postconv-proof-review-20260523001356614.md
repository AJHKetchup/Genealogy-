---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/relationships/chunk-7d3991a78bc8-p0001-01-002-child-mother.md
staged_draft: research/_staging/relationships/chunk-7d3991a78bc8-p0001-01-002-child-mother.md
reviewer: postconv-proof-review-20260523001356614
review_date: 2026-05-23
canonical_readiness: revise
---

# Proof Review: Entry 172 Child-Mother Relationship

## Blockers

- The exact staged relationship, `Jose Miguel` child of `Amelia de la Maza`, is not supported by the visible source image for register page 58, entry 172.
- The assigned converted file and assigned chunk transcribe entry 172 as `Jose Miguel`, mother `Amelia de la Maza`, but the source image shows entry 172 as a different child-mother row: child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`.
- This is a material source/transcription conflict, not a minor normalization issue. The draft should not be promoted or merged into canonical relationship pages.
- The source packet already flags `conversion_confidence: low_due_to_conflicting_derivatives` and recommends `hold_for_conversion_qa`; the image check confirms that the Bunster/de la Maza derivative is not reliable for this entry.
- No independent corroborating source was reviewed by rule. The only source-visible evidence reviewed points away from the staged endpoints.

## Scores

| metric | score | note |
| --- | ---: | --- |
| source_quality_score | 0.92 | Civil birth registration is a strong direct source type for a child-mother relationship when the row is correctly read. |
| conversion_confidence_score | 0.05 | The assigned derivative conflicts with the visible source image for entry 172. |
| evidence_quantity_score | 0.30 | One source image and its disputed derivatives were reviewed; no external corroboration was used. |
| agreement_score | 0.05 | The source image disagrees with the staged draft, assigned chunk, and converted Markdown on the endpoint identities. |
| identity_confidence_score | 0.05 | The staged child and mother identities do not match the source-visible entry 172 identities. |
| claim_probability | 0.02 | Probability applies to the exact staged claim `Jose Miguel` child of `Amelia de la Maza`; the reviewed image does not support it. |
| relevance_level | direct_negative | The reviewed source image is directly relevant to the claimed relationship but contradicts it. |
| relevance_confidence | 0.98 | The image is the referenced source for page 1/register page 58/entry 172. |
| canonical_readiness | revise | Retire or revise this staged candidate after conversion QA reconciles the derivative transcript with the image-visible row. |

## Evidence Strengths

- The staged draft, source packet, assigned chunk, and converted Markdown are internally consistent with one another for the derivative reading `Jose Miguel` and `Amelia de la Maza`.
- The draft correctly carried a low-confidence hold recommendation instead of asking for direct canonical promotion.
- The source image is available at the referenced path and entry 172 is legible enough to test the staged endpoints against the visible register row.

## Review Judgment

The staged child-mother relationship is not canonically ready. The source image supports a child-mother relationship for entry 172, but not the one in this staged draft. The visible row identifies the child as `Jose del Carmen Segundo Pulgar Arriagada` and the mother as `Juana Arriagada de Pulgar`; it does not support `Jose Miguel` as child of `Amelia de la Maza`.

Treat the assigned converted Markdown and chunk as superseded or requiring conversion QA for this entry. Do not use this staged draft as a relationship source for `Jose Miguel` or `Amelia de la Maza`.

## Next Action

Send the assigned converted file and chunk through targeted conversion QA for entry 172, page 58. Revise or retire this staged candidate so it no longer asserts the unsupported `Jose Miguel` to `Amelia de la Maza` relationship, then rerun proof review only after the derivative transcript matches the source-visible entry.
