---
type: identity_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526173522659
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
created: 2026-05-26
---

# Identity Analysis: Entry 172 Current Conversion Conflict

## Blockers

1. The staged draft identifies a material row-level conversion conflict. The assigned chunk and source packet read entry `172` as the Pulgar/Arriagada row, while the current converted Markdown reads entry `172` as a Burgos/de la Cruz row. These are not same-person variants.
2. The father field in the Pulgar/Arriagada reading is not certified at proof-review precision. Preserve the alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA records the visible reading.
3. Existing canonical wiki pages already contain low-confidence or family-supplied Pulgar-line context, but this staged draft cannot promote or repair those pages. It must not attach this entry to canonical `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or parent candidates by name cluster alone.
4. All child identity, birth facts, parent-child relationships, duplicate-person decisions, and canonical readiness remain blocked until conversion QA decides which row controls entry `172`.

## Literal Evidence

From the assigned chunk and staged source packet:

- Entry number: `172`.
- Registration date: 7 April 1888.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: 8 March 1888, about 3 p.m.; place `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.` in the chunk; source packet says the visible field supports at least `Jose del Carmen Pulgar` with an unresolved trailing letter or mark.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth.

From the current converted Markdown:

- Entry number: `172`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: 6 April 1888, about 10 p.m.; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

Existing canonical wiki context checked:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied only and explicitly warns against automatic merges with similar Pulgar clusters.
- `wiki/people/dar-o-pulgar-arriagada.md` is a stub for `Darío Pulgar Arriagada` with a 5 December 2000 expropriation event; it has no parent bridge to entry 172.
- `wiki/people/jose-del-carmen-pulgar.md` is a stub with a separate draft child link to `Tulio Cesar Luis Jose`.
- `wiki/people/juana-arriagada-de-pulgar.md` and `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` contain low-confidence entry-172 evidence snapshots, but the row conflict keeps those snapshots from being promotion-ready.

## Hypotheses

| Rank | Hypothesis | Supporting evidence | Conflicts and limits | Identity confidence | Claim probability | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | The assigned chunk and source packet give a coherent full-row reading with child, birth date/time/place, father, mother, and informant. | Current converted Markdown gives an incompatible Burgos/de la Cruz row for the same entry number; father suffix unresolved. | 0.62 | 0.64 | hold |
| 2 | Entry `172` is the Burgos/de la Cruz row for `Jose Miguel`. | The current converted Markdown gives a complete alternate row. | It conflicts with the assigned chunk and source packet and appears to represent a different row or source-control problem. | 0.28 | 0.30 | hold |
| 3 | `Jose del Carmen Pulgar S.` is the same person as a suffix-free `Jose del Carmen Pulgar` parent candidate. | The base name matches; local wiki has a `Jose del Carmen Pulgar` stub and Pulgar parent-candidate context. | The trailing `S.` or mark is unresolved; the wiki stub has separate evidence and cannot be merged by name alone. | 0.46 | 0.42 | hold |
| 4 | `Juana Arriagada de Pulgar` in entry 172 is the same person as the existing `Juana Arriagada de Pulgar` stub. | Exact name match and existing entry-172 evidence snapshot. | The canonical snapshot depends on this conflicted entry cluster; no independent identity bridge is supplied here. | 0.55 | 0.50 | hold |
| 5 | Entry-172 child or parents bridge to `Dario Arturo Pulgar-Smith`. | Pulgar/Arriagada surname context makes this family-relevant for later checking. | The record does not name Dario, Arturo, Smith, a grandchild, spouse, or any bridge to Alexander John Heinz. | 0.05 | 0.04 | not ready |
| 6 | Entry-172 child or parents bridge to document-level `Dario Arturo Pulgar`. | Shared Pulgar-line context only. | The entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar, and has no CV/document bridge. | 0.04 | 0.03 | not ready |
| 7 | Entry-172 child or parents bridge to `Dario Jose Pulgar-Arriagada`. | Pulgar-Arriagada surname cluster is a reason to compare after row QA. | This staged draft does not name Dario Jose; no age, profession, residence, parent, spouse, or event bridge is present. | 0.03 | 0.02 | not ready |
| 8 | Entry-172 child or parents bridge to `Dario/Dario Pulgar Arriagada` or canonical `Darío Pulgar Arriagada`. | Existing wiki has a `Darío Pulgar Arriagada` page; surname cluster overlaps. | The canonical page records a 2000 event and no parentage; entry 172 is an 1888 birth for a Jose-named child if the chunk controls. | 0.02 | 0.02 | not ready |

## Conflict Assessment

- Same-person conflict: high. `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` have different names, parents, birth dates, birth places, and informants. Treat them as competing row readings, not one child.
- Duplicate-person risk: moderate-high. Prematurely merging `Jose del Carmen Pulgar S.` with `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar` with any broader Juana candidate, would bypass the row and father-field QA blockers.
- Name-variant conflict: moderate. `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is a literal transcription issue, not a proved variant. `Pulgar Arriagada`, `Pulgar-Smith`, and `Pulgar` are not interchangeable without a proof-reviewed bridge.
- Relationship conflict: high. Depending on which derivative controls, the parents are either `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`, or `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Chronology conflict: high. The Pulgar/Arriagada row gives birth on 8 March 1888; the converted Burgos/de la Cruz row gives birth on 6 April 1888.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.62 | The Pulgar/Arriagada row is coherent in the assigned chunk and source packet, but the assigned converted file gives a materially different row. |
| Conflict severity | 0.95 | The conflict changes child, parents, birth date/time/place, informant, and all relationship candidates. |
| Evidence quality | 0.70 | Local evidence includes a chunk, source packet, converted Markdown, and wiki context, but the derivatives disagree. |
| Conversion confidence | 0.35 | The staged packet explicitly flags low conversion confidence and row-control QA need. |
| Claim probability | 0.64 | Probable that the Pulgar/Arriagada row is the intended family-relevant entry if the chunk controls; not safe for promotion. |
| Relevance | 0.90 | The row is directly relevant to Pulgar/Arriagada parent and child candidates and to anti-conflation review for Dario-line clusters. |
| Canonical readiness | 0.15 | Not ready until targeted conversion QA and proof review resolve row control and father-field wording. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, current converted Markdown, staged source packet, and staged conflict draft. The QA note must decide the controlling entry-172 row and certify the father field only to the visible extent as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth claim, parent-child relationship, same-person conclusion, duplicate-person decision, or canonical attachment. For Pulgar-line work, the next proof-review step must explicitly compare certified entry-172 evidence against `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and any other Jose/Juana parent candidates, while preserving separate hypotheses unless a direct bridge is found.
