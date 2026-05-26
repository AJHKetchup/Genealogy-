---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526220053964
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173959405.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173959405.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_page: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-26
source_quality_score: 0.82
conversion_confidence_score: 0.35
evidence_quantity_score: 0.62
agreement_score: 0.42
identity_confidence_score: 0.64
claim_probability: 0.66
relevance_level: high
relevance_confidence: 0.95
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged draft is supported as a hold, not as a promotable claim. The assigned chunk and source packet identify entry `172` as a Pulgar/Arriagada birth registration, but the referenced current converted Markdown identifies entry `172` as a different Burgos/de la Cruz registration.
2. The conflict is row-level and material. It changes the child, birth date and time, birth place, father, mother, informant, and relationship candidates.
3. The father field in the Pulgar/Arriagada row is not proof-ready. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet correctly preserves uncertainty over whether the trailing character is an `S.` or another mark.
4. No canonical identity, parent-child relationship, merge, duplicate-person decision, or Dario-line bridge should be promoted from this staged draft until targeted conversion QA certifies the controlling row and father-field reading.

## Evidence Strengths

- The assigned chunk gives a coherent entry `172` row for `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 about 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged source packet reports direct image review and preserves the same Pulgar/Arriagada reading while explicitly marking conversion confidence low.
- The page image visually supports that entry `172` is the second row on page 58 and is consistent with the Pulgar/Arriagada row layout and names. The visible source is not used here to over-certify the unresolved father suffix.
- The current converted Markdown independently demonstrates the conversion conflict because its entry `172` is a complete alternate Burgos/de la Cruz row: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth 6 April 1888 at 10 p.m. in `En esta`, informant `Oswaldo Burgos`.

## Scored Judgment

| Category | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a high-quality source type for a birth and parent claim, but the review is limited by conversion disagreement and father-field uncertainty. |
| conversion_confidence_score | 0.35 | Low for canonical use because chunk/source packet and current converted Markdown disagree on the row assigned to entry `172`. |
| evidence_quantity_score | 0.62 | Several local artifacts were checked: staged draft, source packet, chunk, converted Markdown, conflict draft, and page image. They are not independent genealogical corroboration. |
| agreement_score | 0.42 | Chunk, source packet, conflict note, and image review align toward Pulgar/Arriagada; current converted Markdown materially disagrees. |
| identity_confidence_score | 0.64 | Pulgar/Arriagada is the stronger hypothesis for this staged review, but proof confidence remains below promotion level due to the conversion conflict. |
| claim_probability | 0.66 | Probable that entry `172` is the Pulgar/Arriagada row if targeted QA confirms row control. Not sufficient for canonical attachment now. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent candidates, and to preventing false Dario/Pulgar cluster merges. |
| relevance_confidence | 0.95 | The reviewed materials explicitly concern this entry and this conflict. |
| canonical_readiness | hold_for_conversion_qa | Hold all dependent claims and relationships pending targeted conversion QA. |

## Identity And Relationship Risk

- Same-person risk is high if `Jose del Carmen Segundo Pulgar Arriagada` is treated as interchangeable with `Jose Miguel`; the rows describe different children and parent sets.
- Parent-child relationship risk is high because one reading names `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`, while the other names `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Duplicate or merge risk is high for any premature merge of `Jose del Carmen Pulgar S.` with an existing `Jose del Carmen Pulgar` candidate, and for any Juana Arriagada candidate merge based only on this conflicted entry.
- Dario-line relevance is contextual only. This source does not visibly support a Dario, Arturo, Smith, grandchild, spouse, or other direct bridge.

## Next Action

Run targeted conversion QA against the source image, assigned chunk, current converted Markdown, staged source packet, and staged conflict draft. The QA note should decide which row controls entry `172` and certify the father field only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that QA exists, rerun proof review before promoting any identity claim, birth event, parent-child relationship, merge, or canonical wiki update.
