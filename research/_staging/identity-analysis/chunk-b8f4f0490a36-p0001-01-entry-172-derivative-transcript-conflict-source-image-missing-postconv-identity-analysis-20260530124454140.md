---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
worker: "postconv-identity-analysis-20260530124454140"
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

# Identity/Conflict Analysis: Entry 172 Derivative Transcript Conflict

This note analyzes the exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md`.

## Blockers First

- Physical row control is unresolved. In this workspace the expected source image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` and conversion-job page image `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` are not present.
- The assigned chunk and current converted Markdown describe materially different people under entry `172`. This is a row-control or derivative-transcript conflict, not a spelling variant.
- No same-person merge, duplicate-person merge, canonical page rename, Dario-line attachment, or promoted parent-child fact is ready from this staged draft.
- The father field `Jose del Carmen Pulgar S.` is only a derivative chunk reading here. The final `S.` or terminal mark needs image-controlled QA before canonical use.
- The staged draft does not literally name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`. Pulgar-line context justifies a later double-check only.
- Existing wiki pages already contain low-confidence/probable snapshots for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, but this task does not validate or strengthen those snapshots while row control remains uncertified.

## Literal Evidence

Assigned chunk and staged source-packet reading:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about three in the afternoon, `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age twenty-six, empleado, resident at `Calle de Valdivia`.

Current converted Markdown reading:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, about ten at night, `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`, age twenty-six, empleado, resident at `En esta`.

Interpretation: these are competing derivative readings of the entry target. They differ by child identity, parent set, birth chronology, birth place, and informant. The most likely issue is row/page-control or derivative-transcript substitution, but the cause cannot be certified without the missing image.

## Hypotheses

| Rank | Hypothesis | Supporting evidence | Conflicts and limits | Claim probability | Identity confidence | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada row. | The assigned chunk and staged source packet agree on the Pulgar/Arriagada child, parents, birth event, and informant. | The current converted Markdown assigns entry `172` to a Burgos/de la Cruz child; no image is available; father suffix remains unverified. | 0.64 | 0.58 | hold_for_conversion_qa |
| 2 | Entry `172` is the Burgos/de la Cruz row. | The current converted Markdown explicitly labels entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. | It conflicts with the assigned chunk and staged source packet; it has no Pulgar-line relevance if controlling. | 0.24 | 0.25 | hold_for_conversion_qa |
| 3 | The assigned chunk and converted Markdown describe different physical rows/images under one entry target. | Names, parent sets, dates, places, and informants all differ while the entry number is the same. | The image is missing, so the exact provenance of the mismatch is unproved. | 0.88 | 0.82 | hold_for_conversion_qa |
| 4 | The Pulgar/Arriagada father is the existing wiki `Jose del Carmen Pulgar`. | The assigned row gives the same base name as the wiki person. | Same-name evidence is insufficient; the wiki person has a separate draft child context, and the `S.` mark plus row control are unresolved. | 0.38 | 0.32 | not_ready |
| 5 | The Pulgar/Arriagada mother is the existing wiki `Juana Arriagada de Pulgar`. | The assigned row and wiki page share the exact name form, and the wiki page currently shows a probable child link to this child. | The link depends on row-control QA; do not merge with other Juana candidates by name alone. | 0.52 | 0.43 | not_ready |
| 6 | The Pulgar/Arriagada child is one of the Dario Pulgar candidates. | Only broad surname/family-line context exists through `Pulgar Arriagada`. | The named child is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario; no `Arturo`, `Smith`, `Dario Jose`, profession, age, spouse, descendant, or chronology bridge appears. | 0.03 | 0.02 | not_ready |

## Pulgar-Line Candidate Comparison

