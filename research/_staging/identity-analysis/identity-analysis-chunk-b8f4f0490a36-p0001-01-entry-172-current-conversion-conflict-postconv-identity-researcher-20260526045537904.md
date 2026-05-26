---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526045537904
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
created: 2026-05-26
---

# Identity Analysis: Entry 172 Current Conversion Conflict

## Blockers First

- The controlling row for entry `172` is unresolved. The staged conflict draft and source packet preserve an assigned-chunk reading for `Jose del Carmen Segundo Pulgar Arriagada`, while the current converted Markdown reads the same entry number as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- This is a material row-level conflict, not a name variant. It changes child identity, birth date and time, birthplace, father, mother, informant, and all downstream relationship candidates.
- The Pulgar father field remains unresolved for proof review. Preserve the alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- Existing canonical wiki stubs for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` are relevant context only. They do not independently certify the contested row because at least some listed evidence is Entry 172-derived.
- No Dario-line bridge is supported by this staged draft. The record does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

## Evidence Reviewed

- Staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md`.
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Existing wiki pages: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`.

## Literal Source Readings

### Assigned Chunk / Source Packet

- Entry: `172`, registered `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk/source-packet reading, with final field form unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age `Veintiseis anos`, employee, resident at `Calle de Valdivia`.

### Current Converted Markdown

- Entry: `172`, registered `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `José Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`, age `Veinte i seis años`, employee, resident `En esta`.

## Hypotheses And Scores

| Rank | Hypothesis | Evidence Supporting | Conflicts / Limits | Identity Confidence | Conflict Severity | Evidence Quality | Conversion Confidence | Claim Probability | Relevance | Canonical Readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | The local artifacts are in a row-control or stale-conversion conflict. | The two derivative readings share the source package and entry number but disagree on nearly every substantive field. | Identity analysis cannot certify the image or repair conversion output. | 0.80 | 0.95 | 0.70 | 0.35 | 0.84 | 0.92 | 0.10 |
| 2 | Entry `172` is the Pulgar/Arriagada birth of `Jose del Carmen Segundo Pulgar Arriagada`. | The staged draft, source packet, and current chunk agree on the Pulgar/Arriagada row. | The current converted Markdown reads a different Burgos/de la Cruz row for the same entry. | 0.68 | 0.95 | 0.62 | 0.35 | 0.58 | 0.92 | 0.08 |
| 3 | Entry `172` is the Burgos/de la Cruz birth of `Jose Miguel`. | The current converted Markdown explicitly gives this reading. | It conflicts with the staged draft, source packet, and chunk. It has low Pulgar-line relevance if controlling. | 0.42 | 0.95 | 0.45 | 0.35 | 0.36 | 0.18 | 0.05 |
| 4 | `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` are unresolved readings of one father field. | The staged draft requires these alternatives; the chunk reads `Jose del Carmen Pulgar S.`. | Not enough to normalize or merge the father candidate with any canonical `Jose del Carmen Pulgar` profile. | 0.55 | 0.70 | 0.55 | 0.35 | 0.52 | 0.80 | 0.08 |
| 5 | `Juana Arriagada de Pulgar` is the mother if the Pulgar row controls. | The assigned chunk/source packet name her as mother; a wiki page carries Entry 172-derived evidence. | Dependent on row-control QA; wiki evidence should not bootstrap the same claim. | 0.66 | 0.80 | 0.58 | 0.35 | 0.56 | 0.86 | 0.08 |
| 6 | `Jose del Carmen Segundo Pulgar Arriagada` is the same person as a Dario Pulgar candidate. | Only broad surname-family context could justify a later double-check. | No Dario, Arturo, Smith, adult identity, descendant, or chronology bridge appears in this staged draft. | 0.04 | 0.80 | 0.25 | 0.35 | 0.03 | 0.35 | 0.00 |

## Pulgar-Line Comparison

| Candidate | Evidence In This Task | Assessment | Probability |
| --- | --- | --- | ---: |
| `Dario Arturo Pulgar-Smith` | Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry 172 does not name Dario, Arturo, Smith, Alexander, or any relationship to him. | No merge, attachment, or variant conclusion supported. Needs a reviewed identity bridge before any use. | 0.02 |
| `Dario Arturo Pulgar` | Other staged CV contexts may use this document-level name, but this entry does not. | No same-person support from Entry 172. Requires a separate proof review using an identity-bearing source that links this person to the Entry 172 family. | 0.02 |
| `Dario Jose Pulgar-Arriagada` | The Pulgar reading names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose Pulgar-Arriagada`. | Name overlap is insufficient; no chronology, parentage, occupation, or place bridge is supplied here. | 0.03 |
| `Dario/Dario Pulgar Arriagada` | Existing wiki context includes `Darío Pulgar Arriagada` with a 2000 expropriation event. | If Entry 172 is Pulgar-controlled, it concerns an 1888 birth for a differently named child. Do not merge by surname pattern. | 0.01 |
| `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` | The Pulgar reading names this father candidate. Existing wiki context has another child relationship for a `Jose del Carmen Pulgar` candidate. | Treat as parent-candidate evidence only after targeted row-control QA and father-field certification. | 0.52 |
| `Juana Arriagada de Pulgar` | The Pulgar reading directly names her as mother. Existing wiki page has Entry 172-derived child evidence. | Plausible if the Pulgar row controls; not independently established while conversion conflict remains. | 0.56 |

## Conflicts

- Same-person conflict: no evidence supports treating `Jose del Carmen Segundo Pulgar Arriagada` and `José Miguel` as the same child.
- Duplicate-person conflict: do not create, merge, or rename people from this record until row-control QA is complete.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must not be silently normalized to `Jose del Carmen Pulgar`.
- Relationship conflict: the Pulgar reading gives parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted Markdown gives parents `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Chronology conflict: the Pulgar reading gives birth `1888-03-08 15:00`; the converted Markdown gives birth `1888-04-06 22:00`.

## Recommended Next Action

Keep the staged draft at `hold_for_conversion_qa`. The exact next step is targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`: compare the source image, current converted Markdown, current chunk, and staged source packet; decide whether the controlling entry `172` row is Pulgar/Arriagada or Burgos/de la Cruz; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent candidate, or Dario-line bridge. Do not attach this record to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` without a later reviewed source that explicitly bridges names, dates, relationships, and life context.
