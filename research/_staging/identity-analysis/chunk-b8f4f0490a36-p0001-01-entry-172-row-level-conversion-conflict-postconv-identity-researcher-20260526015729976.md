---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526015729976
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: 0.00
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers

- Row control is unresolved. The assigned chunk reads entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown reads entry 172 as a Burgos/de la Cruz birth row.
- The father field in the Pulgar/Arriagada reading is not ready for canonical use until targeted conversion QA certifies the visible reading as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No same-person, duplicate-person, parent-child, or Dario-line promotion should proceed from this draft while the same entry number carries two incompatible row readings.
- Existing canonical wiki pages contain entry-172-derived Pulgar snapshots, but those pages do not independently resolve this staged row-control conflict.
- The requested `genealogy-proof-review` contract is applied here as an evidence standard only; this note did not perform external research, document conversion, canonical promotion, page rename, merge, or source-output editing.

## Literal Source Readings Kept Separate

### Assigned Chunk And Held Source Packet Reading

- Entry number: `172`.
- Registration date: 7 April 1888.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: 8 March 1888, about 3 p.m.
- Birthplace: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk/source-packet reading.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.
- Parent residence in the chunk/source-packet reading: `Calle de Colipi`.

### Current Converted Markdown Reading

- Entry number: `172`.
- Registration date: 7 April 1888.
- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: 6 April 1888, about 10 p.m.
- Birthplace: `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Existing Wiki Context Considered

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has an entry-172-derived person stub and life facts for the Pulgar/Arriagada child cluster.
- `wiki/people/juana-arriagada-de-pulgar.md` has an entry-172-derived probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- `wiki/people/jose-del-carmen-pulgar.md` exists as a separate stub and currently includes a different staged child link from entry 513 context, not a resolved entry-172 relationship.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` exists as a separate Juana candidate from entry 513 context and should not be merged with `Juana Arriagada de Pulgar` by given name or married-name form alone.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records need identity review before attachment.
- `wiki/people/dar-o-pulgar-arriagada.md` is a separate Darío Pulgar Arriagada stub with a 2000 expropriation event; this entry supplies no Dario/Darío name or 2000-event bridge.

## Hypotheses And Scores

| Rank | Hypothesis | Evidence supporting | Evidence against or conflict | Identity confidence | Conflict severity | Evidence quality | Conversion confidence | Claim probability | Relevance | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk and held source packet agree on the Pulgar/Arriagada row; existing wiki snapshots reflect this cluster. | Current converted Markdown gives a complete Burgos/de la Cruz row for the same entry number; father suffix/terminal mark remains unresolved. | 0.70 | 0.95 | 0.78 | 0.35 | 0.66 | 0.98 | 0.00 |
| 2 | Entry 172 is the Burgos/de la Cruz birth row for `Jose Miguel`. | Current converted Markdown gives a complete internally coherent Burgos/de la Cruz row. | Assigned chunk and held source packet give a complete Pulgar/Arriagada row for the same entry number and are the family-relevant staged evidence. | 0.45 | 0.95 | 0.60 | 0.35 | 0.34 | 0.20 | 0.00 |
| 3 | The conflict is a derivative row-alignment/conversion-control problem, not a true same-person conflict. | The two readings have different child names, parents, birth dates, places, informants, residences, and neighboring row context. | Requires targeted conversion QA against the source image to decide which row controls the assigned entry/chunk. | 0.88 | 0.95 | 0.82 | 0.35 | 0.90 | 1.00 | 0.00 |

## Identity And Relationship Conflict Findings

- Same-person conflict: `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` should not be treated as the same person. The names, parents, birth date, birthplace, and informant differ materially.
- Duplicate-person conflict: no duplicate-person merge is justified. The issue is row control, not duplicate canonical stubs.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` must remain separate literal possibilities until the father field is certified. `Jose Miguel` is not a name variant of `Jose del Carmen Segundo Pulgar Arriagada`.
- Relationship conflict: under the Pulgar reading, candidate parents are `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; under the converted Markdown reading, parents are `Oswaldo Burgos` and `Concepcion de la Cruz`. These are mutually exclusive parent sets for entry 172.
- Chronology conflict: the Pulgar reading gives birth on 8 March 1888 at about 3 p.m.; the Burgos reading gives birth on 6 April 1888 at about 10 p.m. Both cannot control the same entry-172 child claim.
- Parent-candidate caution: `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are separate local candidates unless a later proof-reviewed source directly bridges them. The entry-172 draft alone does not support merging them.

## Pulgar-Line Comparison

| Candidate | Direct support from this draft | Assessment |
| --- | ---: | --- |
| `Dario Arturo Pulgar-Smith` | 0.00 | Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, a spouse, child, or grandchild. |
| `Dario Arturo Pulgar` | 0.00 | Existing staged CV context elsewhere concerns a document-level subject named `Dario Arturo Pulgar`. This entry does not name Dario or Arturo and gives no CV, occupation, education, or family bridge to that subject. |
| `Dario Jose Pulgar-Arriagada` | 0.00 | The Pulgar-row hypothesis names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose Pulgar-Arriagada`. Shared surname elements are insufficient. |
| `Dario/Darío Pulgar Arriagada` | 0.00 | Existing wiki context keeps `Darío Pulgar Arriagada` as a separate 2000-event cluster. This 1888 entry gives no Dario/Darío name and no chronology bridge. |
| `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` | 0.66 | Candidate father only under the Pulgar row reading. Needs row-control QA and father-field certification before relationship proof review. |
| `Juana Arriagada de Pulgar` | 0.66 | Candidate mother only under the Pulgar row reading. Needs row-control QA before relationship proof review. |
| `Juana de Dios Amagada de Pulgar` | 0.02 | Existing entry-513 context names this separate Juana candidate; this entry-172 draft does not bridge her to `Juana Arriagada de Pulgar`. |

Ranked Pulgar conclusion: entry 172, if QA certifies the Pulgar/Arriagada row, may support a candidate child-parent cluster for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar S.`, and `Juana Arriagada de Pulgar`. It does not support attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` without a later identity-bridge proof review.

## Recommended Next Action

1. Targeted conversion QA should compare the raw source image, current converted Markdown, assigned chunk, and held source packet for entry 172 and decide which row controls the assigned entry/chunk.
2. During that QA, certify the Pulgar-row father field exactly to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. After conversion QA, rerun proof review before any child identity promotion, birth-fact promotion, parent-child relationship promotion, Jose/Juana same-person analysis, canonical wiki update, or Dario-line identity bridge.
4. Keep all entry-172-derived Pulgar/Arriagada and Burgos/de la Cruz claims on hold until the row-level conflict is resolved.
