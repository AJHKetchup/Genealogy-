---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
worker: "postconv-identity-analysis-20260530124851565"
role: identity_researcher
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Entry 172 Source-Image-Missing Conflict

This note analyzes the exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md`.

## Blockers First

- Physical row control is not certified. The conversion review says the expected source image and conversion-job page image were not available, so no worker has image-controlled verification for entry `172` in this task.
- The assigned chunk/source packet and current converted Markdown disagree on child, parents, birth date/time/place, and informant. This is a material derivative-transcript conflict, not a harmless spelling variant.
- No canonical person merge, duplicate-person resolution, name normalization, parent-child promotion, Dario-line attachment, or wiki page update is supported by this staged draft.
- The father reading `Jose del Carmen Pulgar S.` is derivative only. The final `S.` or terminal mark must remain bounded until image QA certifies the visible reading.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` contain only low-confidence/probable staged relationships relevant here; they do not resolve this conflict while row control is open.

## Literal Evidence

Assigned chunk and staged source packet:

| Field | Literal reading |
| --- | --- |
| Entry | `172` |
| Registration date | `Siete de Abril de mil ochocientos ochenta i ocho` |
| Child | `Jose del Carmen Segundo Pulgar Arriagada` |
| Sex | `Hombre` |
| Birth | `Ocho de Marzo de mil ochocientos ochenta i ocho`, about three in the afternoon, `Calle de Valdivia` |
| Father | `Jose del Carmen Pulgar S.` |
| Mother | `Juana Arriagada de Pulgar` |
| Informant | `Ernesto Herrera L.`, present at birth, age twenty-six, empleado, resident at `Calle de Valdivia` |

Current converted Markdown:

| Field | Literal reading |
| --- | --- |
| Entry | `172` |
| Registration date | `Siete de Abril de mil ochocientos ochenta i ocho` |
| Child | `Jose Miguel` |
| Sex | `Varon` |
| Birth | `El seis de Abril de mil ochocientos ochenta i ocho`, about ten at night, `En esta` |
| Father | `Oswaldo Burgos` |
| Mother | `Concepcion de la Cruz` |
| Informant | `Oswaldo Burgos`, age twenty-six, empleado, resident at `En esta` |

Interpretation: these are competing derivative readings attached to the same entry target. They are not alternate readings of one child's name because the parent set, chronology, place, and declarant also change.

## Hypotheses

| Rank | Hypothesis | Evidence supporting | Conflicts and limits | Claim probability | Identity confidence | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada row. | The assigned chunk and staged source packet agree internally on the Pulgar/Arriagada child, parents, birth event, and informant. | The current converted Markdown assigns entry `172` to a different Burgos/de la Cruz child; the source image is missing; father suffix is uncertified. | 0.64 | 0.58 | hold_for_conversion_qa |
| 2 | Entry `172` is the Burgos/de la Cruz row. | The current converted Markdown explicitly labels entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. | It conflicts with the assigned chunk and source packet and has no Pulgar-line relevance if controlling. | 0.24 | 0.25 | hold_for_conversion_qa |
| 3 | The two derivative layers describe different physical rows or images under one entry target. | Nearly every identity-bearing field differs while the entry number is the same. | The missing image prevents identifying the exact provenance error. | 0.88 | 0.82 | hold_for_conversion_qa |
| 4 | The father candidate is existing wiki `Jose del Carmen Pulgar`. | The assigned chunk names father as `Jose del Carmen Pulgar S.`, sharing the base name with the wiki stub. | Same-name evidence is insufficient; the wiki page has separate draft child context and no certified connection to this row. | 0.38 | 0.32 | not_ready |
| 5 | The mother candidate is existing wiki `Juana Arriagada de Pulgar`. | The assigned chunk names mother as `Juana Arriagada de Pulgar`, matching the wiki stub's preferred name. | The existing child link is probable/low-confidence and depends on this unresolved row. | 0.52 | 0.43 | not_ready |
| 6 | `Jose del Carmen Segundo Pulgar Arriagada` is a Dario Pulgar candidate. | Only broad Pulgar/Arriagada surname context exists. | The staged draft does not name Dario, Arturo, Smith, Dario Jose, a later profession, spouse, child, or identity bridge. | 0.03 | 0.02 | not_ready |

