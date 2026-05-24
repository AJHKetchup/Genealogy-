---
type: proof_review
status: draft
role: claim_reviewer
worker: postconv-proof-review-20260524143330194
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
reviewed_context:
  - research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Revision

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The staged draft accurately identifies a material conflict: the assigned converted Markdown still transcribes entry 172 as a different child-parent cluster, with child `José Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`, while the revised chunk, source packet, and visible image support a Pulgar/Arriagada row.
- The father field is not settled enough for canonical identity use. The revised chunk reads `Jose del Carmen Pulgar S.`, while the staged draft correctly leaves the suffix unresolved between `Jose del Carmen Pulgar` and `Jose del Carmen Pulgar S.`.
- Relationship promotion remains blocked. The source likely supports a child-parent cluster, but the unreconciled converted Markdown and father-suffix uncertainty make canonical person or relationship edits premature.
- The staged anti-conflation warning is necessary: this entry does not name Dario, Arturo, Smith, a spouse, a descendant, or any bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, or Dario passenger candidates.

## Scoring

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is an original-style direct source for the recorded birth entry, but image quality and handwriting leave some suffix uncertainty. |
| conversion_confidence_score | 0.48 | The revised chunk is consistent with the image, but the assigned converted Markdown is row-level wrong for entry 172. |
| evidence_quantity_score | 0.62 | One direct source image plus a revised chunk/source packet; no independent corroborating source reviewed in this task. |
| agreement_score | 0.50 | Image, revised chunk, and source packet agree on the Pulgar/Arriagada cluster, but the assigned converted Markdown materially conflicts. |
| identity_confidence_score | 0.76 | Good local confidence for the entry-172 child identity, reduced by conversion conflict and father-suffix uncertainty. |
| claim_probability | 0.82 | The visible page probably records `Jose del Carmen Segundo Pulgar Arriagada` with parents Jose del Carmen Pulgar and Juana Arriagada de Pulgar. |
| relevance_level | critical | The evidence directly concerns the Pulgar/Arriagada identity cluster and is also important as an anti-conflation guardrail. |
| relevance_confidence | 0.94 | The staged draft, source packet, chunk, and image all concern page 58, entry 172. |
| canonical_readiness | hold_for_conversion_qa | Promotion should wait for targeted conversion QA and father-suffix resolution. |

## Evidence Strengths

- The visible page image supports entry 172 as the Pulgar/Arriagada row on page 58, not the unrelated Gomez/de la Cruz cluster in the assigned converted Markdown.
- The revised chunk and source packet consistently identify the child as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
- The revised chunk and source packet support mother `Juana Arriagada de Pulgar` and informant `Ernesto Herrera L.`.
- The staged draft is appropriately cautious: it does not promote the father-name suffix as resolved and explicitly prevents attachment to Dario candidates by surname or family context alone.

## Review Judgment

Hold. The staged identity analysis is well supported as a conflict-aware review note and should remain in staging. The strongest current reading is that page 58, entry 172 probably records the birth of `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. That is a probability judgment, not canonical readiness, because the assigned converted Markdown still carries a different row and the father suffix remains unresolved.

## Next Action

Send to targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`. Reconcile or supersede `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` against the source image, and explicitly record whether the father field should be rendered as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical person, claim, or relationship promotion.
