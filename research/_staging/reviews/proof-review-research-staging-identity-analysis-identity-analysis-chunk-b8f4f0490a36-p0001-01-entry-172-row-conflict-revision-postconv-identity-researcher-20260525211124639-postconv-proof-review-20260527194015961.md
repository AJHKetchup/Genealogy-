---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527194015961
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
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

- The staged draft remains blocked by a row-level derivative conflict. The assigned chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the current converted Markdown identifies entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The referenced raw source image path, `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, was not present in this workspace during review. The manifest's derived page image path under `raw/codex-conversion-jobs/.../page-images/page-0001.png` was also unavailable. I therefore could not visually adjudicate the row from the image.
- The staged draft cites existing wiki context, but this proof review did not use canonical pages for scoring because the task scope permits only the staged draft and directly referenced verification sources. The wiki references should be treated as contextual risk notes, not independent support in this review.
- No child identity, birth event, parent relationship, father merge, mother-child relationship, or Dario-line bridge is canonical-ready from this staged draft.

## Evidence Strengths

- The staged draft accurately reports the conflict between the assigned chunk/source packet and the current converted Markdown.
- The source packet explicitly flags low conversion confidence, identifies the same row-control problem, and recommends `hold_for_conversion_qa`.
- The chunk and source packet agree with each other on the Pulgar/Arriagada reading for entry 172.
- The current converted Markdown gives a coherent but incompatible Burgos/de la Cruz reading for entry 172, confirming this is a row-control or conversion-assignment conflict rather than a minor name variant.
- The staged draft correctly avoids using this entry as literal support for any Dario/Darío Pulgar identity because no reviewed derivative text names Dario, Darío, Arturo, Smith, or Dario Jose.

## Scores

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.80 | Civil birth registration would be strong direct evidence if the correct row were visually certified. |
| conversion_confidence_score | 0.25 | Two derivative readings conflict at the row level, and the referenced image was unavailable for direct check. |
| evidence_quantity_score | 0.45 | Multiple derivative files were available, but they are not independent of the same conversion workflow and disagree materially. |
| agreement_score | 0.20 | Chunk/source packet agree with each other, but they conflict with the current converted Markdown. |
| identity_confidence_score | 0.35 | The Pulgar/Arriagada identity hypothesis is plausible only within one derivative reading; identity use is blocked until row QA. |
| claim_probability | 0.40 | The staged draft's hold conclusion is well supported; any substantive identity or relationship claim from the row remains uncertain. |
| relevance_level | high | If verified, the row would be directly relevant to Pulgar/Arriagada identity and relationship work. |
| relevance_confidence | 0.85 | Relevance is clear from matched Pulgar/Arriagada terms in one derivative path, even though proof is blocked. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical promotion. |

## Claim Judgment

The proof-reviewed claim is not that either row reading is correct. The defensible claim is narrower: this staged draft identifies a material row-control conflict and should remain on hold pending targeted conversion QA. That claim is supported by the staged draft, conflict candidate, source packet, chunk, and converted Markdown.

The Pulgar/Arriagada reading has derivative support from the chunk and source packet, but the current converted Markdown directly contradicts it. The Burgos/de la Cruz reading has derivative support from the current converted Markdown, but is contradicted by the assigned chunk and source packet. With the page image unavailable, neither substantive row reading should be promoted.

## Next Action

Keep `canonical_readiness: hold_for_conversion_qa`. The next required action is targeted conversion QA with access to the actual page image or a valid page-image derivative. QA must decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and should certify the father field only to the extent visible.

After that, rerun proof review before promoting any claims or relationships from this entry.
