---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260524121054587
task_id: identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-a485f4030ce7-P0009-01-no-internal-conflict.md
staged_draft: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-a485f4030ce7-P0009-01-no-internal-conflict.md
source_packet: research/_staging/source-packets/chunk-a485f4030ce7-p0009-01-cv-dario-arturo-pulgar-education-languages.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0009-chunk-01.md
assigned_chunk_id: CHUNK-a485f4030ce7-P0009-01
referenced_chunk_frontmatter_id: CHUNK-c25ee050e822-P0009-01
page_reference: page 9
analysis_status: hold
canonical_readiness: hold_for_identity_bridge_and_metadata_audit
---

# Identity/Conflict Analysis: CV Page 9 Education And Languages

## Blockers

- Exact staged draft reviewed: `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-a485f4030ce7-P0009-01-no-internal-conflict.md`.
- Page 9 does not literally name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, Jose, Juana, or any parent, spouse, child, grandchild, household, birth, death, or relationship.
- Subject attribution is document-level only, from the source title/path and staging metadata for `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- Metadata needs audit before promotion: the staged draft/source packet use `CHUNK-a485f4030ce7-P0009-01` and `converted_sha256: a485f4030ce7...`, while the referenced chunk file and manifest currently show `CHUNK-c25ee050e822-P0009-01` and `converted_sha256: c25ee050e822...`.
- The source packet says the page image is now present and visually matched, but also preserves a controller missing-image/reread concern. Proof review should explicitly accept or reject that QA reconciliation.
- Do not merge people, rename canonical pages, or attach page-9 facts to a canonical person from this evidence alone.

## Literal Source Readings

- `1967 - 1968`: Stanford University, Stanford, California; Fulbright Scholarship; M.A. Communications.
- `1963 - 1966`: Universidad de Concepcion, Escuela de Periodismo, Chile; Journalism.
- `1960 - 1963`: Universidad de Concepcion, Escuela de Derecho, Chile; field of study Law.
- `1954 - 1959`: Liceo Enrique Molina, Concepcion, Chile; Humanities, Baccalaureate.
- Spoken languages: Spanish, English, French, Italian, and Portuguese.
- Written languages: Spanish, English, and French.

Interpretation kept separate: these entries are likely part of a CV locally titled for `Dario Arturo Pulgar`, but the page body itself is not identity-bearing.

## Hypothesis 1: No Internal Page-9 Conflict

Hypothesis: the staged conflict draft is correct that page 9 contains no internal identity, relationship, chronology, or place conflict.

Supporting evidence:

- The page contains a coherent education sequence from 1954 through 1968 followed by language lists.
- The page names no second person and states no competing identity, surname variant, kinship, place, or date assertion.
- The source packet and current chunk agree on the substantive page-9 text.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | The page belongs to a titled CV context, but the page body is unnamed. |
| conflict_severity | 0.10 | No internal contradiction; the main risk is over-attribution. |
| evidence_quality | 0.72 | Typed text and local page-image QA are useful; identity is contextual. |
| conversion_confidence | 0.90 | The chunk reports complete clear text; procedural QA remains open. |
| claim_probability | 0.88 | High probability that page 9 itself has no internal conflict. |
| relevance | 0.98 | Directly addresses the assigned conflict draft. |
| canonical_readiness | hold | Hold for metadata and identity-bridge review. |

## Hypothesis 2: Page 9 Belongs To Document-Level Dario Arturo Pulgar

Hypothesis: the page belongs to the CV source identified locally as `CV of Dario Arturo Pulgar`, so the education and language entries are attributable to the document-level CV subject `Dario Arturo Pulgar`.

Supporting evidence:

- The source path, converted file title, staged draft, and source packet all identify the source as `CV of Dario Arturo Pulgar.pdf`.
- The converted file covers CV pages 4-9; page 8 ends with the `EDUCATION` heading and page 9 continues with education and languages.
- The source packet states that the identity is from the source title/file identity rather than the page-body text.

Conflicts and limits:

- Page 9 itself does not repeat the subject name.
- The `a485f4030ce7` versus `c25ee050e822` identifier mismatch reduces canonical readiness.
- This hypothesis does not prove any family relationship or canonical person match.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.80 | Strong document-context attribution; no standalone page-body identity proof. |
| conflict_severity | 0.25 | No contradiction, but attribution and metadata risks remain. |
| evidence_quality | 0.70 | Multiple local artifacts point to the same source title. |
| conversion_confidence | 0.88 | Clear typed content with local QA note; proof-review acceptance still needed. |
| claim_probability | 0.82 | Probable that page 9 belongs to the Dario Arturo Pulgar CV. |
| relevance | 0.96 | Direct document-context evidence for the assigned page. |
| canonical_readiness | hold_for_identity_bridge_and_metadata_audit | Needs chunk/hash audit and identity-bearing review. |

## Hypothesis 3: Same Person As Canonical Dario Arturo Pulgar-Smith

Hypothesis: the CV subject `Dario Arturo Pulgar` is the same person as canonical `wiki/people/dario-arturo-pulgar-smith.md`, with the CV using a shortened surname form.

Supporting evidence:

- The canonical page gives the family-supplied preferred name `Dario Arturo Pulgar-Smith`.
- The CV document-level name shares `Dario Arturo Pulgar`.
- The canonical page explicitly warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records should be attached only after identity review, so this is a valid hypothesis to test.

Conflicts and limits:

- Page 9 does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, grandchild relationship, parents, spouse, child, birth, or death.
- The canonical page is family-supplied and is not itself a proof-reviewed bridge for this CV page.
- Name overlap justifies a double-check, not a silent merge or fact promotion.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Plausible candidate because of shared name elements, but unproved by this page. |
| conflict_severity | 0.45 | Moderate risk if education/language claims are attached without a bridge. |
| evidence_quality | 0.44 | Family-supplied context plus document title; no direct bridge. |
| conversion_confidence | 0.88 | Conversion quality does not solve the identity gap. |
| claim_probability | 0.55 | Possible same person; not established here. |
| relevance | 0.84 | Main canonical candidate in existing wiki context. |
| canonical_readiness | not_ready | Requires reviewed bridge from `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`. |

## Hypothesis 4: Same Person As Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada / Dario Pulgar A.

Hypothesis: the CV subject is the same person as one of the Pulgar-Arriagada or abbreviated Dario Pulgar candidates in staged or canonical context.

Supporting evidence:

- Existing local context includes records or staged notes for `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar A.`, and canonical `Darío Pulgar Arriagada`.
- These names share `Dario` and `Pulgar`, making them required comparison candidates for Pulgar-line identity review.

Conflicts and limits:

- Page 9 contains none of `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, `Dr`, medical/health-service titles, Geneva photograph context, passenger-list context, property context, or expropriation context.
- The page-9 education chronology does not connect the CV subject to older medical/delegate/passenger/property clusters.
- Merging these candidates by name alone risks conflating separate people, generations, occupations, and source clusters.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Broad name-family overlap only. |
| conflict_severity | 0.72 | High risk of duplicate-person or chronology conflict if merged prematurely. |
| evidence_quality | 0.24 | Comparison context exists, but page 9 contributes no bridge. |
| conversion_confidence | 0.88 | The page is readable, but lacks variant-name evidence. |
| claim_probability | 0.10 | Unsupported from this staged draft. |
| relevance | 0.60 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | not_ready | Preserve separately until explicit full-name/date/profession/residence or family continuity is reviewed. |

