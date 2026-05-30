---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
worker: "postconv-identity-analysis-20260530065613888"
role: identity_researcher
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
identity_confidence_score: 0.32
conflict_severity_score: 0.90
evidence_quality_score: 0.58
conversion_confidence_score: 0.40
claim_probability: 0.55
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Row-Control Conflict

## Blockers First

- Original-image row control is still not certified in this task. The referenced conversion review says the source PNG was not present under `raw/sources/`, so the analysis can compare staged text, chunk text, crop-review notes, and existing wiki context only.
- The assigned chunk and the current converted Markdown give materially different entry `172` rows. This is a conversion row-control conflict, not a same-person or name-variant conflict.
- The father field suffix after `Jose del Carmen Pulgar` is not promotion-ready. Preserve the father only as `Jose del Carmen Pulgar` unless later original-image QA certifies `Pulgar S.` or another suffix.
- No reviewed evidence in this entry bridges `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar` to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, later `Darío Pulgar Arriagada`, or passenger-list `Dario Pulgar` clusters.
- Existing canonical wiki pages already contain some auto-generated entry-172 evidence, but this staged review should not use that as a reason to promote more. The current task remains blocked by the derivative conversion conflict.

## Literal Evidence Compared

The staged conflict draft states that the assigned chunk and existing staged crop assets support a Pulgar/Arriagada row for entry `172`, while the current converted Markdown records a Burgos/de la Cruz row for entry `172`.

The referenced source packet quotes the assigned chunk row as:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

The current converted Markdown instead reads entry `172` as `Jose Miguel`, male, born 6 April 1888, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, with `Oswaldo Burgos` as compareciente.

