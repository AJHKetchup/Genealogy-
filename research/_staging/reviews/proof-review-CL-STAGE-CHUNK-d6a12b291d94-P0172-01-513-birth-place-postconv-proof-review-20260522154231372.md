---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522154231372
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-place.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-place.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available: false
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: event
predicate: birth_place
subject_claimed: Tulio Cesar Luis Jose
object_claimed: "Calle Colon, Los Anjeles, La Laja, Chile"
source_quality_score: 0.92
conversion_confidence_score: 0.25
evidence_quantity_score: 0.55
agreement_score: 0.35
identity_confidence_score: 0.25
claim_probability: 0.45
relevance_level: high
relevance_confidence: 0.80
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-place

## Blockers

- The exact staged claim is not ready for canonical promotion because the subject identity is unstable. The staged draft names `Tulio Cesar Luis Jose`, while the reviewed converted file transcribes entry 513 as `Isolina del Carmen José`, and direct image review does not clearly support the staged full name.
- The requested chunk path is unavailable: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md` could not be read. This blocks clean verification of the exact staged provenance.
- The source packet quotes `Nombre. Tulio Cesar Luis Jose`, but its reviewed converted file does not. That disagreement is a conversion/provenance conflict, not a basis to silently change the source transcription.
- The source image visibly supports `Lugar. Calle Colon` for entry 513, and the heading supports the Los Anjeles/La Laja register context. It does not, by itself, resolve whether this birth-place claim belongs to the staged subject as named.

## Evidence Strengths

- The source is a contemporaneous civil birth-register page, which is strong direct evidence for birth-event details.
- Entry 513 is visible on register page 172, and its birth-place field visibly reads `Calle Colon`.
- The broader jurisdiction is supported by the page heading, which identifies the register as the Circunscripcion de Los Anjeles, num. 1 of La Laja.
- The staged claim is relevant to the source because it concerns entry 513's birth place, a field explicitly present in the register.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is high-quality direct evidence for birth place when the entry identity is secure.
- `conversion_confidence_score`: 0.25. The unavailable requested chunk and conflict between the source packet, converted file, and visible child-name field materially reduce confidence.
- `evidence_quantity_score`: 0.55. There is one direct register entry and a visible source image, but only the place portion is stable.
- `agreement_score`: 0.35. `Calle Colon` agrees across the staged draft, converted file, and image; the claimed subject name does not.
- `identity_confidence_score`: 0.25. The entry 513 child identity needs targeted review before attaching this place to `Tulio Cesar Luis Jose`.
- `claim_probability`: 0.45. The probability is moderate for entry 513 having birth place `Calle Colon`, but low-to-moderate for the exact staged subject-place assertion.
- `relevance_level`: high. The source directly concerns the claimed event field.
- `relevance_confidence`: 0.80. The source is highly relevant despite identity uncertainty.
- `canonical_readiness`: hold. Do not promote this claim as written.

## Next Action

Hold for conversion QA or revise after targeted image review. Reconcile entry 513's child name and the missing chunk reference against the source image, then create or update the staged claim so the stable `Calle Colon` birth-place evidence is attached only to the confirmed entry-513 subject.
