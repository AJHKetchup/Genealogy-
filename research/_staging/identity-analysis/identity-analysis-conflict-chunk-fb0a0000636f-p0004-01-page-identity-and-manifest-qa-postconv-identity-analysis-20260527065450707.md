---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md
worker: postconv-identity-analysis-20260527065450707
staged_draft: research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md
source_path: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0004-01
page_reference: page 4
analysis_status: hold
canonical_readiness: hold_for_page_identity_manifest_qa_and_identity_bridge
---

# Identity/Conflict Analysis: conflict-chunk-fb0a0000636f-p0004-01

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md`.
- The page-4 body does not literally name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Jose`, `Juana`, or any parent, spouse, child, grandchild, or household relationship.
- Subject attribution is document-level only: the source title/path, converted-file metadata, chunk frontmatter, and source packet point to `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The chunk manifest repeats `CHUNK-fb0a0000636f-P0004-01` for page 4 and the same path with different character counts and hashes: `4572` / `5e6aed90f2420572473987255df4bbec4de8750bd2f9701a9b71b2896f27a43f` and `3985` / `504f69374f1d289f20e70388a7653b8f8673e10ae649490cb6df74fe04fc3112`.
- The source packet says the original page image was not reviewed during extraction. I did not run conversion, perform external research, edit source/conversion/chunk/canonical files, merge people, rename pages, or promote facts.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review.

## Hypothesis 1: Page 4 Belongs To Document-Level CV Subject Dario Arturo Pulgar

Literal evidence:

- The source packet records `source_identity: Dario Arturo Pulgar, identified by the source title`.
- The converted file title is `CV of Dario Arturo Pulgar pages 4-9`, and page metadata lists source `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The chunk frontmatter points to the same source PDF and converted file.
- Page-4 literal text contains work-history entries for 1988-1989 FAO in Ndola, Zambia; 1988 CIDA in Ethiopia; 1986-1987 Worldview International Foundation in Rome, Italy; and 1982-1985 independent communications consultant / CIDA.
- The page body contains no competing personal name.

Interpretation:

- This is the strongest narrow hypothesis. The page probably belongs to the locally identified CV subject, but it is not standalone identity proof because the page is unnamed and the page/chunk manifest has duplicate metadata.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.80 | Multiple local metadata layers identify the CV subject; page text is unnamed. |
| conflict_severity | 0.38 | No direct biographical contradiction, but provenance duplication can misattribute claims. |
| evidence_quality | 0.68 | Typed CV text and source packet align, with page-image and manifest QA open. |
| conversion_confidence | 0.62 | Transcription appears complete, but duplicate page-4 manifest rows reduce confidence. |
| claim_probability | 0.82 | Probable document-level attribution to `Dario Arturo Pulgar`. |
| relevance | 0.98 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.24 | Hold pending page image/PDF and manifest audit. |

## Hypothesis 2: Same Person As Canonical Dario Arturo Pulgar-Smith

Literal evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` records family-supplied `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather.
- The CV source title and canonical page share the name elements `Dario Arturo Pulgar`.
- Page 4 does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, parentage, spouse, child, birth date, or another direct identity bridge.

Interpretation:

- Same-person identity is plausible but unproved from this page. The CV's shorter name form cannot be silently normalized to canonical Pulgar-Smith without an identity-bearing CV page or another proof-reviewed bridge.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.62 | Strong name overlap, no direct `Smith` or family bridge. |
| conflict_severity | 0.50 | Wrong attachment would place occupational facts on the wrong canonical person. |
| evidence_quality | 0.55 | Name overlap plus family-supplied canonical context only. |
| conversion_confidence | 0.62 | Conversion readability does not resolve identity. |
| claim_probability | 0.60 | Plausible, not proved. |
| relevance | 0.96 | Required Pulgar-line comparison. |
| canonical_readiness | 0.18 | No merge, attachment, or promotion. |

## Hypothesis 3: Same Person As Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada

Literal evidence:

