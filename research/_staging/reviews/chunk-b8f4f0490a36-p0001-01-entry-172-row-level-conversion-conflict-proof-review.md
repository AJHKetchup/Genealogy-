# Proof Review: Entry 172 Row-Level Conversion Conflict

- Review task id: `proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030052086.md`
- Reviewed staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030052086.md`
- Role: claim_reviewer
- Review status: hold
- canonical_readiness: hold_for_conversion_qa

## Blockers

- The converted Markdown still assigns entry `172` to a different Burgos/de la Cruz birth entry, while the current chunk, source packet, QA note, and visible source image support physical row `172` as the Pulgar/Arriagada birth registration. This unresolved derivative conflict blocks canonical promotion.
- The father field should not be promoted with the chunk's terminal `S.`. The image and QA packet support `Jose del Carmen Pulgar` as the bounded reading, with the terminal mark unresolved.
- The staged analysis correctly rejects a Dario identity bridge. The row does not name Dario, Arturo, Smith, or a later Pulgar-Arriagada adult, so it cannot support same-person or lineage claims to those identities.
- Parent identity links remain candidate-level only. This row supports parents named `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, but not merges to every same-name Jose/Juana stub or to `Juana de Dios Amagada de Pulgar`.

## Scoring

- source_quality_score: 0.88
- conversion_confidence_score: 0.44
- evidence_quantity_score: 0.72
- agreement_score: 0.58
- identity_confidence_score: 0.76
- claim_probability: 0.82
- relevance_level: critical
- relevance_confidence: 0.95
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The source is a contemporary civil birth register image, a strong source type for birth identity, parent names, registration date, and row-control evidence.
- The visible page image shows page 58 with physical entry `172` on the Pulgar/Arriagada row, agreeing with the source packet, QA note, and current chunk on the central row-control finding.
- The staged draft handles uncertainty appropriately by separating the image-supported Pulgar/Arriagada row from the conflicting converted Markdown and by keeping broader Dario/Jose/Juana identity links unpromoted.
- The draft's hold recommendation is proportionate to the risk: the local row identity is probable, but the conversion layer remains unsafe for canonical use.

## Review Judgment

The staged draft is supported as an identity-conflict analysis. The most probable reading is that physical entry `172` in the assigned source image is the Pulgar/Arriagada birth registration, and the Burgos/de la Cruz text in the converted Markdown is stale, row-shifted, or from a different image context. The father-name suffix remains unresolved and should be bounded to `Jose del Carmen Pulgar` unless a focused review certifies the terminal mark.

This review does not approve promotion to canonical claims, relationships, or person pages. The proper proof decision is `hold_for_conversion_qa`, not rejection of the staged analysis and not canonical readiness.

## Next Action

Send the converted Markdown and any downstream chunks for conversion-control reconciliation against the source image for page 58, physical entry `172`. After that reconciliation, run a narrower proof review on the birth claim and parent relationship claims before any canonical promotion.
