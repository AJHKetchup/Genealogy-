---
type: identity_conflict_analysis
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-1940bcca99c5-P0001-01-no-direct-conflict.md"
worker: postconv-identity-analysis-20260523074444653
staged_draft: "research/_staging/conflicts/CONFLICT-STAGE-CHUNK-1940bcca99c5-P0001-01-no-direct-conflict.md"
source_path: "raw/sources/CV of Dario Arturo Pulgar.pdf"
source_packet: "research/_staging/source-packets/SP-STAGE-CHUNK-1940bcca99c5-P0001-01-cv-dario-pulgar-cv-page-4.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-1940bcca99c5-P0001-01"
page_reference: "assigned page 1; CV page 4"
analysis_status: hold_for_identity_and_page_mapping_review
canonical_readiness: hold
---

# Identity/Conflict Analysis: CONFLICT-STAGE-CHUNK-1940bcca99c5-P0001-01

## Blockers

- Exact staged conflict draft analyzed here: `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-1940bcca99c5-P0001-01-no-direct-conflict.md`.
- The staged draft correctly reports no direct internal chronology conflict between the `1999 - 2000` Antamina entry and the `2000` IBRD entry, but it does not resolve identity attribution.
- The page-body text does not literally name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, Jose, or Juana. Attribution to `Dario Arturo Pulgar` depends on the CV source title/path, converted-file title, staged source packet, and page continuity.
- The staged source packet and conflict draft cite chunk path `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0001-chunk-01.md`, but that file is not present in this workspace. The local chunk directory contains `page-0004-chunk-01.md`, so the assigned `P0001` versus CV page 4 mapping needs audit.
- The canonical page `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns against attaching similarly named Dario/Pulgar records without identity review. This staged conflict draft does not itself prove the `Pulgar` to `Pulgar-Smith` bridge.
- The source is a curriculum vitae. It can support self-reported occupational chronology after review, but it is not independent vital-event, parentage, or relationship evidence.
- No external research was performed. No raw source, converted Markdown, chunk, source packet, staged conflict draft, staged identity draft, or canonical wiki page was edited.

## Literal Source Reading

Literal local evidence from the staged conflict draft, source packet, and converted CV page:

- Source path: `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- Converted file title: `CV of Dario Arturo Pulgar pages 4-9`.
- Source packet display page: `CV page 4`; assigned chunk/page reference: `CHUNK-1940bcca99c5-P0001-01`, assigned page 1.
- The source packet states that the continuation page does not repeat the full name in the body text.
- The converted page 4 body records:
  - `2000`, `International Bank for Reconstruction and Development (IBRD)`, `Bolivia, Peru`, `Senior Consultant`.
  - `1999 - 2000`, `Antamina Mining Company`, `Huarmey, Peru`, `Head Community Relations`.
- The staged conflict draft notes minor transcription issues in surrounding text, including `Indian Sates` and `aassessing`, but no direct conflict from the occupational entries.

Interpretation kept separate: if the CV title and page-continuity evidence are accepted, the entries probably belong to the document-level subject `Dario Arturo Pulgar`. The page itself does not independently establish which canonical Dario Pulgar identity this represents.

## Hypothesis 1: No Direct Occupational Chronology Conflict Within This Chunk

Hypothesis: The `1999 - 2000` Antamina role and the `2000` IBRD role can coexist and do not create a direct internal conflict.

Supporting evidence:

- The staged conflict draft identifies the conflict type as `none_observed_in_chunk`.
- The Antamina entry covers `1999 - 2000`; the IBRD entry is dated `2000`.
- The page is a CV-style list of professional entries where adjacent or overlapping consulting periods are plausible without more precise dates.

Conflicts and limits:

- The draft does not provide month/day boundaries for either role.
- Absence of an internal conflict is not proof that every occupational claim is ready for canonical promotion.
- Page mapping and source-subject attribution remain unresolved.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.80 | The no-conflict finding depends mostly on page text, not personal identity. |
| conflict_severity | 0.10 | No direct chronology contradiction is visible in the assigned excerpt. |
| evidence_quality | 0.72 | Typed CV text is clear, but source-subject and chunk-path issues remain. |
| conversion_confidence | 0.76 | Reading is medium-high with minor transcription issues and page mapping uncertainty. |
| claim_probability | 0.86 | The stated occupational sequence can coexist on current evidence. |
| relevance | 1.00 | Directly answers the staged conflict draft. |
| canonical_readiness | 0.38 | Hold for page-mapping and identity proof review before promotion. |

## Hypothesis 2: Document-Level CV Subject Is Dario Arturo Pulgar

Hypothesis: The page belongs to the CV locally identified as `CV of Dario Arturo Pulgar`, so the page-4 occupational entries are attributable to the document-level subject `Dario Arturo Pulgar`.

Supporting evidence:

