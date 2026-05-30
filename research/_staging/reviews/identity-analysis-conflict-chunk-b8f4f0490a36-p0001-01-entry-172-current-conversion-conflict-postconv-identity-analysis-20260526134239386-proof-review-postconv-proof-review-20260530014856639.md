---
type: proof_review
role: claim_reviewer
status: complete
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md
worker: postconv-proof-review-20260530014856639
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md
reviewed_sources:
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-markdown/page-0001.md
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md`.
- The referenced raw source image path and manifest page image path were not available for direct inspection in this workspace during this review. I therefore cannot independently certify the visible handwriting.
- The referenced current converted Markdown and conversion job page Markdown identify entry 172 as a Burgos/de la Cruz birth for child `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- The referenced current chunk and source packet identify entry 172 as a Pulgar/Arriagada birth for child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar` with unresolved trailing mark, and mother `Juana Arriagada de Pulgar`.
- This is a row-level derivative conflict, not a name variant. Child, parents, birth date/time, birthplace, informant, and surrounding page readings differ.
- Parent-child claims, parent identities, cross-entry Jose/Juana merges, and any Dario-line attachment must remain held. The staged draft itself correctly treats Dario only as an anti-conflation concern; no Dario person is named in the reviewed entry readings.
- The father suffix or trailing mark after `Jose del Carmen Pulgar` is not ready for normalization. The source packet explicitly does not certify the final `S.`.

## Evidence Strengths

- The staged draft accurately preserves the central conflict between the chunk/source-packet reading and the current converted-file/page-Markdown reading.
- The source packet states that prior image review favored the Pulgar/Arriagada row and explains why conversion QA is still required.
- The chunk and source packet agree with each other on the Pulgar/Arriagada names, registration date, birth date/time, birthplace, parents, and informant.
- The converted Markdown and page-level conversion job Markdown agree with each other on the competing Burgos/de la Cruz reading.
- The staged draft does not over-promote the Pulgar/Arriagada reading and does not make an unsupported bridge to Dario identities.
- The recommended hold disposition is appropriate because the conflict is material and the direct image was unavailable to this reviewer.

## Scored Judgment

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | A Chilean civil birth register would be strong direct evidence if the row were confirmed, but this review could not inspect the image directly. |
| conversion_confidence_score | 0.25 | The derivative artifacts disagree at the row level, and the image needed to adjudicate them was unavailable here. |
| evidence_quantity_score | 0.58 | There are multiple local artifacts, but they split into two internally consistent and mutually incompatible derivative groups. |
| agreement_score | 0.30 | Chunk/source packet agree with each other; converted Markdown/page Markdown agree with each other; the two groups materially conflict. |
| identity_confidence_score | 0.40 | The Pulgar/Arriagada hypothesis has stronger staged packet support, but direct identity claims remain blocked by conversion conflict and missing image inspection. |
| claim_probability | 0.62 | It is plausible that entry 172 is the Pulgar/Arriagada row based on chunk and packet support, but the probability must be discounted because the current conversion says otherwise and the image was unavailable. |
| relevance_level | high | The reviewed materials directly concern the staged entry-172 identity conflict and Pulgar/Arriagada relevance. |
| relevance_confidence | 0.95 | All reviewed artifacts are explicitly tied to the same staged draft, chunk id, and entry number. |
| canonical_readiness | hold_for_conversion_qa | Do not promote or revise canonical claims until targeted QA reconciles the image, converted Markdown, page Markdown, chunk, and source packet. |

## Claim-Level Findings

| claim or hypothesis | support judgment | probability | readiness |
| --- | --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by chunk and source packet; contradicted by current converted Markdown/page Markdown; not image-certified in this review. | 0.62 | hold_for_conversion_qa |
| Entry 172 is the Burgos/de la Cruz birth row for `Jose Miguel`. | Supported by current converted Markdown and page Markdown; contradicted by chunk and source packet. | 0.25 | hold_for_conversion_qa |
| Father field should be normalized to `Jose del Carmen Pulgar S.`. | Chunk gives this reading, but source packet certifies only `Jose del Carmen Pulgar` with trailing mark unresolved. | 0.45 | hold_for_conversion_qa |
| Parent-child relationships from the Pulgar row are promotable now. | Relationship structure is plausible only if Pulgar row is controlling; the controlling row is not yet certified. | 0.35 | hold |
| Entry 172 bridges to any Dario identity. | No reviewed artifact names Dario or supplies a lineage bridge. | 0.01 | reject_for_this_draft |

## Identity And Relationship Risk

- Identity risk is high if the converted Burgos/de la Cruz row is treated as the same evidence item as the Pulgar/Arriagada row.
- Relationship risk is high if child-parent links are promoted before row control is settled.
- Merge risk is moderate to high for `Jose del Carmen Pulgar` because the unresolved trailing mark and absent cross-entry bridge could incorrectly merge distinct Jose candidates.
- Dario-line conflation risk is high if surname or later family context is used as a bridge. This draft supplies no direct Dario evidence.

## Next Action

Keep the staged draft at `hold_for_conversion_qa`.

Run targeted conversion QA against the original page image or manifest page image, current converted Markdown, conversion job page Markdown, current chunk, and source packet. QA should explicitly decide which row is controlling for entry 172 and certify the father field as one of: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before any canonical promotion of child identity, birth facts, father relationship, mother relationship, parent identities, or cross-entry Jose/Juana comparisons. Do not attach this evidence to a Dario page without a later source that directly supports that bridge.
