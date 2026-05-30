---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260530073828413
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_image_status: missing_from_raw_sources
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md`.
- The original source image referenced by the chunk manifest and source packet is not present in `raw/sources/` under either the accented or unaccented path spelling checked in this workspace. Fresh physical-row certification is therefore unavailable in this review.
- The canonical converted Markdown and conversion-job page Markdown both identify entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888.
- The assigned chunk and source packet identify entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888.
- This is a material row-control conflict, not a name variant. Parent, child, birth date, birth time, place, and informant differ.
- The staged crop assets visibly support Pulgar/Arriagada parent and informant fields, but they do not certify the full row from the original page image and do not make the trailing suffix after `Jose del Carmen Pulgar` promotion-ready.
- No Dario-line identity or relationship bridge is supported by this record. The staged draft correctly keeps Dario, Arturo, Smith, and later Pulgar identity clusters out of canonical attachment.

## Evidence Strengths

- The assigned chunk gives a coherent literal row for `172` with Pulgar/Arriagada child and parent fields, and its chunk manifest links it to the same converted file/source SHA family under review.
- The source packet preserves the derivative conflict instead of silently replacing the converted Markdown reading.
- The conversion review note correctly marks the item `hold_for_conversion_qa` because the original source image was unavailable to that worker.
- The staged crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png` visibly supports `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.` in the Pulgar/Arriagada row-control hypothesis.
- The bottom crop further supports `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Presente al nacimiento`, `Empleado`, and `Calle de Valdivia`; it still leaves the full-row certification and father suffix unresolved.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.58 | Civil registration is a strong source type, but this review lacks the original page image and can only inspect derivative text plus staged crops. |
| conversion_confidence_score | 0.44 | The chunk and crops support Pulgar/Arriagada fields, while the converted Markdown/page Markdown materially disagree. |
| evidence_quantity_score | 0.54 | Multiple local artifacts exist, but they are derivative and internally conflicting; crop coverage is partial. |
| agreement_score | 0.32 | Chunk/source packet/crop review agree with each other, but canonical conversion artifacts conflict on the central row identity. |
| identity_confidence_score | 0.68 | Pulgar/Arriagada row identity is plausible and partially crop-supported, but not certified enough for promotion. |
| claim_probability | 0.66 | The staged conclusion that the Pulgar/Arriagada reading is probable but blocked is supported; exact promoted facts remain on hold. |
| relevance_level | high | The draft directly addresses the assigned row-control conflict and anti-conflation risk. |
| relevance_confidence | 0.96 | All reviewed artifacts concern entry `172` and the same conflict. |
| canonical_readiness | 0.12 | Blocked pending original-image row-control certification and conversion repair/annotation. |

## Claim Review

| Claim or hypothesis | Judgment | Probability | Notes |
| --- | --- | ---: | --- |
| Entry 172 controls as Pulgar/Arriagada | Hold | 0.66 | Supported by assigned chunk and staged crops for parent/informant fields; not fully certifiable without original image. |
| Entry 172 controls as Burgos/de la Cruz | Hold as competing derivative reading | 0.30 | Supported by converted Markdown and page Markdown, but conflicts with assigned chunk and staged crop evidence. |
| Pulgar/Arriagada and Burgos/de la Cruz are the same person or name variants | Reject for promotion | 0.02 | No identity-bearing overlap beyond entry number. |
| Entry 172 directly connects to any Dario Pulgar candidate | Reject for promotion | 0.01 | No Dario, Arturo, Smith, spouse, child, or descendant bridge appears in reviewed evidence. |
| Father field should be promoted as `Jose del Carmen Pulgar S.` | Hold | 0.40 | The chunk reads a suffix, but crop review does not certify it. Use only bounded staged discussion until original-image review. |
| Mother field `Juana Arriagada de Pulgar` in the Pulgar row | Hold | 0.70 | Partially crop-supported and chunk-supported, but dependent on row-control certification. |

## Review Decision

The staged draft is broadly supported as a cautious identity/conflict analysis. Its central conclusion should remain `hold_for_conversion_qa` with `canonical_readiness: blocked`. The review should not promote either row reading, parent-child relationship, or Dario-line identity connection to canonical folders.

Minor note: the staged draft's first blocker references the earlier staged conflict draft as the exact reviewed draft. For this proof-review task, the exact reviewed draft is the identity-analysis file named in the task metadata above. This does not change the evidence judgment.

## Next Action

Run targeted original-image row-control certification for `CHUNK-b8f4f0490a36-P0001-01`, register page 58, physical row entry `172`, using the original page image matching SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`. The certifying worker should decide the controlling row and explicitly state whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain bounded form.
