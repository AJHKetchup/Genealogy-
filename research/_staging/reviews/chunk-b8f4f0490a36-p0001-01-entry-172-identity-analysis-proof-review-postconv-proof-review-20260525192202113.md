---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525192202113
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
review_decision: hold
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

- The staged identity analysis should remain at `hold_for_conversion_qa`; do not promote any identity claim, birth claim, parent-child relationship, parent merge, or Dario-line linkage from this draft.
- The main row-level conflict is real, but the staged draft's description of the current converted Markdown is partly stale. The staged draft says the converted file records `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born 26 March 1888. The converted file currently on disk records entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888.
- The assigned chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at Calle de Valdivia. The source image visibly supports the broad Pulgar/Arriagada row over the converted file's Burgos/de la Cruz row, but this proof review should not rewrite the transcription layer.
- The exact father-name ending after `Pulgar` remains uncertain enough to require targeted conversion QA. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as possible outcomes until QA certifies the visible reading.
- The source packet repeats the stale converted-file conflict details (`Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz`), so dependent drafts should be revised after conversion QA to match the actual file state and source-visible row.

## Evidence Strengths

- The source type is a civil birth registration, which is strong direct evidence for a birth event, child name, parents as declared, registration date, residence, and informant when transcription is reliable.
- The assigned chunk and the source image agree on the controlling family-relevant row at entry 172 in broad terms: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888, father `Jose del Carmen Pulgar...`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`.
- The staged identity analysis correctly rejects any same-person treatment between the Pulgar/Arriagada row and the converted-file row, and correctly rejects a Dario-line identity bridge from this source alone.
- The analysis is appropriately cautious about `Juana Arriagada de Pulgar` and other Juana candidates; this source alone does not prove a merge with any separately staged or canonical Juana identity.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration is a high-quality original-style source for the recorded birth facts, though only a page image/derivative workflow was reviewed here. |
| conversion_confidence_score | 0.40 | The chunk and image broadly agree, but the converted file disagrees materially and the source packet/staged draft describe a stale version of that converted conflict. |
| evidence_quantity_score | 0.55 | One direct register entry supports the row; there is no corroborating independent source in this review scope. |
| agreement_score | 0.42 | Chunk and image agree on the Pulgar/Arriagada row, while the converted Markdown and stale conflict summaries disagree on names, dates, and parents. |
| identity_confidence_score | 0.66 | Moderate confidence for the Pulgar/Arriagada entry as a discrete row; lower for exact father-name form and any cross-document identity linkage. |
| claim_probability | 0.70 | The claim that entry 172 is a Pulgar/Arriagada birth registration is more likely than the converted-file row, based on the visible page and chunk, but still blocked by conversion inconsistency. |
| relevance_level | 0.90 | Highly relevant to Pulgar/Arriagada parent-candidate work if conversion QA confirms the row. |
| relevance_confidence | 0.82 | The surnames and parent/child structure are directly relevant; Dario-line relevance remains unproven. |
| canonical_readiness | 0.10 | Hold for conversion QA and revision before any canonical use. |

## Claim-Level Review

| Claim or inference | Review judgment | Probability | Notes |
| --- | --- | ---: | --- |
| Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada` as the child. | Hold, likely after QA. | 0.72 | Supported by chunk and visible source image; contradicted by converted Markdown. |
| Entry 172 names the father as `Jose del Carmen Pulgar S.`. | Hold for literal QA. | 0.55 | Base name is visible/plausible; final suffix or mark needs certification. |
| Entry 172 names the mother as `Juana Arriagada de Pulgar`. | Hold, likely after QA. | 0.72 | Supported by chunk and visible source image; blocked by derivative conflict. |
| The Pulgar/Arriagada row and converted-file Burgos/de la Cruz row are the same identity or variants. | Not supported. | 0.02 | Names, parents, dates, and row content differ materially. |
| Entry 172 provides a bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`. | Not supported. | 0.04 | The entry does not name Dario, Arturo, Smith, or a later-life context. |
| `Juana Arriagada de Pulgar` can be merged with another Juana candidate. | Not supported from this source alone. | 0.15 | Needs independent identity bridge beyond this entry. |

## Next Action

Run targeted conversion QA against the source image, current converted Markdown, current chunk, and source packet. The QA note should reconcile why the converted file now records a Burgos/de la Cruz row while the chunk and image support a Pulgar/Arriagada row, and should certify the father field only to the extent visible. After QA, revise the stale conflict descriptions and rerun proof review before promotion.
