---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522154732359
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-declarant.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-declarant.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available: false
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: identity
predicate: declarant_for_birth_registration
subject_claimed: Jose del C. Pulgar
object_claimed: "Declared entry 513 as father; age 47; agricultor; domiciled at Calle Colon; known to the official"
source_quality_score: 0.92
conversion_confidence_score: 0.72
evidence_quantity_score: 0.78
agreement_score: 0.86
identity_confidence_score: 0.88
claim_probability: 0.86
relevance_level: high
relevance_confidence: 0.94
canonical_readiness: revise
---

# Proof Review: CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-declarant

## Blockers

- The exact chunk path cited by the staged draft is unavailable: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md`.
- The source packet is marked `hold_for_conversion_qa` because the page has conversion/provenance concerns. Those concerns mainly affect entry 515, but the missing requested chunk and conflicting derivative chunks mean this claim should not be promoted without revising the provenance to an available reviewed evidence file or source-image-verified note.
- Preserve the staged subject as an extracted display value, but reconcile accents and expansion only from the visible source. The visible source supports `José del C. Pulgar` in the declarant column and separately `José del Carmen Pulgar` as father; proof review should not silently normalize the abbreviation beyond what the source shows.

## Evidence Strengths

- The source is a contemporaneous Chilean civil birth register, direct evidence for the declarant named in entry 513.
- The visible source image supports the declarant column for entry 513 as `José del C. Pulgar`, role `Padre`, age `Cuarenta i siete Años`, occupation `Agricultor`, and domicile `Calle Colon`.
- The identity-check column for the same row supports that the declarant was known to the official: `El compareciente es` followed by printed/filled text indicating `Conocido del oficial`.
- The converted file and available replacement chunks agree on the core declarant facts for entry 513, even though they conflict on other fields on the page.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth-register entry is strong direct evidence for the declarant details recorded at registration.
- `conversion_confidence_score`: 0.72. The declarant facts are readable in the image and stable across available derivatives, but the exact requested chunk is missing and the page has known conversion conflicts.
- `evidence_quantity_score`: 0.78. There is one direct source image plus derivative transcription support; no independent second source was reviewed.
- `agreement_score`: 0.86. The staged declarant details agree with the visible image and available derivative text, with only abbreviation/accent handling needing care.
- `identity_confidence_score`: 0.88. The same row links the declarant `José del C. Pulgar` to the father field `José del Carmen Pulgar`, supporting the abbreviated declarant identity with moderate-high confidence.
- `claim_probability`: 0.86. The claim is very likely correct as a reading of entry 513, but provenance needs revision before canonical use.
- `relevance_level`: high. The reviewed page directly records the claimed declarant facts.
- `relevance_confidence`: 0.94. The claim concerns the exact declarant column and identity-check column for entry 513.
- `canonical_readiness`: revise. Revise the evidence reference/provenance before promotion; do not promote from the missing chunk path as written.

## Next Action

Revise the staged claim or its support metadata to cite an available reviewed chunk or source-image-backed evidence note, preserving the visible-source wording `José del C. Pulgar` and the separate father expansion `José del Carmen Pulgar`. After provenance is corrected, the declarant claim is a strong candidate for promotion.
