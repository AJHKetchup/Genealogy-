---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527195113177
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
reviewed_artifacts:
  - "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_image_status: unavailable_at_recorded_path
source_quality_score: 0.70
conversion_confidence_score: 0.25
evidence_quantity_score: 0.45
agreement_score: 0.20
identity_confidence_score: 0.30
claim_probability: 0.35
relevance_level: high_if_pulgar_row_controls
relevance_confidence: 0.55
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row Conflict Identity Analysis

## Blockers First

- The reviewed staged draft is exactly `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md`.
- Canonical readiness is `not_ready`. No child identity, birth fact, parent-child relationship, parent same-person claim, or Dario-line bridge should be promoted from this draft.
- The referenced source image path, `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, was not available as written during review. A limited filename search under `raw/sources` did not locate the entry-172 image.
- The derivative artifacts remain in direct row-level conflict. The chunk and source packet read entry 172 as a Pulgar/Arriagada birth; the converted Markdown reads entry 172 as a Burgos/de la Cruz birth.
- Because the visible source image could not be checked here, this review cannot certify the controlling row or the father-field ending after `Jose del Carmen Pulgar`.
- The Dario-line relevance remains unsupported by this draft. The checked artifacts do not name Dario, Dario Arturo, Dario Jose, Darío, Smith, a spouse, a child, or a grandchild bridge.

## Evidence Strengths

- The assigned chunk and the staged source packet agree on the same Pulgar/Arriagada row for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on 8 March 1888 at 3 p.m. at `Calle de Valdivia`, and informant `Ernesto Herrera L.`.
- The converted Markdown independently supports the existence of a serious conversion conflict by giving the same entry number as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth on 6 April 1888 at 10 p.m. in `En esta`.
- The staged draft correctly treats this as a row-control problem rather than a spelling variant. `Jose Miguel` is not a plausible literal variant of `Jose del Carmen Segundo Pulgar Arriagada`, and the parents, birth date, place, and informant also differ.
- The staged draft appropriately blocks promotion and calls for targeted conversion QA before identity, relationship, or canonical wiki use.

## Scores

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.70 | Civil birth registration would be a strong original source type, but this review could not inspect the image at the recorded path. |
| conversion_confidence_score | 0.25 | Two derivative transcriptions disagree on the entire row for entry 172. |
| evidence_quantity_score | 0.45 | There are multiple derivative artifacts, but no accessible source image confirmation in this review. |
| agreement_score | 0.20 | Chunk/source packet agree with each other, but the converted Markdown gives an incompatible row. |
| identity_confidence_score | 0.30 | The Pulgar/Arriagada identity claim is plausible only if the Pulgar row controls; same-person links remain unproved. |
| claim_probability | 0.35 | Probability is held down by source-image unavailability and row-control conflict. |
| relevance_level | high_if_pulgar_row_controls | The row is highly relevant to Pulgar/Arriagada research only if the chunk/source-packet reading is certified. |
| relevance_confidence | 0.55 | Relevance is clear under the Pulgar reading but not under the Burgos/de la Cruz reading. |
| canonical_readiness | not_ready | Requires targeted conversion QA and renewed proof review. |

## Claim Judgment

The staged draft is supported as a conflict analysis and hold recommendation. It is not supported as proof for promoting the Pulgar/Arriagada birth, the Burgos/de la Cruz birth, any Jose/Juana same-person claim, or any Dario-line bridge.

The safest scored judgment is `hold_for_conversion_qa`: the source type is potentially strong, but the current evidence package is derivative-only at review time and internally contradictory.

## Next Action

Perform targeted conversion QA against the actual page image and the two conflicting derivative readings. The QA note should identify which row controls entry 172 and certify the father field only to the visible-source level, such as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, rerun proof review before any canonical update, claim promotion, parent-child relationship promotion, Jose/Juana identity merge, or Dario-line comparison.
