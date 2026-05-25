---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525210917759
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Row Conflict Hold

## Blockers

- Exact staged conflict draft reviewed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md`.
- The assigned chunk/source packet and current converted Markdown disagree on the whole entry-172 row. This is not a spelling, name-order, or same-person variant issue.
- The chunk/source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- The current converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The father field in the Pulgar reading is not promotion-ready until targeted QA decides whether the controlling literal reading is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical wiki pages already contain entry-172-derived snapshots for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`; this analysis does not promote, retract, merge, or rename those pages.
- The entry does not name Dario, Arturo, Smith, Dario Jose, or Darío/Dario Pulgar Arriagada. Any Pulgar-line bridge to Dario candidates remains blocked.

## Literal Evidence

From the assigned staged draft and source packet:

- Entry: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child under the Pulgar/Arriagada reading: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth under the Pulgar/Arriagada reading: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Parents under the Pulgar/Arriagada reading: father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; both Chilean; residence `Calle de Colipí`.
- Informant under the Pulgar/Arriagada reading: `Ernesto Herrera L.`, present at birth, age 26, employed, resident at `Calle de Valdivia`.

From the conflicting converted Markdown:

- Child under the Burgos/de la Cruz reading: `Jose Miguel`; sex `Varon`.
- Birth under the Burgos/de la Cruz reading: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Parents under the Burgos/de la Cruz reading: father `Oswaldo Burgos`; mother `Concepcion de la Cruz`.
- Informant under the Burgos/de la Cruz reading: `Oswaldo Burgos`, age 26, employed, resident `En esta`.

Existing canonical wiki context reviewed:

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` contains an entry-172-derived evidence snapshot for the Pulgar/Arriagada child and a probable mother link to `Juana Arriagada de Pulgar`.
- `wiki/people/juana-arriagada-de-pulgar.md` contains an entry-172-derived probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- `wiki/people/jose-del-carmen-pulgar.md` is a separate stub with a draft child link to `Tulio Cesar Luis Jose`; it does not prove the entry-172 father is the same person.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and warns against automatic attachment of similarly named Pulgar records.
- `wiki/people/dar-o-pulgar-arriagada.md` is a separate Darío Pulgar Arriagada stub with a 2000 expropriation/event mention, not this 1888 birth entry.

## Hypotheses And Scores

| rank | hypothesis | claim probability | identity confidence | conflict severity | evidence quality | conversion confidence | relevance | canonical readiness |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.72 | 0.66 | 0.95 | 0.78 | 0.35 | 0.98 | 0.10 |
| 2 | Entry 172 is the Burgos/de la Cruz birth row for `Jose Miguel`. | 0.18 | 0.25 | 0.95 | 0.45 | 0.35 | 0.90 | 0.05 |
| 3 | The Pulgar-reading father is the same person as canonical `Jose del Carmen Pulgar`. | 0.35 | 0.30 | 0.60 | 0.55 | 0.30 | 0.70 | 0.05 |
| 4 | `Juana Arriagada de Pulgar` is the mother of the entry-172 Pulgar/Arriagada child. | 0.70 | 0.62 | 0.85 | 0.76 | 0.35 | 0.95 | 0.10 |
| 5 | This entry bridges a Dario Pulgar identity cluster. | 0.02 | 0.03 | 0.80 | 0.20 | 0.35 | 0.25 | 0.00 |

## Evidence Supporting Each Hypothesis

Hypothesis 1, Pulgar/Arriagada row:

- The assigned chunk and staged source packet agree on the Pulgar/Arriagada child, parents, registration date, birth date, place, and informant.
- The source packet states that the visible source image aligns at a high level with the Pulgar/Arriagada row on page 58, entry 172.
- This hypothesis is most relevant to existing Pulgar/Arriagada canonical stubs, but it remains conversion-blocked.

Hypothesis 2, Burgos/de la Cruz row:

- The current assigned converted Markdown explicitly gives entry 172 as `Jose Miguel`, with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`.
- This hypothesis explains the current converted Markdown text, but it conflicts with the assigned chunk/source packet and has no Pulgar-line relevance unless QA finds the chunk/source-packet assignment is wrong.

Hypothesis 3, entry-172 father equals canonical `Jose del Carmen Pulgar`:

- The Pulgar row reads the father as `Jose del Carmen Pulgar S.` or a close father-field variant.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` has a separate draft child link to `Tulio Cesar Luis Jose`, suggesting a local Jose del Carmen Pulgar candidate cluster.
- Name overlap alone is insufficient. A parent-candidate proof review must compare suffix, spouse/mother context, residence, chronology, and other reviewed local sources after row-control QA.

Hypothesis 4, `Juana Arriagada de Pulgar` mother-child relationship:

- Under the Pulgar row, the mother field directly names `Juana Arriagada de Pulgar`.
- The existing Juana wiki page already records this entry-172-derived probable child link.
- The relationship is strong only if targeted QA confirms that the Pulgar row is the controlling row for entry 172.

Hypothesis 5, Dario-line bridge:

- No literal support in this entry names `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or any Dario/Darío variant.
- Shared `Pulgar` or `Pulgar Arriagada` surname context is only a prompt for later double-checking, not evidence for a same-person or lineage bridge.

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical context is family-supplied as Alexander John Heinz's maternal grandfather. This entry does not name him, state `Smith`, or provide a relationship to Alexander John Heinz. Probability this entry directly supports him: 0.01; canonical readiness: 0.00.
- `Dario Arturo Pulgar`: Staged CV contexts concern a document-level subject named Dario Arturo Pulgar. This entry does not name Dario or Arturo and provides no CV, occupation, residence, or family bridge to that subject. Probability this entry directly supports him: 0.02; canonical readiness: 0.00.
- `Dario Jose Pulgar-Arriagada`: Local staged photograph/source contexts use this name, but the entry-172 Pulgar hypothesis reads `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose`. Probability of direct identity support from this entry: 0.02; canonical readiness: 0.00.
- `Dario/Darío Pulgar Arriagada`: Existing wiki context treats `Darío Pulgar Arriagada` as a separate stub tied to a 2000 expropriation event. This 1888 entry does not name Darío/Dario or supply chronology linking the birth child to the 2000 event person. Probability of direct identity support from this entry: 0.02; canonical readiness: 0.00.
- Jose/Juana parent candidates: Under the Pulgar hypothesis, `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` are candidate parents for `Jose del Carmen Segundo Pulgar Arriagada`. These candidates should remain literal-entry candidates until row-control QA and a narrow relationship proof review are complete.

## Conflicts

- Same-entry conversion conflict: Pulgar/Arriagada child-parent row versus Burgos/de la Cruz child-parent row.
- Relationship conflict risk: premature promotion could attach the wrong child to the wrong parents.
- Duplicate-person risk: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and any canonical `Jose del Carmen Pulgar` candidate cannot be merged by name alone.
- Name-variant risk: the Pulgar father-field suffix or mark must remain literal and uncertain until certified.
- Chronology conflict: no impossible chronology is established from this entry alone. The primary issue is conversion control, not dates.
- Dario-line conflation risk: high if Pulgar/Arriagada surname overlap is used to bridge to Dario candidates without proof-reviewed identity evidence.

## Recommended Next Action

Keep this draft on `hold_for_conversion_qa`. The exact next proof-review step is targeted conversion QA for page 58, entry 172: compare the source image, current converted Markdown, assigned chunk, and source packet; decide whether the controlling entry-172 row is Pulgar/Arriagada or Burgos/de la Cruz; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before any child identity promotion, parent-child relationship promotion, parent-candidate merge, canonical wiki update, or Dario-line comparison.
