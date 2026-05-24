---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260524140855216
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
review_status: hold
canonical_readiness: hold
review_date: 2026-05-24
reviewed:
  - research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- Canonical readiness is `hold`. The assigned converted Markdown transcribes entry 172 as a different child-parent cluster: child `Jose Francisco`, father `Oswaldo Gomez`, and mother `Rosario de la Cruz de la Maza`. The assigned chunk and source packet instead describe entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- The conflict is material and row-level. It affects the child name, parents, birth date/time, birthplace, informant, and associated registration details. No identity, birth-event, parent-child, or parental-pair claim should be promoted from this staged draft while the controlling transcript remains unreconciled.
- The father-name suffix is not promotion-ready. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet flags the suffix as unresolved from the image. A later conversion QA note should either confirm the suffix, reject it, or preserve an explicitly uncertain reading.
- The source does not name Dario. The staged draft correctly blocks merger into Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or any Dario Pulgar identity by surname context alone.

## Scores

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.88 | Civil birth registration image is a strong primary source class for birth facts and stated parentage; legibility is usable but not perfect at full-page scale. |
| conversion_confidence_score | 0.45 | The assigned chunk and source packet align with the visible Pulgar/Arriagada row, but the assigned converted Markdown gives an unrelated Gomez/de la Cruz row. |
| evidence_quantity_score | 0.64 | One direct source image, one current chunk, one source packet, and one conflicting converted Markdown file were reviewed; no independent corroborating source was in scope. |
| agreement_score | 0.50 | Chunk, source packet, and image agree on the Pulgar/Arriagada cluster, but the converted Markdown materially disagrees. |
| identity_confidence_score | 0.72 | Moderately high that the staged hold note identifies the relevant Pulgar/Arriagada cluster, reduced by the unresolved derivative conflict and father suffix. |
| claim_probability | 0.86 | The staged draft's recommendation to hold for conversion QA is strongly supported by the reviewed evidence. |
| relevance_level | high | The record is directly relevant to the Pulgar/Arriagada cluster but is also a high-risk identity source until QA resolves the row conflict. |
| relevance_confidence | 0.95 | The reviewed materials all point to the same assigned entry number and source packet context. |
| canonical_readiness | hold | Conversion QA must reconcile or supersede the converted Markdown before canonical promotion. |

## Evidence Strengths

- The source class is strong: a Chilean civil birth register page can directly support a child's registered name, sex, birth timing and place, stated parents, informant, and registration context once transcription is stable.
- The assigned chunk and source packet provide literal support for the staged draft's central observation that the working Pulgar/Arriagada row differs from the converted Markdown's Gomez/de la Cruz row.
- The staged draft handles uncertainty appropriately by recommending `hold_for_conversion_qa` and preserving both father-name readings instead of forcing a canonical name form.
- The staged draft avoids an unsupported relationship jump to any Dario identity. That guardrail is well supported because no Dario is named in the reviewed entry.

## Review Judgment

The staged draft is supportable as a proof-review hold and identity-risk note. It should not be treated as final proof of child identity or parent-child relationships until the conversion conflict is resolved. The strongest supported claim is procedural: this evidence cluster should remain out of canonical promotion while the converted Markdown and chunk disagree on the identity of entry 172.

Claim probability is high for the hold recommendation and Dario guardrail, moderate for the Pulgar/Arriagada identity cluster pending QA, and lower for the exact father-name suffix. The Gomez/de la Cruz reading has support only in the conflicting converted Markdown and should not be promoted from this task.

## Next Action

Keep this staged draft at `hold_for_conversion_qa`. A conversion QA worker should reconcile the assigned converted Markdown against the source image and current chunk, explicitly decide or mark uncertain the father-name suffix, and then rerun proof review on any child identity, birth fact, child-parent, or parental-pair claims before canonical promotion.