- The raw source path and converted file title both identify the source as a CV of Dario Arturo Pulgar.
- The staged source packet explicitly treats the page as occupational evidence for the CV subject, while noting the page-body name omission.
- The converted page body is consistent with a continuing curriculum vitae chronology.
- Existing staged identity analysis for the matching identity draft preserves the same document-level attribution as likely but held for proof review.

Conflicts and limits:

- The assigned page body does not literally name the person.
- The cited `page-0001-chunk-01.md` file is missing; the local chunk directory has a CV page-4 chunk under `page-0004-chunk-01.md`.
- The staged conflict draft's `do_not_promote` recommendation and the source packet's `promote_after_review` recommendation should be reconciled by proof review rather than silently resolved here.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.80 | Multiple local metadata layers agree, but the page body is unnamed. |
| conflict_severity | 0.28 | The risk is attribution and staging metadata, not an internal contradiction. |
| evidence_quality | 0.70 | Clear local source packet and conversion text, weakened by missing referenced chunk path. |
| conversion_confidence | 0.76 | Typed text is readable; page and chunk mapping still need audit. |
| claim_probability | 0.82 | Probable as document-level CV attribution. |
| relevance | 0.98 | Central to whether this no-conflict draft can support claims later. |
| canonical_readiness | 0.34 | Hold until identity-bearing CV context and page mapping are reviewed. |

## Hypothesis 3: Same Person As Canonical Dario Arturo Pulgar-Smith

Hypothesis: The CV subject `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`, with the CV using a shortened surname form.

Supporting evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` gives preferred name `Dario Arturo Pulgar-Smith`.
- The staged CV subject shares the distinctive `Dario Arturo Pulgar` name components.
- Family-supplied context places `Dario Arturo Pulgar-Smith` in the Pulgar-Smith line and makes this a relevant identity candidate to test.

Conflicts and limits:

- The staged conflict draft does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, a birth date, spouse, child, parent, residence, or any direct bridge to the canonical page.
- The canonical page is family-supplied and includes a warning not to attach similar Dario/Pulgar records without identity review.
- Family context justifies a double-check, not silently normalizing `Pulgar` to `Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.62 | Plausible name overlap, but no direct bridge in this chunk. |
| conflict_severity | 0.42 | Incorrect attachment would misattribute occupational chronology to the canonical person. |
| evidence_quality | 0.56 | Evidence is name overlap plus canonical context, not direct proof. |
| conversion_confidence | 0.76 | Conversion supports occupational text, not the surname-variant bridge. |
| claim_probability | 0.60 | Possible but unproved by this staged conflict draft. |
| relevance | 0.96 | Main canonical candidate to test before any promotion. |
| canonical_readiness | 0.20 | Not ready for merge, rename, or fact attachment. |

## Hypothesis 4: Same Person As The Broader CV/Habitat Dario Pulgar Work Cluster

Hypothesis: This page belongs to the same broader staged work-history cluster represented by other CV pages and Habitat-context `Dario Pulgar` references.

Supporting evidence:

- Adjacent staged CV materials identify pages 4-9 as part of the same `CV of Dario Arturo Pulgar`.
- Other local staged CV and Habitat analyses preserve a professional-development and communications work cluster for `Dario Pulgar` or `Dario Arturo Pulgar`.
- The page-4 IBRD and Antamina entries fit a later international development/community-relations career context.

Conflicts and limits:

- This page does not mention Habitat, Chile Films, Canada, exile, `Pulgar-Smith`, or family relationships.
- Cross-source cluster attachment still requires proof review; the present conflict draft is not the bridge by itself.
- Habitat passages may have their own page-boundary and identity-attribution holds.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.68 | Same-CV continuity is strong; cross-source Habitat linkage remains inferential. |
| conflict_severity | 0.34 | Low within the CV, moderate if over-used across sources. |
| evidence_quality | 0.60 | Useful staged context, but indirect for this conflict draft. |
| conversion_confidence | 0.72 | CV page text is usable with page-mapping audit. |
| claim_probability | 0.70 | Probable as a staged work-history cluster, not yet canonical. |
| relevance | 0.84 | Helpful for later identity-bridge review. |
| canonical_readiness | 0.18 | Hold pending CV identity proof review. |

## Hypothesis 5: Same Person As Dario Jose Pulgar-Arriagada / Dario or Dario Pulgar Arriagada

Hypothesis: The CV subject is the same person as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, or canonical `wiki/people/dar-o-pulgar-arriagada.md`.

Supporting evidence:

- The names share broad `Dario/Darío` and `Pulgar` elements.
- Existing local Pulgar-line context includes staged/title `Dario Jose Pulgar-Arriagada`, possible `Dario J. Pulgar Arriagada`, medical/passenger-list candidates, and a canonical `Darío Pulgar Arriagada` expropriation stub.

Conflicts and limits:

