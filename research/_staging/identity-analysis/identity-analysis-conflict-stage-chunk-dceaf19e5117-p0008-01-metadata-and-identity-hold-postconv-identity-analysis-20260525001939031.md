---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-dceaf19e5117-p0008-01-metadata-and-identity-hold.md"
worker: postconv-identity-analysis-20260525001939031
staged_draft: research/_staging/conflicts/chunk-dceaf19e5117-p0008-01-metadata-and-identity-hold.md
source_packet: research/_staging/source-packets/chunk-dceaf19e5117-p0008-01-cv-dario-arturo-pulgar-work-history.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0008-chunk-01.md
chunk_id: CHUNK-dceaf19e5117-P0008-01
canonical_candidate: wiki/people/dario-arturo-pulgar-smith.md
canonical_readiness: hold_for_conversion_qa_and_identity_bridge
---

# Identity/Conflict Analysis: CV Page 8 Metadata And Identity Hold

## Blockers First

- The exact staged draft is `research/_staging/conflicts/chunk-dceaf19e5117-p0008-01-metadata-and-identity-hold.md`.
- The staged draft and source packet cite `CHUNK-dceaf19e5117-P0008-01`, converted SHA `dceaf19e511728a6cacce6d03293232ed56641d0485aa2eabf44020e36edc942`, and chunk path `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0008-chunk-01.md`.
- Current workspace check on 2026-05-25 found the cited page-8 chunk path missing. The current chunk manifest has no page-0008 chunk entry and records converted SHA `b2e036516c17cf6c253a84554ca9fccd71944e51ff46121a8549b9ec6904a7a3`; live SHA256 for the converted file is `4CA8AFB8A1237D8C8955315996E4B5B25EC20EF3A7F99E38F6D43B09F3064CDE`.
- The staged draft also reports earlier live hashes `80E88301BC413B8BC399F89368350D85F7D1CC4E6C47F433771FBD8539C337E7` and `F448C2448CCC713862999298972577E73BD915C6E679A2844B27A229BC5D33C9`, plus older `7bf5ff6de7d9` lineage. This is a material derivative-provenance conflict.
- Page 8 itself does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Pulgar-Smith`, `Smith`, `Dario Jose`, `Dario J.`, `Pulgar-Arriagada`, `Arriagada`, `Jose`, `Juana`, Alexander John Heinz, or any kinship relationship.
- The canonical page `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to automatically merge similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith clusters.

## Literal Evidence

From the assigned staged draft and source packet, page 8 supports a work-history sequence in the CV:

- `1979 - 1982`, United Nations Centre for Human Settlements (HABITAT), Nairobi, Kenya, Development Support Communications Officer.
- `1974 - 1978`, National Film Board of Canada (NFB), Montreal, Canada, Audio Visual Consultant.
- `1972 - 1973`, Chile Films, Santiago, Chile, General Manager Distribution and Exhibition, Head of International Department.
- `1970 - 1972`, Cine, Television/Televisión y Comunicaciones (CITELCO), Santiago, Chile, Producer.

The current converted file also contains the page-8 work-history text in the same broad sequence, including HABITAT, NFB, Chile Films, CITELCO, and the `EDUCATION` heading following the CITELCO entry. That is a derivative-text check only; it does not resolve the missing chunk path or hash lineage.

## Interpretation Boundary

The page can be interpreted as a continuation page within a source titled/path-named `CV of Dario Arturo Pulgar.pdf`. That supports a document-level candidate subject, `Dario Arturo Pulgar`, after conversion/provenance QA. It does not, by itself, prove that the CV subject is the same person as canonical `Dario Arturo Pulgar-Smith`, nor that `Dario Arturo Pulgar` is a variant of any `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar A.`, or Jose/Juana parent cluster.

## Hypotheses And Evidence

### 1. Page 8 Belongs To The CV Subject Dario Arturo Pulgar

Hypothesis: the page-8 work-history entries belong to document-level CV subject `Dario Arturo Pulgar`.

Supporting evidence:

