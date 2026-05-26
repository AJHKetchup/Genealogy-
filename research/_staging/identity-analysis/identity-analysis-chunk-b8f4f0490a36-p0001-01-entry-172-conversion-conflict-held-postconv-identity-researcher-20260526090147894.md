---
type: identity_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526090147894
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Conversion Conflict Held

## Blockers First

- The exact staged draft reviewed here is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md`.
- The assigned chunk/source packet and the current converted Markdown do not identify the same entry-172 row. This is a row-control conversion conflict, not a name-variant or ordinary duplicate-person question.
- The assigned chunk and held source packet support `Jose del Carmen Segundo Pulgar Arriagada`; the current converted Markdown supports `José Miguel` with Burgos/de la Cruz parents.
- The father field in the Pulgar/Arriagada reading is not fully certified. It must remain one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted conversion QA.
- No Dario-line merge, surname normalization, canonical promotion, or parent-child relationship promotion is ready from this draft.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing wiki context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`.
- Prior local proof-review context for this entry, including `research/_staging/reviews/proof-review-research-staging-identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-proof-review-20260526000348338.md`.

## Literal Source Readings

### Reading A: Assigned Chunk And Held Source Packet

The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`. The held source packet says the source image visually aligns with this Pulgar/Arriagada row, while leaving the father-name ending uncertified.

### Reading B: Current Converted Markdown

The current converted Markdown records entry 172 as `José Miguel`, male, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

## Hypothesis 1: Entry 172 Controls To The Pulgar/Arriagada Row

Evidence supporting:

- The assigned chunk and held source packet both stage entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`.
- The source packet reports visual alignment with the Pulgar/Arriagada row on register page 58, entry 172.
- The row is internally coherent: child, sex, birth date/time, birth place, father, mother, residence, and informant are supplied.
- Existing wiki pages already preserve `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` as probable, low-confidence staged links tied to this entry, which shows local relevance but does not independently resolve the conflict.

Evidence against or limiting:

- The current converted Markdown materially conflicts with the assigned chunk on child name, parents, birth date, birth place, and informant.
- The father-name ending after `Pulgar` remains a conversion-QA issue.
- The existing wiki snapshot reflects staged evidence and cannot be used to promote the held reading without QA.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | The Pulgar row is supported by the assigned chunk and source packet, but the derivative conversion conflict remains unresolved. |
| conflict_severity | 0.95 | Competing readings name different children, parents, dates, places, and informants. |
| evidence_quality | 0.72 | Civil birth registration is strong evidence in principle; current control state is not stable. |
| conversion_confidence | 0.35 | Targeted QA has not reconciled the converted Markdown with the chunk/source-packet reading. |
| claim_probability | 0.66 | Probable enough to prioritize QA, not enough for promotion. |
| relevance | 0.90 | High for Pulgar/Arriagada family work if certified. |
| canonical_readiness | 0.10 | Hold only. |

## Hypothesis 2: Entry 172 Controls To The Burgos/de la Cruz Row

Evidence supporting:

- The current converted Markdown explicitly assigns entry 172 to `José Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.

Evidence against or limiting:

- The staged conflict draft and source packet identify the converted Markdown row as the challenged derivative reading.
- The Burgos/de la Cruz row has no Pulgar-line relevance in the reviewed local evidence except as the competing control row.
- The prior proof-review context also held the draft for conversion QA rather than accepting the converted Markdown as controlling.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.28 | Present in one derivative transcript, but directly challenged by the assigned chunk and source-packet image check. |
| conflict_severity | 0.95 | If this row controls, all Pulgar/Arriagada entry-172 claims are displaced. |
| evidence_quality | 0.35 | Reviewed support is derivative and contested. |
| conversion_confidence | 0.25 | The converted file is the object of the row-level conflict. |
| claim_probability | 0.24 | Possible, but currently weaker than the Pulgar/Arriagada staged reading. |
| relevance | 0.15 | Low for Pulgar-line work except as a blocker. |
| canonical_readiness | 0.00 | Not ready. |

## Hypothesis 3: Entry 172 Supports Jose/Juana Parent Candidates

Hypothesis: if Reading A controls, `Jose del Carmen Segundo Pulgar Arriagada` is the child of a father recorded as `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` and a mother recorded as `Juana Arriagada de Pulgar`.

Evidence supporting:

- The assigned chunk gives child, father, and mother in the same civil birth-registration row.
- The mother form `Juana Arriagada de Pulgar` is literal in the assigned chunk/source packet.
- Existing canonical pages preserve separate candidate pages for `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada`, which helps prevent a silent merge.

Evidence against or limiting:

- This parentage is conditional on Reading A being certified as the controlling row.
- The father should not be silently normalized from `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` to canonical `Jose del Carmen Pulgar`.
- Existing canonical `Jose del Carmen Pulgar` also has a separate draft child link to `Tulio Cesar Luis Jose`, so parent-candidate comparison should remain explicit and source-specific.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Coherent if the Pulgar row is certified; not proved while row control and father suffix remain open. |
| conflict_severity | 0.85 | Wrong row control would create false parent-child links. |
| evidence_quality | 0.68 | Strong record type, held back by conversion uncertainty. |
| conversion_confidence | 0.35 | Row control and father ending require QA. |
| claim_probability | 0.55 | Conditional probability only. |
| relevance | 0.88 | High for Jose/Juana and Pulgar/Arriagada parent-candidate work. |
| canonical_readiness | 0.10 | Hold pending QA and proof review. |

## Hypothesis 4: Entry 172 Bridges To Dario-Line Candidates

Candidates explicitly compared:

- `Dario Arturo Pulgar-Smith`: existing canonical page is family supplied as Alexander John Heinz's maternal grandfather and warns not to attach Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review.
- `Dario Arturo Pulgar`: local CV staging uses this document-level name, but existing reviews require a separate bridge before attachment to `Dario Arturo Pulgar-Smith`.
- `Dario Jose Pulgar-Arriagada`: local staged photo/ICRC contexts preserve this name as a separate candidate, often with metadata-only or image-identity limitations.
- `Darío J. Pulgar Arriagada` and `Dario Pulgar A.`: staged medical/title and name-form contexts exist, but `J.` and `A.` are not expanded by this entry.
- `Dario/Darío Pulgar Arriagada`: the existing canonical `wiki/people/dar-o-pulgar-arriagada.md` is a narrow 2000 expropriation/event stub and is not bridged to this 1888 entry.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar` may become parent candidates for the entry-172 child only after QA; this entry does not prove them as parents or ancestors of any Dario candidate.