## Pulgar-Line Candidate Comparison

| Candidate | Evidence considered | Ranked assessment | Exact next proof-review or promotion step |
| --- | --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns not to attach similarly named records without identity review. This staged entry does not literally name him. | Very low support; same-person probability 0.01. | Separate identity-bridge proof review using accepted identity-bearing records before any attachment to the Pulgar-Smith page. |
| `Dario Arturo Pulgar` | Local staged CV context exists elsewhere, but this staged draft and entry do not name `Dario Arturo Pulgar`. | Very low support; same-person probability 0.02. | Proof-review the CV/source attribution separately, then compare only if accepted evidence supplies parentage, birth, age, place, or family links. |
| `Dario Jose Pulgar-Arriagada` | No literal mention. The assigned row gives `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose`. | Very low support; same-person probability 0.03. | Separate proof review of the Dario Jose cluster; do not infer identity from `Jose` plus `Pulgar-Arriagada`. |
| `Dario Pulgar Arriagada` / `Dario Pulgar A.` | Existing wiki context has a separate `Darío Pulgar Arriagada` stub with a 2000 legal-notice event. This 1888 birth conflict does not name Dario. | Very low support; same-person probability 0.02. | Separate identity-bridge review comparing full name, chronology, place, occupation, provenance, and family ties. |
| `Jose del Carmen Pulgar` parent candidate | Assigned chunk/source packet name `Jose del Carmen Pulgar S.` as father. Existing wiki has `Jose del Carmen Pulgar` with separate draft child evidence. | Possible father only if the Pulgar/Arriagada row controls; probability 0.38. | Restore or locate the source/page image, certify row control, then proof-review the father-field reading and father-child relationship. |
| `Juana Arriagada de Pulgar` parent candidate | Assigned chunk/source packet name `Juana Arriagada de Pulgar` as mother. Existing wiki has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`. | Possible/probable mother only if the Pulgar/Arriagada row controls; probability 0.52. | Restore or locate the source/page image, certify row control, then proof-review the mother-child relationship and any Juana reconciliation separately. |

## Conflict Classification

- Same-person evidence: not established for any Dario candidate. Possible but unproved for existing Jose/Juana stubs if the Pulgar/Arriagada row is certified.
- Duplicate-person risk: high if the child, father, or mother pages are merged or strengthened before row-control QA.
- Name-variant evidence: limited to the unresolved father-field mark in `Jose del Carmen Pulgar S.`; no Dario name variant is supported by this entry.
- Relationship conflict: high because the same entry number is tied to two different parent sets.
- Chronology conflict: high because the readings give different birth dates, times, and places.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.58 for the Pulgar/Arriagada staged candidate; 0.02 for Dario attachment | Internal agreement exists between assigned chunk and source packet, but the controlling image is missing and the current conversion conflicts. |
| Conflict severity | 0.93 | Same entry number, different child, parents, birth event, place, and informant. |
| Evidence quality | 0.56 | A civil birth register would be strong evidence, but this task has conflicting derivative text only. |
| Conversion confidence | 0.38 | Assigned chunk and converted Markdown materially disagree, and image-controlled reread is unavailable. |
| Claim probability: Pulgar/Arriagada row controls entry 172 | 0.64 | Supported by assigned chunk and staged packet, not certifiable. |
| Claim probability: Burgos/de la Cruz row controls entry 172 | 0.24 | Supported by current converted Markdown only, contradicted by assigned chunk and packet. |
| Relevance | 0.85 if Pulgar/Arriagada is certified; 0.10 if Burgos/de la Cruz is certified | Pulgar-line relevance depends entirely on row control. |
| Canonical readiness | 0.08 | Not ready for promotion, relationship attachment, merge, rename, or wiki update. |

## Recommended Next Action

Keep the staged draft on `hold_for_conversion_qa`.

Exact next step: a conversion-QA worker must restore or locate the original source image or a certified page image and compare physical entry `172` against the assigned chunk, source packet, and current converted Markdown. That review must decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz, and must bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, run proof review only on the certified literal readings: child name, sex, registration date, birth date/time/place, father-name reading, mother-name reading, informant reading, and parent-child relationships. A separate identity-bridge proof review is required before any comparison or attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`.
