---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity/CHUNK-3d3ab761209f-P0001-01-identity-candidates.md
staged_draft: research/_staging/identity/CHUNK-3d3ab761209f-P0001-01-identity-candidates.md
reviewer: postconv-proof-review-20260522010432120
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: CHUNK-3d3ab761209f-P0001-01 Identity Candidates

## Blockers

- Raw source image is not available at the path cited by the staged draft and conversion: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`. The `raw/sources` directory currently contains only `.gitkeep`.
- No page-image cache is available at the manifest path `raw/codex-conversion-jobs/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513/page-images/page-0001.png`.
- Because the visible source image is absent, this review can verify candidates only against the converted Markdown and assigned chunk, not independently against handwriting, marginal text, emendation text, or crop completeness.
- Hold canonical person creation or merge for all candidates. The birth-register rows support registration-scoped identities, but this staged draft does not compare these people against existing canonical profiles or other corroborating records.
- Hold image-sensitive readings before any canonical use: record 514 witness `Benjamin Utiera`, record 514 street `Calle Sanegueso`, and record 515 surname/emendation note `Neira=emendado=vale`.
- Do not infer a father identity for record 514. The conversion states `Nombre del padre. Se ignora`; the mother and child identity candidates should remain scoped to this entry.

## Scores

- source_quality_score: 0.82
- conversion_confidence_score: 0.74
- evidence_quantity_score: 0.76
- agreement_score: 0.96
- identity_confidence_score: 0.62
- claim_probability: 0.79
- relevance_level: high
- relevance_confidence: 0.92
- canonical_readiness: hold

## Candidate Review

| Candidate id | Judgment | Claim probability | Canonical readiness | Notes |
| --- | --- | ---: | --- | --- |
| id-513-child | supported_from_conversion | 0.86 | hold | The converted file and chunk directly support `Pulgar Amagada / José Luis`, male, born 26 June 1889 at Calle Colon. Name-order interpretation under Chilean surname convention should remain a review note, not an unsupported merge rule. |
| id-513-father | supported_from_conversion_with_identity_caution | 0.82 | hold | The father field supports `José del Carmen Pulgar`; the compareciente field supports `José del C. Pulgar / Padre`, age 47, agriculturist, Calle Colon. Treat the abbreviation as same-entry support, not independent proof of a broader identity match. |
| id-513-mother | supported_from_conversion_with_identity_caution | 0.82 | hold | The conversion supports `Juana de Dios Amagada de Pulgar`, Chilean, domiciled Calle Colon. The married-name form should not be used alone to resolve a birth name or merge profile. |
| id-514-child | supported_from_conversion_with_image_hold | 0.80 | hold | The conversion supports `Riquelme Aviles / Juan Bautista`, male, born 23 June 1889. `Calle Sanegueso` is present but image-sensitive because the conversion flags it as unusual. |
| id-514-mother | supported_from_conversion_with_identity_caution | 0.82 | hold | The conversion supports `Mercedes Riquelme`, mother and compareciente, Chilean seamstress, age 21, domiciled Calle Sanegueso. Same-entry mother/declarant identity is likely but still should not become a canonical merge without profile comparison. |
| id-514-witness-1 | hold_image_check | 0.58 | hold | The conversion gives `Benjamin Utiera`, but explicitly says the surname is difficult to read. Do not create or merge a witness identity until the source image is restored and checked. |
| id-514-witness-2 | supported_low_relevance | 0.72 | hold | `Ignacio Soto` is supported by the conversion as a witness-only mention. There is no age, residence, occupation, or relationship context, so identity confidence is limited. |
| id-515-child | supported_from_conversion_with_image_hold | 0.80 | hold | The conversion supports `Neira Ulloa / Laura de la Cruz`, female, born 18 July 1889 at Calle Santiago. The `Neira=emendado=vale` annotation must be checked against the image before surname normalization or profile creation. |
| id-515-father | supported_from_conversion_with_identity_caution | 0.82 | hold | The conversion supports `Pedro Pablo Neira`, father and compareciente, Chilean agriculturist, age 26, domiciled Santiago. Same-entry father/declarant identity is likely but not a broader merge proof. |
| id-515-mother | supported_from_conversion_with_identity_caution | 0.80 | hold | The conversion supports `Carmen Ulloa`, Chilean, domiciled Santiago. Distinguishing detail is limited, so profile creation or merge needs corroboration. |
| id-515-witnesses | supported_low_relevance | 0.70 | hold | `Rosendo Ramirez H.` and `Santiago Perez` are supported as witness-only mentions in the conversion. No age, residence, occupation, or relationship context is supplied. |

## Evidence Strengths

- The staged identity-candidate table matches the converted file and assigned chunk for entries 513, 514, and 515; no mismatch was found in the cited literal-support snippets.
- The source type is a civil birth register, a strong primary source for birth-event facts and for names of declared parents, declarants, and witnesses within the registration entry.
- The draft appropriately preserves uncertainty for Chilean surname parsing, same-entry abbreviation, married-name form, unknown father in record 514, the difficult witness surname, and the record 515 emendation note.
- The draft does not promote record 514 father identity, which is correct because the father field is transcribed as `Se ignora`.

## Review Judgment

The identity candidates are mostly high-probability staged leads when limited to the converted Markdown and chunk. Child, parent, declarant, and witness names are represented consistently with the available transcription, and the core birth-register context is relevant to genealogical identity work.

Canonical readiness remains `hold`. The source/page image is unavailable, so image-sensitive readings cannot be independently verified. More importantly, person creation or reconciliation requires comparison against canonical profiles or corroborating records, which is outside the evidence supplied by this staged draft.

## Next Action

Restore or regenerate the page image, then re-check `Benjamin Utiera`, `Calle Sanegueso`, and `Neira=emendado=vale` against the visible source. After image review, route child and parent candidates through identity reconciliation before creating or merging canonical person pages; keep witness-only identities as low-priority leads unless corroborating context appears.
