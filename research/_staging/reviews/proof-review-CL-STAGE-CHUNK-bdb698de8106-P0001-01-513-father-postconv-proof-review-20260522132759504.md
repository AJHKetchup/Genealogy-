---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522132759504
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-father.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-father.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_conflict_note: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available_same_directory: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available_same_source: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: parent
subject_claimed: Isolina del Carmen Jose
predicate_claimed: father
object_claimed: Jose del Carmen Pulgar
source_quality_score: 0.92
conversion_confidence_score: 0.45
evidence_quantity_score: 0.60
agreement_score: 0.55
identity_confidence_score: 0.25
claim_probability: 0.35
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-father

## Blockers

- The exact staged relationship is not safely supported because the staged child subject `Isolina del Carmen Jose` is not established by the reviewed materials. The source packet and conflict note say the visible image appears closer to an entry 513 child reading like `Pulgar ... / Jose Luis`, while the available conversion layers also disagree on the child name.
- The draft's referenced chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is unavailable. The same directory contains `page-0172-chunk-01.md`, with a different chunk id, so the missing `CHUNK-bdb698de8106-P0001-01` reference should not be treated as verified.
- The source packet explicitly recommends `hold_for_conversion_qa` because entry 513 has material conflicts between the derivative transcript and the visible image. This parent claim inherits that row-level identity risk.
- The father field supports a father named `Jose/Jose del Carmen Pulgar` for entry 513's child, but it does not support assigning that father relationship to `Isolina del Carmen Jose` unless conversion QA first resolves the child identity.

## Evidence Strengths

- The underlying source is strong: a contemporaneous civil birth-register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, entry 513.
- The visible source image directly supports the entry 513 father field as `José del Carmen Pulgar` or a very close reading.
- Both available conversion layers reviewed for this source include `Nombre del padre. José del Carmen Pulgar` for entry 513, despite disagreeing on other row details.
- The same row also names `José del C. Pulgar` as the compareciente and marks him `Padre`, which internally reinforces the father-field reading without requiring external identity research.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is direct, high-quality evidence for parentage recorded in the entry.
- `conversion_confidence_score`: 0.45. The father name is comparatively stable, but the cited chunk is missing and the same row has unresolved child-identity and other transcription conflicts.
- `evidence_quantity_score`: 0.60. There is one direct register entry plus image review and derivative transcriptions, but no independent corroborating source.
- `agreement_score`: 0.55. The father name agrees across reviewed layers, but agreement for the exact staged relationship is reduced by the unsupported staged child identity.
- `identity_confidence_score`: 0.25. The identity of the entry 513 child as `Isolina del Carmen Jose` is low-confidence.
- `claim_probability`: 0.35. It is probable that entry 513 names `José del Carmen Pulgar` as the father, but the exact staged claim that he is father of `Isolina del Carmen Jose` is unlikely without QA correction.
- `relevance_level`: high. The source is directly relevant to a father claim for entry 513.
- `relevance_confidence`: 0.85. The father column and row are the correct evidence target, with confidence reduced only by the stale chunk reference and child-identity conflict.
- `canonical_readiness`: hold. Do not promote this staged claim until conversion QA reconciles entry 513's child name and repairs the chunk path/id.

## Next Action

Hold for conversion QA. Ask QA to verify entry 513 directly against the source image, repair the cited chunk path/id, and reconcile the child identity before any parent relationship is promoted. After QA, revise the relationship so `José del Carmen Pulgar` is attached only to the child identity visibly supported by the source.