- The source packet and converted file identify the source as `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- Page 8 is internally consistent with a CV work-history page and continues the same professional chronology pattern seen in adjacent CV pages.
- The current converted file retains page-8 text with the same employers and date ranges.

Conflicts and cautions:

- The page body itself does not name the subject.
- The staged derivative metadata is unstable, and the cited page-8 chunk is missing from current chunks.
- The current manifest skips from page 7 to a duplicate page 5 entry and page 9, with no page-8 chunk entry.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.76 | Strong document-title/context attribution, but no page-body name. |
| conflict_severity | 0.62 | Metadata mismatch blocks reliable citation and promotion. |
| evidence_quality | 0.58 | Staged packet plus derivative converted text; missing current chunk. |
| conversion_confidence | 0.50 | Text appears legible, but provenance and page-8 chunk state are unresolved. |
| claim_probability | 0.78 | Probable as document-level CV subject evidence after QA. |
| relevance | 0.95 | Directly relevant to Dario Arturo Pulgar work-history staging. |
| canonical_readiness | 0.20 | Hold until conversion QA reconciles the file/chunk lineage. |

### 2. Same Person As Canonical Dario Arturo Pulgar-Smith

Hypothesis: document-level `Dario Arturo Pulgar` in the CV is the same person as `wiki/people/dario-arturo-pulgar-smith.md`.

Supporting evidence:

- The canonical page names `Dario Arturo Pulgar-Smith`, and the CV source title names `Dario Arturo Pulgar`.
- Family-supplied canonical context identifies Dario Arturo Pulgar-Smith as Alexander John Heinz's maternal grandfather.
- Existing local instructions treat this as the plausible canonical candidate requiring proof review.

Conflicts and cautions:

- Page 8 does not include `Smith`, `Pulgar-Smith`, Alexander John Heinz, family position, birth/death facts, spouse, child, or any identity bridge.
- The canonical page warns against automatically merging similarly named Pulgar clusters.
- Attaching work-history facts to the canonical page would require both resolved conversion metadata and an accepted identity-bearing CV page or bridge.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Plausible name overlap and local candidate, but no page-level bridge. |
| conflict_severity | 0.72 | False canonical attachment risk is significant. |
| evidence_quality | 0.42 | Family-supplied canonical page plus document title, not direct proof. |
| conversion_confidence | 0.50 | Conversion lineage remains unresolved. |
| claim_probability | 0.45 | Live hypothesis only. |
| relevance | 0.96 | This is the staged canonical candidate. |
| canonical_readiness | 0.05 | Not ready for promotion from page 8 alone. |

### 3. Same Person As Dario Jose Pulgar-Arriagada / Dario J. Pulgar Arriagada

Hypothesis: CV subject `Dario Arturo Pulgar` is the same as `Dario Jose Pulgar-Arriagada` or `Darío J. Pulgar Arriagada`.

Supporting evidence:

- Broad Dario/Pulgar name overlap exists in the workspace.
- Local staged packets separately include `Darío J. Pulgar Arriagada` as a 1918 `Médicos-Cirujanos` title-conferral name, and `Dario Jose Pulgar-Arriagada` as photograph/source-metadata context.

Conflicts and cautions:

- Page 8 does not state `Jose`, `J.`, `Arriagada`, medical title, Geneva/ICRC context, parents, spouse, age, or residence.
- The 1918 medical-title packet explicitly says not to merge with `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith` without a separate identity bridge.
- The Dario Jose photograph/source-metadata materials are not visible-text identity proof in the staged context reviewed.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Name-family overlap only. |
| conflict_severity | 0.78 | High risk of cross-generation or occupation-cluster conflation. |
| evidence_quality | 0.20 | No direct bridge in this page. |
| conversion_confidence | 0.50 | Page-8 conversion issue does not help this bridge. |
| claim_probability | 0.08 | Unsupported by assigned evidence. |
| relevance | 0.84 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not merge or promote as a variant. |

### 4. Same Person As Dario/Darío Pulgar Arriagada

Hypothesis: CV subject `Dario Arturo Pulgar` is the same person as the `Dario/Darío Pulgar Arriagada` cluster, including official Chile health-service listings or the existing `wiki/people/dar-o-pulgar-arriagada.md` page.

Supporting evidence:

- Broad Dario/Pulgar overlap.
- Existing staged packets name `Dario Pulgar-Arriagada` under Chile and describe him as `Capitaine du Service de Santé`.
- Existing canonical `Darío Pulgar Arriagada` has a 2000 Chiguayante expropriation event.

Conflicts and cautions:

- Page 8 does not state `Arriagada`, health-service captain, Chiguayante, expropriation, legal notice, or medical/director context.
- The CV page describes communications, film, and development-work roles in 1970-1982, not health-service or medical-office roles.
- The 2000 Chiguayante event supplies no age, occupation, parentage, or bridge to the CV subject in the reviewed page.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Broad name overlap only. |
| conflict_severity | 0.76 | High same-name conflation risk. |
| evidence_quality | 0.18 | No direct identity bridge. |
| conversion_confidence | 0.50 | Page-8 conversion issue does not support this merge. |
| claim_probability | 0.06 | Unsupported by assigned evidence. |
| relevance | 0.82 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Preserve separately. |

### 5. Jose/Juana Parent Candidates

Hypothesis: page-8 evidence supports or conflicts with existing Jose/Juana parent candidates, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Supporting evidence:

- Existing wiki context contains Jose/Juana Pulgar-line parent candidates in other records.

Conflicts and cautions:

- Page 8 contains no parent names, no unnamed-parent phrase, no birth or household facts, and no relationship language.
- Existing Jose/Juana parent candidates are tied to other children or records, not this CV page.
- Family-context hints justify later comparison only after an identity-bearing bridge, not any parent-child conclusion from this page.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.00 | No page-8 parent evidence. |
| conflict_severity | 0.58 | Unsupported parent inference would be misleading. |
| evidence_quality | 0.05 | No relevant literal support in assigned page. |
| conversion_confidence | 0.50 | Conversion state irrelevant to parent identity. |
| claim_probability | 0.00 | Not supported. |
| relevance | 0.65 | Required anti-conflation checkpoint. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person conflict: unresolved between `Dario Arturo Pulgar` and `Dario Arturo Pulgar-Smith`; page 8 cannot resolve it.
- Duplicate-person risk: high if `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, and older medical/health-service clusters are merged by name alone.
- Name-variant conflict: page 8 supports only document-context `Dario Arturo Pulgar`; it does not prove `Pulgar-Smith`, `Smith`, `Jose`, `J.`, `Arriagada`, or `Pulgar-Arriagada` variants.
- Relationship conflict: no relationship is stated on page 8.
- Chronology conflict: no direct chronology conflict within the page-8 CV entries; the larger conflict is cross-cluster chronology if older medical/1918/1929/1953/2000 Pulgar candidates are merged without identity proof.
- Conversion/provenance conflict: severe enough to block promotion. The staged draft, current manifest, and live converted-file hash disagree, and the current page-8 chunk is absent.

