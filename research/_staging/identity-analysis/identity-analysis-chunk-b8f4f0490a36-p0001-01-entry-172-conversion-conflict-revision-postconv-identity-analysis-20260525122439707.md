---
type: identity_analysis
status: draft
worker: postconv-identity-analysis-20260525122439707
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
role: identity_researcher
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Conversion Conflict

This note analyzes the staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md`.

## Blockers First

1. The assigned converted Markdown and the current chunk/source-packet reading disagree on the person recorded in entry 172. This is a row-level conversion or file-assignment conflict, not a spelling variant.
2. The controlling entry cannot be promoted until targeted conversion QA certifies whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row.
3. If the Pulgar/Arriagada row is certified, the father-field ending remains unresolved as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Existing wiki context already contains promoted or staged Pulgar-line pages. That context is relevant for anti-conflation review, but it cannot silently correct this row-level conflict.
5. No evidence in this staged conflict draft names Dario. Do not attach this entry to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Darío Pulgar Arriagada, or Dario passenger stubs by surname alone.

## Literal Source Readings

The staged source packet and current chunk read entry 172 as:

- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father: chunk reads `Jose del Carmen Pulgar S.`; source-packet uncertainty keeps the final element open.
- Mother: `Juana Arriagada de Pulgar`.
- Parent residence: `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at the birth.

The assigned converted Markdown reads entry 172 as:

- Child: `José Francisco` / `Jose Francisco`.
- Birth: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho`, at `En esta`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.

## Hypotheses

| Rank | Hypothesis | Supporting evidence | Conflicting or limiting evidence | Probability | Required next step |
| ---: | --- | --- | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | The current chunk and staged source packet agree on the Pulgar/Arriagada row and provide full child, parent, date, place, and informant fields. Existing canonical wiki pages also reflect a scoped promoted mother-child relationship from earlier proof review. | The assigned converted Markdown for the same file records an unrelated Gomez/de la Cruz child under entry 172. Father suffix is unresolved. | 0.62 | Targeted conversion QA against the source image must certify the controlling row and father-field ending; then rerun proof review for child identity, birth facts, and parent relationships. |
| 2 | Entry 172 is the Gomez/de la Cruz birth registration for `Jose Francisco`. | The assigned converted Markdown explicitly records `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born 26 March 1888. | The current chunk and staged source packet contradict this and identify the page/row as Pulgar/Arriagada. The conflict draft classifies this as row-level conflict. | 0.20 | Conversion QA must determine whether the converted Markdown is from a different row/source or whether the chunk/source-packet reading is misassigned. |
| 3 | `Jose del Carmen Segundo Pulgar Arriagada` is a child of `Juana Arriagada de Pulgar`. | Literal Pulgar/Arriagada row names the mother. Existing `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, and `research/relationships/chunk-b8f4f0490a36-p0001-01-003-child-mother-juana-arriagada-de-pulgar-parent.md` preserve a scoped probable mother-child link. | Current staged conflict reopens conversion confidence because the assigned converted Markdown disagrees at row level. | 0.58 for this staged draft; 0.97 in prior scoped relationship page if QA confirms the Pulgar row | Do not expand or re-promote from this draft until conversion QA closes the row conflict. |
| 4 | The father candidate is canonical/stub `Jose del Carmen Pulgar`. | The Pulgar/Arriagada row names father as `Jose del Carmen Pulgar` with possible suffix. Existing `wiki/people/jose-del-carmen-pulgar.md` has a separate draft child link to Tulio Cesar Luis Jose, showing a same-name parent candidate in the wiki context. | Same-name evidence alone does not prove this entry's father is the same Jose del Carmen Pulgar as the Tulio-related candidate. The final `S.` may be an identity-relevant abbreviated element. | 0.42 | After conversion QA, run a separate Jose parent-candidate identity proof review comparing full name, spouse/mother name, residence, chronology, and child evidence. |
| 5 | The mother candidate is the same as another Juana candidate, including `Juana de Dios Amagada de Pulgar`. | Existing wiki has `Juana Arriagada de Pulgar` for this row and `Juana de Dios Amagada de Pulgar` as a separate Tulio-related draft parent candidate. Both are Pulgar-associated married-style mother names. | The names differ materially: `Arriagada` versus `de Dios Amagada`; the staged draft gives no evidence that they are variants of one person. | 0.18 | Preserve separate candidates until a source-specific proof review compares original spellings, spouse, child, residence, and chronology. |
| 6 | This entry is evidence for Dario Arturo Pulgar-Smith. | Existing canonical context says Dario Arturo Pulgar-Smith is Alexander John Heinz's maternal grandfather and warns that Pulgar records require identity review. The surname/family line makes this worth a later check. | This staged draft does not name Dario, Arturo, Smith, Alexander John Heinz, or a grandparent relationship. | 0.05 | No promotion. Only revisit after conversion QA and a separate bridge source explicitly connects this Jose/Juana cluster to Dario Arturo Pulgar-Smith. |
| 7 | This entry is evidence for document-level CV subject `Dario Arturo Pulgar`. | Other staged CV notes preserve a document-level `Dario Arturo Pulgar` identity cluster. | Entry 172 names a Jose child and Jose/Juana parents, not Dario Arturo Pulgar. | 0.04 | Do not attach. Require explicit parentage or identity bridge from a reviewed local source. |
| 8 | This entry is evidence for `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, or similar Arriagada clusters. | The child surname is `Pulgar Arriagada`, so the row is relevant as an anti-conflation comparator for Pulgar-Arriagada names. | The given forenames are `Jose del Carmen Segundo`, not Dario or Dario Jose. Existing `Darío Pulgar Arriagada` context concerns a 2000 expropriation notice; other Dario Jose contexts are separate and metadata-dependent. | 0.08 | Preserve separately. Require a reviewed source that bridges given names, vital dates, parentage, occupation, or family continuity before any merge. |

