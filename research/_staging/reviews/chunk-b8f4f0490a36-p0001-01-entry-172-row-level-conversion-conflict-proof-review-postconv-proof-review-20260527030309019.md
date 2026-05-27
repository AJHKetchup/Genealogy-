---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260527030309019
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527001051346.md"
staged_draft_reviewed: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527001051346.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_control_update
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical promotion remains blocked because the current converted Markdown assigns entry `172` to `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the source image, chunk, source packet, and targeted QA support the Pulgar/Arriagada row.
2. The father should not be promoted as `Jose del Carmen Pulgar S.` from this proof review. The chunk transcribes a terminal `S.`, but the targeted QA and visual review support only the bounded reading `Jose del Carmen Pulgar` unless a later proof step certifies the suffix.
3. No Dario-line bridge is supported. Entry 172 does not name Dario, Arturo, Smith, a spouse, descendant, or other identity bridge to any Dario Pulgar candidate.
4. No merge between `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` is supported by this record.
5. Relationship promotion should wait until the conversion-control mismatch is explicitly carried forward as a conflict or the derivative conversion is corrected. The proof finding can accept the physical-row identity, but the converted Markdown remains materially unreliable for this entry.

## Evidence Reviewed

- Staged identity/conflict analysis: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527001051346.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md`
- Targeted conversion QA note: `research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Judgment

The physical source image visibly supports entry `172` as the middle row on page 58 and aligns with the assigned chunk, source packet, and targeted QA: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered `Siete de Abril de mil ochocientos ochenta i ocho`, born `Ocho de Marzo de mil ochocientos ochenta i ocho` at about three in the afternoon on `Calle de Valdivia`, father bounded as `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and declarant `Ernesto Herrera L.`.

The current converted Markdown is not reliable for this row. It appears to describe a different page or row set and should not control entry 172 claims for this source image.

## Scores

- source_quality_score: 0.90
- conversion_confidence_score: 0.70 for the chunk/source-packet/QA-controlled Pulgar row; 0.15 for the current converted Markdown entry 172
- evidence_quantity_score: 0.78
- agreement_score: 0.82 among source image, chunk, source packet, and targeted QA; 0.20 when including the stale converted Markdown
- identity_confidence_score: 0.86 for `Jose del Carmen Segundo Pulgar Arriagada` as the child in physical entry 172
- claim_probability: 0.85 that physical entry 172 is the Pulgar/Arriagada birth registration
- relevance_level: high
- relevance_confidence: 0.95
- canonical_readiness: hold_for_conversion_control_update

## Claim-Level Review

| Claim | Review | Probability | Canonical readiness |
|---|---|---:|---|
| Entry 172 is the Pulgar/Arriagada birth row | Supported by image, chunk, packet, and targeted QA despite converted-file conflict | 0.85 | hold_for_conversion_control_update |
| Child is `Jose del Carmen Segundo Pulgar Arriagada` | Supported by physical row and chunk | 0.86 | hold_for_conversion_control_update |
| Father is `Jose del Carmen Pulgar` | Supported as bounded reading | 0.78 | hold_for_father_suffix_review |
| Father is definitely `Jose del Carmen Pulgar S.` | Not sufficiently certified | 0.45 | not_ready |
| Mother is `Juana Arriagada de Pulgar` | Supported for this entry | 0.84 | hold_for_conversion_control_update |
| `Juana Arriagada de Pulgar` equals `Juana de Dios Amagada de Pulgar` | Not supported by this record | 0.18 | not_ready |
| Entry 172 bridges to any Dario Pulgar identity | Not supported by this record | 0.05 | not_ready |

## Evidence Strengths

- Civil birth registration is a high-quality source type for name, date, place, sex, and named parents when the row is controlled.
- The page image, assigned chunk, source packet, and targeted QA independently align on the row location and the Pulgar/Arriagada identity.
- The staged draft properly keeps the derivative conversion conflict visible and avoids canonical promotion.

## Next Action

Revise/hold rather than promote. Accept the proof-review judgment that the controlling physical row for entry `172` is the Pulgar/Arriagada birth registration, but require a conversion-control update or explicit conflict note before canonical claims or relationships are promoted. Promote no Dario bridge and no Juana identity merge from this evidence.