| Candidate | Evidence considered | Ranked assessment | Required next step |
| --- | --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | No literal mention in the staged draft, chunk, source packet, or converted entry. The canonical page is family-supplied and warns against automatic attachment of Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records. | Very low support; same-person probability 0.01. | Separate identity-bridge proof review using accepted identity-bearing records before any attachment to the Pulgar-Smith page. |
| `Dario Arturo Pulgar` | No literal mention in this entry. Local staged CV context treats this as a document-level Dario cluster needing its own bridge. | Very low support; same-person probability 0.02. | Proof-review the CV/source attribution separately, then compare only if accepted evidence gives parentage, birth, age, place, or family links. |
| `Dario Jose Pulgar-Arriagada` | No literal mention. The Pulgar/Arriagada reading contains `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose`. | Very low support; same-person probability 0.03. | Separate proof review of the Dario Jose cluster; do not infer identity from `Jose` or `Pulgar-Arriagada` alone. |
| `Dario Pulgar Arriagada` / `Dario Pulgar A.` | No literal mention. Existing staged/wiki context preserves separate Dario Pulgar Arriagada and Dario Pulgar A. contexts. | Very low support; same-person probability 0.02. | Separate identity-bridge review comparing full name, chronology, profession, location, provenance, and family ties. |
| `Jose del Carmen Pulgar` parent candidate | The assigned chunk/source packet names `Jose del Carmen Pulgar S.` as father; existing wiki has `Jose del Carmen Pulgar` with a separate draft child context. | Possible father only if the Pulgar/Arriagada row controls; probability 0.38. | Restore or locate source/page image, certify row control, then proof-review the father-field reading and any father-child relationship. |
| `Juana Arriagada de Pulgar` parent candidate | The assigned chunk/source packet names `Juana Arriagada de Pulgar` as mother; existing wiki has a probable child link to the assigned child. | Possible/probable mother only if the Pulgar/Arriagada row controls; probability 0.52. | Restore or locate source/page image, certify row control, then proof-review the mother-child relationship and any Juana reconciliation separately. |

## Conflict Classification

- Same-person evidence: not established for any Dario candidate; possible but unproved for the existing Jose/Juana stubs if the Pulgar/Arriagada row is certified.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar` are merged or strengthened before row-control QA.
- Name-variant evidence: limited to the unresolved `Jose del Carmen Pulgar S.` father-field mark; no Dario name variant is supported by this entry.
- Relationship conflict: high because the two derivative readings assign different parent sets to the same entry number.
- Chronology conflict: high because the two derivative readings give different birth dates, times, and places.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.58 for the Pulgar/Arriagada staged candidate; 0.02 for any Dario attachment | The assigned chunk and source packet agree internally, but the controlling image is missing and the current conversion conflicts. |
| Conflict severity | 0.93 | Same entry number, different child, parents, birth event, place, and informant. |
| Evidence quality | 0.56 | The source type would be strong, but this task has only conflicting derivative text layers. |
| Conversion confidence | 0.38 | Assigned chunk and converted Markdown materially disagree, and image-controlled reread is unavailable. |
| Claim probability: Pulgar/Arriagada row controls entry 172 | 0.64 | Supported by assigned chunk and staged packet, not certifiable. |
| Claim probability: Burgos/de la Cruz row controls entry 172 | 0.24 | Supported by current converted Markdown only, contradicted by assigned chunk and packet. |
| Relevance | 0.85 if Pulgar/Arriagada is certified; 0.10 if Burgos/de la Cruz is certified | The Pulgar-line relevance depends on row control. |
| Canonical readiness | 0.08 | Not ready for promotion, relationship attachment, merge, rename, or wiki update. |

## Recommended Next Action

Keep all dependent evidence on `hold_for_conversion_qa`.

Exact next proof-review step: a conversion-QA worker must restore or locate the original source image or a certified page image, then compare physical entry `172` against the assigned chunk and current converted Markdown. That review must decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and must bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, run proof review only on the certified literal readings: child name, sex, registration date, birth date/time/place, father-name reading, mother-name reading, informant reading, and parent-child relationships. A separate identity-bridge proof review is required before comparing any accepted Jose/Juana/child cluster to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`.
