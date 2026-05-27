---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260527015750341
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md
reviewed_status: hold_for_conversion_reconciliation
source_quality_score: 0.88
conversion_confidence_score: 0.70
evidence_quantity_score: 0.72
agreement_score: 0.74
identity_confidence_score: 0.83
claim_probability: 0.86
relevance_level: high
relevance_confidence: 0.96
canonical_readiness: hold
created: 2026-05-27
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical readiness is `hold`. The page image, assigned chunk, source packet, and targeted QA note support the Pulgar/Arriagada row as physical Entry `172`, but the referenced converted Markdown still records Entry `172` as a Burgos/de la Cruz birth entry.
2. The father field is not fully promotion-ready. The row supports `Jose del Carmen Pulgar`; the chunk's added `S.` remains too uncertain to promote without a separate image-level certification.
3. The review does not support any Dario-line identity bridge. The source row names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario Pulgar Arriagada.
4. The mother reading `Juana Arriagada de Pulgar` should not be merged with `Juana de Dios Amagada de Pulgar` from separate wiki context. This entry alone gives no direct bridge between those candidates.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md`.
- Targeted QA note: `research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong direct source for the row; image scale and handwriting still limit the final father suffix. |
| conversion_confidence_score | 0.70 | The targeted QA note and assigned chunk align with the visible row, but the canonical converted Markdown remains materially wrong for Entry `172`. |
| evidence_quantity_score | 0.72 | One source image plus chunk, source packet, and targeted QA are enough for a bounded row-control judgment; not enough for broader identity merges. |
| agreement_score | 0.74 | Image, chunk, packet, and QA note agree on the Pulgar/Arriagada row; the converted Markdown is a direct outlier. |
| identity_confidence_score | 0.83 | `Jose del Carmen Segundo Pulgar Arriagada` is strongly supported as the child in physical Entry `172`; parent identities remain scoped to the row wording. |
| claim_probability | 0.86 | The staged draft's main claim, that physical Entry `172` is Pulgar/Arriagada while the converted Markdown conflicts, is well supported. |
| relevance_level | high | The row directly concerns Pulgar/Arriagada birth and parent evidence. |
| relevance_confidence | 0.96 | The reviewed materials consistently identify this as the same Entry `172` conflict. |
| canonical_readiness | hold | Accept only as staged proof-review evidence until the derivative converted Markdown conflict is retained or corrected through conversion control. |

## Evidence Strengths

- The visible source image shows Entry `172` on page 58 in the second row and supports the Pulgar/Arriagada row structure used by the assigned chunk and targeted QA note.
- The targeted QA note appropriately separates the certified father reading `Jose del Carmen Pulgar` from the uncertain suffix in the chunk.
- The staged identity analysis correctly treats Dario-related names and Juana-name variants as anti-conflation guardrails, not as supported identity or relationship claims.
- The derivative converted Markdown conflict is explicitly documented rather than silently harmonized.

## Next Action

Keep this staged item on hold for canonical promotion until the conversion-control process either corrects the converted Markdown or explicitly preserves it as a known derivative error. After reconciliation, promote only narrowly scoped claims from physical Entry `172`: child name, birth details, recorded father as `Jose del Carmen Pulgar`, recorded mother as `Juana Arriagada de Pulgar`, and declarant details. Do not promote the father suffix, merge Juana candidates, or attach any Dario-line identity without separate direct evidence.
