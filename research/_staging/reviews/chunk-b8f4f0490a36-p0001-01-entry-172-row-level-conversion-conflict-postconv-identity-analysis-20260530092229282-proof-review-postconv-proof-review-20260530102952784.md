---
type: proof_review
status: hold
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
worker: "postconv-proof-review-20260530102952784"
role: claim_reviewer
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530072501797.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530072501797.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_reference: "page 1; register page 58; physical row entry 172"
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md`.

## Blockers First

- Full-page source blocker: the referenced original PNG `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` is not present in this checkout. I could not certify the physical full-page row alignment from the original source image.
- Row-control blocker: the assigned chunk records entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, while the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Derivative disagreement blocker: the staged packet, conversion review note, and chunk agree with the Pulgar/Arriagada reading, but the converted Markdown materially disagrees. This supports a conversion conflict judgment, not immediate fact promotion.
- Crop-scope blocker: the staged crop assets visibly support the Pulgar/Arriagada parent and informant fields, but they do not independently prove the entry number, child name, registration date, birth details, or full row boundaries.
- Father suffix blocker: the visible crop supports `Jose del Carmen Pulgar`; any trailing suffix or mark after `Pulgar` remains uncertain and should not be promoted.
- Identity-bridge blocker: the staged draft correctly withholds attachment to Dario/Dario Arturo/Dario Jose Pulgar identities. The reviewed evidence contains no literal Dario, Arturo, Smith, descendant, occupation, or later-life bridge.

## Evidence Strengths

- The assigned chunk directly transcribes entry `172` as a Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The source packet accurately preserves the conflict and recommends `hold_for_conversion_qa` rather than promotion.
- The conversion review note accurately states that original-image certification is unavailable and that the current converted Markdown gives a Burgos/de la Cruz row for the same entry number.
- The staged crop assets provide narrow visual support for `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Ernesto Herrera L.`, and `Presente al nacimiento`.
- The staged identity analysis appropriately treats Pulgar/Arriagada versus Burgos/de la Cruz as incompatible row-control readings rather than same-person variants.

## Scored Judgment

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration is a strong source class, but this review could not inspect the missing full-page original image. |
| conversion_confidence_score | 0.45 | Chunk and crops favor Pulgar/Arriagada, while the current converted Markdown conflicts materially. |
| evidence_quantity_score | 0.58 | Several derivative/staged items agree, plus two local crops, but the decisive full-page source is unavailable. |
| agreement_score | 0.42 | Agreement exists among the chunk, source packet, QA note, and crops; disagreement with the converted Markdown is severe. |
| identity_confidence_score | 0.62 | Moderate for the local Pulgar/Arriagada row hypothesis; low for any wider family identity attachment. |
| claim_probability | 0.70 | The staged draft's core claim that this is a row-control conflict requiring hold is well supported. The Pulgar row itself remains uncertified for promotion. |
| relevance_level | high | The evidence directly concerns the assigned entry `172` conflict. |
| relevance_confidence | 0.96 | All reviewed materials refer to the exact staged draft, source packet, chunk, and entry number. |
| canonical_readiness | not_ready | Do not promote claims, relationships, identity merges, or wiki updates from this review. |

## Claim-Level Review

- Claim that entry `172` has a Pulgar/Arriagada reading in the assigned chunk: supported by the chunk and source packet; probability `0.86`; canonical readiness `hold`.
- Claim that entry `172` has a Burgos/de la Cruz reading in the current converted Markdown: supported by the converted file; probability `0.95`; canonical readiness `hold` because it conflicts with the assigned chunk.
- Claim that the two readings are incompatible row-control outputs: supported; probability `0.91`; canonical readiness `review_note_only`.
- Claim that `Jose del Carmen Pulgar` is the father in the Pulgar/Arriagada row: locally supported by chunk and crop; probability `0.72`; canonical readiness `not_ready` until row-control is certified.
- Claim that the father name includes a suffix after `Pulgar`: not promotion-ready; probability `0.30`; canonical readiness `not_ready`.
- Claim that this evidence bridges to a Dario Pulgar identity: unsupported; probability `0.02`; canonical readiness `reject_for_now`.

## Next Action

Keep the staged identity analysis at `hold_for_conversion_qa` / `not_ready`. The next action is targeted full-page original-image row-control review for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, comparing the original image against the assigned chunk and current converted Markdown. Only after that review certifies which physical row controls entry `172` should any birth, parent-child, parent-name, or identity-link claim move toward canonical review.
