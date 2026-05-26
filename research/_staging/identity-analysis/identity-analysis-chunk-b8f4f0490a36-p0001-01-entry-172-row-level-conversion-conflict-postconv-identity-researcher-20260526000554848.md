---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: "postconv-identity-analysis-20260526000554848"
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
subject: "Entry 172 birth-registration row"
conflict_type: row_level_conversion_conflict
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers

1. The staged conflict draft and source packet report that entry 172 is a Pulgar/Arriagada row, but the current converted Markdown reports entry 172 as a Burgos/de la Cruz row. This is a controlling row-level conversion conflict.
2. No child identity, birth fact, parent name, parent-child relationship, parent identity merge, or Dario-line bridge should be promoted until targeted conversion QA certifies the controlling entry-172 row.
3. If the Pulgar/Arriagada row is certified, the father field still needs a narrow reread. The current local readings are `Jose del Carmen Pulgar S.`, `Jose del Carmen Pulgar`, or `Jose del Carmen Pulgar [?]`.
4. The staged draft does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Dario J. Pulgar Arriagada, or Darío Pulgar Arriagada. These are anti-conflation checkpoints only.
5. Existing canonical wiki context already contains probable or draft Jose/Juana/Pulgar material with low or unresolved confidence. This task cannot strengthen those pages because the row-control conflict is unresolved.

## Literal Evidence Reviewed

- Staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing wiki context checked: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Row

Interpretation: the assigned chunk and source-packet reading control entry 172, and the current converted Markdown has row-level conversion drift.

Evidence supporting:

- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male.
- The assigned chunk gives birth as 8 March 1888 at 3 p.m., place `Calle de Valdivia`.
- The assigned chunk gives father as `Jose del Carmen Pulgar S.` and mother as `Juana Arriagada de Pulgar`.
- The source packet states a visual review of the source image shows page 58 row 172 as the Pulgar/Arriagada row, not the Burgos/de la Cruz row.
- The source packet was created specifically as a revised post-conversion evidence-extraction note and recommends `hold_for_conversion_qa`.

Evidence against or limiting:

- The current converted Markdown materially disagrees and records a different child, parents, birth date, birth place, informant, and neighboring row set.
- The father-field suffix is not certified.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong staged chunk/source-packet support, but blocked by direct converted-file disagreement. |
| conflict_severity | 0.96 | Two incompatible families are assigned to the same entry number. |
| evidence_quality | 0.72 | Civil birth register evidence is high-value, but this pass relies on staged readings and needs targeted QA. |
| conversion_confidence | 0.40 | The revised chunk is coherent, but the current converted Markdown conflicts materially. |
| claim_probability | 0.76 | Likely the correct row if the source-packet visual check is accepted, still not promotion-ready. |
| relevance | 1.00 | Directly concerns the assigned entry-172 conflict. |
| canonical_readiness | 0.08 | Hold until row-control QA and father-field proof review. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Row

Interpretation: the current converted Markdown controls entry 172, and the assigned chunk/source-packet Pulgar reading reflects a separate conversion or row-selection error.

Evidence supporting:

- The current converted Markdown records entry 172 as `José Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`.
- The converted Markdown gives father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

Evidence against or limiting:

- The staged conflict draft says the assigned chunk/source-image reading identifies the row as Pulgar/Arriagada.
- The source packet explicitly reports a visual source-image check finding row 172 as Pulgar/Arriagada.
- The chunk file itself contains the Pulgar/Arriagada row for entry 172.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.28 | Supported only by the current converted Markdown in this review set. |
| conflict_severity | 0.96 | If accepted, it would invalidate the staged Pulgar extraction for this entry. |
| evidence_quality | 0.46 | Converted text is relevant but contradicted by chunk and source packet. |
| conversion_confidence | 0.24 | Multiple local staged artifacts identify this as a conversion-control problem. |
| claim_probability | 0.22 | Possible until QA, but lower than the Pulgar/Arriagada hypothesis. |
| relevance | 1.00 | Directly concerns the assigned entry-172 conflict. |
| canonical_readiness | 0.00 | No promotion while the row-control conflict remains unresolved. |

## Hypothesis 3: The Pulgar Row Supports Jose/Juana Parent Candidates

