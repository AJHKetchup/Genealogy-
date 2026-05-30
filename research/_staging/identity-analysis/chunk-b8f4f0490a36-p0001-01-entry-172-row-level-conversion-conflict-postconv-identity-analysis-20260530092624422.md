---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530092624422
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
subject: "Entry 172 Pulgar/Arriagada versus Burgos/de la Cruz row-control conflict"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530072501797.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530072501797.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
analysis_status: hold_for_conversion_qa_and_proof_review
canonical_readiness: hold
promotion_recommendation: do_not_promote_or_merge
---

# Identity/Conflict Analysis: Entry 172 Row-Control Hold

## Blockers First

1. Exact staged draft analyzed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md`.
2. This is a conversion row-control conflict, not a same-person or name-variant merge candidate.
3. The assigned chunk records entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, but the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
4. The referenced full source PNG is absent in this checkout (`raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` was not present), so this analysis cannot certify the full physical row.
5. Existing staged crop assets visibly support Pulgar/Arriagada parent and informant fields at crop level, but they do not replace full-page row-control QA and do not settle the possible father-name suffix after `Jose del Carmen Pulgar`.
6. Do not attach the Burgos/de la Cruz details to `Jose del Carmen Segundo Pulgar Arriagada`.
7. Do not use this row to merge or bridge `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, or any Jose/Juana parent candidates.
8. No external research was performed. Raw sources, converted Markdown, chunks, source packets, reviewed notes, and canonical wiki pages were not edited.

## Literal Evidence Reviewed

From the assigned chunk:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

From the current converted Markdown for the same entry number:

```text
Entry 172 ... Nombres. José Miguel ... Fecha. El seis de Abril de mil ochocientos ochenta i ocho ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz
```

From the targeted conversion-review note: staged crop assets support the visible names `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.` at crop level, while the full source image remains unavailable in this checkout.

Interpretation kept separate: the best current interpretation is a held derivative row-control conflict. The Pulgar/Arriagada row may be the controlling entry once full-image QA is available, but it is not promotion-ready from the current evidence packet alone.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Supporting evidence:

- The assigned chunk records entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male.
- The assigned chunk gives registration date `7 April 1888`, birth date/time `8 March 1888, three in the afternoon`, and birth place `Calle de Valdivia`.
- The assigned chunk gives father as `Jose del Carmen Pulgar S.` and mother as `Juana Arriagada de Pulgar`.
- The targeted conversion-review note says staged crop assets visibly support `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.` at crop level.

Conflicts and limits:

- The current converted Markdown materially disagrees with the entire entry row.
- The full source PNG is missing, so physical row order cannot be certified here.
- The father-name suffix after `Pulgar` is not certified; preserve only `Jose del Carmen Pulgar` unless full-image QA confirms `S.` or another mark.
- Existing canonical pages already contain auto-generated Pulgar/Arriagada evidence, but the staged draft directs a hold; do not use this analysis to promote or normalize those pages.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Strong staged chunk and crop support for the page-local row, but full-row certification is blocked. |
| conflict_severity | 0.92 | The converted file and assigned chunk describe different children, parents, dates, and contexts under entry 172. |
| evidence_quality | 0.62 | Direct chunk plus crop-level support, limited by absent full source image. |
| conversion_confidence | 0.45 | Current conversion state is internally inconsistent across derivative outputs. |
| claim_probability | 0.66 | Probable as a held row-control candidate, not yet a promotable fact. |
| relevance | 1.00 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.05 | Hold for conversion QA and proof review before any canonical claim or relationship. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Supporting evidence:

- The current converted Markdown records entry `172` as `José Miguel`, born `6 April 1888`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The converted Markdown is the current derivative conversion file cited in the staged materials.

Conflicts and limits:

- The assigned chunk for the same source hash and entry number instead records the Pulgar/Arriagada row.
- The staged conflict draft and conversion-review note both treat the Burgos/de la Cruz reading as a derivative row-control conflict.
- Burgos/de la Cruz details do not share a child name, parent names, birth date, or location with the Pulgar/Arriagada row; this is not a spelling variant.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | Exists in the current converted file, but is contradicted by the assigned chunk and crop-supported review note. |
| conflict_severity | 0.92 | If treated as the same row, it would substitute an unrelated family. |
| evidence_quality | 0.34 | Derivative conversion text only, with targeted review already flagging row-control failure. |
| conversion_confidence | 0.22 | Low for this row because the current conversion conflicts with chunk and staged QA. |
| claim_probability | 0.20 | Possible only as a misplaced or wrong-row derivative reading until full-image QA resolves it. |
| relevance | 1.00 | This is the competing row in the staged conflict. |
| canonical_readiness | 0.00 | Do not attach to Pulgar/Arriagada or promote from this packet. |

