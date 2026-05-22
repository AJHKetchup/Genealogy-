---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522105816426
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: birth
subject_claimed: Isolina del Carmen Jose
object_claimed: "1889-07-22 at 4:00 a.m.; Calle Colon"
source_quality_score: 0.92
conversion_confidence_score: 0.30
evidence_quantity_score: 0.50
agreement_score: 0.15
identity_confidence_score: 0.20
claim_probability: 0.20
relevance_level: high
relevance_confidence: 0.65
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place

## Blockers

- The exact staged claim is not literally supported as written. The staged subject is `Isolina del Carmen Jose`, but the reviewed source packet says the image appears closer to a masculine `Pulgar ... / Jose Luis` reading, and the reviewed source image shows a masculine entry rather than the staged subject.
- The staged object says `1889-07-22 at 4:00 a.m.; Calle Colon`. The reviewed converted file and available chunk read entry 513's birth field as `veinte i dos ... a las cuatro i veinte de la tarde`, while another available conversion-layer chunk for the same source reads `Junio veinte i seis ... a las cuatro i media de la tarde`. The source image appears to support `Calle Colon`, but the date and time are not stable enough for promotion.
- The staged literal-support block (`El mismo veinte dos ... a las cuatro de la mañana`) does not match the reviewed converted file, the available chunk, or the visible page image.
- The draft's referenced chunk path `page-0001-chunk-01.md` is unavailable in the cited `...los-nge-5ed7132d63` chunk directory. The available file there is `page-0172-chunk-01.md`, with a different chunk id (`CHUNK-4127185dc97c-P0172-01`), so it should not be silently treated as the claimed `CHUNK-bdb698de8106-P0001-01`.
- The source packet already recommends `hold_for_conversion_qa` because the derivative transcript conflicts materially with the source image for entry 513. This staged claim inherits that unresolved conversion risk.

## Evidence Strengths

- The source itself is strong: a contemporaneous civil birth-register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, entry 513.
- Entry 513 is directly relevant to a birth event and has an explicit birth-date/place column.
- The place component `Calle Colon` is supported across the reviewed converted file, the available chunk, and the visible source image.
- The registration context for entry 513 is identifiable on page 172, and the source packet correctly flags the need to preserve disagreement between conversion layers and image-review notes.

## Scored Judgment

- `source_quality_score`: 0.92. The source is a direct civil birth register and would be high-quality evidence if the transcription layer were stable.
- `conversion_confidence_score`: 0.30. Conversion layers and the staged draft disagree on the child identity and birth time/date details.
- `evidence_quantity_score`: 0.50. There is one direct entry, but the usable evidence for this exact subject-date-place claim is weakened by transcription conflict.
- `agreement_score`: 0.15. Only the place `Calle Colon` is consistently supported; the staged subject and time are not.
- `identity_confidence_score`: 0.20. The staged subject `Isolina del Carmen Jose` is not established by the reviewed materials.
- `claim_probability`: 0.20. Low probability that the exact claim as staged is correct; a different entry-513 birth-place claim may be recoverable after conversion QA.
- `relevance_level`: high. The source is directly relevant to a birth date/place claim for entry 513.
- `relevance_confidence`: 0.65. Relevance is clear, but confidence is reduced by the unresolved identity and date/time conflicts.
- `canonical_readiness`: hold. Do not promote this staged claim until conversion QA reconciles entry 513 against the visible source image and repairs the stale chunk reference.

## Next Action

Hold for conversion QA. Ask QA to reconcile entry 513's child identity, sex, birth date, birth time, and chunk id/path directly against the source image. After QA, revise or replace the staged claim from the corrected transcription; retain `Calle Colon` only if the corrected entry still supports that place for the confirmed subject.
