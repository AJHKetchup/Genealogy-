---
type: identity_conflict_analysis
status: completed
role: identity_researcher
worker: postconv-identity-analysis-20260531123359896
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
canonical_readiness: blocked_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Page 5 CV Control Conflict

## Blockers First

1. Physical page control is not certified. `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent locally, and no rendered `page-0005` image was found in the checked conversion-job page-image location.
2. The derivative readings conflict. The assigned chunk reads page 5 as 1979-1970 work history; the conversion-job page Markdown reads page 5 as 1999-1997 consulting work.
3. The chunk manifest contains duplicate `CHUNK-fb0a0000636f-P0005-01` entries, and the staged draft reports hash drift. This blocks using either derivative page-5 reading as the controlling text.
4. Neither page-5 derivative reading names `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, Jose parent candidates, Juana parent candidates, spouses, children, or a family relationship.
5. No same-person merge, duplicate-person decision, name-variant normalization, relationship claim, chronology claim, or canonical wiki update is ready from this staged draft.

## Literal Evidence Checked

- Assigned staged draft: `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531110937491.md`.
- Assigned chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`; literal entries include 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO.
- Conversion-job page Markdown: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`; literal entries include 1999 PROFONANPE and TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen Consultants and SNC Lavalin Agriculture.
- Aggregate converted file: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`; it includes the 1999-1997 page-5 block and later includes the 1979-1970 block, so it does not resolve page control.
- Related staged task: `research/_staging/tasks/TASK-STAGE-CHUNK-fb0a0000636f-P0005-01-conversion-qa-page-control-postconv-evidence-extraction-20260531110937491.md`.
- Reviewed context checked: `research/_staging/reviews/review-identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-proof-review-20260531112815413.md`.
- Canonical wiki context checked: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

## Hypotheses

| Rank | Hypothesis | Evidence supporting | Conflicts / limits | Identity confidence | Claim probability | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | The assigned staged draft is a true page-control conflict. | The chunk and conversion-job page Markdown disagree on the literal page-5 work history; source PDF/page image are absent; manifest duplication is present. | This proves a control problem, not which text is physically correct. | 0.90 | 0.90 | blocked_for_conversion_qa |
| 2 | Page 5 belongs to a document-level CV subject named `Dario Arturo Pulgar`. | The source title, source path, and converted file identify the document as `CV of Dario Arturo Pulgar`. | The page body does not repeat the subject name, and page control is unresolved. | 0.45 | 0.55 | hold_for_conversion_qa |
| 3 | `Dario Arturo Pulgar` from the CV is the same person as canonical `Dario Arturo Pulgar-Smith`. | Name overlap and family-supplied canonical context make this a reasonable bridge-review candidate. | This draft has no `Smith` surname, vital data, relationship to Alexander John Heinz, or other direct identifier. | 0.25 | 0.20 | not_ready |
| 4 | `Dario Arturo Pulgar` should remain a separate unresolved CV identity cluster pending bridge review. | Existing wiki guidance says records mentioning Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith should attach to `Dario Arturo Pulgar-Smith` only after identity review. | Separate cluster status is procedural, not proof of a distinct person. | 0.35 | 0.35 | not_ready |
| 5 | The CV subject is the same person as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Darío Pulgar Arriagada`. | Existing staged/canonical context contains Pulgar-Arriagada leads, including a `Darío Pulgar Arriagada` canonical stub. | This page-5 draft has no Arriagada surname, Jose/J. middle name, medical title, birth fact, or parentage bridge. | 0.05 | 0.03 | not_ready |
| 6 | Page 5 supports Jose/Juana parent candidates or a relationship chain. | Existing wiki context includes Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, and Juana de Dios Amagada de Pulgar. | Page 5 does not name Jose, Juana, parents, children, spouses, or a birth registration; family context only justifies a later double-check. | 0.02 | 0.01 | not_ready |

## Conflicts

- Same-person / duplicate-person: high risk if `Dario Arturo Pulgar` is silently merged with `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada candidate. Current support is document-title context only.
- Name-variant conflict: unresolved. `Pulgar`, `Pulgar-Smith`, `Pulgar-Arriagada`, and `Pulgar Arriagada` must remain separate hypotheses unless identity-bearing evidence is reviewed.
- Relationship conflict: none supported by this page. Jose/Juana parent candidates cannot be imported into the CV page-5 evidence.
- Chronology conflict: severe at the conversion layer. The 1979-1970 and 1999-1997 readings cannot both control physical page 5.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.34 | The document-level `Dario Arturo Pulgar` label is plausible, but no accepted bridge to a canonical Pulgar-line person is present. |
| conflict_severity | 0.88 | Page-control failure can corrupt occupational chronology and encourage Pulgar-line conflation. |
| evidence_quality | 0.30 | Evidence is derivative text plus staged/review notes; the physical source image is missing. |
| conversion_confidence | 0.10 | Competing derivative readings, absent page image/PDF, duplicate manifest entries, and reported hash drift block conversion reliance. |
| claim_probability | 0.90 | High probability that the correct current claim is a hold/conflict finding. |
| relevance | 0.95 | Checked materials are the assigned draft, referenced files, reviewed notes, or existing canonical Pulgar/Jose/Juana context. |
| canonical_readiness | 0.00 | No canonical fact, relationship, chronology claim, identity merge, or wiki update is ready. |

## Recommended Next Action

Hold for conversion QA. The exact next proof-review/promotion step is to restore or regenerate authoritative access to physical page 5 of `raw/sources/CV of Dario Arturo Pulgar.pdf`, compare that page against both derivative readings, and repair or quarantine duplicate chunk/hash metadata through the authorized conversion workflow.

After page control is certified, send only the accepted page-5 work-history claims through proof review. Then run a separate identity-bridge proof review before attaching accepted CV evidence to `wiki/people/dario-arturo-pulgar-smith.md` or merging it with any `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, Jose, or Juana candidate.

No raw sources, converted Markdown, chunks, conversion-job page Markdown, reviewed notes, staged drafts owned by other workers, or canonical wiki pages were edited.
