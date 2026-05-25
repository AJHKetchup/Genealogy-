---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260525204205372
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
reviewed_date: 2026-05-25
canonical_readiness: hold
source_quality_score: 0.82
conversion_confidence_score: 0.38
evidence_quantity_score: 0.55
agreement_score: 0.42
identity_confidence_score: 0.60
claim_probability: 0.68
relevance_level: high
relevance_confidence: 0.86
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers

- Canonical readiness is `hold`. The assigned staged identity analysis must not be promoted while the derivative files disagree about entry 172.
- The source image and assigned chunk support entry 172 as a Pulgar/Arriagada birth registration, but the assigned converted Markdown currently reads entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. That converted-file reading is not the Gomez/de la Cruz de la Maza row described in the staged identity analysis, so the staged analysis contains a stale or incorrect description of one conflict layer.
- The current converted Markdown is not literally supported by the visible page image for entry 172. It appears to represent a different page or a failed conversion, not a defensible variant reading of the same row.
- The father field in the visible Pulgar/Arriagada row is still a transcription-risk point. The visible image supports `Jose del Carmen Pulgar` plus a trailing mark or abbreviation; the exact final reading should remain unresolved as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies it.
- No same-person, duplicate-person, parent-child promotion, Dario-line bridge, or Jose/Juana candidate merge is supported from this staged draft alone.

## Evidence Strengths

- The source image, chunk, source packet, and conflict draft agree that the visible entry 172 on page 58 is family-relevant and names `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888.
- The visible image and chunk support a birth date of 8 March 1888 at about 3 p.m. and a birth place of `Calle de Valdivia`.
- The visible image and chunk support mother `Juana Arriagada de Pulgar`.
- The visible image and chunk support informant `Ernesto Herrera L.`, age 26, employee, resident at `Calle de Valdivia`.
- The staged identity analysis correctly treats the conflict as a row-level or file-assignment conversion problem, not a spelling variant or identity-merge problem.

## Scores

| Review dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a strong primary source, but image contrast and handwriting leave some field-level risk. |
| conversion_confidence_score | 0.38 | The chunk aligns with the visible source image, but the assigned converted Markdown reads a different entry/person set. |
| evidence_quantity_score | 0.55 | One primary source page plus derivative chunk/source packet; enough to identify the conflict, not enough for broader identity bridging. |
| agreement_score | 0.42 | Source image, chunk, source packet, and conflict note mostly agree, but the converted Markdown and staged analysis description of that converted file do not. |
| identity_confidence_score | 0.60 | The visible entry likely concerns `Jose del Carmen Segundo Pulgar Arriagada`; father suffix and derivative conflict prevent stronger identity confidence. |
| claim_probability | 0.68 | Probable that the controlling visible row is Pulgar/Arriagada, but promotion should wait for conversion QA. |
| relevance_level | high | Pulgar and Arriagada family terms are directly present in the visible row. |
| relevance_confidence | 0.86 | Family relevance is clear if the Pulgar/Arriagada row is certified as the controlling entry. |
| canonical_readiness | hold | Requires targeted conversion QA and rerun proof review before canonical use. |

## Claim Judgments

| Claim or hypothesis | Judgment | Claim probability | Identity risk | Canonical readiness |
| --- | --- | ---: | --- | --- |
| Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | Hold as probable, pending conversion QA. | 0.68 | Medium | hold |
| Entry 172 is the Burgos/de la Cruz registration in the current converted Markdown. | Revise/reject for this page image. | 0.08 | High | not_ready |
| Entry 172 is the Gomez/de la Cruz de la Maza registration described by the staged identity analysis. | Revise; not found in the current converted Markdown or visible image reviewed here. | 0.04 | High | not_ready |
| The Pulgar/Arriagada row supplies a direct Dario-line bridge. | Not supported. | 0.03 | High | not_ready |
| The Pulgar/Arriagada row supports immediate Jose/Juana parent-candidate merges. | Hold. | 0.18 | High | hold |

## Verification Context

- Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md`.
- Reviewed conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525171911545.md`.
- Reviewed source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525171911545.md`.
- Reviewed assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Reviewed assigned converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Reviewed page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned converted Markdown, assigned chunk, and source packet. The QA note should certify which derivative file controls entry 172 and should resolve or explicitly preserve uncertainty in the father field after `Pulgar`. After QA, rerun proof review before any claim, relationship, identity merge, or Dario-line bridge is promoted.
