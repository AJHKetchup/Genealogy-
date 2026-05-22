---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522154503628
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-child-name-sex.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-child-name-sex.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available: false
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: identity
predicate: registered_name_and_sex
subject_claimed: Tulio Cesar Luis Jose
object_claimed: "Registered in birth entry 513; sex recorded as Masculino"
source_quality_score: 0.92
conversion_confidence_score: 0.20
evidence_quantity_score: 0.60
agreement_score: 0.20
identity_confidence_score: 0.10
claim_probability: 0.20
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-child-name-sex

## Blockers

- The exact staged claim is not literally supported as written. The staged draft says entry 513 records `Nombre. Tulio Cesar Luis Jose`, but the visible source image places the visible `Tulio...` name in a lower row, not in entry 513.
- The entry 513 child-name field visible in the source image appears to begin with a `Pulgar...` surname line and a later given-name line, but it is not clear enough here to promote a complete replacement child name from proof review alone.
- The reviewed converted file materially disagrees with the staged draft: it transcribes entry 513 as `Isolina del Carmen` / `Jose`, with `Sexo. Masculino`, not `Tulio Cesar Luis Jose`.
- The requested chunk path is unavailable: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md` could not be read. A nearby available replacement chunk also reads entry 513 as `Isolina del Carmen` / `Jose`, not the staged name.
- The source packet quotes `Nombre. Tulio Cesar Luis Jose`, but that quote conflicts with both the reviewed converted file and direct image review. This is a conversion/provenance conflict and should not be resolved by silently rewriting the staged transcription.

## Evidence Strengths

- The source is a contemporaneous civil birth-register page and is strong direct evidence for a registered child name and sex when the row is correctly read.
- Entry 513 is visible on page 172, and its sex field visibly supports `Masculino`.
- The staged claim is highly relevant to the source because entry 513 has an explicit `Nombre i sexo` field.

## Scored Judgment

- `source_quality_score`: 0.92. Civil birth registers are strong direct sources for registered name and sex.
- `conversion_confidence_score`: 0.20. The cited chunk is missing, and the source packet, converted file, replacement chunk, and image review disagree on the child name.
- `evidence_quantity_score`: 0.60. There is one direct source image plus derivative transcriptions, but the name evidence is conflicted.
- `agreement_score`: 0.20. The sex `Masculino` agrees, but the claimed full child name does not.
- `identity_confidence_score`: 0.10. `Tulio Cesar Luis Jose` is not established as the entry 513 child by the reviewed evidence.
- `claim_probability`: 0.20. The sex portion is likely for entry 513, but the exact staged name-and-sex claim is low probability as written.
- `relevance_level`: high. The source directly concerns the claimed registered-name and sex field.
- `relevance_confidence`: 0.85. The page is relevant even though the staged extraction appears row-misaligned or otherwise unreconciled.
- `canonical_readiness`: hold. Do not promote this claim as written.

## Next Action

Hold for targeted conversion QA. Reconcile entry 513's child-name field and the missing chunk reference directly against the source image; preserve `Sexo. Masculino` as supported, but do not create or normalize a canonical child identity from `Tulio Cesar Luis Jose`, `Isolina del Carmen Jose`, or any alternate reading until the visible-source transcription is resolved.
