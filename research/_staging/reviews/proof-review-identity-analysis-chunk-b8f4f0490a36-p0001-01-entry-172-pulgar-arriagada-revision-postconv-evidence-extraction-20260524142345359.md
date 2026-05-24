---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260524144327844
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524142345359.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524142345359.md
reviewed_source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524142345359.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.88
conversion_confidence_score: 0.45
evidence_quantity_score: 0.62
agreement_score: 0.42
identity_confidence_score: 0.72
claim_probability: 0.74
relevance_level: high
relevance_confidence: 0.86
canonical_readiness: hold_for_conversion_qa
recommendation: revise_and_hold
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- The staged draft correctly identifies a row-level conflict between the assigned converted Markdown and the assigned chunk/source image, so this is not ready for canonical use.
- The staged draft's conflict description is partly unsupported by the reviewed converted file. The converted file does transcribe entry 172 as a different child and parents (`Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, place `En esta`), but I did not find the draft's stated `Rosario de la Cruz de la Maza` or `Pellin` in the reviewed converted file.
- The father's final suffix or mark after `Pulgar` remains insufficiently settled for canonical identity work. The chunk reads `Jose del Carmen Pulgar S.`, while the source image supports the broad `Jose del Carmen Pulgar` reading but does not make the final mark fully reliable at review scale.
- Do not connect this entry to any Dario identity. The reviewed draft, chunk, and visible source page do not name Dario.

## Evidence Strengths

- The source is a civil birth register image, which is strong direct evidence for a birth registration, child identity as recorded, parent names as recorded, birth date/place, and informant.
- The assigned chunk and source packet agree that register page 58, entry 172 is for `Jose del Carmen Segundo Pulgar Arriagada`, male, registered `Siete de Abril de mil ochocientos ochenta i ocho`, born `Ocho de Marzo de mil ochocientos ochenta i ocho`, at `Calle de Valdivia`.
- Direct source image review supports the Pulgar/Arriagada row at entry 172 and supports the mother as `Juana Arriagada de Pulgar`, the informant as `Ernesto Herrera L.`, and the warning that this is not a Dario record.
- The draft uses appropriate caution by recommending `hold_for_conversion_qa` rather than promotion.

## Scored Judgment

- `source_quality_score`: 0.88. Civil registration is a direct, high-quality source, though the image is a photographed two-page spread with some handwriting and resolution limits.
- `conversion_confidence_score`: 0.45. The chunk appears consistent with the visible source image, but the assigned converted Markdown contains a material row-level mismatch.
- `evidence_quantity_score`: 0.62. There is one direct source image plus derivative chunk/source-packet support, but no independent corroborating source.
- `agreement_score`: 0.42. The chunk/source packet/image agree on the Pulgar/Arriagada row, but the converted Markdown disagrees materially and the staged draft misstates part of that disagreement.
- `identity_confidence_score`: 0.72. The child/mother/informant row identity is moderately strong from the image and chunk; the father suffix is unresolved.
- `claim_probability`: 0.74. The claim cluster is probably correct as a source-specific transcription/identity analysis, but should not be treated as canonical until conversion QA resolves the derivative-file conflict.
- `relevance_level`: high. Pulgar and Arriagada are explicitly present in the supported row.
- `relevance_confidence`: 0.86. The visible source and assigned chunk support the family relevance, with no visible Dario support.
- `canonical_readiness`: hold_for_conversion_qa. This should remain staged until the converted Markdown is corrected or superseded and the father suffix is documented as resolved or explicitly uncertain.

## Next Action

Revise the staged draft or dependent QA note to correct the converted-file conflict details, then send the source through targeted conversion QA. After QA reconciles the assigned converted Markdown with the visible source image and records the father-name suffix decision, rerun proof review before any canonical promotion.
