---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527194902446
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_quality_score: 0.80
conversion_confidence_score: 0.25
evidence_quantity_score: 0.45
agreement_score: 0.20
identity_confidence_score: 0.35
claim_probability: 0.40
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict Revision

## Blockers

- The staged draft remains blocked by a row-level derivative conflict. The assigned chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the current converted Markdown reads entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The referenced source image path, `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, was not present in this workspace during review. I could not visually adjudicate the handwriting or row assignment from the image.
- The conflict is not a spelling variant or ordinary name uncertainty. It is a different child, parents, birth date, place, and informant set for the same entry number.
- No child identity, birth event, parent-child relationship, father-candidate merge, mother-child relationship, or Dario/Darío Pulgar bridge is canonical-ready from this staged draft.

## Evidence Strengths

- The staged draft accurately identifies the conflict between the assigned chunk/source packet and the current converted Markdown.
- The source packet explicitly flags low conversion confidence and recommends `hold_for_conversion_qa`.
- The assigned chunk and source packet agree with each other on the Pulgar/Arriagada reading for entry 172.
- The current converted Markdown provides a coherent but incompatible Burgos/de la Cruz reading, confirming material disagreement among derivative files.
- The staged draft properly avoids treating this entry as literal support for Dario, Darío, Arturo, Smith, or Dario Jose because none of the reviewed derivative text names those identities.

## Scores

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.80 | A civil birth registration is potentially strong direct evidence, but only after the correct row is visually certified. |
| conversion_confidence_score | 0.25 | The derivative texts disagree at the row level, and the source image was unavailable for direct verification. |
| evidence_quantity_score | 0.45 | Staged draft, source packet, chunk, and converted Markdown were available, but they derive from the same source workflow and conflict materially. |
| agreement_score | 0.20 | Chunk/source packet agreement is outweighed by direct contradiction from the converted Markdown for the same entry number. |
| identity_confidence_score | 0.35 | The Pulgar/Arriagada identity hypothesis is plausible within one derivative path only; identity use remains blocked. |
| claim_probability | 0.40 | The hold recommendation is well supported; the substantive row identity or relationship claims remain unresolved. |
| relevance_level | high | If the Pulgar/Arriagada row is verified, it would be directly relevant to Pulgar/Arriagada identity and relationship work. |
| relevance_confidence | 0.85 | Relevance is clear from one derivative path and the source packet, even though proof is blocked. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical promotion. |

## Claim Judgment

The proof-supported claim is limited to the staging decision: this draft identifies a material row-control conflict and should remain on `hold_for_conversion_qa`. The Pulgar/Arriagada reading has support from the assigned chunk and source packet, while the Burgos/de la Cruz reading has support from the current converted Markdown. Because the visible source image was unavailable and the derivative readings conflict, neither row reading should be promoted.

## Next Action

Keep `canonical_readiness: hold_for_conversion_qa`. The next action is targeted conversion QA with access to the actual page image or a valid page-image derivative. QA should decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and should certify the father field only to the extent visible as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before any canonical claim, relationship, identity merge, parent merge, or Dario-line comparison is promoted.
