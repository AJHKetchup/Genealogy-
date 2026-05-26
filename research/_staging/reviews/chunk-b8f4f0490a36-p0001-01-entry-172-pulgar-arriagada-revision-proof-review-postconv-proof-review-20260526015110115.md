---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526015110115
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
review_decision: hold
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers First

- Keep the staged draft at `hold_for_conversion_qa`; do not promote any child identity, birth fact, parent-child relationship, parent merge, or Dario-line comparison from this draft.
- The staged draft correctly identifies a row-level conflict, but its description of the current converted Markdown is stale. The staged draft says the converted file transcribes entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 20 February 1888 at Pellin. The converted file currently on disk transcribes entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888.
- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at Calle de Valdivia. The visible source image broadly supports the Pulgar/Arriagada row rather than the converted-file Burgos/de la Cruz row, but this review must not rewrite the conversion layer.
- The exact ending after the father's name `Pulgar` remains a literal-reading issue. Treat `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` as unresolved until targeted conversion QA certifies the visible source.
- The source packet repeats the older converted-file conflict description (`Jose Francisco` / `Oswaldo Gomez` / `Rosario de la Cruz de la Maza`), so the packet and staged identity analysis both need revision after conversion QA.

## Evidence Strengths

- The source is a civil birth registration page image, a strong source type for birth registration facts when the row and transcription are settled.
- The assigned chunk and visible source image agree in broad terms that page 58, entry 172 is a Pulgar/Arriagada birth entry with child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged draft properly avoids attaching this record to any Dario identity. The entry does not name Dario, Arturo, Smith, or any later-life identifying context.
- The staged draft's caution around parent-candidate merges is appropriate. This one entry can support a local family cluster only after transcription QA; it cannot independently merge broader Pulgar or Arriagada identities.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is high-quality direct evidence for the recorded birth facts, though reviewed here through a page image and derivative files. |
| conversion_confidence_score | 0.38 | The chunk and image broadly align, but the converted Markdown materially disagrees and the staged draft/source packet describe a stale version of that disagreement. |
| evidence_quantity_score | 0.55 | One direct register entry is in scope; no independent corroborating record was reviewed. |
| agreement_score | 0.40 | Source image and chunk agree on the Pulgar/Arriagada row, while the converted file and stale conflict descriptions disagree on names, dates, and parents. |
| identity_confidence_score | 0.66 | Moderate confidence that the visible row is a discrete Pulgar/Arriagada birth entry; lower confidence for exact father-name form and any cross-record identity linkage. |
| claim_probability | 0.70 | The Pulgar/Arriagada interpretation is more probable than the converted-file row based on the visible image and chunk, but promotion is blocked by conversion conflict. |
| relevance_level | 0.90 | Highly relevant to Pulgar/Arriagada family reconstruction if QA confirms the row. |
| relevance_confidence | 0.82 | Surnames and parent-child structure are directly relevant; Dario-line relevance remains unsupported. |
| canonical_readiness | 0.10 | Hold for conversion QA, source-packet revision, and rerun proof review before canonical use. |

## Claim-Level Review

| Claim or inference | Review judgment | Probability | Notes |
| --- | --- | ---: | --- |
| Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada` as the child. | Hold, likely after QA. | 0.72 | Supported by the chunk and visible image; contradicted by the current converted Markdown. |
| Entry 172 names the father as `Jose del Carmen Pulgar S.`. | Hold for literal QA. | 0.55 | The base Pulgar reading is plausible from the image; the final suffix/mark needs certification. |
| Entry 172 names the mother as `Juana Arriagada de Pulgar`. | Hold, likely after QA. | 0.72 | Supported by the chunk and visible image; blocked by derivative-file conflict. |
| Entry 172 names informant `Ernesto Herrera L.` as present at the birth. | Hold, likely after QA. | 0.70 | Supported by the chunk and visible image, subject to the same conversion conflict. |
| The Pulgar/Arriagada row and the converted-file Burgos/de la Cruz row are variants of the same identity cluster. | Not supported. | 0.02 | Child name, parents, birth date, and contextual details differ materially. |
| This source identifies or bridges any Dario Pulgar candidate. | Not supported. | 0.04 | The record does not name Dario and supplies no later-life identity bridge. |
| `Juana Arriagada de Pulgar` can be merged with another Juana candidate. | Not supported from this source alone. | 0.15 | Requires independent identity evidence beyond this single entry. |

## Next Action

Run targeted conversion QA against the visible source image, current converted Markdown, current chunk, and source packet. The QA note should identify the controlling row for entry 172, explain why the converted Markdown currently records a Burgos/de la Cruz row while the chunk/image support a Pulgar/Arriagada row, and certify the father field only to the degree visible. After that, revise the stale source packet and staged identity analysis, then rerun proof review before any canonical promotion.
