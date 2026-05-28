---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260528221039468"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

1. The staged identity-analysis draft is materially supported in identifying a row-control conflict, but the conflict remains unresolved: the chunk and visible page image support a Pulgar/Arriagada row for entry 172, while the converted Markdown still transcribes entry 172 as a Burgos/de la Cruz row.
2. The current converted Markdown is not reliable for promotion of entry-172 facts because it disagrees with the chunk, source packet, and visual page check on the child, parents, birth date, birth place, and informant.
3. The father field in the Pulgar/Arriagada row is not fully certified. The visible source and staged materials support `Jose del Carmen Pulgar` with a trailing mark or abbreviation, but this review should not force the reading to `S.` without targeted conversion QA.
4. No relationship, identity merge, Dario-line bridge, or canonical person/family update is ready from this staged draft. The draft correctly treats Dario/Pulgar-Arriagada/Pulgar-Smith links as anti-conflation checkpoints only.

## Evidence Strengths

- The assigned chunk gives entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source packet reports a visual source-image check finding page 58, row 172 as the Pulgar/Arriagada row rather than the Burgos/de la Cruz row.
- Direct visual review in this proof pass is consistent with the source packet: page 58, entry 172 visibly contains the Pulgar/Arriagada family row.
- The staged identity-analysis draft appropriately recommends `hold_for_conversion_qa` and does not promote child identity, parent relationships, parent identity merges, or Dario-line attachments.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a high-value primary source, but the current proof item depends on resolving a transcription/control conflict. |
| conversion_confidence_score | 0.42 | Chunk and visual check agree on Pulgar/Arriagada, but the converted Markdown assigns the same entry to a different family. |
| evidence_quantity_score | 0.62 | Evidence includes one source image, one chunk, one converted file, one source packet, and one conflict draft; quantity is enough to diagnose conflict but not enough for canonical promotion. |
| agreement_score | 0.48 | Source packet, chunk, and image agree against the converted Markdown; local conversion artifacts do not yet have full agreement. |
| identity_confidence_score | 0.70 | Entry 172 is probably the Pulgar/Arriagada row, but the unresolved converted-file contradiction and father-field uncertainty lower identity confidence. |
| claim_probability | 0.74 | The staged draft's central claim that this is a row-level conversion conflict is well supported; the Pulgar row itself remains promotion-blocked. |
| relevance_level | 1.00 | The reviewed materials directly concern the assigned staged draft and entry-172 conversion conflict. |
| relevance_confidence | 0.98 | All reviewed artifacts point to the same page, entry number, source image, chunk id, and staged conflict. |
| canonical_readiness | 0.05 | Hold. The item should not be promoted until targeted conversion QA certifies the controlling row and father-field reading. |

## Claim Review

The staged draft's main proof posture is supported: this is a severe row-level conversion conflict, not a promotion-ready identity claim. The visible source image and assigned chunk favor the Pulgar/Arriagada row for entry 172, while the converted Markdown contains a different entry-172 family. That disagreement blocks canonical use of either the Pulgar/Arriagada or Burgos/de la Cruz identity facts until conversion QA decides the controlling transcription.

Relationship claims are not ready. If later QA certifies the Pulgar/Arriagada row, the row can support a child-parent structure involving `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`, but this review cannot certify the father's trailing abbreviation or merge him to any existing Jose del Carmen Pulgar candidate.

The draft's anti-conflation treatment of Dario-related people is appropriate. Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, or a direct bridge to any Dario Pulgar-Arriagada cluster.

## Next Action

Run targeted conversion QA against the source image for page 58, entry 172. The QA note should decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row and should separately certify the father's field as exactly visible. Keep this staged draft and all dependent claims on hold until that QA exists.
