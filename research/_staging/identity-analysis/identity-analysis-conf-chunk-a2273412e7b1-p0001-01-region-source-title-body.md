---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/conf-chunk-a2273412e7b1-p0001-01-region-source-title-body.md"
worker: postconv-identity-analysis-20260523095657496
staged_conflict_draft: "research/_staging/conflicts/conf-chunk-a2273412e7b1-p0001-01-region-source-title-body.md"
source_packet: "research/_staging/source-packets/sp-chunk-a2273412e7b1-p0001-01-resolucion-283-expropriation-pulgar.md"
chunk_id: "CHUNK-a2273412e7b1-P0001-01"
analysis_date: 2026-05-23
promotion_recommendation: hold_for_conversion_qa
tags: [identity-analysis, conflict-review, source-metadata, pulgar]
---

# Identity And Conflict Analysis: Region Title Versus Body Text

## Blockers First

- The assigned staged conflict draft `research/_staging/conflicts/conf-chunk-a2273412e7b1-p0001-01-region-source-title-body.md` is a source-identity/metadata conflict, not a direct person-identity conflict. It must not be promoted as a canonical person conflict.
- The source title/file path and converted page title identify `V Región de Valparaíso`, while the notice body names `Serviu Región del Bío Bío`, Chiguayante, and `Director Serviu Región del Bío Bío`.
- The source packet keeps a controller `reread-page` / conversion-QA hold even though the converted page says the page is clear and legible.
- The body text names `Darío Pulgar Arriagada` as the apparent domain holder of a Chiguayante property, but the assigned conflict draft does not itself supply age, birth date, death date, occupation, parent, spouse, child, or other identity anchors.
- Existing Pulgar-line context includes separate or unresolved candidates: `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, passenger-list `Dario Pulgar` candidates, and Jose/Juana parent candidates. The region mismatch does not bridge any of these identities.
- The requested `$genealogy-proof-review` skill is not installed in this session; this note applies the evidence-contract requirements from the assignment using local staged, converted, reviewed, and canonical wiki materials only.

## Literal Source Reading

The staged conflict draft preserves this title/header reading:

```text
MINISTERIO DE VIVIENDA Y URBANISMO; SERVICIO DE VIVIENDA Y
URBANIZACIÓN; V REGIÓN DE VALPARAÍSO
```

It also preserves this body-text reading:

```text
Por resolución 283, 5 diciembre 2000, Serviu Región del Bío Bío ordenó
expropiación parcial inmueble ubicado en Línea Ferrea s/n° ... comuna Chiguayante
```

and:

```text
Director Serviu Región del Bío Bío.
```

The referenced source packet and chunk add that the property was of apparent domain of `Darío Pulgar Arriagada` and that the appraisal commission included `Luis Abarzúa Ceballos`.

Interpretation kept separate: the literal text supports a QA caution that the document title/path/header region and the body region/place do not agree. It does not, by itself, change the literal name `Darío Pulgar Arriagada` into another Dario Pulgar identity or prove any family relationship.

## Hypothesis 1: Metadata Or Header Region Error, Body Text Still Refers To Bío Bío / Chiguayante Notice

Hypothesis: the title/path/header region is erroneous or inherited metadata, while the body text accurately describes a Serviu Región del Bío Bío expropriation in Chiguayante.

Evidence supporting:

- The body text repeats Bío Bío context twice: `Serviu Región del Bío Bío` in the opening sentence and `Director Serviu Región del Bío Bío` at the end.
- The body gives a specific Bío Bío-area place, `comuna Chiguayante`, and a specific project, `Mejoramiento Vial Eje O'Higgins de Chiguayante`.
- The source packet treats the mismatch as a conversion-QA concern while still extracting the Pulgar and Luis Abarzúa evidence from the body text.

Conflicts and limits:

- The visible title/header and source filename still say `V Región de Valparaíso`.
- No page-image reread has been recorded for this exact mismatch in the assigned conflict draft.
- This hypothesis does not independently prove that the PDF was filed, titled, or downloaded under the wrong region; it only ranks the body text as internally coherent.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | For source-body identity, repeated Bío Bío/Chiguayante body cues are coherent. |
| conflict_severity | 0.62 | The region mismatch materially affects source citation and claim context. |
| evidence_quality | 0.70 | Official-style notice text is clear, but still derivative conversion output pending reread. |
| conversion_confidence | 0.76 | Conversion reports clear legibility; controller reread and metadata conflict remain. |
| claim_probability | 0.78 | Probable that the notice body is about Bío Bío/Chiguayante if the transcription is confirmed. |
| relevance | 0.94 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.34 | Hold until page/PDF reread reconciles title/header/body. |

## Hypothesis 2: Source Title/Header Correct, Body Text May Be Misfiled Or Imported From Another Notice

Hypothesis: the `V Región de Valparaíso` title/header is authoritative for the source identity, and the Bío Bío/Chiguayante body text may indicate a misfiled or mixed notice.

