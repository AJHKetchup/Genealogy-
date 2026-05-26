---
type: identity_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526174214617
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
created: 2026-05-26
---

# Identity Analysis: Entry 172 Current Conversion Conflict

## Blockers First

1. The exact staged conflict draft is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md`.
2. The assigned chunk and staged source packet read entry `172` as a Pulgar/Arriagada birth registration, while the current converted Markdown reads entry `172` as a Burgos/de la Cruz birth registration. This is a material row-control conflict, not a same-person or name-variant issue.
3. The conflict changes the child, birth date/time/place, father, mother, informant, and all dependent relationship claims.
4. The Pulgar father field is not fully certified. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA states the visible reading.
5. Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada. Existing wiki and staged Dario context is anti-conflation context only.
6. Do not promote child identity, parent-child relationships, parent merges, duplicate-person conclusions, Dario-line attachments, or canonical facts until row QA is complete and proof review follows.

## Literal Evidence

- Staged draft Pulgar/Arriagada reading: `Jose del Carmen Segundo Pulgar Arriagada`, male; registered 7 April 1888; born 8 March 1888 about 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar` with possible trailing `S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- Assigned chunk reading: entry `172` on page 58 names `Jose del Carmen Segundo Pulgar Arriagada`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- Staged source packet states that source-image review supports the Pulgar/Arriagada row for entry `172`, with father visible at least as `Jose del Carmen Pulgar` and a trailing mark compatible with `S.`.
- Current converted Markdown reading: entry `172` names `José Miguel`; born 6 April 1888 about 10 p.m. at `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.
- Existing canonical context checked: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`.

Interpretation kept separate: if the Pulgar row is certified, this is a strong local source for one Pulgar/Arriagada birth-registration cluster. It is not a bridge to the Dario clusters or a merge instruction for existing Jose/Juana candidates.

## Hypotheses And Scores

| Rank | Hypothesis | Supporting Evidence | Conflicts / Limits | Probability | Identity Confidence | Canonical Readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | Entry `172` is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk and staged source packet give a coherent Pulgar/Arriagada row and image-review statement. | Current converted Markdown gives a wholly different row; father suffix remains unresolved. | 0.66 | 0.64 | 0.15 |
| 2 | Entry `172` is the Burgos/de la Cruz row for `José Miguel`. | Current converted Markdown gives a complete row with Burgos/de la Cruz parents. | Directly contradicted by assigned chunk and staged source packet for the same entry number. | 0.30 | 0.28 | 0.05 |
| 3 | The Pulgar-row father is a `Jose del Carmen Pulgar [?]` parent candidate. | Assigned chunk reads `Jose del Carmen Pulgar S.`; staged packet supports at least `Jose del Carmen Pulgar`. Existing wiki has a `Jose del Carmen Pulgar` stub. | Exact suffix and cross-entry identity are unproved; do not merge to suffix-free canonical cluster yet. | 0.44 | 0.46 | 0.10 |
| 4 | The Pulgar-row mother is `Juana Arriagada de Pulgar`, compatible with the existing same-name stub. | Assigned chunk and source packet name `Juana Arriagada de Pulgar`; wiki stub has derivative entry-172 context. | Canonical stub evidence is not independent of this conflicted cluster; do not conflate with other Juana candidates. | 0.52 | 0.55 | 0.12 |
| 5 | Entry 172 bridges to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | Broad Pulgar-line relevance only; canonical Pulgar-Smith page is family-supplied and warns against automatic merges. | No Dario, Arturo, Smith, Pulgar-Smith, CV, spouse, child, grandchild, or Alexander John Heinz bridge appears here. | 0.04 | 0.05 | 0.00 |
| 6 | Entry 172 bridges to `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`. | The certified Pulgar row would share the surname combination `Pulgar Arriagada`. | Entry names `Jose del Carmen Segundo`, not Dario; no age, role, property, medical, ICRC, or full-name bridge. | 0.02 | 0.03 | 0.00 |
| 7 | Entry 172 resolves broader Jose/Juana parent candidates from other register clusters. | Name overlap with `Jose del Carmen Pulgar` and direct mother reading for `Juana Arriagada de Pulgar` if the Pulgar row controls. | Other clusters are separate, draft, or conversion-sensitive; family-context hints do not prove relationships. | 0.16 | 0.18 | 0.03 |

## Conflict Classification

- Same-person conflict: `Jose del Carmen Segundo Pulgar Arriagada` and `José Miguel` should be treated as competing row readings, not one child with variant names.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is merged into `Jose del Carmen Pulgar` or if Juana candidates are merged across entries before row and field QA.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is a transcription/field-certification issue. `Pulgar Arriagada`, `Pulgar-Smith`, `Dario Arturo Pulgar`, and `Dario Jose Pulgar-Arriagada` are not proved variants here.
- Relationship conflict: competing rows name different parent pairs: `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar` versus `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Chronology conflict: the Pulgar/Arriagada reading gives birth on 8 March 1888; the converted Burgos/de la Cruz reading gives birth on 6 April 1888.
- Conversion conflict: row-level conversion confidence is low until targeted QA reconciles the source image, assigned chunk, staged packet, and current converted Markdown.

## Overall Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Highest for the Pulgar/Arriagada row, but blocked by the conflicting converted-file row. |
| conflict_severity | 0.95 | The conflict changes the whole identity and family structure of entry `172`. |
| evidence_quality | 0.70 | Useful local staged evidence, but derivative readings disagree. |
| conversion_confidence | 0.35 | Targeted row and father-field QA is required. |
| claim_probability | 0.66 | Pulgar/Arriagada is probable if the assigned chunk/source-packet image review is certified. |
| relevance | 0.95 | Directly addresses the assigned staged draft and required Pulgar-line anti-conflation comparisons. |
| canonical_readiness | 0.10 | Hold; no canonical promotion or merge. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, current converted Markdown, staged source packet, and staged conflict draft. The QA must decide which row controls entry `172` and certify the father field only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, run proof review before promoting any child identity, birth fact, parent-child relationship, same-person conclusion, duplicate-person decision, parent merge, or canonical attachment. The exact next Pulgar-line proof-review step should explicitly compare the certified entry-172 evidence against `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and other Jose/Juana parent candidates, preserving separate hypotheses unless a direct bridge is found.
