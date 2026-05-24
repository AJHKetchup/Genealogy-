---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260524115620837
task_id: identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-a485f4030ce7-P0009-01-no-internal-conflict.md
staged_draft: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-a485f4030ce7-P0009-01-no-internal-conflict.md
source_packet: research/_staging/source-packets/chunk-a485f4030ce7-p0009-01-cv-dario-arturo-pulgar-education-languages.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0009-chunk-01.md
assigned_chunk_id: CHUNK-a485f4030ce7-P0009-01
referenced_chunk_frontmatter_id: CHUNK-c25ee050e822-P0009-01
conflict_type: identity_bridge_and_metadata_watch
canonical_readiness: hold_for_identity_bridge_and_metadata_audit
---

# Identity/Conflict Analysis: CV Page 9 Education And Languages

## Blockers

- The staged draft under review is `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-a485f4030ce7-P0009-01-no-internal-conflict.md`. It correctly finds no internal page-9 conflict, but canonical promotion is blocked because page 9 does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Pulgar-Arriagada`, `Dario Jose`, any Jose/Juana parent, or any family relationship.
- The strongest identity support is document-level context from the source title/path and staging metadata: `raw/sources/CV of Dario Arturo Pulgar.pdf`. That is not a same-person bridge to canonical `wiki/people/dario-arturo-pulgar-smith.md`.
- Metadata needs audit before promotion. The staged draft/source packet cite `CHUNK-a485f4030ce7-P0009-01`, but the referenced chunk file and chunk manifest identify page 9 as `CHUNK-c25ee050e822-P0009-01` with `converted_sha256: c25ee050e822d69b8942d42bf54c9d894d1cc674fc4bdde9c718befdc3239552`.
- The source packet reports a prior controller missing-image/reread concern. A local task says the page image is now present and visually matched, but proof review must accept that QA reconciliation before canonical use.
- Do not merge or rename any Pulgar-line people from this evidence. Page 9 supplies education/language chronology only; it supplies no parent, spouse, child, grandchild, household, birth, death, or surname-variant proof.

## Literal Source Readings

- Page 9 lists education entries: Stanford University, Stanford, California, Fulbright Scholarship, M.A. Communications, 1967-1968.
- Page 9 lists Universidad de Concepcion, Escuela de Periodismo, Chile, Journalism, 1963-1966.
- Page 9 lists Universidad de Concepcion, Escuela de Derecho, Chile, field of study Law, 1960-1963.
- Page 9 lists Liceo Enrique Molina, Concepcion, Chile, Humanities/Baccalaureate, 1954-1959.
- Page 9 lists spoken languages as Spanish, English, French, Italian, and Portuguese.
- Page 9 lists written languages as Spanish, English, and French.

Interpretation kept separate: these readings are likely part of a CV locally titled for `Dario Arturo Pulgar`, but the page body itself does not name the subject.

## Hypothesis 1: No Internal Page-9 Conflict

Hypothesis: the staged conflict draft is correct that page 9 contains no internal identity, relationship, chronology, or place conflict.

Supporting evidence:

- The page contains a coherent education chronology from 1954-1968 followed by language lists.
- No second person, parent, spouse, child, variant surname, or competing relationship appears in the page body.
- The source packet and chunk agree on the substantive literal page-9 content.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| conflict_severity | 0.10 | No contradiction inside page 9; risk is over-attribution rather than conflict in the text. |
| evidence_quality | 0.72 | Typed CV page and local page-image QA are useful, but identity is document-title dependent. |
| conversion_confidence | 0.90 | Chunk and source packet report clear complete text; prior image issue remains a proof-review procedural blocker. |
| claim_probability | 0.88 | High probability that the page itself has no internal conflict. |
| relevance | 0.96 | Directly relevant to the assigned staged conflict draft. |
| canonical_readiness | hold | Hold for metadata and identity-bridge review. |

## Hypothesis 2: Page 9 Belongs To Document-Level `Dario Arturo Pulgar`

Hypothesis: the page belongs to the local CV source identified as `CV of Dario Arturo Pulgar`, so the education and language entries are attributable to the document-level CV subject `Dario Arturo Pulgar`.

Supporting evidence:

- The source path, converted file title, staged draft, and source packet all identify the source as `CV of Dario Arturo Pulgar.pdf`.
- The converted file covers pages 4-9 of that CV and page 9 is the final education/languages continuation page.
- Prior local page-9 review for another staged chunk reached the same narrow result: document-level attribution is probable, while canonical attachment remains on hold.

Conflicts and limits:

- Page 9 itself is unnamed.
- The metadata mismatch between assigned `a485f4030ce7` and current chunk `c25ee050e822` reduces readiness.
- This hypothesis does not prove any family relationship or canonical person match.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Probable at document-context level; not standalone page-body identity proof. |
| conflict_severity | 0.25 | No contradiction, but metadata mismatch and unnamed page create moderate procedural risk. |
| evidence_quality | 0.70 | Multiple local artifacts point to the same source title; no independent identity-bearing statement on page 9. |
| conversion_confidence | 0.90 | Clear typed content with local QA note; proof-review acceptance still needed. |
| claim_probability | 0.80 | Probable that page 9 belongs to the Dario Arturo Pulgar CV. |
| relevance | 0.94 | Direct document-context evidence for the assigned CV page. |
| canonical_readiness | hold_for_identity_bridge_and_metadata_audit | Needs chunk/hash audit and identity-bearing review. |

## Hypothesis 3: Same Person As Canonical `Dario Arturo Pulgar-Smith`

Hypothesis: the CV subject `Dario Arturo Pulgar` is the same person as canonical `wiki/people/dario-arturo-pulgar-smith.md`, with the CV using a shortened name.

Supporting evidence:

- The canonical page gives the family-supplied preferred name `Dario Arturo Pulgar-Smith`.
- The CV document-level name shares the distinctive given names `Dario Arturo` and the `Pulgar` surname element.
- The canonical page explicitly marks Pulgar/Pulgar-Smith records as candidates for identity review, making this a relevant hypothesis to test.

Conflicts and limits:

- Page 9 does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, grandchild relationship, parents, spouse, child, birth, or death.
- The canonical page is family-supplied and warns against automatically attaching similarly named Pulgar records.
- A name overlap is not enough to merge identities or promote education/language facts to the canonical person.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Plausible candidate because of shared name elements, but unproved by this page. |
| conflict_severity | 0.45 | Moderate identity-overreach risk if promoted without a bridge. |
| evidence_quality | 0.44 | Family-supplied canonical context plus document-level CV title, but no direct bridge. |
| conversion_confidence | 0.90 | Conversion quality does not solve the identity gap. |
| claim_probability | 0.55 | Possible same person; not established. |
| relevance | 0.82 | Relevant canonical candidate, but not directly supported by page-body text. |
| canonical_readiness | not_ready | Requires a reviewed bridge from `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`. |

## Hypothesis 4: Same Person As `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, Or `Dario Pulgar A.`