## Hypothesis 3: Jose del Carmen Pulgar And Juana Arriagada de Pulgar Are Parents Of Jose del Carmen Segundo Pulgar Arriagada

Supporting evidence:

- The assigned chunk names father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar` in the same row as child `Jose del Carmen Segundo Pulgar Arriagada`.
- The staged conversion-review note says crop assets visibly support the parent and informant fields.
- Existing canonical stubs preserve `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` as local Pulgar-line candidates.

Conflicts and limits:

- The father suffix is unresolved; do not promote `S.` as a stable name element.
- The current converted Markdown names different parents for entry `172`.
- Existing local context also includes `Juana de Dios Amagada de Pulgar` and a separate `Jose del Carmen Pulgar` parent candidate for `Tulio Cesar Luis Jose`; this record does not prove whether the Jose/Juana candidates are the same people across records.

| Metric | Score | Rationale |
| --- | ---: | --- |
| relationship_confidence | 0.60 | The assigned row supports parentage if row-control is confirmed. |
| conflict_severity | 0.88 | Parent assignment would be wrong if the row-control issue resolves against Pulgar/Arriagada. |
| evidence_quality | 0.58 | Direct row text plus crop support, but no full-page certification. |
| conversion_confidence | 0.44 | Parent fields are crop-supported, while row control remains unresolved. |
| claim_probability | 0.58 | Plausible and family-relevant, but held. |
| relevance | 0.95 | Directly relevant to the Pulgar/Arriagada row. |
| canonical_readiness | 0.04 | Do not promote parent links until full-image QA and proof review accept the row. |

## Hypothesis 4: Jose/Juana Parent Candidates Link This Row To Dario-Line Identities

Supporting evidence:

- The row includes Pulgar and Arriagada surname elements that are relevant to broader Pulgar-line review.
- Existing wiki/staged context includes `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and canonical `Darío Pulgar Arriagada`.

Conflicts and limits:

- The assigned row names no Dario.
- The row states no spouse, child, descendant, grandchild, occupation continuity, property, passenger, CV, or diplomatic/medical context connecting it to a Dario identity.
- `Jose del Carmen Segundo Pulgar Arriagada` is a child born in 1888; no evidence here makes him the same person as any Dario Pulgar candidate.
- Family-context hints justify a future double-check, not a silent correction or Dario-line attachment.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_or_relationship_confidence | 0.04 | No direct Dario or descendant relationship appears in the row. |
| conflict_severity | 0.82 | Unsupported Dario-line attachment could create major duplicate-person and chronology conflicts. |
| evidence_quality | 0.30 | Only surname/family-context relevance, not identity evidence. |
| conversion_confidence | 0.40 | The underlying row remains QA-sensitive. |
| claim_probability | 0.03 | No Dario identity bridge is supported by this row. |
| relevance | 0.82 | Required Pulgar-line anti-conflation check. |
| canonical_readiness | 0.00 | No Dario-line merge, attachment, or relationship promotion. |

## Required Pulgar-Line Comparison

