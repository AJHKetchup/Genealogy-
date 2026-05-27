---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md"
worker: "postconv-identity-analysis-20260527224953897"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-rowcert-postconv-evidence-extraction-20260527221218880.md"
proof_review_request: "research/_staging/tasks/chunk-b8f4f0490a36-p0001-01-entry-172-proof-review-request-postconv-evidence-extraction-20260527221218880.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
analysis_status: "hold_for_proof_review"
canonical_readiness: "not_ready"
---

# Identity And Conflict Analysis: Entry 172 Derivative Row Conflict

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md`.
- The primary blocker is row control. The staged conflict and source packet say physical entry `172` is the Pulgar/Arriagada birth row, while the current converted Markdown says entry `172` is a Burgos/de la Cruz row.
- Canonical promotion is blocked until proof review confirms original-image control for physical entry `172` and preserves or corrects the derivative converted-Markdown conflict.
- The father field is bounded to `Jose del Carmen Pulgar`. The chunk's trailing `S.` after `Pulgar` is unresolved and must not be promoted.
- This evidence does not prove a marriage between the named parents; `de Pulgar` is a family-context hint only.
- No reviewed item in this evidence set names `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or any Dario-line relationship bridge.
- No external research was performed. No raw source, converted Markdown, chunk, source packet, staged conflict draft, or canonical wiki page was edited.

## Literal Evidence Reviewed

- Staged conflict draft: original image and assigned chunk identify physical row `172` as the Pulgar/Arriagada registration for `Jose del Carmen Segundo Pulgar Arriagada`; converted Markdown identifies entry `172` as Burgos/de la Cruz for `Jose Miguel`.
- Source packet literal row: entry `172`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`; child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; birth `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- Source packet boundary: the father field is staged only as `Jose del Carmen Pulgar`; the possible suffix is not promoted.
- Current converted Markdown literal conflict: entry `172` is rendered as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho`.
- Existing wiki context: `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` have low/probable evidence from this entry; `Jose del Carmen Pulgar` also appears in a separate draft child cluster for `Tulio Cesar Luis Jose`; `Juana de Dios Amagada de Pulgar` appears in that separate Tulio cluster.
- Existing Dario context: canonical `Dario Arturo Pulgar-Smith` is family supplied; staged `Dario Arturo Pulgar` CV evidence remains a separate identity-bridge problem; canonical `Darío Pulgar Arriagada` is represented by a 2000 expropriation event. None of those pages is bridged by this 1888 row.

Interpretation kept separate: the local evidence supports a page-local birth-registration candidate for `Jose del Carmen Segundo Pulgar Arriagada` and parent candidates `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, subject to proof review. It does not support a Dario merge, Pulgar-Smith attachment, parent-candidate duplicate merge, or spousal promotion.

## Hypothesis 1: Physical Entry 172 Is Jose del Carmen Segundo Pulgar Arriagada

Evidence supporting:

