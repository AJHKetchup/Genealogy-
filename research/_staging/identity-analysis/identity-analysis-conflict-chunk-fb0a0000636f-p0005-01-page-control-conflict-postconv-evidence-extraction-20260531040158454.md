---
type: identity_conflict_analysis
status: complete
role: identity_researcher
worker: postconv-identity-analysis-20260531050733476
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
canonical_readiness: not_ready
recommended_next_action: hold_for_conversion_qa
---

# Identity Analysis: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This analysis covers staged draft `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md`.

## Blockers First

1. Page control is unresolved. The assigned chunk for page 5 transcribes a CV work-history sequence from `1979 - 1982` HABITAT through `1970 - 1972` CITELCO and ends with `EDUCATION`; the conversion-job page Markdown for page 5 transcribes `1999`, `1998 - 1999`, and `1997-1998` consulting entries for PROFONANPE, TVE, Arca/European Commission, Klohn Crippen, and SNC Lavalin.
2. The controlling physical source cannot be checked in this workspace. `raw/sources/CV of Dario Arturo Pulgar.pdf`, the job-local staged PDF, and `page-images/page-0005.jpg` are absent.
3. Metadata control is unstable. The chunk records converted SHA-256 `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, while the observed converted file hash is `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`. The staged draft also reports duplicate manifest entries for the same chunk id with conflicting counts and hashes.
4. Neither derivative page-5 reading repeats a page-local personal name. Attribution to `Dario Arturo Pulgar` comes from the source title/path and document context only.
5. The page contains no literal `Smith`, `Arriagada`, `Jose`, `Juana`, parent, spouse, child, grandchild, household, birth, or death statement. No relationship claim or canonical merge can be made from this page.

## Literal Evidence

- Staged draft: identifies the source path as `raw/sources/CV of Dario Arturo Pulgar.pdf`, but reports the source unavailable locally and recommends `hold_for_conversion_qa`.
- Assigned chunk: literal work-history entries are HABITAT, National Film Board of Canada, Chile Films, and CITELCO, dated 1979-1970.
- Conversion-job page Markdown: literal work-history entries are PROFONANPE, TVE, Arca/European Commission, Klohn Crippen, and SNC Lavalin, dated 1999-1997.
- Existing canonical page `wiki/people/dario-arturo-pulgar-smith.md`: represents `Dario Arturo Pulgar-Smith` from family-supplied knowledge as Alexander John Heinz's maternal grandfather and warns not to automatically merge similarly named source clusters.
- Existing canonical page `wiki/people/dar-o-pulgar-arriagada.md`: represents `Darío Pulgar Arriagada` as a separate stub with a 2000 expropriation-notice life fact.
- Existing canonical pages `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`: preserve Jose/Juana parent-candidate stubs from other staged or reviewed evidence, not from this CV page.

## Hypotheses Ranked

| Rank | Hypothesis | Evidence supporting | Evidence against / limits | Probability | Identity confidence |
| ---: | --- | --- | --- | ---: | ---: |
| 1 | The broader source packet is a CV for document-level subject `Dario Arturo Pulgar`. | Source title/path and converted-file header consistently say `CV of Dario Arturo Pulgar`; both derivative page texts are coherent CV work-history content. | Page 5 itself does not name him, and page control is unresolved. | 0.55 | 0.45 |
| 2 | The CV subject may be the canonical `Dario Arturo Pulgar-Smith`. | Name overlap is meaningful, and the canonical page is an open Pulgar-Smith identity home that explicitly expects later identity review. | This page lacks `Smith`, family links, dates, Alexander John Heinz, or any bridge identifier. Family-supplied context is a prompt for review, not a correction to the source. | 0.30 | 0.25 |
| 3 | The CV subject is the same person as `Dario Jose Pulgar-Arriagada`. | Pulgar-line context makes this a comparison candidate. | This page lacks `Jose`, `Arriagada`, medical/Geneva context, birth/age/parent data, or relationship bridge. Name overlap alone is insufficient. | 0.05 | 0.05 |
| 4 | The CV subject is the same person as `Dario/Darío Pulgar Arriagada`. | Shared given name and surname family cluster. | Canonical `Darío Pulgar Arriagada` is currently supported by a 2000 expropriation notice; this page gives no `Arriagada`, property, residence, or chronology bridge. | 0.05 | 0.05 |
| 5 | Page 5 supports Jose/Juana parent candidates or Pulgar-Arriagada child relationships. | Jose/Juana candidates exist in other wiki/staged contexts. | This page has no Jose/Juana names and no kinship language. Relationship evidence is absent here. | 0.01 | 0.02 |

## Conflicts

- Conversion conflict: two derivative transcripts claim to represent page 5 but preserve different chronological sections of the CV.
- Chronology conflict: the assigned chunk's 1979-1970 sequence cannot be silently reconciled with the conversion-job page Markdown's 1999-1997 sequence as one page.
- Identity-scope conflict: the source title supplies `Dario Arturo Pulgar`, but page-local text supplies only unnamed work-history entries.
- Duplicate-person/name-variant risk: `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, and `Darío Pulgar Arriagada` remain separate candidates until a reviewed identity bridge compares names, dates, occupations, places, relationships, and source provenance.
- Relationship-conflict risk: Jose/Juana parent candidates are irrelevant to this page unless later proof review finds a direct bridge in a different source. This page should not affect those parent-candidate pages.

## Scores

| Dimension | Score / Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.45 for document-level `Dario Arturo Pulgar`; 0.25 for `Dario Arturo Pulgar-Smith`; 0.05 or lower for Pulgar-Arriagada candidates | Page-local identity is absent; source-title context is the only identity support. |
| conflict_severity | high | Page-control and hash conflicts block all downstream identity and chronology use. |
| evidence_quality | low | Evidence is derivative and metadata-unstable; original PDF/page image is unavailable. |
| conversion_confidence | 0.15 | Competing page-5 transcripts and missing image prevent source-controlled selection. |
| claim_probability | 0.55 that the source packet concerns `Dario Arturo Pulgar`; 0.30 that it may later bridge to `Dario Arturo Pulgar-Smith`; 0.05 or lower for Pulgar-Arriagada; 0.01 for Jose/Juana relationship support | Probabilities distinguish document attribution from canonical identity or relationship claims. |
| relevance | high | A CV titled for `Dario Arturo Pulgar` is relevant to the Pulgar identity cluster, but this page is not promotion-ready. |
| canonical_readiness | not_ready | Conversion QA and separate identity-bridge proof review are required before canonical use. |

## Recommended Next Action

Hold all page-5 claims and identity attachments for conversion QA. Restore or verify the source PDF or authoritative rendered page image, reconcile the duplicate chunk/hash metadata, and certify whether physical page 5 is the 1999-1997 page or the 1979-1970 page. After that, run a separate identity-bridge proof review comparing the accepted CV subject against `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, and any Jose/Juana parent candidates only if the accepted evidence provides direct bridge facts.

No raw sources, converted Markdown, chunks, conversion-job page Markdown, or canonical wiki pages were edited.
