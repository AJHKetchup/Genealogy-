---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260526022046811
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
created: "2026-05-26"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict Identity Analysis

## Blockers First

1. Row-control remains blocked. The staged identity analysis, source packet, chunk, and visible source image support entry 172 on page 58 as a Pulgar/Arriagada row, while the referenced converted Markdown records a different Burgos/de la Cruz row for entry 172. This conflict affects the child, parents, birth date, place, informant, and downstream identity conclusions.
2. The father suffix is not fully certified by this proof review. The visible image supports the father-name field beginning `Jose del Carmen Pulgar`; the trailing mark or suffix should remain unresolved among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA.
3. The staged draft correctly blocks Dario-line attachment. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`; it does not itself identify any Dario candidate or bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.
4. Parent-identity merging is not ready. The entry may eventually support child-parent claims for the Pulgar/Arriagada family, but it does not prove duplicate identity between existing Jose/Juana clusters or resolve `Arriagada` versus `Amagada`.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source type is strong: a civil birth register page is direct evidence for a birth entry when the row is controlled.
- The visible source image supports the packet/chunk claim that page 58 entry 172 is for `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. on Calle de Valdivia, with mother `Juana Arriagada de Pulgar` and informant `Ernesto Herrera L.`.
- The staged identity analysis accurately treats the Burgos/de la Cruz converted-file reading as a row-level conversion conflict rather than as an ordinary name/date variant.
- The staged identity analysis uses appropriate anti-conflation guardrails for Dario candidates and Jose/Juana parent candidates.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a high-quality source for row-level birth facts, but this review does not certify every ambiguous name suffix. |
| conversion_confidence_score | 0.42 | The assigned chunk aligns with the image, but the referenced converted Markdown materially contradicts it. |
| evidence_quantity_score | 0.68 | There is one direct source image plus a chunk and source packet; no independent corroborating source was reviewed for identity merges. |
| agreement_score | 0.52 | Staged draft, packet, chunk, and image agree on the Pulgar/Arriagada row, but the converted Markdown disagrees sharply. |
| identity_confidence_score | 0.72 | Probable that the row is for `Jose del Carmen Segundo Pulgar Arriagada`; low for any broader same-person or parent-duplicate conclusion. |
| claim_probability | 0.70 | The row-control claim favoring Pulgar/Arriagada is probable, but not ready while conversion QA remains unresolved. |
| relevance_level | high | Highly relevant to Pulgar/Arriagada child-parent research and as an anti-conflation checkpoint. |
| relevance_confidence | 0.90 | The surnames and row contents make relevance clear if the row is certified. |
| canonical_readiness | hold | Do not promote claims, relationships, merges, or Dario comparisons until targeted conversion QA resolves the row and father field. |

## Claim Probability By Issue

| Issue | Probability | Canonical Readiness |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada row on page 58 | 0.70 | Hold for targeted conversion QA. |
| Current converted Markdown's Burgos/de la Cruz entry controls this source packet | 0.15 | Not ready; contradicted by image/chunk/packet. |
| Father field can be promoted as exactly `Jose del Carmen Pulgar S.` | 0.55 | Hold; visible start is stronger than suffix certification. |
| Entry supports a Dario candidate same-person claim | 0.03 | Not ready; unsupported. |
| Entry supports merging Jose/Juana parent clusters | 0.20 | Not ready; requires separate proof review after row QA. |

## Next Action

Targeted conversion QA should certify the controlling row for entry 172 against the source image and reconcile or replace the contradictory converted Markdown. The QA note should separately record the father field to the visible extent, then rerun proof review for any child identity, birth fact, parent-name, parent-child relationship, or parent-merge claims. Until then, keep this staged identity analysis at `hold_for_conversion_qa` and do not promote to canonical folders.
