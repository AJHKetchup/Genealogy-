---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md"
worker: "postconv-identity-analysis-20260530110953508"
role: identity_researcher
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Entry 172 Row Control

This note analyzes the exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md`.

## Blockers First

- Row-control blocker: the assigned chunk and the current converted Markdown assign entry `172` to different identity clusters.
- Full-image blocker: the source packet reports that the full original PNG for SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2` was absent in this checkout. Local verification also found the source path absent and no page-image directory in the conversion job.
- Relationship blocker: the two readings name different children, parents, birth dates, birth places, and informants. No parent-child claim from this draft is promotion-ready.
- Father-field blocker: the assigned chunk reads `Jose del Carmen Pulgar S.`, but the source packet directs holding the father as `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar [?]` until the suffix is certified.
- Pulgar-line blocker: this entry does not literally name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`. Those comparisons remain anti-conflation checks only.
- Jose/Juana blocker: existing wiki and staged context include separate Jose/Juana candidates, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`. This row conflict cannot merge or reconcile them.

## Literal Source Readings

Assigned chunk and source-packet reading:

- Entry `172`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about three in the afternoon, at `Calle de Valdivia`.
- Father: chunk transcription `Jose del Carmen Pulgar S.`; bounded packet reading pending QA is `Jose del Carmen Pulgar` or uncertain suffix.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, resident at `Calle de Valdivia`.

Current converted Markdown reading:

