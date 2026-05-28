---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528195042394
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528172745327.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528172745327.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528170150642.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528170150642.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote the current converted Markdown's entry `172` Burgos/de la Cruz reading as the controlled row for this task. The visible source image, assigned chunk, source packet, and targeted QA note support the physical entry `172` row on page 58 as a Pulgar/Arriagada birth registration.
2. Do not promote the father-name suffix after `Pulgar`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the targeted image-control QA certifies only `Jose del Carmen Pulgar`.
3. Do not promote any Dario-line identity bridge, same-person merge, or relationship from this draft. The checked source names no Dario, Arturo, Smith, Dario Jose, spouse, descendant, or later-life identifier.
4. Do not merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` from this item. The reviewed source supports only the mother as named in entry `172`.
5. Canonical promotion should remain on hold until a downstream claim workflow explicitly handles the conversion conflict and uses the bounded row-control reading rather than silently normalizing the converted file.

## Evidence Strengths

- The source image visibly places entry `172` on page 58 in the middle row, with child name consistent with `Jose del Carmen Segundo Pulgar Arriagada`.
- The assigned chunk, source packet, and targeted conversion-review note agree that the physical row `172` is the Pulgar/Arriagada row, not the Burgos/de la Cruz text in the current converted Markdown.
- The source image and reviewed derivatives support a birth registration dated 7 April 1888 for a child born 8 March 1888, with father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- The staged identity analysis correctly treats the Burgos/de la Cruz text as a derivative conversion conflict and correctly keeps Dario identity questions unresolved.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 8/10 for row-control after image review; 5/10 for the uncorrected converted Markdown; 5/10 for the trailing father suffix |
| evidence_quantity_score | 4/10 |
| agreement_score | 8/10 among source image, chunk, source packet, and QA note for the Pulgar/Arriagada row; 2/10 if the current converted Markdown is included without conflict handling |
| identity_confidence_score | 8/10 for the source-named child and parents within this single birth row; 1/10 for any Dario-line identity bridge; 1/10 for any Juana duplicate-person merge |
| claim_probability | 0.90 that physical row entry `172` is the Pulgar/Arriagada birth registration; 0.82 that the father should be bounded as `Jose del Carmen Pulgar`; 0.87 that the mother is recorded as `Juana Arriagada de Pulgar`; 0.03 or lower for Dario-line attachment; 0.05 for a Juana merge |
| relevance_level | high for the Pulgar/Arriagada parent-child cluster; low for Dario-line identity analysis |
| relevance_confidence | 0.88 for Pulgar/Arriagada relevance; 0.12 for Dario-line relevance |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a conflict-control and proof-hold analysis. The strongest supported conclusion is narrow: the image-controlled physical row for entry `172` records `Jose del Carmen Segundo Pulgar Arriagada`, with source-named parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

The draft should not be used to promote the unreviewed `Pulgar S.` suffix, to overwrite the converted Markdown without preserving the conversion conflict, or to attach this record to any Dario or Pulgar-Smith identity. The current converted Markdown remains materially inconsistent and should be treated as a conversion-conflict artifact.

## Next Action

Keep this item on hold for canonical promotion. A later claim workflow may stage only the bounded row-control facts and parent-child candidates for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`, while explicitly carrying the Burgos/de la Cruz derivative conflict and leaving Dario and Juana duplicate-person questions unresolved.
