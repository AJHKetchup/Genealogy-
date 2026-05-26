---
type: identity_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526085239273
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The assigned chunk and held source packet support an entry-172 Pulgar/Arriagada row, while the current converted Markdown for the same source path records a different Burgos/de la Cruz row. This is a row-level conversion conflict, not a normal name variant.
- The father field in the Pulgar/Arriagada reading is not fully certified. The held source packet says the image appears to read `Jose del Carmen Pulgar` followed by a possible `S.` or other terminal mark.
- Existing canonical pages already contain staged/probable links for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, but this new conflict draft requires dependent claims and relationships to remain held until conversion QA resolves the controlling row.
- No same-person bridge is present from entry 172 to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, or the 2000 `Darío Pulgar Arriagada` canonical stub.
- Do not merge, rename, promote parentage, or normalize `Jose del Carmen Pulgar S.` to canonical `Jose del Carmen Pulgar` until targeted conversion QA and proof review certify the row and father name.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md`.
- Held source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`.
- Existing staged context located by local search for `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, and related Pulgar name-form watches.

## Literal Source Readings

### Reading A: Assigned Chunk And Held Source Packet

The assigned chunk transcribes entry 172 as:

```text
Jose del Carmen Segundo Pulgar Arriagada
```

with birth on `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.

The held source packet repeats this reading and adds that source-image review visually aligns with the Pulgar/Arriagada row, while leaving the father-name ending uncertified.

### Reading B: Current Converted Markdown

The current converted Markdown records entry 172 as `José Miguel`, male, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

## Hypotheses

### Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Evidence supporting:

- The assigned chunk and held source packet both identify entry 172 on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`.
- The held source packet reports direct source-image alignment with the Pulgar/Arriagada row.
- Names, parents, residence, and informant are internally coherent within the assigned chunk.

Evidence against or limiting:

- The current converted Markdown for the same converted file conflicts materially and gives a different child, parents, birth date, and place.
- The father-name terminal mark remains uncertain.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Strong staged chunk/source-packet alignment, reduced by unreconciled derivative conflict. |
| conflict_severity | 0.95 | Different child and parents for the same entry number. |
| evidence_quality | 0.72 | Civil registration evidence is strong in principle, but current text state is conflicted. |
| conversion_confidence | 0.35 | Conversion QA has not resolved which row controls. |
| claim_probability | 0.66 | Probable as the correct row, not ready for promotion. |
| relevance | 0.90 | High Pulgar/Arriagada family relevance if certified. |
| canonical_readiness | 0.10 | Hold only. |

### Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Evidence supporting:

- The current converted Markdown explicitly presents the Burgos/de la Cruz row under entry 172.

Evidence against or limiting:

- The staged conflict draft and held source packet both say source-image review supports the Pulgar/Arriagada row instead.
- The Burgos/de la Cruz reading has no Pulgar-line relevance and conflicts with assigned chunk metadata and source-packet review.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.28 | Present in one derivative transcript, but contradicted by the assigned chunk/source-packet review. |
| conflict_severity | 0.95 | If accepted, it displaces every Pulgar/Arriagada claim for this entry. |
| evidence_quality | 0.35 | Derivative transcript only, currently challenged. |
| conversion_confidence | 0.25 | The conflict draft specifically treats this as the problematic derivative reading. |
| claim_probability | 0.24 | Possible but less likely under current staged evidence. |
| relevance | 0.15 | Low Pulgar-line relevance except as the conflicting control row. |
| canonical_readiness | 0.00 | Not ready for promotion. |

### Hypothesis 3: `Jose del Carmen Segundo Pulgar Arriagada` Is A Child Of `Jose del Carmen Pulgar S.` And `Juana Arriagada de Pulgar`

Evidence supporting:

- The assigned chunk states a child named `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
- The mother candidate has an existing canonical stub with a probable child link to this child, though that existing snapshot should remain subordinate to the new hold.
- The child has an existing canonical stub with life facts and a probable mother link sourced to an earlier entry-172 source packet.

Evidence against or limiting:

- The parent-child relationship depends entirely on accepting the Pulgar/Arriagada row as the controlling entry-172 reading.
- The father candidate `Jose del Carmen Pulgar` has an existing child link to `Tulio Cesar Luis Jose`, not a certified entry-172 child link in the reviewed canonical snapshot inspected here.
- The possible `S.` after the father's surname could be an initial, mark, or misread; it should not be silently dropped.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Coherent if Reading A is certified; currently blocked by row conflict. |
| conflict_severity | 0.85 | Parentage would be wrong if the Burgos/de la Cruz row controls. |
| evidence_quality | 0.68 | Strong record type, but derivative control is unsettled. |
| conversion_confidence | 0.35 | Father field and controlling row need QA. |
| claim_probability | 0.55 | Plausible/probable only after Reading A survives QA. |
| relevance | 0.88 | High for Pulgar/Arriagada parent-candidate work. |
| canonical_readiness | 0.10 | Hold; no promotion. |

