---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525004127800
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524231550559.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524231550559.md
reviewed_source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524231550559.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
decision: hold
source_quality_score: 0.88
conversion_confidence_score: 0.38
evidence_quantity_score: 0.64
agreement_score: 0.45
identity_confidence_score: 0.74
claim_probability: 0.80
relevance_level: critical
relevance_confidence: 0.94
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- Canonical use is blocked by a material derivative-transcription conflict. The visible source image and referenced chunk support page 58, entry 172 as the Pulgar/Arriagada row, but the referenced converted Markdown currently transcribes entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 in `En esta`.
- The staged draft correctly warns that the converted Markdown conflicts with the Pulgar/Arriagada row, but its quoted conflict details do not match the converted file reviewed for this task. The draft says the converted file gives `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born in `Pellin`; those details were not present in the converted Markdown at review time.
- The exact father-name suffix remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet and image review leave the final suffix or mark after `Pulgar` uncertain for canonical use.
- No Dario-related identity or relationship claim is supported. The reviewed source context does not name Dario, and surname/family context alone would be an identity jump.
- Do not promote child identity, birth facts, parent-child relationships, parent-candidate merge claims, or wiki/canonical content from this staged draft until targeted conversion QA reconciles or supersedes the converted Markdown.

## Evidence Strengths

- The raw page image is available and visibly places entry 172 on register page 58 as the Pulgar/Arriagada row.
- The chunk agrees with the visible source image on the core cluster: child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, broad father reading `Jose del Carmen Pulgar`, informant `Ernesto Herrera L.`, and birth on 8 March 1888 at Calle de Valdivia.
- The source type is strong direct evidence once the row and transcription lineage are reconciled: a civil birth register can support child identity and declared-parent facts.
- The staged draft is appropriately conservative in its main recommendation to hold for conversion QA and to avoid attaching the record to any Dario candidate.

## Scored Judgment

| factor | score / value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is a high-value source class; the image is usable, though handwriting and father suffix need targeted review. |
| conversion_confidence_score | 0.38 | The assigned converted Markdown conflicts at row level with the chunk and image. |
| evidence_quantity_score | 0.64 | One source image, one chunk, one converted file, and one source packet were checked; enough for a hold judgment, not enough for canonical promotion. |
| agreement_score | 0.45 | Image, chunk, source packet, and staged conclusion agree on the broad Pulgar/Arriagada row, but the converted file and the draft's quoted conflict details disagree. |
| identity_confidence_score | 0.74 | The Pulgar/Arriagada row identity is probable from image/chunk review, but conversion lineage conflict and father suffix uncertainty reduce confidence. |
| claim_probability | 0.80 | The staged draft's hold-for-QA and no-Dario conclusions are well supported; the underlying identity cluster remains probable but not canonically ready. |
| relevance_level | critical | This review directly determines whether the staged identity analysis can proceed. |
| relevance_confidence | 0.94 | All reviewed materials point to the same source image/page/entry despite derivative-text conflict. |
| canonical_readiness | hold_for_conversion_qa | Hold until targeted conversion QA reconciles the converted Markdown and records the father-field reading. |

## Next Action

Run targeted conversion QA against the source image for page 58, entry 172. QA should reconcile or supersede the referenced converted Markdown, correct the conflict description to match the current converted file or updated QA result, and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, identity merge, or wiki promotion.
