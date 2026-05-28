---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528004119205
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525205832459.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525205832459.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote any child identity, birth fact, parent fact, parent-child relationship, or same-person merge from the staged draft. The converted Markdown and chunk remain in direct row-level conflict for entry 172.
2. The visible source image supports the Pulgar/Arriagada row for entry 172, while the assigned converted Markdown records a Burgos/de la Cruz row. This is a conversion or file-assignment defect, not an identity variant.
3. The father field is still not fully safe for canonical normalization. The visible row supports `Jose del Carmen Pulgar` and appears consistent with the staged `Jose del Carmen Pulgar S.` reading, but the final suffix/mark after `Pulgar` should remain a targeted QA question.
4. The staged draft correctly blocks Dario-line attachment. The reviewed source row does not name Dario, Arturo, Smith, Pulgar-Smith, a spouse, a child of any Dario candidate, or a later-life identity bridge.

## Evidence Strengths

- The source is a civil birth register, which is a strong source type for a birth event and stated parents when the row is correctly assigned.
- The page image, chunk, source packet, and conflict draft agree that entry 172 on page 58 is a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar...` and mother `Juana Arriagada de Pulgar`.
- The staged identity analysis accurately treats the Burgos/de la Cruz converted Markdown as a row-level conflict and keeps canonical readiness at `hold_for_conversion_qa`.
- The staged analysis preserves uncertainty instead of silently correcting the converted Markdown or promoting a normalized father name.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 3/10 overall because assigned derivatives conflict; 7/10 for the chunk/source-packet reading against the visible image |
| evidence_quantity_score | 4/10 |
| agreement_score | 5/10 overall; high agreement among image, chunk, source packet, and conflict draft, but direct disagreement with the assigned converted Markdown |
| identity_confidence_score | 6/10 for the narrow Pulgar/Arriagada entry-172 row; 4/10 for attaching the father to an existing `Jose del Carmen Pulgar` person; 5/10 for the literal mother name; 0.5/10 for any Dario-line identity bridge |
| claim_probability | 0.82 that the visible source row for entry 172 is Pulgar/Arriagada; 0.30 that the converted Markdown's Burgos/de la Cruz row controls this source image; 0.50 that `Jose del Carmen Pulgar S.` is the exact father reading; 0.05 for a Dario attachment |
| relevance_level | high for Pulgar/Arriagada birth and parent research; low for Dario identity bridging |
| relevance_confidence | 0.88 for Pulgar/Arriagada relevance; 0.95 that Dario relevance is only anti-conflation context |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold note. Its central judgment is sound: this is a row-level conversion conflict with identity-bearing consequences. Visual review of the referenced source image favors the chunk/source-packet Pulgar/Arriagada row for entry 172, but proof review should not repair the converted Markdown or promote the claim while the derivative record set remains contradictory.

The safest claim-level status is `hold_for_conversion_qa`, not canonical promotion. If later QA certifies the Pulgar/Arriagada row, the child name, birth date, registration date, mother name, and parent-child relationships can be reviewed as direct civil-registration evidence. The father field still needs a focused reread for the suffix after `Pulgar`.

## Next Action

Run targeted conversion QA against the source image, converted Markdown, chunk, source packet, and conflict draft. The QA result should certify whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, then explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical claim, relationship, merge, or Dario-line comparison is promoted.
