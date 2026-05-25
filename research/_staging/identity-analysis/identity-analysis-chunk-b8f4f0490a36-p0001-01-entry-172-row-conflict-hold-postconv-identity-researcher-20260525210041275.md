---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525210041275
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
conflict_type: row_level_conversion_conflict
identity_confidence_score: 0.56
conflict_severity_score: 0.93
evidence_quality_score: 0.74
conversion_confidence_score: 0.30
claim_probability: 0.62
relevance_score: 0.86
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Identity/Conflict Analysis: Entry 172 Row Conflict Hold

This note analyzes the exact staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md`.

## Blockers First

- Canonical readiness is blocked at `hold_for_conversion_qa`. The assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth row, while the assigned converted Markdown reads entry 172 as a Burgos/de la Cruz birth row.
- The conflict is row-level and identity-bearing. It changes the child, parents, birth date/time, birth place, parent residence, informant, and family relevance. This is not a same-person, duplicate-person, or spelling-variant issue.
- The Pulgar father field is not certified. The assigned chunk reads `Jose del Carmen Pulgar S.`, while reviewed notes in this workspace have treated the final suffix as unresolved. QA must decide `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical wiki pages already contain low-confidence or draft Pulgar/Arriagada context from this chunk family. This task cannot strengthen, merge, rename, or promote any of those pages.
- No Dario-line bridge is present in this entry. The row does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Darío Pulgar Arriagada`, or a Dario parent/spouse/child relationship.

## Literal Evidence

From the assigned chunk and source packet:

- Entry: `172`, register page 58, registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, `a las tres de la tarde`, `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.`, Chilean, employee, resident at `Calle de Colipí`.
- Mother: `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident at `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employee, resident at `Calle de Valdivia`.

From the assigned converted Markdown:

- Entry: `172`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, `a las diez de la noche`, `En esta`.
- Father: `Oswaldo Burgos`, Chilean, single, agriculturist, resident `de este`.
- Mother: `Concepcion de la Cruz`, Chilean, single, resident `de este`.
- Informant: `Oswaldo Burgos`, age 26, employee, resident `En esta`.

Interpretation: these cannot both be the same child-parent row for entry 172. The conflict must be resolved as a conversion/source-assignment problem before identity conclusions can be promoted.

## Hypotheses And Scores

| Rank | Hypothesis | Identity confidence | Conflict severity | Evidence quality | Conversion confidence | Claim probability | Relevance | Canonical readiness |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` / `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`. | 0.56 | 0.93 | 0.74 | 0.30 | 0.62 | 0.95 | hold_for_conversion_qa |
| 2 | Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. | 0.28 | 0.93 | 0.55 | 0.30 | 0.28 | 0.20 | hold_for_conversion_qa |
| 3 | The derivative files reflect mismatched row, image, or conversion-state assignments rather than a genealogical same-person conflict. | 0.72 | 0.95 | 0.75 | 0.30 | 0.76 | 0.90 | hold_for_conversion_qa |
| 4 | `Jose del Carmen Pulgar S.` in the Pulgar row is the same person as existing `Jose del Carmen Pulgar`. | 0.42 | 0.75 | 0.58 | 0.30 | 0.50 | 0.82 | blocked |
| 5 | `Juana Arriagada de Pulgar` in the Pulgar row is the same person as existing `Juana Arriagada de Pulgar`. | 0.46 | 0.72 | 0.62 | 0.30 | 0.58 | 0.84 | blocked |
| 6 | Entry 172 provides bridge evidence for any Dario Pulgar candidate. | 0.05 | 0.75 | 0.35 | 0.30 | 0.08 | 0.30 | blocked |

## Evidence Supporting Each Hypothesis

### H1: Pulgar/Arriagada Row Controls

Supporting evidence:

- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`.
- The assigned source packet repeats the same Pulgar/Arriagada row and records high family relevance with low conversion confidence.
- A civil birth registration, once conversion-reviewed, would be strong evidence for a birth identity and parent-name claim.
- Existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` show local staged Pulgar/Arriagada context.

Conflicts and limits:

- The assigned converted Markdown directly contradicts the Pulgar/Arriagada reading.
- The father suffix after `Pulgar` is not certified.
- No canonical child, parent, or parent-pair promotion should proceed until targeted conversion QA and proof review are complete.

### H2: Burgos/de la Cruz Row Controls

Supporting evidence:

- The assigned converted Markdown explicitly places `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz` under entry 172.
- That converted row is internally coherent as a birth-registration abstraction.

Conflicts and limits:

- The assigned chunk and source packet contradict it in every identity-bearing field.
- This reading has no Pulgar/Arriagada family relevance unless QA shows the Pulgar row belongs elsewhere.
- It cannot explain the Pulgar/Arriagada row as a same-person or name-variant issue.

### H3: Derivative Assignment Or Conversion-State Mismatch

Supporting evidence:

- The disagreement includes child name, parents, birth event, residence, informant, and row context under the same entry number.
- The staged draft and source packet already recommend conversion QA rather than identity merge.

Conflicts and limits:

- Identity analysis cannot certify the controlling row.
- The correct output is a QA/proof-review step, not a person attachment.

### H4: Jose Parent Candidate

Supporting evidence:

- The Pulgar/Arriagada row names the father as `Jose del Carmen Pulgar S.` in the assigned chunk.
- Existing `wiki/people/jose-del-carmen-pulgar.md` contains local parent context from another staged child candidate.

Conflicts and limits:

- The `S.` may be a second-surname initial, suffix, stray mark, or conversion artifact.
- Do not silently normalize the father to `Jose del Carmen Pulgar`.
- Do not merge this father candidate into the canonical stub before row QA and father-field proof review.

