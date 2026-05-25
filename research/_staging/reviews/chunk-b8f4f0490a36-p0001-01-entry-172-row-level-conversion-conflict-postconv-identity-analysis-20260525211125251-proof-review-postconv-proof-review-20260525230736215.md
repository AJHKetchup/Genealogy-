---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525230736215
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211125251.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211125251.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged identity analysis is supported as a conflict hold, not as a promotable identity or relationship proof.
- The assigned converted Markdown and assigned chunk describe incompatible entry-172 rows. The converted Markdown gives `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the chunk and source packet give `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- This is not a spelling variant or ordinary uncertainty. It is a row-level conversion/file-assignment conflict involving different children, parent pairs, dates, residences, and family clusters.
- The father field in the Pulgar/Arriagada reading remains unresolved at the suffix level. Do not normalize `Jose del Carmen Pulgar S.` to `Jose del Carmen Pulgar` without targeted image QA.
- Entry 172 does not literally name any Dario/Darío candidate. Any Dario-line use is anti-conflation only and is not ready for a lineage bridge.

## Evidence Strengths

- The source type is a civil birth registration, which would be strong direct evidence for a birth identity and parent-child relationship after row control is certified.
- The assigned chunk and staged source packet agree on the Pulgar/Arriagada row for register page 58, entry 172.
- The referenced page image visibly supports the presence of a Pulgar/Arriagada-looking entry in row 172 and does not support treating the conflict as a simple name variant.
- The staged identity analysis correctly preserves the boundary between verification context and transcription correction by routing the item to conversion QA rather than rewriting the converted file.

## Scored Judgment

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a high-quality direct source for the event, but the current proof depends on derivative row control that is disputed. |
| conversion_confidence_score | 0.30 | The converted Markdown and chunk disagree at the controlling row level for entry 172. |
| evidence_quantity_score | 0.55 | There is one source image plus two derivative readings; quantity is enough to identify the conflict but not enough to resolve it. |
| agreement_score | 0.42 | Chunk and source packet agree with each other, but the assigned converted Markdown directly conflicts. |
| identity_confidence_score | 0.58 | Pulgar/Arriagada is the better-supported working identity for the staged conflict, but row control and father suffix remain unresolved. |
| claim_probability | 0.68 | It is probable that the Pulgar/Arriagada row is the intended controlling row, but the probability is below promotion threshold because the assigned converted file says otherwise. |
| relevance_level | high | The conflict directly affects child identity, parent names, parent-child relationships, and possible duplicate/merge handling. |
| relevance_confidence | 0.90 | The referenced files all concern the same entry number and source image. |
| canonical_readiness | not_ready | Hold for conversion QA before any claim, relationship, identity merge, or Dario-line comparison is promoted. |

## Review Assessment

The staged identity analysis is literally supported as a proof judgment about a conflict. It should remain `hold_for_conversion_qa`. Its main conclusion, that the Pulgar/Arriagada reading is more plausible than the Burgos/de la Cruz reading, is reasonable but not canonical-ready because the controlling converted Markdown still records a different row.

Identity risk is high if this is promoted prematurely. The child, father, and mother would be assigned to a different family cluster depending on which derivative controls. Relationship risk is also high because a parent-child relationship to `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` cannot be accepted while the assigned converted file names `Oswaldo Burgos` and `Concepcion de la Cruz`.

No relationship jump to any Dario/Darío candidate is supported. The only relevant Dario-line conclusion is negative: entry 172 should not be used as a bridge to a Dario identity unless later evidence supplies that connection.

## Next Action

Keep the staged draft on hold and send the source image, assigned converted Markdown, assigned chunk, and source packet to targeted conversion QA. QA should identify which row controls entry 172 and record the father field with explicit uncertainty if needed. After QA, rerun proof review before promoting any canonical claim, parent-child relationship, same-person merge, or Dario-line linkage.
