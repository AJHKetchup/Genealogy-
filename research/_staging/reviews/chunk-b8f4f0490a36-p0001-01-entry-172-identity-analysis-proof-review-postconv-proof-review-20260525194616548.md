---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525194616548
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525122440361.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525122440361.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
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

- Keep this staged identity analysis at `hold_for_conversion_qa`; do not promote any identity claim, parent-child relationship, parent merge, or Dario-line attachment from this draft.
- The staged draft and source packet contain a stale or unsupported description of the current converted Markdown. They say the converted file records `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, and a 26 March 1888 birth. The converted file currently on disk records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and birth on 6 April 1888.
- The row-level conflict remains material even after correcting that description: the current chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at Calle de Valdivia. The current converted Markdown records a different child, parents, date, and place.
- The source image visibly supports the broad Pulgar/Arriagada row for entry 172 over the converted-file Burgos/de la Cruz row, but this review should not edit or supersede the transcription layer.
- The final mark or suffix after the father's name remains uncertain enough for QA. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as possible literal outcomes until a conversion QA note certifies the visible reading.

## Evidence Strengths

- The reviewed source is a civil birth register image, a strong source class for a birth event, declared parents, registration date, residence, and informant when the row is correctly transcribed.
- The current chunk and visible source image agree in broad terms that entry 172 is the Pulgar/Arriagada birth row: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at Calle de Valdivia, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The staged analysis correctly treats the Pulgar/Arriagada row and the converted-file row as mutually exclusive row readings, not name variants.
- The staged analysis appropriately rejects a Dario-line bridge from this entry alone. No reviewed source in scope names Dario, Arturo, Smith, or a later-life identity anchor.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration image is high-quality original-style evidence for the recorded birth facts; image legibility is usable, though the father-name ending is not fully settled. |
| conversion_confidence_score | 0.40 | The chunk and source image broadly agree, but the converted Markdown conflicts materially and the staged draft/source packet describe a stale version of that conflict. |
| evidence_quantity_score | 0.55 | One direct register row is in scope; no independent corroborating source was reviewed for identity linkage. |
| agreement_score | 0.42 | Chunk and image agree on the Pulgar/Arriagada row, while the converted Markdown and stale conflict descriptions disagree on child, parents, dates, and places. |
| identity_confidence_score | 0.66 | Moderate confidence for the Pulgar/Arriagada row as a local birth entry; lower for exact father-name form and any cross-document identity bridge. |
| claim_probability | 0.70 | The Pulgar/Arriagada reading is more probable than the converted-file row after image review, but not proof-ready until conversion QA reconciles the derivatives. |
| relevance_level | 0.90 | Highly relevant to Pulgar/Arriagada parent-child and parent-candidate work if QA confirms the row. |
| relevance_confidence | 0.82 | The row directly contains Pulgar and Arriagada names; broader Dario-line relevance remains unproven. |
| canonical_readiness | 0.10 | Hold for conversion QA and revision before any canonical use. |

## Claim-Level Review

| Claim or inference | Review judgment | Probability | Notes |
| --- | --- | ---: | --- |
| Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada` as the child. | Hold, likely after QA. | 0.72 | Supported by the chunk and visible source image; contradicted by the converted Markdown. |
| Entry 172 names the father as `Jose del Carmen Pulgar S.`. | Hold for literal QA. | 0.55 | The base name is supported/plausible from chunk and image; the final suffix or mark needs targeted certification. |
| Entry 172 names the mother as `Juana Arriagada de Pulgar`. | Hold, likely after QA. | 0.72 | Supported by chunk and visible source image; blocked by derivative conflict. |
| The Pulgar/Arriagada row and converted-file Burgos/de la Cruz row are the same identity or minor variants. | Not supported. | 0.02 | Child, parents, dates, and row content differ materially. |
| Entry 172 provides a bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. | Not supported. | 0.04 | No reviewed item in scope names Dario or provides a later identity bridge. |
| `Juana Arriagada de Pulgar` can be merged with another Juana candidate. | Not supported from this source alone. | 0.15 | Needs independent identity evidence beyond this entry. |

## Next Action

Run targeted conversion QA against the source image, current converted Markdown, current chunk, and source packet. The QA note should reconcile why the converted file records a Burgos/de la Cruz row while the chunk and image support a Pulgar/Arriagada row, and it should certify the father field only to the extent visible. After QA, revise the stale conflict descriptions and rerun proof review before promotion.
