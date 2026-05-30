---
type: identity_conflict_analysis
role: identity_researcher
worker: postconv-identity-analysis-20260530223135997
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
analysis_status: hold_for_conversion_qa
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01

## Blockers First

- Page-control blocker: the assigned chunk and aggregate converted file contain a 1979-1982 / 1974-1978 / 1972-1973 / 1970-1972 work-history sequence, while the conversion job page Markdown for page 5 contains 1999 / 1998-1999 / 1997-1998 entries. Both cannot be the controlling page-5 transcription.
- Image blocker: the job manifest records `page-images/page-0005.jpg`, but that file is not present in this checkout, so this worker cannot visually proof-review page 5.
- Manifest/hash blocker: the chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice with different character counts and hashes; the source packet also records a converted-file hash mismatch between chunk metadata and observed converted content.
- Identity blocker: the assigned page body does not repeat the subject's full name. `Dario Arturo Pulgar` is a document-title/source-context label, not a page-local name statement.
- Relationship blocker: the assigned evidence names no parents, spouse, children, siblings, household members, or descendants. Jose/Juana parent candidates must remain outside this page-5 claim set.

## Literal Evidence

Assigned chunk / aggregate converted file literal reading:

- `1979 - 1982` United Nations Centre for Human Settlements (HABITAT), Nairobi, Kenya, Development Support Communications Officer.
- `1974 - 1978` National Film Board of Canada (NFB), Montreal, Canada, Audio Visual Consultant.
- `1972 - 1973` Chile Films, Santiago, Chile, General Manager Distribution and Exhibition, Head of International Department.
- `1970 - 1972` Cine, Television y Comunicaciones (CITELCO), Santiago, Chile, Producer.
- The page ends with `EDUCATION`.

Conflicting conversion job page-Markdown literal reading:

- `1999` National Trust Fund for Protected Areas in Peru (PROFONANPE), Peru, Consultant.
- `1999` Television Trust for the Environment (TVE), London, England, Consultant.
- `1998 - 1999` Arca Consulting / European Commission, Lesotho, Team Leader.
- `1997-1998` Klohn Crippen Consultants, Huaraz, Peru, Socio-economic Consultant.
- `1997-1998` SNC Lavalin Agriculture, Maracaibo, Venezuela, Training Consultant.

Interpretation: these are both plausible CV work-history pages for the same document, but their date ranges and entries conflict as controlling page-5 text. The conflict is derivative transcription/page-control, not a genealogical relationship conflict.

## Hypotheses And Ranked Identity Assessment

| Rank | Hypothesis | Evidence supporting | Evidence limiting or conflicting | Claim probability | Identity confidence | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | The staged draft should remain a held page-control conflict for the document-level CV subject `Dario Arturo Pulgar`. | Source title and source packet identify `CV of Dario Arturo Pulgar`; both competing texts are CV work-history material; no alternate named subject appears on page 5. | Page body does not repeat the full name; page-control and image/hash blockers remain unresolved. | 0.82 | 0.68 | not_ready |
| 2 | If conversion QA certifies the assigned chunk, page 5 can support work-history claims for document-level `Dario Arturo Pulgar`. | The chunk and aggregate converted file agree on the HABITAT/NFB/Chile Films/CITELCO sequence; chronology fits a CV career sequence leading into education. | Missing page image and duplicate chunk manifest prevent proof-level acceptance now. | 0.58 | 0.50 | hold_for_conversion_qa |
| 3 | If conversion QA certifies the page-Markdown text, page 5 can support the 1999/1998 consultant sequence for document-level `Dario Arturo Pulgar`. | The conversion job page Markdown contains structured CV entries that fit adjacent pages 4 and 6 chronologically. | It conflicts directly with the assigned chunk and aggregate converted file; no page image is available here to decide control. | 0.42 | 0.38 | hold_for_conversion_qa |
| 4 | `Dario Arturo Pulgar` in the CV is the same person as canonical `Dario Arturo Pulgar-Smith`. | Existing canonical wiki context has a family-supplied `Dario Arturo Pulgar-Smith`; the name overlaps with the CV title's `Dario Arturo Pulgar`. | The page does not state `Smith`, family relationship, age, birth, spouse, child, grandchild, or other bridge to Alexander John Heinz. Same-name overlap is insufficient. | 0.35 | 0.25 | not_ready |
| 5 | This page bridges to `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | Existing staged/wiki context has separate Pulgar-Arriagada candidates and a canonical `Darío Pulgar Arriagada` page with a 2000 expropriation event. | Page 5 does not contain `Jose`, `J.`, `Arriagada`, medical/military context, parentage, Chiguayante, Geneva, or a chronology bridge to those clusters. | 0.08 | 0.05 | not_ready |
| 6 | Jose/Juana parent candidates explain or bridge this page-5 subject. | Existing wiki/staged context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` variants in separate Pulgar-line work. | This page gives no Jose or Juana names and no parent-child terms. Family context can justify later comparison only, not promotion or silent correction. | 0.03 | 0.02 | not_ready |

## Conflict Classification And Scores

| Category | Score | Assessment |
| --- | ---: | --- |
| identity confidence | 0.68 | Moderate for document-level `Dario Arturo Pulgar`; low for any canonical merge. |
| conflict severity | 0.86 | High page-control conflict because competing derivatives support materially different work-history claims. |
| evidence quality | 0.46 | Literal derivative text is readable, but source-image proof and stable metadata are missing. |
| conversion confidence | 0.20 | Blocked by missing page image, duplicate manifest entries, and hash mismatch. |
| claim probability | 0.58 | Assigned chunk may be correct, but cannot be preferred over page Markdown without QA. |
| relevance | 0.88 | High relevance to Pulgar-line CV work-history and possible later identity bridge. |
| canonical readiness | 0.10 | Not ready for canonical promotion or merge. |

## Pulgar-Line Comparison Boundary

- `Dario Arturo Pulgar`: best current label for this staged CV evidence, but only at document level until page control is restored.
- `Dario Arturo Pulgar-Smith`: plausible future comparison because of overlapping `Dario Arturo Pulgar` name elements and existing family-supplied canonical context; not proved by this page.
- `Dario Jose Pulgar-Arriagada`: not supported by this page; no `Jose`, `J.`, or `Arriagada` appears.
- `Dario/Dario Pulgar Arriagada` / `Darío Pulgar Arriagada`: not supported by this page; existing canonical/staged Pulgar-Arriagada records remain separate.
- Jose/Juana parent candidates: no page-local evidence. Do not attach or reconcile `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar` from this CV page.

## Recommended Next Action

Keep this staged draft and any dependent page-5 work-history claims on `hold_for_conversion_qa`.

Exact next proof-review/promotion step: a conversion-QA worker should restore or regenerate `page-images/page-0005.jpg`, repair the duplicate `CHUNK-fb0a0000636f-P0005-01` manifest state, reconcile the converted-file hash mismatch, and certify whether page 5 is controlled by the 1979-1970 assigned-chunk sequence or the 1999/1998 page-Markdown sequence. After that, run visual proof review of the certified page text. Only then should a separate identity-bridge review compare the accepted CV subject evidence against `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, and Jose/Juana parent candidates.

No same-person merge, duplicate-person merge, name-variant promotion, relationship promotion, chronology promotion, or canonical wiki update is recommended from this staged draft.
