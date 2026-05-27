---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md
worker: postconv-identity-analysis-20260527065926865
staged_draft: research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md
source_path: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0004-01
page_reference: page 4
analysis_status: hold
canonical_readiness: hold_for_manifest_page_identity_qa_and_identity_bridge
---

# Identity/Conflict Analysis: conflict-chunk-fb0a0000636f-p0004-01

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md`.
- The literal chunk body does not name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Jose`, `Juana`, or any parent, spouse, child, grandchild, or household relationship.
- Subject attribution is document-level only: the source path, source packet, converted-file title, and chunk frontmatter identify a CV source titled for `Dario Arturo Pulgar`.
- The chunk manifest repeats `CHUNK-fb0a0000636f-P0004-01` for page 4 at the same chunk path with different character counts and hashes: `4572` / `5e6aed90f2420572473987255df4bbec4de8750bd2f9701a9b71b2896f27a43f` and `3985` / `504f69374f1d289f20e70388a7653b8f8673e10ae649490cb6df74fe04fc3112`.
- The converted file includes a first page-4 section with 2000 and 1999 work-history entries, while the referenced chunk contains 1988-1982 entries and appears later in the assembled converted file after page-6 material. This is a page-continuity/provenance blocker, not a genealogical contradiction.
- The source packet states that the original page image was not reviewed during extraction. I did not run conversion, perform external research, edit raw/conversion/chunk/canonical files, merge people, rename pages, or promote facts.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to attach similarly named Pulgar records until identity review.

## Hypothesis 1: Page Text Belongs To Document-Level CV Subject Dario Arturo Pulgar

Literal evidence:

- The source packet records `source_identity: Dario Arturo Pulgar, identified by the source title`.
- The source packet, converted file, and chunk frontmatter all point to `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The referenced chunk literal text gives typed CV work-history entries for 1988-1989 FAO in Ndola, Zambia; 1988 CIDA in Ethiopia; 1986-1987 Worldview International Foundation in Rome, Italy; and 1982-1985 independent communications consultant / CIDA.
- The page body contains no competing personal name.

Interpretation:

- This is the strongest narrow reading. The text probably belongs somewhere in the locally staged CV for `Dario Arturo Pulgar`, but the specific page-4/chunk identity is not promotion-ready because the page body is unnamed and the chunk/converted-file metadata conflict.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.76 | Local document metadata supports `Dario Arturo Pulgar`; page-local text is unnamed and page identity is unstable. |
| conflict_severity | 0.42 | No direct biographical contradiction, but provenance errors could misattribute occupational claims. |
| evidence_quality | 0.64 | Typed CV text is clear, while page image review and manifest reconciliation remain open. |
| conversion_confidence | 0.56 | Text reads cleanly, but duplicate manifest rows and page-continuity ambiguity reduce confidence. |
| claim_probability | 0.78 | Probable document-level CV attribution; less secure for exact page-4 claim attachment. |
| relevance | 0.99 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.20 | Hold pending page/provenance QA and identity bridge review. |

## Hypothesis 2: Same Person As Canonical Dario Arturo Pulgar-Smith

Literal evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` records family-supplied `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather.
- The CV source title and canonical page share the name elements `Dario Arturo Pulgar`.
- The referenced chunk does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, parentage, spouse, child, residence, birth date, or another direct identity bridge.

Interpretation:

- Same-person identity is plausible but unproved from this page. The shorter CV title/name cannot be silently normalized to the canonical Pulgar-Smith person without an identity-bearing CV page or another proof-reviewed bridge.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.58 | Strong name overlap, but no `Smith` surname or family bridge in the page text. |
| conflict_severity | 0.52 | Wrong attachment would place career facts on the wrong canonical person. |
| evidence_quality | 0.52 | Name overlap plus family-supplied context only. |
| conversion_confidence | 0.56 | Conversion readability does not resolve canonical identity. |
| claim_probability | 0.56 | Plausible, not proved. |
| relevance | 0.96 | Required Pulgar-line comparison. |
| canonical_readiness | 0.16 | No merge, attachment, or promotion. |

## Hypothesis 3: Same Person As Dario Jose Pulgar-Arriagada / Dario Or Darío Pulgar Arriagada

Literal evidence:

- Existing local context includes staged/canonical Pulgar-Arriagada evidence, including `Darío J. Pulgar Arriagada` as a 1918 médico-cirujano title recipient and canonical `Darío Pulgar Arriagada` named in a 2000 Chiguayante expropriation event.
- The referenced CV chunk does not print `Jose`, `J.`, `Arriagada`, `Pulgar A.`, a medical-surgeon role, Geneva/ICRC context, expropriation/property context, or any lineage bridge.

Interpretation:

- Name overlap is insufficient and potentially dangerous. Preserve these candidates as separate or unresolved until a proof-reviewed source explicitly bridges them to `Dario Arturo Pulgar` or to canonical `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.10 | Given-name/surname overlap only; page text lacks the key variant terms. |
| conflict_severity | 0.80 | Name-only merging could collapse distinct people, generations, and contexts. |
| evidence_quality | 0.42 | Compared evidence is indirect for this page and has separate review tracks. |
| conversion_confidence | 0.48 | This page's QA is unresolved and does not contain the variant names. |
| claim_probability | 0.08 | Low from this staged draft. |
| relevance | 0.88 | Required anti-conflation comparison. |
| canonical_readiness | 0.02 | Do not attach or merge. |

