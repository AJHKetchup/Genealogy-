---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
worker: "postconv-identity-analysis-20260530092229282"
role: identity_researcher
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530072501797.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530072501797.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

This note analyzes the exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md`.

## Blockers First

- Row-control blocker: the assigned chunk records entry `172` as a Pulgar/Arriagada birth row, while the current converted Markdown records entry `172` as a Burgos/de la Cruz birth row.
- Original-image blocker: both expected source paths for the original PNG are absent in this checkout, so this identity analysis cannot freshly certify the full-page row alignment.
- Derivative-only blocker: staged parent-field crops support the Pulgar/Arriagada parent/informant fields at crop level, but crop evidence does not replace full-page row-control proof review.
- Father-name blocker: preserve the father only as `Jose del Carmen Pulgar` unless proof review certifies the possible trailing `S.` or other suffix.
- Identity-scope blocker: this staged draft does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada. Surname and family-line context are review leads only.
- Canonical blocker: no merge, rename, canonical attachment, or fact promotion should happen from this conflict note.

## Literal Evidence

Assigned chunk and staged packet reading:

- Entry `172`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`.
- Birth `Ocho de Marzo de mil ochocientos ochenta i ocho`, `a las tres de la tarde`, at `Calle de Valdivia`.
- Father field transcribed in the chunk as `Jose del Carmen Pulgar S.`, but the staged packet/review says to preserve only `Jose del Carmen Pulgar`.
- Mother `Juana Arriagada de Pulgar`.
- Informant `Ernesto Herrera L.`, present at the birth.

Current converted Markdown reading:

- Entry `172`, child `Jose Miguel`.
- Birth 6 April 1888 at 10 p.m., place `En esta`.
- Father `Oswaldo Burgos`.
- Mother `Concepcion de la Cruz`.

Interpretation: these are incompatible row-control readings, not name variants for the same child or parent set.

## Ranked Hypotheses

| Rank | Hypothesis | Evidence for | Evidence against / limits | Claim probability | Identity confidence | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | Physical entry `172` is the Pulgar/Arriagada birth registration. | Assigned chunk, staged source packet, and crop-level QA support `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.` | Current converted Markdown conflicts; full-page original image is unavailable in this checkout; father suffix unresolved. | 0.72 | 0.68 | hold |
| 2 | Physical entry `172` is the Burgos/de la Cruz registration. | Current converted Markdown reads `Jose Miguel`, `Oswaldo Burgos`, and `Concepcion de la Cruz`. | Contradicted by assigned chunk, source packet, and staged crop-level review; no Pulgar family overlap. | 0.18 | 0.20 | hold |
| 3 | The two readings are shifted-row or shifted-page derivative outputs. | The names, parents, dates, and places differ materially while sharing an entry number; this fits row-control failure better than identity variation. | The exact source of the shift cannot be certified without full-page original-image review. | 0.80 | 0.75 | hold |
| 4 | `Juana Arriagada de Pulgar` is the recorded mother of `Jose del Carmen Segundo Pulgar Arriagada`. | Direct in the assigned chunk and staged packet; existing canonical page has a probable child link. | Dependent on row-control certification; do not merge with other Juana candidates by married-name similarity. | 0.68 | 0.55 | not_ready |
| 5 | `Jose del Carmen Pulgar` is the recorded father of `Jose del Carmen Segundo Pulgar Arriagada`. | Father field appears in assigned chunk and crop-level review. | Row-control unresolved; possible suffix after `Pulgar` unresolved; same-name match to existing canonical `Jose del Carmen Pulgar` is not enough for merge. | 0.48 | 0.40 | not_ready |
| 6 | Entry `172` directly identifies or bridges to a Dario Pulgar identity. | Pulgar/Arriagada surname context may justify later review if the row is certified. | No `Dario`, `Arturo`, `Smith`, adult occupation, spouse, descendant, or later-life bridge appears here. | 0.03 | 0.02 | not_ready |
| 7 | Pulgar/Arriagada and Burgos/de la Cruz are same-person/name-variant evidence. | Entry-number overlap only. | Different child names, parent names, birth dates, and birth places. | 0.01 | 0.02 | reject |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns against automatic merges with similarly named clusters. Entry `172` supplies no `Dario`, `Arturo`, `Smith`, or Alexander relationship evidence. Probability of direct same-person or relationship bridge from this packet: 0.01.
- `Dario Arturo Pulgar`: staged CV contexts elsewhere name a document-level `Dario Arturo Pulgar`; entry `172` names `Jose del Carmen Segundo Pulgar Arriagada` and gives no CV, occupation, chronology, or descendant bridge. Probability: 0.02.
- `Dario Jose Pulgar-Arriagada`: staged ICRC/portrait contexts elsewhere preserve this as a separate candidate. Entry `172` includes `Jose` as part of `Jose del Carmen Segundo`, but does not name `Dario Jose`; do not convert the name form silently. Probability: 0.03.
- `Dario/Dario Pulgar Arriagada` and canonical `Darío Pulgar Arriagada`: canonical context has a 2000 expropriation notice for `Darío Pulgar Arriagada`; entry `172` has surname overlap only and no bridge from the 1888 child or parents. Probability: 0.02.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are the only direct parent candidates in this staged draft if the Pulgar row controls. Existing `Juana de Dios Amagada de Pulgar` and other Jose/Juana Pulgar-line candidates remain separate unless a later proof-review step supplies direct evidence.

## Conflict Classification

- Same-person conflict: none resolved; reject same-person treatment between the Pulgar/Arriagada and Burgos/de la Cruz readings.
- Duplicate-person risk: moderate to high for Jose/Juana parent pages if same-name or married-name clues are promoted without row-control proof.
- Name-variant issue: limited to `Jose del Carmen Pulgar` versus possible `Jose del Carmen Pulgar S.`; not proof-ready.
- Relationship conflict: high, because the two derivative readings assign different parents and children to entry `172`.
- Chronology conflict: high at row level, because Pulgar/Arriagada gives birth on 8 March 1888 at 3 p.m., while Burgos/de la Cruz gives birth on 6 April 1888 at 10 p.m.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.68 | Strongest for a row-local Pulgar/Arriagada child identity if row-control is certified; not sufficient for wider identity linkage. |
| Conflict severity | 0.92 | The same entry number has different child, parent, date/time, and place facts across derivative outputs. |
| Evidence quality | 0.62 | Civil registration is a strong source type and crop-level support is useful, but full-page original certification is missing here. |
| Conversion confidence | 0.45 | Assigned chunk/crops favor Pulgar/Arriagada, but current converted Markdown materially conflicts. |
| Claim probability | 0.72 | Pulgar/Arriagada row is the leading local hypothesis, still held for QA. |
| Relevance | 0.96 | Directly relevant to the assigned Pulgar/Arriagada row-control conflict. |
| Canonical readiness | 0.10 | Not ready for promotion, merge, or canonical strengthening from this note. |

## Recommended Next Action

Keep the staged draft on `hold_for_conversion_qa`. The exact next proof-review step is targeted full-page original-image row-control review for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, comparing the staged source packet, conversion review note, assigned chunk, current converted Markdown, manifest context, and staged parent-field crops.

That proof review must decide which physical row controls entry `172` and whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain `Jose del Carmen Pulgar [?]`. Only after row-control is certified should narrow birth-name, birth-event, parent-name, and parent-child claims be reviewed. A separate identity-bridge review is required before any attachment to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or any Jose/Juana parent candidate beyond the literal row.
