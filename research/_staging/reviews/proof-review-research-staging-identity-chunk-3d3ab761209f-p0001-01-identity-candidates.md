---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity/CHUNK-3d3ab761209f-P0001-01-identity-candidates.md
staged_draft: research/_staging/identity/CHUNK-3d3ab761209f-P0001-01-identity-candidates.md
reviewer: postconv-proof-review-20260522021007491
review_date: 2026-05-22
canonical_readiness: revise
---

# Proof Review: CHUNK-3d3ab761209f-P0001-01 Identity Candidates

## Blockers

- Revise before canonical promotion: the staged draft cites chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, but that file's front matter/transcription carries a different chunk id/hash and does not support the staged identity table. The matching chunk is `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md`.
- Revise before canonical promotion: the converted file currently at `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md` does not agree with the staged identity table for the principal child names, record 514 street/witnesses, or record 515 identities. This creates a provenance conflict even though the restored source image and matching chunk support most staged candidates.
- Hold or separately re-check image-sensitive readings before canonical use: record 514 `Benjamin Utiera`, record 514 `Calle Sanegueso`, and the record 515 `Neira=emendado=vale` note. The image is now available, but the handwriting and competing conversion outputs require a focused transcription review rather than silent normalization.
- Do not create or merge canonical people from this draft alone. The register supports registration-scoped identities, but this review did not compare the candidates against existing canonical profiles or corroborating records.
- Record 514 has no father candidate in this identity draft, which is appropriate; the matching chunk reads `Nombre del padre. Se ignora`. Do not infer a father from later context without stronger evidence.

## Scores

- source_quality_score: 0.86
- conversion_confidence_score: 0.62
- evidence_quantity_score: 0.78
- agreement_score: 0.64
- identity_confidence_score: 0.70
- claim_probability: 0.77
- relevance_level: high
- relevance_confidence: 0.92
- canonical_readiness: revise

## Candidate Review

| Candidate id | Judgment | Claim probability | Canonical readiness | Notes |
| --- | --- | ---: | --- | --- |
| id-513-child | supported_with_citation_revision | 0.86 | revise | The restored image and matching chunk support child name `Pulgar Amagada / Jose Luis`, male, born 26 June 1889 at Calle Colon. The cited converted file does not support this reading, so fix source linkage before promotion. |
| id-513-father | supported_with_identity_caution | 0.84 | revise | The image and matching chunk support `Jose del Carmen Pulgar`; the compareciente field supports `Jose del C. Pulgar / Padre`, age 47, agriculturist, Calle Colon. Treat the abbreviation as same-entry support only. |
| id-513-mother | supported_with_identity_caution | 0.82 | revise | The image and matching chunk support `Juana de Dios Amagada de Pulgar`, Chilean, domiciled Calle Colon. Do not resolve birth surname or broader profile identity from the married-name form alone. |
| id-514-child | supported_with_image_sensitive_place | 0.78 | revise | The matching chunk supports `Riquelme Aviles / Juan Bautista`, male, born 23 June 1889. The source image appears consistent with the staged child identity, but the street `Calle Sanegueso` remains transcription-sensitive because of competing conversion text. |
| id-514-mother | supported_with_identity_caution | 0.80 | revise | The matching chunk supports `Mercedes Riquelme`, mother and compareciente, Chilean seamstress, age 21, domiciled Calle Sanegueso. Same-entry mother/declarant identity is likely but not a broader canonical merge proof. |
| id-514-witness-1 | hold_transcription_check | 0.56 | hold | The matching chunk reads `Benjamin Utiera`; the restored image shows a plausible but difficult surname. Keep this as a witness lead only until focused handwriting review resolves the surname. |
| id-514-witness-2 | supported_low_relevance | 0.70 | hold | The matching chunk reads `Ignacio Soto` as a witness-only mention. The cited converted file has a conflicting witness reading, and there is no age, residence, occupation, or relationship context. |
| id-515-child | supported_with_emendation_caution | 0.78 | revise | The matching chunk and visible lower portion of the image support `Neira Ulloa / Laura de la Cruz`, female, born 18 July 1889 at Calle Santiago. The `Neira=emendado=vale` note should be retained as source uncertainty until rechecked. |
| id-515-father | supported_with_identity_caution | 0.80 | revise | The matching chunk supports `Pedro Pablo Neira`, father and compareciente, Chilean agriculturist, age 26, domiciled Santiago. Same-entry father/declarant identity is likely but not a broader merge proof. |
| id-515-mother | supported_limited_detail | 0.78 | revise | The matching chunk supports `Carmen Ulloa`, Chilean, domiciled Santiago. Distinguishing detail is limited, so any profile creation or merge needs corroboration. |
| id-515-witnesses | supported_low_relevance | 0.66 | hold | The matching chunk reads `Rosendo Ramirez H.` and `Santiago Perez`; the visible image area is low-confidence enough that these should remain witness-only leads pending focused image review. |

## Evidence Strengths

- The restored raw source image is now present at the staged source path and visibly corresponds to page 172 of an 1889 Los Anjeles/La Laja birth register with entries 513, 514, and 515.
- The chunk file that actually carries `chunk_id: CHUNK-3d3ab761209f-P0001-01` directly supports the staged identity candidates for the three child identities, their named parents where declared, and the declarant roles.
- The source type is a civil birth register, a strong primary source for birth-event facts and for names of declared parents, declarants, and witnesses within the registration entry.
- The staged draft correctly avoids creating a father candidate for record 514, where the matching chunk reads `Se ignora`.
- The staged draft preserves uncertainty for Chilean surname parsing, same-entry abbreviation, married-name form, witness-only mentions, record 514 witness/street readings, and the record 515 emendation note.

## Review Judgment

The staged identity candidates are relevant and mostly probable as registration-scoped leads when checked against the restored source image and the matching `CHUNK-3d3ab761209f-P0001-01` chunk. The main risk is not that the identity draft invented unsupported people; it is that the draft's cited verification path and the current converted file conflict with the draft and with the matching chunk.

Canonical readiness is `revise`. Repair the chunk/converted-file provenance and rerun or document a focused image transcription check before promoting any identity, relationship, or place-normalized claim. Witness-only identities remain low-relevance holds unless later records add identifying context.

## Next Action

Revise the staged draft or its source reference metadata so it cites the chunk file that actually carries `CHUNK-3d3ab761209f-P0001-01`, and resolve the converted-file mismatch. Then perform targeted image checks for `Benjamin Utiera`, `Ignacio Soto`, `Calle Sanegueso`, the `Neira=emendado=vale` note, and record 515 witnesses before canonical promotion.