- This staged CV page names no `Jose`, no `J.`, no `Arriagada`, and no `Pulgar-Arriagada`.
- The page describes late-1990s/2000 international development and mining-community-relations roles, not medical, Geneva, passenger-list, or expropriation contexts.
- Existing Pulgar-Arriagada materials are held or context-specific and do not bridge to this CV page by name alone.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.14 | Only broad name overlap exists. |
| conflict_severity | 0.78 | A name-only merge could collapse distinct Pulgar generations and career clusters. |
| evidence_quality | 0.44 | Compared Arriagada evidence is separate, held, or metadata-dependent. |
| conversion_confidence | 0.58 | This CV page is readable, but comparison clusters have independent QA holds. |
| claim_probability | 0.12 | Low on current local evidence. |
| relevance | 0.86 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.03 | Do not attach or merge. |

## Hypothesis 6: Connected To Jose/Juana Parent Candidates

Hypothesis: Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, Juana de Dios Amagada de Pulgar, or related Jose/Juana candidates connect the CV subject to a Pulgar lineage.

Supporting evidence:

- Existing local wiki and staged records preserve Jose/Juana Pulgar and Pulgar-Arriagada candidates.
- Those records may be relevant to a future Pulgar-line proof argument.

Conflicts and limits:

- This staged conflict draft contains no Jose or Juana name.
- It states no parent, child, spouse, household, birth-register, or lineage relationship.
- Existing Jose/Juana materials contain conversion-sensitive name and relationship issues, so they cannot be used as a silent bridge to the CV subject.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.06 | No direct identity or kinship bridge appears on this page. |
| conflict_severity | 0.62 | Unsupported lineage attachment would create relationship conflicts. |
| evidence_quality | 0.36 | Parent-candidate evidence is separate and partly unresolved. |
| conversion_confidence | 0.48 | Related register evidence remains image-sensitive; this page does not address it. |
| claim_probability | 0.05 | No Jose/Juana connection is supported by the staged draft. |
| relevance | 0.62 | Relevant only as required Pulgar-line comparison context. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflicts

- Direct chronology conflict: none observed within this chunk. The `1999 - 2000` Antamina entry and `2000` IBRD entry can coexist without contradiction.
- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`; high if merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, passenger-list candidates, or Jose/Juana lineage candidates.
- Name-variant conflict: this staged evidence supports only document-level `Dario Arturo Pulgar`. It does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.` variants.
- Relationship-conflict evidence: none on this page. It does not state the maternal-grandfather relationship to Alexander John Heinz and does not name Jose/Juana parent candidates.
- Chronology-conflict evidence: none inside the page-4 1999-2000 occupational entries. Cross-cluster chronology and occupational context should still prevent name-only merging with older medical, passenger, ICRC, or expropriation clusters.
- Conversion/staging conflict: the converted page text is readable, but the cited staged chunk path is missing and should be reconciled with the existing `page-0004-chunk-01.md` and CV page-4 metadata before promotion.

## Ranked Hypotheses

| rank | hypothesis | probability | exact next proof-review or promotion step |
|---:|---|---:|---|
| 1 | No direct occupational chronology conflict within the assigned chunk | 0.86 | Retain as a staged no-conflict finding, but do not promote until page mapping and identity attribution are reviewed. |
| 2 | Assigned page belongs to document-level CV subject `Dario Arturo Pulgar` | 0.82 | Reconcile `CHUNK-1940bcca99c5-P0001-01`, missing `page-0001-chunk-01.md`, and actual `page-0004-chunk-01.md`; verify CV page 4 and title/source attribution. |
| 3 | Same broader staged CV/Habitat work-history cluster | 0.70 | Compare only after accepted CV identity-bearing context and Habitat page-boundary reviews are complete. |
| 4 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.60 | Require a reviewed bridge from `Dario Arturo Pulgar` to `Pulgar-Smith` before attaching occupational claims. |
| 5 | Same as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, or `Dario Pulgar A.` | 0.12 | Preserve separately or unresolved; require explicit full-name/date/profession/relationship continuity. |
| 6 | Connected to Jose/Juana parent candidates | 0.05 | No action from this page; revisit only with relationship-bearing evidence. |

## Recommended Next Action

Keep `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-1940bcca99c5-P0001-01-no-direct-conflict.md` as a staged no-direct-conflict note, not a promoted canonical conflict or fact source. Do not merge people, rename canonical pages, or attach the page-4 occupational claims to `wiki/people/dario-arturo-pulgar-smith.md` from this staged draft alone.

The exact next proof-review step is targeted CV identity and page-mapping review: reconcile the assigned `CHUNK-1940bcca99c5-P0001-01` and missing `page-0001-chunk-01.md` path against the existing CV page-4 chunk/page-image materials, verify the IBRD and Antamina entries against the page image or accepted conversion QA, and identify an evidence-grade CV title page or adjacent identity-bearing page that explicitly supports `Dario Arturo Pulgar` as the CV subject. Separately require an identity-bearing local source before treating `Dario Arturo Pulgar` as `Dario Arturo Pulgar-Smith`; preserve `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, and Jose/Juana parent candidates as separate hypotheses until a reviewed bridge exists.
