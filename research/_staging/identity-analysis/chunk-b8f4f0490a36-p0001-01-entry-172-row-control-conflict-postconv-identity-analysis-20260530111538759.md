---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md"
worker: "postconv-identity-analysis-20260530111449894"
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

- Row-control blocker: the assigned chunk and the current converted Markdown identify different people and families for entry `172`.
- Source-image blocker: the referenced source path `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` is absent in this checkout, matching the source packet's warning that the full original source image is unavailable.
- Conversion blocker: the chunk transcribes a Pulgar/Arriagada row, while the current converted Markdown transcribes a Burgos/de la Cruz row for the same entry number. This cannot be resolved by name normalization.
- Relationship blocker: parent-child claims depend on deciding which row controls entry `172`; no child-parent relationship from this draft is ready for canonical promotion.
- Father-field blocker: the chunk reads `Jose del Carmen Pulgar S.`, but the source packet requires holding the father field to `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar [?]` until the trailing mark is image-certified.
- Pulgar-line blocker: this draft does not literally name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`. Those names must remain anti-conflation comparisons only.
- Jose/Juana blocker: existing wiki context includes `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and separate Jose/Juana-related candidates from other entries. This entry cannot merge or reconcile them by family context alone.

## Literal Source Readings

Assigned chunk and revised source packet reading:

- Entry number: `172`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about three in the afternoon, at `Calle de Valdivia`.
- Father: chunk transcription `Jose del Carmen Pulgar S.`; proof boundary is `Jose del Carmen Pulgar` or uncertain suffix until image QA certifies the visible mark.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age twenty-six, empleado, resident at `Calle de Valdivia`.

Current converted Markdown reading:

- Entry number: `172`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, at ten at night, at `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`, age twenty-six, empleado, resident at `En esta`.

Interpretation: the conflict is row-control/page-alignment evidence, not a same-person, duplicate-person, or spelling-variant issue. The child, parents, birth date/time, birth place, and informant all differ.

## Hypotheses And Evidence

| Rank | Hypothesis | Evidence supporting | Conflicts and limits | Claim probability | Identity confidence | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada row. | The assigned chunk and source packet consistently state `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`. Existing wiki pages for the child and mother carry low-confidence/probable evidence from this cluster. | The current converted Markdown assigns entry `172` to a different family; full-image QA is unavailable here; father suffix is unresolved. | 0.68 | 0.62 | hold_for_conversion_qa |
| 2 | Entry `172` is the Burgos/de la Cruz row. | The current converted Markdown explicitly labels entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. | The assigned chunk and source packet directly conflict; this reading has no Pulgar-family relevance. | 0.20 | 0.22 | hold_for_conversion_qa |
| 3 | The evidence represents a derivative row/page mismatch. | Every identity-controlling field differs between the two readings. | The exact source of the mismatch cannot be resolved without full-page image review. | 0.84 | 0.78 | hold_for_conversion_qa |
| 4 | The assigned-row father is the existing `Jose del Carmen Pulgar` candidate. | Same literal name base appears in the assigned row and an existing canonical stub exists. | Same-name evidence is insufficient; the suffix may matter; row-control is unresolved; other Jose candidates must stay separate. | 0.42 | 0.34 | not_ready |
| 5 | The assigned-row mother is the existing `Juana Arriagada de Pulgar` candidate. | Exact name match to an existing canonical stub; the wiki snapshot already labels the child link as probable but very low confidence. | Relationship depends on row-control certification; do not merge with other Juana variants from separate entries. | 0.55 | 0.45 | not_ready |
| 6 | The assigned-row child is a Dario Pulgar identity candidate. | Only broad surname context: `Pulgar Arriagada`. | The child is named `Jose del Carmen Segundo Pulgar Arriagada`, not Dario; this draft provides no Arturo, Smith, Dario Jose, profession, spouse, age, descendant, or chronology bridge. | 0.03 | 0.02 | not_ready |

## Pulgar-Line Comparison