### H5: Juana Parent Candidate

Supporting evidence:

- The Pulgar/Arriagada row names `Juana Arriagada de Pulgar` as mother.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` contains a low-confidence evidence snapshot for this child from the same chunk cluster.

Conflicts and limits:

- Row-level conversion conflict blocks promotion.
- Preserve the literal married-name form.
- Do not merge with any other Juana candidate, including differently read `Juana de Dios...` candidates, without a separate proof review comparing literal names, spouse context, children, chronology, and sources.

### H6: Dario-Line Candidate Or Name-Variant Bridge

Supporting evidence:

- The workspace contains unresolved Pulgar-line candidates, including canonical `Dario Arturo Pulgar-Smith`, staged document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Dario/Dario Pulgar Arriagada` / `Darío Pulgar Arriagada` contexts.
- The surname overlap justifies an anti-conflation check.

Conflicts and limits:

- Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, Dario Jose, Dario J., or a Dario relationship.
- It gives no professional, CV, passenger-list, Geneva/ICRC, expropriation, Alexander John Heinz, or later-life context for a Dario candidate.
- The canonical `Dario Arturo Pulgar-Smith` page is family-supplied and explicitly warns against automatic merges with similarly named source clusters.
- Staged CV evidence for `Dario Arturo Pulgar` remains document-level unless a separate identity bridge connects that person to canonical `Dario Arturo Pulgar-Smith`.

## Conflict Assessment

- Same-person conflict: `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` are competing row readings, not variants of one person.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is merged into `Jose del Carmen Pulgar` before father-field QA; moderate-high if `Juana Arriagada de Pulgar` is merged with other Juana candidates by family context alone.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` remains unresolved; `Juana Arriagada de Pulgar` should remain literal.
- Relationship conflict: high. One reading gives Pulgar/Arriagada parents; the other gives Burgos/de la Cruz parents.
- Chronology conflict: high. The Pulgar row gives birth on 1888-03-08 at 3 p.m.; the converted Markdown gives 1888-04-06 at 10 p.m.
- Dario-line conflict: no positive Dario bridge is present; all Dario candidates remain anti-conflation checkpoints only.

## Ranked Pulgar-Line Comparison

| Rank | Candidate / cluster | Relationship to this staged draft | Probability for attachment from this evidence | Required next proof-review or promotion step |
| ---: | --- | --- | ---: | --- |
| 1 | `Jose del Carmen Segundo Pulgar Arriagada` | Direct child candidate if the Pulgar/Arriagada row controls. | 0.62 | Targeted conversion QA for row identity, then proof review of child name, sex, birth date/time/place, and registration date. |
| 2 | `Juana Arriagada de Pulgar` | Direct mother candidate if the Pulgar/Arriagada row controls. | 0.58 | Conversion QA plus parent-candidate proof review; preserve the literal married-name form. |
| 3 | `Jose del Carmen Pulgar S.` / `Jose del Carmen Pulgar` | Direct father candidate only if the Pulgar/Arriagada row controls. | 0.50 | Targeted image reread and certification of the father field before any merge or name normalization. |
| 4 | `Dario Arturo Pulgar-Smith` | Existing family-supplied maternal-grandfather page; no direct evidence in this entry. | 0.02 | Separate identity-bridge proof review explicitly connecting a Dario source to Pulgar-Smith; do not attach entry 172. |
| 5 | `Dario Arturo Pulgar` | Existing/staged CV document-level subject; no direct evidence in this entry. | 0.02 | Separate CV identity bridge review; do not attach entry 172. |
| 6 | `Dario Jose Pulgar-Arriagada` | Separate staged/title/photo cluster; no direct evidence in this entry. | 0.03 | Separate proof review comparing name, profession, dates, and parent or relationship evidence. |
| 7 | `Dario/Dario Pulgar Arriagada` / `Darío Pulgar Arriagada` | Separate Pulgar-Arriagada contexts; no direct evidence in this entry. | 0.02 | Separate identity bridge with vital-date, relationship, or chronology continuity. |
| 8 | Other Jose/Juana parent candidates | Only broad parent-pair context; no proven same-person bridge from this draft. | 0.20 | Parent-candidate proof review after row QA, comparing literal names, spouse context, child chronology, and source reliability. |

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| identity_confidence_score | 0.56 | Moderate for the Pulgar/Arriagada row as the likely family-relevant row, but not enough for canonical identity attachment. |
| conflict_severity_score | 0.93 | The derivative records disagree on all major identity-bearing fields. |
| evidence_quality_score | 0.74 | Civil-register evidence and staged image-reviewed context are strong, but this task did not perform conversion QA. |
| conversion_confidence_score | 0.30 | The assigned converted Markdown and assigned chunk/source packet remain in direct row-level conflict. |
| claim_probability | 0.62 | Pulgar/Arriagada is more probable from the staged source packet and chunk, but uncertified. |
| relevance_score | 0.86 | High for Pulgar/Arriagada parent research; low for direct Dario identity bridging. |
| canonical_readiness | hold_for_conversion_qa | No promotion, merge, or canonical strengthening should occur before targeted conversion QA and rerun proof review. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` using the source image, assigned converted Markdown, assigned chunk, and assigned source packet. The QA output must certify whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row. If Pulgar/Arriagada controls, it must also certify the father field as exactly one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review before promoting any child identity, birth fact, sex, parent-name claim, child-parent relationship, parent-pair clue, duplicate-person decision, or canonical attachment. Keep `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and other Jose/Juana candidates separate unless a later proof-reviewed bridge explicitly connects them.
