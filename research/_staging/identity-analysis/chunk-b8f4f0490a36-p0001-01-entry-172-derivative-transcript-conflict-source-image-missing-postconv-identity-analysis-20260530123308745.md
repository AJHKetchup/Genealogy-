---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
worker: "postconv-identity-analysis-20260530123308745"
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

- Row-control blocker: the assigned chunk and current converted Markdown give different people for entry `172`, including different child names, parents, birth dates, birth places, and informants.
- Source-image blocker: the conversion review says the expected original source image and conversion-job page image were unavailable to that worker, so the physical row was not certified.
- Conversion blocker: this is a derivative transcript conflict, not a spelling variant or normalizing issue.
- Relationship blocker: no parent-child claim from this staged draft is promotion-ready until image-controlled row QA decides whether entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row.
- Father-field blocker: the assigned chunk reads `Jose del Carmen Pulgar S.`, while the source packet explicitly holds the suffix/terminal mark pending image QA.
- Pulgar-line blocker: this staged draft does not literally name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`.
- Jose/Juana blocker: existing wiki context has separate Jose/Juana candidates, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`; this draft cannot merge or reconcile them by name or family context alone.

## Literal Source Readings

Assigned chunk and staged source-packet reading:

- Entry `172`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`.
- Birth `Ocho de Marzo de mil ochocientos ochenta i ocho`, about 3 p.m., at `Calle de Valdivia`.
- Father `Jose del Carmen Pulgar S.`; suffix remains unresolved for promotion.
- Mother `Juana Arriagada de Pulgar`.
- Informant `Ernesto Herrera L.`, present at birth, age twenty-six, empleado, resident at `Calle de Valdivia`.

Current converted Markdown reading:

- Entry `172`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child `Jose Miguel`, sex `Varon`.
- Birth `El seis de Abril de mil ochocientos ochenta i ocho`, about 10 p.m., at `En esta`.
- Father `Oswaldo Burgos`.
- Mother `Concepcion de la Cruz`.
- Informant `Oswaldo Burgos`, age twenty-six, empleado, resident at `En esta`.

Interpretation: the derivative layers are not two readings of the same family. They represent a material row/page-control conflict.

## Hypotheses And Evidence

| Rank | Hypothesis | Evidence supporting | Conflicts and limits | Claim probability | Identity confidence | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada row. | Assigned chunk and staged source packet consistently read `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.` | Current converted Markdown assigns entry `172` to `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; image QA is missing; father suffix is unresolved. | 0.66 | 0.60 | hold_for_conversion_qa |
| 2 | Entry `172` is the Burgos/de la Cruz row. | Current converted Markdown explicitly labels entry `172` as `Jose Miguel`, with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`. | Directly conflicts with the assigned chunk and staged packet; no Pulgar-line relevance if this row controls. | 0.22 | 0.24 | hold_for_conversion_qa |
| 3 | The evidence reflects a derivative row/page mismatch. | Child, parents, date, place, and informant all differ between derivative layers. | Cause cannot be resolved without the original/full-page image or certified page image. | 0.88 | 0.80 | hold_for_conversion_qa |
| 4 | Assigned-row father is the existing `Jose del Carmen Pulgar` candidate. | The assigned row has the same base father name, and an existing wiki stub exists for `Jose del Carmen Pulgar`. | Same-name evidence is insufficient; row control and `S.` suffix remain unresolved; existing Jose evidence includes other child contexts. | 0.40 | 0.33 | not_ready |
| 5 | Assigned-row mother is the existing `Juana Arriagada de Pulgar` candidate. | Assigned row and existing wiki page share the exact name form; wiki snapshot has a probable/low-confidence child link to the assigned child. | Relationship depends on row-control QA; do not merge with other Juana variants or parent candidates. | 0.54 | 0.44 | not_ready |
| 6 | Assigned-row child is a Dario Pulgar identity candidate. | Only broad surname context: `Pulgar Arriagada`. | Child is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario; no `Arturo`, `Smith`, `Dario Jose`, age, occupation, spouse, descendant, or chronology bridge appears. | 0.03 | 0.02 | not_ready |

## Pulgar-Line Comparison

| Candidate | Evidence from this draft and existing wiki context | Ranked assessment | Exact next proof-review or promotion step needed |
| --- | --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | No literal mention in the draft. Canonical page is family-supplied and warns against attaching Dario/Pulgar records without identity review. | Very low same-person support; probability 0.01. | Separate identity-bridge proof review using accepted identity-bearing records before attaching this entry-172 evidence to the Pulgar-Smith page. |
| `Dario Arturo Pulgar` | No literal mention in the draft. Local CV staging preserves `Dario Arturo Pulgar` as a separate document-level cluster. | Very low same-person support; probability 0.02. | Proof-review an identity-bearing CV/source bridge separately, then compare only if accepted records supply parentage, birth, age, place, or family links. |
| `Dario Jose Pulgar-Arriagada` | No literal mention. The assigned reading contains `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose`. | Very low same-person support; probability 0.03. | Separate proof review of the Dario Jose cluster; do not infer identity from shared surname or the `Jose` element. |
| `Dario Pulgar Arriagada` / `Dario Pulgar A.` | No literal mention. Existing wiki/staged context preserves separate Dario Pulgar Arriagada and Dario Pulgar A. contexts. | Very low same-person support; probability 0.02. | Separate bridge review comparing full name, chronology, place, profession, source provenance, and family ties. |
| `Jose del Carmen Pulgar` parent candidate | Assigned chunk/source packet name a father with this base name, possibly with suffix `S.`; existing wiki page has a separate child context. | Possible father only if Pulgar/Arriagada controls entry `172`; probability 0.40. | Full-image row-control QA plus father-field review before parent claim, merge, or canonical strengthening. |
| `Juana Arriagada de Pulgar` parent candidate | Assigned chunk/source packet name this mother; existing wiki page has a probable child link to the assigned child. | Possible/probable mother only if Pulgar/Arriagada controls entry `172`; probability 0.54. | Full-image row-control QA, then proof review the mother-child relationship and any Juana/Jose reconciliation separately. |

## Conflict Classification

- Same-person evidence: not established for any Dario candidate; possible but unproved for existing Jose/Juana stubs if the Pulgar row controls.
- Duplicate-person risk: high if the assigned child or parents are merged or attached to canonical pages before row-control and father-field QA.
- Name-variant evidence: limited to possible `S.` after `Jose del Carmen Pulgar`; no Dario name variant is proved.
- Relationship conflict: high because the competing readings assign different parents to the same entry number.
- Chronology conflict: high because the competing readings give different birth dates, times, and places.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.60 for the Pulgar/Arriagada row as a staged candidate; 0.02 for any Dario attachment | Assigned chunk and packet are internally consistent, but the image is missing and the current conversion conflicts. |
| Conflict severity | 0.92 | Same entry number, different child, parents, birth event, place, and informant. |
| Evidence quality | 0.58 | A civil birth register would be strong evidence, but only conflicting derivative layers are available here. |
| Conversion confidence | 0.40 | Assigned chunk and converted Markdown materially disagree, and no image-controlled reread is available in this staged packet. |
| Claim probability: Pulgar/Arriagada row controls entry 172 | 0.66 | Supported by assigned chunk and staged packet, not certifiable without image QA. |
| Claim probability: Burgos/de la Cruz row controls entry 172 | 0.22 | Supported by current converted Markdown only, contradicted by assigned chunk and packet. |
| Relevance | 0.86 | High for Pulgar-line work only if the Pulgar/Arriagada row is later certified; otherwise low. |
| Canonical readiness | 0.08 | Not ready for promotion, relationship attachment, merge, rename, or canonical wiki update. |

## Recommended Next Action

Keep this staged draft on `hold_for_conversion_qa`. Do not promote birth facts, parent-child relationships, identity merges, canonical name changes, Dario-line attachments, or Jose/Juana reconciliation from this evidence.

Exact next step: a conversion-QA worker must restore or locate the full source image or certified page image, compare physical entry `172` against the assigned chunk and current converted Markdown, and certify whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz. The same QA pass must bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, run proof review only on the certified literal claims: child name, sex, birth date/time/place, father-name reading, mother-name reading, informant reading, and parent-child relationships. A separate identity-bridge proof review is required before comparing any accepted Jose/Juana/child cluster to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`.
