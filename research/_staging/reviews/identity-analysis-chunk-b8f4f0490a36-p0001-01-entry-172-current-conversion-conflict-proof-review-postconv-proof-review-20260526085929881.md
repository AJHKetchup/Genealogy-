---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526085929881
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045206977.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045206977.md
reviewed_source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md
reviewed_conflict_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
created: 2026-05-26
source_quality_score: 0.82
conversion_confidence_score: 0.42
evidence_quantity_score: 0.62
agreement_score: 0.34
identity_confidence_score: 0.66
claim_probability: 0.58
relevance_level: high
relevance_confidence: 0.88
canonical_readiness: hold
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

- Canonical readiness is `hold`. The staged identity analysis is well supported as a conflict analysis, but the underlying derivative record set remains internally inconsistent: the current converted Markdown reads entry `172` as a Burgos/de la Cruz birth for `Jose Miguel`, while the chunk, source packet, conflict draft, and visible source image support a Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`.
- The claim cannot be promoted as a child identity, birth event, parent-child relationship, parent identity, or Dario-line bridge until targeted conversion QA reconciles the current converted Markdown against the chunk and image.
- The father field remains a proof blocker. The visible row and chunk support `Jose del Carmen Pulgar` with a trailing mark or suffix, but this review does not certify whether the controlled reading should be `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No evidence reviewed here supports any merge or bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.

## Evidence Strengths

- The staged draft accurately identifies a material row-level conflict rather than a spelling or same-person variant. The competing readings disagree on child name, sex wording, birth date/time, place, father, mother, informant, and nearby page context.
- The source packet and conflict draft consistently report the assigned chunk reading for entry `172`: `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The referenced page image visibly supports the chunk/source-packet row at a broad row level: entry `172` on page 58 appears to name `Jose del Carmen Segundo Pulgar Arriagada`, shows `Calle de Valdivia`, names the mother as `Juana Arriagada de Pulgar`, and names the informant as `Ernesto Herrera L.`.
- The staged draft correctly keeps canonical wiki stubs and other derivative pages from bootstrapping proof. This is appropriate because the row-control problem is within the source transcription chain.

## Scored Judgment

| Category | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registration image is a strong record type for birth identity and parent declarations, but the reviewed image is not being formally re-transcribed in this proof-review pass. |
| conversion_confidence_score | 0.42 | The chunk and image broadly align, but the current converted Markdown is materially inconsistent with them. Conversion QA remains required. |
| evidence_quantity_score | 0.62 | One source image plus multiple derivative artifacts were reviewed; all evidence comes from the same source package, so quantity is moderate, not independent corroboration. |
| agreement_score | 0.34 | Chunk, source packet, conflict draft, and image agree broadly; current converted Markdown sharply disagrees. |
| identity_confidence_score | 0.66 | The Pulgar/Arriagada identity is plausible for the visible row, but not proof-ready while the official converted Markdown conflicts and father suffix is unresolved. |
| claim_probability | 0.58 | Probable enough to justify holding the Pulgar/Arriagada conflict analysis, not high enough for canonical promotion. |
| relevance_level | high | If QA confirms the row, it directly concerns a Pulgar/Arriagada birth registration and parent candidates. |
| relevance_confidence | 0.88 | The Pulgar and Arriagada terms are visibly and textually present in the chunk-supported row. |
| canonical_readiness | hold | Requires targeted conversion QA and a renewed proof review before promotion. |

## Claim-Level Assessment

| Claim | Assessment | Probability | Canonical Readiness |
| --- | --- | ---: | --- |
| Entry `172` is a Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by chunk, source packet, conflict draft, and broad visual inspection; contradicted by current converted Markdown. | 0.64 | hold |
| Entry `172` is a Burgos/de la Cruz birth row for `Jose Miguel`. | Supported only by the current converted Markdown among reviewed materials; contradicted by chunk, source packet, conflict draft, and visible page row. | 0.22 | hold/revise after QA |
| The staged identity analysis correctly recommends `hold_for_conversion_qa`. | Strongly supported; the analysis preserves uncertainty and does not promote unsupported relationships. | 0.90 | ready as staging review only |
| `Jose del Carmen Pulgar S.` is the father. | Plausible from the chunk; final suffix/mark is not certified by this review. | 0.52 | hold |
| `Juana Arriagada de Pulgar` is the mother in the Pulgar row. | Strongly supported if the Pulgar row controls; still dependent on QA reconciliation. | 0.68 | hold |
| Any Dario-line bridge or merge is supported by this record. | Not supported by the reviewed source packet, chunk, converted file, or image. | 0.02 | not ready |

## Next Action

Keep the staged draft at `hold_for_conversion_qa`. The next action is targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`, comparing the source image, current converted Markdown, and chunk, then either correcting or superseding the conflicting derivative transcription. After QA, rerun proof review for the child identity, birth fact, parent names, parent-child relationships, and any later Pulgar/Arriagada identity comparison.
