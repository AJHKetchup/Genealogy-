---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522132543215
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_conflict_note: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available_same_directory: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available_same_source: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: appearance
subject_claimed: Jose del C. Pulgar
object_claimed: "entry 513; father; age 47; agricultor; domiciled Calle Colon"
source_quality_score: 0.92
conversion_confidence_score: 0.55
evidence_quantity_score: 0.65
agreement_score: 0.68
identity_confidence_score: 0.80
claim_probability: 0.78
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant

## Blockers

- The draft's referenced chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is unavailable. The same directory contains `page-0172-chunk-01.md`, with chunk id `CHUNK-0554d5747bd2-P0172-01`, so the missing `CHUNK-bdb698de8106-P0001-01` reference should not be treated as verified.
- The reviewed conversion layers disagree on material row details. The converted file and `page-0172-chunk-01.md` read the declarant's profession as `Jornalero`, while the visible image and the alternate same-source `page-0001-chunk-01.md` read the declarant's profession as `Agricultor`.
- The source packet and conflict note both recommend `hold_for_conversion_qa` for this page because entry 513 has a material child-name conflict between derivative transcript layers and the visible source image. This declarant claim is better supported than the child-name claim, but it remains attached to the same unresolved row-level QA issue.

## Evidence Strengths

- The underlying source is a contemporaneous civil birth-register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, entry 513.
- The visible source image directly supports a declarant/informant line reading `José del C. Pulgar`, with role `Padre`, age `Cuarenta i siete Años`, profession appearing as `Agricultor`, and domicile `Calle Colon`.
- The same row's father field reads `José del Carmen Pulgar`; this supports treating the abbreviated declarant name `José del C. Pulgar` as the father named in the parent column, without needing an external identity jump.
- The alternate same-source chunk `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md` agrees with the staged declarant claim on name, father role, age 47, profession `Agricultor`, and Calle Colon domicile.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is direct evidence for the declarant and his stated attributes in the entry.
- `conversion_confidence_score`: 0.55. The key declarant line is visibly supported, but the requested chunk is missing and conversion layers disagree on the profession and other row data.
- `evidence_quantity_score`: 0.65. There is one direct register entry plus image review, but no independent corroborating source.
- `agreement_score`: 0.68. Name, role, age, and domicile agree well across the visible source and at least one conversion layer; profession and row-level transcription details remain conflicted.
- `identity_confidence_score`: 0.80. The claim is internally supported by the same-row father and declarant fields, but the abbreviated middle name and unresolved row QA keep it below canonical certainty.
- `claim_probability`: 0.78. The declarant/father claim is probably correct as staged, including age and Calle Colon; the profession `Agricultor` is supported by the image but conflicts with one conversion layer.
- `relevance_level`: high. The reviewed source is directly relevant to whether José del C. Pulgar appeared as declarant/father in entry 513.
- `relevance_confidence`: 0.90. The entry and column are clearly the right evidence target.
- `canonical_readiness`: hold. Do not promote until conversion QA repairs the stale chunk reference and reconciles entry 513's conflicted transcript layers, especially the declarant profession and child-name row conflict.

## Next Action

Hold for conversion QA. Ask QA to verify entry 513 against the page image, repair the cited chunk path/id, and reconcile whether the declarant profession should be read as `Agricultor` or `Jornalero`. The name `José del C. Pulgar`, role `Padre`, age 47, and domicile `Calle Colon` have direct visible support, but the complete atomic claim should remain staged until the conversion conflict is resolved.
