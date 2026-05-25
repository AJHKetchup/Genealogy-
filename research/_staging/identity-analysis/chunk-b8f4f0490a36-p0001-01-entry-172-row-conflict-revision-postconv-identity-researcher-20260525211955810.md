---
type: identity_conflict_analysis
status: draft
analysis_status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525211955810
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md
staged_conflict_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Row Conflict

## Blockers

1. Row-level conversion conflict: the staged conflict draft says the assigned chunk reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at Calle de Valdivia. The same staged draft says the current converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
2. This is not a name variant or minor transcription issue. The child, parents, birth date, birth place, informant context, and row neighborhood differ.
3. No child identity, parent relationship, birth fact, residence fact, or canonical Pulgar-line bridge should be promoted until targeted conversion QA identifies the controlling entry-172 row from the source image.
4. The father field remains specially blocked: proof review must certify whether it reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
5. The named `genealogy-proof-review` skill was not available in this session; this note follows the task's evidence-contract rules and preserves literal readings separately from interpretation.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md`.
- Revised source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Existing wiki context checked: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/dario-pulgar-adult-passenger-age-64.md`, `wiki/people/dario-pulgar-child-passenger-age-11.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

## Literal Source Readings

### Reading A: Assigned Chunk / Revised Source Packet

The assigned chunk presents entry 172 on page 58 as a male child named `Jose del Carmen Segundo Pulgar Arriagada`, registered 7 April 1888, born 8 March 1888 at 3 p.m. at Calle de Valdivia. It names father `Jose del Carmen Pulgar S.`, Chilean, employee, resident at Calle de Colipi, and mother `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident at Calle de Colipi. The compareciente is `Ernesto Herrera L.`, present at birth.

### Reading B: Current Converted Markdown

The current converted Markdown presents entry 172 as a male child named `Jose Miguel`, registered 7 April 1888, born 6 April 1888 at 10 p.m. in `En esta`. It names father `Oswaldo Burgos` and mother `Concepcion de la Cruz`.

## Hypotheses

### H1: Entry 172 Is The Pulgar/Arriagada Birth Row

Evidence supporting: the assigned chunk and revised source packet agree on a full Pulgar/Arriagada row for entry 172, including child, father, mother, birth date, place, residences, and informant.

Evidence against or limiting: the current converted Markdown gives a completely different entry 172. Existing wiki pages already contain low-confidence/probable evidence snapshots for the Pulgar/Arriagada row, but those rely on the same conflicted conversion cluster and cannot independently resolve the row assignment.

Scores: identity confidence 0.42; conflict severity 0.95; evidence quality 0.45; conversion confidence 0.25; claim probability 0.42; relevance 0.95; canonical readiness 0.05.

Posture: hold for conversion QA.

### H2: Entry 172 Is The Burgos / De la Cruz Birth Row

Evidence supporting: the current converted Markdown explicitly assigns entry 172 to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.

Evidence against or limiting: the staged conflict draft and revised source packet were created because the assigned chunk disagrees and gives a full Pulgar/Arriagada row for the same entry. No existing canonical family context reviewed here supplies an identity reason to prefer the Burgos reading.

Scores: identity confidence 0.35; conflict severity 0.95; evidence quality 0.40; conversion confidence 0.25; claim probability 0.35; relevance 0.25; canonical readiness 0.05.

Posture: hold for conversion QA.

### H3: `Jose del Carmen Segundo Pulgar Arriagada` Is A Child Of `Jose del Carmen Pulgar S.` And `Juana Arriagada de Pulgar`

Evidence supporting: if Reading A is the controlling row, the assigned chunk directly states the child, father, and mother in one civil birth-registration row. Existing wiki stubs for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` contain related staged evidence snapshots.

Evidence against or limiting: the relationship is entirely dependent on resolving Reading A. The father suffix or final mark after `Pulgar` remains uncertified. Existing `Jose del Carmen Pulgar` also has a separate draft child link to `Tulio Cesar Luis Jose`; that may be family-context evidence later, but it does not prove this row.

Scores: identity confidence 0.40; conflict severity 0.90; evidence quality 0.45; conversion confidence 0.25; claim probability 0.40; relevance 0.92; canonical readiness 0.05.

Posture: hold for conversion QA and father-field proof review.

### H4: `Juana Arriagada de Pulgar` And `Juana de Dios Amagada de Pulgar` Are The Same Parent Candidate

Evidence supporting: both existing wiki pages are Pulgar-associated Juana parent candidates in Los Angeles-area birth-register context, and both are attached in local context to children of a `Jose del Carmen Pulgar`-type father.

