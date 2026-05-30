---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530091304569
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
subject: "Entry 172 Pulgar/Arriagada versus Burgos/de la Cruz row-control conflict"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530072501797.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530072501797.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
analysis_status: hold_for_original_image_row_control_qa
canonical_readiness: hold
promotion_recommendation: do_not_promote_from_conflict_note
---

# Identity/Conflict Analysis: Entry 172 Row-Control Conflict

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md`.
- This is a conversion row-control conflict, not a same-person merge candidate. The assigned chunk and staged packet identify entry `172` as a Pulgar/Arriagada birth row; the current converted Markdown for the same converted file identifies entry `172` as a Burgos/de la Cruz birth row.
- The referenced original source PNG is not present under either expected `raw/sources/` spelling in this checkout, so this review cannot freshly certify the full-page original image.
- Existing staged crop assets are useful row-local support for the Pulgar/Arriagada parent/informant fields, but they do not replace full-page row-control QA and do not certify the suffix after `Jose del Carmen Pulgar`.
- Do not attach `Jose Miguel`, `Oswaldo Burgos`, or `Concepcion de la Cruz` details to `Jose del Carmen Segundo Pulgar Arriagada`.
- Do not merge or attach this entry to `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or any Jose/Juana parent candidate by surname or family context alone.
- No external research was performed. Raw sources, converted Markdown, chunks, source packets, reviewed notes, and canonical wiki pages were not edited.

## Literal Evidence Reviewed

- Assigned staged conflict draft says the assigned chunk and existing crop assets support a Pulgar/Arriagada row for entry `172`, while the current converted Markdown records Burgos/de la Cruz for entry `172`.
- Assigned source packet literal row: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at three in the afternoon at Calle de Valdivia; father transcribed in derivative text as `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- Assigned conversion-review note says staged crops visibly support `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`, but not the father-name trailing suffix.
- Current converted Markdown reads entry `172` as `Jose Miguel`, born 6 April 1888, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.

Interpretation kept separate: these are competing row-control readings for the same entry number. They are not alternate names for one child or one parent set.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Supporting evidence:

- The assigned chunk and source packet identify physical row `172` as `Jose del Carmen Segundo Pulgar Arriagada`.
- The staged row gives a coherent birth registration: child, sex, registration date, birth date/time/place, father, mother, and informant.
- Crop-level staged assets support the Pulgar/Arriagada parent and informant fields.
- Existing canonical pages preserve a `Jose del Carmen Segundo Pulgar Arriagada` cluster and a probable mother link to `Juana Arriagada de Pulgar`, but those pages remain low-confidence/held because of this row-control issue.

Conflicts and limits:

- The current converted Markdown gives a materially different row `172`.
- Full-page original-image certification is unavailable in this task.
- The father suffix after `Pulgar` remains unresolved.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong for a row-local child identity if the Pulgar row controls. |
| conflict_severity | 0.92 | Same entry number has different children, parents, and birth data. |
| evidence_quality | 0.68 | Staged row plus crop support, blocked by missing full-page image certification. |
| conversion_confidence | 0.45 | Derivative artifacts conflict; original-image row control is required. |
| claim_probability | 0.74 | Probable staged reading, not promotion-ready. |
| relevance | 1.00 | Directly addresses the assigned conflict draft. |
| canonical_readiness | 0.20 | Hold pending row-control QA and proof review. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Supporting evidence:

- The current converted Markdown renders entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888.

Conflicts and limits:

- The assigned chunk, source packet, and crop-supported QA note contradict this as the controlling row for the staged Pulgar evidence.
- There is no name, parent, date, or family-context overlap sufficient to treat Burgos/de la Cruz as a Pulgar/Arriagada variant.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.28 | Supported here only by the current converted Markdown. |
| conflict_severity | 0.92 | If controlling, it invalidates Pulgar/Arriagada staged claims for entry 172. |
| evidence_quality | 0.42 | Derivative conversion text, contradicted by staged row/crop review. |
| conversion_confidence | 0.30 | Material row-control problem. |
| claim_probability | 0.22 | Possible as current conversion text, weak as controlling row here. |
| relevance | 0.95 | Central conflicting reading. |
| canonical_readiness | 0.00 | Do not promote or attach to Pulgar pages. |

## Hypothesis 3: The Pulgar/Arriagada And Burgos/de la Cruz Readings Are Same-Person Or Name-Variant Evidence

Supporting evidence:

- Both readings are attached to entry number `172` in derivative local materials.

Conflicts and limits:

- Child names, parent names, birth dates, and row context differ materially.
- No reviewed local source bridges `Jose Miguel` to `Jose del Carmen Segundo Pulgar Arriagada`, or `Oswaldo Burgos` / `Concepcion de la Cruz` to `Jose del Carmen Pulgar` / `Juana Arriagada de Pulgar`.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.02 | Entry-number overlap only. |
| conflict_severity | 0.95 | A merge would create false identity and relationship claims. |
| evidence_quality | 0.10 | No identity bridge. |
| conversion_confidence | 0.20 | The issue is conversion-level row control. |
| claim_probability | 0.01 | Not supported. |
| relevance | 0.88 | Necessary anti-merge finding. |
| canonical_readiness | 0.00 | Reject as a merge hypothesis. |

## Hypothesis 4: Jose/Juana Parent Candidate Attachments

Supporting evidence:

- If the Pulgar row controls, the row names father `Jose del Carmen Pulgar S.` in derivative text and mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` is a separate father-name cluster and should remain separate until row-control and suffix QA are resolved.
- Existing local context also contains a distinct `Juana de Dios Ama[?]gada/Amagada de Pulgar` style candidate for other Pulgar entries; that is not named in entry `172`.

