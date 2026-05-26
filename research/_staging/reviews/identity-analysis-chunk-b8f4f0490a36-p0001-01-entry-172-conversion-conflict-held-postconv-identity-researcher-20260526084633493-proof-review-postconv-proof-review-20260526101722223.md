---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526101722223
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
created: 2026-05-26
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

- The staged identity analysis is correctly blocked by a derivative row-control conflict: the current converted Markdown records entry `172` as a Burgos/de la Cruz birth, while the chunk, held source packet, and visible source image support a Pulgar/Arriagada row for entry `172`.
- The conflict affects identity-bearing facts, not minor wording: child name, birth date/time, birth place, father, mother, informant, residence, and parent-child relationships all differ.
- The father field in the Pulgar/Arriagada row is not fully certified from the reviewed evidence. Preserve uncertainty among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA decides the literal reading.
- No relationship bridge to any Dario Pulgar identity is supported by this evidence. The staged analysis is right to treat Dario comparisons as anti-conflation only.
- Canonical promotion is not ready. Do not promote child identity, parent-child relationships, parent identities, same-person merges, or Dario-line links from this staged draft.

## Review Scope

- Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md`.
- Reviewed referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md`.
- Reviewed held source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md`.
- Reviewed current converted Markdown and chunk named in the staged draft.
- Checked the referenced source image only to verify the row-control issue; no raw source or conversion file was edited.

## Evidence Judgment

| Dimension | Score / Level | Review Finding |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a strong source type for names, birth facts, parents, and informant details, but the review is constrained by image legibility and conflicting derivative files. |
| conversion_confidence_score | 0.34 | The chunk and converted Markdown disagree on the same entry number; the father-field ending also remains uncertain. |
| evidence_quantity_score | 0.62 | There is one source image plus two incompatible derivative transcriptions and a held packet. Quantity is enough to identify the conflict, not enough to resolve all literal fields. |
| agreement_score | 0.38 | The chunk, packet, and image align broadly on Pulgar/Arriagada, but the current converted Markdown directly conflicts. |
| identity_confidence_score | 0.66 | It is plausible that entry 172 concerns `Jose del Carmen Segundo Pulgar Arriagada`, but identity confidence must stay below promotion level while the official converted transcript conflicts. |
| claim_probability | 0.58 | The staged analysis's central claim that this is a row-level conversion conflict is more likely than not and well supported; the precise father literal and any downstream identity claims remain lower probability. |
| relevance_level | high | If the Pulgar/Arriagada row controls, the entry is highly relevant to Pulgar/Arriagada family reconstruction. |
| relevance_confidence | 0.90 | The chunk and visible image include Pulgar and Arriagada names in entry 172, making relevance clear despite the conversion conflict. |
| canonical_readiness | 0.08 | Not ready for canonical use until targeted conversion QA resolves controlling row and father-field reading, followed by renewed proof review. |

## Evidence Strengths

- The staged analysis accurately identifies the conflict as row-level, not a spelling variation or identity merge problem.
- The held source packet and chunk consistently give a Pulgar/Arriagada reading for entry `172`, including child, parents, birth date/time, place, and informant.
- The source image visibly supports the presence of a Pulgar/Arriagada entry at entry `172`, making the current converted Markdown's Burgos/de la Cruz reading a serious conversion-control concern.
- The staged analysis appropriately avoids using existing wiki pages or Dario-line context as independent proof.

## Limits And Risks

- The current converted Markdown cannot be ignored because it is the canonical derivative file referenced by the chunk metadata and source packet.
- The review cannot certify whether the father field ends with `S.`, another mark, or no suffix.
- Promoting the Pulgar row before conversion QA would create a high duplicate-person and wrong-relationship risk if the derivative conflict is later resolved differently.
- The source supports no same-person claim involving `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.

## Next Action

Keep the staged identity analysis on hold for targeted conversion QA. QA should compare the source image, converted Markdown, chunk, and held source packet; decide which row controls entry `172`; and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, identity, or Dario-line bridge is promoted.
