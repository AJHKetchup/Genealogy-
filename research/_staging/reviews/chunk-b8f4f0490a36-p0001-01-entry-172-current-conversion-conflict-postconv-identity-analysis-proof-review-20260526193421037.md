---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526193421037
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526174903677.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526174903677.md
subject: "Entry 172, Los Angeles birth register, 1888"
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-26
---

# Proof Review: Entry 172 Current Conversion Conflict Identity Analysis

## Blockers First

1. Canonical readiness remains blocked because the current converted Markdown and the assigned chunk give incompatible rows for entry `172`.
2. The source image and assigned chunk support the Pulgar/Arriagada row for entry `172`, but the converted Markdown still records a Burgos/de la Cruz row under the same entry number. This is a row-control conflict, not a spelling or identity variant.
3. The father field for the Pulgar/Arriagada row is not fully certified. It visibly supports `Jose del Carmen Pulgar`, while the trailing character or mark after `Pulgar` requires targeted conversion QA before being used as a literal suffix.
4. The staged identity-analysis draft properly refuses to bridge this entry to any Dario Pulgar identity. No reviewed source in this task names Dario, Arturo, Smith, or a later Pulgar-Arriagada identity.
5. No relationship, identity merge, or canonical claim should be promoted from this staged draft until conversion QA certifies the controlling row and the father-field reading.

## Evidence Checked

- Reviewed staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526174903677.md`.
- Referenced conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md`.
- Referenced assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| Metric | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong primary source for the event, but this review depends on a difficult image and derivative conversions. |
| conversion_confidence_score | 0.42 | The assigned chunk aligns with the image for entry `172`; the current converted Markdown conflicts materially and keeps conversion confidence low overall. |
| evidence_quantity_score | 0.70 | One primary source image plus two conflicting derivative transcriptions are enough to identify the conflict, not enough to promote dependent claims. |
| agreement_score | 0.46 | Source image, chunk, staged packet, and conflict note agree on Pulgar/Arriagada, but the converted Markdown sharply disagrees. |
| identity_confidence_score | 0.78 | The Pulgar/Arriagada row appears to be the stronger reading for physical entry `172`, subject to conversion QA. Same-person linkage to Burgos/de la Cruz or Dario identities is unsupported. |
| claim_probability | 0.74 | Probable that entry `172` is the Pulgar/Arriagada row, but not canonical-ready while row control remains unresolved in the conversion set. |
| relevance_level | high | The draft is directly relevant to Pulgar/Arriagada identity and relationship claims and to preventing an incorrect merge or promotion. |
| relevance_confidence | 0.98 | The staged draft and reviewed files all concern the same entry number, image, chunk, and conversion conflict. |
| canonical_readiness | blocked | Hold for targeted conversion QA before any promotion, merge, or relationship update. |

## Evidence Strengths

- The staged draft accurately identifies the core conflict: entry `172` is Pulgar/Arriagada in the assigned chunk and Burgos/de la Cruz in the current converted Markdown.
- The page image visibly supports entry `172` on page 58 as a Pulgar/Arriagada row, consistent with the assigned chunk's child, mother, informant, date, and place readings.
- The draft correctly treats the two readings as mutually incompatible rows rather than as variants of one person.
- The draft appropriately keeps the Dario Pulgar comparison as a guardrail and does not convert it into a relationship or same-person claim.
- The draft's recommendation for targeted conversion QA is proportionate to the conflict and protects against overpromotion.

## Review Notes

- The Pulgar/Arriagada claim has stronger support than the Burgos/de la Cruz claim for the visible source image reviewed here, but this proof review should not overwrite or correct the converted Markdown.
- The father field should be cited conservatively as `Jose del Carmen Pulgar` with an unresolved trailing mark until a conversion-QA reviewer certifies whether the visible source supports `S.`, another suffix, or no suffix.
- The staged draft's scores are directionally appropriate. This proof review keeps the same conclusion: high relevance, moderate-to-high probability for the Pulgar row, low overall conversion confidence, and blocked canonical readiness.

## Next Action

Run targeted conversion QA against the source image, assigned chunk, current converted Markdown, and staged source packet. The QA note should certify the physical row controlling entry `172`, explain why the converted Markdown differs, and resolve the father-field suffix only to the visible extent. After that QA note exists, rerun proof review before any canonical claim, relationship, merge, or wiki update.