Conflicts and limits:

- The current conflict note cannot prove parent relationships until the controlling row is certified.
- The father suffix `S.` must not be expanded or used to merge identities.
- `Juana Arriagada de Pulgar` must not be merged with other Juana candidates by married-name similarity.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_or_relationship_confidence | 0.70 mother if row confirmed; 0.44 father pending suffix; 0.05 alternate Juana candidates | Mother is direct in the staged row; father and alternates remain unresolved. |
| conflict_severity | 0.76 | Parent merges or suffix expansion could corrupt Pulgar-line relationships. |
| evidence_quality | 0.60 | Good derivative row text, blocked by row-control and suffix QA. |
| conversion_confidence | 0.42 | Dependent on full-page original-image review. |
| claim_probability | 0.68 mother; 0.40 father; 0.05 alternate Juana/Jose expansion | Scored from local reviewed evidence only. |
| relevance | 0.95 | Parent candidates are central to the staged Pulgar row. |
| canonical_readiness | 0.18 | Hold; revisit only after row-control proof review. |

## Pulgar-Line Comparison

### Dario Arturo Pulgar-Smith

Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family supplied and explicitly warns against automatic attachment of Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records. Entry `172` does not state `Dario`, `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, or a descendant relationship.

Scores: identity confidence 0.00; conflict severity 0.82 if merged by family context; evidence quality 0.20 for this comparison; conversion confidence not applicable to a Dario bridge; claim probability 0.00; relevance 0.80; canonical readiness 0.00.

### Dario Arturo Pulgar

Staged CV contexts identify a document-level `Dario Arturo Pulgar`, but entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`. No same-person, parent, descendant, or chronology bridge is present.

Scores: identity confidence 0.00; conflict severity 0.78; evidence quality 0.20; conversion confidence not applicable to a Dario bridge; claim probability 0.00; relevance 0.76; canonical readiness 0.00.

### Dario Jose Pulgar-Arriagada

Local staged context preserves `Dario Jose Pulgar-Arriagada` / `Darío J. Pulgar Arriagada` as a separate medical/public-role bridge-review candidate. Entry `172` does not state `Dario`, a `J.` initial, a medical role, or adult identity. `Jose del Carmen Segundo` is the child-name reading in the staged Pulgar row and must not be silently converted into `Dario Jose`.

Scores: identity confidence 0.03; conflict severity 0.80; evidence quality 0.22; conversion confidence 0.40 because the row itself is held; claim probability 0.02; relevance 0.82; canonical readiness 0.00.