Evidence supporting:

- If the Pulgar/Arriagada row controls, the surname pair is relevant enough to flag for later Pulgar-line comparison.

Evidence against or limiting:

- Entry 172 names `Jose del Carmen Segundo`, not Dario, Arturo, Dario Jose, Darío J., or Dario Pulgar A.
- The entry does not mention `Smith`, `Pulgar-Smith`, Alexander John Heinz, a spouse, a child, a medical role, a CV, Geneva/ICRC, property, travel, or any later Dario identifying detail.
- No reviewed local source supplies the intermediate lineage or same-person bridge needed to connect the entry-172 child or parents to any Dario candidate.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | No direct Dario name, relationship, chronology, or bridge evidence. |
| conflict_severity | 0.75 | Premature attachment would contaminate several Pulgar clusters. |
| evidence_quality | 0.30 | Only broad surname/context overlap. |
| conversion_confidence | 0.35 | Entry 172 itself remains held. |
| claim_probability | 0.06 | Anti-conflation lead only. |
| relevance | 0.70 | Relevant as a future comparison point only if QA certifies the Pulgar row. |
| canonical_readiness | 0.00 | Not ready. |

## Conflict Summary

- Same-person conflict: no same-person conclusion is supported between `Jose del Carmen Segundo Pulgar Arriagada` and any Dario-line person.
- Duplicate-person conflict: preserve separately `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar A.`, `Dario/Darío Pulgar Arriagada`, and Jose/Juana parent candidates.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must not be normalized to `Jose del Carmen Pulgar` until father-field QA; Dario/Pulgar-Smith/Pulgar-Arriagada forms are not proved variants from this entry.
- Relationship conflict: possible child-parent links for `Jose del Carmen Segundo Pulgar Arriagada`, the father candidate, and `Juana Arriagada de Pulgar` depend entirely on Reading A.
- Chronology conflict: Reading A gives birth on 1888-03-08 at 3 p.m.; Reading B gives birth on 1888-04-06 at 10 p.m. These cannot both describe the same child and parent set for entry 172.

## Ranked Conclusions

| Rank | Hypothesis | Probability | Exact next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 probably controls to the Pulgar/Arriagada row. | 0.66 | Targeted conversion QA must certify row alignment and father field against the source image, chunk, converted file, and source packet. |
| 2 | Entry 172 may control to the Burgos/de la Cruz row. | 0.24 | Preserve as the competing derivative reading until QA resolves row control. |
| 3 | `Jose del Carmen Segundo Pulgar Arriagada` is child of `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`. | 0.55 conditional | After Reading A is certified, run proof review on child identity, birth facts, father, mother, and parent-child claims before promotion. |
| 4 | Entry 172 directly bridges to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar A.`, or `Dario/Darío Pulgar Arriagada`. | 0.06 | Do not promote; require a separate identity-bridge proof review with direct Dario evidence and intermediate lineage/identity evidence. |

## Recommended Next Action

Keep the staged draft at `hold_for_conversion_qa`.

Run targeted conversion QA for register page 58, entry 172. QA must decide whether the controlling row is the Pulgar/Arriagada row or the Burgos/de la Cruz row and must certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth date/place, father/mother attribute, parent-child relationship, duplicate-person decision, or Dario-line comparison. If the Pulgar row is certified, the next Pulgar-line step is a separate identity-bridge proof review comparing the certified entry-172 evidence against the Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío J./Dario Pulgar A., Dario/Darío Pulgar Arriagada, and Jose/Juana parent-candidate clusters.
