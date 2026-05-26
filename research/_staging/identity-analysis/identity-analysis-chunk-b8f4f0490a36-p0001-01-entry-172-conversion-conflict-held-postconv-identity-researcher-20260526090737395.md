---
type: identity_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526090635826
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
conflict_type: conversion_row_conflict
canonical_readiness: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Conversion Conflict Hold

## Blockers First

- Do not promote child identity, birth facts, parent-child relationships, parent-candidate merges, or Dario-line comparisons from the staged conflict draft. The current converted Markdown and the assigned chunk give materially different people for entry 172.
- The current converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`. The assigned chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at Calle de Valdivia.
- The father-name ending after `Jose del Carmen Pulgar` remains uncertified. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as competing literal readings until targeted conversion QA decides the source-visible text.
- Existing canonical pages already contain auto-generated evidence derived from this chunk for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`; this analysis does not validate further promotion while the conversion-row conflict remains unresolved.

## Literal Source Readings

- Assigned chunk/source-packet reading: entry 172 names child `Jose del Carmen Segundo Pulgar Arriagada`, male; registration date 7 April 1888; birth date 8 March 1888 at 3 p.m.; birthplace Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at the birth.
- Staged conflict's image-check interpretation: the source image visually aligns with the Pulgar/Arriagada row, but the final father-name mark after `Pulgar` needs QA certification.
- Current converted Markdown reading: entry 172 names child `Jose Miguel`, male; born 6 April 1888 at 10 p.m.; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

## Hypotheses And Evidence

| Rank | Hypothesis | Supporting evidence | Conflicts | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by the assigned chunk, source packet, and staged conflict image-check summary. Names, parents, residence, and informant form a coherent birth-register row. | Current converted Markdown gives a different child, parents, birth date, and informant. Father suffix remains uncertain. | 0.72 |
| 2 | Entry 172 is the Burgos/de la Cruz registration for `Jose Miguel`. | Supported only by the current converted Markdown artifact. | Contradicted by the assigned chunk and staged source-packet/image-check reading for the same page reference and chunk id. | 0.22 |
| 3 | The Pulgar/Arriagada and Burgos/de la Cruz readings are duplicate or variant readings of the same person/family. | None beyond shared entry number in derivative artifacts. | Names, parents, dates, places, and informants are materially different; this is not a normal name variant. | 0.03 |
| 4 | The entry directly identifies or bridges a Dario-line person. | No direct support. | The staged draft, chunk, and converted file do not name Dario, Arturo, Smith, or a later-life bridge. | 0.04 |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: existing canonical page is family-supplied and warns against attaching similarly named Pulgar records without identity review. Entry 172 does not name Dario Arturo Pulgar-Smith, Smith, a grandchild, spouse, occupation, or date range that bridges to this person.
- `Dario Arturo Pulgar`: no direct support in the staged draft. The entry concerns either a Pulgar/Arriagada birth cluster or a Burgos/de la Cruz converted-file row, not a Dario Arturo identity.
- `Dario Jose Pulgar-Arriagada`: no direct support. The child name in the Pulgar hypothesis is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose.
- `Dario/Dario Pulgar Arriagada`: no direct support. Existing canonical context includes a separate `Darío Pulgar Arriagada` property/expropriation cluster, but this 1888 entry does not provide a same-person bridge.
- Jose/Juana parent candidates: the Pulgar hypothesis supports possible parents `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` only after conversion QA. Do not merge either parent candidate to broader Jose/Juana pages from this draft alone.

## Conflicts

- Same-entry conflict: chunk/source-packet/image-check reading and converted Markdown identify wholly different families for page 58, entry 172.
- Name-form conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar [?]` remains unresolved.
- Canonical exposure conflict: existing canonical snapshots include some auto-generated evidence from this chunk, but the current staged conflict requires hold status until the conversion layer is reconciled.
- Chronology conflict between hypotheses: Pulgar reading gives birth 8 March 1888; converted Markdown gives birth 6 April 1888.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Moderate for a discrete Pulgar/Arriagada row being present, but low for any final canonical identity action until conversion QA resolves the row conflict. |
| conflict_severity | 0.95 | The disagreement changes child, parents, birth date, place, and informant. |
| evidence_quality | 0.78 | Civil birth registration is strong evidence if the row is certified; current review uses staged/chunk/converted derivatives plus local canonical context. |
| conversion_confidence | 0.34 | The controlling conversion artifacts disagree materially. |
| claim_probability | 0.72 | Pulgar/Arriagada is the leading hypothesis from the assigned chunk and image-check note, but not promotion-ready. |
| relevance | 0.88 | Highly relevant to Pulgar/Arriagada family reconstruction; not directly relevant to Dario identity without later bridge evidence. |
| canonical_readiness | 0.10 | Hold for conversion QA and rerun proof review. |

## Recommended Next Action

Run targeted conversion QA for page 58, entry 172 against the source image, current converted Markdown, assigned chunk, and source packet. The QA step must certify the controlling row and father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent merge, or Dario-line comparison.