- Entry `172`; child `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, at ten at night, at `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`, age twenty-six, employed, resident at `En esta`.

Interpretation: these are not spelling variants or duplicate-name variants. They are mutually incompatible row-control readings for the same entry number.

## Hypotheses And Evidence

| Rank | Hypothesis | Evidence supporting | Conflicts and limits | Claim probability | Identity confidence | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry `172` is controlled by the Pulgar/Arriagada row. | Assigned chunk and revised source packet consistently name `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`. Existing wiki stubs preserve this cluster as low-confidence/probable evidence. | Current converted Markdown gives a different entry-172 row; full image is absent; father suffix is unresolved. | 0.68 | 0.62 | hold_for_conversion_qa |
| 2 | Entry `172` is controlled by the Burgos/de la Cruz row. | Current converted Markdown explicitly labels entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. | Assigned chunk and source packet directly conflict; no Pulgar-family relevance follows from this reading. | 0.20 | 0.22 | hold_for_conversion_qa |
| 3 | The conflict is a derivative row/page mismatch rather than an identity variant. | Every identity-controlling field differs: child name, parents, birth date/time, place, and informant. | Exact cause cannot be resolved without original full-page row-control QA. | 0.84 | 0.78 | hold_for_conversion_qa |
| 4 | The father in the assigned row is the existing `Jose del Carmen Pulgar` candidate. | Same name and local Pulgar/Juana staged context; canonical stub exists. | Same-name evidence is insufficient; the suffix may matter; row-control remains unresolved; do not merge with other Jose candidates. | 0.42 | 0.34 | not_ready |
| 5 | The mother in the assigned row is the existing `Juana Arriagada de Pulgar` candidate. | Exact name match to existing canonical stub; existing evidence snapshot has a low-confidence/probable child link to `Jose del Carmen Segundo Pulgar Arriagada`. | Relationship depends on row-control certification; do not merge with `Juana de Dios Amagada de Pulgar` or related entry-513 variants by family context alone. | 0.55 | 0.45 | not_ready |
| 6 | The assigned entry-172 child is a Dario Pulgar identity candidate. | Only broad `Pulgar Arriagada` surname context. | The child is named `Jose del Carmen Segundo Pulgar Arriagada`, not Dario; no Arturo, Smith, Dario Jose, medical/professional, spouse, descendant, or chronology bridge appears here. | 0.03 | 0.02 | not_ready |

## Pulgar-Line Comparison

| Candidate | Evidence from this draft | Ranked assessment | Exact next proof-review step needed |
| --- | --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | No literal mention of Dario, Arturo, Smith, Alexander John Heinz, maternal-grandfather status, or family-supplied relationship. Existing canonical page warns against automatic merges. | Very low same-person support from this draft; probability 0.01. | Separate identity-bridge review comparing accepted identity-bearing records to the family-supplied Pulgar-Smith page. Entry 172 cannot do that work. |
| `Dario Arturo Pulgar` | No literal mention. Other staged CV material may identify a document-level Dario Arturo Pulgar, but this birth-entry conflict gives no bridge. | Very low same-person support; probability 0.02. | Proof-reviewed CV identity bridge first; then compare to certified Pulgar/Juana parent cluster only if later evidence gives a parent, birth, age, or family link. |
| `Dario Jose Pulgar-Arriagada` | No literal mention of Dario Jose. Surname overlap only. | Very low same-person support; probability 0.03. | Separate proof review comparing the Dario Jose source cluster against identity-bearing Dario/Jose records; do not infer from `Jose del Carmen Segundo`. |
| `Dario Pulgar Arriagada` / `Dario Pulgar A.` | No literal mention. Existing staged context has later medical, passenger, property, or legal-notice leads, but none are bridged here. | Very low same-person support; probability 0.02. | Separate identity-bridge proof review comparing proof-reviewed Dario Pulgar Arriagada, Dario J. Pulgar Arriagada, Dario Pulgar A., and property/medical facts. |
| `Jose del Carmen Pulgar` parent candidate | Assigned chunk/source packet name father as `Jose del Carmen Pulgar` with possible suffix `S.`. | Possible father candidate only if Pulgar row is certified; probability 0.42. | Full-image row-control QA plus father-field crop review before any parent claim or merge. |
| `Juana Arriagada de Pulgar` parent candidate | Assigned chunk/source packet name mother as `Juana Arriagada de Pulgar`; existing wiki has low-confidence entry-172 child evidence. | Possible/probable mother candidate only if Pulgar row is certified; probability 0.55. | Full-image row-control QA before relationship promotion; separate Jose/Juana comparison before merging with `Juana de Dios Amagada de Pulgar` or other maternal-surname variants. |
| `Juana de Dios Amagada de Pulgar` parent candidate | Not named in this draft. Appears in separate entry-513/Tulio context. | Separate candidate; probability 0.10 for identity with entry-172 mother from this draft alone. | Separate parent-candidate proof review using entry-513 evidence and image-sensitive surname review; do not reconcile through spouse or broad Pulgar context. |

## Conflict Classification

- Same-person conflict: unresolved. This draft cannot support a Dario same-person conclusion.
- Duplicate-person risk: high if the entry-172 Pulgar child or parents are merged to existing canonical pages before row-control QA.
- Name-variant issue: limited to the father-field suffix after `Jose del Carmen Pulgar`; this is not a Dario-name variant.
- Relationship conflict: high. The two readings assign different parent-child sets to entry `172`.
- Chronology conflict: high. The two readings give different birth dates, times, and places.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Conflict severity | 0.90 | Same entry number, different child, parents, birth event, place, and informant. |
| Evidence quality | 0.60 | Civil birth registration would be strong evidence, but the usable derivative layers disagree and the full image is absent. |
| Conversion confidence | 0.42 | Assigned chunk and current converted Markdown materially conflict. |
| Claim probability: Pulgar/Arriagada row controls entry 172 | 0.68 | Strong staged support, but not certifiable without full-page QA. |
| Claim probability: Burgos/de la Cruz row controls entry 172 | 0.20 | Supported by current converted Markdown only, contradicted by chunk and packet. |
| Relevance | 0.88 | High if the Pulgar/Arriagada row is certified; otherwise no Pulgar-line relevance. |
| Canonical readiness | 0.10 | Not ready for promotion, merge, relationship attachment, or wiki update. |

## Recommended Next Action

Keep this staged draft on `hold_for_conversion_qa`. Do not merge people, rename canonical pages, promote birth facts, promote parent-child relationships, attach entry `172` to any Dario identity, or strengthen existing canonical Pulgar/Juana facts from this packet.

Exact next step: targeted row-control QA using the original full-page image, assigned chunk, current converted Markdown, manifest, and any staged crop assets. The reviewer must certify whether entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and must bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, run proof review only on the narrow certified claims: child name, birth date/time/place, father-name reading, mother-name reading, informant reading, and parent-child relationships. A separate identity-bridge proof review is required before comparing any certified Jose/Juana/child cluster to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`.
