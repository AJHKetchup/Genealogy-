---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522152804624
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-declarant.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-declarant.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: appearance
subject_claimed: Pedro Pablo Leiva
object_claimed: "appeared as declarant in entry 515; father"
source_quality_score: 0.92
conversion_confidence_score: 0.20
evidence_quantity_score: 0.45
agreement_score: 0.15
identity_confidence_score: 0.15
claim_probability: 0.18
relevance_level: high
relevance_confidence: 0.78
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-515-declarant

## Blockers

- The staged claim identifies the declarant/father as `Pedro Pablo Leiva`, but the source packet records a targeted image-review conflict for entry 515 and says the visible father/declarant name appears closer to `Pedro Pablo Neira`.
- Direct review of the referenced source image supports the presence of an entry-515 father/declarant line beginning `Pedro Pablo ...` and a `Padre` role, but the visible surname does not safely support the staged `Leiva` reading. It appears closer to `Neira`, and this review should not substitute a corrected transcription for the unresolved conversion layer.
- The converted file and chunk agree with the staged `Pedro Pablo Leiva` reading, but they are derivative layers already flagged by the source packet as materially conflicting with the image for entry 515. Their agreement is therefore weak support, not independent corroboration.
- Identity risk is high. The exact staged subject should not be used to create or connect a canonical `Pedro Pablo Leiva` person, declarant appearance, or father relationship for entry 515 until conversion QA reconciles the surname directly from the image.
- Canonical readiness is `hold` because the source packet recommendation is `hold_for_conversion_qa`, and the conflict affects the core identity element of this claim.

## Evidence Strengths

- The underlying source is a contemporaneous civil birth register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, and is a strong record type for identifying a birth-entry declarant when the row is legible and correctly transcribed.
- Entry 515 is present on the referenced page, and the source is directly relevant to whether a named person appeared as compareciente/declarant and stated the role `Padre`.
- The staged draft, source packet, converted file, chunk, and image all point to the same source page and entry 515 context.
- The visible source image gives some support for the non-identity portion of the claim: entry 515 appears to include a `Pedro Pablo ...` declarant/father, with the role line `Padre`.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is high-quality direct evidence for a declarant-role claim if the name is accurately read.
- `conversion_confidence_score`: 0.20. The converted and chunked text read `Leiva`, but the source packet and direct image review flag the surname as unsafe.
- `evidence_quantity_score`: 0.45. There is one directly relevant register entry plus derivative transcript support, but the usable evidence is limited by partial visibility and a core-name conflict.
- `agreement_score`: 0.15. The derivative conversion layers agree with the staged claim, but the image-reviewed evidence conflicts with the exact surname.
- `identity_confidence_score`: 0.15. `Pedro Pablo Leiva` is not established as the entry-515 declarant; the visible surname appears materially different.
- `claim_probability`: 0.18. Low probability that the exact staged claim is correct as written.
- `relevance_level`: high. The cited source directly addresses the declarant/father field for entry 515.
- `relevance_confidence`: 0.78. Relevance is clear, but confidence is reduced by conversion conflict and surname uncertainty.
- `canonical_readiness`: hold. Do not promote until entry 515 is re-read from the source image and the father/declarant surname is reconciled.

## Next Action

Hold for conversion QA. Ask QA to re-read entry 515's father/declarant surname directly from the source image, preserving uncertainty if needed, and then revise or replace this staged claim from the image-supported reading. Do not promote the current `Pedro Pablo Leiva` declarant claim.
