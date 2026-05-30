---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
worker: "postconv-identity-analysis-20260530122346003"
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

# Identity/Conflict Analysis: Entry 172 Source Image Missing

This note analyzes the exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md`.

## Blockers First

- Row-control blocker: the assigned chunk and the current converted Markdown assign entry `172` to different children, parents, birth dates, birth places, and informants.
- Source-image blocker: `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` and the expected conversion-job `page-0001.png` were not present in this checkout, so I could not certify the physical row.
- Conversion blocker: this is a derivative transcript conflict, not a harmless name variant or translation difference.
- Relationship blocker: no parent-child claim from this draft is canonical-ready until image-controlled row QA decides whether entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row.
- Father-field blocker: the chunk reads `Jose del Carmen Pulgar S.`, but the source packet says the suffix/terminal mark must remain unpromoted until image QA certifies it.
- Pulgar-line blocker: this staged draft does not literally name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`.
- Jose/Juana blocker: existing wiki context includes `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and other Jose/Juana contexts from separate records. This draft cannot merge or reconcile them by family context alone.

## Literal Source Readings

Assigned chunk/source-packet reading:

- Entry number: `172`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about three in the afternoon, at `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk, with the suffix held as unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age twenty-six, empleado, resident at `Calle de Valdivia`.

Current converted Markdown reading:

- Entry number: `172`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, at ten at night, at `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`, age twenty-six, empleado, resident at `En esta`.

Interpretation: the competing derivative readings describe materially different rows or materially different source-page states. The conflict controls identity, relationship, and chronology.

## Hypotheses And Evidence

| Rank | Hypothesis | Evidence supporting | Conflicts and limits | Claim probability | Identity confidence | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada row. | The assigned chunk and staged source packet consistently read `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`. Existing wiki stubs already carry low-confidence/probable evidence from this cluster. | The current converted Markdown assigns entry `172` to `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; source image is absent; father suffix is unresolved. | 0.66 | 0.60 | hold_for_conversion_qa |
| 2 | Entry `172` is the Burgos/de la Cruz row. | The current converted Markdown explicitly labels entry `172` as `Jose Miguel`, with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`. | Directly conflicts with the assigned chunk and staged packet; no Pulgar-line relevance if this row controls. | 0.22 | 0.24 | hold_for_conversion_qa |
| 3 | The evidence is a derivative row/page mismatch. | Child, parents, birth event, place, and informant all differ between the derivative layers. | The cause cannot be resolved without the original/full-page image or certified page image. | 0.88 | 0.80 | hold_for_conversion_qa |
| 4 | Assigned-row father is the existing `Jose del Carmen Pulgar` candidate. | Same base name appears in the assigned row, and an existing canonical stub for `Jose del Carmen Pulgar` exists. | Same-name evidence is not enough; row control and `S.` suffix remain unresolved; separate Jose candidates must stay separate. | 0.40 | 0.33 | not_ready |
| 5 | Assigned-row mother is the existing `Juana Arriagada de Pulgar` candidate. | The assigned row and existing canonical stub share the exact name form; the wiki snapshot has a low-confidence child link to the assigned child. | Relationship depends entirely on row-control QA; do not merge with other Juana variants or parent candidates from separate records. | 0.54 | 0.44 | not_ready |
| 6 | Assigned-row child is a Dario Pulgar identity candidate. | Only broad surname context: `Pulgar Arriagada`. | The assigned child is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario; no `Arturo`, `Smith`, `Dario Jose`, age, occupation, spouse, descendant, or chronology bridge appears. | 0.03 | 0.02 | not_ready |

## Pulgar-Line Comparison