- The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`.
- The row-certified source packet says the original image controls this staging pass and places Pulgar/Arriagada at physical row `172`.
- The row has internally coherent child, birth date/time/place, parent, and informant fields.

Conflicts and limits:

- The current converted Markdown assigns entry `172` to a different child, `Jose Miguel`, with different parents.
- Promotion requires proof review of the row-control override and father-name boundary.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.86 | Strong local row support for the page-local child identity. |
| conflict_severity | 0.88 | Same entry number is attached to different children and parents. |
| evidence_quality | 0.82 | Civil birth registration is strong evidence, but derivative conflict remains. |
| conversion_confidence | 0.58 | Assigned chunk/source packet are image-reviewed; assembled conversion conflicts. |
| claim_probability | 0.84 | Probable if proof review accepts row control. |
| relevance | 1.00 | Direct subject of the staged conflict. |
| canonical_readiness | 0.34 | Hold pending proof review. |

## Hypothesis 2: Converted Entry 172 Is Jose Miguel Burgos/de la Cruz

Evidence supporting:

- The current converted Markdown explicitly labels the Burgos/de la Cruz entry as `Entry 172`.

Conflicts and limits:

- The staged conflict draft, assigned chunk, and source packet all identify physical row `172` as Pulgar/Arriagada.
- No reviewed local context found for this task supports promoting Burgos/de la Cruz as the controlling identity for the staged Pulgar source packet.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Support comes from the derivative conversion under challenge. |
| conflict_severity | 0.88 | Direct row and family contradiction. |
| evidence_quality | 0.30 | Derivative transcription only in this review context. |
| conversion_confidence | 0.20 | Converted Markdown is specifically flagged as conflicted. |
| claim_probability | 0.16 | Low unless proof review overturns the row-certified packet. |
| relevance | 0.96 | Direct conflict alternative. |
| canonical_readiness | 0.02 | Not ready for promotion. |

## Hypothesis 3: Father Candidate Jose del Carmen Pulgar

Evidence supporting:

- The assigned chunk reads the father field as `Jose del Carmen Pulgar S.`.
- The source packet explicitly bounds the father claim to `Jose del Carmen Pulgar`.
- The proof-review request asks review to confirm whether claims may promote with father limited to `Jose del Carmen Pulgar`.

Conflicts and limits:

- The trailing `S.` is unresolved.
- Existing wiki context has a same-named `Jose del Carmen Pulgar` attached to a separate draft child cluster, so same-person or duplicate-person status is not proven here.
- The converted Markdown conflict gives `Oswaldo Burgos` as father.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong for bounded father-name reading, weaker for canonical identity. |
| conflict_severity | 0.72 | Wrong row control or same-name merge would attach the wrong father. |
| evidence_quality | 0.76 | Direct father field, but suffix unresolved. |
| conversion_confidence | 0.55 | Row packet supports bounded reading despite conversion conflict. |
| claim_probability | 0.76 | Probable as father in the Pulgar row after proof review. |
| relevance | 0.96 | Central parent candidate. |
| canonical_readiness | 0.28 | Hold; do not promote suffix or duplicate merge. |

## Hypothesis 4: Mother Candidate Juana Arriagada de Pulgar

Evidence supporting:

- The assigned chunk and source packet read the mother as `Juana Arriagada de Pulgar`.
- Existing canonical context has a probable child link between `Juana Arriagada de Pulgar` and `Jose del Carmen Segundo Pulgar Arriagada` from this entry.

Conflicts and limits:

- The converted Markdown conflict gives `Concepcion de la Cruz` as mother.
- `Juana Arriagada de Pulgar` is not proven to be the same person as `Juana de Dios Amagada de Pulgar`; the latter belongs to a separate draft Tulio cluster in reviewed wiki context.
- `de Pulgar` should not be treated as a promoted marriage fact from this birth row alone.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.82 | Consistent local support for the mother field. |
| conflict_severity | 0.70 | Wrong row or Juana-name conflation would corrupt relationships. |
| evidence_quality | 0.78 | Direct mother field in a civil register row. |
| conversion_confidence | 0.60 | Packet and chunk support it despite converted Markdown conflict. |
| claim_probability | 0.80 | Probable as mother in the Pulgar row after proof review. |
| relevance | 0.96 | Central parent candidate. |
| canonical_readiness | 0.32 | Hold pending proof review. |

## Hypothesis 5: Same Person As Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Evidence supporting:

- Existing wiki and staged context place these names in the broader Pulgar-line research environment.

Conflicts and limits:

- Entry `172` names no Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, grandchild, CV subject, or modern family relationship.
- Family-context hints justify later lineage review only; they do not justify attachment from this row.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No row-local Dario identity evidence. |
| conflict_severity | 0.62 | Premature attachment would create an unsupported lineage bridge. |
| evidence_quality | 0.36 | Broader context only, not direct evidence. |
| conversion_confidence | 0.40 | Row conflict does not supply Dario evidence. |
| claim_probability | 0.04 | Not supported by this staged draft. |
| relevance | 0.70 | Required anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not attach. |

## Hypothesis 6: Same Person As Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Or Other Dario Pulgar Clusters

Evidence supporting:

- The names share broad Pulgar/Arriagada surname space in existing local context.

Conflicts and limits:

- Entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.
- It gives no `Jose` middle name for a Dario, no `Dario J.`, no `Dario Pulgar A.`, no medical, passenger, property, CV, or convention context.
- Surname overlap alone is insufficient for a same-person or duplicate-person conclusion.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No direct same-person evidence. |
| conflict_severity | 0.76 | High risk of cross-generation or cross-cluster conflation. |
| evidence_quality | 0.34 | Anti-conflation context only. |
| conversion_confidence | 0.40 | Neither row reading names Dario. |
| claim_probability | 0.02 | Not supported by this staged conflict. |
| relevance | 0.72 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Preserve separately or unresolved. |

## Conflict Summary

- Same-person conflict: strongest page-local conclusion is that physical row `172` likely identifies `Jose del Carmen Segundo Pulgar Arriagada`, not the converted Markdown's `Jose Miguel`.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` because existing wiki context has a same-named parent candidate in another draft cluster; high if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar`; high if this row is used to bridge to Dario clusters.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is unresolved; `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are not proven variants.
- Relationship conflict: the row supports father and mother fields for the child, subject to proof review. It does not prove a marriage.
- Chronology conflict: no internal chronology conflict in the Pulgar/Arriagada row; cross-cluster chronology cautions against attaching an 1888 child/parent row to later Dario clusters without lineage proof.
- Conversion conflict: assigned chunk/source packet support Pulgar/Arriagada row control; current converted Markdown supports a different Burgos/de la Cruz row.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Physical entry `172` is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.84 | Proof review must confirm original-image row control and document the converted Markdown as a derivative row conflict. |
| 2 | `Juana Arriagada de Pulgar` is the mother recorded in physical entry `172`. | 0.80 | Promote only after row-control proof review; keep separate from `Juana de Dios Amagada de Pulgar` unless later evidence bridges them. |
| 3 | `Jose del Carmen Pulgar` is the father recorded in physical entry `172`. | 0.76 | Promote only the bounded name after proof review; do not promote `S.` or merge same-named father candidates. |
| 4 | Converted Markdown's Burgos/de la Cruz row is the correct identity for entry `172`. | 0.16 | Requires proof review to overturn the row-certified packet; otherwise keep as conversion conflict only. |
| 5 | Entry `172` bridges to `Dario Arturo Pulgar-Smith` or `Dario Arturo Pulgar`. | 0.04 | No promotion from this row; require separate lineage or identity-bridge proof. |
| 6 | Entry `172` bridges to `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or other Dario Pulgar clusters. | 0.02 | Preserve separately; require direct identity-bearing or lineage evidence before any merge. |

## Recommended Next Action

Keep this staged conflict at `hold_for_proof_review`. The exact next step is the proof review requested in `research/_staging/tasks/chunk-b8f4f0490a36-p0001-01-entry-172-proof-review-request-postconv-evidence-extraction-20260527221218880.md`: confirm that the original image controls physical entry `172` as Pulgar/Arriagada, confirm that the Burgos/de la Cruz text in the current converted Markdown is a derivative-transcript conflict, and decide whether claims may promote with the father limited to `Jose del Carmen Pulgar`.

Do not merge people, rename pages, promote `Jose del Carmen Pulgar S.`, infer a marriage from `de Pulgar`, merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar`, or attach this row to any Dario Pulgar/Pulgar-Smith/Pulgar-Arriagada cluster without separate proof review.
