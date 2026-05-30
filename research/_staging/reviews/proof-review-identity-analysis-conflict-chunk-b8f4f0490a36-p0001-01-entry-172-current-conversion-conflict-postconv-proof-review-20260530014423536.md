---
type: proof_review
role: claim_reviewer
status: complete
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md"
worker: "postconv-proof-review-20260530014423536"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-evidence-extraction-20260526095657171.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image_attempted: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_image_status: "unavailable_at_referenced_path"
canonical_readiness: "hold_for_conversion_qa"
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers

- The referenced converted Markdown and referenced chunk materially disagree for register page 58, entry 172. The converted file reads a Burgos/de la Cruz birth row; the chunk reads a Pulgar/Arriagada birth row.
- The exact referenced source image path was unavailable during this review, so I did not independently certify the page image reading.
- The source packet reports prior image review favoring the Pulgar/Arriagada row, but that remains derivative review evidence for this task, not a direct visual certification by this reviewer.
- The father field is not fully settled. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet only certifies `Jose del Carmen Pulgar` and leaves the trailing mark unresolved.
- No Dario identity is named in the staged draft, converted file, chunk, source packet, or conflict draft reviewed here. Any Dario-line attachment would be a relationship jump.

## Evidence Strengths

- The staged identity analysis accurately identifies the central row-level derivative conflict and treats it as a hold rather than a promotable identity conclusion.
- The source packet and conflict draft agree that the chunk-supported reading is `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. on Calle de Valdivia, with father `Jose del Carmen Pulgar`/`Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The converted Markdown explicitly supports the competing row: `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The staged draft keeps the Burgos/de la Cruz people, Pulgar/Arriagada people, Jose/Juana parent candidates, and Dario identities separated rather than merging by surname or proximity.

## Scored Judgment

| factor | score / value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | A civil birth register is strong direct evidence when the row is correctly controlled. Usability is reduced here because the image was unavailable at the referenced path for this review. |
| conversion_confidence_score | 0.22 | The two derivative transcripts disagree on nearly every identity and event field for entry 172. |
| evidence_quantity_score | 0.46 | There is one source packet, one conflict draft, one chunk, and one converted file, but no independently available source image in this review pass. |
| agreement_score | 0.28 | The chunk, source packet, and conflict draft align with each other, but the referenced converted Markdown directly contradicts them. |
| identity_confidence_score | 0.58 | The Pulgar/Arriagada row is better supported by the staged packet/chunk evidence than the Burgos row for family relevance, but not enough for canonical identity work without row-control QA. |
| claim_probability | 0.60 | Probable that the staged draft's hold-for-QA assessment is correct; not probable enough to promote the Pulgar/Arriagada child or parent relationships. |
| relevance_level | high | Entry 172 directly concerns Pulgar/Arriagada family-relevant evidence and a material conversion conflict. |
| relevance_confidence | 0.92 | The reviewed artifacts all point to the same entry-172 dispute. |
| canonical_readiness | hold_for_conversion_qa | Do not promote, merge, or attach to canonical people/families until row-control QA resolves the derivative conflict and father-field ending. |

## Claim-Level Disposition

| claim or hypothesis | probability | disposition |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.60 | Hold for targeted conversion QA; plausible but not canonically ready. |
| Entry 172 is the Burgos/de la Cruz row in the current converted Markdown. | 0.12 | Hold as the competing derivative reading; do not promote from this conflict. |
| `Jose del Carmen Pulgar`/`Juana Arriagada de Pulgar` are the parents of the child in entry 172. | 0.55 | Hold pending row-control QA and father-field certification. |
| The father field includes a meaningful suffix `S.`. | 0.35 | Hold; preserve as unresolved literal uncertainty. |
| Entry 172 supports any Dario identity or Dario-line bridge. | 0.01 | Reject for this draft; use only as anti-conflation context. |

## Next Action

Keep the staged draft at `hold_for_conversion_qa`. The next action is targeted row-control QA against the original page image and the current derivative artifacts, explicitly deciding whether register page 58, entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row and certifying the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

No canonical pages, claim files, relationship files, or source transcriptions should be edited from this review.