Evidence supporting:

- The converted page title and source path both name `V Región de Valparaíso`.
- The converted page metadata says the document title is `Resolución 283, Ministerio de Vivienda y Urbanismo; Servicio de Vivienda y Urbanización; V Región de Valparaíso`.
- The source packet explicitly preserves this title/body mismatch as a QA concern.

Conflicts and limits:

- The body text is specific and internally consistent for Bío Bío and Chiguayante.
- No second page, adjacent notice, or mixed-page evidence appears in the assigned converted file or chunk.
- This remains a source QA hypothesis, not evidence that named persons belong to a Valparaíso event.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | The title/path/header support Valparaíso, but the body text points strongly elsewhere. |
| conflict_severity | 0.68 | If true, citation and source identity would need correction before promotion. |
| evidence_quality | 0.54 | Metadata is relevant but less detailed than the body notice. |
| conversion_confidence | 0.64 | Could reflect source metadata capture rather than body transcription. |
| claim_probability | 0.32 | Possible, but not the best fit to the body text. |
| relevance | 0.90 | Directly addresses the assigned conflict. |
| canonical_readiness | 0.18 | Not ready until original page/PDF is reread. |

## Hypothesis 3: Same Legal-Notice Person As Canonical `Darío Pulgar Arriagada`

Hypothesis: despite the region-title conflict, the named person in the notice body is the same legal-notice cluster represented by `wiki/people/dar-o-pulgar-arriagada.md`.

Evidence supporting:

- The source packet's literal support names `Darío Pulgar Arriagada` in apparent domain of the expropriated property.
- The canonical `wiki/people/dar-o-pulgar-arriagada.md` evidence snapshot already records the same 2000-12-05 Serviu Región del Bío Bío expropriation notice and cites this source packet.
- The assigned conflict draft states that the uncertainty is about document/source identity metadata, not about the literal presence of personal names.

Conflicts and limits:

- The canonical stub relies on the same source cluster; it does not add independent corroboration.
- The region mismatch lowers canonical readiness for the associated claim until page reread.
- The phrase `aparente dominio` must remain apparent ownership/domain, not full proven title ownership.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.90 | Exact same name and same expropriation source cluster. |
| conflict_severity | 0.22 | Low person-identity conflict; moderate source-QA hold. |
| evidence_quality | 0.72 | Clear notice text for a narrow claim, but single-source and QA-held. |
| conversion_confidence | 0.76 | Clear conversion with unreconciled reread/title-body issue. |
| claim_probability | 0.84 | Probable that the notice names Darío Pulgar Arriagada if reread confirms. |
| relevance | 0.88 | Direct person named in the source packet behind the conflict draft. |
| canonical_readiness | 0.50 | Existing stub can remain, but no broader claims should be promoted before QA. |

## Hypothesis 4: Same As `Dario Arturo Pulgar` Or `Dario Arturo Pulgar-Smith`

Hypothesis: the notice-body `Darío Pulgar Arriagada` is the same person as staged CV subject `Dario Arturo Pulgar` or canonical family-supplied `Dario Arturo Pulgar-Smith`.

Evidence supporting:

- The names share `Dario/Darío Pulgar`.
- The canonical `Dario Arturo Pulgar-Smith` page explicitly instructs that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith require identity review before attachment.

Conflicts and limits:

- The assigned notice reads `Darío Pulgar Arriagada`, not `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith`.
- The notice gives no `Arturo`, no `Smith`, no family relationship, no occupation, no birth date, and no biographical bridge.
- Family context can justify later comparison, but cannot silently normalize `Pulgar Arriagada` to `Pulgar-Smith`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared given name/surname only; key identity elements are missing or different. |
| conflict_severity | 0.66 | High conflation risk if attached by name alone. |
| evidence_quality | 0.48 | Local family/canonical context is relevant but not a bridge to this notice. |
| conversion_confidence | 0.76 | The notice reading is usable only for its own name form pending reread. |
| claim_probability | 0.12 | Same-person claim is unsupported by this conflict draft. |
| relevance | 0.82 | Required Pulgar-line guardrail comparison. |
| canonical_readiness | 0.03 | Do not attach to Pulgar-Smith or the CV subject from this source alone. |

## Hypothesis 5: Same As `Dario Jose Pulgar-Arriagada` Or Other `Dario/Darío Pulgar Arriagada` Candidates

Hypothesis: `Darío Pulgar Arriagada` in the notice is a variant or duplicate of `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario Pulgar A.` clusters.

Evidence supporting:

- The surname pattern `Pulgar Arriagada` overlaps with these local staged/canonical Pulgar-line candidates.
- Existing identity-analysis notes preserve `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, and `Dario Pulgar A.` as candidates requiring careful bridge review.

Conflicts and limits:

- The assigned conflict draft and converted notice do not state `Jose`, `J.`, `A.`, medical/surgeon occupation, passenger-list age, ICRC context, or Geneva/France travel context.
- For passenger-list `Dario Pulgar A.` age 39 in 1928, a 2000 event would imply about age 111 if the same person, a severe chronology caution without vital-date proof.
- The ICRC group-photo `Dario Jose Pulgar-Arriagada` evidence is metadata/title dependent and not visibly identified in the converted image region.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | Name-pattern overlap exists, but no bridge marker appears in this notice. |
| conflict_severity | 0.70 | Duplicate-person and chronology risks are substantial. |
| evidence_quality | 0.46 | Compared evidence is staged, single-source, or QA-sensitive. |
| conversion_confidence | 0.62 | Mixed across the compared Pulgar-Arriagada materials. |
| claim_probability | 0.20 | Possible only as an unresolved hypothesis. |
| relevance | 0.82 | Required by the Pulgar-line guardrail. |
| canonical_readiness | 0.06 | No merge or name normalization should occur. |

## Hypothesis 6: Relationship To Jose/Juana Parent Candidates

Hypothesis: the notice-body `Darío Pulgar Arriagada` may connect genealogically to Jose/Juana parent candidates in the existing Pulgar-line context.

Evidence supporting:

- Existing wiki context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- `Jose del Carmen Segundo Pulgar Arriagada` shares the `Pulgar Arriagada` surname pattern.

Conflicts and limits:

- The assigned notice does not mention Jose, Juana, parentage, spouse, child, sibling, household, or lineage.
- Existing Jose/Juana materials include draft/probable relationships and conversion-sensitive readings.
- The source-metadata region conflict does not create a relationship conflict or a relationship bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | This is lineage-context only, not same-person evidence. |
| conflict_severity | 0.36 | Risk is unsupported family-link promotion from surname overlap. |
| evidence_quality | 0.34 | Jose/Juana evidence is local but not connected to this notice. |
| conversion_confidence | 0.50 | Mixed across referenced parent-candidate materials. |
| claim_probability | 0.05 | No relationship is stated in the assigned source. |
| relevance | 0.58 | Useful only as an anti-conflation check. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person conflict: none directly created by the region-title/body mismatch. The notice body supports only the narrow `Darío Pulgar Arriagada` legal-notice cluster pending reread.
- Duplicate-person risk: low for alignment with the existing `Darío Pulgar Arriagada` stub that already reflects this source; high if merged with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario Pulgar A.` by name alone.
- Name-variant conflict: this source supports `Darío Pulgar Arriagada` only. It does not prove `Arturo`, `Smith`, `Jose`, `J.`, or `A.` variants.
- Relationship conflict: none stated. Co-occurrence with Luis Abarzúa Ceballos and the presence of Pulgar/Juana/Jose family context elsewhere do not support kinship.
- Chronology conflict: none inside the assigned conflict draft; chronology becomes a serious anti-conflation check only if someone tries to merge this 2000/2001 notice with much earlier medical, passenger, or ICRC candidates.
- Source metadata conflict: high enough to block promotion until page/PDF reread confirms whether the title/header, source path, body text, or metadata should control citation.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Body text is a Bío Bío/Chiguayante notice despite Valparaíso title/path/header | 0.78 | Reread the page/PDF and reconcile source metadata against visible body text. |
| 2 | Named person aligns only with existing `Darío Pulgar Arriagada` expropriation-notice cluster | 0.84 | After reread, promote only the narrow apparent-domain/legal-notice claim if confirmed. |
| 3 | Valparaíso title/header is authoritative and body indicates a misfiled/mixed notice | 0.32 | Page/PDF reread plus source-manifest audit; do not infer person facts from title alone. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` or other Pulgar-Arriagada clusters | 0.20 | Require proof-reviewed bridge evidence with date, occupation, relationship, property, or vital data. |
| 5 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.12 | Require an explicit source linking `Pulgar Arriagada` with `Arturo` or `Pulgar-Smith`. |
| 6 | Connected to Jose/Juana parent candidates | 0.05 | No action from this notice; revisit only if a reviewed lineage source names the connection. |

## Recommended Next Action

Hold this staged conflict as a conversion/source-identity QA note. The exact next proof-review step is a targeted reread of `CHUNK-a2273412e7b1-P0001-01` and the underlying PDF/page image to verify:

- whether the visible header/title really says `V Región de Valparaíso`;
- whether the body really says `Serviu Región del Bío Bío`, `Chiguayante`, and `Director Serviu Región del Bío Bío`;
- whether the body name reads `Darío Pulgar Arriagada`, with accent and line break as converted;
- whether the source citation should preserve the title/path mismatch or be corrected through the normal conversion-QA workflow.

If reread confirms the current text, the promotion path should be narrow: keep the source-metadata caution attached, promote only a claim that `Darío Pulgar Arriagada` was named as apparent domain holder in the 2000-12-05 Chiguayante expropriation notice, and do not promote any same-person merge or family relationship.
