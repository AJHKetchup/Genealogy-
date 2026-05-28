---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528201342398
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173704312.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173704312.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528170150642.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528170150642.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote the current converted Markdown's `Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz` reading as entry `172` for this physical row. It conflicts with the assigned chunk, source packet, targeted row-control QA, and visible page image for page 58.
2. Do not promote `Jose del Carmen Pulgar S.` as a certified father name. The reviewed evidence supports only the bounded father reading `Jose del Carmen Pulgar`; the trailing mark or suffix remains unresolved.
3. Do not attach this row to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. The visible row does not name Dario, Arturo, Smith, a spouse, later-life facts, or any bridge identifier.
4. Do not merge or normalize `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` from this item alone. This row supports the former reading only and does not resolve the separate Juana variant question.
5. Relationship promotion should stay scoped. The row supports stated parent candidates for this birth registration, but it does not by itself prove that every same-named canonical stub is the same person.

## Evidence Strengths

- The source is a civil birth register page, a strong source type for a narrow birth-registration and parentage claim.
- The assigned chunk places entry `172` on page 58 and transcribes the child as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
- The source packet and targeted conversion review both state that direct image row-control supports the Pulgar/Arriagada row, not the Burgos/de la Cruz derivative conversion.
- Visual inspection of the referenced page image is consistent with entry `172` being the middle row on page 58 and with the Pulgar/Arriagada names in that row.
- The mother field is consistently represented in the chunk, source packet, and QA note as `Juana Arriagada de Pulgar`.
- The staged identity analysis correctly treats Dario-line links as anti-conflation checks rather than promoted conclusions.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8.5/10 |
| conversion_confidence_score | 8/10 for the row-control conclusion; 6.5/10 for the bounded father-name field because of the unresolved terminal mark; 2/10 for the conflicting converted Markdown entry-172 text |
| evidence_quantity_score | 6/10 |
| agreement_score | 8/10 among source image, assigned chunk, source packet, and QA note for the Pulgar/Arriagada row; 1/10 between those sources and the older converted Markdown |
| identity_confidence_score | 8.5/10 for the narrow claim that physical row `172` names `Jose del Carmen Segundo Pulgar Arriagada`; 6/10 for attaching the recorded parent names as row-level parent candidates; 0.5/10 for any Dario-line same-person bridge |
| claim_probability | 0.90 that physical row `172` is the Pulgar/Arriagada birth registration; 0.88 that the child is recorded as `Jose del Carmen Segundo Pulgar Arriagada`; 0.82 that the mother is recorded as `Juana Arriagada de Pulgar`; 0.70 that the father field should be promoted only as `Jose del Carmen Pulgar`; 0.02 or lower for Dario-line attachment |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold for canonical promotion until the row-control conflict is accepted by the downstream claim workflow; ready only as reviewed staging evidence for narrow row-level claims |

## Review Finding

The staged identity analysis is well supported as a conflict-control and anti-conflation review. The best-supported conclusion is that the physical entry `172` on page 58 is the Pulgar/Arriagada birth registration, while the Burgos/de la Cruz text in the current converted Markdown is a derivative conversion conflict.

The review should not be used to rewrite the source transcription directly. It should be used to hold or revise downstream claims so that any future promotion relies on the image-controlled row reading and preserves the older converted Markdown conflict as a warning.

## Next Action

Accept the staged draft as proof-reviewed for narrow row-level use, with canonical readiness set to `hold`. A downstream claim worker may stage narrow claims for the child name, sex, birth date/time/place, registration date, recorded father, recorded mother, and informant details after accepting the targeted row-control QA. Keep the father suffix, Juana variant merge, same-named parent-stub identity merges, and all Dario-line bridges on hold pending separate proof review.
