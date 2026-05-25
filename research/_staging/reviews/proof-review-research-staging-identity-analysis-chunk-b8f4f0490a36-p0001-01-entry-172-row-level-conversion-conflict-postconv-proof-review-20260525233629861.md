---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260525233629861
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211627479.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211627479.md
reviewed_source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
created: 2026-05-25
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged identity analysis correctly identifies a row-level conflict: the assigned converted Markdown records entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, while the assigned chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- Direct source-image review supports the chunk/source-packet row for entry 172 on page 58: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on 1888-03-08 at Calle de Valdivia, registration on 1888-04-07.
- The converted Markdown remains an unresolved derivative-source defect and should not be silently overwritten in this review task.
- The father field still needs targeted QA for the suffix/abbreviation after `Pulgar`; the visible row supports preserving `Jose del Carmen Pulgar S.` or an explicitly uncertain equivalent, not dropping the suffix without review.
- No identity bridge to any Dario/Pulgar candidate is proved by this entry. The surname overlap is relevant as anti-conflation context only.

## Evidence Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth register image is a strong original/near-original source for the event and named relationships. |
| conversion_confidence_score | 0.45 | The chunk aligns with the visible image, but the assigned converted Markdown conflicts sharply and must be reconciled by conversion QA. |
| evidence_quantity_score | 0.55 | One direct register row plus derivative chunk/source packet; enough for a targeted judgment, not enough to bridge broader identities. |
| agreement_score | 0.50 | Source image, chunk, and source packet agree on the Pulgar/Arriagada row; the assigned converted Markdown is wholly discordant. |
| identity_confidence_score | 0.78 | Confidence is high that the visible entry 172 row names the Pulgar/Arriagada child and parents, but father-name normalization remains open. |
| claim_probability | 0.76 | The Pulgar/Arriagada reading is more probable than the converted-file Burgos/de la Cruz reading for this image and entry. |
| relevance_level | high | The row directly concerns a Pulgar child and Arriagada mother. |
| relevance_confidence | 0.92 | Family-name relevance is explicit in the visible row. |
| canonical_readiness | 0.20 | Hold for conversion QA before any canonical claim, relationship, merge, or identity bridge. |

## Evidence Strengths

- The source image visibly places entry `172` on page 58 and shows the child name as `Jose del Carmen Segundo Pulgar Arriagada`.
- The same visible row names the father as `Jose del Carmen Pulgar S.` and the mother as `Juana Arriagada de Pulgar`.
- The registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, birth place `Calle de Valdivia`, father domicile `Calle de Colipí`, mother domicile `Calle de Colipí`, and compareciente `Ernesto Herrera L.` are materially consistent between the image, chunk, and source packet.
- The conflict is not a name variant or identity ambiguity; it is a derivative conversion/file-assignment problem because the converted Markdown's entry 172 family does not match the visible row.

## Source Reliability And Conversion Assessment

The source image is reliable for a civil birth registration row, but the derivative record set is not internally reliable until QA reconciles the converted Markdown and chunk. For proof purposes, the image and chunk support the Pulgar/Arriagada row; the converted Markdown supports only the existence of a conversion conflict and should not be used as contrary identity evidence for this specific image without further QA.

## Identity And Relationship Risk

- Child identity: supported as `Jose del Carmen Segundo Pulgar Arriagada` for the visible entry 172 row, with no support for identifying the child as Dario or as `José Miguel`.
- Father relationship: supported at the row level, but held because the father field includes `S.` and should not be normalized to `Jose del Carmen Pulgar` without a QA note.
- Mother relationship: supported at the row level as `Juana Arriagada de Pulgar`; do not merge or correct this to nearby Juana variants from other records.
- Dario-line relationship jumps: unsupported. Any connection to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío/Dario Pulgar Arriagada` requires separate evidence.

## Canonical Readiness

Canonical readiness is `hold_for_conversion_qa`.

No canonical promotion is ready from this staged draft because the assigned converted Markdown remains contradictory. If targeted conversion QA confirms the image/chunk reading and records the father suffix explicitly, later proof review can treat the birth row as strong evidence for the child identity, birth event, father relationship, and mother relationship. Until then, canonical pages and relationship files should not be updated from this draft.

## Next Action

Run targeted conversion QA on the source image, converted Markdown, chunk, and source packet. The QA note should identify the controlling entry 172 row and preserve the father field as `Jose del Carmen Pulgar S.`, `Jose del Carmen Pulgar [?]`, or another visibly supported reading. After QA, rerun proof review before any canonical promotion or Pulgar/Dario identity comparison.
