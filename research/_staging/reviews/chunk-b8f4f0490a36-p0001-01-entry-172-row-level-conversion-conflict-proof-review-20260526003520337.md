---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526003520337
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525234847240.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525234847240.md"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness is `hold`. The staged draft is materially supported as a conflict analysis, but no child identity, birth fact, parent-child relationship, parent merge, or Pulgar-to-Dario comparison should be promoted from this item until conversion QA resolves the row-control conflict.
- The referenced converted Markdown identifies entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. The referenced chunk, source packet, and page image identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar...` and `Juana Arriagada de Pulgar`, born 8 March 1888.
- The father field in the Pulgar/Arriagada row is not fully certified for the trailing suffix. The image and packet support a reading beginning `Jose del Carmen Pulgar`; whether the final mark is `S.`, another suffix, or uncertainty needs targeted conversion QA.
- The requested `genealogy-proof-review` skill is not installed in this session. This review follows the controller's explicit proof-review instructions and the local evidence only.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525234847240.md`.
- Conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

No external research was performed. No raw source, converted Markdown, chunk, source packet, or canonical page was edited.

## Scored Judgment

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth-register page image is a direct source for the registration row; image legibility is adequate for row identity, though the father suffix remains uncertain. |
| conversion_confidence_score | 0.42 | The assigned chunk matches the visible row and source packet, but the main converted Markdown is a materially different transcription for the same entry number. |
| evidence_quantity_score | 0.72 | Evidence includes staged analysis, conflict draft, source packet, chunk, converted Markdown, and page image; there is still only one source event for the identity claim. |
| agreement_score | 0.38 | Chunk, source packet, and image agree on the Pulgar/Arriagada row, but the converted Markdown directly conflicts on every identity-bearing field. |
| identity_confidence_score | 0.70 | The visible entry-172 row supports the Pulgar/Arriagada child identity as a candidate, but conversion-control conflict and father suffix uncertainty prevent promotion. |
| claim_probability | 0.78 | The staged draft's main claim, that this is a row-level conversion conflict and should be held, is strongly supported. The underlying Pulgar/Arriagada birth claim is probable but not canonically ready. |
| relevance_level | high | The row directly concerns Pulgar/Arriagada family names and parent-child assertions. |
| relevance_confidence | 0.95 | The page image and chunk show the Pulgar/Arriagada names in entry 172, making the evidence directly relevant. |
| canonical_readiness | hold | Targeted conversion QA must resolve the controlling transcription before canonical promotion. |

## Evidence Strengths

- The source packet and assigned chunk preserve a coherent entry-172 transcription for `Jose del Carmen Segundo Pulgar Arriagada`, with birth date, place, parents, and informant aligned to the same row.
- The page image visually confirms that entry 172 on page 58 is the Pulgar/Arriagada row, not the Burgos/de la Cruz row currently represented in the converted Markdown.
- The staged identity analysis correctly treats the issue as a row-control or conversion-control conflict rather than as a normal name variant or same-person merge question.
- The staged analysis correctly keeps Dario/Pulgar identity-bridge hypotheses separate from the literal source transcription. This entry does not itself support a merge to any Dario identity.

## Claim Probability And Identity Risk

The probability that the staged draft correctly identifies a serious conversion conflict is `0.90`. The probability that entry 172 should ultimately support a Pulgar/Arriagada birth-registration candidate is `0.78`, pending conversion QA. The probability that the Burgos/de la Cruz converted-Markdown reading is the controlling row for this page image is `0.08` based on the visible row alignment.

Identity risk is high if promoted prematurely. The conflicting readings name different children, different parents, different birth dates, different birth places, and different informants. Treating them as variants or duplicates would create unsupported parent-child relationships and likely contaminate Pulgar, Arriagada, Burgos, and de la Cruz clusters.

## Next Action

Keep this item on `hold_for_conversion_qa`.

Targeted conversion QA should compare the page image against the converted Markdown and decide the controlling entry-172 transcription. It should also certify the father-field ending as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that QA note exists, run a fresh proof review before promoting any child identity, birth fact, parent-child relationship, parent identity merge, or Dario/Pulgar comparison.
