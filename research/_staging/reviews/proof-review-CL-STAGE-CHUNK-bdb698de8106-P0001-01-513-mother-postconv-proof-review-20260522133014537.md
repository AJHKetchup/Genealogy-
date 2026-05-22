---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522133014537
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-mother.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-mother.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_conflict_note: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available_same_directory: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available_same_source: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: parent
subject_claimed: Isolina del Carmen Jose
predicate_claimed: mother
object_claimed: Juana de Dios Amador de Pulgar
source_quality_score: 0.92
conversion_confidence_score: 0.35
evidence_quantity_score: 0.60
agreement_score: 0.35
identity_confidence_score: 0.20
claim_probability: 0.25
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-mother

## Blockers

- The exact staged relationship is not safely supported because the staged child subject `Isolina del Carmen Jose` is not established by the reviewed materials. The source packet and conflict note say the visible image appears closer to an entry 513 child reading like `Pulgar ... / Jose Luis`, while the available conversion layers disagree on the child name.
- The mother-name reading is materially conflicted. The reviewed converted file and same-directory available chunk read `Juana de Dios Amador`, while the alternate same-source chunk reads `Juana de Dios Amagada de Pulgar`; the visible source image appears closer to the alternate `Juana de Dios ... de Pulgar` form, but the surname remains a conversion-QA issue.
- The exact object `Juana de Dios Amador de Pulgar` is therefore not literally established as written. The staged draft combines a surname from one conversion layer with the married-name form from another layer.
- The draft's referenced chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is unavailable. The same directory contains `page-0172-chunk-01.md`, with a different chunk id, so the missing `CHUNK-bdb698de8106-P0001-01` reference should not be treated as verified.
- The source packet explicitly recommends `hold_for_conversion_qa` because entry 513 has material conflicts between the derivative transcript and the visible image. This mother claim inherits both the row-level child identity risk and the mother-surname risk.

## Evidence Strengths

- The underlying source is strong: a contemporaneous civil birth-register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, entry 513.
- Entry 513 has an explicit `Nombre de la madre` field, making the source directly relevant to a mother claim for the child in that row.
- All reviewed layers agree that the entry 513 mother is named `Juana de Dios` and that she is associated with the Pulgar family/household at `Calle Colon`.
- The visible source image supports a mother-field reading close to `Juana de Dios ... de Pulgar`, but not with enough confidence to promote the exact staged surname without conversion QA.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is direct, high-quality evidence for parentage recorded in the entry.
- `conversion_confidence_score`: 0.35. The cited chunk is missing, conversion layers conflict on the child name and mother surname, and the source packet flags the page for QA.
- `evidence_quantity_score`: 0.60. There is one direct register entry plus derivative transcription and image review, but no independent corroborating source.
- `agreement_score`: 0.35. The given name `Juana de Dios` is stable, but the exact surname/married-name form and the staged child identity do not agree across reviewed materials.
- `identity_confidence_score`: 0.20. The staged subject `Isolina del Carmen Jose` is not established as the entry 513 child.
- `claim_probability`: 0.25. It is likely that entry 513 names a mother `Juana de Dios ... de Pulgar`, but the exact staged claim that `Juana de Dios Amador de Pulgar` is mother of `Isolina del Carmen Jose` is low probability until QA resolves the row.
- `relevance_level`: high. The reviewed source is directly relevant to the mother of the child registered in entry 513.
- `relevance_confidence`: 0.85. The row and mother column are the correct evidence target, with confidence reduced by the stale chunk reference and unresolved transcription conflict.
- `canonical_readiness`: hold. Do not promote this staged claim until conversion QA reconciles entry 513's child name, mother surname/married-name form, and chunk path/id.

## Next Action

Hold for conversion QA. Ask QA to verify entry 513 directly against the source image, repair the cited chunk path/id, and reconcile whether the mother field should read `Juana de Dios Amador`, `Juana de Dios Amagada de Pulgar`, or another visible-source-supported form. After QA, revise the relationship so the mother is attached only to the child identity and name form visibly supported by the source.
