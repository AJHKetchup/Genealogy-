---
type: identity_conflict_analysis
status: completed
role: identity_researcher
worker: postconv-identity-analysis-20260531122550211
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

# Identity/Conflict Analysis: CV Page 5 Control Conflict

## Blockers First

1. Physical page control is unresolved. The staged conflict draft reports that the source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent locally, no rendered page-0005 image was available, and the derivative artifacts disagree.
2. The assigned chunk reads page 5 as a 1979-1970 work-history page containing HABITAT, National Film Board of Canada, Chile Films, and CITELCO. The conversion-job `page-0005.md` reads page 5 as a different 1999-1997 consulting-work page containing PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
3. Derivative provenance is unstable: the staged draft reports duplicate manifest/hash drift for `CHUNK-fb0a0000636f-P0005-01`. That blocks any chronology or identity attachment.
4. Neither competing page-5 derivative text independently states `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, parents, spouse, children, or a kinship bridge.
5. No same-person merge, duplicate-person decision, name-variant normalization, Jose/Juana relationship claim, chronology repair, or canonical wiki update is ready from this draft.

## Literal Evidence Checked

- Assigned staged draft: `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531110937491.md`.
- Assigned chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`; literal work-history span is 1979-1982 through 1970-1972.
- Conversion-job page Markdown: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`; literal work-history span is 1999 through 1997-1998.
- Existing proof-review context checked: `research/_staging/reviews/review-identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-proof-review-20260531112815413.md` and `research/_staging/reviews/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-researcher-20260531051655241-proof-review-postconv-proof-review-20260531113039307.md`.
- Existing canonical context checked: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`.

## Hypotheses

| Rank | Hypothesis | Evidence supporting | Conflicts / limits | Identity confidence | Claim probability | Canonical readiness |
| --- | --- | --- | --- | ---: | ---: | --- |
| 1 | The assigned staged draft correctly identifies a page-control conflict. | Two local derivative readings assign incompatible content to page 5; proof reviews confirm missing source/page image and manifest/hash concerns. | Does not decide which derivative controls physical page 5. | 0.90 | 0.90 | blocked_for_conversion_qa |
| 2 | Page 5 belongs to a document-level CV subject labeled `Dario Arturo Pulgar`. | The source path and converted document title identify the broader source as `CV of Dario Arturo Pulgar`. | Page 5 itself does not restate the subject name, and page control is unresolved. | 0.45 | 0.55 | hold_for_conversion_qa |
| 3 | `Dario Arturo Pulgar` from the CV is the same person as canonical `Dario Arturo Pulgar-Smith`. | The canonical page exists and the names are close, with `Smith` absent from the CV title. | No accepted local bridge in this draft supplies `Smith`, a family relationship, vital anchors, or direct alias evidence. | 0.25 | 0.20 | not_ready |
| 4 | `Dario Arturo Pulgar` is a name variant to preserve separately until bridged. | The workspace has staged CV evidence under `Dario Arturo Pulgar` and a canonical `Dario Arturo Pulgar-Smith` page that warns against automatic merges. | Name similarity alone cannot prove identity. | 0.35 | 0.35 | not_ready |
| 5 | The CV subject is the same person as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada`. | The broader workspace contains separate Pulgar-Arriagada candidates and a canonical `Dario Pulgar Arriagada` stub. | This staged draft does not mention Jose, J., Arriagada, medical/health-service titles, parents, or other bridge evidence. | 0.05 | 0.03 | not_ready |
| 6 | The page-5 draft supports Jose/Juana parent candidates or relationships. | Existing wiki context contains Jose del Carmen Pulgar, Juana Arriagada de Pulgar, and Jose del Carmen Segundo Pulgar Arriagada. | This CV page-control draft does not name Jose, Juana, a child, spouse, birth event, or parent relation. Family context is only a prompt for later double-checking. | 0.02 | 0.01 | not_ready |

## Conflicts

- Same-person / duplicate-person: high risk if `Dario Arturo Pulgar` is silently merged with `Dario Arturo Pulgar-Smith` or Pulgar-Arriagada candidates. Current support is document-context only.
- Name-variant: unresolved. `Pulgar`, `Pulgar-Smith`, and `Pulgar-Arriagada` must remain distinct hypotheses unless a separate identity-bridge proof review accepts direct identifiers.
- Relationship conflict: no relationship claim is present. Importing Jose/Juana parent context into this CV page would exceed the literal evidence.
- Chronology conflict: severe at the conversion layer. The 1979-1970 and 1999-1997 readings cannot both control physical page 5.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.34 | Plausible document-level `Dario Arturo Pulgar` label, but no canonical bridge. |
| conflict_severity | 0.88 | Page-control failure would affect chronology and could cause Pulgar-line conflation. |
| evidence_quality | 0.30 | Evidence is derivative and reviewed-note based; source/page image is missing. |
| conversion_confidence | 0.10 | Competing derivative texts, missing source/image, and hash drift block reliability. |
| claim_probability | 0.90 | High probability that the staged draft is correct as a hold/conflict finding. |
| relevance | 0.95 | Checked materials directly reference the staged draft, source, chunk, reviews, or local Pulgar canonical context. |
| canonical_readiness | 0.00 | No claim, relationship, identity merge, or canonical attachment is ready. |

## Recommended Next Action

Hold for conversion QA. The exact next step is to restore or regenerate authoritative access to physical page 5 of `raw/sources/CV of Dario Arturo Pulgar.pdf`, compare the physical page against both derivative readings, and repair or quarantine duplicate chunk/hash metadata through the authorized conversion workflow.

After page control is certified, run proof review only on the accepted narrow page-5 work-history claims. Then run a separate identity-bridge proof review before attaching accepted CV evidence to `wiki/people/dario-arturo-pulgar-smith.md` or merging it with any `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, Jose, or Juana candidate.

No raw sources, converted Markdown, chunks, reviewed notes, staged drafts owned by other workers, or canonical wiki pages were edited.