| Candidate | Evidence from this draft | Ranked assessment | Exact next proof-review or promotion step needed |
| --- | --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | No literal mention of Dario, Arturo, Smith, Alexander John Heinz, or maternal-grandfather relationship. Existing canonical page says not to automatically merge similarly named Pulgar clusters. | Very low same-person support; probability 0.01. | Separate identity-bridge proof review using accepted identity-bearing records before attaching any staged Pulgar evidence to the family-supplied Pulgar-Smith page. |
| `Dario Arturo Pulgar` | No literal mention. Other staged CV contexts may mention a document-level Dario Arturo Pulgar, but this entry does not bridge to that person. | Very low same-person support; probability 0.02. | Proof-review the CV identity bridge separately, then compare only if later accepted evidence provides parentage, birth, age, or family links. |
| `Dario Jose Pulgar-Arriagada` | No literal mention. The draft contains `Jose del Carmen Segundo Pulgar Arriagada`, which is not a Dario Jose reading. | Very low same-person support; probability 0.03. | Separate proof review of the Dario Jose source cluster; do not infer identity from surname or the shared `Jose` element. |
| `Dario Pulgar Arriagada` / `Dario Pulgar A.` | No literal mention. Existing staged context for medical, passenger, property, or legal-notice leads is not bridged by this birth-entry conflict. | Very low same-person support; probability 0.02. | Separate identity-bridge proof review comparing accepted Dario Pulgar Arriagada, Dario J. Pulgar Arriagada, and Dario Pulgar A. evidence. |
| `Jose del Carmen Pulgar` parent candidate | Assigned chunk/source packet name a father with this base name, with possible suffix after `Pulgar`. | Possible father candidate only if the Pulgar row controls entry `172`; probability 0.42. | Full-image row-control QA plus father-field review before any parent claim, merge, or canonical strengthening. |
| `Juana Arriagada de Pulgar` parent candidate | Assigned chunk/source packet name this mother, and existing wiki context has a low-confidence child link. | Possible/probable mother candidate only if the Pulgar row controls entry `172`; probability 0.55. | Full-image row-control QA before promotion; separate Jose/Juana proof review before reconciling with any other Juana candidate. |

## Conflict Classification

- Same-person evidence: not established. This draft does not support identifying the entry-172 child with any Dario candidate.
- Duplicate-person risk: high if the Pulgar child or parents are merged to canonical pages before row-control and father-field QA.
- Name-variant issue: limited to the father suffix after `Jose del Carmen Pulgar`; this is not a Dario name-variant issue.
- Relationship conflict: high because the competing readings assign different parents to the same entry number.
- Chronology conflict: high because the readings give different birth dates, times, and places.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Conflict severity | 0.90 | Same entry number, but different child, parents, birth event, place, and informant. |
| Evidence quality | 0.60 | A civil birth registration would be strong evidence, but the available derivative layers conflict and the full image is absent. |
| Conversion confidence | 0.42 | The chunk and current converted Markdown materially disagree. |
| Claim probability: Pulgar/Arriagada row controls entry 172 | 0.68 | Strong staged support from chunk/source packet, but not certifiable here without full-page QA. |
| Claim probability: Burgos/de la Cruz row controls entry 172 | 0.20 | Supported by the current converted Markdown only, contradicted by the assigned chunk and packet. |
| Relevance | 0.88 | High if the Pulgar/Arriagada row is certified; otherwise low for Pulgar-line work. |
| Canonical readiness | 0.10 | Not ready for promotion, relationship attachment, merge, rename, or wiki update. |

## Recommended Next Action

Keep the staged draft on `hold_for_conversion_qa`. Do not promote birth facts, parent-child relationships, identity merges, canonical name changes, or Dario-line attachments from this evidence.

Exact next action: a conversion-QA worker must restore or locate the full source image, compare the physical row for entry `172` against the assigned chunk and current converted Markdown, and certify whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz. The same QA pass must bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, run proof review only on the certified literal claims: child name, sex, birth date/time/place, father-name reading, mother-name reading, informant reading, and parent-child relationships. A separate identity-bridge proof review is required before comparing any accepted Jose/Juana/child cluster to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`.
