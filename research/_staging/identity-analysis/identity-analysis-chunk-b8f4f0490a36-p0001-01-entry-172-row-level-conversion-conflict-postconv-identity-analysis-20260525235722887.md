---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525235722887
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-25
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Row-control blocker: the staged conflict draft reports that the assigned chunk/source-image reading and the current converted Markdown do not identify the same entry-172 family.
- Current converted Markdown blocker: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- Assigned chunk/source-packet blocker: the referenced chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.` in the chunk text, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- Father-name blocker: the source packet says visual review supports `Jose del Carmen Pulgar` at the start of the father field, but the trailing element is not certified and must be resolved as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Canonical readiness blocker: no child identity, birth fact, parent name, parent-child relationship, Jose/Juana merge, or Dario-line attachment should be promoted until targeted conversion QA establishes the controlling entry-172 transcription.

## Literal Readings

Staged conflict draft: the assigned chunk/source-image reading is `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`; father `Jose del Carmen Pulgar S.` by chunk reading; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.

Referenced source packet: visual review says page 58 row numbered `172` is the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the converted Markdown. It preserves uncertainty on the father's final suffix.

Current converted Markdown: entry 172 is `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

Interpretation kept separate: this is best treated as a conversion-control conflict, not as evidence that the Pulgar/Arriagada child and Burgos/de la Cruz child are the same person.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Hypothesis: the controlling source image row for entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.

Supporting evidence:

- The staged conflict draft summarizes the assigned chunk/source-image reading as the Pulgar/Arriagada family.
- The source packet says visual review of page 58 row `172` supports the Pulgar/Arriagada row.
- The chunk transcription explicitly gives child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- Existing canonical stubs already contain low-confidence or probable entry-172-derived evidence for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, but those remain dependent on this conversion QA.

Conflicts and limits:

- The current converted Markdown materially disagrees on child, parents, birth date, birth time, place, informant, and apparent page family.
- The father suffix is unresolved.
- The record does not name Dario, Arturo, Smith, Dario Jose, or Dario Pulgar Arriagada.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Strong local staged/chunk/source-packet support, but row-control conflict prevents certification. |
| conflict_severity | 0.94 | Different child and parents in the same entry number. |
| evidence_quality | 0.70 | Civil birth register context is high value; current evidence is derivative plus source-packet visual review, not final QA. |
| conversion_confidence | 0.42 | Assigned chunk and converted Markdown conflict materially. |
| claim_probability | 0.72 | Probable working reading pending targeted QA. |
| relevance | 1.00 | Directly controls the assigned staged conflict. |
| canonical_readiness | 0.12 | Hold until conversion QA resolves row control and father suffix. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Hypothesis: the current converted Markdown is controlling, and entry 172 records `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Supporting evidence:

- The current converted Markdown directly transcribes entry 172 as the Burgos/de la Cruz row.

Conflicts and limits:

- The staged conflict draft and source packet state that visual review of the assigned source image supports the Pulgar/Arriagada row instead.
- The Burgos/de la Cruz reading has no Pulgar/Arriagada family relevance and no support from the assigned source packet.
- If this reading controls, the Pulgar/Arriagada source packet, related claims, and existing wiki evidence generated from this chunk would need correction or retirement rather than promotion.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.28 | Present in the converted Markdown, but contradicted by the staged visual-review packet. |
| conflict_severity | 0.94 | Same entry number but different family. |
| evidence_quality | 0.45 | Current converted text is specific, but appears to be the disputed derivative layer. |
| conversion_confidence | 0.30 | Conversion layer is the source of the conflict. |
| claim_probability | 0.28 | Possible only until QA decides row control. |
| relevance | 0.88 | Controls whether Pulgar/Arriagada evidence is usable. |
| canonical_readiness | 0.05 | Not promotable from this conflict state. |

## Hypothesis 3: Father Candidate `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.`

Hypothesis: the entry-172 father is the same page-local parent candidate as `Jose del Carmen Pulgar`, with a possible suffix or additional initial `S.`.

Supporting evidence:

- The chunk reads the father as `Jose del Carmen Pulgar S.`, Chilean, employed, domiciled at `Calle de Colipi`.
- The source packet's image check says the father field appears to begin `Jose del Carmen Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` is a separate stub with a draft child link to `Tulio Cesar Luis Jose` from another entry; that context makes this a Jose/Pulgar duplicate-person risk, not a merge.

Conflicts and limits:

- The suffix `S.` is not certified.
- The existing Jose del Carmen Pulgar canonical stub is tied to a different staged entry/person cluster (`Tulio Cesar Luis Jose`) and should not be merged with the entry-172 father by name alone.
- This entry does not state the father's age, spouse relationship beyond parent-field context, or direct relationship to any Dario candidate.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Page-local father candidate is likely if Pulgar row controls, but exact name form is unresolved. |
| conflict_severity | 0.78 | Suffix uncertainty and possible duplicate Jose del Carmen Pulgar candidates affect parent identity. |
| evidence_quality | 0.64 | Birth-register parent field is useful but not yet QA-certified. |
| conversion_confidence | 0.40 | Depends on resolving the row-control and suffix conflict. |
| claim_probability | 0.60 | Probable page-local father, not a proven merge to existing Jose page. |
| relevance | 0.96 | Direct parent candidate. |
| canonical_readiness | 0.10 | Hold for targeted father-field QA and Jose parent-candidate proof review. |

## Hypothesis 4: Mother Candidate `Juana Arriagada de Pulgar`

Hypothesis: the entry-172 mother is the page-local parent candidate `Juana Arriagada de Pulgar`.

Supporting evidence:

- The assigned chunk and source packet both name mother `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, domiciled at `Calle de Colipi`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` contains an entry-172-derived probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts and limits:

- This mother evidence remains blocked by the row-control conflict.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate candidate tied to `Tulio Cesar Luis Jose`; the names are not equivalent and should not be merged without separate image/proof review.
- The record does not connect Juana Arriagada de Pulgar to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Stronger page-local mother reading if Pulgar row controls. |
| conflict_severity | 0.72 | Main issue is row control plus possible confusion with other Juana/Pulgar candidates. |
| evidence_quality | 0.66 | Specific birth-register mother field, pending QA. |
| conversion_confidence | 0.42 | Depends on accepting the Pulgar/Arriagada row. |
| claim_probability | 0.68 | Probable page-local mother, not a proven duplicate of other Juana candidates. |
| relevance | 0.96 | Direct parent candidate. |
| canonical_readiness | 0.12 | Hold for conversion QA and parent-candidate review. |

## Pulgar-Line Anti-Conflation Comparison

`Dario Arturo Pulgar-Smith`: existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to attach Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review. This entry does not name Dario Arturo or Smith.

`Dario Arturo Pulgar`: existing staged CV context supports a document-level `Dario Arturo Pulgar` identity in CV materials. This entry does not name Dario Arturo Pulgar, contain CV context, or provide an occupation/date bridge to that cluster.

`Dario Jose Pulgar-Arriagada`: staged photograph and archival-source contexts name Dario Jose Pulgar-Arriagada, but this entry names a child `Jose del Carmen Segundo Pulgar Arriagada`. Shared Pulgar/Arriagada surname elements are insufficient for identity merger.

`Dario/Dario Pulgar Arriagada`: existing staged/canonical context includes `Dario Pulgar Arriagada`, `Dario Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dr Dario Pulgar A.`, and a canonical `Darío Pulgar Arriagada` expropriation-event stub. Entry 172 is an 1888 birth-registration conflict for a differently named child and gives no Dario-specific event.

Jose/Juana parent candidates: entry 172 directly concerns possible parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. Existing context also has `Juana de Dios Amagada de Pulgar` and another `Jose del Carmen Pulgar` cluster from a different entry. These are relevant duplicate/relationship-conflict candidates but should remain separate until side-by-side proof review confirms whether the records concern the same parents, siblings, duplicate rows, or unrelated Pulgar families.

Ranked Pulgar-line hypotheses:

| rank | hypothesis | probability | required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 directly supports page-local `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`/`Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`. | 0.72 | Targeted conversion QA for row control and father suffix; then proof-review child, birth, father, mother, and parent-child claims. |
| 2 | Entry-172 father/mother may duplicate or relate to other Jose/Juana Pulgar parent candidates. | 0.38 | Side-by-side proof review of the relevant Jose/Juana register entries before any merge or relationship promotion. |
| 3 | Entry 172 has indirect lineage relevance to later Pulgar/Arriagada family research but no current Dario identity attachment. | 0.18 | Revisit only after a reviewed source bridges this child or parents to a later Dario-line person. |
| 4 | Entry 172 supports any same-person merge with `Dario Arturo Pulgar-Smith` or `Dario Arturo Pulgar`. | 0.04 | Require direct identity bridge naming Dario/Arturo/Smith or a documented chain from child/parents to the canonical Dario person. |
| 5 | Entry 172 supports any same-person merge with `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío Pulgar Arriagada`. | 0.03 | Preserve separately; require full-name, date, occupation, residence, parentage, or other direct continuity evidence. |

## Conflict Types

- Same-person conflict: unresolved only for page-local parent candidates versus existing Jose/Juana stubs; no same-person basis for any Dario cluster.
- Duplicate-person conflict: high risk if entry-172 `Jose del Carmen Pulgar` is merged with another Jose del Carmen Pulgar stub by name alone; high risk if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar` by surname/married-name context alone.
- Name-variant conflict: father may be `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`; Dario/Pulgar surname variants are not resolved by this entry.
- Relationship conflict: parent-child relationships for the Pulgar/Arriagada reading conflict with the Burgos/de la Cruz converted-text family.
- Chronology conflict: the two readings give different birth dates and times, 8 March 1888 at 3 p.m. versus 6 April 1888 at 10 p.m.; these should not be normalized.

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md` at `hold_for_conversion_qa`.

Exact next proof-review step: targeted conversion QA must compare the source image, assigned chunk, and converted Markdown for `CHUNK-b8f4f0490a36-P0001-01`; certify whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row; and settle the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review on the child identity, birth date/time/place, father, mother, informant, and parent-child relationship drafts. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` unless a later reviewed identity bridge supplies direct support.
