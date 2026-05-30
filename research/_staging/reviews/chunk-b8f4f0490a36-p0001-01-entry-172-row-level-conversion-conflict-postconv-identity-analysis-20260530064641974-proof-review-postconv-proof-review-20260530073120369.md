---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530073120369
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

1. Do not promote this draft to canonical claims, relationships, person pages, family pages, or Dario-line attachments. The row-control conflict remains unresolved between the assigned chunk and the converted Markdown.
2. The original source PNG named by the source packet and manifests is not present at either checked `raw/sources/` path. The job page image path in the conversion manifest is also absent, so this review cannot certify the entire physical row from the full original image.
3. The assigned chunk and source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888. The converted Markdown and page Markdown read entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888.
4. The staged crop assets visually support the Pulgar/Arriagada parent and informant area, but they do not by themselves certify the full row, the child name column, the registration number, or the birth date column.
5. The father suffix after `Jose del Carmen Pulgar` is not promotion-ready. Preserve the literal staged reading `Jose del Carmen Pulgar S.` only as unresolved verification text, not as a normalized identity conclusion.

## Evidence Strengths

- The staged draft accurately identifies the conflict as a derivative row-control problem, not a spelling variant or same-person problem.
- The assigned chunk, source packet, and conversion review note agree on a Pulgar/Arriagada row for entry `172`.
- The visible staged crop assets support the lower parent/informant fields for the Pulgar/Arriagada row, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`.
- The converted Markdown and page Markdown consistently preserve the competing Burgos/de la Cruz reading, which should remain as a competing derivative transcription until original-image QA resolves row control.
- The staged draft correctly rejects any direct bridge from this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or broader Jose/Juana parent clusters.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 |
| conversion_confidence_score | 5/10 overall; 7/10 for the cropped Pulgar/Arriagada parent/informant area only |
| evidence_quantity_score | 5/10 |
| agreement_score | 4/10 across all derivatives; 8/10 within the Pulgar/Arriagada staged packet set |
| identity_confidence_score | 7/10 that the staged Pulgar/Arriagada row is a coherent separate identity if row control is certified; 1/10 for same-person treatment with Burgos/de la Cruz; 0/10 for direct Dario identity attachment |
| claim_probability | 0.68 for the narrow Pulgar/Arriagada row reading pending full-page QA; 0.27 for the Burgos/de la Cruz derivative reading controlling this staged row; 0.02 for same-person/name-variant treatment; 0.00 for a direct Dario bridge |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | blocked; hold for original-image row-control QA and suffix review |

## Review Finding

The staged identity analysis is supported as a cautionary conflict analysis. It should remain staged and blocked from canonical promotion. The safest proof judgment is that the Pulgar/Arriagada reading is plausible and partially crop-supported, while the controlling row cannot be certified because the full original page image is unavailable and the converted Markdown contains a materially incompatible entry `172`.

No relationship jump is supported. If the Pulgar/Arriagada row is later certified, it may support only narrow birth-entry and stated-parent candidates for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`. It does not support a merge with Burgos/de la Cruz identities, a direct Dario-line attachment, or a broader Jose/Juana cluster merge.

## Next Action

Hold this item for targeted original-image row-control QA using the full page image. The next reviewer should verify physical row `172` across all columns and explicitly decide whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Until then, preserve both derivative readings as a conversion conflict and do not promote downstream claims.
