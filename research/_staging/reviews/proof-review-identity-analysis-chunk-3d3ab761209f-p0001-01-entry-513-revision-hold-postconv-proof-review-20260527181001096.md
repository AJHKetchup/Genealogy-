---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527181001096
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-proof-review-revision-hold-postconv-evidence-extraction-20260527152606301.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-proof-review-revision-hold-postconv-evidence-extraction-20260527152606301.md"
reviewed_files:
  - "research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-proof-review-revision-hold-postconv-evidence-extraction-20260527152606301.md"
  - "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-proof-review-revision-hold-postconv-evidence-extraction-20260527152606301.md"
  - "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
  - "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
  - "raw/codex-conversion-jobs/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513/manifest.json"
source_image_attempted: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_image_available_for_review: false
source_quality_score: 0.72
conversion_confidence_score: 0.22
evidence_quantity_score: 0.44
agreement_score: 0.30
identity_confidence_score: 0.36
claim_probability: 0.86
relevance_level: high
relevance_confidence: 0.72
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 513 Pulgar Revision Hold

## Blockers

- The referenced raw source image is not available at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`, and no matching local image file was found for this review.
- The conversion job manifest points to `raw/codex-conversion-jobs/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513/page-images/page-0001.png`, but that page image is also unavailable. The manifest still marks page 1 as `todo`.
- The converted file and chunk materially disagree on entry 513. The converted file reads child `Isolina del Carmen / Jose`, mother `Juana de Dios Amador de Pulgar`, and birth on July 22 at 4:00 a.m.; the chunk reads child `Pulgar Amagada / Jose Luis`, mother `Juana de Dios Amagada de Pulgar`, and birth June 26 at 4:30 p.m.
- The source packet adds a third image-reviewed reading favoring `Pulgar Arriagada / Jose Dario[?]`, mother `Juana de Dios Arriagada de Pulgar`, and birth June 22 at 4:30 p.m. Because the image is absent, this review cannot certify that reading.
- The draft cannot support any canonical attachment, merge, parent-child relationship, birth-event claim, or identity bridge to Dario Arturo Pulgar-Smith, Dario/Jose Dario Pulgar Arriagada, Jose del Carmen Segundo Pulgar Arriagada, or existing Jose/Juana pages.

## Evidence Strengths

- The staged draft accurately treats entry 513 as a registration-scoped Pulgar family lead rather than a canonical identity attachment.
- The father/declarant field is the strongest available point of agreement: the converted file, chunk, and source packet all support Jose del Carmen Pulgar / Jose del C. Pulgar as father or declarant in the entry.
- The draft correctly refuses to equate `Amagada`, `Amador`, and `Arriagada` as surname variants without visible-source certification.
- The draft's warning about entry 515 is supported by the derivative materials: entry 515 is a separate lower row and should not be used for Pulgar-family claims from entry 513.

## Scoring

| category | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.72 | A civil birth register is a strong source type for birth, parentage, and declarant facts, but the actual image was unavailable for independent inspection. |
| conversion_confidence_score | 0.22 | The derivative conversion and chunk conflict on the child name, mother surname, and birth date/time, with an uncertified image-reviewed reading differing from both. |
| evidence_quantity_score | 0.44 | There is one directly relevant register entry plus row-control context, but the reviewable evidence is limited to conflicting derivative text. |
| agreement_score | 0.30 | Jose del Carmen Pulgar as father/declarant is broadly consistent; the identity-bearing child, mother, and birth details are not. |
| identity_confidence_score | 0.36 | Pulgar-family relevance is plausible, but the child's identity and maternal surname remain unresolved. |
| claim_probability | 0.86 | The staged draft's main claim, that entry 513 should stay on hold for conversion QA, is strongly supported by the conflicts and missing image. |
| relevance_level | high | If the Pulgar row is confirmed, this entry is directly relevant to Pulgar/Arriagada family reconstruction. |
| relevance_confidence | 0.72 | Relevance is supported by repeated Pulgar father/declarant readings, while unresolved row details limit confidence. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical claims, relationships, identity pages, family pages, or merges. |

## Claim Probability By Proposed Use

| proposed use | probability | readiness |
| --- | ---: | --- |
| Keep this staged draft on hold for targeted conversion QA. | 0.94 | ready as review disposition |
| Treat entry 513 as a Pulgar-family registration lead. | 0.78 | hold |
| Treat the child name as `Jose Dario Pulgar Arriagada`. | 0.42 | hold |
| Treat the mother as `Juana de Dios Arriagada de Pulgar`. | 0.48 | hold |
| Promote the birth date/time as June 22, 1889, 4:30 p.m. | 0.40 | hold |
| Merge or attach this entry to any existing Dario/Jose/Juana canonical page. | 0.08 | not ready |

## Next Action

Locate or restore the original source image or a high-resolution row crop for register page 172, entry 513. Run targeted conversion QA for the child full name, sex, exact birth date/time/place, father/declarant wording, mother full name and surname, and entry 515 row boundary. After a QA-certified transcription exists, rerun proof review on separate atomic identity, birth-event, declarant, mother, father, and parent-child relationship claims.
