---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260527202018552"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
reviewed_files:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: "hold_for_conversion_qa"
---

# Proof Review: Entry 172 Derivative Row Conflict

## Blockers

1. The staged draft is correct that the referenced raw source image and job page image are not available in this checkout. I verified the referenced `raw/sources/...Entry No. 172;.png` path and the job `page-images/page-0001.png` path are absent, so this review cannot independently inspect the handwritten row.
2. The derivative artifacts are materially incompatible. The assigned chunk/source packet identify entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the current converted Markdown identifies entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
3. Because row control is unresolved in the currently referenced conversion set, no child identity, parent-child relationship, father suffix, mother identity, or Dario-line bridge from entry `172` is canonical-ready.
4. The father field remains bounded. The chunk literal reads `Jose del Carmen Pulgar S.`, but this review cannot visually certify whether the terminal mark is `S.`, another mark, or absent.
5. No reviewed evidence for this staged draft names Dario, Dario Arturo, Dario Jose, or Arturo in entry `172`; any Dario attachment would be an unsupported relationship jump.

## Evidence Strengths

- The staged draft accurately describes the row-level derivative conflict and treats it as a conversion QA blocker rather than a promotable identity finding.
- The source packet preserves the Pulgar/Arriagada reading as a held derivative packet and explicitly warns that physical row control is not certified in the absence of the image.
- The current converted Markdown directly supports the existence of an incompatible Burgos/de la Cruz reading for entry `172`, confirming the conflict is not a spelling variant.
- Prior staged review/task context located in the assigned review area is consistent with holding the record for row-control QA and father-field certification, but this review does not treat those notes as a substitute for the absent image.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.84 | A civil birth register would be strong direct evidence if the image were available; score is reduced because this review only has conflicting derivatives. |
| conversion_confidence_score | 0.32 | The chunk/source packet and converted Markdown disagree on child, parents, birth date, place, and informant cluster. |
| evidence_quantity_score | 0.48 | Several derivative and staged context files agree that a conflict exists, but there is only one underlying source event and no available image for this review. |
| agreement_score | 0.38 | The chunk and source packet agree with each other; the converted Markdown gives a different family. Agreement is strong for the existence of conflict, weak for the controlling row. |
| identity_confidence_score | 0.58 | Pulgar/Arriagada is plausible from the assigned chunk and held packet, but identity confidence is capped by the unresolved derivative conflict and absent image. |
| claim_probability | 0.88 | High probability that the staged draft's central claim is correct: entry `172` must remain held for conversion QA. |
| relevance_level | high | The conflict directly affects family-relevant Pulgar/Arriagada identity and relationship candidates. |
| relevance_confidence | 0.91 | The reviewed files are all tied to the assigned draft, source packet, chunk, and converted file. |
| canonical_readiness | hold_for_conversion_qa | Do not promote, merge, rename, or update canonical pages from this draft. |

## Claim Probability By Claim

| Claim | Probability | Readiness |
| --- | ---: | --- |
| A row-level derivative conflict exists for entry `172`. | 0.96 | review-supported |
| Entry `172` is the Pulgar/Arriagada birth row. | 0.70 | hold_for_conversion_qa |
| Entry `172` is the Burgos/de la Cruz birth row. | 0.20 | not_ready |
| Father can be canonically recorded as `Jose del Carmen Pulgar S.` from this review. | 0.30 | not_ready |
| Entry `172` supports any Dario-line same-person or ancestor bridge. | 0.04 | not_ready |

## Next Action

Keep the staged draft at `hold_for_conversion_qa`. The next action is targeted conversion QA against the source image or an accepted image-reviewed QA note that explicitly reconciles the assigned chunk with the current converted Markdown and certifies the father field only as far as the visible source supports: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that QA decision is recorded, rerun proof review before any canonical claim, relationship, identity merge, parent-page attachment, or Dario-line comparison is promoted.