Evidence against or limiting: `Arriagada` and `Amagada` are materially different readings unless a source-image reread proves one is a misread or variant. The entry-172 row conflict must be resolved before using it as evidence. Entry 513 context is separate and should not silently correct this entry.

Scores: identity confidence 0.22; conflict severity 0.70; evidence quality 0.35; conversion confidence 0.25; claim probability 0.22; relevance 0.72; canonical readiness 0.03.

Posture: preserve as separate hypotheses pending targeted parent-name proof review.

### H5: Entry 172 Connects To `Dario Arturo Pulgar-Smith` Or Document-Level `Dario Arturo Pulgar`

Evidence supporting: canonical `Dario Arturo Pulgar-Smith` is a family-supplied Pulgar-line person, and staged CV materials elsewhere use `Dario Arturo Pulgar`. A confirmed Pulgar/Arriagada 1888 birth row could be a future lineage lead.

Evidence against or limiting: the staged conflict draft and assigned row do not mention Dario, Arturo, Smith, a spouse, descendant, grandchild, CV, passenger list, or any lineage bridge to the canonical Dario profile. The canonical page explicitly warns not to attach similarly named Pulgar records without identity review.

Scores: identity confidence 0.08; conflict severity 0.75; evidence quality 0.20; conversion confidence 0.25; claim probability 0.08; relevance 0.55; canonical readiness 0.01.

Posture: do not promote; compare only after entry QA and an explicit lineage bridge.

### H6: Entry 172 Connects To `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, Or `Dario/Darío Pulgar Arriagada`

Evidence supporting: local staged and wiki context contains separate Pulgar-Arriagada/Dario clusters, including a canonical `Darío Pulgar Arriagada` stub and staged medical/Geneva public-role notes. The Pulgar-Arriagada surname pattern makes this worth checking after the row is stabilized.

Evidence against or limiting: this entry, even under Reading A, names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario. It gives no age, occupation, medical title, Geneva role, spouse, child, or direct same-person bridge to any Dario cluster. The Dario clusters must not be merged by surname pattern or family context alone.

Scores: identity confidence 0.06; conflict severity 0.75; evidence quality 0.20; conversion confidence 0.25; claim probability 0.06; relevance 0.60; canonical readiness 0.01.

Posture: do not promote; preserve as a later comparison candidate only.

## Conflicts

- Same-person conflict: unresolved between the Pulgar/Arriagada child reading and the Burgos/De la Cruz child reading; these are different people unless source QA proves one reading is a row-assignment error.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` is promoted while the controlling row remains disputed; moderate if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar` without a parent-name reread.
- Name-variant conflict: `Jose del Carmen Pulgar S.` may be a full father name plus suffix/initial, but the exact field is not yet certified. `Arriagada` and `Amagada` remain separate readings.
- Relationship conflict: all child-parent claims from entry 172 are blocked by the row conflict.
- Chronology conflict: none proven after interpretation is separated from literal readings. The apparent chronology only becomes usable if Reading A is QA-confirmed.

## Ranked Conclusions

| Rank | Hypothesis | Probability | Required next proof step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 may be the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.42 | Targeted source-image conversion QA must choose the controlling entry-172 row. |
| 2 | Entry 172 may be the Burgos/De la Cruz row for `Jose Miguel`. | 0.35 | Same targeted source-image conversion QA. |
| 3 | `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` are the child's parents. | 0.40, conditional on H1 | After H1 passes, proof-review the father and mother fields and rerun relationship review. |
| 4 | `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person. | 0.22 | Compare proof-reviewed parent-name images from entry 172 and entry 513; do not merge from names alone. |
| 5 | Entry 172 provides a lineage bridge to `Dario Arturo Pulgar-Smith` / `Dario Arturo Pulgar`. | 0.08 | First prove the entry row, then use separate lineage records explicitly connecting the verified family to Dario Arturo. |
| 6 | Entry 172 provides a bridge to `Dario Jose Pulgar-Arriagada` / `Darío J. Pulgar Arriagada` / `Dario/Darío Pulgar Arriagada`. | 0.06 | Only after row QA, run a separate Pulgar-Arriagada identity-bridge proof review comparing dates, parents, names, occupations, and places. |

## Recommended Next Action

Keep the conflict draft and all dependent identity, birth, residence, parent, and relationship claims on `hold_for_conversion_qa`. The exact next action is targeted conversion QA against the source image, current converted Markdown, assigned chunk, and revised source packet to identify the controlling row for entry 172 and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that QA, rerun proof review before any canonical promotion, parent merge, Dario-line comparison, relationship claim, or page rename.
