---
type: identity_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526085712831
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Conversion Conflict Held

## Blockers First

- The exact staged draft under review is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md`.
- The assigned chunk and held source packet support an entry-172 Pulgar/Arriagada row, while the current converted Markdown for the same source path records a different Burgos/de la Cruz row. This is a row-level conversion conflict, not a spelling or name-variant conflict.
- The father field in the Pulgar/Arriagada reading remains uncertified. The staged packet reports `Jose del Carmen Pulgar` followed by possible `S.` or another terminal mark.
- Existing canonical context includes `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar` staging, `Dario Jose Pulgar-Arriagada` staging, canonical `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; this entry does not bridge them by itself.
- No merge, rename, promoted parentage, Dario-line attachment, or father-name normalization is ready until targeted conversion QA resolves the controlling row and proof review accepts the result.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Canonical wiki context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`.
- Local staged/review context found by text search for `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar A.`, `Dario Pulgar Arriagada`, and `Pulgar-Smith`.

## Literal Source Readings

### Reading A: Assigned Chunk And Source Packet

The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`. The staged source packet says source-image review visually aligns with this Pulgar/Arriagada row, while leaving the father-name ending uncertified.

### Reading B: Current Converted Markdown

The current converted Markdown records entry 172 as `José Miguel`, male, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

## Hypothesis 1: Entry 172 Controls To The Pulgar/Arriagada Row

Evidence supporting:

- The assigned chunk and held source packet independently stage entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`.
- The held source packet reports source-image alignment with the Pulgar/Arriagada row.
- The Pulgar/Arriagada row is internally coherent: child, father, mother, residence, birth date/place, and informant are all supplied.

Evidence against or limiting:

- The current converted Markdown materially conflicts on child name, parents, birth date, birth place, and informant.
- The father field's terminal mark is not certified.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Strong staged chunk/source-packet support, reduced by the live derivative conflict. |
| conflict_severity | 0.95 | The competing row names a different child and different parents. |
| evidence_quality | 0.72 | Civil register evidence is strong in principle, but derivative control is unsettled. |
| conversion_confidence | 0.35 | QA has not resolved the row-control problem. |
| claim_probability | 0.66 | Probable but not promotion-ready. |
| relevance | 0.90 | High Pulgar/Arriagada relevance if certified. |
| canonical_readiness | 0.10 | Hold only. |

## Hypothesis 2: Entry 172 Controls To The Burgos/de la Cruz Row

Evidence supporting:

- The current converted Markdown explicitly places the Burgos/de la Cruz family under entry 172.

Evidence against or limiting:

- The conflict draft and source packet treat that derivative reading as conflicting with the assigned chunk and source-image review.
- The Burgos/de la Cruz reading has no Pulgar-line support in the reviewed staging evidence.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.28 | Present in one derivative transcript, but challenged by the assigned chunk/source packet. |
| conflict_severity | 0.95 | If correct, it displaces every Pulgar/Arriagada claim for entry 172. |
| evidence_quality | 0.35 | Derivative transcript only in this review state. |
| conversion_confidence | 0.25 | Current conversion is specifically under row-level challenge. |
| claim_probability | 0.24 | Possible, but currently weaker than the staged Pulgar reading. |
| relevance | 0.15 | Low Pulgar-line relevance except as the competing control row. |
| canonical_readiness | 0.00 | Not ready. |

## Hypothesis 3: Entry 172 Supports Jose/Juana Parent Candidates

Hypothesis: if Reading A controls, `Jose del Carmen Segundo Pulgar Arriagada` is the child of `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`.

Evidence supporting:

- The assigned chunk names the child, father, and mother in one civil birth-registration row.
- Canonical `Juana Arriagada de Pulgar` already has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`, and canonical `Jose del Carmen Segundo Pulgar Arriagada` already carries staged entry-172 life facts.
- Canonical `Jose del Carmen Pulgar` exists as a local parent-candidate page, though the inspected snapshot does not certify him as the entry-172 father.

Evidence against or limiting:

- Parent-child claims depend entirely on resolving the row conflict in favor of Reading A.
- The father-name ending must not be silently collapsed from `Pulgar S.` or `Pulgar [?]` to canonical `Jose del Carmen Pulgar`.
- Existing canonical snippets are not enough to promote a fresh relationship from this held conflict draft.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Coherent if the Pulgar row is certified. |
| conflict_severity | 0.85 | Parentage would be wrong if the Burgos row controls. |
| evidence_quality | 0.68 | Strong record type, held back by conversion uncertainty. |
| conversion_confidence | 0.35 | Father field and row control need QA. |
| claim_probability | 0.55 | Conditional probability after Reading A certification. |
| relevance | 0.88 | High for Pulgar/Arriagada parent-candidate work. |
| canonical_readiness | 0.10 | Hold pending QA and proof review. |

