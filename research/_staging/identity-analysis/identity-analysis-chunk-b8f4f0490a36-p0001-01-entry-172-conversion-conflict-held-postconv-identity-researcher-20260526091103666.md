---
type: identity_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526091103666
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

- Do not promote identity, birth, parentage, relationship, duplicate-person, or Dario-line conclusions from this staged draft. The assigned chunk/source-packet reading and the current converted Markdown identify different children, parents, birth dates, places, and informants for the same page/reference.
- The controlling entry-172 row is unresolved. The assigned chunk and source packet support a Pulgar/Arriagada row; the current converted Markdown supports a Burgos/de la Cruz row.
- The father field in the Pulgar/Arriagada reading remains image-sensitive after `Jose del Carmen Pulgar`. Keep `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` separate until targeted conversion QA certifies the literal reading.
- Existing canonical pages already contain some auto-generated evidence derived from this chunk for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`; this note does not validate further promotion while the row-level conversion conflict is open.

## Literal Source Readings

- Assigned chunk/source packet: entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, male; registered 7 April 1888; born 8 March 1888 at 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at the birth.
- Staged conflict image-check statement: the source image visually supports the Pulgar/Arriagada row, but the terminal mark after `Jose del Carmen Pulgar` requires targeted QA.
- Current converted Markdown: entry 172 records `Jose Miguel`, male; born 6 April 1888 at 10 p.m. in `En esta`; father and informant `Oswaldo Burgos`; mother `Concepcion de la Cruz`.

## Hypotheses

| Rank | Hypothesis | Evidence supporting | Conflicts | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by the assigned chunk, source packet, and staged image-check summary. The child, parents, residence, and informant form a coherent row. | Contradicted by the current converted Markdown; father-name suffix remains uncertified. | 0.72 |
| 2 | Entry 172 is the Burgos/de la Cruz birth registration for `Jose Miguel`. | Supported by the current converted Markdown artifact. | Contradicted by the assigned chunk and source-packet/image-check reading for the same page and entry reference. | 0.22 |
| 3 | The Pulgar/Arriagada and Burgos/de la Cruz readings are duplicate or variant readings of one person or family. | Only the shared entry number in derivative artifacts. | Names, parents, dates, places, and informants differ materially; this is not a normal spelling or name-variant conflict. | 0.03 |
| 4 | Entry 172 directly identifies a Dario-line person or proves a Dario identity bridge. | No direct support in the staged draft, chunk, source packet, converted file, or canonical context reviewed for this task. | The record names no Dario, Arturo, Smith, Dario Jose, or same-person bridge facts. | 0.04 |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: canonical page is family-supplied and explicitly cautions against automatic merges with similarly named source clusters. This entry does not name `Dario Arturo Pulgar-Smith`, `Smith`, Alexander John Heinz, a grandchild relationship, or any bridge event.
- `Dario Arturo Pulgar`: staged CV-related context elsewhere may support a document-level person by this name, but this entry does not name Dario Arturo Pulgar and cannot attach the birth-register cluster to that person.
- `Dario Jose Pulgar-Arriagada`: no direct support. The leading Pulgar hypothesis names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose.
- `Dario/Darío Pulgar Arriagada`: existing canonical context includes a separate `Darío Pulgar Arriagada` property/expropriation cluster dated 2000-12-05. The 1888 entry provides no same-person, parent-child, or chronology bridge to that cluster.
- Jose/Juana parent candidates: under the Pulgar hypothesis, possible parents are `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. Treat these as parent candidates only after conversion QA; do not merge them to broader Jose/Juana profiles from this conflict draft alone.

## Conflicts

- Same-person / duplicate-person: no duplicate-person conclusion is supported. The row conflict creates two competing families, not a same-person variant.
- Name-variant: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` remains a literal-reading issue, not a resolved variant.
- Relationship conflict: parent-child claims for `Jose del Carmen Segundo Pulgar Arriagada` with `Jose del Carmen Pulgar`/`Juana Arriagada de Pulgar` must remain held because the controlling row is not certified.
- Chronology conflict: the Pulgar hypothesis gives birth 8 March 1888 at 3 p.m.; the converted Markdown Burgos hypothesis gives birth 6 April 1888 at 10 p.m.
- Canonical-readiness conflict: canonical snapshots contain generated evidence from this chunk, but the current staged evidence requires `hold_for_conversion_qa`.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Moderate for the presence of a Pulgar/Arriagada row in the assigned chunk/source packet; insufficient for final identity or relationship promotion. |
| conflict_severity | 0.95 | The conflict changes the child, parents, birth date, birthplace, informant, and family cluster. |
| evidence_quality | 0.78 | Civil birth registration would be strong evidence once row-certified; this analysis is limited to staged/chunk/converted/wiki context. |
| conversion_confidence | 0.34 | The conversion artifacts disagree materially, and the father-field ending remains uncertified. |
| claim_probability | 0.72 | The Pulgar/Arriagada hypothesis leads because assigned chunk and source packet agree with staged image-check language. |
| relevance | 0.88 | Highly relevant to Pulgar/Arriagada reconstruction; only a research lead for Dario-line work. |
| canonical_readiness | 0.10 | Hold for targeted conversion QA and rerun proof review before any canonical action. |

## Recommended Next Action

Run targeted conversion QA for page 58, entry 172 against the source image, assigned chunk, source packet, and current converted Markdown. The QA result must certify the controlling row and decide the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting child identity, birth facts, parent-child relationships, parent merges, duplicate-person conclusions, or any Dario-line comparison.
