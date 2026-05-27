---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527021841209
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000231135.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000231135.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold_for_conversion_reconciliation
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical promotion remains blocked because the referenced converted Markdown materially conflicts with the source image, assigned chunk, source packet, and targeted QA note. The converted Markdown records entry `172` as a Burgos/de la Cruz birth for `Jose Miguel`; the visible source image and staged QA materials support entry `172` as the Pulgar/Arriagada row.
2. The father field is not ready beyond `Jose del Carmen Pulgar`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the page image and QA note do not make the suffix clear enough for promotion.
3. The staged identity analysis correctly blocks any Dario-line identity bridge. This entry does not name Dario, Arturo, Smith, a spouse, child, or descendant, and it provides no direct bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada`.
4. The mother claim must remain scoped to the recorded entry wording `Juana Arriagada de Pulgar`. This source does not prove that she is the same person as `Juana de Dios Amagada de Pulgar`.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000231135.md`
- Conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526232323475.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md`
- Targeted QA note: `research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Review Judgment

The staged draft is well supported as a conflict analysis and should remain a hold, not a promotion-ready claim package. The physical source image visibly places entry `172` on page 58 as the Pulgar/Arriagada birth registration. The assigned chunk, source packet, and targeted QA note are internally consistent on the controlling row. The converted Markdown is the outlier and appears stale, row-shifted, or derived from a different page set under the same source identity.

The staged draft stays within the correct boundary between verification and transcription. It does not silently replace the canonical conversion; it reports a row-control conflict, preserves the Burgos/de la Cruz mismatch as a derivative-transcript problem, and limits the father reading to the clearer form certified by QA.

## Evidence Strengths

- The source image directly supports the row-control finding: entry `172` is on page 58 and is the row for `Jose del Carmen Segundo Pulgar Arriagada`.
- The assigned chunk and targeted QA note agree on the child, sex, registration date, birth date/time, birth place, mother, declarant, and general father name.
- The conflict with the converted Markdown is concrete and material, involving a different child, different parents, different birth date/time, different place, and different page context.
- The staged analysis appropriately treats Dario-line and Juana-variant issues as anti-conflation risks rather than promoted identity conclusions.

## Scores

- source_quality_score: 0.88
- conversion_confidence_score: 0.70
- evidence_quantity_score: 0.78
- agreement_score: 0.76
- identity_confidence_score: 0.84 for the bounded claim that physical entry `172` is the Pulgar/Arriagada row; 0.66 for the father field limited to `Jose del Carmen Pulgar`; 0.08 or lower for any Dario-line bridge.
- claim_probability: 0.84 that physical entry `172` records the birth of `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, with the father suffix unresolved.
- relevance_level: high for Pulgar/Arriagada row-control and parent-candidate evidence; low for Dario identity attachment except as anti-conflation context.
- relevance_confidence: 0.92 for Pulgar/Arriagada relevance; 0.35 for Dario-line relevance.
- canonical_readiness: hold_for_conversion_reconciliation.

## Next Action

Hold canonical promotion until conversion-control resolves or annotates the stale Burgos/de la Cruz converted Markdown. If promoted later, promote only narrow Entry 172 claims supported by the image-reviewed Pulgar/Arriagada row, with father recorded as `Jose del Carmen Pulgar` and a note that the possible suffix/initial is unresolved. Do not merge Jose/Juana parent candidates or attach any Dario-line identity from this source.
