---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530221648063
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md
subject: "Dario Arturo Pulgar, document-level CV subject"
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conflict_type: derivative_transcription_page_control
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This note analyzes the staged draft `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md`.

## Blockers First

1. Page control is unresolved. The assigned chunk and aggregate converted file include 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO. The conversion job page Markdown for `page-0005.md` instead includes 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen/SNC Lavalin text.
2. The source packet records a hash mismatch: `converted_sha256_recorded_in_chunk` is `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, while `converted_sha256_observed` is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`.
3. The source packet reports duplicate manifest entries for `CHUNK-fb0a0000636f-P0005-01` with different character counts/hashes and reports that no `page-0005.jpg` was found under the conversion job page-images path. The job manifest, however, records an expected `page-images/page-0005.jpg`; this needs conversion QA, not silent normalization.
4. Page 5 body text does not repeat `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Pulgar-Arriagada`, `Dario Jose`, parent names, spouse, child, grandchild, birth, death, or any kinship statement. Identity attribution is document-level, not page-local.
5. No canonical attachment, merge, rename, parent-child claim, or work-history promotion is ready until conversion QA selects the controlling page-5 transcription and a separate identity bridge evaluates the CV subject.

## Literal Evidence

### Assigned Chunk / Aggregate Converted File Reading

- Source title/path: `CV of Dario Arturo Pulgar.pdf`.
- Page-body work-history sequence:
  - `1979 - 1982`, United Nations Centre for Human Settlements (HABITAT), Nairobi, Kenya, Development Support Communications Officer.
  - `1974 - 1978`, National Film Board of Canada (NFB), Montreal, Canada, Audio Visual Consultant.
  - `1972 - 1973`, Chile Films, Santiago, Chile, General Manager Distribution and Exhibition, Head of International Department.
  - `1970 - 1972`, Cine, Television y Comunicaciones (CITELCO), Santiago, Chile, Producer.
- The page ends with `EDUCATION`.

### Conversion Job Page Markdown Reading

- Page-body work-history sequence:
  - `1999`, National Trust Fund for Protected Areas in Peru (PROFONANPE), Peru, Consultant.
  - `1999`, Television Trust for the Environment (TVE), London, England, Consultant.
  - `1998 - 1999`, Arca Consulting/European Commission, Lesotho, Team Leader.
  - `1997-1998`, Klohn Crippen Consultants, Huaraz, Peru, Socio-economic Consultant.
  - `1997-1998`, SNC Lavalin Agriculture, Maracaibo, Venezuela, Training Consultant.
- The page text ends mid-sentence after `a study tour`.

### Existing Canonical Wiki Context

- `wiki/people/dario-arturo-pulgar-smith.md` names `Dario Arturo Pulgar-Smith` from family-supplied knowledge as Alexander John Heinz's maternal grandfather and explicitly warns not to automatically merge similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records.
- No canonical `wiki/people/dario-arturo-pulgar.md` or `wiki/people/dario-jose-pulgar-arriagada.md` page was found.
- `wiki/people/dar-o-pulgar-arriagada.md` is a separate stub for `Dario Pulgar Arriagada` with a 2000-12-05 Serviu Region del Bio Bio expropriation event.
- `wiki/people/dario-pulgar-child-passenger-age-11.md` and `wiki/people/dario-pulgar-adult-passenger-age-64.md` are separate passenger-list clusters.
- `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md` remain separate parent-candidate/person pages with their own limited staged evidence.

## Hypotheses

### H1: Page 5 Belongs To The Document-Level CV Subject `Dario Arturo Pulgar`

Evidence supporting:

- The source title, converted file title, source packet, and staged draft all identify the document as `CV of Dario Arturo Pulgar`.
- Both competing page-5 readings are CV-style occupational text and are compatible with a work-history page from the same kind of document.

Evidence against or limiting:

- The page body does not name the subject.
- Page control is blocked by incompatible derivative transcriptions and hash/manifest concerns.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.72 | Strong document-title context, but no page-local name and page control is blocked. |
| conflict severity | 0.85 | Different page-5 work histories cannot both be the controlling transcription. |
| evidence quality | 0.45 | Local staged evidence is relevant but derivative conflict prevents promotion. |
| conversion confidence | 0.20 | Explicit hash, page-control, and manifest/image QA blockers. |
| claim probability | 0.70 | Probable document-subject attribution only; not a promoted occupational claim. |
| relevance | 0.80 | High for Dario CV/work-history identity review, low for kinship. |
| canonical readiness | 0.10 | Not ready for canonical promotion. |

### H2: `Dario Arturo Pulgar` In This CV Is The Same Person As Canonical `Dario Arturo Pulgar-Smith`

Evidence supporting:

- The canonical name includes the full sequence `Dario Arturo Pulgar`.
- Family context makes this a reasonable identity-bridge target after page/control QA.

Evidence against or limiting:

- The CV title lacks `Smith`.
- Page 5 contains no family relationship, birth/death data, spouse, child, grandchild, or other identity bridge to Alexander John Heinz.
- The canonical page explicitly cautions against automatic attachment of similarly named Pulgar records.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.58 | Plausible same-person hypothesis, not proven by this page. |
| conflict severity | 0.55 | Moderate duplicate-person/name-variant risk if promoted prematurely. |
| evidence quality | 0.35 | Name overlap comes from document/canonical context, not page body. |
| conversion confidence | 0.20 | Same page-control blocker applies. |
| claim probability | 0.55 | Possible-to-probable, requiring identity-bridge proof review. |
| relevance | 0.75 | Relevant to maternal-line research if bridged. |
| canonical readiness | 0.10 | Not ready. |

### H3: Same Person As `Dario Jose Pulgar-Arriagada` Or `Dario/Dario Pulgar Arriagada`

Evidence supporting:

- Broader local context contains multiple Pulgar-Arriagada/Dario candidates, including a canonical stub for `Dario Pulgar Arriagada`.
- A later bridge might compare professional chronology, name forms, and local records across Pulgar clusters.

Evidence against or limiting:

- This staged draft and page-5 body do not use `Jose`, `Arriagada`, `Pulgar-Arriagada`, `Dario J.`, or `Dario Pulgar A.`.
- Existing Pulgar-Arriagada contexts are separate staged/canonical clusters and require their own proof-reviewed identity bridges.
- Name similarity alone is insufficient and risks merging distinct generations or relatives.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.20 | No direct name-form bridge from this page. |
| conflict severity | 0.70 | High conflation risk across Pulgar-line candidates. |
| evidence quality | 0.20 | Only broad family/name context, no page-local support. |
| conversion confidence | 0.20 | Page control remains blocked. |
| claim probability | 0.18 | Possible only as a future comparison hypothesis. |
| relevance | 0.55 | Relevant for anti-conflation, not for promotion. |
| canonical readiness | 0.05 | Not ready. |

### H4: Same Person As Jose/Juana Parent-Candidate Cluster

Evidence supporting:

- Existing wiki context includes `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, and `Juana Arriagada de Pulgar` as Pulgar-line candidates.

Evidence against or limiting:

- The assigned staged draft and page-5 body do not name Jose, Juana, parents, birth registration, spouse, child, or any kinship relationship.
- Parent-candidate records are from different staged birth-registration contexts with their own unresolved conversion/name issues.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity confidence | 0.05 | No evidence that page-5 CV subject is a Jose/Juana parent candidate. |
| conflict severity | 0.65 | High if parent candidates are imported into this CV by family context alone. |
| evidence quality | 0.10 | No direct support in assigned evidence. |
| conversion confidence | 0.20 | Page control still blocked. |
| claim probability | 0.03 | Not supported by this source. |
| relevance | 0.35 | Relevant only as an explicit anti-merge check. |
| canonical readiness | 0.00 | Not ready. |

## Conflict Assessment

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`; high if merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, passenger-list Dario candidates, or Jose/Juana parent candidates.
- Name-variant conflict: unresolved for `Pulgar` versus `Pulgar-Smith` and `Pulgar-Arriagada`; page 5 does not contain enough identity-bearing text to decide.
- Relationship conflict: none directly from this page. It does not state parents, spouse, children, grandchildren, or Alexander John Heinz relationship.
- Chronology conflict: direct chronology conflict exists only at the transcription-control level. The 1999/1998 sequence and the 1979-1970 sequence cannot both control the same source page 5. Do not build a life chronology from either until QA resolves the page.
- Conversion/provenance conflict: severe and controlling.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required Next Step |
| ---: | --- | ---: | --- |
| 1 | Page 5 is part of the CV locally titled for `Dario Arturo Pulgar` | 0.70 | Conversion QA must select the controlling page-5 transcription, reconcile hashes/manifest entries, and verify page image/PDF continuity. |
| 2 | The CV subject `Dario Arturo Pulgar` is canonical `Dario Arturo Pulgar-Smith` using a shortened surname form | 0.55 | After page-control QA, run a targeted identity-bridge proof review using identity-bearing CV title/front matter or other accepted local evidence explicitly connecting `Dario Arturo Pulgar` to `Pulgar-Smith`. |
| 3 | The CV subject is the same as `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada` | 0.18 | Only compare after separate proof-reviewed Pulgar-Arriagada identity evidence is assembled; require full-name, date, profession, place, and chronology bridge. |
| 4 | The CV subject can be attached to Jose/Juana parent candidates | 0.03 | No action from this page except anti-conflation; parent claims require their own birth-registration proof review. |

## Recommended Next Action

Hold all claims from this staged draft for conversion QA. The exact next proof-review step is: restore or confirm the page-5 image/PDF control, reconcile the duplicate manifest/hash discrepancy, and decide whether assigned page 5 is the 1979-1970 HABITAT/NFB/Chile Films/CITELCO page or the 1999/1998 PROFONANPE/TVE/Arca/Klohn/SNC page. After that, run a separate identity-bridge review comparing the accepted CV subject `Dario Arturo Pulgar` against canonical `Dario Arturo Pulgar-Smith`, while keeping `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, passenger-list Dario candidates, and Jose/Juana parent candidates separate unless direct reviewed evidence bridges them.
