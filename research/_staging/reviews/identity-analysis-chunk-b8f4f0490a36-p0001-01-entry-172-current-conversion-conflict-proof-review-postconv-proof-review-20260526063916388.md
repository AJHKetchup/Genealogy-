---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526063916388
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044220967.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044220967.md"
reviewed_sources:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.88
conversion_confidence_score: 0.35
evidence_quantity_score: 0.70
agreement_score: 0.45
identity_confidence_score: 0.62
claim_probability: 0.68
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged identity-analysis draft is directionally supported, but canonical use remains blocked because the referenced converted Markdown and referenced chunk give materially different readings for the same source, page, and entry number.
2. The current converted Markdown reads entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the chunk, source packet, and visible page image instead support a Pulgar/Arriagada row for entry 172. This is a row-level conversion conflict, not a spelling variant.
3. The father field should not be normalized beyond the visible/supporting evidence in this proof review. The chunk gives `Jose del Carmen Pulgar S.`, while the page image supports `Jose del Carmen Pulgar` at minimum and leaves any suffix or following mark insufficiently proof-ready here.
4. No Dario-line bridge is supported by this source. The staged draft correctly treats Dario relevance as anti-conflation context only.
5. Do not promote any child identity, parent-child relationship, parent merge, or canonical wiki update from this draft until the converted Markdown is corrected or targeted conversion QA certifies the controlling entry-172 row and father-field reading.

## Evidence Strengths

- The source is a civil birth register image with a specific page and entry number, which is a strong source type for birth identity, birth date, parent names, and informant when the row transcription is settled.
- The referenced chunk and source packet agree that page 58, entry 172 concerns `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 1888-04-07, born 1888-03-08 at 3 p.m. on Calle de Valdivia, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The visible page image supports the staged draft's main conflict claim: entry 172 on page 58 is visibly a Pulgar/Arriagada row, while the converted Markdown's Burgos/de la Cruz row is not the visible entry 172 on this page image.
- The staged draft appropriately identifies the conflict as blocking canonical promotion and avoids upgrading same-cluster canonical pages into independent corroboration.

## Scores And Judgment

| Category | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration image, source-linked and entry-specific; strong primary-source type. |
| conversion_confidence_score | 0.35 | The visible image favors the chunk/source-packet reading, but the current converted Markdown remains contradictory and needs formal correction or QA certification. |
| evidence_quantity_score | 0.70 | One primary source image plus two derivative local readings; sufficient to identify the conflict, not sufficient for canonical promotion while conversion state is unresolved. |
| agreement_score | 0.45 | Chunk, source packet, and image broadly agree; converted Markdown sharply disagrees. |
| identity_confidence_score | 0.62 | Pulgar/Arriagada identity is the best-supported row reading, but father suffix and conversion conflict keep identity proof below promotion level. |
| claim_probability | 0.68 | Probability that entry 172 is the Pulgar/Arriagada birth row is moderately high based on the visible image and chunk agreement. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent candidates; only indirectly relevant to Dario anti-conflation. |
| relevance_confidence | 0.90 | The source and staged draft are plainly relevant to the named Pulgar/Arriagada issue. |
| canonical_readiness | hold_for_conversion_qa | Review supports hold/revise workflow, not canonical promotion. |

## Claim Review

- Claim that a material row-level conflict exists: supported. The converted Markdown and chunk/source packet do not describe the same entry-172 row.
- Claim that the Pulgar/Arriagada row is the stronger current hypothesis: supported with moderate confidence. The visible image aligns with the chunk/source-packet reading for entry 172.
- Claim that father identity is proof-ready as `Jose del Carmen Pulgar S.`: hold. The chunk transcribes this, but the visible image does not make the suffix sufficiently certain for this review to certify it.
- Claim that mother is `Juana Arriagada de Pulgar`: supported at the row-reading level, but hold for canonical promotion until conversion QA resolves the entry-level conflict.
- Claim that this source supports a Dario identity bridge: not supported. Any Dario comparison should remain a later anti-conflation review after the entry-172 row is certified.

## Next Action

Run targeted conversion QA or conversion correction for the referenced converted Markdown against the page image and chunk. The QA/correction should explicitly decide the controlling entry-172 row and preserve the father field as one of: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review for the child identity, birth facts, parent claims, and parent-child relationships before any canonical update.
