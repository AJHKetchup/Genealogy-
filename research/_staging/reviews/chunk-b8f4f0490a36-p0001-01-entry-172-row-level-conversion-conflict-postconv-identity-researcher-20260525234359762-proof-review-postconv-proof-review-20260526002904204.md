---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526002904204"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md"
output_area: "research/_staging/reviews/"
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

Review of staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md`.

## Blockers First

1. The reviewed draft correctly identifies a row-control conflict: the assigned chunk/source packet and visible source image place a Pulgar/Arriagada birth at entry 172, while the current converted Markdown places a Burgos/de la Cruz birth at entry 172.
2. This is not ready for canonical promotion. The converted Markdown is the referenced conversion artifact and materially disagrees with the source image and chunk on child name, parents, birth date, birth place, and informant.
3. The father field in the Pulgar/Arriagada reading remains a targeted transcription blocker. The visible source supports a father beginning `Jose del Carmen Pulgar`, but this review does not certify whether the trailing element is `S.`, another mark, or no suffix.
4. No child identity, birth fact, parent claim, parent-child relationship, parent merge, or Pulgar-to-Dario bridge should be promoted from this draft before conversion QA certifies the controlling row and father-field reading.
5. The draft's Dario/Pulgar comparison is relevant as anti-conflation context only. The source row reviewed here does not name Dario, Arturo, Smith, or any lineage bridge to Dario Arturo Pulgar-Smith or related Dario candidates.

## Evidence Reviewed

- Staged identity analysis: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md`.
- Staged conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

The source is a civil birth-registration image, which is a strong source type for a birth event and parent names. Visual review of page 58 shows row 172 as a Pulgar/Arriagada entry and aligns with the assigned chunk and source packet: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at Calle de Valdivia, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.

The converted Markdown instead gives entry 172 as `José Miguel`, father/informant `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. The converted artifact appears to describe a different set of rows than the source image and chunk. This supports the staged draft's central conclusion that the problem is conversion control, not ordinary identity variation.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is direct evidence for the row, though the review depends on a page image rather than a certified final conversion. |
| conversion_confidence_score | 0.38 | Assigned chunk and visible image agree, but the current converted Markdown conflicts materially with them. |
| evidence_quantity_score | 0.62 | One direct source image plus derivative chunk/source packet; no independent corroborating record reviewed for identity bridges. |
| agreement_score | 0.52 | Source image, chunk, source packet, and conflict draft agree on Pulgar/Arriagada; converted Markdown sharply disagrees. |
| identity_confidence_score | 0.55 | The row-level Pulgar/Arriagada identity is plausible from the image/chunk, but canonical person attachment remains blocked. |
| claim_probability | 0.63 | The claim that entry 172 in the source image is the Pulgar/Arriagada row is more likely than not; promotion-level claims remain lower until QA. |
| relevance_level | high | Directly controls Pulgar/Arriagada child identity, parent names, and parent-child relationship candidates. |
| relevance_confidence | 0.95 | The staged draft, chunk, source packet, and image all concern the same entry-172 conflict. |
| canonical_readiness | hold_for_conversion_qa | A targeted conversion QA note must certify the controlling row and father-field reading before canonical use. |

## Claim Probability Notes

The staged draft's recommendation to hold for conversion QA is supported. Its probabilities are generally conservative and appropriate. I would treat the Pulgar/Arriagada row-control hypothesis as moderately supported because the visible image, assigned chunk, and source packet agree, but I would not raise canonical readiness above hold while the official converted Markdown remains contradictory.

Relationship jumps are not supported. The reviewed materials do not prove that `Juana Arriagada de Pulgar` is identical to another Juana candidate, that the father should be merged to an existing Jose page, or that this row connects to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario J. Pulgar Arriagada.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, and converted Markdown. The QA note should explicitly decide whether the controlling entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, then certify the father field exactly as visible. After that, separate proof reviews can evaluate child identity, birth facts, parent claims, and any parent or Dario-line identity bridges.
