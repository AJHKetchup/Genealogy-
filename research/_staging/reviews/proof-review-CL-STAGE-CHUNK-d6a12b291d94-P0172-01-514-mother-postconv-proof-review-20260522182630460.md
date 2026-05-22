---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260522182630460
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-514-mother.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-514-mother.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_recorded_in_draft: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_quality_score: 8.0
conversion_confidence_score: 5.5
evidence_quantity_score: 6.5
agreement_score: 5.0
identity_confidence_score: 7.0
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.95
canonical_readiness: revise
---

# Proof Review: Entry 514 Mother Claim

## Blockers

- The staged draft references `page-0172-chunk-01.md`, but that exact chunk path is unavailable. The available chunk in the same chunk directory is `page-0001-chunk-01.md`, with a different chunk id and converted hash.
- The staged object says Mercedes Riquelme was domiciled at `Calle San Joaquin`. The converted file/chunk read the domicile as `Calle Saneguin`, explicitly uncertain as possibly `Sanequin` or similar. The visible source image also appears closer to `Calle Saneguin`/similar, not `Calle San Joaquin`.
- The staged literal support says the child is `Rigoberto Juan Bautista`; the available conversion reads entry 514 child name as `Riquelme Juan Teodoro`. The visible source appears closer to `Rigoberto Juan Bautista`, but this conflict creates conversion-confidence and identity-risk concerns for the linked child identity.

## Evidence Strengths

- Entry 514 visibly places `Mercedes Riquelme` in the mother field.
- The same entry supports the mother attributes `Nac. Chilena` and `Prof. Costurera`.
- The declarant column independently repeats `Mercedes Riquelme`, identifies her as `Madre`, and lists profession `Costurera` and domicile on the same street line, strengthening the identity link to the mother named in the parent column.
- The source is a civil birth register page, contemporaneous with the recorded birth and registration, so the source quality is strong for birth-parent identity and parent attributes.

## Scored Judgment

- source_quality_score: 8.0/10
- conversion_confidence_score: 5.5/10
- evidence_quantity_score: 6.5/10
- agreement_score: 5.0/10
- identity_confidence_score: 7.0/10
- claim_probability: 0.62
- relevance_level: high
- relevance_confidence: 0.95
- canonical_readiness: revise

## Assessment

The core assertion that Mercedes Riquelme is the mother in entry 514, Chilean, and a seamstress is directly relevant and substantially supported by the source image and available derivative transcription. The claim as written should not be promoted because the domicile is stated as `Calle San Joaquin`, while the reviewed evidence supports an uncertain `Calle Saneguin`/similar reading. The child-name conflict between the staged draft and available conversion also warrants preserving uncertainty in any revised claim that ties the mother to a specific child identity.

## Next Action

Revise before canonical promotion: change the domicile wording to the source-supported uncertain street reading rather than `Calle San Joaquin`, and flag the entry 514 child-name conflict for conversion QA or proof reconciliation. Do not promote the current staged draft as written.
