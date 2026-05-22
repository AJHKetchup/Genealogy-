---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522151229536
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-birth-date.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-birth-date.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available: false
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: birth
subject_claimed: Rosa Elvira del Carmen
object_claimed: "1889-07-23 at 10:00 a.m.; place not transcribed"
source_quality_score: 0.92
conversion_confidence_score: 0.20
evidence_quantity_score: 0.35
agreement_score: 0.05
identity_confidence_score: 0.15
claim_probability: 0.10
relevance_level: high
relevance_confidence: 0.60
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-birth-date

## Blockers

- The staged literal-support quote is not supported by the reviewed converted file for entry 515. The converted file reads entry 515's birth field as `veinte i seis ... a las seis de la mañana` with `Lugar. Calle Colon`, not 23 July 1889 at 10:00 a.m. with no place transcribed.
- The staged quote appears to match the converted file's entry 514 birth date/time pattern rather than entry 515. This is a row-alignment risk and prevents treating the staged claim as proven for entry 515.
- The referenced chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is unavailable, so the exact cited chunk could not be verified.
- The source packet recommends `hold_for_conversion_qa` and records material conflicts between the bdb derivative transcript and the visible source image for entry 515, including child name and father/declarant readings. The visible source image also shows only the upper portion of entry 515, leaving the lower birth-field details difficult to verify directly from the available image view.
- The staged subject `Rosa Elvira del Carmen` conflicts with the source packet's image-review note, which says entry 515 appears closer to `Neira Elvira / Laura de la Cruz...`. This creates identity risk for any birth-date claim attached to the staged subject.

## Evidence Strengths

- The source itself is a strong record type: a contemporaneous civil birth register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172.
- Entry 515 is present on the page and is directly relevant to a birth event.
- The converted file has a specific entry-515 birth-date/time/place field, so a corrected claim may be recoverable after conversion QA.
- The source packet preserves the key disagreement between the derivative transcript and image-reviewed evidence instead of silently normalizing the conflict.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is high-quality direct evidence for birth details when the entry is legible and correctly transcribed.
- `conversion_confidence_score`: 0.20. The staged claim, converted file, unavailable chunk reference, and source-packet image notes do not agree for entry 515.
- `evidence_quantity_score`: 0.35. There is one relevant register entry, but the usable evidence for this exact claim is limited by the missing chunk and row/identity conflicts.
- `agreement_score`: 0.05. The exact staged birth date/time is contradicted by the reviewed converted file for entry 515.
- `identity_confidence_score`: 0.15. The claimed subject is not stable across the reviewed derivative transcript and source-packet image notes.
- `claim_probability`: 0.10. Low probability that the exact staged claim is correct for entry 515 as written.
- `relevance_level`: high. The source is directly relevant to a birth-date claim for entry 515.
- `relevance_confidence`: 0.60. Relevance is clear, but confidence is reduced by the unresolved row alignment, identity, and conversion QA issues.
- `canonical_readiness`: hold. Do not promote this claim until conversion QA reconciles entry 515 against the source image and fixes the stale chunk reference.

## Next Action

Hold for conversion QA. Ask QA to reconcile entry 515's child identity, birth date, birth time, place field, and chunk path directly against the source image. After QA, revise or replace this staged claim from the corrected entry-515 transcription; do not promote the current `1889-07-23 at 10:00 a.m.` claim for `Rosa Elvira del Carmen`.
