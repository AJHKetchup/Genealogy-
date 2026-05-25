---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525220052958
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-analysis-20260525211749345.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-analysis-20260525211749345.md"
reviewed_files:
  - "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-analysis-20260525211749345.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict Identity Analysis

## Blockers First

- The staged identity analysis is supported as a conflict analysis, not as promotion-ready proof. The assigned converted Markdown still records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, while the chunk, source packet, conflict draft, and visible page image support a different entry 172 row for `Jose del Carmen Segundo Pulgar Arriagada`.
- The source image inspection supports the Pulgar/Arriagada row at the row-assignment level, but the father field remains too uncertain for normalization. The review cannot promote `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` as a resolved father identity.
- The analysis correctly blocks same-person or relationship jumps to Dario-line identities. Entry 172 does not literally name Dario, Arturo, Smith, Pulgar-Smith, or a descendant bridge.
- Existing canonical or staged snippets that match the Pulgar/Arriagada row appear derivative of the same evidence cluster and should not be treated as independent confirmation.

## Evidence Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register page image is a strong original-style source for the event, but this review did not perform a full fresh source transcription. |
| conversion_confidence_score | 0.42 | The chunk and image agree at a high level, but the assigned converted Markdown is materially wrong or misassigned for the row. |
| evidence_quantity_score | 0.62 | One source image plus several local derivatives; quantity is adequate for a hold decision but not independent enough for promotion. |
| agreement_score | 0.54 | Chunk, source packet, conflict draft, and image agree against the converted Markdown; derivative disagreement remains severe. |
| identity_confidence_score | 0.70 | `Jose del Carmen Segundo Pulgar Arriagada` is probably the visible entry 172 child, but unresolved conversion QA prevents canonical identity use. |
| claim_probability | 0.68 | The staged claim that a Pulgar/Arriagada row controls is probable, but not certified for canonical claims. |
| relevance_level | high | The row is directly relevant to Pulgar/Arriagada family research if confirmed. |
| relevance_confidence | 0.90 | Pulgar and Arriagada are visible in the staged evidence and consistent with the family-relevance filter. |
| canonical_readiness | hold_for_conversion_qa | No promotion, merge, relationship creation, or Dario-line attachment should occur from this review. |

## Evidence Strengths

- The staged identity analysis accurately identifies a row-level conflict rather than treating the two readings as name variants.
- The chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, with mother `Juana Arriagada de Pulgar`, registration date 7 April 1888, and birth date 8 March 1888.
- The source packet and conflict draft faithfully report the contradiction with the assigned converted Markdown.
- The page image, viewed for this proof review, visually supports the chunk/source-packet row assignment for entry 172 on page 58 at a high level. It does not support replacing the uncertainty note for the father suffix with a firm normalized reading.
- The staged analysis appropriately treats Dario comparisons as anti-conflation context only.

## Review Judgment

The staged draft should remain held. Its main conclusion is sound: this is a conversion/row-assignment conflict that blocks canonical promotion. The Pulgar/Arriagada reading is more probable than the Burgos/de la Cruz reading for the referenced image and chunk, but the assigned converted Markdown is still contradictory and the father-field suffix remains unresolved.

No claim should be promoted to `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or other canonical folders from this staged draft.

## Next Action

Run targeted conversion QA against the page image, assigned converted Markdown, assigned chunk, and source packet. The QA note should explicitly decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and if Pulgar/Arriagada controls, should preserve or certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