| Candidate | Evidence from this staged draft and local context | Probability from this row | Disposition |
| --- | --- | ---: | --- |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal-grandfather page exists and warns against automatic attachment of similar Pulgar records. This row does not state `Dario`, `Arturo`, `Smith`, or Alexander John Heinz. | 0.02 | Do not attach; require explicit reviewed bridge from a Dario/Pulgar-Smith source. |
| `Dario Arturo Pulgar` | Staged CV materials preserve a document-level `Dario Arturo Pulgar` cluster. This row does not state `Dario Arturo` or CV/work-history facts. | 0.02 | Separate hypothesis only; require CV identity-bridge proof review. |
| `Dario Jose Pulgar-Arriagada` | Local staged materials preserve a `Dario Jose Pulgar-Arriagada` lead in other source contexts. This row names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. | 0.03 | Do not merge; require a source naming Dario Jose with parents, dates, or other direct bridge. |
| `Dario/Dario Pulgar Arriagada` / `Darío Pulgar Arriagada` | Existing canonical stub records `Darío Pulgar Arriagada` in a 2000 legal/expropriation context. This 1888 birth-row candidate does not state Dario or later property context. | 0.03 | Do not attach; chronology and identity bridge required. |
| `Jose del Carmen Pulgar` parent candidate | Assigned row supports father `Jose del Carmen Pulgar` if Pulgar/Arriagada row is certified. Existing `Jose del Carmen Pulgar` wiki page also has separate held child evidence for Tulio Cesar Luis Jose. | 0.58 parentage for this child if row certified; 0.20 same as other Jose candidate | Hold parentage; do not merge Jose candidates across records without proof review. |
| `Juana Arriagada de Pulgar` parent candidate | Assigned row and crop review support mother `Juana Arriagada de Pulgar` if row is certified. | 0.60 parentage for this child if row certified | Hold parentage until full-image row-control QA. |
| `Juana de Dios Amagada de Pulgar` parent candidate | Existing wiki context has a separate Juana candidate for Tulio Cesar Luis Jose. The assigned row reads `Juana Arriagada de Pulgar`, not `Juana de Dios Amagada de Pulgar`. | 0.12 same person | Do not merge; require name and relationship proof across records. |

## Conflict Findings

- Same-person evidence: none between Pulgar/Arriagada and Burgos/de la Cruz. They are competing row-control readings, not one person with variant names.
- Duplicate-person evidence: unresolved for `Jose del Carmen Pulgar` and Juana candidates across other local birth records; not resolvable from this row while row-control is held.
- Name-variant evidence: `Jose del Carmen Pulgar S.` may contain a suffix or mark, but this analysis preserves only the broad certified name `Jose del Carmen Pulgar` pending full-image QA. `Juana Arriagada de Pulgar` is not silently normalized to `Juana de Dios Amagada de Pulgar`.
- Relationship-conflict evidence: assigning Burgos/de la Cruz parents to `Jose del Carmen Segundo Pulgar Arriagada` would be a material relationship error. Assigning Jose/Juana parentage is plausible only if the Pulgar/Arriagada row is certified.
- Chronology-conflict evidence: none internal to the Pulgar/Arriagada row once read as a birth registration, but cross-cluster Dario attachment is chronology-sensitive and unsupported.
- Conversion-confidence conflict: current converted Markdown and assigned chunk disagree at row level; staged crop assets favor Pulgar/Arriagada parent fields but do not certify the full source row.

## Ranked Conclusion

| Rank | Candidate or interpretation | Probability | Current disposition |
| ---: | --- | ---: | --- |
| 1 | Held row-control candidate: entry 172 is the Pulgar/Arriagada birth row | 0.66 | Hold for full-image conversion QA and proof review. |
| 2 | Parentage: Jose del Carmen Pulgar and Juana Arriagada de Pulgar are parents of Jose del Carmen Segundo Pulgar Arriagada | 0.58 | Hold; promote only after row-control certification. |
| 3 | Current converted Markdown's Burgos/de la Cruz entry is the controlling row | 0.20 | Treat as unresolved competing derivative reading; do not attach to Pulgar row. |
| 4 | Same Jose/Juana candidates as other local Jose/Juana parent clusters | 0.12-0.20 | Preserve as future comparison only; do not merge. |
| 5 | Bridge to `Dario Jose Pulgar-Arriagada` or `Darío Pulgar Arriagada` | 0.03 | Unsupported from this row; no Dario attachment. |
| 6 | Bridge to `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith` | 0.02 | Unsupported from this row; no Pulgar-Smith attachment. |

## Recommended Next Action

Keep the staged conflict draft and all dependent claims at `hold_for_conversion_qa`.

Exact next proof-review step: a conversion-QA worker with access to the original full-page PNG should compare the full source image, assigned chunk, current converted Markdown, and staged crop assets to certify whether physical entry `172` is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row. That review must preserve the father field only as the image supports: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, rerun proof review before any canonical claim, relationship, parent merge, Dario-line bridge, or wiki update. Until then, do not merge `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` by name or surname context alone.
