---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
worker: postconv-identity-analysis-20260525205449265
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: blocked
---

# Identity/Conflict Analysis: Entry 172 Row Conflict

This note analyzes the staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md`.

## Blockers First

1. The assigned chunk and the assigned converted Markdown disagree on the entire row-level identity for entry 172. The chunk/source-packet line supports `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the assigned converted Markdown supports `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
2. This is not a spelling, abbreviation, or name-order variant. It is an incompatible child identity, parent identity, birth-date, residence, and source-row conflict.
3. The father field has a specific unresolved reading requirement: QA must certify whether it reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Existing canonical pages already contain low-confidence Pulgar/Arriagada evidence derived from this chunk cluster, including `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`. This task cannot safely strengthen those pages while the derivative row conflict remains unresolved.
5. No Dario-line merge or relationship inference is supported by this exact entry. The Dario names in existing wiki/staging context are relevant only as anti-conflation checks.

## Literal Evidence

From the assigned chunk and source packet:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, `a las tres de la tarde`, `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.`; Chilean; employee; resident at `Calle de Colipí`.
- Mother field: `Juana Arriagada de Pulgar`; Chilean; `Su sexo`; resident at `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employee, resident at `Calle de Valdivia`.

From the assigned converted Markdown:

- Entry number: `172`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, `a las diez de la noche`, `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

Interpretation is intentionally held: the literal derivative readings cannot both describe the same entry 172 row.

## Hypotheses And Scores

| Rank | Hypothesis | Identity confidence | Conflict severity | Evidence quality | Conversion confidence | Claim probability | Relevance | Canonical readiness |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | The controlling entry 172 is the Pulgar/Arriagada row, with child `Jose del Carmen Segundo Pulgar Arriagada` and parents `Jose del Carmen Pulgar S.` / `Juana Arriagada de Pulgar`. | 0.58 | 0.92 | 0.70 | 0.42 | 0.58 | 0.95 | 0.10 |
| 2 | The controlling entry 172 is the Burgos/de la Cruz row, with child `Jose Miguel` and parents `Oswaldo Burgos` / `Concepcion de la Cruz`. | 0.38 | 0.92 | 0.55 | 0.35 | 0.38 | 0.20 | 0.05 |
| 3 | The two derivative files are describing different source images or page states under the same entry-172 assignment. | 0.72 | 0.95 | 0.75 | 0.30 | 0.72 | 0.90 | 0.05 |
| 4 | `Jose del Carmen Segundo Pulgar Arriagada` is a child of `Jose del Carmen Pulgar`/`Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. | 0.50 | 0.80 | 0.62 | 0.42 | 0.50 | 0.95 | 0.08 |
| 5 | Entry 172 supplies identity or relationship evidence for any Dario Pulgar candidate. | 0.03 | 0.75 | 0.35 | 0.42 | 0.03 | 0.30 | 0.00 |

Score rationale: the chunk and source packet are internally consistent for the Pulgar/Arriagada row and match existing staged Pulgar work, but the assigned converted file directly contradicts them. Until targeted conversion QA resolves which derivative is controlling, identity confidence and canonical readiness remain low.

## Evidence By Hypothesis

### H1: Pulgar/Arriagada Row Controls

Supporting evidence:

- The assigned chunk transcribes page 58 entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`.
- The staged source packet repeats that row and marks family relevance high because it names a Pulgar child and Arriagada mother in a civil birth register.
- Existing canonical stubs for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` contain evidence snapshots tied to this chunk/source-packet cluster.

Conflicts and limits:

- The assigned converted Markdown gives a completely different row for entry 172.
- The father suffix/mark after `Pulgar` is not certified.
- The existing canonical evidence remains low-confidence or draft/probable and should not be strengthened by this task.

### H2: Burgos/de la Cruz Row Controls

Supporting evidence:

- The assigned converted Markdown explicitly records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- It includes a coherent row with child, parents, birth time, place, and informant.

Conflicts and limits:

- The assigned chunk and new staged source packet contradict the converted Markdown in every identity-bearing field.
- The staged conflict draft already classifies this as a row-level conversion conflict and recommends holding for conversion QA.
- No existing Pulgar-line canonical attachment should rely on the Burgos/de la Cruz reading.

### H3: Assignment Or Derivative-State Mismatch

Supporting evidence:

- The chunk and converted file share the same converted SHA metadata but preserve incompatible row content.
- The page metadata and row numbers look structurally similar, which raises the possibility of source-image, conversion-state, or derivative assignment drift rather than a genealogical identity conflict.

Conflicts and limits:

- Identity analysis cannot resolve a derivative assignment problem without conversion QA.
- The output of this hypothesis is not a person merge; it is a targeted conversion review request.

### H4: Jose/Juana Parent Candidate Cluster

Supporting evidence:

