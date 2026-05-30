---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530231621335
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This note analyzes the exact staged conflict draft `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md`.

## Blockers First

1. Page control is blocked. The assigned chunk says page 5 begins with `1979 - 1982` United Nations Centre for Human Settlements (HABITAT), Nairobi, while the conversion-job `page-markdown/page-0005.md` says page 5 begins with `1999` National Trust Fund for Protected Areas in Peru (PROFONANPE), Peru.
2. The source packet reports conversion/provenance instability: the converted SHA-256 recorded in the chunk differs from the observed converted SHA-256, and the chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting counts and hashes.
3. The source packet states `page-images/page-0005.jpg` is absent. The staged draft correctly treats the physical page-5 transcription as unresolved.
4. The page body reviewed here does not independently name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, any Jose/Juana parent candidate, spouse, child, grandchild, or Alexander John Heinz.
5. No same-person merge, duplicate-person cleanup, canonical page rename, family relationship, or work-history promotion is ready from this draft.

## Literal Source Readings

- Staged conflict draft: names subject `Dario Arturo Pulgar` in metadata and describes a page-control conflict between assigned chunk text and competing page Markdown.
- Source packet: identifies source title/path as `CV of Dario Arturo Pulgar`; states page control is disputed and recommends `hold_for_conversion_qa`.
- Assigned chunk literal reading: typed CV work-history sequence for `1979 - 1982` HABITAT in Nairobi; `1974 - 1978` National Film Board of Canada in Montreal; `1972 - 1973` Chile Films in Santiago; `1970 - 1972` CITELCO in Santiago; then `EDUCATION`.
- Competing page Markdown literal reading: typed CV work-history sequence for `1999` PROFONANPE in Peru and Television Trust for the Environment in London, followed by `1998 - 1999` Arca Consulting/European Commission in Lesotho, `1997-1998` Klohn Crippen in Huaraz, Peru, and SNC Lavalin Agriculture in Maracaibo, Venezuela.
- Canonical wiki context: `wiki/people/dario-arturo-pulgar-smith.md` is family supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to attach Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review.

## Interpretation Kept Separate

The local evidence supports a real derivative-text conflict for page 5 of a document locally titled `CV of Dario Arturo Pulgar`. It does not support choosing either work-history sequence as the controlling physical page 5. It also does not bridge document-level `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith` or to any Pulgar-Arriagada/Jose/Juana cluster.

## Hypotheses And Scores

