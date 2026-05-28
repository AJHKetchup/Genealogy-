---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527235531684
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-identity-analysis-20260527234235205.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-identity-analysis-20260527234235205.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260527222756266.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-evidence-extraction-20260527222756266.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

1. The current converted Markdown is not reliable for entry `172`; it records a different child and parents (`Jose Miguel`, `Oswaldo Burgos`, `Concepcion de la Cruz`) than the visible source image and assigned chunk.
2. The father name should remain bounded to `Jose del Carmen Pulgar` for any downstream claim. The assigned chunk includes a possible trailing `S.`, but the staged packet correctly treats that suffix as unresolved and not promotable.
3. No Dario-line identity bridge is supported by this birth entry. The visible source names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario/Dario Arturo/Dario Jose/Dario Pulgar-Smith.
4. Parent-child claims for the Pulgar/Arriagada row are source-supported, but canonical promotion should remain on hold until the row-control conflict is resolved or clearly carried as a conversion QA exception.

## Evidence Strengths

- The source image visibly places physical entry `172` on page 58 as the Pulgar/Arriagada row.
- The assigned chunk matches the visible source for the core row: registration date 7 April 1888, child `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 about 3 p.m., place `Calle de Valdivia`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet accurately preserves the derivative conflict and does not use the Burgos/de la Cruz converted text as controlling evidence.
- The staged identity analysis correctly rejects immediate merges between the 1888 child and Dario-line candidates, and correctly treats same-name parent clustering as unresolved.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 8/10 for the image-reviewed assigned chunk; 2/10 for the current converted Markdown entry assignment |
| evidence_quantity_score | 5/10 |
| agreement_score | 7/10 overall; high between source image, source packet, and chunk, but low against the current converted Markdown |
| identity_confidence_score | 8/10 for `Jose del Carmen Segundo Pulgar Arriagada` as the row-controlled child; 2/10 or lower for Dario-line identity attachment |
| claim_probability | 0.90 for the narrow row-control claim that entry `172` is the Pulgar/Arriagada birth row; 0.85 for the core child and parent readings excluding the unresolved father suffix; 0.05 for a Dario-line merge from this evidence |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold for canonical promotion while the conversion conflict remains active; revise/queue only narrow Pulgar/Arriagada claims with explicit row-control provenance |

## Review Finding

The staged identity analysis is supported as a hold/revise decision. The visible source image and assigned chunk support the Pulgar/Arriagada row for physical entry `172`; the current converted Markdown is a conflicting derivative artifact and should not control identity or relationship claims for this source.

The evidence supports a probable staged birth-registration claim for `Jose del Carmen Segundo Pulgar Arriagada` and parent candidates `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, provided the father suffix is excluded. It does not support any same-person merge to Dario candidates or any relationship jump beyond the named parents in this row.

## Next Action

Revise or carry forward only the narrow, row-controlled Pulgar/Arriagada extraction with explicit QA language about the converted Markdown conflict. Keep canonical promotion, parent merges across other entries, and all Dario-line attachments on hold pending a corrected conversion or a separate identity-bridge proof review.