Interpretation: if Hypothesis 1 is certified, entry 172 can support a child identity for `Jose del Carmen Segundo Pulgar Arriagada` and parent candidates `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.

Evidence supporting:

- The chunk gives a parent-child structure: child `Jose del Carmen Segundo Pulgar Arriagada`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`.
- Existing canonical wiki page `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has a probable mother link to `Juana Arriagada de Pulgar` and staged birth facts from entry 172.
- Existing canonical wiki page `wiki/people/juana-arriagada-de-pulgar.md` has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.

Evidence against or limiting:

- Row-control QA is unresolved.
- The father identity is not stable because the suffix or abbreviation after `Pulgar` remains uncertified.
- Existing `wiki/people/jose-del-carmen-pulgar.md` contains a separate draft child link to `Tulio Cesar Luis Jose`; this task does not prove the same father person.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.60 | Coherent if the Pulgar row controls, but parent identity needs separate proof review. |
| conflict_severity | 0.82 | Parent-child and parent-identity facts are materially affected by the row conflict. |
| evidence_quality | 0.70 | Direct civil-register style evidence, currently staged and QA-blocked. |
| conversion_confidence | 0.40 | Same row-control conflict applies. |
| claim_probability | 0.58 | Plausible after row certification, not before. |
| relevance | 0.98 | Direct Pulgar/Juana parent-candidate relevance. |
| canonical_readiness | 0.06 | Requires row QA, father-field certification, and parent-identity proof review. |

## Hypothesis 4: The Row Bridges To Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Interpretation: the Pulgar/Arriagada surname cluster may be part of the broader Pulgar line, but this row does not itself identify canonical Dario Arturo Pulgar-Smith or staged CV subject Dario Arturo Pulgar.

Evidence supporting:

- Existing canonical `wiki/people/dario-arturo-pulgar-smith.md` is a family-supplied Pulgar-Smith line page and warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records require identity review before attachment.
- The staged row, if certified, contains Pulgar and Arriagada names that are relevant enough to keep as a future comparison point.

Evidence against or limiting:

- The row does not name Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, or a grandparent relationship.
- The child candidate is `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith`.
- No chronology bridge, residence chain, parent chain, spouse, child, or descendant bridge appears in the assigned draft.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Surname context only; no direct identity bridge. |
| conflict_severity | 0.66 | High conflation risk if promoted by name pattern alone. |
| evidence_quality | 0.30 | The evidence is not identity-bearing for Dario. |
| conversion_confidence | 0.40 | Underlying row is QA-blocked. |
| claim_probability | 0.05 | This row alone does not support a Dario bridge. |
| relevance | 0.55 | Relevant only as Pulgar-line anti-conflation context. |
| canonical_readiness | 0.00 | Do not attach to canonical Dario Arturo Pulgar-Smith or staged Dario Arturo Pulgar. |

## Hypothesis 5: The Row Bridges To Dario Jose Pulgar-Arriagada Or Dario/Dario Pulgar Arriagada

Interpretation: separate staged and canonical context uses forms including `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar A.`, and `Darío Pulgar Arriagada`; this entry does not prove those are the same person as the entry-172 child or parents.

Evidence supporting:

- Existing local context includes a canonical `Darío Pulgar Arriagada` page tied to a 5 December 2000 Serviu Región del Bío Bío expropriation notice.
- Staged local materials include separate Dario Jose/Dario J./Dario Pulgar-Arriagada photograph, medical-title, and official-list contexts.
- The Pulgar/Arriagada surname pattern justifies explicit comparison.

Evidence against or limiting:

- Entry 172 does not name Dario or Darío.
- Entry 172 does not state `Jose` as a Dario middle name; it states the child name as `Jose del Carmen Segundo` under the Pulgar hypothesis.
- No role, age, medical title, public office, 1929 Geneva context, 2000 property context, spouse, parent chain, or descendant chain bridges these Dario clusters to the entry-172 family.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.07 | Name-family overlap only. |
| conflict_severity | 0.72 | High duplicate/merge risk if surname overlap is treated as proof. |
| evidence_quality | 0.28 | No direct same-person evidence in the assigned row. |
| conversion_confidence | 0.40 | Underlying row is QA-blocked. |
| claim_probability | 0.04 | This row alone does not support attachment to these Dario clusters. |
| relevance | 0.62 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | Preserve separately unless a later proof review supplies an explicit bridge. |

## Conflict Findings

- Same-person conflict: unresolved between the Pulgar/Arriagada reading and Burgos/de la Cruz reading for the same entry number; no same-person merge can be made.
- Duplicate-person risk: high for any attempt to merge `Jose del Carmen Pulgar S.` with existing `Jose del Carmen Pulgar` without father-field QA and parent-identity proof review.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` must remain distinct readings until certified.
- Relationship conflict: parent-child evidence for `Jose del Carmen Segundo Pulgar Arriagada` with Jose/Juana is directly blocked by the row-control conflict.
- Chronology conflict: none inside the certified Pulgar row itself, but the row supplies no chronology bridge to later Dario Pulgar-Arriagada, Dario Arturo Pulgar, or Dario Arturo Pulgar-Smith contexts.
- Conversion conflict: severe. The staged source packet and chunk identify a different entry-172 family than the current converted Markdown.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Canonical readiness | Required next proof-review or promotion step |
| ---: | --- | ---: | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada row and converted Markdown has row drift. | 0.76 | 0.08 | Targeted conversion QA against source image/page 58, entry 172. |
| 2 | Entry 172 is the Burgos/de la Cruz row and staged Pulgar extraction is wrong. | 0.22 | 0.00 | Same targeted conversion QA; if accepted, release or supersede Pulgar claims. |
| 3 | Certified Pulgar row supports Jose/Juana parent candidates. | 0.58 conditional | 0.06 | After row QA, father-field proof review and parent-identity proof review. |
| 4 | Row bridges to Dario Arturo Pulgar-Smith or Dario Arturo Pulgar. | 0.05 | 0.00 | Separate identity-bridge proof review using explicit Dario/Pulgar-Smith evidence; do not use this row alone. |
| 5 | Row bridges to Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Darío Pulgar Arriagada. | 0.04 | 0.00 | Separate anti-conflation identity review using age, role, chronology, and direct names; preserve as separate. |

## Recommended Next Action

Run targeted conversion QA for `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, page 58, row 172, comparing the source image directly against the chunk and converted Markdown. The QA result should certify whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row.

If the Pulgar/Arriagada row is certified, immediately run father-field proof review and record the father exactly as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Only after that should proof review consider promotion of the child identity, birth facts, mother/father claims, informant claim, and parent-child relationships. A separate identity-bridge proof review is required before connecting this row to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, `Darío Pulgar Arriagada`, or any existing Jose/Juana parent candidate beyond the literal row evidence.
