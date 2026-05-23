---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-23b2269a97df-p0001-01-identity-candidates.md
worker: postconv-proof-review-20260523120609953
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-23b2269a97df-p0001-01-identity-candidates.md
reviewed_source_packet: research/_staging/source-packets/chunk-23b2269a97df-p0001-01-entry-172-pulgar-arriagada.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md
review_status: hold
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Identity Candidates

## Blockers

- The staged draft depends on a Pulgar/Arriagada identity reading for entry 172, but the current converted Markdown and current chunk transcribe entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`. That is a material identity conflict, not a minor spelling issue.
- The source packet explicitly marks `conversion_confidence: mixed` and `promotion_recommendation: hold_for_conversion_qa`, so none of the identity hypotheses should be promoted or merged canonically from this draft.
- The current chunk file front matter identifies itself as `CHUNK-25813b5a53d9-P0001-01`, while the staged draft/source packet refer to `CHUNK-23b2269a97df-P0001-01`. That metadata drift increases the assignment/reconciliation risk.
- The visible source image supports the Pulgar/Arriagada row, but this review should not rewrite the converted text or chunk. It should trigger conversion QA to reconcile which transcript is controlling.
- The entry does not name Dario. Any attachment to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Darío/Dario Pulgar Arriagada would be an unsupported identity jump.
- Father and informant exact readings still need targeted QA. The source packet gives father as `Jose del Carmen Pulgar`; related staging has preserved a possible suffix and variant informant readings.

## Evidence Strengths

- The referenced source image was available and visibly shows entry 172 on page 58 as a Pulgar/Arriagada birth-registration row: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. on Calle de Valdivia, with father appearing as `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- The source packet matches the visible-image direction and preserves the needed uncertainty instead of treating the derivative transcript as settled.
- The staged draft correctly treats the Pulgar/Arriagada reading as blocked by conversion QA rather than canonically ready.
- The Dario-line comparison is appropriately negative: the evidence is relevant as an anti-conflation guardrail, not as support for a Dario identity.

## Scored Judgment

| measure | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth-register image is a strong original-source class and the referenced image is present, but the page is a photographed spread with handwriting and some fields require close reread. |
| conversion_confidence_score | 0.22 | The current converted Markdown/chunk conflict with the visible Pulgar/Arriagada row and with the staged source packet; the chunk id metadata also differs from the staged id. |
| evidence_quantity_score | 0.58 | There is one direct register entry plus a source packet and prior staging context; there is not yet an independent corroborating record for identity merges. |
| agreement_score | 0.38 | Source image and source packet agree directionally, but the assigned derivative artifacts disagree on the core child and parents. |
| identity_confidence_score | 0.78 | Probable that the visible entry-172 row is the Pulgar/Arriagada child-parent cluster, reduced by unresolved conversion/chunk conflict and exact-name uncertainty. |
| claim_probability | 0.76 | The main staged identity claim is more likely than not on the visible image, but not ready for canonical use until QA records the controlling transcript. |
| relevance_level | direct | The row directly controls the child identity and parent candidates in this staged draft. |
| relevance_confidence | 0.96 | The staged draft, source packet, and image all refer to entry 172/page 58; the only serious relevance issue is derivative artifact mismatch. |
| canonical_readiness | 0.10 | Hold for conversion QA; do not promote, merge, or attach to canonical people. |

## Identity And Relationship Risk

- Duplicate-person risk is high if the current derivative `Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz` transcription is promoted from this draft without reconciliation.
- Duplicate-person risk is moderate if `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar` are merged with other Jose/Juana candidates by name similarity alone.
- Relationship risk is high because child-father, child-mother, and parental-pair conclusions all depend on the same conflicted transcript.
- Dario identity risk is low if this draft remains a negative guardrail; it becomes high only if surname overlap is used to bridge to Dario profiles.

## Next Action

Keep this staged draft on hold with `canonical_readiness: not_ready`.

Run targeted conversion QA for the referenced source image, converted Markdown, and chunk. The QA note should settle whether entry 172's controlling transcript is the visible Pulgar/Arriagada row, explain the chunk-id/converted-sha drift, and record the exact father and informant readings. After that, rerun proof review for the identity candidates and dependent claim/relationship drafts before any canonical promotion.
