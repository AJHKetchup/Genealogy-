---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260523194714286
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
referenced_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_at: 2026-05-23
source_quality_score: 0.88
conversion_confidence_score: 0.32
evidence_quantity_score: 0.58
agreement_score: 0.34
identity_confidence_score: 0.30
claim_probability: 0.41
relevance_level: direct
relevance_confidence: 0.97
canonical_readiness: hold
---

# Proof Review: Page 172 Identity Candidates

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md`.
- Review scope was limited to the staged draft, referenced source packet, referenced converted file, restored referenced chunk, source page image, and directly relevant local QA notes already cited by this evidence cluster. No external research was performed.
- The staged draft should remain on hold. It correctly treats page 172 entries 513-515 as identity-risk candidates rather than promotion-ready people, but some of its internal support text is stale against the currently restored chunk and converted file.
- Citation/version mismatch remains material: the source packet and staged draft cite `CHUNK-4127185dc97c-P0172-01`, while the restored chunk file now declares `CHUNK-d6a12b291d94-P0172-01` and converted SHA-256 `d6a12b...`.
- Entry 513 has unresolved child-name and maternal-surname risk. The current converted/chunk text reads child `Tulio Cesar Luis José`, father `José del Carmen Pulgar`, mother `Juana de Dios Amagada de Pulgar`, and declarant `José del C. Pulgar`; the source image supports a Pulgar-family row but the child given-name line and maternal surname remain difficult enough to block identity promotion.
- Entry 514 has a relationship blocker. The current converted/chunk text reads father `Belisario Riquelme`, but the source image and local QA notes appear closer to `Se ignora`; the same row supports mother/declarant `Mercedes Riquelme`, but not a promoted named-father relationship.
- Entry 515 has a surname/identity blocker. The current converted/chunk text reads father/declarant `Pedro Pablo Leiva`, child `Rosa Elvira del Carmen`, and mother `Carmen Fuentes`; the source image shows strong competing `Neira` evidence, including `Pedro Pablo Neira` and the right-margin note `Neira=emendado= / vale=`.
- The staged draft discusses older converted/chunk readings that are not present in the restored current chunk, including `Isolina del Carmen / José` and `Juana de Dios Amador de Pulgar`. Treat those as stale verification context, not current literal support.
- No entry on this page should be merged into or used as a lineage bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, Jose del Carmen Pulgar, Juana de Dios Amagada de Pulgar, or Juana Arriagada de Pulgar from this staged draft alone.

## Evidence Strengths

- Source reliability is high in kind: the underlying source is a civil birth register page image with visible register page 172 and entries 513, 514, and 515.
- Page and entry scope are well supported: the source image, converted file, chunk, and source packet agree that the page is a birth register page for Los Angeles/La Laja, Chile, in 1889, and that entries 513-515 are present.
- Entry 513 has partial agreement for a Pulgar-related row: the source image and current converted/chunk text support `José del Carmen Pulgar` as father/declarant candidate and `Calle Colon` context, but not enough for final identity linkage.
- Entry 514 has partial agreement for `Mercedes Riquelme` as mother/declarant and `Calle San Joaquin` context. The father field remains the critical conflict.
- Entry 515 is directly relevant to the staged identity draft because the source image visibly challenges the current converted `Leiva` reading with `Neira` evidence.
- The staged draft's overall hold recommendation is proportionate to the evidence conflicts and avoids impermissible normalization by family context.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong source type, though this page has difficult handwriting/cropping in relevant fields. |
| conversion_confidence_score | 0.32 | Converted file and chunk are readable but conflict with the visible image and QA notes on material identity and relationship fields. |
| evidence_quantity_score | 0.58 | One source page plus source packet, derivative files, and local QA notes give enough context to identify conflicts, not enough to prove final identities. |
| agreement_score | 0.34 | Page/entry frame agrees; names, surnames, and father fields have material disagreements. |
| identity_confidence_score | 0.30 | Individual identity claims remain low confidence; page-level identity is stronger than person-level identity. |
| claim_probability | 0.41 | The most probable claim is that the draft is a hold-for-QA identity-risk item, not a promotable identity proof. |
| relevance_level | direct | The reviewed evidence is the exact page and staged identity analysis assigned. |
| relevance_confidence | 0.97 | The source packet, converted file, chunk, and image all point to page 172 entries 513-515. |
| canonical_readiness | hold | Do not promote or merge. Resolve conversion/citation conflicts first. |

## Item Findings

| Item | Probability | Finding |
| --- | ---: | --- |
| Overall staged identity draft | 0.72 | The draft's `hold_for_conversion_qa` posture is supported, though some cited support text is stale against the restored current chunk. |
| Entry 513 Pulgar-family row | 0.64 | A Pulgar-related row with father/declarant `José del Carmen Pulgar` is plausible, but the child and mother readings are not settled. |
| Entry 513 canonical linkage to Jose/Juana pages | 0.18 | Not ready; same-name and surname-context evidence is insufficient without field-level source QA. |
| Entry 514 named father `Belisario Riquelme` | 0.12 | The image appears closer to `Se ignora`, so the named-father claim should be held/revised after conversion QA. |
| Entry 514 mother/declarant `Mercedes Riquelme` | 0.78 | This is the strongest row-level identity element, but still should remain staged until the row is reconciled. |
| Entry 515 `Leiva` identity readings | 0.16 | The image has strong `Neira` evidence, so the converted `Leiva` readings should not be promoted. |
| Entry 515 `Neira` competing hypothesis | 0.70 | `Neira` is visibly plausible, but this review does not rewrite the source transcription or promote a corrected identity. |
| Dario/Pulgar lineage bridge from page 172 | 0.04 | No direct Dario/Arturo evidence appears on this page; using entry 513 by surname context alone would be a high-risk relationship jump. |

## Next Action

Keep the staged draft and all person/relationship claims from page 172 on `hold_for_conversion_qa`.

The next action is targeted conversion QA against the source image for entries 513-515, starting with the chunk/version mismatch (`CHUNK-4127185dc97c-P0172-01` versus `CHUNK-d6a12b291d94-P0172-01`). Then verify entry 513 child name and maternal surname, entry 514 father field, and entry 515 surname/emendation before any proof review attempts canonical identity linkage.
