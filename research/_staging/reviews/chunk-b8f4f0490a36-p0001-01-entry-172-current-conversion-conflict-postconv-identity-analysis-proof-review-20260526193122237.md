---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526193122237
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526174903677.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526174903677.md
reviewed: 2026-05-26
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

1. Canonical readiness is blocked because the current converted Markdown records entry `172` as a Burgos/de la Cruz row, while the assigned chunk, staged source packet, staged conflict note, and visible source image support entry `172` as the Pulgar/Arriagada row.
2. This is a row-level conversion conflict, not a spelling, translation, or identity-variant issue. The two readings disagree on child, parents, birth date, birth time, birthplace/residence context, informant, and surrounding entries.
3. The father field in the Pulgar/Arriagada row should remain unresolved beyond `Jose del Carmen Pulgar`; the assigned chunk reads `Jose del Carmen Pulgar S.`, but the image review available here does not certify whether the trailing mark is `S.`, another letter/mark, or an artifact.
4. The staged draft correctly avoids promoting a bridge from this entry to any Dario Pulgar identity. The reviewed evidence does not name Dario, Arturo, Smith, or any later-life identifier that would support such a bridge.
5. No canonical claim, relationship, merge, or wiki update should be made from this staged draft until targeted conversion QA reconciles the current converted Markdown against the image and assigned chunk.

## Evidence Reviewed

- Staged identity-analysis draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526174903677.md`.
- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md`.
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

- source_quality_score: 0.88
- conversion_confidence_score: 0.42
- evidence_quantity_score: 0.76
- agreement_score: 0.52
- identity_confidence_score: 0.78 for the Pulgar/Arriagada row controlling entry `172`; 0.03 for same-person treatment with the Burgos/de la Cruz row; 0.05 for any Dario-identity bridge from this draft
- claim_probability: 0.74 that the physical entry `172` is the Pulgar/Arriagada row, held because the official converted Markdown remains contradictory
- relevance_level: high
- relevance_confidence: 0.98
- canonical_readiness: blocked

## Evidence Strengths

The staged identity-analysis draft is materially supported by the assigned chunk and staged source packet. Both preserve entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with mother `Juana Arriagada de Pulgar` and informant `Ernesto Herrera L.`.

The referenced page image visually supports the same row placement: entry `172` is on page 58 between entries `171` and `173`, and its row is visibly a Pulgar/Arriagada entry rather than the Burgos/de la Cruz text now present in the current converted Markdown.

The staged draft also correctly separates the identity-control problem from relationship promotion. It treats `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` as parent candidates only if conversion QA certifies the row, and it rejects an unsupported bridge to Dario-named Pulgar clusters.

## Reliability And Risk

The underlying source type is strong: a civil birth registration image. However, the derivative evidence is split because the current converted Markdown is internally coherent but appears to describe different entries than the assigned image/chunk. That keeps conversion confidence low for automated promotion even though the visible image favors the Pulgar/Arriagada row.

Identity risk is high if promoted prematurely. A wrong row-control decision would create false parent-child relationships and could contaminate later Pulgar/Arriagada identity work. Relationship-jump risk is also high for Dario-related candidates because this source does not name or identify any Dario person.

## Next Action

Hold this staged identity-analysis draft for targeted conversion QA. The QA should certify which physical row controls entry `172`, reconcile or replace the current converted Markdown if it is stale or row-shifted, and preserve the father field only to the visible/certified reading. After QA, rerun proof review before any canonical claim, relationship, merge, or wiki-page update.