Hypothesis: the CV subject is the same person as one of the Pulgar-Arriagada or abbreviated Dario Pulgar candidates in local staged/canonical context.

Supporting evidence:

- Existing local context includes staged records for `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, and `Dr Dario Pulgar A.`.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` exists as a separate stub with a 2000 legal-notice/expropriation event.
- These names share `Dario` and `Pulgar`, so they remain comparison candidates in Pulgar-line review.

Conflicts and limits:

- Page 9 says none of `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, `Dr`, or medical/health-service titles.
- The page-9 education chronology is not enough to connect the CV subject to older medical/delegate/passenger/property clusters.
- Merging the CV subject with Pulgar-Arriagada candidates by name alone risks conflating separate people across different professions and periods.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Name-family overlap only; no direct page-9 support. |
| conflict_severity | 0.70 | High risk of duplicate-person or chronology conflict if merged prematurely. |
| evidence_quality | 0.24 | Comparison context exists, but this page contributes no bridge. |
| conversion_confidence | 0.90 | The page is readable, but it lacks the needed variant-name evidence. |
| claim_probability | 0.12 | Unsupported from this page. |
| relevance | 0.55 | Relevant only as a required Pulgar-line comparison. |
| canonical_readiness | not_ready | Preserve separately until a source explicitly aligns full name, dates, occupation, residence, or family relationships. |

## Hypothesis 5: Jose/Juana Parent Candidates Connect This Page To A Pulgar Line

Hypothesis: Jose or Juana parent candidates in local Pulgar-line context connect the page-9 CV subject to a family lineage.

Supporting evidence:

- Local canonical pages include `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, `Jose del Carmen Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- These pages are relevant to Pulgar-line analysis and should remain visible as possible future comparison points.

Conflicts and limits:

- Page 9 names no Jose, Juana, parent, child, spouse, sibling, household, or birth-registration fact.
- Existing Jose/Juana pages concern other staged records; page 9 does not connect to them.
- Family-context hints justify a double-check only. They cannot silently correct or extend the CV subject identity.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | No page-9 parent/child evidence. |
| conflict_severity | 0.60 | Moderate-high relationship-overreach risk if lineage is inferred. |
| evidence_quality | 0.18 | Local context exists but is not evidence from this page. |
| conversion_confidence | 0.90 | Conversion is not the limiting issue. |
| claim_probability | 0.03 | Unsupported by the staged draft and page-9 text. |
| relevance | 0.42 | Required comparison due to Pulgar-line instruction, not direct evidence. |
| canonical_readiness | not_ready | Needs a direct relationship source, not this CV continuation page. |

## Ranked Judgment

| Rank | Hypothesis | Probability | Next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Page 9 has no internal conflict | 0.88 | Accept only after proof review confirms page-image QA and metadata reconciliation. |
| 2 | Page 9 belongs to document-level CV subject `Dario Arturo Pulgar` | 0.80 | Audit `CHUNK-a485f4030ce7` versus `CHUNK-c25ee050e822`, then review an identity-bearing CV page/title/front matter. |
| 3 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.55 | Require a reviewed bridge explicitly connecting `Dario Arturo Pulgar` to `Pulgar-Smith` before canonical attachment. |
| 4 | Same person as `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or `Dario Pulgar A.` | 0.12 | Preserve as separate hypotheses; require explicit full-name/date/profession/residence continuity. |
| 5 | Connected to Jose/Juana parent candidates | 0.03 | Require direct relationship evidence naming the relevant parent/child connection. |

## Conflict Summary

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`; high if merged by name alone with Pulgar-Arriagada, Dario Jose, Dario Pulgar A., or Jose/Juana family candidates.
- Name-variant conflict: page 9 supports no variant beyond the document-level source title `Dario Arturo Pulgar`.
- Relationship conflict: none in page 9; any parent/grandchild/family relationship would be unsupported from this page.
- Chronology conflict: none inside the page-9 education sequence. Chronology risk arises only if the page is merged into older medical/delegate/person clusters without identity proof.

## Recommended Next Action

Keep the staged conflict draft on hold, not promoted. The exact next step is a targeted proof-review/metadata audit that reconciles the assigned staged identifiers (`CHUNK-a485f4030ce7-P0009-01`, source-packet `converted_sha256: a485f4030ce7...`) with the current chunk manifest (`CHUNK-c25ee050e822-P0009-01`, `converted_sha256: c25ee050e822...`) and accepts or rejects the local page-image QA reconciliation.

After metadata is reconciled, review an identity-bearing CV page, title page, front matter, or other accepted local source that explicitly connects the document-level `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`. Until that bridge exists, preserve `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, and Jose/Juana parent candidates as separate hypotheses.
