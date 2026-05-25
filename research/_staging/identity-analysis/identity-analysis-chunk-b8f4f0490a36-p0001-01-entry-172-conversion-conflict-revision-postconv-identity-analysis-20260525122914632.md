---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525122914632
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
analysis_status: hold
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conflict

## Blockers

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md`.
- The assigned converted Markdown and the current chunk are mutually exclusive for entry 172. This is a row-level conversion or assignment conflict, not a spelling variant.
- The current chunk/source-packet reading identifies entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`.
- The assigned converted Markdown identifies entry 172 as `Jose Francisco`, child of `Oswaldo Gomez` and `Emilia de la Cruz`.
- The father field after `Jose del Carmen Pulgar` is unresolved. Current local evidence preserves `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as open readings until targeted conversion QA.
- Existing canonical pages already contain low-confidence or draft Pulgar/Juana evidence from this chunk family. Those pages must not be treated as independent corroboration while the row-level conflict remains open.
- No external research was performed. No raw sources, converted Markdown, chunks, or canonical wiki pages were edited.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Hypothesis: the controlling row for register entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`.

Literal evidence:

- The staged conflict draft states that the current chunk and image-reviewed evidence support entry 172 as a Pulgar/Arriagada birth registration.
- The source packet for this exact worker records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The chunk records father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, parent residence `Calle de Colipí`, and informant `Ernesto Herrera L.`.
- Existing canonical stubs for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` reflect this Pulgar/Arriagada cluster, but their evidence snapshots keep relationship and claim confidence low or unknown.

Interpretation:

- This is the strongest family-relevant reading if the current chunk is the correct row transcription.
- It is not ready for canonical promotion because the assigned converted Markdown points to a different entry 172 and the father suffix remains unresolved.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.72 | The chunk/source-packet reading is internally specific, but derivative records conflict. |
| conflict_severity | 0.94 | The competing row names different child, parents, date, place, and informant context. |
| evidence_quality | 0.62 | Current chunk is detailed and source-linked; conversion conflict prevents treating it as settled. |
| conversion_confidence | 0.42 | Mixed: chunk supports Pulgar/Arriagada, assigned converted Markdown does not. |
| claim_probability | 0.68 | Probable enough to preserve as a candidate, not enough to promote. |
| relevance | 1.00 | Directly addresses the staged conflict. |
| canonical_readiness | 0.08 | Hold for targeted conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Hypothesis: the controlling row for register entry 172 is the converted-file row for `Jose Francisco`, child of `Oswaldo Gomez` and `Emilia de la Cruz`.

Literal evidence:

- The assigned converted Markdown records entry 172 as `Jose Francisco`, sex `Varon`, born `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`, at `En esta`.
- The same converted Markdown records father `Oswaldo Gomez`, mother `Emilia de la Cruz`, and compareciente `Oswaldo Gomez`.
- The staged conflict draft explicitly preserves this as the competing converted Markdown reading.

Interpretation:

- This reading cannot be dismissed silently because it is in the assigned converted file for the same source path.
- It currently looks less compatible with the source packet and current chunk, so the safest treatment is a competing row-assignment hypothesis pending QA.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.34 | Supported by the converted Markdown, contradicted by current chunk/source-packet evidence. |
| conflict_severity | 0.94 | If true, all Pulgar/Arriagada entry-172 claims are attached to the wrong row. |
| evidence_quality | 0.40 | Single derivative layer conflicts with chunk and staged image-reviewed notes. |
| conversion_confidence | 0.30 | The converted file is the source of the conflict rather than a settled control. |
| claim_probability | 0.28 | Possible row assignment, but weaker under the staged packet. |
| relevance | 1.00 | Direct competing reading. |
| canonical_readiness | 0.00 | Do not promote from this conflict state. |

## Hypothesis 3: Jose del Carmen Pulgar Parent Candidate

Hypothesis: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` in the Pulgar/Arriagada row is the father of `Jose del Carmen Segundo Pulgar Arriagada`.

Literal evidence:

- The current chunk reads the father field as `Jose del Carmen Pulgar S.`.
- The staged conflict draft says the father-name ending is unresolved and must remain open as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` exists, but its evidence snapshot currently links him as a draft parent of `Tulio Cesar Luis Jose`, not as a settled father from this entry.

Interpretation:

- `Jose del Carmen Pulgar` is a real parent candidate for this row if the Pulgar/Arriagada row is certified.
- The suffix cannot be used to create or merge a distinct person. The existing Jose page should not be merged with this row's father solely by name.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.55 | Father name is present in the chunk, but suffix and canonical attachment are unresolved. |
| conflict_severity | 0.78 | Wrong father reading would create an unsupported parent-child link. |
| evidence_quality | 0.50 | Direct row evidence is useful but blocked by row-level conflict. |
| conversion_confidence | 0.36 | Father field requires targeted image-level QA. |
| claim_probability | 0.52 | Candidate father only. |
| relevance | 0.96 | Direct parent candidate in the staged draft. |
| canonical_readiness | 0.05 | Hold; no parent promotion or merge. |

## Hypothesis 4: Juana Arriagada de Pulgar Mother Candidate

Hypothesis: `Juana Arriagada de Pulgar` in the Pulgar/Arriagada row is the mother of `Jose del Carmen Segundo Pulgar Arriagada`.

Literal evidence:

- The current chunk and source packet record mother `Juana Arriagada de Pulgar`.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` lists child `Jose del Carmen Segundo Pulgar Arriagada` as probable, with confidence 1, and keeps the supporting source packet tied to this chunk family.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate candidate tied to a draft parent relationship for `Tulio Cesar Luis Jose`, not this entry 172 row.

Interpretation:

- The mother reading is more textually stable than the father's suffix, but it is still dependent on resolving the row-level conversion conflict.
- `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` should remain separate or unresolved; the names differ and their staged child contexts differ.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.66 | Mother name is consistently stated in the Pulgar/Arriagada chunk reading. |
| conflict_severity | 0.82 | Wrong row selection would create a false mother-child link. |
| evidence_quality | 0.58 | Direct row text plus existing low-confidence canonical reflection. |
| conversion_confidence | 0.42 | Blocked by the same row conflict. |
| claim_probability | 0.62 | Probable if the Pulgar row is certified. |
| relevance | 0.96 | Direct parent candidate in the staged draft. |
| canonical_readiness | 0.08 | Hold; do not promote beyond existing low-confidence/draft state. |

## Pulgar-Line Anti-Conflation Comparisons

### Dario Arturo Pulgar-Smith

Literal evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` represents Dario Arturo Pulgar-Smith from family-supplied knowledge as Alexander John Heinz's maternal grandfather.
- That canonical page warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review.
- The entry 172 conflict draft does not name Dario Arturo Pulgar-Smith, Alexander John Heinz, `Smith`, a grandchild, or any later-life identity bridge.

Interpretation:

- Entry 172 may be relevant to the broader Pulgar line only after row QA and proof review. It is not evidence that `Jose del Carmen Segundo Pulgar Arriagada` or either parent is Dario Arturo Pulgar-Smith.

Scores: identity confidence 0.02; conflict severity 0.72; evidence quality 0.28; conversion confidence 0.42; claim probability 0.02; relevance 0.74; canonical readiness 0.00.

### Dario Arturo Pulgar

Literal evidence:

- Existing staged CV analyses preserve `Dario Arturo Pulgar` as a document-level CV subject with unresolved bridge to canonical `Dario Arturo Pulgar-Smith`.
- Entry 172 names no `Dario` or `Arturo`; it names a child `Jose del Carmen Segundo Pulgar Arriagada` if the Pulgar/Arriagada row controls.

Interpretation:

- Shared Pulgar surname does not establish same-person identity, ancestry, or a name variant. This entry could become lineage context only after a separate proof chain connects generations.

Scores: identity confidence 0.03; conflict severity 0.70; evidence quality 0.30; conversion confidence 0.42; claim probability 0.03; relevance 0.72; canonical readiness 0.00.

### Dario Jose Pulgar-Arriagada

Literal evidence:

- Existing staged context elsewhere contains `Dario Jose Pulgar-Arriagada` in separate Pulgar-Arriagada clusters.
- This entry 172 draft does not name `Dario Jose`; it names `Jose del Carmen Segundo Pulgar Arriagada` under the Pulgar/Arriagada hypothesis.

Interpretation:

- `Jose` appearing as a given-name element in different people is not a bridge. Preserve `Dario Jose Pulgar-Arriagada` separately from `Jose del Carmen Segundo Pulgar Arriagada`.

Scores: identity confidence 0.04; conflict severity 0.78; evidence quality 0.32; conversion confidence 0.42; claim probability 0.04; relevance 0.78; canonical readiness 0.00.

### Dario/Dario Pulgar Arriagada

Literal evidence:

- Canonical `wiki/people/dar-o-pulgar-arriagada.md` records a narrow 2000-12-05 expropriation event naming `Darío Pulgar Arriagada`.
- Entry 172, if Pulgar/Arriagada, is an 1888 birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Pulgar Arriagada`.

