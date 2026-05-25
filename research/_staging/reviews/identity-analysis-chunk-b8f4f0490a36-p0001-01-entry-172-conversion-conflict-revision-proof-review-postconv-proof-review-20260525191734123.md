---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525191734123
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
reviewed_context:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`.
- The staged identity analysis correctly treats the item as a material row-level conversion/file-assignment conflict and correctly blocks canonical promotion.
- The staged identity analysis misquotes the currently referenced converted Markdown. The staged analysis says the converted file records `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`; the referenced converted file currently records entry 172 as `José Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- The mismatch above does not remove the blocker. It reinforces that the converted-file layer is unstable or assigned to a different page/row than the chunk and source packet.
- Do not promote any child identity, birth event, parent-child relationship, Jose/Juana identity merge, father-name suffix, or Dario-line relationship from this draft until targeted conversion QA reconciles the source image, converted Markdown, and chunk.

## Evidence Strengths

- The page image visibly supports entry 172 on page 58 as a Pulgar/Arriagada birth registration, not the current converted-file reading.
- The chunk and staged source packet agree on the core Pulgar/Arriagada reading: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at Calle de Valdivia, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`.
- The staged identity analysis appropriately rejects same-person treatment between the Pulgar/Arriagada row and the conflicting converted-file row because child name, parents, date/place details, and informant differ materially.
- The staged identity analysis appropriately rejects Dario-line linkage from this record. The reviewed evidence does not name Dario, Arturo, Smith, Dario Jose, or any later professional/property/passenger context.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is a strong primary source, and the page image is available. |
| conversion_confidence_score | 0.42 | The source image and chunk align on the Pulgar/Arriagada row, but the referenced converted Markdown is materially different and the staged analysis misstates that converted-file text. |
| evidence_quantity_score | 0.62 | One direct civil record supports the birth-row facts if QA confirms the row; no independent corroborating source is included. |
| agreement_score | 0.46 | Chunk, source packet, and image agree broadly; converted Markdown and parts of the staged conflict wording disagree. |
| identity_confidence_score | 0.72 | Strong enough for a provisional Pulgar/Arriagada row identity, but not enough for canonical identity work while the conversion/file-assignment conflict remains unresolved. |
| claim_probability | 0.78 | The probability that entry 172 in the visible source is the Pulgar/Arriagada birth row is fairly high, but canonical use remains blocked by derivative inconsistency. |
| relevance_level | high | If confirmed, the record is directly relevant to Pulgar/Arriagada parent-candidate work. |
| relevance_confidence | 0.86 | The surnames and parent-child structure are plainly relevant, subject to conversion QA. |
| canonical_readiness | hold_for_conversion_qa | The review cannot approve canonical promotion until the conversion conflict and father-name suffix are certified. |

## Claim Judgment

The staged draft's central judgment is supported: this is a critical conversion/file-assignment conflict, not a name variant or duplicate-person problem. The source image and chunk favor the Pulgar/Arriagada row, but the current converted Markdown is inconsistent with that row and the staged identity analysis repeats an outdated or incorrect description of the converted-file reading.

The father field should remain unresolved as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until source-image QA certifies the literal reading. The visible image appears compatible with the chunk's `Jose del Carmen Pulgar S.` reading, but this proof review should not rewrite the transcription.

## Next Action

Run targeted conversion QA on the source image, converted Markdown, chunk, and source packet. The QA note should decide whether the converted Markdown is from a different page/conversion state or should be superseded, and it should explicitly certify the father field. After QA, rerun proof review before any canonical claim, relationship, parent merge, or Dario-line comparison is promoted.
