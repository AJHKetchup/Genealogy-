---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530070102977
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
subject: "Entry 172 Pulgar/Arriagada versus Burgos/de la Cruz row-control conflict"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
analysis_status: hold_for_original_image_row_control_qa
canonical_readiness: hold
promotion_recommendation: do_not_promote_from_conflict_note
---

# Identity/Conflict Analysis: Entry 172 Row-Control Conflict

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md`.
- The assigned staged source packet and targeted QA note report a material row-control conflict: staged chunk/crop evidence supports a Pulgar/Arriagada entry 172, while the current converted Markdown at `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` records Burgos/de la Cruz details for entry 172.
- The evidence-extraction worker could not complete fresh original-image certification because the referenced PNG was not present under `raw/sources/` in that checkout. This blocks promotion from the new staged draft even though older promoted context says an earlier image reread supported the Pulgar/Arriagada row.
- This is not a same-person merge candidate. Do not attach `Jose Miguel`, `Oswaldo Burgos`, or `Concepcion de la Cruz` facts to `Jose del Carmen Segundo Pulgar Arriagada`.
- The father field remains suffix-sensitive. Preserve the literal staged reading `Jose del Carmen Pulgar S.` as derivative text, but interpret/promote only `Jose del Carmen Pulgar` until proof review certifies whether the trailing `S.` is present, absent, or uncertain.
- Existing Pulgar-line context includes unresolved or separate candidates: `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, adult and child `Dario Pulgar` passenger entries, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`. Entry 172 does not merge them.
- No external research was performed. Raw sources, converted Markdown, chunks, source packets, reviewed notes, and canonical wiki pages were not edited.

## Literal Evidence Reviewed

From the assigned staged source packet:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

From the targeted QA note, the staged crop assets support the lower parent/informant fields for the Pulgar/Arriagada row, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`, but do not certify a trailing suffix after `Pulgar`.

From the current converted Markdown:

- Entry 172 is rendered as `Jose Miguel`, born 6 April 1888, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Interpretation kept separate: the staged Pulgar/Arriagada evidence and the converted Burgos/de la Cruz evidence are competing row-control readings for entry 172. They are not alternate names for one child or one parent set.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Supporting evidence:

- The assigned staged source packet identifies row 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male.
- The staged row gives registration date 7 April 1888 and birth date/time 8 March 1888 at three in the afternoon at Calle de Valdivia.
- Parent fields name `Jose del Carmen Pulgar S.` in derivative text and `Juana Arriagada de Pulgar`.
- The targeted QA note says existing staged crop assets visibly support `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.` for the Pulgar/Arriagada row.
- Existing canonical pages already preserve a narrow `Jose del Carmen Segundo Pulgar Arriagada` cluster and a probable mother relationship to `Juana Arriagada de Pulgar`, while warning on proof-review and conversion issues.

Conflicts and limits:

- The current converted Markdown for the same converted file has a different entry 172.
- The new staged worker did not certify the original source image directly.
- The father-name suffix cannot be promoted from this review.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong for the staged row-local child identity, held by row-control conflict. |
| conflict_severity | 0.92 | Same entry number has different child and parent sets. |
| evidence_quality | 0.68 | Direct staged row and crop-based QA, but no fresh original-image certification. |
| conversion_confidence | 0.45 | Mixed derivative artifacts; original-image row control must decide. |
| claim_probability | 0.74 | Probable staged reading, not promotion-ready from this task. |
| relevance | 1.00 | Directly answers the assigned conflict draft. |
| canonical_readiness | 0.20 | Hold pending proof-reviewed row-control resolution. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Registration

Supporting evidence:

- The current converted Markdown renders entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888.

Conflicts and limits:

- The assigned staged source packet and targeted QA note directly contradict this reading for physical row 172.
- Burgos/de la Cruz has no name, parent, date, or place overlap with the Pulgar/Arriagada row sufficient to treat it as a variant.
- The staged draft explicitly frames Burgos/de la Cruz as the conflicting current conversion, not a family-relevant Pulgar identity.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.28 | Supported only by the current converted Markdown in this review set. |
| conflict_severity | 0.92 | If accepted for entry 172, it displaces all Pulgar/Arriagada row claims. |
| evidence_quality | 0.42 | Derivative conversion only, contradicted by staged packet/crop review. |
| conversion_confidence | 0.30 | Material row-control concern. |
| claim_probability | 0.22 | Possible conversion row, but weak as controlling entry 172 here. |
| relevance | 0.95 | Central conflicting reading. |
| canonical_readiness | 0.00 | Do not promote or attach to Pulgar pages. |

