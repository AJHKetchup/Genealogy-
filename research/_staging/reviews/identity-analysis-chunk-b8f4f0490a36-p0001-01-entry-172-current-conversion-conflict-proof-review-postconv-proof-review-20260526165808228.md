---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526165808228
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-identity-researcher-20260526135632244.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-identity-researcher-20260526135632244.md
reviewed_source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: hold
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- Canonical readiness: `hold`.
- The staged draft is literally supported in identifying a material row-level conflict: the chunk and source packet describe entry 172 as a Pulgar/Arriagada birth, while the converted Markdown describes entry 172 as a Burgos/de la Cruz birth.
- The source image was checked for this review and supports the staged/source-packet concern that page 58 entry 172 is the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the current converted Markdown.
- The father field remains only partly certified for canonical use. The safe reviewed reading is `Jose del Carmen Pulgar`; the chunk's trailing `S.` or mark should remain unresolved until targeted conversion QA.
- No parent-child relationship, identity merge, Dario-line bridge, name variant, or canonical person fact should be promoted from this staged draft until the converted file, chunk, source packet, and image are reconciled.

## Evidence Strengths

- The source packet, chunk, and visible page image agree on the core Pulgar/Arriagada identity cluster for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged draft accurately preserves the contradictory converted-file reading: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.
- The staged draft properly treats the Dario/Pulgar surname overlap as anti-conflation context only. This record does not name Dario, Arturo, Smith, Geneva, ICRC, a spouse, a child, or any bridging relationship.

## Scored Judgment

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a direct record and the relevant row is visible, but handwriting and derivative disagreement require QA. |
| conversion_confidence_score | 0.30 | Low because the converted Markdown materially conflicts with the chunk/source packet/image at the row level. |
| evidence_quantity_score | 0.66 | Multiple local artifacts were checked, but they are all one source cluster rather than independent corroboration. |
| agreement_score | 0.54 | Source packet, chunk, and image agree; converted Markdown sharply disagrees. |
| identity_confidence_score | 0.70 | Probable Pulgar/Arriagada row identity, but not canonically ready while conversion conflict remains unresolved. |
| claim_probability | 0.76 | The claim that entry 172 is the Pulgar/Arriagada birth is more likely than the converted-file Burgos/de la Cruz reading. |
| relevance_level | 1.00 | Directly reviews the assigned staged draft and its named conflict. |
| relevance_confidence | 1.00 | All reviewed files are referenced by the staged draft/source packet and match the task assignment. |
| canonical_readiness | 0.10 | Hold for targeted conversion QA before any promotion or relationship use. |

## Claim-Level Review

| claim | support judgment | probability | readiness |
| --- | --- | ---: | --- |
| Entry 172 is `Jose del Carmen Segundo Pulgar Arriagada` | Supported by chunk/source packet/image; contradicted by converted Markdown. | 0.76 | hold |
| Father is `Jose del Carmen Pulgar` | Supported as safe name reading if Pulgar row controls; suffix/trailing mark unresolved. | 0.58 | hold |
| Mother is `Juana Arriagada de Pulgar` | Supported by chunk/source packet/image if Pulgar row controls; contradicted by converted Markdown. | 0.65 | hold |
| Entry 172 is `Jose Miguel`, child of Oswaldo Burgos and Concepcion de la Cruz | Supported only by the conflicted converted Markdown reviewed here. | 0.14 | hold/revise after QA |
| Entry 172 bridges to any Dario Pulgar candidate | No literal support in the reviewed source cluster beyond surname context. | 0.04 | not ready |

## Next Action

Targeted conversion QA should reconcile the original image, converted Markdown, chunk, and source packet for page 58 entry 172. The QA note should decide whether the Pulgar/Arriagada row or Burgos/de la Cruz row controls, explain the derivative mismatch, and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an explicitly uncertain reading. After that, rerun proof review before promoting identity facts or parent-child relationships.
