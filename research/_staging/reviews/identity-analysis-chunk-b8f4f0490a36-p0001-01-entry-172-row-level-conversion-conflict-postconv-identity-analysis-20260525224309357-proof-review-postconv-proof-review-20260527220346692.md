---
type: proof_review
status: hold
role: claim_reviewer
worker: "postconv-proof-review-20260527220346692"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525224309357.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525224309357.md"
reviewed: "2026-05-27"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The staged draft is supported as a conflict analysis, but it is not ready to promote any child identity, birth fact, parent-child relationship, parent identity merge, or Dario-line bridge.
- The referenced chunk and source packet identify entry 172 as the Pulgar/Arriagada row. The referenced converted Markdown identifies entry 172 as a Burgos/de la Cruz row. These are materially different families, dates, places, and informants.
- The page image reviewed for verification context visually favors the chunk/source-packet row for entry 172, but the converted Markdown remains the recorded conversion layer and must be corrected or superseded by targeted conversion QA before canonical use.
- The father reading in the Pulgar-row layer remains uncertified beyond the staged alternatives. Do not silently normalize `Jose del Carmen Pulgar S.` to `Jose del Carmen Pulgar`.
- No visible evidence in this task supports changing, merging, or promoting any Dario Arturo Pulgar, Dario Arturo Pulgar-Smith, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada identity.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525224309357.md`.
- Conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| Review target | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| Staged draft's central claim that a row-level conversion conflict exists | 0.88 | 0.34 | 0.82 | 0.18 | 0.72 | 0.93 | high | 0.96 | hold_for_conversion_qa |
| Pulgar/Arriagada row as the likely visible entry 172 in the source image | 0.88 | 0.58 | 0.74 | 0.72 | 0.70 | 0.78 | high | 0.95 | hold_for_conversion_qa |
| Burgos/de la Cruz row as the controlling entry 172 for this source image | 0.55 | 0.28 | 0.42 | 0.15 | 0.25 | 0.18 | medium | 0.80 | not_ready |
| `Jose del Carmen Segundo Pulgar Arriagada` child identity from this draft | 0.86 | 0.55 | 0.70 | 0.66 | 0.68 | 0.70 | high | 0.94 | hold_for_conversion_qa |
| `Jose del Carmen Pulgar` father candidate from this draft | 0.82 | 0.42 | 0.58 | 0.52 | 0.45 | 0.46 | high | 0.90 | not_ready |
| `Juana Arriagada de Pulgar` mother candidate from this draft | 0.84 | 0.54 | 0.64 | 0.62 | 0.62 | 0.64 | high | 0.91 | hold_for_conversion_qa |
| Any Dario-line identity or relationship bridge from this draft | 0.50 | 0.30 | 0.12 | 0.08 | 0.05 | 0.04 | low | 0.86 | not_ready |

## Evidence Strengths

- The staged draft accurately preserves the central conflict: the chunk/source-packet layer and the converted Markdown layer do not describe the same entry 172 family.
- The chunk, source packet, and source image align at the review level with the Pulgar/Arriagada reading for entry 172. This strengthens the probability that the converted Markdown is misaligned or stale.
- The draft correctly treats the conflict as row-control/conversion-control, not as a name variant or same-person proof problem.
- The draft appropriately blocks Dario-line attachment and parent merge work because the entry does not name Dario and does not provide a lineage bridge to Dario Arturo Pulgar-Smith or other Dario candidates.

## Risks And Uncertainty

- The converted Markdown is still a referenced conversion product for this source and explicitly gives a different entry 172. Until QA resolves that layer, derived claims remain unsafe for canonical folders.
- The father-field suffix or mark in the Pulgar-row layer needs a focused reread before any father identity attachment.
- A visual review in this proof note is verification context only. It should not substitute for a targeted conversion QA note that reconciles or replaces the conflicting converted Markdown.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, chunk, source packet, and converted Markdown. The QA note should decide whether the active entry 172 conversion controls as the Pulgar/Arriagada row and should explicitly certify the father field only to the visible extent.

After QA, rerun proof review before promoting any child identity, birth event, parent relationship, parent merge, or Dario-line comparison. Current disposition: hold.
