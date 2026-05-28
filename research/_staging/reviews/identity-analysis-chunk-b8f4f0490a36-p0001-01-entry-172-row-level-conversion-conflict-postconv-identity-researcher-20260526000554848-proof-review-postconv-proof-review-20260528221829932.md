---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260528221829932"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: "hold"
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

1. The staged draft is correct that the assigned entry has a controlling row-level conversion conflict. The chunk and source packet identify entry 172 as a Pulgar/Arriagada birth registration, while the current converted Markdown identifies entry 172 as a Burgos/de la Cruz birth registration.
2. The source image supports the Pulgar/Arriagada row-control reading for page 58, entry 172, but the father-field suffix after `Jose del Carmen Pulgar` remains too uncertain for canonical promotion without targeted conversion QA.
3. No child identity, birth fact, parent-child relationship, parent identity merge, or Pulgar/Arriagada-to-Dario bridge is ready for canonical use from this staged draft.
4. The staged draft includes contextual references to existing wiki pages. This review did not use those canonical pages as proof because the row-control question is resolved enough from the cited source image, chunk, source packet, and converted Markdown; any canonical-page reconciliation still needs a separate proof review.

## Evidence Strengths

- The source type is a civil birth registration, which is high-quality direct evidence for a birth row when the row is correctly controlled.
- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father read as `Jose del Carmen Pulgar S.` and mother as `Juana Arriagada de Pulgar`.
- The source packet explicitly reports a visual source-image check and recommends `hold_for_conversion_qa`.
- Direct inspection of the cited source image shows page 58, entry 172 as the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the current converted Markdown.
- The staged draft handles the Dario/Pulgar comparisons as anti-conflation checkpoints rather than as promoted identity bridges, which is supported by the absence of a Dario, Arturo, Smith, spouse, descendant, or chronology bridge in the cited entry.

## Scored Judgment

| Metric | Score / Level | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration image is a strong source for the row, but the review is still affected by the existing conversion disagreement. |
| conversion_confidence_score | 0.42 | The assigned chunk is coherent and visually plausible, but the canonical converted Markdown materially disagrees. |
| evidence_quantity_score | 0.68 | One source image, one chunk, one source packet, and one conflicting converted file are enough to identify the conflict, not enough to promote identities. |
| agreement_score | 0.46 | Source image, chunk, and source packet agree on Pulgar/Arriagada; converted Markdown sharply disagrees. |
| identity_confidence_score | 0.70 | The row likely concerns the Pulgar/Arriagada family, but exact father-name reading and downstream identity attachment remain unresolved. |
| claim_probability | 0.74 | The main claim that entry 172 is a Pulgar/Arriagada row-control conflict is probable and visibly supported. |
| relevance_level | high | The evidence directly concerns the assigned staged draft and entry number. |
| relevance_confidence | 0.96 | The cited files and image all point to the same page/reference set. |
| canonical_readiness | hold | Do not promote until targeted conversion QA certifies row control and the father field. |

## Claim Review

- Claim reviewed: entry 172 should be held because the Pulgar/Arriagada chunk/source-image reading conflicts with the Burgos/de la Cruz converted Markdown reading.
  - Judgment: supported.
  - Claim probability: 0.74.
  - Canonical readiness: hold.

- Claim reviewed: if the Pulgar/Arriagada row is certified, the row may support `Jose del Carmen Segundo Pulgar Arriagada` as child of `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
  - Judgment: conditionally supported.
  - Claim probability: 0.58 until row-control and father-field QA are complete.
  - Canonical readiness: hold.

- Claim reviewed: this row bridges to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Darío Pulgar Arriagada.
  - Judgment: not supported by the cited entry.
  - Claim probability: 0.04.
  - Canonical readiness: not ready.

## Next Action

Keep the staged draft on hold and route the cited source image, chunk, and converted Markdown to targeted conversion QA. QA should certify whether entry 172 is the Pulgar/Arriagada row and record the father field exactly as visible, especially the trailing element after `Jose del Carmen Pulgar`.