## Hypothesis 4: Entry 172 Bridges To Dario-Line Candidates

Candidates explicitly compared:

- `Dario Arturo Pulgar-Smith`: the canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against attaching Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review.
- `Dario Arturo Pulgar`: local CV staging uses this document-level name, but reviewed notes require a separate bridge before attaching it to `Dario Arturo Pulgar-Smith`.
- `Dario Jose Pulgar-Arriagada`: local staged context preserves this as a separate Pulgar-Arriagada candidate, not bridged to entry 172.
- `Darío J. Pulgar Arriagada`: staged medical-title context exists, but `J.` is not expanded here and no parent or birth bridge appears in the reviewed entry-172 material.
- `Dario/Darío Pulgar Arriagada`: canonical and staged contexts include later Pulgar Arriagada references, including a 2000 event for canonical `Darío Pulgar Arriagada`, but no reviewed source ties those references to this 1888 child.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar` may become parent candidates only for the entry-172 child after QA; they are not proven parents or ancestors of any Dario candidate here.

Evidence supporting:

- If the Pulgar/Arriagada row controls, the surname pair is relevant enough to flag for later Pulgar-line comparison.

Evidence against or limiting:

- The entry-172 child is named `Jose del Carmen Segundo`, not Dario, Arturo, Dario Jose, or Darío J.
- The entry does not mention `Smith`, `Pulgar-Smith`, Alexander John Heinz, a spouse, a child, a medical role, a CV, a Geneva/ICRC context, property, or any later Dario identifying details.
- No reviewed local source supplies the intermediate lineage or same-person bridge needed to connect the entry-172 child or parents to any Dario candidate.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | No direct name or relationship bridge. |
| conflict_severity | 0.75 | Premature attachment would contaminate several Pulgar clusters. |
| evidence_quality | 0.30 | Only broad surname/context overlap. |
| conversion_confidence | 0.35 | Entry 172 itself is still held. |
| claim_probability | 0.06 | Anti-conflation lead only. |
| relevance | 0.70 | Relevant for future Pulgar-line review after QA. |
| canonical_readiness | 0.00 | Not ready. |

## Conflict Summary

- Same-person conflict: no same-person conclusion is supported between `Jose del Carmen Segundo Pulgar Arriagada` and any Dario-line person.
- Duplicate-person conflict: no duplicate decision is supported; preserve `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, and Jose/Juana parent candidates separately.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must not be normalized to `Jose del Carmen Pulgar` until father-field QA; `Dario Arturo`, `Dario Jose`, `Darío J.`, `Dario Pulgar A.`, `Pulgar-Smith`, and `Pulgar Arriagada` are not proved variants of the entry-172 child.
- Relationship conflict: possible child-parent links for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]`, and `Juana Arriagada de Pulgar` are conditional on Reading A.
- Chronology conflict: Reading A gives birth on 1888-03-08 at 3 p.m.; Reading B gives birth on 1888-04-06 at 10 p.m. They cannot both describe the same entry-172 child and parents.

## Ranked Conclusions

| Rank | Hypothesis | Probability | Next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 probably controls to the Pulgar/Arriagada row. | 0.66 | Targeted conversion QA must certify row alignment and father field. |
| 2 | Entry 172 may control to the Burgos/de la Cruz row. | 0.24 | Preserve as competing derivative reading until QA resolves it. |
| 3 | `Jose del Carmen Segundo Pulgar Arriagada` is child of `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`. | 0.55 conditional | Only after Reading A is certified, run proof review on child identity, birth facts, father, mother, and parent-child claims. |
| 4 | Entry 172 directly bridges to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`. | 0.06 | Do not promote; require a separate identity-bridge proof review with direct Dario evidence and intermediate lineage evidence. |

## Recommended Next Action

Run targeted conversion QA on register page 58, entry 172. The QA must decide whether the controlling row is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and must certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth date/place, father/mother attributes, parent-child relationship, or Dario-line comparison. The next Pulgar-line step, if the Pulgar row is certified, is a separate identity-bridge proof review comparing certified entry-172 evidence against the Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Darío Pulgar Arriagada, and Jose/Juana parent-candidate clusters.
