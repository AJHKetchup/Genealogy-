---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526045120066
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

- The controlling row for entry `172` is unresolved. The staged conflict draft and source packet report the assigned chunk reading as `Jose del Carmen Segundo Pulgar Arriagada`, while the current converted Markdown for the same source and entry number reads `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- This is not a same-person/name-variant conflict. It is a material row-level conversion conflict affecting child identity, sex wording, birth date and time, birth place, father, mother, informant, and downstream relationship candidates.
- The father field in the Pulgar/Arriagada reading remains unresolved for proof review: preserve alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- Existing canonical wiki pages already contain low-confidence Entry 172-derived stubs for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`; those should stay held and should not be treated as independent confirmation of the staged draft.
- No Dario-line merge or bridge is supported by this record as currently staged. The entry does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md`.
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Existing wiki context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/dario-arturo-pulgar-smith.md`, and `wiki/people/dar-o-pulgar-arriagada.md`.

## Literal Source Readings

### Assigned Chunk / Source Packet Reading

- Registration: entry `172`, registered `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.` in the chunk; proof-review alternatives remain `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age `Veintiseis anos`, employee, resident at `Calle de Valdivia`.

### Current Converted Markdown Reading

- Registration: entry `172`, registered `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `José Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`, age `Veinte i seis años`, employee, resident `En esta`.

## Hypotheses And Scores

| Rank | Hypothesis | Supporting Evidence | Conflicts / Limits | Identity Confidence | Conflict Severity | Evidence Quality | Conversion Confidence | Claim Probability | Relevance | Canonical Readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Entry `172` is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | The assigned chunk and staged source packet agree on child, parents, birth date, place, and informant. The source packet says the local image appears broadly consistent with this row but is not QA certification. | Current converted Markdown gives a wholly different Burgos/de la Cruz row for the same entry number. | 0.68 | 0.95 | 0.62 | 0.35 | 0.58 | 0.92 | 0.08 |
| 2 | Entry `172` is the Burgos/de la Cruz birth registration for `Jose Miguel`. | Current converted Markdown explicitly reads entry `172` this way. | Assigned chunk and staged source packet read a different row; family relevance to Pulgar/Arriagada disappears if this controls. | 0.42 | 0.95 | 0.45 | 0.35 | 0.36 | 0.18 | 0.05 |
| 3 | One derivative is misassigned or stale, and the source/chunk/converted-file references need QA reconciliation. | The two readings differ across nearly every row field while sharing entry number and date context, which is more consistent with assignment/conversion-row mismatch than ordinary transcription variation. | Identity researcher cannot run conversion or certify the image. | 0.78 | 0.95 | 0.70 | 0.35 | 0.82 | 0.90 | 0.10 |
| 4 | `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` are alternative readings of one father field. | The staged draft and source packet explicitly require these alternatives to remain open. | This is a field-reading problem, not proof that all forms are stable name variants or the same canonical person. | 0.55 | 0.70 | 0.55 | 0.35 | 0.52 | 0.80 | 0.08 |
| 5 | `Juana Arriagada de Pulgar` is the mother in the Pulgar/Arriagada row. | The assigned chunk and source packet name her as mother; existing wiki stub carries an Entry 172-derived probable child link. | Dependent on confirming the Pulgar/Arriagada row; wiki stub is derivative and should not bootstrap confidence. | 0.66 | 0.80 | 0.58 | 0.35 | 0.56 | 0.86 | 0.08 |
| 6 | `Jose del Carmen Segundo Pulgar Arriagada` is a same-person candidate for a Dario Pulgar identity. | Shared Pulgar/Arriagada surname pattern may justify later review if independent bridge evidence appears. | This entry does not name Dario, Arturo, Smith, adult occupation, spouse, descendants, Geneva/medical context, or a date bridge. | 0.04 | 0.80 | 0.25 | 0.35 | 0.03 | 0.35 | 0.00 |

## Pulgar-Line Comparison

| Candidate | Evidence From This Task | Assessment | Probability |
| --- | --- | --- | ---: |
| `Dario Arturo Pulgar-Smith` | Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry 172 does not name Dario, Arturo, Smith, Alexander, or a family relationship to him. | No merge or attachment supported. Needs a reviewed identity bridge tying any Entry 172 person to canonical Pulgar-Smith. | 0.02 |
| `Dario Arturo Pulgar` | Local staged context elsewhere has CV/document-level sources for this name, but this Entry 172 task does not mention Dario Arturo. | No same-person support from this record. Requires a later proof review with an identity-bearing source linking `Dario Arturo Pulgar` to the Entry 172 family, if such evidence exists locally. | 0.02 |
| `Dario Jose Pulgar-Arriagada` | The possible child in the Pulgar row is `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose Pulgar-Arriagada`. | Name overlap is insufficient; no chronology, parentage, occupation, or place bridge is supplied here. | 0.03 |
| `Dario/Darío Pulgar Arriagada` | Existing wiki `Darío Pulgar Arriagada` has a 2000 expropriation event. Entry 172, if Pulgar-controlled, would concern an 1888 birth for a differently named child. | Strong chronology and identity caution. Do not merge by surname pattern. | 0.01 |
| `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` | The Pulgar reading names this father candidate, but the suffix/mark is unresolved. Existing `Jose del Carmen Pulgar` wiki page has other child evidence for `Tulio Cesar Luis Jose`, not direct proof for this Entry 172 row. | Treat as a parent candidate only after targeted row-control QA and father-field certification. | 0.52 |
| `Juana Arriagada de Pulgar` | The Pulgar reading directly names her as mother. Existing wiki page has Entry 172-derived child evidence. | Plausible parent candidate if Pulgar row controls; not independently proved while conversion conflict remains. | 0.56 |

## Conflicts

- Same-person conflict: no evidence supports treating `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` as the same child.
- Duplicate-person conflict: existing canonical stubs should not be duplicated or merged further until row-control QA decides which Entry 172 row is valid for this source package.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must not be silently normalized to `Jose del Carmen Pulgar`; the final suffix or mark is unresolved.
- Relationship conflict: Pulgar reading gives parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; converted Markdown gives parents `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Chronology conflict: Pulgar reading gives birth `1888-03-08 15:00`; converted Markdown gives birth `1888-04-06 22:00`.

## Recommended Next Action

Keep this staged draft at `hold_for_conversion_qa`. The exact next proof-review/promotion step is targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`: compare the source image, current converted Markdown, current chunk, and staged source packet; decide whether the controlling entry `172` row is the Pulgar/Arriagada row or the Burgos/de la Cruz row; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent candidate, or Dario-line bridge. Do not merge or attach this record to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` without a later reviewed source that explicitly bridges names, dates, relationships, and life context.