## Hypothesis 3: Burgos/de la Cruz And Pulgar/Arriagada Are Same-Person Or Name-Variant Evidence

Supporting evidence:

- Both readings are attached to an entry numbered 172 in derivative materials.

Conflicts and limits:

- The child names, parent names, birth dates, and family contexts differ materially.
- There is no literal source reading connecting `Jose Miguel` to `Jose del Carmen Segundo Pulgar Arriagada`, or `Oswaldo Burgos` / `Concepcion de la Cruz` to `Jose del Carmen Pulgar` / `Juana Arriagada de Pulgar`.
- The staged draft correctly treats this as row-control conflict, not identity variation.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.02 | Entry-number overlap only. |
| conflict_severity | 0.95 | A same-person merge would create severe false identity and relationship claims. |
| evidence_quality | 0.10 | No direct identity bridge. |
| conversion_confidence | 0.20 | The conflict itself is conversion-level. |
| claim_probability | 0.01 | Not supported. |
| relevance | 0.88 | Necessary anti-merge finding. |
| canonical_readiness | 0.00 | Reject as a merge hypothesis. |

## Hypothesis 4: Jose/Juana Parent Candidate Attachments

Supporting evidence:

- The staged Pulgar/Arriagada row names father `Jose del Carmen Pulgar S.` in derivative text and mother `Juana Arriagada de Pulgar`.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` preserves a separate `Jose del Carmen Pulgar` cluster with a draft child relationship to `Tulio Cesar Luis Jose`.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` preserves a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- Existing canonical `wiki/people/juana-de-dios-amagada-de-pulgar.md` preserves a separate draft child link to `Tulio Cesar Luis Jose`.

Conflicts and limits:

- Entry 172 supports only the mother name `Juana Arriagada de Pulgar` if the Pulgar/Arriagada row is controlling; it does not name `Juana de Dios Amagada de Pulgar`.
- The father suffix after `Pulgar` remains unresolved and should not be used to expand or merge identities.
- Do not merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` by married-style name similarity or shared Pulgar context.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_or_relationship_confidence | 0.70 for recorded mother if row is confirmed; 0.44 for recorded father; 0.08 for Juana de Dios Amagada link | Mother is direct in the staged row; father suffix and alternate Juana are unresolved. |
| conflict_severity | 0.75 | Parent merges or suffix expansion could corrupt Pulgar-line relationships. |
| evidence_quality | 0.60 | Good row text for names, but blocked by row-control and suffix QA. |
| conversion_confidence | 0.42 | Dependent on original-image row-control proof review. |
| claim_probability | 0.68 mother; 0.40 father; 0.05 Juana de Dios | Scored from reviewed local evidence only. |
| relevance | 0.95 | Parent candidates are central to the staged Pulgar row. |
| canonical_readiness | 0.18 | Hold; only narrow mother link may resume after row-control proof review. |

## Pulgar-Line Comparison Required By Contract

### Dario Arturo Pulgar-Smith

Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family supplied and warns not to attach similarly named Pulgar records without identity review. Entry 172 does not state `Dario`, `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, or a descendant relationship.

Scores: identity confidence 0.00; conflict severity 0.82 if merged by name family context; evidence quality 0.20 for this comparison; conversion confidence not applicable to a Dario bridge; claim probability 0.00; relevance 0.80; canonical readiness 0.00.

### Dario Arturo Pulgar

Staged CV contexts identify a document-level `Dario Arturo Pulgar`, but entry 172 names `Jose del Carmen Segundo Pulgar Arriagada` as a child and does not mention `Dario` or `Arturo`. No same-person, parent, descendant, or chronology bridge is present.

Scores: identity confidence 0.00; conflict severity 0.78; evidence quality 0.20; conversion confidence not applicable to a Dario bridge; claim probability 0.00; relevance 0.76; canonical readiness 0.00.

### Dario Jose Pulgar-Arriagada

Local staged contexts preserve `Dario Jose Pulgar-Arriagada` as a separate bridge-review candidate. Entry 172 does not state `Dario`, `Jose` as a Dario middle name, medical role, adult identity, or any bridge to Dario Jose. `Jose del Carmen Segundo` is a different literal child-name reading and must not be silently transformed into `Dario Jose`.