## Ranked Outcome

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Page 8 is document-level work-history evidence for `Dario Arturo Pulgar` after conversion QA. | 0.78 | Hold for conversion/chunk/hash reconciliation. |
| 2 | CV subject may be canonical `Dario Arturo Pulgar-Smith`. | 0.45 | Require separate identity-bearing CV page or accepted local bridge before promotion. |
| 3 | Same as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada`. | 0.08 | Preserve as separate unresolved cluster; do not merge. |
| 4 | Same as `Dario/Darío Pulgar Arriagada`. | 0.06 | Preserve as separate unresolved cluster; do not merge. |
| 5 | Supports Jose/Juana parent candidates. | 0.00 | No relationship action. |

## Recommended Next Action

Do not promote the page-8 work-history claims and do not attach them to `wiki/people/dario-arturo-pulgar-smith.md` yet. The exact next proof-review step is conversion/provenance QA for `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md` and its chunk manifest: restore or regenerate a current page-0008 chunk, reconcile the converted SHA lineage (`dceaf19e5117`, `7bf5ff6de7d9`, `80E883...`, `b2e036...`, and live `4CA8AF...`), and visually/proof-review page 8 against the source PDF/page image. After that, run a separate identity-bridge proof review using an identity-bearing CV page or accepted local bridge to decide whether document-level `Dario Arturo Pulgar` can be attached to canonical `Dario Arturo Pulgar-Smith`. Keep all Pulgar-Arriagada and Jose/Juana parent candidates separate unless a direct, proof-reviewed bridge names compatible identity anchors.
