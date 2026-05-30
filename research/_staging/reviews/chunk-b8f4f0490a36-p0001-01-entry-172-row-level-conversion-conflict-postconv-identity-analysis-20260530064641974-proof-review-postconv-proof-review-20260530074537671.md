---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530074537671
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

1. Do not promote a canonical birth claim or parent-child relationship from this staged draft. The assigned chunk and source packet support a Pulgar/Arriagada entry 172, but the converted Markdown assigns entry 172 to a different Burgos/de la Cruz child.
2. The original source PNG cited by the chunk, packet, and conversion review is not present under either cited `raw/sources/` filename variant in this checkout. This review therefore cannot certify the full physical row from the original page image.
3. The available staged crop supports the Pulgar/Arriagada parent and informant area, but it is only partial row evidence. It does not by itself resolve the row-control conflict against the converted Markdown.
4. The possible trailing mark after `Jose del Carmen Pulgar` is not promotion-ready. Preserve the literal uncertainty and do not expand or normalize the suffix.
5. No Dario-line identity bridge, Jose/Juana cluster merge, or same-person conclusion between Pulgar/Arriagada and Burgos/de la Cruz is supported by this evidence.

## Evidence Strengths

- The staged draft accurately reports a material conflict: the assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, while the converted file reads entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The source packet, chunk, and conversion review agree on the Pulgar/Arriagada staged reading: child `Jose del Carmen Segundo Pulgar Arriagada`, father field `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png` visibly supports the mother and informant readings and supports a father field beginning `Jose del Carmen Pulgar`.
- The staged draft correctly treats the Burgos/de la Cruz reading as a competing row-control artifact rather than as a name variant or identity bridge.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10: civil birth registration would be strong primary evidence, but the original page image is unavailable for this review and only derivative text plus partial crop context was checked. |
| conversion_confidence_score | 5/10: the assigned chunk is internally coherent and partially crop-supported, but the canonical converted Markdown materially conflicts with it. |
| evidence_quantity_score | 3/10: one disputed birth-register row, one source packet, one conversion review note, and partial crop support. |
| agreement_score | 4/10 overall: staged packet, chunk, and crop agree for Pulgar/Arriagada fields, but the converted file disagrees on the controlling entry 172 row. |
| identity_confidence_score | 7/10 for a staged Pulgar/Arriagada row reading; 2/10 for Burgos/de la Cruz controlling this staged Pulgar claim; 0/10 for any Dario identity bridge. |
| claim_probability | 0.70 that the staged Pulgar/Arriagada reading reflects the intended row; 0.25 that the Burgos/de la Cruz converted-file reading controls instead; 0.02 that both readings refer to the same person. |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | blocked: hold for original-image row-control QA before any canonical claim, relationship, identity merge, or wiki update. |

## Review Finding

The staged identity analysis is supported as a cautious hold/block recommendation. Its core warning is well founded: the local artifacts contain an unresolved row-control conflict, not a simple transcription variant.

The narrow Pulgar/Arriagada reading is plausible and partly supported by the staged crop, but this proof review cannot certify the full entry because the original source image is unavailable and the current converted Markdown names a different child and parents for entry `172`.

## Next Action

Route `CHUNK-b8f4f0490a36-P0001-01`, page 1/register page 58/entry 172, to targeted original-image row-control QA. That QA must decide whether entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row and must leave the father suffix after `Jose del Carmen Pulgar` uncertain unless the visible source clearly supports it.