- The Pulgar/Arriagada reading names father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing wiki pages include `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, and `Juana Arriagada de Pulgar`.
- Existing wiki context also shows `Jose del Carmen Pulgar` connected to a separate child candidate, `Tulio Cesar Luis Jose`, from another draft relationship.

Conflicts and limits:

- The `S.` after `Pulgar` may be a suffix, abbreviated second surname, or uncertain mark; it cannot be silently normalized away.
- `Juana Arriagada de Pulgar` in this row should not be automatically equated with other Juana candidates, including any `Juana de Dios ... de Pulgar`, without a separate parent-candidate proof review.
- If the Burgos/de la Cruz row controls, the Jose/Juana parent claim for entry 172 fails for this source.

### H5: Dario-Line Candidate Or Name-Variant Bridge

Supporting evidence:

- Existing wiki/staged context contains several Pulgar-line candidates that must be guarded against conflation: `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, `Dario Pulgar A.`, and canonical `Darío Pulgar Arriagada`.
- The broader surname/context overlap justifies checking that this entry is not misused as Dario-line proof.

Conflicts and limits:

- This entry does not name Dario, Arturo, Jose as a Dario middle-name cluster, Pulgar-Smith, or any Dario spouse/child/parent relationship.
- `Dario Arturo Pulgar-Smith` is currently family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merges with similarly named Pulgar records.
- `Dario Arturo Pulgar` appears in CV staging as a document-level subject, with a separate unresolved bridge to `Dario Arturo Pulgar-Smith`.
- `Dario Jose Pulgar-Arriagada` and `Dario J. Pulgar Arriagada` are represented in local staged/photo/title contexts, but those do not connect to entry 172.
- Canonical `Darío Pulgar Arriagada` is supported by a 2000 expropriation-event snapshot, not by this 1888 birth-entry conflict.

## Conflict Assessment

- Same-person conflict: unresolved only between the row-level person candidates created by derivative readings. `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` should be treated as competing readings for entry 172, not as the same person.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is merged into `Jose del Carmen Pulgar` without resolving the suffix/mark and comparing other Jose parent evidence.
- Name-variant conflict: `Pulgar S.` versus `Pulgar` is unresolved; `Juana Arriagada de Pulgar` should remain literal.
- Relationship conflict: high. The child-parent relationship is Pulgar/Arriagada under one reading and Burgos/de la Cruz under the other.
- Chronology conflict: high. The Pulgar/Arriagada reading gives birth on 1888-03-08 at 3 p.m.; the converted Markdown gives 1888-04-06 at 10 p.m.
- Dario-line conflict: no positive bridge. Treat all Dario candidates as separate or unresolved for this task.

## Ranked Pulgar-Line Comparison

| Rank | Candidate / cluster | Current relationship to this staged draft | Probability for attachment from this evidence | Required next step |
| ---: | --- | --- | ---: | --- |
| 1 | `Jose del Carmen Segundo Pulgar Arriagada` | Direct child candidate if Pulgar/Arriagada row controls. | 0.58 | Conversion QA for row identity and proof review for child name/date/parents. |
| 2 | `Juana Arriagada de Pulgar` | Direct mother candidate if Pulgar/Arriagada row controls. | 0.55 | Conversion QA plus parent-candidate proof review; preserve literal married-name form. |
| 3 | `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` | Direct father candidate only under Pulgar/Arriagada row. | 0.50 | Targeted image reread of father field, then Jose parent-candidate comparison across records. |
| 4 | `Dario Arturo Pulgar-Smith` | Existing family-supplied maternal-grandfather page; no direct evidence in entry 172. | 0.02 | Separate identity bridge source; do not attach entry 172. |
| 5 | `Dario Arturo Pulgar` | Existing CV document-level subject; no direct evidence in entry 172. | 0.02 | Separate CV identity bridge review; do not attach entry 172. |
| 6 | `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` | Separate staged/photo/title cluster; no direct evidence in entry 172. | 0.03 | Separate proof review comparing full name, profession, dates, and parent evidence. |
| 7 | `Dario/Dario Pulgar Arriagada` / canonical `Darío Pulgar Arriagada` | Separate legal/property/expropriation context; no direct evidence in entry 172. | 0.02 | Separate identity bridge with vital-date or relationship continuity. |

## Recommendation

Hold this conflict for targeted conversion QA. The exact next step is to compare the source image, assigned converted Markdown, assigned chunk, and staged source packet for `CHUNK-b8f4f0490a36-P0001-01`, then certify the controlling row for entry 172 and the exact father-field reading: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review before promoting any child birth-name, birth date/time/place, registration date, sex, father, mother, informant, or child-parent relationship claim. If the Pulgar/Arriagada row is confirmed, run a separate Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, or any other Jose/Juana candidates across records. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada` without a later proof-reviewed bridge source.