Scores: identity confidence 0.03; conflict severity 0.80; evidence quality 0.22; conversion confidence 0.40 because the row itself is held; claim probability 0.02; relevance 0.82; canonical readiness 0.00.

### Dario/Dario Pulgar Arriagada

Canonical `wiki/people/dar-o-pulgar-arriagada.md` carries a 2000 legal-notice/expropriation event for `Darío Pulgar Arriagada`. Entry 172 has surname overlap only through `Pulgar Arriagada`; it names a child born in 1888 as `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario`. A lineage clue is possible for future review, but no identity merge is supported.

Scores: identity confidence 0.04; conflict severity 0.82; evidence quality 0.25; conversion confidence 0.40; claim probability 0.03; relevance 0.82; canonical readiness 0.00.

### Jose/Juana Parent Candidates

The only Jose/Juana candidates directly implicated by the staged Pulgar row are `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. `Juana de Dios Amagada de Pulgar` appears in existing wiki context as a separate mother candidate for a different child and should not be merged into this row. No Dario parentage is supported here.

Scores: relationship confidence 0.70 for `Juana Arriagada de Pulgar` as recorded mother if row-control is confirmed; 0.44 for `Jose del Carmen Pulgar` as recorded father pending suffix/row-control QA; 0.05 for any alternate Juana/Jose expansion; conflict severity 0.76; evidence quality 0.60; conversion confidence 0.42; canonical readiness 0.18.

## Conflict Summary

- Same-person conflict: none proved; reject the same-person hypothesis between Pulgar/Arriagada and Burgos/de la Cruz readings.
- Duplicate-person conflict: unresolved only for existing Jose/Juana and Pulgar-line candidate clusters; do not duplicate or merge from this row-control note.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` remains suffix QA; Burgos/de la Cruz is not a name variant of Pulgar/Arriagada.
- Relationship conflict: high risk if Burgos/de la Cruz parent facts are attached to `Jose del Carmen Segundo Pulgar Arriagada`, or if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar`.
- Chronology conflict: no internal chronology conflict within the staged Pulgar row; cross-cluster Dario comparisons have no evidence bridge from this entry and should remain separate.
- Conversion-confidence conflict: controlling issue is derivative row control between the assigned chunk/crop-supported Pulgar row and the current converted Burgos row.

## Ranked Hypotheses

| Rank | Candidate or interpretation | Probability | Current disposition |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada` | 0.74 | Hold for original-image row-control QA and proof review. |
| 2 | Entry 172 is the Burgos/de la Cruz birth registration for `Jose Miguel` | 0.22 | Treat as conflicting derivative conversion; do not attach to Pulgar. |
| 3 | `Juana Arriagada de Pulgar` is the recorded mother if Pulgar row is confirmed | 0.68 | Hold until row-control proof review; preserve as recorded mother name. |
| 4 | `Jose del Carmen Pulgar` is the recorded father if Pulgar row is confirmed | 0.40 | Hold father claim until suffix and row-control QA. |
| 5 | Pulgar/Arriagada row is a bridge to Dario/Dario Pulgar Arriagada or Dario Jose Pulgar-Arriagada | 0.03 | Future lineage clue only; no merge. |
| 6 | Pulgar/Arriagada row is a bridge to `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith` | 0.00 | Unsupported; do not attach. |
| 7 | Burgos/de la Cruz and Pulgar/Arriagada are same-person/name-variant evidence | 0.01 | Reject as identity hypothesis. |

## Recommended Next Action

Keep the assigned staged conflict on `hold_for_conversion_qa`. The exact next proof-review step is an original-image row-control review for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, page 1/register page 58, physical row entry 172, comparing:

- `research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md`
- `research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md`
- the current converted Markdown's Burgos/de la Cruz entry 172
- the staged parent-field crop noted in the QA review

If the original image certifies the Pulgar/Arriagada row as controlling, proof review may proceed only on narrow row facts and should separately decide the father-name suffix. If the Burgos/de la Cruz row is certified instead, dependent Pulgar/Arriagada staged claims and relationship links must remain held or be reworked as non-controlling derivative evidence. No Dario-line merge, Dario Arturo Pulgar-Smith attachment, Jose/Juana parent merge, or canonical promotion should occur from this conflict note alone.