| Candidate | Evidence from this draft and existing wiki context | Ranked assessment | Exact next proof-review or promotion step needed |
| --- | --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | No literal mention of Dario, Arturo, Smith, Alexander John Heinz, or a maternal-grandfather relationship. Canonical page is family-supplied and warns against automatic attachment of Pulgar records. | Very low same-person support; probability 0.01. | Separate identity-bridge proof review using accepted identity-bearing records before attaching this or any Pulgar/Arriagada evidence to the Pulgar-Smith page. |
| `Dario Arturo Pulgar` | No literal mention. Other local CV contexts may identify a document-level `Dario Arturo Pulgar`, but this birth-entry conflict does not bridge to him. | Very low same-person support; probability 0.02. | Proof-review the CV subject bridge separately, then compare only if accepted records supply parentage, birth, age, place, or family links. |
| `Dario Jose Pulgar-Arriagada` | No literal mention. The assigned reading contains `Jose del Carmen Segundo Pulgar Arriagada`, which is not a `Dario Jose` reading. | Very low same-person support; probability 0.03. | Separate proof review of the Dario Jose source cluster; do not infer identity from shared surname or the `Jose` element. |
| `Dario Pulgar Arriagada` / `Dario Pulgar A.` | No literal mention. Existing wiki context includes a separate `Dario Pulgar Arriagada` stub and staged `Dario Pulgar A.` contexts, but this draft supplies no bridge. | Very low same-person support; probability 0.02. | Separate identity-bridge proof review comparing accepted Dario Pulgar Arriagada, Dario J./Jose Pulgar Arriagada, and Dario Pulgar A. evidence by full name, chronology, place, profession, and family ties. |
| `Jose del Carmen Pulgar` parent candidate | Assigned chunk/source packet name a father with this base name, possibly with suffix `S.`. Existing canonical stub has separate draft evidence for another child. | Possible father only if the Pulgar row controls entry `172`; probability 0.40. | Full-image row-control QA plus father-field review before any parent claim, merge, or canonical strengthening. |
| `Juana Arriagada de Pulgar` parent candidate | Assigned chunk/source packet name this mother, and the existing wiki page has a low-confidence probable child link. | Possible/probable mother only if the Pulgar row controls entry `172`; probability 0.54. | Full-image row-control QA before promotion; then proof review the mother-child relationship and any Juana/Jose reconciliation separately. |

## Conflict Classification

- Same-person evidence: not established for any Dario candidate; possible but unproved for the existing Jose/Juana stubs if the Pulgar row controls.
- Duplicate-person risk: high if the assigned child or parents are merged or attached to canonical pages before row-control and father-field QA.
- Name-variant evidence: limited to the possible `S.` suffix after `Jose del Carmen Pulgar`; no Dario name variant is proved.
- Relationship conflict: high because the competing readings assign different parents to the same entry number.
- Chronology conflict: high because the competing readings give different birth dates, times, and places.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.60 for the Pulgar/Arriagada row as a staged candidate; 0.02 for any Dario attachment | The assigned chunk and packet are internally consistent, but the image is missing and the current conversion conflicts. |
| Conflict severity | 0.92 | Same entry number, different child, parents, birth event, place, and informant. |
| Evidence quality | 0.58 | A civil birth register would be strong evidence, but only conflicting derivative layers are available here. |
| Conversion confidence | 0.40 | The assigned chunk and current converted Markdown materially disagree, and no image-controlled reread is possible. |
| Claim probability: Pulgar/Arriagada row controls entry 172 | 0.66 | Supported by assigned chunk and staged packet, not certifiable without image QA. |
| Claim probability: Burgos/de la Cruz row controls entry 172 | 0.22 | Supported by current converted Markdown only, contradicted by assigned chunk and packet. |
| Relevance | 0.86 | High for Pulgar-line work only if the Pulgar/Arriagada row is later certified; otherwise low. |
| Canonical readiness | 0.08 | Not ready for promotion, relationship attachment, merge, rename, or canonical wiki update. |

## Recommended Next Action

Keep this staged draft on `hold_for_conversion_qa`. Do not promote birth facts, parent-child relationships, identity merges, canonical name changes, Dario-line attachments, or Jose/Juana reconciliation from this evidence.

Exact next step: a conversion-QA worker must restore or locate the full source image or certified page image, compare the physical entry `172` row against the assigned chunk and current converted Markdown, and certify whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz. The same QA pass must bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, run proof review only on the certified literal claims: child name, sex, birth date/time/place, father-name reading, mother-name reading, informant reading, and parent-child relationships. A separate identity-bridge proof review is required before comparing any accepted Jose/Juana/child cluster to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`.