### Hypothesis 4: Entry 172 Child Is A Same-Person Or Direct Ancestor Bridge To Dario-Line Candidates

Candidates explicitly compared:

- `Dario Arturo Pulgar-Smith`: canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns not to attach Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review.
- `Dario Arturo Pulgar`: staged CV context exists locally, but those notes generally treat `Dario Arturo Pulgar` as document-level CV attribution needing a bridge to `Dario Arturo Pulgar-Smith`.
- `Dario Jose Pulgar-Arriagada`: staged portrait/Geneva source-context notes exist, but the notes found locally do not establish a bridge to entry 172 or to the child `Jose del Carmen Segundo`.
- `Darío J. Pulgar Arriagada`: staged university/medical-title notes record the name form, with `J.` unexpanded and no parents or age in the local watch notes.
- `Dario/Darío Pulgar Arriagada`: staged and canonical contexts include military/medical, Geneva, and 2000 expropriation-style mentions, but no local bridge to entry 172 was found in the reviewed materials.
- Jose/Juana parent candidates: entry 172's possible parents are `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; these cannot be treated as parents or grandparents of any Dario candidate without an intermediate proof-reviewed lineage bridge.

Evidence supporting:

- Entry 172, if Pulgar/Arriagada, may be part of the same broad surname cluster and may justify future lineage comparison.

Evidence against or limiting:

- The entry-172 child is named `Jose del Carmen Segundo`, not Dario.
- No reviewed local source states that `Jose del Carmen Segundo Pulgar Arriagada` is the same person as any Dario candidate.
- No reviewed local source connects `Jose del Carmen Pulgar S.` or `Juana Arriagada de Pulgar` as parents, grandparents, or other relatives of any Dario candidate.
- Chronology cannot be safely interpreted until the birth row is certified and an intermediate relationship chain is found.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Name and relationship bridge are absent. |
| conflict_severity | 0.75 | A premature merge would contaminate multiple Pulgar-line clusters. |
| evidence_quality | 0.30 | Only broad local context and surname overlap. |
| conversion_confidence | 0.35 | Entry 172 is still under conversion QA hold. |
| claim_probability | 0.06 | Not supported beyond a double-check lead. |
| relevance | 0.70 | Relevant as a future Pulgar-line lead after QA. |
| canonical_readiness | 0.00 | Not ready. |

## Conflict Summary

- Same-person conflict: no supported same-person conclusion between entry-172 child `Jose del Carmen Segundo Pulgar Arriagada` and any Dario-line person.
- Duplicate-person conflict: no duplicate-person decision is supported; all Dario/Pulgar-Arriagada clusters remain separate unless bridged by proof-reviewed evidence.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must not be normalized to `Jose del Carmen Pulgar` without father-field QA; `Dario Jose`, `Dario J.`, `Dario Arturo`, `Dario Pulgar`, and `Pulgar-Smith` forms are not variants of this entry-172 child on current evidence.
- Relationship conflict: possible parent-child links for `Jose del Carmen Segundo Pulgar Arriagada` depend on resolving the row conflict.
- Chronology conflict: the staged Pulgar row reports birth on 1888-03-08; the converted Burgos row reports birth on 1888-04-06. These cannot both describe the same child and family for entry 172.

## Ranked Conclusion

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 probably controls to the Pulgar/Arriagada row after source-image QA. | 0.66 | Hold for targeted conversion QA and father-field certification. |
| 2 | Entry 172 may control to the Burgos/de la Cruz derivative row. | 0.24 | Preserve as competing reading until QA resolves row alignment. |
| 3 | `Jose del Carmen Segundo Pulgar Arriagada` is child of `Jose del Carmen Pulgar S.`/`Juana Arriagada de Pulgar`. | 0.55 conditional | Consider only if Rank 1 is certified; then run proof review before promotion. |
| 4 | Entry 172 provides a Dario-line same-person or direct relationship bridge. | 0.06 | Do not use; only flag for later lineage review after row QA and intermediate evidence. |

## Recommended Next Action

Run targeted conversion QA on the source image and row alignment for register page 58, entry 172. The QA result must explicitly decide whether the controlling row is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and must certify the father field as one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that, run proof review before promoting any child identity, birth date/place, father/mother attributes, parent-child relationship, or Dario-line comparison. The required next Dario-line promotion step is a separate identity-bridge proof review that connects a certified entry-172 person or Jose/Juana parent candidate to a specific Dario candidate with direct evidence, not name overlap.
