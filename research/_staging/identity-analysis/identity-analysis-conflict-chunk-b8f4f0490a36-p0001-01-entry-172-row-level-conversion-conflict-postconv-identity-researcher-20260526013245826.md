---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260526013245826
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers

- Exact staged conflict draft reviewed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md`.
- The assigned chunk/source packet and the current converted Markdown materially disagree about the row controlled by entry 172. The chunk/source packet read entry 172 as a Pulgar/Arriagada row; the converted Markdown reads entry 172 as a Burgos/de la Cruz row.
- This is a row-level conversion-control conflict, not a routine same-person, duplicate-person, or name-variant conflict. No child identity, parent relationship, birth-event, residence, informant, or parent-merge claim is canonical-ready from this draft.
- The father field remains uncertified. The next conversion QA step must decide whether the source-visible form is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical wiki context already contains entry-172-derived pages or evidence snapshots for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and a separate `Jose del Carmen Pulgar` stub, but this staged conflict prevents treating those facts as settled by this task.
- The entry does not name Dario, Arturo, Smith, Dario Jose, or Dario Pulgar Arriagada. Any Dario-line attachment requires a later proof-reviewed bridge source after row-control QA.

## Literal Evidence

Assigned chunk/source-packet reading:

- Entry and registration date: `172`; `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Parents: father read in the chunk as `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; both Chilean and resident at `Calle de Colipí`/`Calle de Colipi`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employed, resident at `Calle de Valdivia`.

Conflicting converted Markdown reading:

- Child: `Jose Miguel`.
- Birth: 6 April 1888, about 10 p.m.; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

Existing canonical wiki context:

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has entry-172-derived evidence snapshot material for the Pulgar/Arriagada child, including a probable mother link to `Juana Arriagada de Pulgar`.
- `wiki/people/juana-arriagada-de-pulgar.md` has an entry-172-derived probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- `wiki/people/jose-del-carmen-pulgar.md` is a separate stub with a draft child link to `Tulio Cesar Luis Jose`; it does not settle whether the entry-172 father candidate is the same person.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate Juana-name parent candidate in existing wiki context; it is not proved to be the same person as `Juana Arriagada de Pulgar` by this entry.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to attach similarly named Pulgar records without identity review.
- `wiki/people/dar-o-pulgar-arriagada.md` is a separate `Darío Pulgar Arriagada` stub supported by a 5 December 2000 event, not by this 1888 birth entry.

## Hypotheses And Scores

| rank | hypothesis | claim probability | identity confidence | conflict severity | evidence quality | conversion confidence | relevance | canonical readiness | next required step |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.74 | 0.66 | 0.95 | 0.78 | 0.35 | 0.98 | 0.10 | Targeted conversion QA must certify the controlling row and father-field reading, then rerun proof review. |
| 2 | Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.18 | 0.25 | 0.95 | 0.45 | 0.35 | 0.90 | 0.05 | Conversion QA must explain whether the converted Markdown is from the wrong row/image assignment or supersedes the chunk/source packet. |
| 3 | The entry-172 father candidate is the same person as canonical `Jose del Carmen Pulgar`. | 0.35 | 0.30 | 0.60 | 0.55 | 0.30 | 0.70 | 0.05 | After row-control QA, run a parent-candidate proof review using father name, suffix/mark, residence, mother/spouse context, chronology, and other reviewed local sources. |
| 4 | `Juana Arriagada de Pulgar` is the mother of the entry-172 Pulgar/Arriagada child. | 0.70 | 0.62 | 0.85 | 0.76 | 0.35 | 0.95 | 0.10 | After row-control QA, proof-review this as a narrow civil-registration mother-child relationship claim. |
| 5 | `Juana Arriagada de Pulgar` and existing `Juana de Dios Amagada de Pulgar` are the same person or name variants. | 0.22 | 0.18 | 0.70 | 0.42 | 0.30 | 0.55 | 0.00 | Do not merge. Require a separate Juana parent-candidate proof review comparing literal names, spouses/children, residences, dates, and source provenance. |
| 6 | This entry bridges any Dario Pulgar identity cluster. | 0.02 | 0.03 | 0.80 | 0.20 | 0.35 | 0.25 | 0.00 | Do not attach to a Dario candidate unless later proof-reviewed evidence directly connects the Jose/Juana cluster to that Dario identity. |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: The canonical page is family-supplied and contains a maternal-grandfather relationship to Alexander John Heinz. Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, a spouse, a descendant, or any lineage bridge. Same-person or lineage attachment from this entry is unsupported.
- `Dario Arturo Pulgar`: Local staged CV context concerns a document-level subject named Dario Arturo Pulgar. This birth-register entry names no Dario or Arturo and provides no CV, occupation, age, residence, or family bridge to that document-level subject.
- `Dario Jose Pulgar-Arriagada`: The Pulgar hypothesis for this entry reads the child as `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose`. Shared Pulgar/Arriagada surname elements are only family-context hints.
- `Dario/Darío Pulgar Arriagada`: Existing canonical/staged context keeps this as a separate cluster, including a 2000 expropriation event. This 1888 entry provides no Dario name, adulthood chronology, property event, or identity bridge.
- Jose/Juana parent candidates: Under the Pulgar hypothesis, `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` are candidate parents for the entry-172 child. The mother reading is more direct in the chunk/source packet; the father reading is additionally blocked by the unresolved suffix/mark and possible overlap with other `Jose del Carmen Pulgar` candidates. Existing `Juana de Dios Amagada de Pulgar` must remain a separate candidate unless a later proof review shows that `Amagada` is a conversion/name variant of `Arriagada` and that the surrounding relationships align.

## Conflicts

- Same-entry conflict: Pulgar/Arriagada child-parent row versus Burgos/de la Cruz child-parent row.
- Relationship-conflict risk: Promoting before QA could attach the wrong child to the wrong parents.
- Name-variant risk: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` must remain separate literal readings until certified.
- Duplicate-person risk: The existing `Jose del Carmen Pulgar` stub and the entry-172 father candidate cannot be merged by name alone.
- Juana-name conflict risk: `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` may be separate people or may reflect conversion/name variation, but this staged draft does not prove either result.
- Chronology conflict: No impossible chronology is established from this entry alone. The blocking issue is row control and transcription reliability.
- Dario-line conflation risk: High if Pulgar/Arriagada surname overlap is used as a bridge to Dario candidates without proof-reviewed identity evidence.

## Recommended Next Action

Keep this staged conflict on `hold_for_conversion_qa`. The exact next proof-review or promotion step is targeted conversion QA for page 58, entry 172: compare the source image, converted Markdown, assigned chunk, and source packet; decide the controlling entry-172 row; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review before any child identity promotion, parent-child relationship promotion, `Jose del Carmen Pulgar` parent-candidate merge, Juana-name merge, canonical wiki update, or Dario-line comparison.
