---
type: identity_conflict_analysis
status: complete
role: identity_researcher
worker: postconv-identity-analysis-20260531052136436
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01

This note analyzes staged conflict draft `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md`.

## Blockers First

- Page control is not established. The assigned chunk reads page 5 as a 1979-1970 CV work-history page ending with `EDUCATION`, while the conversion-job page Markdown and assembled converted file read page 5 as a 1999-1997 consulting-work page.
- The physical source cannot resolve the conflict in this pass. `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent locally, and no `page-0005.jpg`, `page-0005.jpeg`, or `page-0005.png` was found under the conversion-job directory.
- Metadata control is unstable. The chunk manifest contains duplicate `CHUNK-fb0a0000636f-P0005-01` entries with different character counts and hashes, and the conflict draft reports observed hash drift.
- Neither derivative page body literally names the person. `Dario Arturo Pulgar` is a document-level/source-title attribution, not a page-local reading.
- No page-5 derivative states `Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose`, `Juana`, parentage, spouse, child, grandchild, birth, death, or household relationships.
- No same-person merge, duplicate-person resolution, name-variant normalization, relationship claim, chronology claim, or canonical promotion is ready.

## Literal Evidence Reviewed

- Staged conflict draft: marks confidence low and recommends `hold_for_conversion_qa` because derivative transcripts disagree and the source PDF/page image is unavailable.
- Assigned chunk: preserves `1979 - 1982` United Nations Centre for Human Settlements (HABITAT), `1974 - 1978` National Film Board of Canada, `1972 - 1973` Chile Films, `1970 - 1972` Cine, Television y Comunicaciones (CITELCO), and `EDUCATION`.
- Conversion-job page Markdown / assembled converted file: preserve `1999` PROFONANPE, `1999` Television Trust for the Environment, `1998 - 1999` Arca Consulting/European Commission, `1997-1998` Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- Existing source packets for page-5 CV work identify the subject as `Dario Arturo Pulgar` from source title/file context and state that the page body does not repeat the subject's name.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and warns not to attach similarly named Dario/Pulgar records without identity review.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` is a separate `Dario Pulgar Arriagada` stub with a narrow 2000 expropriation-notice fact.
- Existing Jose/Juana pages and notes concern separate register-derived contexts; they are not named in this page-control conflict.

## Hypotheses And Scores

| rank | hypothesis | evidence supporting | conflicts / limits | identity_confidence | conflict_severity | evidence_quality | conversion_confidence | claim_probability | relevance | canonical_readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | The broader source is a CV for document-level subject `Dario Arturo Pulgar`. | Source title/path, converted-file title, and staged packets identify the document as a CV of `Dario Arturo Pulgar`; both competing derivatives look like CV work-history pages. | Page-local name absent; physical page 5 is not controlled; two competing chronologies cannot both be the controlling page. | 0.45 | 0.88 | 0.32 | 0.15 | 0.55 | 0.95 | 0.03 |
| 2 | `Dario Arturo Pulgar` may be canonical `Dario Arturo Pulgar-Smith`. | Name overlap with the family-supplied canonical person; the canonical page expects later identity review. | No `Smith`, Alexander John Heinz relationship, birth date, spouse, child, or other bridge appears in either page-5 derivative. | 0.25 | 0.70 | 0.24 | 0.15 | 0.30 | 0.95 | 0.00 |
| 3 | Same person as a staged CV/HABITAT work-history cluster. | The chunk's 1979-1982 HABITAT reading resembles other local CV/HABITAT materials for Dario Pulgar. | The page-control conflict means the HABITAT text may not be controlling page 5; identity remains document-level. | 0.22 | 0.74 | 0.25 | 0.15 | 0.24 | 0.82 | 0.00 |
| 4 | Same person as `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`. | Broad Dario/Pulgar name overlap and Pulgar-line context require anti-conflation review. | No `Jose`, `Arriagada`, medical/delegate context, property context, age, residence, or kinship bridge appears here. | 0.06 | 0.76 | 0.18 | 0.15 | 0.06 | 0.74 | 0.00 |
| 5 | Page 5 supports Jose/Juana parent candidates. | Jose/Juana candidates exist in separate local Pulgar/Arriagada register contexts. | This page-control conflict names no Jose or Juana and states no parent-child relationship. | 0.01 | 0.62 | 0.10 | 0.15 | 0.01 | 0.45 | 0.00 |

## Conflict Findings

- Same-person conflict: unresolved between source-title `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: high if `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, and `Dario/Dario Pulgar Arriagada` are merged by name alone.
- Name-variant conflict: this page does not prove `Pulgar` as a shortened form of `Pulgar-Smith`, does not reconcile `Arturo` with `Jose`, and does not equate `Pulgar` with `Pulgar-Arriagada`.
- Relationship conflict: none supported from this staged page-control evidence. Alexander John Heinz and Jose/Juana parent contexts remain external to this page.
- Chronology conflict: severe. The derivative 1979-1970 sequence conflicts materially with the derivative 1999-1997 sequence.
- Conversion conflict: severe. Missing physical control plus manifest/hash drift blocks proof review and canonical readiness.

## Recommended Next Action

Keep this staged conflict on `hold_for_conversion_qa`. The exact next step is to restore or confirm access to `raw/sources/CV of Dario Arturo Pulgar.pdf` or an authoritative rendered page-5 image, compare it against both derivative readings, repair the duplicate manifest/hash drift, and certify the controlling page-5 transcription.

After page control is certified, run proof review only on the accepted page-5 work-history claims. A separate identity-bridge proof review must then compare the certified CV subject against `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, and Jose/Juana parent candidates before any canonical attachment. Do not merge, rename, normalize, attach, or promote any canonical fact from this conflicted page.