## Hypothesis 4: Relationship To Jose/Juana Parent Candidates

Literal evidence:

- Existing wiki/staged context includes Jose/Juana Pulgar-line candidates such as Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, and Juana de Dios Amagada de Pulgar.
- The referenced CV chunk contains no Jose, Juana, parent, spouse, child, household, lineage, birth, marriage, or death statement.
- The staged draft concerns CV work history and manifest QA, not a civil-register relationship.

Interpretation:

- Jose/Juana candidates justify a future Pulgar-line double-check only. They are not evidence for or against this CV page identity and cannot support parentage or ancestry claims here.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct identity or relationship bridge. |
| conflict_severity | 0.66 | Premature lineage attachment would create unsupported relationships. |
| evidence_quality | 0.36 | Related register evidence is outside this page and has separate QA caveats. |
| conversion_confidence | 0.38 | This page does not contain the names. |
| claim_probability | 0.04 | Page text supports no Jose/Juana relationship claim. |
| relevance | 0.62 | Relevant as anti-conflation context. |
| canonical_readiness | 0.01 | No relationship action. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for CV `Dario Arturo Pulgar` versus canonical Pulgar-Smith; high if conflated by name alone with `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar A.`, or Jose/Juana parent clusters.
- Name-variant conflict: this staged item supports only document-level `Dario Arturo Pulgar`; it does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, or `Dario Pulgar A.` as variants.
- Relationship-conflict evidence: none. No parent, spouse, child, grandchild, or relationship to Alexander John Heinz appears in the referenced chunk.
- Chronology-conflict evidence: none inside the 1982-1989 work-history sequence. The entries can coexist chronologically.
- Conversion/provenance conflict: material procedural conflict from duplicate page-4 manifest entries and converted-file page-continuity ambiguity.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Referenced text belongs to the document-level CV subject `Dario Arturo Pulgar` | 0.78 | Keep as held CV work-history evidence pending page/manifest QA. |
| 2 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.56 | Require explicit identity bridge from CV identity-bearing pages or another proof-reviewed source. |
| 3 | Same as `Dario Jose Pulgar-Arriagada` / `Dario/Darío Pulgar Arriagada` / `Darío J. Pulgar Arriagada` / `Dario Pulgar A.` | 0.08 | Preserve separately or unresolved; do not merge by name alone. |
| 4 | Connected to Jose/Juana parent candidates | 0.04 | No relationship action from this page; revisit only if lineage evidence appears. |

## Recommended Next Action

Keep `research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md` on hold for canonical promotion. Do not merge people, rename canonical pages, promote the page-4 work-history facts, or attach them to `wiki/people/dario-arturo-pulgar-smith.md` yet.

The exact next proof-review step is targeted CV page/provenance QA: compare the rendered PDF page 4 and surrounding pages against the converted file and chunk, reconcile why `CHUNK-fb0a0000636f-P0004-01` appears twice with different character counts and hashes, and determine which text belongs to source page 4. After that, perform a separate identity-bridge review using an identity-bearing CV page or other reviewed local evidence before attaching any CV occupational facts to canonical `Dario Arturo Pulgar-Smith`. Keep anti-conflation checks separate for `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar A.`, and Jose/Juana parent candidates.
