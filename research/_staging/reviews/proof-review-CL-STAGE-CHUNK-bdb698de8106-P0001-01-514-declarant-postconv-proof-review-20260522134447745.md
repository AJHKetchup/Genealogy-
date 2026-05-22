---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522134447745
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-declarant.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-declarant.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_conflict_note: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available_same_directory: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available_same_source: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: appearance
subject_claimed: Mercedes Riquelme
object_claimed: "entry 514; mother; wife of Juan Soler; age 21; costurera; domiciled Calle Saneguin"
source_quality_score: 0.92
conversion_confidence_score: 0.48
evidence_quantity_score: 0.62
agreement_score: 0.42
identity_confidence_score: 0.78
claim_probability: 0.50
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: revise_or_hold
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-declarant

## Blockers

- The staged draft's referenced chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is unavailable. The same directory contains `page-0172-chunk-01.md`, with chunk id `CHUNK-0554d5747bd2-P0172-01`, so the cited `CHUNK-bdb698de8106-P0001-01` layer is not directly verifiable as referenced.
- The exact spouse wording in the staged claim is not supported by the reviewed evidence. The staged draft says `Esposa de Juan Soler`; the converted file and available `page-0172-chunk-01.md` read `Esposa de Juan de Dios Rivas`; the alternate same-source chunk and visible page image instead support a note closer to `No firma por no saber`, not a spouse statement.
- The domicile/street is unresolved. The staged draft uses `Calle Saneguin`; the converted file and available `page-0172-chunk-01.md` read `Calle Paneque`; the alternate same-source chunk and source packet image review favor a `Calle San...` reading closer to `Calle Sanegueso`. This should remain paleographically uncertain until conversion QA reconciles the image.
- The source packet and conflict note both recommend `hold_for_conversion_qa` for this page because entry 514 has material conflicts in the child name, father field, witnesses, and street readings. The declarant/mother identity is better supported than those conflicted fields, but the atomic claim includes unsupported and disputed details.

## Evidence Strengths

- The underlying source is a contemporaneous civil birth-register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, entry 514.
- The visible source image directly supports `Mercedes Riquelme` in the mother/declarant area and the declarant role `Madre`.
- The visible source image and alternate same-source chunk support the declarant's age as `Veintiun Años` and profession as `Costurera`.
- The page is directly relevant to an appearance claim for Mercedes Riquelme in entry 514; the uncertainty is about exact associated descriptors, not whether this is the right entry.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is direct evidence for the declarant and stated attributes in the entry.
- `conversion_confidence_score`: 0.48. The requested chunk is missing, and derivative transcript layers materially disagree with one another and with the image review.
- `evidence_quantity_score`: 0.62. There is one direct register entry and image review, but no independent corroborating source.
- `agreement_score`: 0.42. Name, mother/declarant role, age, and profession have meaningful agreement; spouse wording and street wording do not.
- `identity_confidence_score`: 0.78. `Mercedes Riquelme` is consistently tied to entry 514 as mother/declarant, but exact row details remain unsettled.
- `claim_probability`: 0.50. The core appearance-as-mother/declarant portion is probable, but the full atomic claim as staged is only about even because `wife of Juan Soler` lacks visible support and the street reading is unresolved.
- `relevance_level`: high. The reviewed source is the correct direct source for entry 514 declarant details.
- `relevance_confidence`: 0.90. The entry and declarant column are clearly the target evidence.
- `canonical_readiness`: revise_or_hold. Do not promote this exact claim. Hold for conversion QA or revise to a narrower claim limited to the supported declarant/mother, age, and profession details, with street uncertainty preserved.

## Next Action

Hold for conversion QA before canonical promotion. Ask QA to repair the stale chunk path/id, reconcile entry 514 against the page image, and specifically verify whether the declarant line after `Madre` reads a no-signature note rather than a spouse statement. Any revised claim should not state `Esposa de Juan Soler` unless that wording is visibly supported by the source.
