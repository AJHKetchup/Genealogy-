---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530032703657
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-postconv-identity-analysis-20260525210459114.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-postconv-identity-analysis-20260525210459114.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conflict

## Blockers First

1. The staged draft is not canonical-ready. The assigned chunk and assigned converted Markdown give incompatible readings for the same entry number 172.
2. The assigned chunk reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the assigned converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
3. The original source image path recorded in the draft and manifest was not available in this checkout, and the manifest's `page-images/page-0001.png` was also not present. This review therefore cannot independently certify the visible handwriting or the father-field suffix.
4. No claim should use this item to bridge to Dario, Arturo, Smith, `Dario Jose Pulgar-Arriagada`, or any Dario Pulgar identity cluster. None of the checked derivative evidence names Dario, Arturo, Smith, a spouse, a descendant, or another bridge fact.
5. Parent-child and same-person claims must remain staged or held until targeted conversion QA selects the controlling row and certifies the father-field reading.

## Evidence Strengths

- The staged draft accurately identifies the conflict as row-level and material, not a spelling variant.
- The source packet and conflict draft consistently flag the same blocker and recommend `hold_for_conversion_qa`.
- If the chunk is later certified as controlling, it would be a strong source type for a narrow birth-registration claim because it is a civil birth register row naming a child, father, mother, date, place, and informant.
- The staged draft's negative conclusion about Dario-line attachment is supported by the checked files: the relevant derivative readings do not contain a Dario identity bridge.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the source type in principle; 5/10 usable here because the source image was unavailable for direct verification |
| conversion_confidence_score | 3/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 between the assigned chunk and assigned converted Markdown; 8/10 between the staged draft, source packet, and conflict draft about the existence of the conflict |
| identity_confidence_score | 6/10 for the Pulgar/Arriagada row as a staged hypothesis; 2/10 for the Burgos/de la Cruz row as controlling; 0.5/10 for any Dario-line bridge |
| claim_probability | 0.65 that the Pulgar/Arriagada row is the intended entry 172 evidence; 0.20 that the Burgos/de la Cruz converted-file reading is controlling; 0.02 that this item supports a Dario-line identity bridge |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold notice. It correctly prevents promotion of a child identity, birth event, parent-child relationship, parent merge, same-person merge, or Dario-line comparison from this conflicted evidence.

The proof posture should remain conservative because the checked derivative files disagree on child, parents, birth date, place, informant, and page/register context. The source packet's statement that the visible image aligns with the Pulgar/Arriagada row is useful context, but it is not independently reverified here because the referenced image files are unavailable.

## Next Action

Keep this item on `hold_for_conversion_qa`. The next worker should perform targeted conversion QA against the actual page image for page 58, entry 172, decide whether the Pulgar/Arriagada or Burgos/de la Cruz reading controls, and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical promotion.
