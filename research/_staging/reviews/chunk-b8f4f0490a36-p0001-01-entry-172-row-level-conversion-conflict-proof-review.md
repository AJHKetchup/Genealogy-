# Proof Review: Entry 172 Row-Level Conversion Conflict

- Review task id: `proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000231135.md`
- Reviewed staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000231135.md`
- Role: claim_reviewer
- Review status: hold
- canonical_readiness: hold_for_conversion_reconciliation

## Blockers

- The converted Markdown still records entry `172` as a Burgos/de la Cruz birth for `Jose Miguel`, while the source image, assigned chunk, source packet, QA note, and staged identity analysis support the physical entry `172` row as the Pulgar/Arriagada birth for `Jose del Carmen Segundo Pulgar Arriagada`.
- The father field should not be promoted with the suffix `S.`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the targeted QA note certifies only `Jose del Carmen Pulgar`; the visible source leaves the suffix too uncertain for canonical use.
- No Dario-line identity or lineage bridge is supported by this entry. The record names `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`; it does not name or connect `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, or any Dario Pulgar-Arriagada candidate.
- `Juana Arriagada de Pulgar` must not be merged with `Juana de Dios Amagada de Pulgar` from this evidence alone. This entry supports only the recorded mother name in this row.

## Scoring

- source_quality_score: 0.90
- conversion_confidence_score: 0.62
- evidence_quantity_score: 0.72
- agreement_score: 0.68
- identity_confidence_score: 0.82
- claim_probability: 0.84
- relevance_level: high
- relevance_confidence: 0.93
- canonical_readiness: hold_for_conversion_reconciliation

## Evidence Strengths

- The original civil birth register image is available and directly relevant to the row-control question for page 58, entry `172`.
- Visual review supports the targeted QA note: the physical row numbered `172` on page 58 is the Pulgar/Arriagada row, with child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth on `Ocho de Marzo de mil ochocientos ochenta i ocho`, and birth place `Calle de Valdivia`.
- The assigned chunk, source packet, QA note, and staged identity analysis materially agree on the controlling Pulgar/Arriagada row.
- The staged analysis correctly treats the converted Markdown as a derivative row-control conflict and does not promote Dario-line or Juana-variant merges.

## Review Judgment

The staged identity analysis is well supported as a conflict analysis. The best current judgment is that physical entry `172` is the Pulgar/Arriagada birth registration and that the converted Markdown is stale, row-shifted, or otherwise mismatched for this source identity.

This review should remain a hold, not a canonical promotion. The row-control probability is high, but canonical readiness is blocked by the unresolved derivative conversion conflict and by the uncertain father-name suffix.

## Next Action

Send the converted Markdown and chunk set to conversion-control reconciliation against the source image. If reconciliation accepts the image-reviewed Pulgar/Arriagada row, promote only narrowly scoped Entry 172 facts and relationships: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` without suffix, and mother `Juana Arriagada de Pulgar`. Do not merge Juana candidates or attach any Dario-line identity without separate direct bridge evidence.
