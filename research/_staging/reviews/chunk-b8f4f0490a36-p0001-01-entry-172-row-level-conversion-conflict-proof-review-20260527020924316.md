---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260527020924316
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000231135.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000231135.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_reconciliation
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical promotion must remain on hold because the referenced converted Markdown materially conflicts with the visible source image and assigned chunk. It records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the visible page 58 row and assigned chunk support the Pulgar/Arriagada entry.
2. The father suffix is not promotion-ready. The chunk reads `Jose del Carmen Pulgar S.`, but the targeted QA note certifies only `Jose del Carmen Pulgar`; the visible image does not justify promoting the suffix as a definite part of the name.
3. No Dario-line bridge is supported. The reviewed source names `Jose del Carmen Segundo Pulgar Arriagada` and his parents; it does not name any Dario/Darío candidate or provide a relationship path to one.
4. No merge is supported between `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`. This source supports only the former reading for this entry.

## Evidence Scores

- source_quality_score: 0.86
- conversion_confidence_score: 0.72
- evidence_quantity_score: 0.74
- agreement_score: 0.70
- identity_confidence_score: 0.84 for physical entry `172` as the Pulgar/Arriagada birth row
- claim_probability: 0.84 that the controlling visible entry `172` records `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888, son of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`
- relevance_level: high
- relevance_confidence: 0.94
- canonical_readiness: hold_for_conversion_reconciliation

## Evidence Strengths

The staged draft is materially supported by the referenced source packet, targeted conversion QA note, assigned chunk, and visible source image. The image shows entry `172` as the middle row on page 58, and the row-level content aligns with the Pulgar/Arriagada reading rather than the Burgos/de la Cruz reading in the converted Markdown.

The staged draft correctly keeps the conflict scoped as a conversion/row-control problem and does not over-promote the father suffix, parent merges, or Dario-line identity bridges. Its claim probabilities are reasonable for a proof-review hold rather than a canonical-ready conclusion.

## Judgment

Revise/hold, not promote. Accept the staged draft's main proof judgment that the physical row controls as the Pulgar/Arriagada entry, but keep canonical readiness on hold until conversion-control reconciles or corrects the stale converted Markdown. If promoted later, the safe claim scope is limited to the visible row reading: child `Jose del Carmen Segundo Pulgar Arriagada`; father `Jose del Carmen Pulgar`; mother `Juana Arriagada de Pulgar`; registration date 7 April 1888; birth date/time 8 March 1888 at 3 p.m.; birthplace `Calle de Valdivia`.

## Next Action

Send to conversion-control for correction or explicit quarantine of the mismatched converted Markdown. After that, rerun promotion only for narrow Entry 172 claims and relationships. Do not promote the `S.` suffix, merge Juana candidates, or attach any Dario-line identity from this source.
