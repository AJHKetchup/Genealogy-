---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260527020228864
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
reviewed_conversion_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_reconciliation
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The canonical promotion gate remains blocked by a material derivative conflict. The converted Markdown records entry `172` as a Burgos/de la Cruz birth entry for `Jose Miguel`, while the source image, assigned chunk, source packet, and targeted QA note support entry `172` as the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`.
2. The father name is supported only as `Jose del Carmen Pulgar` for promotion purposes. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the source image does not make the mark after `Pulgar` clear enough for this proof review to certify a definite `S.`.
3. No same-person, duplicate-person, lineage, or relationship bridge to any Dario-line person is supported by this entry. The staged draft correctly treats any Dario attachment as not ready.
4. `Juana Arriagada de Pulgar` must not be merged with `Juana de Dios Amagada de Pulgar` from this evidence. This entry supports only the mother name visible in entry `172`.

## Evidence Strengths

- The original source is a civil birth register image and is strong direct evidence for the registration row, child name, sex, birth date/time, birthplace, and named parents.
- The source image visibly places entry `172` in the middle row of register page 58 and supports the Pulgar/Arriagada row-control decision.
- The assigned chunk, targeted QA note, and source packet agree on the controlling row and on the core Pulgar/Arriagada facts.
- The staged identity/conflict analysis is appropriately conservative: it keeps the converted Markdown conflict visible, limits the father suffix, rejects Dario-line attachment, and holds canonical promotion pending proof review and conversion reconciliation.

## Scored Judgment

| Item | Score / Value | Rationale |
|---|---:|---|
| source_quality_score | 0.90 | Civil birth register image; direct contemporary record for the birth registration. |
| conversion_confidence_score | 0.72 | Image, chunk, QA note, and packet support the Pulgar/Arriagada row, but the main converted Markdown remains materially mismatched. |
| evidence_quantity_score | 0.76 | One direct source image plus derivative chunk, source packet, and targeted QA note; no independent corroborating source reviewed. |
| agreement_score | 0.78 | Strong agreement among source image, chunk, packet, and QA note; direct conflict with the converted Markdown lowers the score. |
| identity_confidence_score | 0.84 | High confidence that physical entry `172` is for `Jose del Carmen Segundo Pulgar Arriagada`; lower for any broader identity linkage. |
| claim_probability | 0.84 | The row-control claim is probable and image-supported, but promotion should wait for conversion reconciliation. |
| relevance_level | high | Entry directly names Pulgar and Arriagada family members. |
| relevance_confidence | 0.94 | The family relevance is directly supported by the visible child and parent names. |
| canonical_readiness | hold_for_conversion_reconciliation | Do not promote until the derivative conversion conflict is reconciled or explicitly retained as a known conversion error. |

## Claim-Level Notes

- Physical entry `172` as the Pulgar/Arriagada row: supported; probability `0.84`; canonical readiness `hold`.
- Child `Jose del Carmen Segundo Pulgar Arriagada`, male: supported by image-reviewed row and chunk; probability `0.86`; canonical readiness `hold`.
- Birth date/time `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`: supported; probability `0.84`; canonical readiness `hold`.
- Birthplace `Calle de Valdivia`: supported; probability `0.84`; canonical readiness `hold`.
- Father `Jose del Carmen Pulgar`: supported; probability `0.78`; canonical readiness `hold`.
- Father suffix `S.`: not certified; probability `0.45`; canonical readiness `not_ready`.
- Mother `Juana Arriagada de Pulgar`: supported; probability `0.86`; canonical readiness `hold`.
- Declarant `Ernesto Herrera L.`, present at birth: supported; probability `0.82`; canonical readiness `hold`.
- Any merge or bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada: not supported; probability `0.05`; canonical readiness `not_ready`.

## Next Action

Hold canonical promotion. Accept the staged draft's conservative conflict analysis for review purposes, then resolve the conversion-control issue separately: either correct the converted Markdown through the proper conversion process or explicitly record it as a stale/row-shifted derivative conflict. After that, promote only narrowly scoped entry `172` facts and parent relationships, preserving the father suffix uncertainty and avoiding all Dario-line or Juana-variant merges without separate direct proof.
