---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260523000644405
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name.md
claim_type: identity
subject: Rosa Elvira del Carmen
predicate: registered_name
object: Registered in birth entry 515
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
referenced_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
available_chunk_checked: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entry 515
source_quality_score: 0.78
conversion_confidence_score: 0.12
evidence_quantity_score: 0.42
agreement_score: 0.05
identity_confidence_score: 0.06
claim_probability: 0.07
relevance_level: direct
relevance_confidence: 0.97
canonical_readiness: not_ready_revise_or_hold_for_conversion_qa
---

# Proof Review: Entry 515 Child Name

## Blockers

- The staged claim is not literally supported by the restored source image. The visible entry 515 child-name field appears closer to `Neira Ulloa / Laura de la Cruz` than to `Rosa Elvira del Carmen`.
- The staged draft references `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, but that exact chunk file is unavailable. The same chunk folder contains `page-0172-chunk-01.md`, whose entry 515 reading also conflicts with the staged claim.
- The converted file and available page-0172 chunk disagree materially: one derivative layer has `Rosa Elvira del Carmen`, while the available chunk has `Neira Ulloa / Laura de la Cruz`. The source packet already flags this row as a conversion conflict.
- Do not promote or normalize this staged claim from the derivative `Rosa Elvira del Carmen` text. Any replacement reading must come through conversion QA, not from this proof review note.

## Evidence Strengths

- The cited source is an original civil birth register image, directly relevant to a registered-name claim.
- The page and row context are strong: page 172 includes entries 513, 514, and 515, and entry 515 is visible enough to identify a material conflict with the staged name.
- The claim topic is direct rather than circumstantial because the evidence is the `Nombre i sexo` field for the exact birth-register entry.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | Original civil register image; entry 515 is low on the page and partly constrained by the image edge, but the name field is visible enough to test the claim. |
| conversion_confidence_score | 0.12 | The derivative reading used by the staged claim conflicts with the restored source image and with the available page-0172 chunk. |
| evidence_quantity_score | 0.42 | One direct image, one converted file, one source packet, and one available related chunk were checked; the exact referenced chunk path is missing. |
| agreement_score | 0.05 | The staged claim's supporting text does not agree with the visible name field or the available chunk. |
| identity_confidence_score | 0.06 | `Rosa Elvira del Carmen` is not securely tied to entry 515 after image review. |
| claim_probability | 0.07 | Very low probability as written; the visible entry supports a different child-name structure. |
| relevance_level | direct | The materials are the birth-register page and row for the claimed registered name. |
| relevance_confidence | 0.97 | The source/page/entry alignment is clear even though the claim reading is unsupported. |
| canonical_readiness | not_ready_revise_or_hold_for_conversion_qa | Do not promote. Revise only after conversion QA establishes the literal entry 515 name from the source image. |

## Next Action

Hold this staged claim for conversion QA or retire/revise it after QA. The next reviewer should reconcile entry 515 against the restored image and the available `page-0172-chunk-01.md`, while preserving the boundary between visible transcription and identity interpretation.
