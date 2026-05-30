---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530014204174
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
qa_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260528234152427.md"
canonical_readiness: hold_for_conversion_chain_cleanup
source_quality_score: 0.86
conversion_confidence_score: 0.55
evidence_quantity_score: 0.72
agreement_score: 0.62
identity_confidence_score: 0.76
claim_probability: 0.78
relevance_level: high
relevance_confidence: 0.93
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

- Hold canonical use. The current converted Markdown still assigns entry `172` to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888, while the chunk assigns entry `172` to `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at Calle de Valdivia.
- The staged draft and source packet describe the converted-file conflict as `Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz` / 26 March. That is not what the referenced converted file currently says. This stale conflict summary should be revised before the analysis is reused as a controlling proof note.
- The referenced raw source image path was not available in the workspace during this review, and the manifest page-image path was also absent. I therefore did not independently transcribe the image. I relied on the assigned chunk, the converted Markdown, the source packet, and the targeted QA note.
- A targeted conversion QA note dated 2026-05-28 reports image review and certifies the physical row numbered `172` as the Pulgar/Arriagada row, but it certifies the father field only through `Jose del Carmen Pulgar`; it does not certify the chunk's trailing `S.`.
- No reviewed evidence names Dario in entry `172`. Any Dario attachment, merge, or relationship bridge remains unsupported.

## Evidence Strengths

- The chunk and source packet agree on the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, and declarant `Ernesto Herrera L.`.
- The targeted QA note strengthens row control by stating that the original page image controls and that physical row `172` is the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the converted Markdown.
- The staged draft correctly treats the issue as a material row-level conversion conflict rather than a name variant or ordinary identity merge problem.
- The anti-conflation conclusions are supported: do not merge the Entry 172 father with a same-name canonical `Jose del Carmen Pulgar` page without additional identity proof; do not normalize `Juana Arriagada de Pulgar` to `Juana de Dios Amagada de Pulgar`; do not attach this record to Dario-line candidates by surname context alone.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil registration is a strong source type, but the source image was not available to this proof reviewer. |
| conversion_confidence_score | 0.55 | QA note supports Pulgar/Arriagada row control, but the canonical converted Markdown remains contradictory and the staged draft repeats stale conflict details. |
| evidence_quantity_score | 0.72 | Multiple local derivatives and one targeted QA note address the same row, but there is no independent source-image review in this pass. |
| agreement_score | 0.62 | Chunk, source packet, and QA note agree on Pulgar/Arriagada; converted Markdown disagrees materially. |
| identity_confidence_score | 0.76 | The Pulgar/Arriagada child and mother identities are coherent under the QA-supported row-control reading; father suffix remains limited. |
| claim_probability | 0.78 | Best current judgment: entry 172 probably controls to the Pulgar/Arriagada row, with derivative cleanup still required. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child evidence, and to Dario anti-attachment controls. |
| relevance_confidence | 0.93 | The reviewed row, names, and conflict analysis are directly tied to the staged identity analysis. |
| canonical_readiness | hold_for_conversion_chain_cleanup | Do not promote until converted Markdown conflict and stale staged-summary wording are reconciled or explicitly superseded. |

## Claim-Specific Probabilities

| Claim / hypothesis | Probability | Judgment |
| --- | ---: | --- |
| Physical entry `172` is the Pulgar/Arriagada birth row | 0.84 | Supported by chunk/source packet plus targeted QA note; limited by unavailable image and stale converted Markdown. |
| Converted Markdown's Burgos/de la Cruz row controls this assignment | 0.16 | Literally present in converted file, but contradicted by chunk and targeted QA note. |
| Father field can be promoted as `Jose del Carmen Pulgar S.` | 0.46 | Chunk reads `S.`, but QA note certifies only through `Jose del Carmen Pulgar`. |
| Entry 172 supports a Dario identity or relationship bridge | 0.04 | No Dario is named and no relationship bridge was reviewed. |
| `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` should be merged | 0.12 | Similar local context only; literal names and child clusters differ. |

## Next Action

Revise or supersede the staged identity analysis so its converted-file conflict summary matches the current converted Markdown: `Jose Miguel`, `Oswaldo Burgos`, `Concepcion de la Cruz`, 6 April 1888. Then either update/supersede the converted Markdown or record a controlling conversion-chain decision that the 2026-05-28 targeted QA note controls over the stale converted transcription. After that cleanup, rerun proof review for any child identity, parent relationship, father-name form, or canonical wiki update.

Until then, keep this staged draft and dependent claims at `hold_for_conversion_chain_cleanup`; no canonical promotion, merge, rename, or Dario attachment is supported.