## Conflict Analysis

- Same-person conflict: unresolved for the father `Jose del Carmen Pulgar` because the suffix and same-name candidate comparison are not settled.
- Duplicate-person risk: high if the Pulgar/Arriagada child, Jose parent, Juana parent, Dario CV cluster, Dario Jose cluster, and Darío Pulgar Arriagada cluster are merged by surname or broad family context.
- Name-variant conflict: `Jose del Carmen Segundo Pulgar Arriagada` is not a demonstrated variant of any Dario name in this draft.
- Relationship conflict: mother-child evidence is strong only if the Pulgar/Arriagada row is confirmed as the controlling entry 172. Father-child evidence must wait on the father-field suffix and row QA.
- Chronology conflict: no direct chronology conflict is proved between the 1888 birth row and Dario clusters because no Dario identity is named here. The row may later provide ancestor/relative evidence, but not without a bridge.
- Conversion conflict: severe. The current chunk/source packet and assigned converted Markdown describe different children, parents, dates, and places for entry 172.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.54 | The Pulgar/Arriagada row is internally detailed, but the assigned converted Markdown creates a controlling row-level conflict. |
| conflict_severity | 0.96 | Different child, father, mother, birth date, and place are recorded for the same entry number. |
| evidence_quality | 0.70 | Civil birth registration is high-quality evidence if row identity is certified; current derivative disagreement lowers usable quality. |
| conversion_confidence | 0.38 | The task's conversion artifacts disagree materially. |
| claim_probability | 0.62 | Best current hypothesis favors the Pulgar/Arriagada row, but promotion must wait for QA. |
| relevance | 0.88 | Directly relevant to Pulgar/Arriagada and Jose/Juana parent candidates; only indirect anti-conflation relevance to Dario clusters. |
| canonical_readiness | 0.10 | Hold for conversion QA; no merge, rename, or promoted fact should be made from this staged conflict note. |

## Recommended Next Action

Keep this staged conflict at `hold_for_conversion_qa`. The exact next proof-review or promotion step is:

1. Run targeted conversion QA on the source image, current chunk, and assigned converted Markdown to decide whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row.
2. In the same QA step, record the father field exactly as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. After QA, rerun proof review for the narrow child identity, birth facts, mother-child relationship, father-child relationship, and Jose/Juana parent-candidate comparison.
4. Only after those steps, perform any Pulgar-line bridge review comparing Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, canonical Darío Pulgar Arriagada, and the Jose/Juana parent candidates. Do not merge any of them by name alone.
