---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525114353507
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525091344655.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525091344655.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525081514407.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers

1. The assigned converted Markdown and the current chunk materially disagree about entry 172. The converted file transcribes entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, while the chunk and visible source image support a Pulgar/Arriagada entry for the same numbered row.
2. This is a row-level conversion or assignment conflict, not a spelling variant. The staged draft is not ready for canonical claims, relationships, parent attachment, duplicate-person merges, or wiki promotion.
3. The father field remains unresolved for canonical transcription. The chunk reads `Jose del Carmen Pulgar S.`, while the image supports the Pulgar father reading broadly but does not make the final mark safe enough for this proof review to certify as `S.` rather than an unresolved suffix or mark.
4. No direct Dario-line bridge is supported. Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, a grandchild relationship, or the separate public/medical/CV identity contexts discussed in the staged draft.
5. The Juana mother candidate must not be merged with other Juana candidates from this record alone. The reviewed evidence supports a literal mother name only if the Pulgar/Arriagada row is confirmed by conversion QA.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | A civil birth register image is a strong source type for birth and declared-parent facts, but row-level readability is imperfect at this image resolution. |
| conversion_confidence_score | 0.40 | The chunk aligns with the visible source image for the Pulgar/Arriagada row, but the assigned converted Markdown is materially inconsistent. |
| evidence_quantity_score | 0.50 | Review used one source image plus one chunk, one converted Markdown file, the source packet, and the related conflict draft; no independent corroborating record was in scope. |
| agreement_score | 0.48 | The chunk, source packet, conflict draft, staged analysis, and image broadly agree on the Pulgar/Arriagada row, but the converted Markdown disagrees completely on identity-bearing facts. |
| identity_confidence_score | 0.66 | Moderate confidence that the visible entry 172 is the Pulgar/Arriagada cluster; reduced by the unresolved controlling conversion artifact and father suffix. |
| claim_probability | 0.70 | The staged draft's central claim, that entry 172 likely concerns the Pulgar/Arriagada birth while remaining blocked, is probable but not promotion-ready. |
| relevance_level | high | The entry directly concerns Pulgar and Arriagada names and a parent-child cluster relevant to the local staging context. |
| relevance_confidence | 0.92 | Family-line relevance is clear if the Pulgar/Arriagada row is confirmed; broader Dario relevance is not directly supported. |
| canonical_readiness | hold_for_conversion_qa | Targeted conversion QA must reconcile or supersede the converted Markdown before canonical use. |

## Evidence Strengths

- The visible source image supports the chunk's broad reading for page 58, entry 172: a child named `Jose del Carmen Segundo Pulgar Arriagada`, a father named `Jose del Carmen Pulgar` with an unresolved possible suffix or mark, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The reviewed chunk gives a coherent civil registration row with registration date, birth date and place, child name and sex, father, mother, residence, informant, and official signature.
- The source packet and conflict draft correctly preserve the derivative conflict instead of treating the converted Markdown as clean support.
- The staged identity analysis is appropriately conservative: it recommends `hold_for_conversion_qa`, keeps father-name alternatives separate, and rejects unsupported Dario-line or same-person conclusions.

## Review Findings

- Literal support for the Pulgar/Arriagada child identity is present in the chunk and visible image, but the repository's assigned converted Markdown contradicts it.
- Literal support for the Gomez/de la Cruz version exists only in the converted Markdown reviewed here and is contradicted by the chunk and visible image.
- The father-name ending should remain unresolved as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted QA certifies the source-visible form.
- Relationship claims to `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are plausible from the Pulgar row but must remain staged until conversion QA resolves the row conflict.
- Dario-related identity, ancestor, or collateral-line claims are not supported by this entry without a separate proof-reviewed bridge.

## Next Action

Keep this staged identity analysis and dependent claims at `hold_for_conversion_qa`. The next worker should run targeted conversion QA against the source image, assigned converted Markdown, current chunk, and source packet, explicitly deciding whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row and certifying the father field. Rerun proof review after QA before any canonical claim, relationship, identity merge, Dario-line comparison, or wiki promotion.
