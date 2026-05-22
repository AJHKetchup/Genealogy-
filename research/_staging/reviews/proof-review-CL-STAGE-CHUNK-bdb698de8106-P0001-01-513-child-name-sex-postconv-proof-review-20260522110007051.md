---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522110007051
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-name-sex.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-name-sex.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: identity
subject_claimed: Isolina del Carmen Jose
object_claimed: "Registered in birth entry 513; sex recorded as Masculino"
source_quality_score: 0.92
conversion_confidence_score: 0.25
evidence_quantity_score: 0.55
agreement_score: 0.25
identity_confidence_score: 0.20
claim_probability: 0.25
relevance_level: high
relevance_confidence: 0.75
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-name-sex

## Blockers

- The staged child name `Isolina del Carmen Jose` is not literally supported by the reviewed materials. The reviewed converted file and the available `page-0172-chunk-01.md` read entry 513 as `Isidoro del Carmen Diaz`, while another available conversion-layer chunk for the same source reads closer to `Pulgar Amagada / Jose Luis`. The source packet also records a targeted image-review conflict, saying the image appears closer to `Pulgar ... / Jose Luis`.
- The visible source image supports entry 513 as a masculine child, but it does not support the exact staged name. The name appears to begin with `Pulgar Arriagada` or a similar surname line, followed by a given-name line; this confirms the staged name is unsafe, not that a replacement reading is ready for canonical use.
- The draft's referenced chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is unavailable. The file present in that directory is `page-0172-chunk-01.md`, with chunk id `CHUNK-4127185dc97c-P0172-01`, so it should not be silently treated as the claimed `CHUNK-bdb698de8106-P0001-01`.
- The source packet explicitly recommends `hold_for_conversion_qa` because the derivative transcript conflicts materially with the source image for entry 513. This staged identity claim inherits that conversion risk.

## Evidence Strengths

- The source itself is strong: a contemporaneous civil birth-register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, entry 513.
- Entry 513 is directly relevant to the child's registered name and sex because the register has an explicit `Nombre i sexo` column.
- The sex component `Masculino` is supported by the reviewed converted file, the available chunks, the source packet, and the visible source image.
- The claim correctly remains in draft/hold posture and does not ask to normalize or promote the conflicted child name.

## Scored Judgment

- `source_quality_score`: 0.92. The underlying source is a direct civil register entry and is high-quality evidence for a birth registration.
- `conversion_confidence_score`: 0.25. Conversion layers disagree materially on the child name for entry 513, and the source packet flags the converted text as unsafe for promotion.
- `evidence_quantity_score`: 0.55. There is one direct register entry, but the usable evidence for the exact name-and-sex claim is limited by the unresolved transcription conflict.
- `agreement_score`: 0.25. The sex reading agrees across materials, but the staged child name does not.
- `identity_confidence_score`: 0.20. The staged subject `Isolina del Carmen Jose` is not established as the entry 513 child.
- `claim_probability`: 0.25. Low probability that the exact composite claim as staged is correct; only the `Masculino` component is well supported.
- `relevance_level`: high. The reviewed source is directly relevant to entry 513 child identity and sex.
- `relevance_confidence`: 0.75. Relevance is clear, but confidence is reduced by the missing cited chunk and unresolved name conflict.
- `canonical_readiness`: hold. Do not promote this staged claim until conversion QA reconciles entry 513's child name directly against the source image and repairs the stale chunk reference.

## Next Action

Hold for conversion QA. Ask QA to reconcile entry 513's child name and the correct chunk id/path against the source image. Preserve `Sexo. Masculino` as supported, but do not create or normalize a canonical child identity from `Isolina del Carmen Jose` or from any alternate reading until the visible-source transcription is resolved.
