---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522151446938
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available: false
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: identity
subject_claimed: Rosa Elvira del Carmen
object_claimed: "Registered in birth entry 515"
source_quality_score: 0.92
conversion_confidence_score: 0.20
evidence_quantity_score: 0.40
agreement_score: 0.10
identity_confidence_score: 0.15
claim_probability: 0.20
relevance_level: high
relevance_confidence: 0.70
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-child-name

## Blockers

- The staged claim depends on the converted reading `Nombre. Rosa Elvira del Carmen`, but the source packet records a targeted image-review conflict for entry 515: the visible name appears closer to `Neira Elvira / Laura de la Cruz...`, not the converted `Rosa Elvira del Carmen`.
- Direct review of the page image confirms that entry 515 is only partially visible and that the child-name field does not provide a clean, promotion-ready reading of `Rosa Elvira del Carmen`. The visible source should be double-checked by conversion QA before any canonical identity is formed from this row.
- The referenced chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is unavailable, so the exact cited chunk cannot be verified.
- The source packet's promotion recommendation is `hold_for_conversion_qa` because the bdb derivative transcript conflicts materially with image-reviewed evidence across entries 513-515. That conflict directly affects this child-name claim.
- The staged object only says `Registered in birth entry 515`, while the claim title and literal support are about the child's registered name. The proof question is therefore not just whether entry 515 exists, but whether this exact child-name reading is supported; it is not ready as written.

## Evidence Strengths

- The source itself is a contemporaneous civil birth register page for Los Anjeles/Los Angeles, La Laja, Chile, and is a strong source type for registered child names when the entry is legible and correctly transcribed.
- Entry 515 is present on page 172, and the source is directly relevant to identifying the child registered in that entry.
- The converted file contains a specific entry-515 child-name transcription, so a corrected or confirmed claim may be recoverable after conversion QA reconciles the transcript against the source image.
- The source packet preserves the derivative-transcript/image-review disagreement instead of silently normalizing it, which gives a clear path for targeted QA.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is high-quality direct evidence for a registered child name when the row is legible and aligned.
- `conversion_confidence_score`: 0.20. The converted name is specifically disputed by source-packet image review, and the requested chunk is unavailable.
- `evidence_quantity_score`: 0.40. There is one directly relevant register entry plus a derivative transcript, but the usable support is reduced by partial visibility and unresolved conversion conflict.
- `agreement_score`: 0.10. The staged claim agrees with the converted file but conflicts with the source packet's image-review note and with direct image review uncertainty.
- `identity_confidence_score`: 0.15. The claimed subject name is unstable across the derivative transcript and image-reviewed evidence, creating high identity risk.
- `claim_probability`: 0.20. Low probability that `Rosa Elvira del Carmen` is the correct entry-515 child name as written.
- `relevance_level`: high. The cited register page is directly relevant to the registered-name claim for entry 515.
- `relevance_confidence`: 0.70. Relevance is clear, but confidence is limited by partial row visibility, chunk unavailability, and conversion QA concerns.
- `canonical_readiness`: hold. Do not promote this claim until conversion QA reconciles entry 515's child-name field directly against the source image and repairs the stale chunk reference.

## Next Action

Hold for conversion QA. Ask QA to re-read entry 515's child-name field from the source image and explicitly resolve whether the visible source supports `Rosa Elvira del Carmen`, `Neira Elvira / Laura de la Cruz...`, or another uncertain reading. After QA, revise or replace the staged claim from the corrected entry-515 transcription; do not promote the current `Rosa Elvira del Carmen` identity claim.
