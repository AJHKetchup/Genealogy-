---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525220939499
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

- The staged identity analysis correctly identifies a row-level conflict: the chunk/source-packet path gives entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, while the assigned converted Markdown gives entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- This is not a minor transcription variant. The child identity, parent set, birth date, birth place, declarant, and surrounding entries differ between the chunk and converted Markdown.
- The father field in the Pulgar/Arriagada reading remains suffix-sensitive. The visible-source review supports the Pulgar/Arriagada row at a high level, but I am not replacing the derivative transcription with a new certified reading of the suffix.
- The staged draft makes several contextual comparisons to canonical Dario/Pulgar pages. Those comparisons are useful as anti-conflation warnings only; entry 172 does not directly name Dario, Arturo, Smith, Pulgar-Smith, or a later Pulgar-Arriagada identity.
- No claim, relationship, merge, rename, or canonical page update should be promoted from this item until targeted conversion QA resolves the converted-file/chunk mismatch.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth registration image is a strong primary source; image quality is usable but requires careful row and field reading. |
| conversion_confidence_score | 0.35 | Low because the assigned converted Markdown and assigned chunk are mutually incompatible for entry 172. |
| evidence_quantity_score | 0.62 | There is one primary image plus multiple derivative notes, but the derivatives are not independent evidence. |
| agreement_score | 0.42 | The staged draft, conflict note, source packet, chunk, and visible image broadly agree on the Pulgar/Arriagada conflict assessment; the converted Markdown sharply disagrees. |
| identity_confidence_score | 0.70 | The staged draft's leading hypothesis that the relevant row is Pulgar/Arriagada is plausible, but not proof-ready while the conversion conflict remains unresolved. |
| claim_probability | 0.68 | Probable as a held conflict-analysis conclusion, not as a promoted birth or relationship claim. |
| relevance_level | 0.88 | Highly relevant to the Pulgar/Arriagada staging cluster if QA confirms the row; low relevance to Dario identities except as anti-conflation context. |
| relevance_confidence | 0.82 | The reviewed files consistently frame the issue as a Pulgar/Arriagada family-relevance hold with explicit Dario non-attachment warnings. |
| canonical_readiness | 0.10 | Hold for conversion QA; not ready for canonical promotion. |

## Evidence Strengths

- The staged draft is literally supported on the main point it asks to preserve: there is a documented conflict between the assigned converted Markdown and the assigned chunk/source packet.
- The conflict draft and source packet both state the same blocker and recommend `hold_for_conversion_qa`.
- The assigned chunk gives a complete Pulgar/Arriagada row for entry 172 with child, parents, birth details, declarant, and register context.
- The assigned converted Markdown gives a complete but incompatible Burgos/de la Cruz row for entry 172, confirming that the staged draft is not overstating the conflict.
- The referenced source image, reviewed only for high-level verification, appears consistent with the Pulgar/Arriagada row for entry 172 on page 58 and does not resemble the Burgos/de la Cruz reading in the converted Markdown.

## Claim Review

The staged identity-analysis claim should stand as a reviewable conflict assessment. It is adequately supported when it says the item must be held and that the Pulgar/Arriagada, Burgos/de la Cruz, father-field, mother-identity, and Dario-bridge issues must remain separated.

The draft should not be treated as proof that `Jose del Carmen Segundo Pulgar Arriagada` is canonically established, that `Jose del Carmen Pulgar S.` is the same person as an existing `Jose del Carmen Pulgar` page, or that `Juana Arriagada de Pulgar` can be merged with any other Juana candidate. Those are downstream proof questions after conversion QA.

The Dario-related hypotheses are appropriately conservative. This source has no direct same-person or relationship support for `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or canonical `Darío Pulgar Arriagada`.

## Next Action

Hold this staged draft for targeted conversion QA. The next worker should compare the source image, assigned converted Markdown, assigned chunk, and source packet; decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row; and, if the Pulgar/Arriagada row controls, certify the exact father-field reading without normalizing away the suffix or uncertainty.

After QA, rerun proof review before any canonical promotion to claims, relationships, people pages, family pages, or Dario-line identity bridges.