| Rank | Hypothesis | Evidence supporting | Evidence against / conflict | identity_confidence | conflict_severity | evidence_quality | conversion_confidence | claim_probability | relevance | canonical_readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | This staged draft is a valid page-control/provenance conflict and should remain held. | The assigned chunk and page Markdown materially disagree; source packet records hash drift, duplicate manifest entries, and missing page image. | None material; the conflict is directly documented by local artifacts. | 0.86 | 0.92 | 0.72 | 0.18 | 0.90 | 0.95 | 0.02 |
| 2 | Page 5 controls the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence. | Assigned chunk and source packet quote this sequence; chunk text is internally coherent CV text. | Competing page Markdown gives a different page-5 sequence; physical page image is absent; metadata is unstable. | 0.45 | 0.88 | 0.55 | 0.18 | 0.38 | 0.85 | 0.02 |
| 3 | Page 5 controls the 1999-1997 PROFONANPE/TVE/Arca/Klohn/SNC Lavalin sequence. | Conversion-job page Markdown names this as page 5 and gives coherent CV text. | Assigned chunk and packet for this task quote the older 1979-1970 sequence; manifest/hash drift is unresolved. | 0.43 | 0.88 | 0.55 | 0.18 | 0.36 | 0.85 | 0.02 |
| 4 | The disputed page belongs at document level to the `Dario Arturo Pulgar` CV cluster. | Source title/path, source packet metadata, and converted-file context identify `CV of Dario Arturo Pulgar`. | Page body does not repeat the subject name; page-control and provenance are blocked. | 0.50 | 0.70 | 0.48 | 0.18 | 0.50 | 0.90 | 0.03 |
| 5 | Document-level `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`. | Strong name overlap with the family-supplied canonical anchor. | No `Smith`, `Pulgar-Smith`, grandchild, parent, spouse, vital data, or relationship bridge appears in this page-control draft. Canonical page requires identity review before attachment. | 0.34 | 0.82 | 0.35 | 0.18 | 0.28 | 0.92 | 0.01 |
| 6 | This draft supports the same person as `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`. | Required Pulgar-line comparison; broad `Dario` and `Pulgar` overlap exists in local wiki/staging context. | This draft does not say `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, medical title, property/expropriation context, parents, or older public-role context. | 0.08 | 0.80 | 0.28 | 0.18 | 0.05 | 0.70 | 0.00 |
| 7 | This draft supports Jose/Juana parent-candidate relationships. | Local Pulgar-line wiki context includes `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`. | The staged draft and both competing page-5 texts name no Jose/Juana parent, no child, no birth entry, and no relationship. | 0.02 | 0.70 | 0.18 | 0.18 | 0.01 | 0.45 | 0.00 |

## Pulgar-Line Anti-Conflation Check

| Candidate | Current evidence from this draft and existing wiki context | Disposition |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Existing canonical page is family supplied as Alexander John Heinz's maternal grandfather. This draft supplies only document-level `Dario Arturo Pulgar` CV context and no `Smith` or relationship bridge. | Do not merge or attach. Exact next step: identity-bridge proof review using an identity-bearing CV page or other reviewed source that explicitly connects `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`. |
| `Dario Arturo Pulgar` | Source title/path and packet identify the CV subject, but page 5 body is not identity-bearing and page control is disputed. | Preserve as provisional document-level CV subject only. Exact next step: conversion QA must select the controlling page-5 transcription before any work-history claim review. |
| `Dario Jose Pulgar-Arriagada` | No `Jose`, `J.`, medical/service title, Geneva/convention context, parentage, or Arriagada surname appears in the assigned draft. | Same-person probability low. Exact next step: compare only after separate proof-reviewed identity-bearing Pulgar-Arriagada materials are assembled. |
| `Dario/Dario Pulgar Arriagada` | Canonical `Darío Pulgar Arriagada` has a separate 2000 expropriation evidence snapshot; this page-control draft has no property, expropriation, Arriagada, or date bridge. | Keep separate. Exact next step: no comparison until page-control QA and a later identity bridge supply direct identifiers. |
| Jose/Juana parent candidates | Existing wiki has `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` from separate birth-register staging. This CV page-control draft names no parents or children. | No relationship inference. Exact next step: none from this draft; use only separate proof-reviewed birth/lineage packets for Jose/Juana relationships. |

## Conflict Findings

- Same-person conflict: unresolved for document-level `Dario Arturo Pulgar` versus canonical `Dario Arturo Pulgar-Smith`; this draft is not enough to decide.
- Duplicate-person risk: high if the CV subject is merged into Pulgar-Smith, Pulgar-Arriagada, Dario Jose, Darío Pulgar Arriagada, passenger, property, or Jose/Juana clusters by name alone.
- Name-variant conflict: this draft supports only provisional document-level `Dario Arturo Pulgar`; it does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.` as variants.
- Relationship-conflict evidence: none. No parent, spouse, child, grandchild, or maternal-grandfather relationship appears in the page text.
- Chronology conflict: material for work history only. The competing page-5 transcriptions produce mutually incompatible CV chronology segments, so no page-5 work-history fact should be promoted.

## Recommended Next Action

Keep this staged draft on `hold_for_conversion_qa`. Restore or locate the original PDF/page image for page 5, reconcile the duplicate manifest entries and hash drift, and certify whether the controlling physical page 5 is the 1979-1970 sequence or the 1999-1997 sequence.

After page control is fixed, run claim proof review only for the certified page text. Separately, run an identity-bridge proof review before attaching any CV work-history evidence to `Dario Arturo Pulgar-Smith` or comparing the CV subject to `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or Jose/Juana parent candidates.
