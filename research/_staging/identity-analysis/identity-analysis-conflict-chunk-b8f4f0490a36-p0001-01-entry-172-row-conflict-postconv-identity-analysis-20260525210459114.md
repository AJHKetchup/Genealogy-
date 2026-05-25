---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525210459114
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

# Identity And Conflict Analysis: Entry 172 Row-Level Conflict

## Blockers

- The exact staged conflict draft reviewed is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md`.
- The assigned chunk and assigned converted Markdown disagree about the same entry number. The chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the converted Markdown records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This is a material row-level conversion conflict, not a same-person, duplicate-person, or name-variant conflict. No child identity, parent-child relationship, or birth-event claim is canonical-ready until targeted conversion QA selects the controlling row or supersedes the conflicting derivative file.
- The father field in the Pulgar/Arriagada reading is not settled. Existing staged notes require QA to decide among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- The entry does not name Dario, Arturo, Smith, Dario Jose, or Dario Pulgar Arriagada. It cannot bridge `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` to this 1888 birth row.
- Existing wiki stubs already contain some entry-172-derived evidence snapshots, but this analysis does not promote, merge, rename, or correct those pages. The current staged conflict should remain a hold signal until conversion QA and proof review are complete.

## Literal Evidence

From the assigned chunk:

- Entry number and registration date: `172`; `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child reading: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth reading: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Parent reading: father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; both listed as Chilean and resident at `Calle de Colipí`.
- Informant reading: `Ernesto Herrera L.`, present at birth, age 26, employed, resident at `Calle de Valdivia`.

From the assigned converted Markdown:

- Entry number and registration date: `172`; `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child reading: `José Miguel`; sex `Varon`.
- Birth reading: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Parent reading: father `Oswaldo Burgos`; mother `Concepcion de la Cruz`.

The source packet for this task states that the source image aligns at a high level with the Pulgar/Arriagada row, but it also records low conversion confidence because the derivative transcriptions conflict.

## Hypotheses

| rank | hypothesis | probability | identity confidence | evidence support | required next step |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | Entry 172 is probably the Pulgar/Arriagada birth row, but not promotion-ready. | 0.72 | 0.66 | The assigned chunk and task source packet support `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar S.`, and `Juana Arriagada de Pulgar`; prior reviewed notes also describe the visible image as supporting the broad Pulgar/Arriagada row. | Targeted conversion QA must certify the controlling row and father-field reading, then rerun proof review. |
| 2 | The converted Markdown's Burgos/de la Cruz reading is the controlling entry 172. | 0.18 | 0.25 | The assigned converted Markdown contains this reading, but it conflicts with the assigned chunk, source packet, and staged conflict draft. | Conversion QA must explain whether the converted Markdown is from the wrong row/image assignment or whether the current chunk should be superseded. |
| 3 | `Jose del Carmen Pulgar` in this row is the same person as canonical `wiki/people/jose-del-carmen-pulgar.md`. | 0.35 | 0.30 | Name overlap is present. The canonical page currently has a separate probable child link to Tulio Cesar Luis Jose, but this row's father suffix and row control are unresolved. | After conversion QA, run parent-candidate proof review comparing father name, residence, spouse/mother context, chronology, and any reviewed local sources. |
| 4 | `Juana Arriagada de Pulgar` in this row is the mother of `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | 0.62 | The chunk and source packet explicitly read her as mother in the Pulgar/Arriagada hypothesis; the canonical stub already has an entry-172-derived probable child link. | After conversion QA, proof-review the mother-child relationship as a narrow civil-registration claim. |
| 5 | This entry supports a same-person bridge to any Dario Pulgar identity cluster. | 0.02 | 0.03 | No Dario name, Arturo middle name, Smith surname, Dario Jose form, medical title, passenger detail, spouse, descendant, or chronology bridge appears in this entry. | Do not use this row for Dario-line attachment unless a later proof-reviewed source explicitly connects the Jose/Juana family to a Dario candidate. |

## Required Pulgar-Line Comparison

`Dario Arturo Pulgar-Smith`: Existing canonical page is family-supplied and warns not to attach similarly named Pulgar records without identity review. Entry 172 does not name Dario Arturo, Smith, a child, spouse, grandchild, or Alexander John Heinz. Same-person or lineage bridge from this row is unsupported.

`Dario Arturo Pulgar`: Local staged CV materials concern a document-level subject named Dario Arturo Pulgar, but this 1888 birth row does not name Dario or Arturo and provides no CV, occupation, age, or relationship bridge. No merge or attachment should be made.

`Dario Jose Pulgar-Arriagada`: The entry-172 child is read as `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. Shared Pulgar/Arriagada surnames are family-context hints only. They justify future double-checking after QA, not a silent correction or merge.

`Dario/Dario Pulgar Arriagada`: Existing canonical/staged context includes a separate `Darío Pulgar Arriagada` cluster. Entry 172 does not state Dario and is separated by unresolved row control and lack of chronology bridge. Same-person probability from this entry alone is near zero.

Jose/Juana parent candidates: Under the Pulgar/Arriagada hypothesis, `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` are candidate parents for the entry-172 child. The father candidate is more blocked than the mother candidate because the final suffix/mark is unresolved and the existing `Jose del Carmen Pulgar` canonical page points to another child from different staged evidence. The mother candidate is directly named in the chunk, but still depends on row-control QA.

## Conflicts

- Same-entry conflict: Pulgar/Arriagada row versus Burgos/de la Cruz row for entry 172.
- Relationship conflict risk: Promoting either row before QA could attach a child to the wrong parents.
- Name-variant risk: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` must remain distinct readings until the father field is certified.
- Duplicate-person risk: Existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Pulgar` should not be treated as resolved duplicates or fully proved relationships from this conflicted draft.
- Chronology conflict: None established from this entry alone. The issue is transcription/row control, not an impossible date sequence.
- Dario-line conflation risk: High if `Pulgar Arriagada` surname overlap is used to connect this entry to Dario candidates without a reviewed bridge source.

## Scores

| factor | score / value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | The Pulgar/Arriagada child-parent cluster is probable from staged chunk/source-packet context, but row-level conflict blocks a firm conclusion. |
| conflict_severity | 0.95 | The conflict changes the child, parents, birth details, and family line. |
| evidence_quality | 0.78 | Civil birth registration is a strong source type, and the source packet reports image support; derivative conflict reduces usable quality. |
| conversion_confidence | 0.35 | Assigned chunk and converted Markdown materially disagree. |
| claim_probability | 0.72 | Probable that the staged Pulgar/Arriagada row is relevant, but not yet proof-ready. |
| relevance | 0.98 | All reviewed materials directly concern the exact staged conflict draft, source packet, chunk id, page reference, and entry number. |
| canonical_readiness | 0.10 | Hold for targeted conversion QA and later proof review. |

## Recommended Next Action

Keep this staged conflict on `hold_for_conversion_qa`. The exact next step is targeted conversion QA for page 58, entry 172 to decide the controlling row and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting any child identity, parent-child relationship, parent-candidate merge, or Dario-line comparison.
