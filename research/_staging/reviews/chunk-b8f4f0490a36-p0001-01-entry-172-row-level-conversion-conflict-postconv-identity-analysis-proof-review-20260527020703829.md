---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527020703829
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526235734395.md
reviewed_claim_type: identity_conflict_analysis
reviewed_subject: "Entry 172 row-level conversion conflict"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md
conversion_review_note: research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
source_page_image_checked: "yes; page 58 entry 172 visible in referenced PNG"
source_quality_score: 0.90
conversion_confidence_score: 0.66
evidence_quantity_score: 0.72
agreement_score: 0.74
identity_confidence_score: 0.84
claim_probability: 0.85
relevance_level: critical
relevance_confidence: 0.95
canonical_readiness: hold_for_conversion_reconciliation
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Canonical readiness is `hold_for_conversion_reconciliation`. The visible page image, assigned chunk, source packet, and targeted QA note support the Pulgar/Arriagada row for physical entry `172`, but the referenced converted Markdown still records entry `172` as a different Burgos/de la Cruz birth entry.
- The father name is not promotion-ready with the suffix. The image and chunk support `Jose del Carmen Pulgar` clearly enough for a bounded father reading, but the possible mark after `Pulgar` is not strong enough in this review to promote as definite `S.`.
- No Dario-line identity bridge is supported by this source. The entry names `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`; it does not name or connect to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío Pulgar Arriagada`.
- The review supports a row-control judgment, not a conversion edit. The derivative transcript conflict should be retained or corrected only through the appropriate conversion-control process.

## Evidence Strengths

- The referenced civil birth-register image is an original-style register page and directly shows page 58, entry `172`.
- Visual inspection supports the staged draft's controlling row: child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, birthplace `Calle de Valdivia`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and declarant `Ernesto Herrera L.`.
- The assigned chunk agrees with the Pulgar/Arriagada row structure and does not match the Burgos/de la Cruz entry found in the converted Markdown.
- The targeted QA note correctly scopes the father-field uncertainty and warns against parent merges, identity merges, or Dario-line attachments.

## Scored Judgment

- `source_quality_score: 0.90` - contemporary civil birth registration with direct page-image access.
- `conversion_confidence_score: 0.66` - high confidence in the image-reviewed row and assigned chunk, reduced because the main converted Markdown remains materially contradictory.
- `evidence_quantity_score: 0.72` - one direct source image plus derivative chunk, source packet, and targeted QA note; no independent source reviewed for identity extension.
- `agreement_score: 0.74` - image, chunk, source packet, and QA note agree, but the referenced converted file is a major internal disagreement.
- `identity_confidence_score: 0.84` - high for the bounded identity of the child named in entry `172`; low for any proposed identity bridge beyond that row.
- `claim_probability: 0.85` - the staged row-control conclusion is probable on the visible source and QA materials, with the conversion conflict preventing canonical readiness.
- `relevance_level: critical`; `relevance_confidence: 0.95` - the row controls whether staged Entry 172 Pulgar/Arriagada claims can be used at all.
- `canonical_readiness: hold_for_conversion_reconciliation`.

## Review Judgment

The staged identity/conflict analysis is materially supported for its central conclusion: physical entry `172` on the referenced page is the Pulgar/Arriagada birth row, not the Burgos/de la Cruz row currently present in the converted Markdown. The analysis also correctly treats the possible father suffix and all Dario-line connections as unresolved or unsupported.

This should remain a hold for canonical promotion. The row-control probability is high enough to preserve the Pulgar/Arriagada interpretation in staging, but canonical claims and relationships should wait until the derivative conversion conflict is reconciled or explicitly documented as a retained conversion mismatch.

## Next Action

Route this item to conversion reconciliation or conversion-control review for `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`. After that, promote only narrowly scoped Entry 172 facts supported by the image-reviewed row, with father recorded no more specifically than `Jose del Carmen Pulgar` unless a later image-level review certifies the suffix.
