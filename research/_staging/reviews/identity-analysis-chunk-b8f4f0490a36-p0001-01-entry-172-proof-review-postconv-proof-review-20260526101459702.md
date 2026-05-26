---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526101459702
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526085239273.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526085239273.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_page: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.88
conversion_confidence_score: 0.35
evidence_quantity_score: 0.62
agreement_score: 0.48
identity_confidence_score: 0.58
claim_probability: 0.60
relevance_level: high
relevance_confidence: 0.86
canonical_readiness: hold
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

- The staged identity analysis is materially supported as a hold note, but the underlying entry remains blocked by a row-level conversion conflict. The chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`; the current converted Markdown for the same source path reads entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The source image visually supports the Pulgar/Arriagada row at page 58, entry 172, but the converted Markdown still conflicts. This review cannot repair or overwrite the converted Markdown.
- The father field appears consistent with `Jose del Carmen Pulgar` followed by a possible terminal `S.` or mark. This review does not certify whether the correct father reading is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Parent-child claims for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar S.`, and `Juana Arriagada de Pulgar` are not ready for canonical promotion until conversion QA decides the controlling transcription.
- No reviewed evidence supports treating this entry as a same-person or direct relationship bridge to any Dario-line candidate. At most, it supports a future "double-check whether this is relevant to the Dario/Pulgar line" lead after row QA.

## Evidence Strengths

- The source type is strong: a civil birth registration image for Los Angeles, Chile, 1888.
- The assigned chunk gives a coherent row for entry 172: registration date 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; male; birth 8 March 1888 at 3 p.m.; place `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- The held source packet repeats the same Pulgar/Arriagada row and correctly flags the conversion conflict and father-field uncertainty.
- Visual inspection of the referenced source page aligns with the chunk/source-packet row for page 58, entry 172 and does not support rewriting the staged draft to a Dario identity.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration image is a high-quality source class, and the page image is available for direct review. |
| conversion_confidence_score | 0.35 | Low because the current converted Markdown materially disagrees with the assigned chunk, source packet, and visible row. |
| evidence_quantity_score | 0.62 | One main source image plus derivative chunk/source-packet support; no independent corroborating source reviewed. |
| agreement_score | 0.48 | The chunk, source packet, and image agree broadly, but the converted Markdown gives a different family and birth facts. |
| identity_confidence_score | 0.58 | Pulgar/Arriagada identity is plausible and visually supported, but still held because conversion control is unresolved. |
| claim_probability | 0.60 | The staged draft's hold conclusion is more likely than not; dependent genealogical claims remain conditional. |
| relevance_level | high | The Pulgar/Arriagada row is highly relevant if certified. |
| relevance_confidence | 0.86 | Names and family terms directly match the Pulgar/Arriagada research cluster. |
| canonical_readiness | hold | Do not promote identity, birth facts, parent facts, relationships, merges, or Dario-line links. |

## Review Decision

The staged identity analysis is acceptable as a hold-for-QA review product. Its blockers, uncertainty, and non-promotion recommendation are supported by the referenced files and the visible source page.

The Pulgar/Arriagada row has better support than the Burgos/de la Cruz derivative reading in the reviewed materials, but the conflict is not resolved in the canonical conversion layer. Proof review should therefore preserve the row conflict instead of promoting a corrected transcription or dependent claims.

## Next Action

Run targeted conversion QA on the source image and conversion output for register page 58, entry 172. The QA note should explicitly decide the controlling row and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical claim, relationship, parent merge, or Dario-line comparison is promoted.
