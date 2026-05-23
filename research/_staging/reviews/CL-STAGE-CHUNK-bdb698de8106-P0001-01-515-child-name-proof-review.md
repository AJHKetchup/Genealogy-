---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260523000006369
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name.md
claim_type: identity
subject: Rosa Elvira del Carmen
predicate: registered_name
object: Registered in birth entry 515
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entry 515
source_quality_score: 0.72
conversion_confidence_score: 0.20
evidence_quantity_score: 0.35
agreement_score: 0.15
identity_confidence_score: 0.20
claim_probability: 0.18
relevance_level: direct
relevance_confidence: 0.95
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 515 Child Name

## Blockers

- The staged claim relies on the converted/chunk reading `Nombre. Rosa Elvira del Carmen`, but the visible source image does not confidently support that literal name for entry 515.
- Entry 515 is only partially visible at the bottom of the page image. The child-name field appears closer to an unresolved reading such as `Neira/Neira? Elvira` followed by `Laura de la Cruz...`, matching the source-packet conflict note rather than the converted `Rosa Elvira del Carmen`.
- The source packet already records a material conflict for entry 515: image-reviewed child-name evidence conflicts with the converted name and with the converted father/declarant surname. This row-level conversion issue must be resolved before canonical use.

## Evidence Strengths

- The source is a civil birth register page, a high-relevance original-record type for a registered child-name claim.
- The page identity and entry context are strong: page 172 includes entries 513, 514, and a partial 515, and the staged draft points to the correct converted file, chunk, source packet, and source image.
- The claim is directly relevant to entry 515 because it concerns the child-name field in that specific register row.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.72 | Original civil register image, but entry 515 is cut off/partial in the available page image. |
| conversion_confidence_score | 0.20 | Converted name conflicts with targeted image review and visible source evidence. |
| evidence_quantity_score | 0.35 | One direct source and one derivative conversion layer; the decisive row is only partially visible. |
| agreement_score | 0.15 | Converted/chunk transcript and image-review notes materially disagree on the child name. |
| identity_confidence_score | 0.20 | The asserted identity string is not securely tied to the visible entry 515 name field. |
| claim_probability | 0.18 | Possible only as an unstable derivative reading; not sufficiently supported by the visible source. |
| relevance_level | direct | The evidence is the birth-register row for the claimed registered name. |
| relevance_confidence | 0.95 | The cited materials are the correct page/entry context. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until conversion QA supplies a stable literal transcription for entry 515. |

## Next Action

Hold this claim for targeted conversion QA on entry 515. The QA task should reconcile the partial source image against the converted `Rosa Elvira del Carmen` reading without replacing the transcription from inference alone.
