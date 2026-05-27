---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260527065102397
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031003832.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031003832.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
review_decision: hold
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.88
conversion_confidence_score: 0.44
evidence_quantity_score: 0.72
agreement_score: 0.58
identity_confidence_score: 0.76
claim_probability: 0.82
relevance_level: high
relevance_confidence: 0.94
canonical_readiness_score: 0.12
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The visible source image and assigned chunk support entry `172` as the Pulgar/Arriagada row, but the current converted Markdown still records a materially different Burgos/de la Cruz entry under entry `172`.
- The father field is not proof-ready beyond `Jose del Carmen Pulgar`. The chunk reads `Jose del Carmen Pulgar S.`, but the QA note and source-packet image review do not certify the terminal mark or suffix.
- No Dario identity bridge is supported by this entry. The source-visible entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.
- Parent identity expansion is blocked. `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are supported as row-local parent readings only; this review does not merge them with broader Jose or Juana candidates.
- Relationship promotion is blocked until conversion control resolves or quarantines the conflicting converted Markdown. The disagreement affects child identity, parentage, birth date/time, residence context, and informant.

## Evidence Strengths

- The source is a civil birth register image, a strong primary source for the birth-registration facts visible on the row.
- Direct review of the page image supports the staged QA finding that physical entry `172` on page 58 is the Pulgar/Arriagada row, not the Burgos/de la Cruz row found in the converted Markdown.
- The assigned chunk, source packet, targeted QA note, and visible image agree on the major Pulgar/Arriagada facts: child name, male sex, registration date, birth date/time, birth place, mother, informant, and row number.
- The staged draft preserves uncertainty correctly by treating the converted Markdown as conflicting derivative evidence and by holding canonical edits.

## Scored Judgment

| Metric | Score / Level | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration image is strong primary evidence for row-local facts, with handwriting limits on the father suffix. |
| conversion_confidence_score | 0.44 | Mixed derivative state: chunk and QA are image-aligned, while the current converted Markdown conflicts materially. |
| evidence_quantity_score | 0.72 | One primary image plus three local derivative/QA layers are enough for row-control review, not enough for external identity merges. |
| agreement_score | 0.58 | Strong agreement among image, chunk, packet, and QA on Pulgar/Arriagada; severe disagreement with converted Markdown. |
| identity_confidence_score | 0.76 | Moderate-high for the local child identity as `Jose del Carmen Segundo Pulgar Arriagada`; low for any broader Dario/Jose/Juana merge. |
| claim_probability | 0.82 | Probable that physical entry `172` in this task is the Pulgar/Arriagada row and that the converted Markdown is stale, shifted, or mismatched. |
| relevance_level | high | High Pulgar-line relevance and high risk of erroneous canonical attachment if the derivative conflict is ignored. |
| relevance_confidence | 0.94 | The source directly concerns Pulgar/Arriagada family names, but not Dario identities. |
| canonical_readiness | hold_for_conversion_qa | Do not promote new claims or relationships from this review until conversion-control resolves the row-level conflict. |

## Claim Probability Notes

- Row-control claim: `0.82`. The visible source image and staged QA support the Pulgar/Arriagada row for entry `172`; the remaining risk comes from the unresolved converted Markdown conflict.
- Child identity claim for this row: `0.78`. The row supports `Jose del Carmen Segundo Pulgar Arriagada` locally, but the derivative conflict prevents canonical promotion.
- Father suffix claim: `0.30`. `Jose del Carmen Pulgar` is supported; the extra `S.` should remain unresolved pending a focused crop or later proof review.
- Dario identity bridge claim: `0.05`. This entry does not name Dario or provide a relationship bridge to a Dario candidate.
- Broader parent merge claims: `0.20` for Jose candidates and `0.24` for Juana candidates. Same-name or surname overlap is insufficient without separate bridge evidence.

## Source Reliability And Conversion Confidence

The page image is the controlling source for row placement and literal row content. The chunk is useful because it agrees with the visible row on the major facts, but its father-suffix reading exceeds what the source packet and QA note certify. The converted Markdown is not reliable for entry `172` in its current state because it records a different child, different parents, different birth date/time, and different contextual details.

This review therefore accepts the staged draft's conflict analysis as substantially supported, while retaining a hold decision for canonical use.

## Next Action

Conversion-control should repair, supersede, or quarantine the current converted Markdown for this source before any further claim or relationship promotion. If a father suffix is genealogically important, request a focused image crop or separate proof review of the father field only. Keep any Dario or broader Jose/Juana identity bridge work in separate proof-reviewed tasks.