## Hypothesis 5: Jose/Juana Parent Candidates Connect This Page To A Pulgar Line

Hypothesis: Jose or Juana parent candidates in local Pulgar-line context connect the page-9 CV subject to a family lineage.

Supporting evidence:

- Existing canonical pages include `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Those pages are relevant Pulgar-line comparison points for future relationship review.

Conflicts and limits:

- Page 9 names no Jose, Juana, parent, child, spouse, sibling, household, or birth-registration fact.
- Existing Jose/Juana records concern other staged sources; this page does not connect to them.
- Family-context hints justify a targeted double-check only. They cannot correct or extend the CV identity silently.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | No page-9 parent/child evidence. |
| conflict_severity | 0.60 | Relationship-overreach risk if lineage is inferred. |
| evidence_quality | 0.18 | Local context exists but is not evidence from this page. |
| conversion_confidence | 0.88 | Conversion is not the limiting issue. |
| claim_probability | 0.03 | Unsupported by the staged draft and page text. |
| relevance | 0.44 | Required comparison context, not direct evidence. |
| canonical_readiness | not_ready | Needs direct relationship evidence, not this CV continuation page. |

## Ranked Judgment

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Page 9 has no internal conflict | 0.88 | Proof review should accept page-image QA and resolve metadata before any promotion. |
| 2 | Page 9 belongs to document-level CV subject `Dario Arturo Pulgar` | 0.82 | Audit `CHUNK-a485f4030ce7` versus `CHUNK-c25ee050e822`, then review an identity-bearing CV page/title/front matter. |
| 3 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.55 | Require a reviewed local bridge explicitly connecting `Dario Arturo Pulgar` to `Pulgar-Smith`. |
| 4 | Same person as `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or `Dario Pulgar A.` | 0.10 | Preserve as separate or unresolved hypotheses; require explicit continuity evidence. |
| 5 | Connected to Jose/Juana parent candidates | 0.03 | Require direct relationship evidence naming the relevant parent/child connection. |

## Conflict Summary

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`; high if merged by name alone with Pulgar-Arriagada, Dario Jose, Dario Pulgar A., or Jose/Juana family candidates.
- Name-variant conflict: page 9 supports no variant beyond the document-level source title `Dario Arturo Pulgar`.
- Relationship conflict: none in page 9; any parent, grandchild, or family relationship would be unsupported from this page.
- Chronology conflict: none inside the page-9 education sequence. Chronology risk arises only if the page is merged into older medical/delegate/passenger/person clusters without identity proof.

## Recommended Next Action

Keep `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-a485f4030ce7-P0009-01-no-internal-conflict.md` on hold and do not promote, merge, rename, or attach its education/language facts to a canonical person yet.

The exact next proof-review step is a targeted metadata and CV-identity audit: reconcile the assigned staged identifiers (`CHUNK-a485f4030ce7-P0009-01`, source-packet `converted_sha256: a485f4030ce7...`) with the current chunk manifest (`CHUNK-c25ee050e822-P0009-01`, `converted_sha256: c25ee050e822...`), accept or reject the local page-image QA reconciliation, and then review an identity-bearing CV page or other accepted local source that explicitly connects document-level `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`. Until that bridge is accepted, preserve `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Dario Pulgar A.`, and Jose/Juana parent candidates as separate hypotheses.