Interpretation:

- The surname pattern is relevant as a watch item, not a merge basis. The time gap and different given names require a later reviewed bridge before any relationship or duplicate-person claim.

Scores: identity confidence 0.03; conflict severity 0.82; evidence quality 0.34; conversion confidence 0.42; claim probability 0.03; relevance 0.80; canonical readiness 0.00.

### Jose/Juana Parent Candidates

Literal evidence:

- Direct candidates in this staged draft are `Jose del Carmen Pulgar`/`Jose del Carmen Pulgar S.`/`Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`.
- Existing wiki context also contains `Juana de Dios Amagada de Pulgar`, tied to a separate `Tulio Cesar Luis Jose` draft parent cluster.

Interpretation:

- The Pulgar/Arriagada row and the Tulio/Juana de Dios Amagada cluster should remain separate until source-visible names, child identities, dates, and relationships are compared in proof review.

Scores: identity confidence 0.44; conflict severity 0.84; evidence quality 0.46; conversion confidence 0.38; claim probability 0.40; relevance 0.92; canonical readiness 0.03.

## Conflicts

- Same-person conflict: none can be resolved. The draft concerns competing row identity for entry 172, not a proven same-person match.
- Duplicate-person risk: high if `Jose del Carmen Pulgar` from entry 172 is automatically merged with the existing Jose page or with other Jose Pulgar candidates.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` must remain separate readings of one unresolved field, not separate promoted identities.
- Relationship conflict: Pulgar/Arriagada parent-child links are directly contradicted by the Gomez/de la Cruz converted-row reading for the same entry number.
- Chronology conflict: no internal chronology conflict if the Pulgar/Arriagada row controls; the Gomez/de la Cruz row gives a different birth date and place for a different child.
- Canonical conflict: existing wiki snapshots already reflect low-confidence Pulgar/Arriagada claims from this chunk family; those are not ready for strengthening while this exact conflict remains open.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada` | 0.68 | Hold as candidate; send to targeted conversion QA. |
| 2 | `Juana Arriagada de Pulgar` is the mother if the Pulgar row controls | 0.62 | Hold parent link pending row QA and proof review. |
| 3 | `Jose del Carmen Pulgar`/suffix variant is the father if the Pulgar row controls | 0.52 | Hold parent link; require father-field QA. |
| 4 | Entry 172 is the Gomez/de la Cruz row for `Jose Francisco` | 0.28 | Preserve as competing converted-file hypothesis until QA. |
| 5 | Entry 172 supports a Dario-line identity or relationship bridge | 0.03 | Do not merge or attach to Dario clusters by name alone. |

## Recommended Next Action

Keep the staged conflict at `hold_for_conversion_qa`. The exact next proof-review step is targeted conversion QA against the source image for `CHUNK-b8f4f0490a36-P0001-01`: confirm whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row, then explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review on child identity, birth facts, father claim, mother claim, child-parent relationships, and any parent-pair or Pulgar-line comparison. Until that happens, do not merge people, rename canonical pages, promote claims, or attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or Jose/Juana parent candidates beyond explicitly held hypotheses.