The conversion-review note reports that staged crop assets visibly support lower parent/informant fields for the Pulgar/Arriagada row, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`, but do not certify the suffix after `Pulgar` or substitute for full original-page row-control QA.

## Hypotheses Ranked

1. Hypothesis A: entry `172` is the Pulgar/Arriagada birth row, and the current converted Markdown is stale, row-shifted, or from a different page/image context.
   - Support: assigned chunk, staged source packet, and conversion-review note all align on child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, registration date 7 April 1888, and birth date 8 March 1888.
   - Limits: original PNG was unavailable for this worker's fresh certification; crop support is partial and derivative.
   - Probability: 0.62.
   - Identity confidence: 0.55 for the page-local Pulgar/Arriagada family unit only.

2. Hypothesis B: entry `172` is the Burgos/de la Cruz birth row as represented in the current converted Markdown.
   - Support: current converted Markdown explicitly assigns entry `172` to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
   - Limits: the assigned chunk and later staged QA notes contradict this reading; no Pulgar/Arriagada identity should be reconciled into Burgos/de la Cruz.
   - Probability: 0.25.
   - Identity confidence: 0.25 for using the converted Markdown row as controlling.

3. Hypothesis C: both readings reflect distinct real rows/pages and the conflict is caused by page/source identity mismatch rather than simple row shift.
   - Support: the converted Markdown has a coherent separate Burgos/de la Cruz entry set, while the assigned chunk has a coherent separate Pulgar/Arriagada entry set.
   - Limits: current local evidence does not establish which source image each derivative text came from.
   - Probability: 0.13.
   - Identity confidence: 0.20 until source-image SHA and page identity are checked.

## Pulgar-Line Identity Comparison

- `Dario Arturo Pulgar-Smith`: existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry `172` does not name `Dario`, `Arturo`, or `Smith`, and does not state a bridge to this canonical person. Same-person probability with the 1888 child is very low on present evidence: 0.03.
- `Dario Arturo Pulgar`: staged CV packets are document-level occupational evidence for a CV subject named `Dario Arturo Pulgar`; they require identity-bridge proof review before attachment to `Dario Arturo Pulgar-Smith`. Entry `172` does not provide a direct bridge. Same-person probability with the 1888 child: 0.05.
- `Dario Jose Pulgar-Arriagada`: staged portrait/group-photo packets use source title or metadata context for the name, often with no visible page caption. Entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. Possible broader surname-line relevance exists, but no same-person support. Same-person probability: 0.04.
- `Darío J. Pulgar Arriagada` / `Darío Pulgar Arriagada`: the 1918 university title-conferral packet supports a narrow claim that `Darío J. Pulgar Arriagada` was listed under `Médicos-Cirujanos`; later wiki context includes a `Darío Pulgar Arriagada` property-resolution stub. Entry `172` could be a generational or collateral clue only if later proof establishes parentage, dates, and name continuity. Same-person probability with the 1888 child is not supported because the given names differ and no `Dario` reading appears in entry `172`: 0.08.
- `Jose del Carmen Pulgar`: entry `172`, if row-controlled as Pulgar/Arriagada, likely identifies a father named `Jose del Carmen Pulgar`; the suffix remains unresolved. Existing wiki context also has a `Jose del Carmen Pulgar` stub with a separate draft child link from entry 513. Duplicate-person probability between the entry-172 father and the existing stub is plausible but unproved: 0.45. Required next step: proof review after original-image row-control QA, followed by a dedicated parent-identity review comparing entry 172 and entry 513 father/declarant evidence.
- `Juana Arriagada de Pulgar`: entry `172`, if row-controlled as Pulgar/Arriagada, identifies the mother as `Juana Arriagada de Pulgar`. Existing canonical page of that name has an auto-generated probable child link from entry 172. This is likely the same page-local candidate, but canonical readiness remains blocked by the row-control conflict: 0.60 for page-local identity, 0.35 for canonical promotion readiness.
- `Juana de Dios Amagada de Pulgar` and related Juana parent candidates: existing wiki context has a separate `Juana de Dios Amagada de Pulgar` stub tied to a draft entry 513 child link. Entry `172` reads `Juana Arriagada de Pulgar`; entry 513 notes elsewhere preserve uncertainty around `Ama[?]gar` / `Ama[?]gada` and warn not to normalize to Arriagada. Duplicate-person probability between these Juana candidates is low-to-moderate and blocked: 0.25. Required next step: separate identity review after both entries have proof-reviewed, uncertainty-marked parent fields.
- Burgos/de la Cruz candidates: the converted Markdown row names `Jose Miguel`, `Oswaldo Burgos`, and `Concepcion de la Cruz`. If this row belongs to another page, it should remain a separate non-Pulgar cluster. Same-person or relationship probability with the Pulgar/Arriagada row is near zero: 0.02.

## Conflict Assessment

- Conflict type: row-control conversion conflict.
- Same-person conflict: not established. The conflict is between derivative representations of entry `172`, not between two name variants for one person.
- Relationship conflict: high severity if promoted, because one derivative row creates a Pulgar/Arriagada parent-child unit and the other creates a Burgos/de la Cruz parent-child unit for the same entry number.
- Chronology conflict: high severity for entry `172` because birth dates differ, 8 March 1888 versus 6 April 1888. No chronology bridge to later Dario clusters is supported.
- Name-variant conflict: low for the Pulgar row itself; `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` is an unresolved suffix issue, not a full identity variant.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Page-local Pulgar/Arriagada identities are plausible, but no Dario-line identity bridge is proved. |
| conflict_severity | 0.90 | Wrong row control would attach the wrong child, parents, dates, and family line. |
| evidence_quality | 0.58 | Civil-registration evidence would be strong, but current support is derivative plus partial crop QA. |
| conversion_confidence | 0.40 | Assigned chunk and crop notes align, but current converted Markdown materially conflicts and original image is not certified here. |
| claim_probability | 0.55 | Pulgar/Arriagada row is more likely than Burgos/de la Cruz on staged evidence, but not promotion-ready. |
| relevance | high | Pulgar/Arriagada terms and parent-child evidence are directly family-relevant if row control is confirmed. |
| relevance_confidence | 0.85 | The family relevance is strong under Hypothesis A, but depends on row-control resolution. |
| canonical_readiness | hold_for_conversion_qa | Do not promote, merge, rename, or attach Dario-line facts yet. |

## Recommended Next Action

Run targeted original-image conversion QA for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, comparing the original source image, assigned chunk, current converted Markdown, staged crop assets, and the source packet. The QA must decide whether entry `172` is controlled by the Pulgar/Arriagada row, the Burgos/de la Cruz row, or a page/source mismatch, and must preserve the father field only to the visible level of certainty.

After that, run proof review on this staged identity analysis and the dependent source packet/relationship claims before any canonical claim, relationship, Dario-line attachment, identity merge, wiki update, or parent-candidate reconciliation.
