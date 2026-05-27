---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527144615754
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210041275.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210041275.md"
reviewed_sources:
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source_quality_score: 0.88
conversion_confidence_score: 0.34
evidence_quantity_score: 0.52
agreement_score: 0.22
identity_confidence_score: 0.56
claim_probability: 0.62
relevance_level: high_for_pulgar_arriagada_low_for_dario_bridge
relevance_confidence: 0.83
canonical_readiness: hold_for_conversion_qa
created: 2026-05-27
---

# Proof Review: Entry 172 Row Conflict

This proof review covers the staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210041275.md`.

## Blockers First

- Canonical readiness remains `hold_for_conversion_qa`. The assigned chunk/source-packet evidence and the assigned converted Markdown give incompatible entry 172 rows.
- The conflict is identity-bearing, not a spelling variant. The competing readings disagree on child name, parent names, birth date/time/place, informant, residence, and broader family relevance.
- The visible source image appears to support the Pulgar/Arriagada row at entry 172, but this proof-review task should not silently overwrite the converted Markdown or certify a corrected transcription. A targeted conversion QA note is still required.
- The father field remains unresolved. The chunk/source packet read `Jose del Carmen Pulgar S.`, but the final mark or suffix needs image-level certification before any canonical father claim or merge.
- No Dario bridge is supported by this entry. The reviewed materials do not name Dario, Arturo, Smith, Pulgar-Smith, or a later-life relationship/context connecting this row to any Dario candidate.

## Evidence Strengths

- The underlying source is a civil birth register image for Los Angeles, Chile, 1888, pages 58-59, entries 171-176. As a source type, it is strong for birth identity, parent names, registration date, and birth event claims once the row transcription is certified.
- The assigned chunk gives a coherent entry 172 for `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 1888-04-07, born 1888-03-08 at 3 p.m. on Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source packet accurately flags the derivative conflict and does not over-promote the Pulgar/Arriagada reading.
- The conflict draft correctly identifies that the converted Markdown instead gives entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 1888-04-06 at 10 p.m. in `En esta`.

## Judgment

The staged identity analysis is well supported as a conflict/hold analysis. It should not be promoted as a canonical person, parent-child relationship, or Dario-line bridge. The most probable explanation is a conversion or derivative-assignment problem in which the current converted Markdown does not match the page image/chunk row used by the source packet. That said, proof review should leave the correction boundary intact: the next worker must certify the controlling row and father-field text from the image rather than inheriting this note as a corrected transcription.

## Scores

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong primary-style source for the claimed event and relationships. |
| conversion_confidence_score | 0.34 | The chunk/source packet and converted Markdown conflict at row level; image appears to favor the chunk but QA has not certified the corrected conversion. |
| evidence_quantity_score | 0.52 | There is one direct source image and several derivative notes, but only one underlying record and no independent corroborating source. |
| agreement_score | 0.22 | Agreement is low because the assigned converted Markdown contradicts the chunk/source-packet row in every key identity field. |
| identity_confidence_score | 0.56 | Moderate confidence that the family-relevant row is Pulgar/Arriagada, but insufficient for canonical identity attachment while the conversion conflict remains open. |
| claim_probability | 0.62 | The Pulgar/Arriagada interpretation is more probable than the Burgos/de la Cruz interpretation for this staged packet, but the claim remains held. |
| relevance_level | high_for_pulgar_arriagada_low_for_dario_bridge | Relevant to Pulgar/Arriagada parent research; not direct evidence for any Dario candidate. |
| relevance_confidence | 0.83 | The surname/family relevance is clear if the Pulgar row controls; the lack of Dario evidence is also clear. |
| canonical_readiness | hold_for_conversion_qa | No canonical promotion, merge, relationship creation, or Dario attachment should occur before targeted conversion QA and rerun proof review. |

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned converted Markdown, chunk, and source packet. The QA note should certify whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row and should explicitly resolve the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim or relationship is promoted.