### Dario/Dario Pulgar Arriagada

Canonical `wiki/people/dar-o-pulgar-arriagada.md` carries a later legal-notice/expropriation event for `Darío Pulgar Arriagada`. Entry `172` has surname overlap only through `Pulgar Arriagada`; it names a child born in 1888 as `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario`.

Scores: identity confidence 0.04; conflict severity 0.82; evidence quality 0.25; conversion confidence 0.40; claim probability 0.03; relevance 0.82; canonical readiness 0.00.

### Jose/Juana Parent Candidates

The only Jose/Juana candidates directly implicated by the staged Pulgar row are `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. Other Jose/Juana Pulgar-line candidates in existing wiki/staged context require separate review and must not be merged into this row. Entry `172` supplies no Dario parentage.

Scores: relationship confidence 0.70 for `Juana Arriagada de Pulgar` as recorded mother if row-control is confirmed; 0.44 for `Jose del Carmen Pulgar` as recorded father pending suffix/row-control QA; 0.05 for alternate Jose/Juana expansion; conflict severity 0.76; evidence quality 0.60; conversion confidence 0.42; canonical readiness 0.18.

## Conflict Summary

- Same-person conflict: none proved; reject same-person treatment between Pulgar/Arriagada and Burgos/de la Cruz readings.
- Duplicate-person conflict: unresolved only for broader Pulgar-line Jose/Juana and Dario clusters; no duplicate or merge action is supported here.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` is a suffix-certification issue; Burgos/de la Cruz is not a Pulgar/Arriagada name variant.
- Relationship conflict: high risk if Burgos/de la Cruz parent facts attach to `Jose del Carmen Segundo Pulgar Arriagada`, or if `Juana Arriagada de Pulgar` is merged with another Juana candidate.
- Chronology conflict: no internal chronology conflict within the staged Pulgar row; Dario comparisons have no evidence bridge from this 1888 entry.
- Conversion conflict: controlling issue is derivative row control between assigned chunk/crop-supported Pulgar row and current converted Burgos row.

## Ranked Hypotheses

| Rank | Candidate or interpretation | Probability | Current disposition |
| ---: | --- | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada` | 0.74 | Hold for full-page original-image row-control QA and proof review. |
| 2 | Entry `172` is the Burgos/de la Cruz birth registration for `Jose Miguel` | 0.22 | Treat as conflicting derivative conversion; do not attach to Pulgar. |
| 3 | `Juana Arriagada de Pulgar` is the recorded mother if Pulgar row is confirmed | 0.68 | Hold until row-control proof review; preserve literal name. |
| 4 | `Jose del Carmen Pulgar` is the recorded father if Pulgar row is confirmed | 0.40 | Hold father claim until row-control and suffix QA. |
| 5 | Pulgar/Arriagada row bridges to Dario/Dario Pulgar Arriagada or Dario Jose Pulgar-Arriagada | 0.03 | Future lineage clue only; no merge. |
| 6 | Pulgar/Arriagada row bridges to `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith` | 0.00 | Unsupported; do not attach. |
| 7 | Burgos/de la Cruz and Pulgar/Arriagada are same-person/name-variant evidence | 0.01 | Reject as identity hypothesis. |

## Recommended Next Action

Keep the assigned staged conflict on `hold_for_conversion_qa`. The exact next proof-review step is full-page original-image row-control QA for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, page 1/register page 58, physical row entry `172`, comparing:

- `research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530072501797.md`
- `research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530072501797.md`
- `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- the staged parent-field crops under `research/_staging/conversion-review-assets/`

If the original image certifies the Pulgar/Arriagada row as controlling, proof review may proceed only on narrow row facts and must separately decide whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. If the Burgos/de la Cruz row is certified instead, dependent Pulgar/Arriagada claims and relationships should remain held or be reworked as non-controlling derivative evidence. No Dario-line merge, Dario Arturo Pulgar-Smith attachment, Jose/Juana parent merge, or canonical promotion should occur from this conflict note alone.
