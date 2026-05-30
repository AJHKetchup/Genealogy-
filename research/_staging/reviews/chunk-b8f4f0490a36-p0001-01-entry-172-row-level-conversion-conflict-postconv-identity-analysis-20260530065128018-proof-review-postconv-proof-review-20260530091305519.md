---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260530091305519
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
- The original source PNG named by the chunk, source packet, and conversion review is not present under the checked `raw/sources/` paths, so this review cannot certify the full physical row from the original page image.
- The referenced converted Markdown and assigned chunk materially conflict for entry `172`.
- The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The converted Markdown reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The available staged crop assets support parts of the Pulgar/Arriagada parent and informant fields, but they do not replace full-page row-control certification and do not make the possible trailing suffix after `Jose del Carmen Pulgar` promotion-ready.
- No canonical claim, relationship, identity merge, name normalization, Dario-line attachment, or wiki update is ready from this staged draft.

## Evidence Review

The staged draft accurately reports the central conflict between the assigned chunk and the current converted Markdown. The assigned chunk, source packet, and conversion review agree that the Pulgar/Arriagada reading is the working staged reading for physical row entry `172`, while the converted Markdown preserves a contradictory Burgos/de la Cruz derivative reading.

The visible staged crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png` supports the presence of Pulgar/Arriagada parent-field content and the informant `Ernesto Herrera L.` in the reviewed row area. The companion bottom crop also supports `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Presente al nacimiento`, `Veinte i seis anos`, `Empleado`, and `Calle de Valdivia`. These crops are useful corroboration, but because they are partial staged assets, they do not fully resolve entry numbering, page-level row alignment, or all child/birth fields against the converted Markdown.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | Civil birth register is a strong source type, but the original page image is unavailable for this review. |
| conversion_confidence_score | 0.50 | The assigned chunk is coherent and partly crop-supported, but the current converted Markdown gives a wholly different row reading. |
| evidence_quantity_score | 0.58 | Multiple staged derivatives agree on Pulgar/Arriagada, with partial crop support; full original-image proof is missing. |
| agreement_score | 0.46 | Chunk, source packet, and conversion review agree with each other, but the converted Markdown directly conflicts. |
| identity_confidence_score | 0.70 | Pulgar/Arriagada identity is plausible for the staged row; same-person or Dario-bridge claims are unsupported. |
| claim_probability | 0.68 | The narrow Pulgar/Arriagada birth-row claim is more likely than the converted Markdown reading in this staged context, but remains unproven. |
| relevance_level | 1.00 | The reviewed evidence directly concerns the assigned entry `172` row-control conflict. |
| relevance_confidence | 0.98 | All checked files identify the same staged draft, chunk, source packet, and entry number. |
| canonical_readiness | 0.12 | Blocked pending original-image row-control QA and suffix handling. |

## Claim Probability By Hypothesis

| Hypothesis | Probability | Review judgment |
| --- | ---: | --- |
| Entry `172` controls as Pulgar/Arriagada | 0.68 | Supported by assigned chunk, source packet, conversion review, and partial staged crop assets; not promotion-ready. |
| Entry `172` controls as Burgos/de la Cruz | 0.27 | Preserved in the current converted Markdown but contradicted by the staged review set. |
| Pulgar/Arriagada and Burgos/de la Cruz are the same person or name variants | 0.02 | Unsupported; treat as anti-conflation warning. |
| Entry `172` directly identifies or bridges to any Dario Pulgar candidate | 0.01 | Not supported by the reviewed row evidence. |
| `Juana Arriagada de Pulgar` equals `Juana de Dios Amagada de Pulgar` | 0.04 | Not established by this source packet; requires separate parent-cluster proof review. |

## Evidence Strengths

- The staged draft clearly separates literal row conflict from broader identity speculation.
- The Pulgar/Arriagada reading is consistently carried by the assigned chunk, staged source packet, and conversion review note.
- Partial crop assets visually support the lower parent/informant fields for the Pulgar/Arriagada row.
- The draft correctly treats Burgos/de la Cruz as a competing derivative row-control reading, not a spelling variant.
- The draft correctly blocks Dario-line attachment and wider Jose/Juana cluster merging.

## Next Action

Hold this item for targeted original-image row-control QA. A later worker with the full source page image should certify which physical row controls entry `172`, then explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Until that happens, keep dependent claims and relationships staged only.
