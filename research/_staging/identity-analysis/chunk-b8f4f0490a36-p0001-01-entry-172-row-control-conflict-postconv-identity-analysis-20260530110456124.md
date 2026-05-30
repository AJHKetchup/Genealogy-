---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md"
worker: "postconv-identity-analysis-20260530110456124"
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

- Row-control blocker: the assigned chunk and current converted Markdown do not describe the same entry-172 person cluster.
- Full-image blocker: the staged source packet says the full original PNG was absent in this checkout and available crop assets cannot certify the physical row number.
- Father-name blocker: the chunk reads `Jose del Carmen Pulgar S.`, while the packet instructs holding the father as `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar [?]` until the suffix is visible and certified.
- Relationship blocker: the conflict assigns different parents to entry `172`, so no parent-child claim from this draft is ready for promotion.
- Pulgar-line blocker: the staged draft does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada. No Dario identity bridge is supported by this entry alone.

## Literal Readings

Assigned chunk/source-packet reading:

- Entry `172`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about three in the afternoon, at `Calle de Valdivia`.
- Father: chunk transcription `Jose del Carmen Pulgar S.`; source-packet bound reading `Jose del Carmen Pulgar` pending suffix QA.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, resident at `Calle de Valdivia`.

Current converted Markdown reading:

- Entry `172`; child `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, at ten at night, at `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`, age twenty-six, employed, resident at `En esta`.

Interpretation: these readings are not spelling variants. They are a material row-control conflict involving child identity, parents, date/time, place, and informant.

## Hypotheses And Evidence

| Rank | Hypothesis | Supporting evidence | Conflicts/limits | Claim probability | Identity confidence | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada row. | Assigned chunk and staged source packet consistently name `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`; existing wiki stubs already preserve the child/mother cluster as low-confidence/probable. | Current converted Markdown gives a different row; full source image was not available in this extraction pass. | 0.68 | 0.62 | hold |
| 2 | Entry `172` is the Burgos/de la Cruz row from the current converted Markdown. | Current converted file explicitly labels entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. | Assigned chunk and source packet conflict directly; no Pulgar/Arriagada bridge exists for this reading. | 0.20 | 0.22 | hold |
| 3 | The two readings reflect a derivative row/page mismatch. | The two clusters differ across every identity-controlling field, which is more consistent with row-control drift than same-person variation. | Exact cause cannot be resolved without full-page source QA. | 0.82 | 0.76 | hold |
| 4 | The father in the assigned row is the canonical `Jose del Carmen Pulgar`. | Same name and Pulgar family context; a canonical stub exists. | Same-name evidence is insufficient; suffix unresolved; row-control unresolved. | 0.42 | 0.34 | not_ready |
| 5 | The mother in the assigned row is the canonical `Juana Arriagada de Pulgar`. | Exact name match to canonical stub; existing wiki has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`. | Relationship depends on row-control certification and does not independently prove broader identity. | 0.55 | 0.45 | not_ready |
| 6 | The assigned entry-172 child is the same person as a Dario Pulgar candidate. | Only a broad Pulgar/Arriagada surname context exists. | The child is named `Jose del Carmen Segundo Pulgar Arriagada`, not Dario; no Arturo, Smith, Dario Jose, occupation, spouse, descendant, or later-life bridge appears here. | 0.03 | 0.02 | not_ready |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merges with similarly named Pulgar records. This entry supplies no `Dario`, `Arturo`, `Smith`, Alexander relationship, or maternal-grandfather evidence. Same-person probability from this draft: 0.01.
- `Dario Arturo Pulgar`: staged CV context elsewhere identifies a document subject by source title, but this entry does not name Dario Arturo or connect the 1888 Jose/Juana cluster to the CV subject. Same-person probability: 0.02.
- `Dario Jose Pulgar-Arriagada`: the surname overlap is not enough. Entry `172` names `Jose del Carmen Segundo Pulgar Arriagada` and gives no later identity bridge. Same-person probability: 0.03.
- `Dario/Dario Pulgar Arriagada`: existing context includes a later legal-notice/name cluster for Dario Pulgar Arriagada, but this entry supplies no age, parentage bridge, address bridge, profession bridge, or continuous chronology to that person. Same-person probability: 0.02.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` remain candidates only if full-image QA certifies the Pulgar/Arriagada row as entry `172`. Do not silently equate `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` from other staged context.

## Conflict Classification

- Same-person conflict: unresolved; no Dario same-person conclusion is supported.
- Duplicate-person risk: high if the child or parents are merged to canonical pages before row-control QA.
- Name-variant issue: limited to the possible father suffix after `Pulgar`; do not promote `S.` yet.
- Relationship conflict: high because the two readings assign different parent-child sets to the same entry number.
- Chronology conflict: high because the two readings give different birth dates, times, and places.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Conflict severity | 0.90 | Same entry number, different child, parents, birth event, place, and informant. |
| Evidence quality | 0.60 | Civil birth registration is strong evidence type, but this pass lacks full-image row certification. |
| Conversion confidence | 0.42 | The assigned chunk and current converted Markdown materially disagree. |
| Claim probability: Pulgar/Arriagada row controls | 0.68 | Strong staged support, but blocked by full-page QA. |
| Relevance | 0.88 | High relevance if the Pulgar/Arriagada row is certified. |
| Canonical readiness | 0.10 | Not ready for promotion, merge, relationship attachment, or wiki update. |

## Recommended Next Action

Keep this draft on `hold_for_conversion_qa`. Do not merge people, rename pages, promote parent-child relationships, attach entry `172` to any Dario identity, or strengthen existing canonical facts from this packet.

Exact next step: targeted row-control proof review using the original full-page image, assigned chunk, current converted Markdown, manifest, and any staged crop assets. The reviewer must certify which physical row controls entry `172` and bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Only after that should proof review consider narrow birth-name, birth-event, parent-name, and parent-child claims. A separate identity-bridge review is required before comparing any certified Jose/Juana/child cluster to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.
