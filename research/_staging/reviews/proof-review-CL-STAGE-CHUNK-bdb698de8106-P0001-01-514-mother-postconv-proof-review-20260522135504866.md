---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522135504866
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-mother.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-mother.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available_same_directory: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available_same_source: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: parent
subject_claimed: Riquelme Juan Teodoro
predicate_claimed: mother
object_claimed: Mercedes Riquelme
source_quality_score: 0.92
conversion_confidence_score: 0.40
evidence_quantity_score: 0.55
agreement_score: 0.35
identity_confidence_score: 0.30
claim_probability: 0.38
relevance_level: high
relevance_confidence: 0.88
canonical_readiness: revise
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-mother

## Blockers

- The draft's referenced chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is unavailable. The same directory contains `page-0172-chunk-01.md`, but that is a different chunk id and cannot verify the staged `CHUNK-bdb698de8106-P0001-01` reference as cited.
- The staged subject `Riquelme Juan Teodoro` is not literally supported by the reviewed conversion layers or the visible source image. The available derivative readings for entry 514 conflict, including `Rigoberto Juan Bautista` in the converted file and `Riquelme Aviles / Juan Bautista` in the alternate same-source chunk. The image visibly supports a reading closer to `Riquelme / Juan Bautista`, not `Juan Teodoro`.
- The source packet recommends `hold_for_conversion_qa` because entry 514 has material conflicts between the assigned converted/chunk transcript and image-reviewed evidence, including child name, father field, witnesses, and street name.
- The mother field itself is strong, but attaching that mother to the staged child identity creates an identity-risk problem. This should be revised only after conversion QA establishes the child's literal name for entry 514.

## Evidence Strengths

- The underlying source is a contemporaneous civil birth-register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, entry 514.
- The visible source image directly shows entry 514's mother field as `Mercedes Riquelme`, followed by wording indicating that she requested her name be recorded, with nationality `Chilena`, profession `Costurera`, and domicile on a `Calle San...` line.
- The converted file, the available same-directory chunk, the alternate same-source chunk, and the source packet all agree that the mother named for entry 514 is `Mercedes Riquelme`.
- The informant/declarant column also names `Mercedes Riquelme` as `Madre`, strengthening the internal support that she is the mother named in the row.

## Scored Judgment

- `source_quality_score`: 0.92. A civil birth register is direct evidence for a child-parent relationship recorded at birth registration.
- `conversion_confidence_score`: 0.40. The mother name is stable, but the requested chunk is missing and the entry has serious row-level transcript conflicts.
- `evidence_quantity_score`: 0.55. There is one direct register entry plus image review; no independent corroborating source was reviewed for identity resolution.
- `agreement_score`: 0.35. The mother name agrees across layers, but the staged child identity does not agree with the visible image or available conversion layers.
- `identity_confidence_score`: 0.30. The identity of the child as `Riquelme Juan Teodoro` is not supported; the row appears to concern a Juan Bautista Riquelme/related surname reading.
- `claim_probability`: 0.38. It is highly likely that Mercedes Riquelme is the mother named in entry 514, but unlikely that this exact staged claim is correct because the subject name is unsupported.
- `relevance_level`: high. The reviewed source directly concerns entry 514 and its mother field.
- `relevance_confidence`: 0.88. The evidence target is the correct row and column, despite transcript instability.
- `canonical_readiness`: revise. Do not promote this staged claim as written. Revise after conversion QA reconciles entry 514's child-name reading and repairs the stale chunk reference.

## Next Action

Hold for conversion QA and revise the staged claim. Ask QA to verify entry 514's child-name field against the page image and reconcile the competing readings before any mother relationship is promoted. The mother name `Mercedes Riquelme` is directly supported for entry 514, but the subject `Riquelme Juan Teodoro` is not.
