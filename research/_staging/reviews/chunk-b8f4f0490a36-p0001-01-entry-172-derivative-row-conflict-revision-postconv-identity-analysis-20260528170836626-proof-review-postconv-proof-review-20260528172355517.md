---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528172355517
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-identity-analysis-20260528170836626.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-identity-analysis-20260528170836626.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-evidence-extraction-20260528133324374.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260528133324374.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: blocked
---

# Proof Review: Entry 172 Derivative Row Conflict

## Blockers First

1. Do not promote from this staged identity analysis to canonical claims, relationships, people pages, or family pages. The assigned converted Markdown and the assigned chunk/source packet disagree on the contents of entry `172`.
2. The original page image and the assigned chunk support physical page 58 entry `172` as a Pulgar/Arriagada birth registration, but the converted Markdown records entry `172` as a Burgos/de la Cruz registration. This is a row-control blocker, not a normal variant.
3. Do not attach this source to any Dario/Pulgar-Smith/Pulgar-Arriagada identity cluster. The visible entry names the child as `Jose del Carmen Segundo Pulgar Arriagada`; it does not provide `Dario`, `Arturo`, `Smith`, later-life facts, or a bridge identity.
4. Do not certify the father beyond `Jose del Carmen Pulgar` from this review. The chunk includes a trailing `S.`, but the source packet correctly treats that suffix as not certified.
5. Do not merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` or other Juana candidates from this evidence. This entry supports only the mother name visible in the Pulgar/Arriagada row, subject to row-control QA.

## Evidence Strengths

- The source is a primary civil birth register image for Los Angeles, Chile, 1888, page 58/59. Source quality is high for a birth-registration event once the correct row is controlled.
- Visual inspection of the referenced source image shows page 58 entry `172` as a middle-row registration naming `Jose del Carmen Segundo Pulgar Arriagada`, with parents in the Pulgar/Arriagada columns and declarant `Ernesto Herrera L.`.
- The assigned chunk agrees with the source packet on the Pulgar/Arriagada row: registration date 7 April 1888; birth date 8 March 1888; male child; father `Jose del Carmen Pulgar S.` in the chunk; mother `Juana Arriagada de Pulgar`; declarant `Ernesto Herrera L.`.
- The staged identity analysis correctly keeps the derivative conflict explicit and recommends hold for conversion QA instead of silently normalizing the converted Markdown.
- The staged analysis correctly treats Dario identity connections and parent merges as unsupported by this evidence set.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 3/10 for the assigned converted Markdown because it conflicts with the image/chunk; 7/10 for the Pulgar row reading after visual check, still pending row-control QA |
| evidence_quantity_score | 4/10 |
| agreement_score | 4/10 overall because derivative layers conflict; 8/10 between the source image, assigned chunk, and source packet for the Pulgar/Arriagada row |
| identity_confidence_score | 7/10 for a distinct child recorded as `Jose del Carmen Segundo Pulgar Arriagada`; 6.5/10 for the mother as `Juana Arriagada de Pulgar`; 6/10 for the father as `Jose del Carmen Pulgar`; 1/10 for same-person identity with any Dario/Pulgar-Smith candidate |
| claim_probability | 0.82 that physical entry `172` on page 58 is the Pulgar/Arriagada row; 0.72 that the mother claim is correctly bounded; 0.68 that the father claim is correctly bounded without suffix; 0.03 that the child is a Dario/Pulgar-Smith candidate |
| relevance_level | high for Pulgar/Arriagada family triage and row-control repair; low for Dario identity attachment |
| relevance_confidence | 0.90 |
| canonical_readiness | blocked: hold for targeted conversion QA and proof-review rerun before any canonical promotion |

## Review Finding

The staged identity analysis is supported as a conflict analysis. Its central blocker is real: the visible source image and assigned chunk identify entry `172` as the Pulgar/Arriagada row, while the assigned converted Markdown gives a different Burgos/de la Cruz registration. The staged draft appropriately treats this as a conversion row-control conflict and blocks canonical use.

The Pulgar/Arriagada row is relevant and probably correct for physical entry `172`, but current evidence handling is not canonically ready because the derivative conversion disagreement must be resolved first. The Dario and Pulgar-Smith identity bridges remain unsupported by this source.

## Next Action

Run targeted conversion QA on the exact source image, assigned converted Markdown, and assigned chunk. The QA result should decide the controlling row for entry `172`, document why the converted Markdown disagrees, and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an explicitly uncertain reading. After that, rerun proof review before staging any canonical claim or relationship.