- Local staged context has an identity candidate for `Dario Jose Pulgar-Arriagada` from source metadata/title of an ICRC group photograph, with low confidence for image-level identification.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` records a 2000-12-05 event naming `Darío Pulgar Arriagada`.
- Page 4 does not print `Jose`, `Arriagada`, `Pulgar A.`, a medical-surgeon role, Geneva/ICRC context, expropriation/property context, or any lineage bridge.

Interpretation:

- Name overlap is insufficient. These must remain separate or unresolved until a proof-reviewed source explicitly bridges them to `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.12 | Given-name/surname overlap only. |
| conflict_severity | 0.78 | Name-only merging could collapse distinct people, generations, and contexts. |
| evidence_quality | 0.44 | Compared evidence is sparse for this page and held elsewhere. |
| conversion_confidence | 0.50 | Page-4 QA and separate Pulgar-Arriagada QA remain unresolved. |
| claim_probability | 0.10 | Low from this staged draft. |
| relevance | 0.88 | Required anti-conflation comparison. |
| canonical_readiness | 0.03 | Do not attach or merge. |

## Hypothesis 4: Relationship To Jose/Juana Parent Candidates

Literal evidence:

- Existing canonical context includes Jose/Juana Pulgar-line candidate pages and relationship candidates.
- Page 4 contains no Jose, Juana, parent, spouse, child, household, lineage, birth, marriage, or death statement.
- The staged draft concerns CV work history and manifest QA, not a family-register relationship.

Interpretation:

- Jose/Juana candidates justify a future Pulgar-line double-check only. They are not evidence for or against this page-4 CV identity and cannot support parentage or ancestry claims here.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.06 | No direct identity or relationship bridge. |
| conflict_severity | 0.64 | Premature lineage attachment would create unsupported relationships. |
| evidence_quality | 0.38 | Related register evidence is outside this page and has separate QA caveats. |
| conversion_confidence | 0.40 | This page does not contain the names. |
| claim_probability | 0.05 | Page 4 supports no Jose/Juana relationship claim. |
| relevance | 0.62 | Relevant as anti-conflation context. |
| canonical_readiness | 0.01 | No relationship action. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for CV `Dario Arturo Pulgar` versus canonical Pulgar-Smith; high if conflated by name alone with `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Darío Pulgar Arriagada`, `Dario Pulgar A.`, or Jose/Juana parent clusters.
- Name-variant conflict: page 4 supports only document-level `Dario Arturo Pulgar`; it does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, or `Dario Pulgar A.` as variants.
- Relationship-conflict evidence: none. No parent, spouse, child, grandchild, or relationship to Alexander John Heinz appears on page 4.
- Chronology-conflict evidence: none inside the page-4 work-history entries. The 1982-1989 entries can coexist chronologically.
- Conversion/provenance conflict: material procedural conflict from duplicate page-4 manifest entries for the same chunk id/path with different character counts and hashes.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Page 4 belongs to document-level CV subject `Dario Arturo Pulgar` | 0.82 | Keep as held CV work-history evidence pending page/manifest QA. |
| 2 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.60 | Require explicit identity bridge from CV identity-bearing pages or another proof-reviewed source. |
| 3 | Same as `Dario Jose Pulgar-Arriagada` / `Dario/Darío Pulgar Arriagada` / `Darío Pulgar Arriagada` / `Dario Pulgar A.` | 0.10 | Preserve separately or unresolved; do not merge by name alone. |
| 4 | Connected to Jose/Juana parent candidates | 0.05 | No relationship action from page 4; revisit only if lineage evidence appears. |

## Recommended Next Action

Keep `research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md` on hold for canonical promotion. Do not merge people, rename canonical pages, promote page-4 work-history facts, or attach them to `wiki/people/dario-arturo-pulgar-smith.md` yet.

The exact next proof-review step is targeted CV page/provenance QA: compare the rendered PDF page 4 against the chunk and converted file, reconcile why the chunk manifest repeats `CHUNK-fb0a0000636f-P0004-01` with different character counts and hashes, and confirm document continuity from an identity-bearing CV page. Only after that should a separate identity-bridge review decide whether document-level `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`. Keep anti-conflation checks separate for `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Darío Pulgar Arriagada`, `Dario Pulgar A.`, and Jose/Juana parent candidates.
