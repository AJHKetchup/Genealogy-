---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525121551449
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: hold
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conflict

## Blockers First

- The assigned staged conflict draft reports a material row-level conflict for entry 172. The current chunk/source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, while the assigned converted Markdown reads entry 172 as `Jose Francisco`, child of `Oswaldo Gomez` and `Emilia de la Cruz`.
- This is not a same-person or spelling-variant problem. It is a controlling row identity/conversion-assignment conflict. No dependent child identity, parent-child relationship, parent merge, or Dario-line comparison should be promoted until targeted conversion QA certifies the controlling row.
- The father field is not fully settled. The chunk reads `Jose del Carmen Pulgar S.`, but the exact ending must remain open as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` pending source-visible QA.
- Existing canonical pages already contain held or low-confidence b8f4f0490a36-derived evidence for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`. This staged conflict should block further reliance on those facts until QA/proof review reconciles the source packet, chunk, and converted Markdown.

## Literal Evidence Under Review

From the staged draft and source packet:

- Current chunk reading: entry `172`, registered `Siete de Abril de mil ochocientos ochenta i ocho`.
- Current chunk child: `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`.
- Current chunk birth detail: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`.
- Current chunk parents: father read as `Jose del Carmen Pulgar S.` with suffix unresolved; mother `Juana Arriagada de Pulgar`; parent residence `Calle de Colipi`.
- Current chunk informant: `Ernesto Herrera L.`, present at the birth.

Conflicting converted Markdown:

- Converted entry `172` child: `Jose Francisco`, sex `Varon`.
- Converted birth detail: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En esta`.
- Converted parents: `Oswaldo Gomez` and `Emilia de la Cruz`.

Interpretation kept separate: if the current chunk/source-packet reading is certified, the row is strong local evidence for a Pulgar/Arriagada birth registration. Until then, the literal evidence is mixed because the assigned converted file gives a different row identity.

## Hypothesis 1: Entry 172 Is Jose del Carmen Segundo Pulgar Arriagada

Hypothesis: the controlling source-visible entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`.

Supporting evidence:

- The current chunk and source packet consistently identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`.
- The current chunk gives matching Pulgar-line parent context: father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing canonical pages `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` and `wiki/people/juana-arriagada-de-pulgar.md` contain b8f4f0490a36-derived evidence snapshots for this child/mother relationship, but those pages are not independent proof because they depend on the same disputed row.

Contrary/conflicting evidence:

- The assigned converted Markdown for the same converted file reads entry 172 as `Jose Francisco`, not `Jose del Carmen Segundo Pulgar Arriagada`.
- The converted file gives different parents, birth date, birth place, professions, residences, and official signature context.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | The current chunk/source packet are internally consistent, but the assigned converted file directly conflicts. |
| conflict_severity | 0.95 | Different child, parents, dates, place, and row context. |
| evidence_quality | 0.58 | Good derivative chunk detail, but derivative disagreement prevents clean proof use. |
| conversion_confidence | 0.35 | Mixed; targeted row-level QA is required. |
| claim_probability | 0.64 | Probable if the current chunk is accepted; not promotable before QA. |
| relevance | 0.92 | Direct Pulgar/Arriagada family relevance if certified. |
| canonical_readiness | 0.10 | Hold; do not promote or update canonical pages from this task. |

## Hypothesis 2: Entry 172 Is Jose Francisco, Child Of Oswaldo Gomez And Emilia de la Cruz

Hypothesis: the assigned converted Markdown is the controlling reading for entry 172.

Supporting evidence:

- The assigned converted Markdown explicitly labels row `172` as `José Francisco`, son of `Oswaldo Gomez` and `Emilia de la Cruz`.

Contrary/conflicting evidence:

- The current chunk and source packet for the same source path and chunk id read entry 172 as the Pulgar/Arriagada row.
- The staged conflict draft was specifically created because the converted-file row identity disagrees with the image-reviewed/current chunk evidence.
- This hypothesis has no Pulgar-line relevance unless it explains a conversion assignment mismatch.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.30 | Present in the assigned converted file, but contradicted by the current chunk/source packet. |
| conflict_severity | 0.95 | Mutually exclusive with the Pulgar/Arriagada entry-172 hypothesis. |
| evidence_quality | 0.45 | Derivative converted text only in this review set. |
| conversion_confidence | 0.30 | The row may be from a different page/assignment. |
| claim_probability | 0.30 | Possible as a conversion text reading, not safe as the controlling row. |
| relevance | 0.10 | Not directly relevant to the Pulgar line except as a blocker. |
| canonical_readiness | 0.00 | Do not create/promote person or relationship claims. |

## Hypothesis 3: Jose del Carmen Pulgar / Jose del Carmen Pulgar S. Is The Father In This Row

Hypothesis: if the Pulgar/Arriagada row is certified, the father is a Jose del Carmen Pulgar candidate, possibly with suffix/initial `S.`.

Supporting evidence:

