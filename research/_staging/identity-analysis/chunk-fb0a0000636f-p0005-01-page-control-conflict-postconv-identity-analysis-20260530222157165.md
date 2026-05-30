---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530222157165
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md
subject: "Dario Arturo Pulgar, document-level CV subject"
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
conflict_type: derivative_transcription_page_control
analysis_status: hold_for_conversion_qa
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This note analyzes staged draft `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md`.

## Blockers First

1. Page control is unresolved. The assigned chunk reads page 5 as the 1979-1970 HABITAT/NFB/Chile Films/CITELCO work-history page. The conversion job `page-markdown/page-0005.md` reads page 5 as the 1999/1998 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin page.
2. The source packet records hash drift: the chunk-recorded converted SHA-256 is `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, while the observed converted SHA-256 is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`.
3. The source packet reports duplicate manifest entries for `CHUNK-fb0a0000636f-P0005-01` with different counts/hashes.
4. `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is absent in this checkout, and `raw/sources/CV of Dario Arturo Pulgar.pdf` is also absent. I could not perform independent image/PDF page-control review.
5. Neither derivative page-5 text repeats `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, Jose, Juana, Alexander John Heinz, or any kinship statement.
6. No canonical merge, canonical rename, relationship promotion, or work-history promotion is ready from this evidence.

## Literal Evidence

Assigned chunk / aggregate converted-file reading:

- Source title/path identifies a CV of `Dario Arturo Pulgar`.
- Page body reads `1979 - 1982` United Nations Centre for Human Settlements (HABITAT), Nairobi, Development Support Communications Officer.
- It then reads `1974 - 1978` National Film Board of Canada, Montreal, Audio Visual Consultant; `1972 - 1973` Chile Films, Santiago; and `1970 - 1972` Cine, Television y Comunicaciones (CITELCO), Santiago.
- The page ends with the heading `EDUCATION`.

Conversion job page Markdown reading:

- Page body reads `1999` National Trust Fund for Protected Areas in Peru (PROFONANPE), Peru, Consultant.
- It also reads `Television Trust for the Environment (TVE)`, London, Consultant; `1998 - 1999` Arca Consulting/European Commission, Lesotho, Team Leader; `1997-1998` Klohn Crippen Consultants, Huaraz; and `SNC Lavalin Agriculture`, Maracaibo.
- The text ends mid-sentence after `a study tour`.

Existing canonical/staged context:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and identifies `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather. It explicitly warns not to automatically merge similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records.
- `wiki/people/dar-o-pulgar-arriagada.md` is a separate stub for `Dario Pulgar Arriagada` with a 2000-12-05 expropriation event.
- `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md` are separate parent-candidate/person pages from other evidence clusters. This page-5 CV evidence does not name them.

## Hypotheses

### H1: Page 5 belongs to the document-level CV subject `Dario Arturo Pulgar`

Supporting evidence: source title, converted-file title, source packet, and staged draft all identify the document as `CV of Dario Arturo Pulgar`. Both competing page-5 readings are coherent CV work-history text.

Conflicts and limits: page body is unnamed; page control is blocked by derivative disagreement, missing page image/PDF, duplicate manifest entries, and hash drift.

Scores: identity confidence 0.62; conflict severity 0.86; evidence quality 0.38; conversion confidence 0.20; claim probability 0.55; relevance 0.98; canonical readiness 0.05.

### H2: `Dario Arturo Pulgar` in this CV is canonical `Dario Arturo Pulgar-Smith`

Supporting evidence: strong name overlap at `Dario Arturo Pulgar`; the canonical Pulgar-Smith page is the most obvious local identity-bridge target for this CV subject.

Conflicts and limits: this page lacks `Smith`, family relationships, birth/death data, Alexander John Heinz, or another bridge identifier. Family context justifies a double-check, not a silent correction.

Scores: identity confidence 0.43; conflict severity 0.55; evidence quality 0.32; conversion confidence 0.20; claim probability 0.40; relevance 0.75; canonical readiness 0.05.

### H3: The CV subject is `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada`

Supporting evidence: the broader workspace has Pulgar-Arriagada identity candidates and a canonical `Dario Pulgar Arriagada` stub, so this is a required anti-conflation comparison.

Conflicts and limits: this staged draft and page body do not state `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, medical/Geneva context, property context, parents, spouse, or child. Name overlap alone is insufficient.

Scores: identity confidence 0.08; conflict severity 0.72; evidence quality 0.18; conversion confidence 0.20; claim probability 0.07; relevance 0.58; canonical readiness 0.00.

### H4: The CV subject connects to Jose/Juana parent candidates

Supporting evidence: Jose del Carmen Pulgar, Juana Arriagada de Pulgar, and Juana de Dios Amagada de Pulgar exist in local Pulgar-line context.

Conflicts and limits: this page contains no Jose/Juana name and no parent, spouse, child, household, or other relationship statement. Parent candidates come from separate birth-registration evidence and cannot bridge this CV page.

Scores: identity confidence 0.03; conflict severity 0.65; evidence quality 0.08; conversion confidence 0.20; claim probability 0.02; relevance 0.35; canonical readiness 0.00.

## Conflict Assessment

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`; this page does not prove or disprove the match.
- Duplicate-person risk: moderate for `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`; high if merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, passenger-list Dario candidates, or Jose/Juana parent candidates.
- Name-variant conflict: unresolved. Page 5 supports no page-local full name form.
- Relationship conflict: none directly evidenced. No parents, spouse, children, grandchildren, or Alexander John Heinz relationship is stated.
- Chronology conflict: severe at the derivative transcription/page-control level. The 1979-1970 sequence and the 1999/1998 sequence cannot both be the controlling transcription for physical page 5.
- Conversion/provenance conflict: controlling blocker.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Both derivative texts likely belong somewhere in the Dario Arturo Pulgar CV, but page-5 assignment/control is corrupted | 0.70 | Conversion QA must restore/confirm page image or PDF control, reconcile manifest/hash drift, and select the controlling page-5 transcription. |
| 2 | Page 5 is attributable at document level to `Dario Arturo Pulgar` | 0.55 | After page-control QA, proof review must verify visible page continuity and the identity-bearing CV title/front matter. |
| 3 | CV subject is canonical `Dario Arturo Pulgar-Smith` | 0.40 | Run separate identity-bridge proof review using accepted local identity-bearing evidence connecting `Dario Arturo Pulgar` to `Pulgar-Smith`. |
| 4 | CV subject is `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` / `Dario/Dario Pulgar Arriagada` | 0.07 | Preserve separately unless later reviewed evidence supplies full-name, date, profession, place, and chronology bridge. |
| 5 | CV subject connects to Jose/Juana parent candidates | 0.02 | No action from this page; parentage requires separate relationship proof review. |

## Recommended Next Action

Hold all claims from this staged draft for conversion QA. The exact next proof-review step is to restore or confirm `page-0005.jpg` or source-PDF access, reconcile duplicate manifest entries and hash drift, compare physical page 5 against both derivative readings, and decide whether page 5 controls to the 1979-1970 HABITAT/NFB/Chile Films/CITELCO text or the 1999/1998 PROFONANPE/TVE/Arca/Klohn/SNC text.

Only after page control is certified should a separate identity-bridge review compare the accepted CV subject `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`. Keep `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, passenger-list Dario candidates, and Jose/Juana parent candidates separate unless direct reviewed evidence bridges them.

No raw sources, converted Markdown, chunks, source packets, staged drafts outside this note, or canonical wiki pages were edited.
