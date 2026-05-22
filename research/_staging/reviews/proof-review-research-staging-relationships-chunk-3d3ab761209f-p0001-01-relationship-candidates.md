---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/relationships/CHUNK-3d3ab761209f-P0001-01-relationship-candidates.md
staged_draft: research/_staging/relationships/CHUNK-3d3ab761209f-P0001-01-relationship-candidates.md
reviewer: postconv-proof-review-20260522010228190
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: CHUNK-3d3ab761209f-P0001-01 Relationship Candidates

## Blockers

- Raw source image is not available at the path cited by the staged draft and conversion: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`. The `raw/sources` directory currently contains only `.gitkeep`.
- No page-image cache is available in the cited conversion job directory; it contains `page-markdown`, `work-orders`, `manifest.json`, and `README.md`, but no `page-images` directory.
- Because the visible source image is absent, the relationship candidates can be checked only against the converted Markdown and assigned chunk, not independently against handwriting, marginal text, crop completeness, or the record 515 `Neira=emendado= vale=` note.
- Hold canonical identity merges. Each parent-child relationship is directly stated within one civil birth-register entry, but the staged draft does not establish whether the named parent or child should be merged into any existing canonical person profile.
- Record 513 father support should rely on the full father field `José del Carmen Pulgar`; the compareciente abbreviation `José del C. Pulgar` is consistent same-entry support but should not be treated as independent identity proof.
- Record 514's father field says `Se ignora`; the staged draft correctly excludes a father relationship candidate. Do not infer or create a father relationship from this entry.

## Scores

- source_quality_score: 0.82
- conversion_confidence_score: 0.74
- evidence_quantity_score: 0.76
- agreement_score: 0.96
- identity_confidence_score: 0.64
- claim_probability: 0.82
- relevance_level: high
- relevance_confidence: 0.92
- canonical_readiness: hold

## Relationship Review

| Candidate id | Judgment | Claim probability | Canonical readiness | Notes |
| --- | --- | ---: | --- | --- |
| rel-513-father | supported_from_conversion | 0.84 | hold | The converted file and chunk directly list child `Pulgar Amagada / José Luis` and father `José del Carmen Pulgar`. The compareciente `José del C. Pulgar / Padre` is useful same-entry context but needs identity review before canonical merging. |
| rel-513-mother | supported_from_conversion | 0.84 | hold | The converted file and chunk directly list child `Pulgar Amagada / José Luis` and mother `Juana de Dios Amagada de Pulgar`. The married-surname form should not be used to infer a birth surname or profile merge without corroboration. |
| rel-514-mother | supported_from_conversion | 0.86 | hold | The converted file and chunk directly list child `Riquelme Aviles / Juan Bautista` and mother `Mercedes Riquelme`, with `Mercedes Riquelme / Madre` as compareciente. The father field is `Se ignora`, which supports excluding any father relationship. |
| rel-515-father | supported_from_conversion_with_image_hold | 0.82 | hold | The converted file and chunk directly list child `Neira Ulloa / Laura de la Cruz` and father `Pedro Pablo Neira`, with `Pedro Pablo Neira / Padre` as compareciente. The `Neira` emendation note should be checked against the image before canonical surname normalization or profile merging. |
| rel-515-mother | supported_from_conversion | 0.84 | hold | The converted file and chunk directly list child `Neira Ulloa / Laura de la Cruz` and mother `Carmen Ulloa`. Identity merge remains separate from the literal parent-child statement. |

## Evidence Strengths

- The staged relationship candidates match the available converted file and assigned chunk. No mismatch was found between the cited literal-support snippets and the conversion text.
- The source type is a civil birth register, a strong primary source for registration-scoped parent-child relationships when parents were declared in the entry.
- Each proposed relationship is supported by a parent field in the same birth-registration row as the named child; the draft does not rely only on surname order or later inference.
- The draft correctly treats record 514's `Se ignora` father field as a non-relationship note rather than creating an unsupported relationship.
- The draft preserves relevant uncertainty for abbreviation, married-name form, unknown father, and the record 515 emendation note.

## Review Judgment

The five parent-child relationship candidates are high-probability staged relationships based on the converted Markdown and chunk. They are literal, registration-scoped relationships rather than extended kinship inferences. No conflict was found inside the reviewed conversion/chunk.

Canonical readiness remains `hold` because image-level verification cannot be completed in the current workspace and identity reconciliation has not been performed. These candidates should not be promoted to canonical relationship or person pages until the source/page image is restored or regenerated and the parent/child identities are reviewed against the relevant canonical profiles.

## Next Action

Restore or regenerate the page image, then re-check the record 515 `Neira` emendation and confirm the relevant parent/child name fields against the image. After image review, route the five direct parent-child relationships through identity review before any canonical promotion.