- The current chunk/source packet read the father field as `Jose del Carmen Pulgar S.`, Chilean, employee, resident at `Calle de Colipi`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` is a separate stub with other Pulgar-family evidence, including a draft child link to `Tulio Cesar Luis Jose`. That is useful context for comparison but not proof that all Jose del Carmen Pulgar mentions are the same person.

Contrary/conflicting evidence:

- The assigned converted Markdown names the father as `Oswaldo Gomez`, not Jose del Carmen Pulgar.
- The father suffix/initial is unresolved, and the existing Jose del Carmen Pulgar canonical page does not itself prove that this 1888 entry-172 father is the same Jose candidate as other records.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.52 | Plausible row-level father candidate only after QA. |
| conflict_severity | 0.85 | Father identity changes completely under the competing converted reading. |
| evidence_quality | 0.55 | Specific current-chunk father field, but unresolved suffix and conversion conflict. |
| conversion_confidence | 0.35 | Dependent on row-level QA. |
| claim_probability | 0.58 | Probable only under Hypothesis 1. |
| relevance | 0.88 | Potential Pulgar-line parent candidate. |
| canonical_readiness | 0.08 | Hold; no merge with existing Jose page by name alone. |

## Hypothesis 4: Juana Arriagada de Pulgar Is The Mother In This Row

Hypothesis: if the Pulgar/Arriagada row is certified, the mother is `Juana Arriagada de Pulgar`.

Supporting evidence:

- The current chunk/source packet read the mother field as `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident at `Calle de Colipi`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` records a child link to `Jose del Carmen Segundo Pulgar Arriagada`, but that evidence is b8f4f0490a36-derived and remains affected by this row conflict.

Contrary/conflicting evidence:

- The assigned converted Markdown names the mother as `Emilia de la Cruz`.
- `Juana de Dios Amagada de Pulgar` is a separate existing canonical stub tied to a different entry/child context. The shared forename `Juana` and married-name form `de Pulgar` do not justify merging `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.56 | Plausible row-level mother candidate under the current chunk reading. |
| conflict_severity | 0.85 | Competing converted row gives a different mother. |
| evidence_quality | 0.55 | Specific current-chunk mother field, but derivative conflict remains. |
| conversion_confidence | 0.35 | Dependent on row-level QA. |
| claim_probability | 0.60 | Probable only under Hypothesis 1. |
| relevance | 0.88 | Potential Pulgar/Arriagada parent candidate. |
| canonical_readiness | 0.08 | Hold; no Juana merge or promotion. |

## Pulgar-Line Anti-Conflation Comparison

This staged draft does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada in the entry-172 row. Those identities are therefore comparison context only.

Ranked hypotheses:

| Rank | Hypothesis | Probability | Current disposition |
| ---: | --- | ---: | --- |
| 1 | Entry 172, if QA-certified as Pulgar/Arriagada, is a row-level record for `Jose del Carmen Segundo Pulgar Arriagada`, not a Dario record. | 0.64 | Hold for conversion QA. |
| 2 | The father is a Jose del Carmen Pulgar candidate, possibly `Jose del Carmen Pulgar S.`. | 0.58 | Preserve as row-level candidate; do not merge to existing Jose page yet. |
| 3 | The mother is `Juana Arriagada de Pulgar`, separate from `Juana de Dios Amagada de Pulgar` unless later proof bridges them. | 0.60 | Preserve separately; do not merge Juana candidates. |
| 4 | This 1888 child or parent pair is an ancestor/lineage clue relevant to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | 0.25 | Possible family-context hint only; needs explicit lineage bridge. |
| 5 | This row supports a same-person merge with `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | 0.08 | Not supported by this row; do not merge by surname/name pattern. |
| 6 | This row supports a same-person merge with `Dario Pulgar` adult or child passenger candidates. | 0.05 | Not supported by this row; chronology and identity bridge absent. |

Comparison notes:

- `Dario Arturo Pulgar-Smith`: existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. The page itself warns not to auto-merge records mentioning Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith. Entry 172 does not mention Dario, Arturo, or Smith.
- `Dario Arturo Pulgar`: local staged CV/Habitat context elsewhere supports a document-level Dario Arturo/Dario Pulgar work cluster, but this birth-register row does not bridge to that person.
- `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada`: local staging elsewhere preserves medical/professional candidates with J./Jose/Arriagada forms. Entry 172 does not name Dario and cannot be used as a same-person bridge.
- `Dario/Dario Pulgar Arriagada` and canonical `wiki/people/dar-o-pulgar-arriagada.md`: existing canonical evidence concerns a 2000 expropriation event. Entry 172 is an 1888 birth-registration conflict for a Jose child and cannot bridge that identity.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` must remain separate or unresolved pending field-level and relationship proof review.

## Conflict Summary

- Same-person conflict: unresolved. The safe conclusion is that there are competing row identities for assigned entry 172.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is silently merged into `Jose del Carmen Pulgar`, or if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar`.
- Name-variant conflict: high for the father suffix/initial; medium for Juana surname variants only because separate local candidates exist. No Dario name-variant claim is supported by this row.
- Relationship conflict: high. The child-parent pair is either Pulgar/Arriagada or Gomez/de la Cruz under the competing derivative readings.
- Chronology conflict: not internally resolvable until row QA; dates differ between `1888-03-08` and `1888-03-26` for the assigned entry.

## Recommended Next Action

Run targeted conversion QA on the exact source image/chunk assignment for `CHUNK-b8f4f0490a36-P0001-01` and certify whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row. The QA note must explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that, run proof review on the certified row before any canonical promotion. If the Pulgar/Arriagada reading is certified, the next proof-review step should evaluate only row-level claims first: child birth name, birth date/place, registration date, father candidate, mother candidate, and child-parent relationships. A separate identity-bridge review is required before connecting this evidence to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, passenger-list Dario candidates, or any broader Pulgar-line merge.
