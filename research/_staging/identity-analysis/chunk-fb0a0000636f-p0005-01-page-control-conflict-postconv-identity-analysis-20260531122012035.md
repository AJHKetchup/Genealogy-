---
type: identity_conflict_analysis
status: completed
role: identity_researcher
worker: postconv-identity-analysis-20260531122012035
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531110937491.md
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531110937491.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
identity_confidence: low
conflict_severity: high
evidence_quality: low
conversion_confidence: very_low
claim_probability: 0.90
relevance: high
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: CV Page 5 Control Conflict

## Blockers First

1. The original source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent locally, and no rendered `page-0005` image was found in the conversion-job page-image path checked during this analysis.
2. Page control is unresolved. The assigned chunk reads page 5 as a 1979-1970 work-history page ending at `EDUCATION`; the conversion-job page Markdown reads page 5 as a different 1999-1997 consulting-work page.
3. The chunk manifest contains duplicate `CHUNK-fb0a0000636f-P0005-01` entries with divergent metadata, and the staged draft reports observed hash drift. This makes the derivative layer unsafe for canonical identity attachment.
4. Neither competing page-5 derivative text names `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, parents, spouse, children, or a kinship bridge.
5. No merge, duplicate-person conclusion, relationship assertion, chronology repair, or canonical wiki update is ready from this staged draft.

## Literal Evidence Checked

- Assigned staged draft: `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531110937491.md`.
- Assigned chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`; literal entries include HABITAT, National Film Board of Canada, Chile Films, and CITELCO.
- Conversion-job page Markdown: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`; literal entries include PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- Aggregate converted file: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`; it contains both the page-5 conversion-job reading and, later in the same pages 4-9 aggregate, the 1979-1970 work-history text.
- Existing canonical wiki context checked: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`.

## Hypotheses

| Rank | Hypothesis | Evidence supporting | Conflicts / limits | Identity confidence | Claim probability | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | This staged draft is correctly identifying a page-control conflict, not a resolved identity claim. | Two local derivative readings assign materially different CV content to page 5; source PDF and page image are absent; manifest duplicates the chunk id. | Does not decide which text controls physical page 5. | 0.90 | 0.90 | blocked |
| 2 | The page-5 material is document-level CV evidence for a person labeled `Dario Arturo Pulgar`. | Source path, converted title, and surrounding CV pages identify the document as `CV of Dario Arturo Pulgar`. | The page-5 body does not restate the subject name, and page control is unresolved. | 0.45 | 0.55 | hold_for_conversion_qa |
| 3 | The CV subject is the canonical `Dario Arturo Pulgar-Smith`. | Existing wiki has a family-supplied canonical person `Dario Arturo Pulgar-Smith`; the source title is close to that preferred name minus `Smith`. | No page-5 text supplies `Smith`, family relationship, date/place identity anchors, or a direct bridge. | 0.25 | 0.20 | not_ready |
| 4 | The CV subject is the same person as `Dario Arturo Pulgar` without `Smith`, as a name variant. | Document title uses `Dario Arturo Pulgar`; canonical page uses `Dario Arturo Pulgar-Smith`. | Name similarity alone is insufficient; no direct alias, vital fact, parent, spouse, or family bridge is present in this draft. | 0.35 | 0.35 | not_ready |
| 5 | The CV subject is the same person as `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío/Dario Pulgar Arriagada`. | Broader workspace context contains separate Pulgar-Arriagada and Darío Pulgar Arriagada candidates. | The assigned staged draft and page-5 derivatives do not mention `Jose`, `J.`, `Arriagada`, health-service captain language, medical title evidence, parents, or any same-person bridge. | 0.05 | 0.03 | not_ready |
| 6 | The page-5 conflict can support Jose/Juana parent-candidate merges or parent-child relationships. | Existing wiki context includes `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada`. | This CV page-control draft does not name Jose, Juana, a child, a spouse, a birth event, or a parent relation. Family-context hints justify later checking only; they do not alter this source reading. | 0.02 | 0.01 | not_ready |

## Conflict Assessment

- Same-person conflict: high risk if `Dario Arturo Pulgar` from the CV is silently attached to `Dario Arturo Pulgar-Smith` or to Pulgar-Arriagada candidates. The current evidence supports only a document-level label pending page control and identity-bridge review.
- Duplicate-person risk: unresolved. `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, and `Darío/Dario Pulgar Arriagada` must remain distinct hypotheses until a proof-review bridge compares direct identifiers across sources.
- Name-variant risk: medium to high. Dropping `Smith` or adding `Arriagada/Jose/J.` would be interpretation, not literal support from the assigned page-5 materials.
- Relationship-conflict risk: high if any Jose/Juana parent context is imported into this CV page. No parent-child or spouse claim is present here.
- Chronology-conflict risk: high at the conversion layer. The assigned chunk places page 5 at 1979-1970; the conversion-job page Markdown places page 5 at 1999-1997. This is a page-control conflict before it is a biographical chronology claim.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.34 | The document-level label `Dario Arturo Pulgar` is plausible from file/title context, but no canonical person bridge is proved. |
| conflict_severity | 0.88 | Competing page content and potential Pulgar-line conflation would materially affect chronology and identity attachment. |
| evidence_quality | 0.30 | Evidence is derivative-only for this task; source PDF/page image is missing. |
| conversion_confidence | 0.10 | Page-control conflict, missing image/PDF, duplicate chunk metadata, and hash drift block reliable extraction. |
| claim_probability | 0.90 | High probability that the staged draft's hold/conflict finding is correct. |
| relevance | 0.95 | All checked evidence directly references the assigned staged draft, source, chunk, or local canonical Pulgar context. |
| canonical_readiness | 0.00 | No fact, relationship, identity merge, or wiki update is ready. |

## Recommended Next Action

Hold this staged draft for conversion QA. The exact next proof-review/promotion path is:

1. Restore or regenerate authoritative access to physical page 5 of `raw/sources/CV of Dario Arturo Pulgar.pdf`.
2. Compare the physical page against both derivative readings and repair or quarantine the duplicate chunk/hash metadata through the authorized conversion workflow.
3. After page control is certified, run proof review only on the accepted narrow page-5 work-history claims.
4. Run a separate identity-bridge proof review before attaching accepted CV claims to `wiki/people/dario-arturo-pulgar-smith.md` or merging with any `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Darío/Dario Pulgar Arriagada`, Jose, or Juana candidate.

No raw sources, converted Markdown, chunks, reviewed notes, or canonical wiki pages were edited.
