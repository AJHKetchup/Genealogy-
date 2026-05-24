---
type: identity_conflict_analysis
status: draft
worker: postconv-identity-analysis-20260524203442007
task_id: identity-analysis:research/_staging/conflicts/chunk-8a2aa5e638cf-p0001-01-no-material-conflict.md
role: identity_researcher
staged_draft: research/_staging/conflicts/chunk-8a2aa5e638cf-p0001-01-no-material-conflict.md
source_packet: research/_staging/source-packets/chunk-8a2aa5e638cf-p0001-01-cv-dario-arturo-pulgar-work-history.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
referenced_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0001-chunk-01.md
observed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
promotion_recommendation: hold_for_traceability_and_identity_bridge
---

# Identity/Conflict Analysis: CV Page 4 Work-History No-Material-Conflict Draft

## Blockers First

- The exact staged draft under review is `research/_staging/conflicts/chunk-8a2aa5e638cf-p0001-01-no-material-conflict.md`.
- Traceability is blocked: the staged draft and source packet cite `CHUNK-8a2aa5e638cf-P0001-01`, `converted page 1; CV page 4`, and `page-0001-chunk-01.md`, but that chunk path is not present. The current chunk manifest for the same converted file contains `CHUNK-2ff9cc4cddcb-P0004-01` at `page-0004-chunk-01.md`.
- The source packet uses document-level subject attribution to `Dario Arturo Pulgar`; the page 4 body itself does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar A.`, Jose/Juana parent candidates, or any family relationship.
- The converted page reports complete transcription and no illegible text, but the page metadata also records a proof-review hold about missing rendered page image review before canonical promotion.
- The canonical `wiki/people/dario-arturo-pulgar-smith.md` page is family-supplied and explicitly warns against automatic Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith merges without identity review. This draft does not provide that identity bridge.

## Literal Source Readings

- The converted page 4 text lists a `2000` entry for `International Bank for Reconstruction and Development (IBRD)`, location `Bolivia, Peru`, role `Senior Consultant`.
- The IBRD paragraph describes preparation of project appraisal/concept documents for Peru and Bolivia projects, including an IBRD/GEF-funded PROFONANPE second phase.
- The same page lists a `1999 - 2000` entry for `Antamina Mining Company`, location `Huarmey, Peru`, role `Head Community Relations`.
- The Antamina paragraph describes community-relations planning, work for communities affected by port-facility construction, evacuation supervision during blasts, and representation with local authorities and community organizations.

## Hypotheses Ranked

| Rank | Hypothesis | Evidence Supporting | Evidence Against / Limits | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | Page 4 belongs to the document-level CV subject `Dario Arturo Pulgar`. | Source title/path, converted-file title, and source packet identify the document as `CV of Dario Arturo Pulgar`; page content fits a continuing CV work-history page. | Page body is unnamed; staged chunk/hash/path references are stale or mismatched. | 0.72 |
| 2 | The document-level `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`. | Strong name overlap on `Dario Arturo Pulgar`; canonical page provides a family-supplied fuller Pulgar-Smith identity. | No `Smith`, birth data, family relationship, signature, residence bridge, or reviewed same-person proof appears on this page. | 0.46 |
| 3 | The CV subject is the same person as other staged Habitat/passenger/work-history `Dario Pulgar` clusters. | Pulgar name overlap and local CV/Habitat career context make comparison relevant. | This page supplies no age, travel, family, or direct cross-source bridge. | 0.35 |
| 4 | The CV subject is the same person as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`. | Shared `Dario` and `Pulgar` elements only. | No `Jose`, `J.`, `Arriagada`, medical-title, Geneva/delegate, parentage, or chronology bridge appears here. | 0.10 |
| 5 | The page directly connects the CV subject to Jose/Juana parent candidates such as `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar`. | None in the assigned draft. | No birth registration, father, mother, spouse, child, household, or lineage statement appears on the page. | 0.03 |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`; this page alone does not prove or disprove the match.
- Duplicate-person risk: moderate for `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`; high if merged by name alone with Pulgar-Arriagada, passenger Dario Pulgar, or Jose/Juana parent-candidate clusters.
- Name-variant conflict: unresolved. The page does not support treating `Pulgar`, `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.` as variants of one person.
- Relationship conflict: none found. The page states no parent, spouse, child, grandchild, or relationship to Alexander John Heinz.
- Chronology conflict: none material from this page. The 1999-2000 Antamina and 2000 IBRD entries overlap in year but are not stated as mutually exclusive.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Probable document-level attribution to `Dario Arturo Pulgar`; no page-local name and chunk metadata drift weaken the identity case. |
| conflict_severity | 0.20 | No direct genealogical conflict appears; the main risk is downstream identity conflation. |
| evidence_quality | 0.66 | Typed CV work-history text is specific, but self-reported/derivative and currently has traceability drift. |
| conversion_confidence | 0.70 | Transcript reports complete/no illegible text, but page-image review and chunk reconciliation remain blockers. |
| claim_probability | 0.78 | The narrow claim that the CV reports these work-history entries is likely; canonical attachment is not. |
| relevance | 0.45 | Biographical career context only; no vital, relationship, or lineage evidence. |
| canonical_readiness | 0.25 | Hold until chunk metadata/path drift and identity bridge are proof-reviewed. |

## Recommended Next Action

Reconcile the staged `CHUNK-8a2aa5e638cf-P0001-01` / `page-0001-chunk-01.md` references with the current `CHUNK-2ff9cc4cddcb-P0004-01` / `page-0004-chunk-01.md` chunk manifest. Then run targeted proof review of an identity-bearing CV title/front/contact/signature page or another reviewed local bridge that explicitly connects document-level `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`. Do not promote page 4 work-history facts, merge people, rename pages, or use Pulgar-Arriagada or Jose/Juana parent candidates as bridge evidence from this draft alone.
