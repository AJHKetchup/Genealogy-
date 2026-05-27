---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260527144844135
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525205449265.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525205449265.md"
reviewed_context:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.84
conversion_confidence_score: 0.38
evidence_quantity_score: 0.63
agreement_score: 0.34
identity_confidence_score: 0.56
claim_probability: 0.56
relevance_level: high
relevance_confidence: 0.88
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict

Review of staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525205449265.md`.

## Blockers First

1. The staged draft correctly identifies a row-level derivative conflict: the assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth row, while the assigned converted Markdown reads entry 172 as a Burgos/de la Cruz row.
2. The conflict is identity-bearing across child name, parents, birth date, birth place, declarant, and residence. This is not a normal spelling or name-order variant.
3. The source image visible in this review broadly supports the chunk/source-packet Pulgar/Arriagada row for entry 172 and does not visibly support the converted Markdown's `Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz` reading for that row. However, this review should not rewrite the conversion; the converted Markdown remains a contradictory referenced derivative.
4. The father field is not certified at proof-review level. The visible row appears consistent with `Jose del Carmen Pulgar` followed by an additional mark or suffix, but whether the field should be read as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` still requires targeted conversion QA.
5. No canonical identity, relationship, merge, or Dario-line inference should be promoted from this staged draft until conversion QA reconciles the source image, converted Markdown, chunk, and source packet.

## Evidence Strengths

- The source type is strong: a civil birth registration page is direct evidence for a birth event and declared parent names when the row is correctly identified.
- The assigned chunk, source packet, conflict note, and visible source image are mutually consistent at a high level for a Pulgar/Arriagada entry 172 on register page 58.
- The chunk gives a full row-level context: registration date, child name and sex, birth date/time/place, father, mother, informant, residences, and official signature.
- The staged identity analysis appropriately treats Dario-related names only as anti-conflation context. This exact entry does not name Dario and does not support a Dario-line bridge.

## Scored Judgment

| Review dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.84 | Civil birth registration is a high-quality source for the row's birth and parent statements, assuming the row is correctly transcribed. |
| conversion_confidence_score | 0.38 | The controlling derivative set is internally inconsistent; the image and chunk favor Pulgar/Arriagada, but the converted Markdown gives an incompatible row. |
| evidence_quantity_score | 0.63 | There is one source image plus several derivative notes, but they are not independent sources and cannot resolve the father-field suffix alone. |
| agreement_score | 0.34 | Chunk/source packet/conflict draft/image broadly agree, but the assigned converted Markdown directly disagrees in all identity-bearing fields. |
| identity_confidence_score | 0.56 | Pulgar/Arriagada is the better-supported reading for the visible row, but identity confidence remains limited by derivative conflict and uncertified father reading. |
| claim_probability | 0.56 | Probability that entry 172 supports `Jose del Carmen Segundo Pulgar Arriagada` as child of `Jose del Carmen Pulgar ...` and `Juana Arriagada de Pulgar`, held below promotion threshold pending QA. |
| relevance_level | high | If confirmed, this is direct Pulgar/Arriagada birth and parent evidence. |
| relevance_confidence | 0.88 | The names in the chunk/source packet are family-relevant; the uncertainty concerns transcription control, not relevance. |
| canonical_readiness | blocked | Do not promote until conversion QA certifies the controlling row and father-field reading. |

## Claim Probability Detail

- Pulgar/Arriagada row controls entry 172: 0.64. The visible page and assigned chunk/source packet support this more strongly than the converted Markdown.
- Burgos/de la Cruz row controls entry 172: 0.12. This is supported only by the assigned converted Markdown and is contradicted by the chunk and visible image.
- Derivative assignment or conversion-state mismatch explains the conflict: 0.74. The same source/converted/chunk metadata points to incompatible row content, making a workflow or derivative-state problem likely.
- Father should be normalized simply to `Jose del Carmen Pulgar`: 0.45. The base name is supported, but the following mark/suffix is unresolved.
- Entry 172 supports a Dario-line identity bridge: 0.02. No Dario name or relationship appears in the reviewed row.

## Literal Support Check

Supported by chunk/source packet and broadly visible on the source image:

- Entry number `172`.
- Registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child reading as `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth date/time/place reading as `Ocho de Marzo de mil ochocientos ochenta i ocho`, `a las tres de la tarde`, `Calle de Valdivia`.
- Mother reading as `Juana Arriagada de Pulgar`.
- Informant reading as `Ernesto Herrera L.`, present at the birth, with residence at `Calle de Valdivia`.

Contradicted by chunk/source packet and visible image for entry 172:

- Converted Markdown reading of child `Jose Miguel`.
- Converted Markdown father `Oswaldo Burgos`.
- Converted Markdown mother `Concepcion de la Cruz`.
- Converted Markdown birth date/time/place `El seis de Abril... a las diez de la noche`, `En esta`.

Unresolved:

- Exact father-field form after `Jose del Carmen Pulgar`: possible `S.`, an uncertain suffix/mark, or no reliable suffix. This must remain literal/uncertain until image QA certifies the reading.

## Next Action

Hold for targeted conversion QA. The QA note should compare the source image against the assigned converted Markdown and assigned chunk, then certify:

1. Which row is the controlling entry 172 transcription.
2. Whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. Whether the converted Markdown should be regenerated or otherwise marked as superseded for this source.

After QA, rerun proof review before promoting any claim, relationship, person identity, parent pair, or wiki-page update. Do not attach this entry to any Dario candidate without a separate proof-reviewed bridge source.
