---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526045956374
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

- The controlling entry `172` row is unresolved. The staged conflict draft and held source packet preserve a Pulgar/Arriagada reading, while the current converted Markdown preserves a Burgos/de la Cruz reading for the same entry number.
- This is not a spelling, accent, or name-variant issue. The competing readings change the child, sex label, birth date and time, birth place, father, mother, informant, and downstream relationships.
- The Pulgar father field is not certified. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as alternative readings until targeted conversion QA decides the field.
- Existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` are context only. Their Entry 172-derived evidence cannot be used to bootstrap the contested row.
- No Dario-line bridge is supported by this staged conflict draft. It does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md`.
- Held source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Existing wiki context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/dario-arturo-pulgar-smith.md`, and `wiki/people/dar-o-pulgar-arriagada.md`.

## Literal Readings

### Assigned Chunk / Held Source Packet

- Entry `172`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father `Jose del Carmen Pulgar S.` in the chunk/source-packet reading, with the final suffix or mark unresolved for proof-review use.
- Mother `Juana Arriagada de Pulgar`.
- Informant `Ernesto Herrera L.`, present at birth, age `Veintiseis anos`, employee, domiciled `Calle de Valdivia`.

### Current Converted Markdown

- Entry `172`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child `José Miguel`; sex `Varon`.
- Birth `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Father `Oswaldo Burgos`.
- Mother `Concepcion de la Cruz`.
- Informant `Oswaldo Burgos`, age `Veinte i seis años`, employee, domiciled `En esta`.

## Hypotheses

| Rank | Hypothesis | Evidence Supporting | Conflicts / Limits | Identity Confidence | Conflict Severity | Evidence Quality | Conversion Confidence | Claim Probability | Relevance | Canonical Readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | The artifacts preserve a row-control or stale-conversion conflict. | Same source package and entry number produce two incompatible derivative readings. | Identity analysis cannot certify the source image or repair conversion output. | 0.82 | 0.95 | 0.70 | 0.35 | 0.86 | 0.92 | 0.10 |
| 2 | Entry `172` is the Pulgar/Arriagada birth of `Jose del Carmen Segundo Pulgar Arriagada`. | Staged conflict draft, held source packet, and current chunk agree on the Pulgar/Arriagada row. | Current converted Markdown reads the same entry as a Burgos/de la Cruz row. | 0.68 | 0.95 | 0.62 | 0.35 | 0.58 | 0.92 | 0.08 |
| 3 | Entry `172` is the Burgos/de la Cruz birth of `José Miguel`. | Current converted Markdown explicitly gives this row. | Conflicts with staged draft, held source packet, and current chunk; low Pulgar-line relevance if controlling. | 0.42 | 0.95 | 0.45 | 0.35 | 0.36 | 0.18 | 0.05 |
| 4 | `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` are unresolved readings of one father field. | Pulgar reading names a father candidate; task requires preserving all alternatives. | Insufficient to normalize or merge with canonical `Jose del Carmen Pulgar`. | 0.55 | 0.70 | 0.55 | 0.35 | 0.52 | 0.80 | 0.08 |
| 5 | `Juana Arriagada de Pulgar` is the mother if the Pulgar row controls. | Pulgar reading directly names her as mother; existing wiki page carries Entry 172-derived context. | Fully dependent on row-control QA; wiki page is not independent evidence. | 0.66 | 0.80 | 0.58 | 0.35 | 0.56 | 0.86 | 0.08 |
| 6 | `Jose del Carmen Segundo Pulgar Arriagada` is the same person as a Dario Pulgar candidate. | Only broad Pulgar/Arriagada family-context overlap exists. | No Dario, Arturo, Smith, adult chronology, relationship bridge, or descendant clue appears in this task. | 0.04 | 0.80 | 0.25 | 0.35 | 0.03 | 0.35 | 0.00 |

## Pulgar-Line Comparison

| Candidate | Evidence In This Task | Assessment | Probability |
| --- | --- | --- | ---: |
| `Dario Arturo Pulgar-Smith` | Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry 172 does not name Dario, Arturo, Smith, Alexander, or a relationship to him. | Do not attach, merge, or treat as a name variant from this evidence. Needs a proof-reviewed identity bridge. | 0.02 |
| `Dario Arturo Pulgar` | Other staged CV contexts may use this document-level name, but Entry 172 does not. | No same-person support from this staged draft. Needs a separate identity-bearing source and proof review. | 0.02 |
| `Dario Jose Pulgar-Arriagada` | This task's Pulgar reading names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose Pulgar-Arriagada`. | Name-family overlap is insufficient; no chronology, parentage, occupation, or place bridge is supplied here. | 0.03 |
| `Dario/Darío Pulgar Arriagada` | Existing wiki context includes `Darío Pulgar Arriagada` with a 2000 expropriation event. | If Entry 172 is Pulgar-controlled, it concerns an 1888 birth for a differently named child. Do not merge by surname pattern. | 0.01 |
| `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` | Pulgar reading names this father candidate; existing wiki context has a `Jose del Carmen Pulgar` page with a separate child relationship. | Treat only as a parent candidate until row-control QA and father-field certification are complete. | 0.52 |
| `Juana Arriagada de Pulgar` | Pulgar reading directly names her as mother. Existing wiki page has Entry 172-derived child evidence. | Plausible if the Pulgar row controls; not independently established while conversion conflict remains. | 0.56 |

## Conflicts

- Same-person conflict: no evidence supports treating `Jose del Carmen Segundo Pulgar Arriagada` and `José Miguel` as the same child.
- Duplicate-person conflict: do not create, merge, or rename people from this record while row-control remains unresolved.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must not be silently normalized to `Jose del Carmen Pulgar`.
- Relationship conflict: the Pulgar reading gives parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted Markdown gives parents `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Chronology conflict: the Pulgar reading gives birth `1888-03-08 15:00`; the converted Markdown gives birth `1888-04-06 22:00`.

## Recommended Next Action

Keep this staged conflict on `hold_for_conversion_qa`. The exact next step is targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`: compare the source image, current converted Markdown, current chunk, and held source packet; decide whether entry `172` is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent candidate, same-person claim, or Dario-line bridge. Do not attach this evidence to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` without a later reviewed source that explicitly bridges names, dates, relationships, and life context.
