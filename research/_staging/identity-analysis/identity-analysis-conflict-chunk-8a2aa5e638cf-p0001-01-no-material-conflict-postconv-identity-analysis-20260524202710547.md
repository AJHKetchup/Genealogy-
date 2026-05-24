---
type: identity_conflict_analysis
status: draft
worker: postconv-identity-analysis-20260524202710547
task_id: identity-analysis:research/_staging/conflicts/chunk-8a2aa5e638cf-p0001-01-no-material-conflict.md
role: identity_researcher
staged_draft: research/_staging/conflicts/chunk-8a2aa5e638cf-p0001-01-no-material-conflict.md
source_packet: research/_staging/source-packets/chunk-8a2aa5e638cf-p0001-01-cv-dario-arturo-pulgar-work-history.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
referenced_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0001-chunk-01.md
current_chunk_observed: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
promotion_recommendation: hold_for_metadata_reconciliation_and_identity_bridge
---

# Identity/Conflict Analysis: CV Page 4 Work-History No-Material-Conflict Draft

## Blockers First

- The staged draft and source packet reference `CHUNK-8a2aa5e638cf-P0001-01`, `converted page 1; CV page 4`, and `page-0001-chunk-01.md`. The currently available chunk directory for the cited converted file contains `page-0004-chunk-01.md`, whose front matter identifies `CHUNK-2ff9cc4cddcb-P0004-01`; no `page-0001-chunk-01.md` was present at the referenced path during this review.
- The source packet records `converted_sha256: 8a2aa5e638cf...`, while the current chunk manifest for the same converted file records `converted_sha256: 2ff9cc4cddcb...`. This traceability drift must be reconciled before any canonical promotion.
- Page 4 itself does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar A.`, Jose/Juana parent candidates, spouse, child, or other family relationship terms. Subject attribution is document-level context from the CV title/path and surrounding conversion, not page-local identity evidence.
- Existing canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to merge similarly named Dario/Pulgar clusters without identity review. This page 4 draft does not supply the missing bridge.

## Literal Source Readings

- The converted page 4 text lists a `2000` entry for `International Bank for Reconstruction and Development (IBRD)`, places `Bolivia, Peru`, and role `Senior Consultant`.
- The same page lists work on Project Appraisal/Concept documents for Indigenous Management of Protected Areas in Peru, a Learning and Innovation Loan in Bolivia, and a second-phase IBRD/GEF project for PROFONANPE.
- The page lists a `1999 - 2000` entry for `Antamina Mining Company`, place `Huarmey, Peru`, and role `Head Community Relations`.
- The Antamina paragraph describes planning and supervising community relations, activities for communities affected by port-facility construction, evacuation supervision during blasts, and representation with local authorities and community organizations.
- The page's conversion says there are no uncertain or illegible words and that the page is fully transcribed, but the page metadata also records proof-review concern that a rendered page image had been missing and should be restored/generated before canonical promotion.

## Hypotheses Ranked

| Rank | Hypothesis | Evidence For | Evidence Against / Limits | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | The work-history entries belong to the document-level CV subject named `Dario Arturo Pulgar`. | Source title/path and converted-file title are `CV of Dario Arturo Pulgar`; source packet identifies the page as continuing his CV work history. | Page body is unnamed; the staged chunk id/path is stale or mismatched against current chunk files. | 0.72 |
| 2 | The document-level `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`. | Name overlap on `Dario Arturo Pulgar`; canonical page gives a family-supplied person with that fuller name. | Page 4 does not include `Smith`, family context, dates of birth, relatives, residence sufficient for identity, or any proof-reviewed bridge to the canonical page. | 0.46 |
| 3 | The page 4 CV subject is the same person as a source cluster named `Dario Pulgar` in Habitat/passenger/work-history context. | Occupational and geographic themes may fit a broader Dario Pulgar career cluster, but this page alone does not name those other contexts. | Name form and identity bridge are not page-local; no age, birth, spouse, child, or travel details here. | 0.35 |
| 4 | The page 4 CV subject is the same person as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` / `Dario Pulgar-Arriagada`. | Shared first name and paternal surname only. | The Pulgar-Arriagada records concern medical, Chile delegate, Geneva, and earlier-life contexts; this CV page gives no `Jose`, `J.`, `Arriagada`, medical-service title, or chronology bridge. | 0.10 |
| 5 | The page 4 CV subject is directly tied to Jose/Juana parent candidates such as `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or `Juana de Dios ... de Pulgar`. | None from this page. | No parents, birth registration, household, or kinship evidence appears in the page 4 text. | 0.03 |

## Conflicts And Non-Conflicts

- Same-person conflict: no direct same-person conflict is created by the page 4 literal text. The only identity risk is over-attachment from document title to canonical Pulgar-Smith or to Pulgar-Arriagada/Jose/Juana clusters without a bridge.
- Duplicate-person conflict: not resolved. The existing canonical/stub landscape includes `Dario Arturo Pulgar-Smith`, `Darío Pulgar Arriagada`, adult/child passenger Dario Pulgar stubs, and Jose/Juana-related Pulgar pages. Page 4 provides no duplicate-resolution evidence.
- Name-variant conflict: not resolved. This page supports only document-level `Dario Arturo Pulgar`; it does not support treating `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.` as variants of the same person.
- Relationship conflict: none found on this page. It states no parent, spouse, child, grandchild, or relationship to Alexander John Heinz.
- Chronology conflict: no internal chronology conflict in the page 4 work-history entries was found. The 1999-2000 Antamina entry and 2000 IBRD entry may overlap, but the CV text does not present them as mutually exclusive.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Probable document-level attribution to `Dario Arturo Pulgar`, but page-local identity is absent and metadata drift weakens traceability. |
| conflict_severity | 0.20 | No material genealogical conflict appears in the literal page text; risk is mainly downstream identity conflation. |
| evidence_quality | 0.66 | Typed CV text is specific for work history, but it is derivative/self-reported CV evidence and currently has staging/chunk metadata drift. |
| conversion_confidence | 0.70 | The transcript says complete/no illegible text, but prior page-image QA concern and current hash/chunk mismatch require reconciliation. |
| claim_probability | 0.78 | The narrow claim that the CV reports these work-history entries is likely; canonical person attachment is less probable. |
| relevance | 0.45 | Medium family relevance as biographical career context only, not relationship or vital-record evidence. |
| canonical_readiness | 0.25 | Hold until chunk metadata and identity bridge are proof-reviewed. |

## Recommended Next Action

Reconcile the staged `CHUNK-8a2aa5e638cf-P0001-01` / `page-0001-chunk-01.md` references with the current `CHUNK-2ff9cc4cddcb-P0004-01` / `page-0004-chunk-01.md` chunk manifest for the same converted file. Then perform a targeted proof-review step on an identity-bearing CV title/front-matter page or other local bridge that explicitly connects document-level `Dario Arturo Pulgar` to canonical `wiki/people/dario-arturo-pulgar-smith.md`. Until that is complete, do not promote page 4 work-history facts to canonical people and do not merge this CV subject with Pulgar-Smith, Pulgar-Arriagada, passenger, or Jose/Juana parent-candidate clusters.
