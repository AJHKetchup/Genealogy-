---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260530091638466
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_reference: "page 1; register page 58; physical row entry 172"
review_decision: hold
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md`.
- The requested `$genealogy-proof-review` skill file was not available in the workspace skill list or local skill search, so this review follows the task's explicit proof-review contract.
- The original source PNG named by the source packet, chunk, and conversion review is not present at `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png`; fresh full-page source certification was not possible.
- The assigned chunk and current converted Markdown materially conflict for entry `172`.
- The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The current converted Markdown reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The available staged crop assets support only part of the Pulgar/Arriagada row, mainly the lower parent and informant fields. They do not certify the full page row control or the possible suffix after `Jose del Carmen Pulgar`.
- No canonical claim, relationship, identity merge, Dario-line attachment, or wiki update is ready from this staged draft.

## Evidence Review

The staged identity analysis is well supported as an analysis of a row-control conflict. It accurately reports that the assigned chunk, source packet, and conversion review note carry the Pulgar/Arriagada reading, while the current converted Markdown carries an incompatible Burgos/de la Cruz reading for the same entry number.

The staged crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png` visibly supports Pulgar/Arriagada parent-field content and `Ernesto Herrera L.` in the reviewed row area. The companion bottom crop supports `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Presente al nacimiento`, `Veinte i seis anos`, `Empleado`, and `Calle de Valdivia`. These are meaningful corroborating assets, but they are partial crops rather than the full original page image and therefore do not fully resolve entry numbering, row alignment, child name, birth date/time/place, or the father suffix.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | Civil birth registration is a strong source type, but the original page image is unavailable for this review. |
| conversion_confidence_score | 0.50 | The assigned chunk is coherent and partly crop-supported, but the current converted Markdown gives a different family and event details. |
| evidence_quantity_score | 0.58 | Multiple staged derivatives agree on Pulgar/Arriagada, with partial crop support; full original-image proof is missing. |
| agreement_score | 0.46 | Chunk, source packet, conversion review, and staged analysis agree with each other, but the converted Markdown directly conflicts. |
| identity_confidence_score | 0.70 | Pulgar/Arriagada is plausible for the staged row; same-person, Dario-bridge, and broader Jose/Juana cluster claims are unsupported here. |
| claim_probability | 0.68 | The narrow Pulgar/Arriagada row claim is more likely than the converted Markdown reading in this staged context, but remains unproven. |
| relevance_level | 1.00 | The reviewed files directly concern the assigned entry `172` row-control conflict. |
| relevance_confidence | 0.98 | All checked files identify the same staged draft, source packet, chunk, and entry number. |
| canonical_readiness | 0.12 | Blocked pending full original-image row-control QA and explicit father-field handling. |

## Claim Probability By Hypothesis

| Hypothesis | Probability | Review judgment |
| --- | ---: | --- |
| Entry `172` controls as Pulgar/Arriagada | 0.68 | Supported by the assigned chunk, source packet, conversion review, identity analysis, and partial staged crop assets; not promotion-ready. |
| Entry `172` controls as Burgos/de la Cruz | 0.27 | Present in the current converted Markdown, but contradicted by the staged review set and crop-supported lower fields. |
| Pulgar/Arriagada and Burgos/de la Cruz are the same person or name variants | 0.02 | Unsupported; this is an anti-conflation warning, not a merge path. |
| Entry `172` directly identifies or bridges to any Dario Pulgar candidate | 0.01 | The reviewed evidence does not name Dario or provide an identity bridge. |
| `Juana Arriagada de Pulgar` equals `Juana de Dios Amagada de Pulgar` | 0.04 | Not established by this packet; requires separate parent-cluster proof review. |

## Evidence Strengths

- The staged draft keeps the conflict framed as row control rather than as a name variant.
- The Pulgar/Arriagada reading is consistent across the assigned chunk, source packet, conversion review note, and staged identity analysis.
- Partial crop assets visually support the lower parent and informant fields for the Pulgar/Arriagada row.
- The draft appropriately blocks Dario-line attachment, Burgos/de la Cruz conflation, and broader Jose/Juana cluster merging.

## Next Action

Hold this item for targeted original-image row-control QA. A later reviewer with the full source page image should certify which physical row controls entry `172` and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Until then, keep dependent claims, relationships, identity attachments, and wiki work staged only.
