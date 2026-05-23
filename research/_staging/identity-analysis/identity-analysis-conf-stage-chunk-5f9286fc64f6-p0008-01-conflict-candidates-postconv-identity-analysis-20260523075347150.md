---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/CONF-STAGE-CHUNK-5f9286fc64f6-P0008-01-conflict-candidates.md
worker: postconv-identity-analysis-20260523075347150
staged_draft: research/_staging/conflicts/CONF-STAGE-CHUNK-5f9286fc64f6-P0008-01-conflict-candidates.md
source_path: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-5f9286fc64f6-P0008-01-cv-dario-pulgar-page-8.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0008-chunk-01.md
chunk_id: CHUNK-5f9286fc64f6-P0008-01
page_reference: page 8
analysis_status: hold
canonical_readiness: hold
---

# Identity/Conflict Analysis: CONF-STAGE-CHUNK-5f9286fc64f6-P0008-01

## Blockers

- Exact staged draft reviewed: `research/_staging/conflicts/CONF-STAGE-CHUNK-5f9286fc64f6-P0008-01-conflict-candidates.md`.
- Page 8 has no page-body personal name. It lists occupational entries and an `EDUCATION` heading, but does not repeat `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, `Jose`, or `Juana`.
- The attribution to `Dario Arturo Pulgar` is document-level evidence from the source title/path, converted-file title, staged draft, and source packet. It is not a literal page-8 name reading.
- The page-8 body does not state birth, death, parents, spouse, children, grandchild, or any relationship to Alexander John Heinz.
- The canonical page `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith require identity review before attachment.
- Conversion QA remains unresolved. The source packet says the rendered page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0008.jpg` is missing from the workspace and must be compared before canonical promotion.
- Metadata should be reconciled before promotion: the assigned staged draft and source packet use `CHUNK-5f9286fc64f6-P0008-01`, while the referenced chunk file frontmatter records `CHUNK-56be215c030b-P0008-01` and `converted_sha256: 56be215c030b...`.
- This analysis did not perform external research, run conversion, edit raw sources, edit converted Markdown, edit chunks, merge people, rename canonical pages, or promote facts.

## Literal Evidence Reviewed

- Staged conflict draft: no direct evidence conflict was found in the chunk; the stated caution is identity attribution because page 8 does not repeat the subject's full name.
- Source packet: `source_identity: Dario Arturo Pulgar, from source title/file identity rather than page-body text`.
- Page 8 literal entries:
  - `1979 - 1982` United Nations Centre for Human Settlements (HABITAT), Nairobi, Kenya, `Development Support Communications Officer`.
  - `1974 - 1978` National Film Board of Canada (NFB), Montreal, Canada, `Audio Visual Consultant`.
  - `1972 - 1973` Chile Films, Santiago, Chile, `General Manager Distribution and Exhibition, Head of International Department`.
  - `1970 - 1972` Cine, Television y Comunicaciones (CITELCO), Santiago, Chile, `Producer`.
- Canonical context: `wiki/people/dario-arturo-pulgar-smith.md` names `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather from family-supplied knowledge only.
- Local Pulgar-line context includes separate or unresolved candidates: `Dario Pulgar (child passenger, age 11)`, `Dario Pulgar (adult passenger, age 64)`, `Dario Pulgar A.`, `Dario J. Pulgar Arriagada`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

## Hypothesis 1: Page 8 Belongs To Document-Level CV Subject Dario Arturo Pulgar

Evidence supporting:

- The source path, converted file, source packet, and staged conflict draft all identify the broader document as `CV of Dario Arturo Pulgar`.
- Page 8 reads as a continuation of a CV and contains no competing personal name.
- The occupational sequence is internally coherent: CITELCO 1970-1972, Chile Films 1972-1973, NFB 1974-1978, HABITAT 1979-1982.

Interpretation:

- This is the strongest narrow hypothesis. Page 8 probably belongs to the document-level CV subject `Dario Arturo Pulgar`.
- It remains a document-context attribution, not page-body identity proof.

Scores:

| metric | score | note |
|---|---:|---|
| identity_confidence | 0.82 | Document-level metadata is consistent, but the page itself is unnamed. |
| conflict_severity | 0.24 | No internal contradiction; risk is attribution and QA scope. |
| evidence_quality | 0.70 | Staged and converted evidence align, but depend on source-title context. |
| conversion_confidence | 0.72 | Transcription is high confidence, but page-image QA is unresolved. |
| claim_probability | 0.86 | Probable that the page belongs to the CV subject. |
| relevance | 0.96 | Directly addresses the assigned conflict draft. |
| canonical_readiness | 0.30 | Hold pending image QA, metadata reconciliation, and identity bridge. |

## Hypothesis 2: Same Person As Canonical Dario Arturo Pulgar-Smith

Evidence supporting:

- The given-name pair `Dario Arturo` and surname element `Pulgar` overlap between the CV document identity and canonical `Dario Arturo Pulgar-Smith`.
- The canonical person is a Pulgar-Smith maternal-line person and is the obvious local candidate for a Dario Arturo Pulgar CV.

Evidence against or limiting:

- Page 8 does not say `Smith` or `Pulgar-Smith`.
- Page 8 does not name Alexander John Heinz or any family relationship.
- The canonical page itself says similarly named Pulgar records should not be automatically merged.

Interpretation:

- Same-person identity is plausible, but this page cannot prove the shortened-name variant.
- Do not silently normalize `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.

Scores:

| metric | score | note |
|---|---:|---|
| identity_confidence | 0.62 | Meaningful name overlap, but no surname-variant or family bridge. |
| conflict_severity | 0.44 | Wrong attachment would place CV work history on the wrong canonical person. |
| evidence_quality | 0.56 | Mostly metadata plus family-supplied canonical context. |
| conversion_confidence | 0.72 | Text QA does not solve the identity bridge. |
| claim_probability | 0.62 | Plausible, not proved. |
| relevance | 0.97 | This is the main canonical candidate. |
| canonical_readiness | 0.22 | Hold; no merge or fact promotion. |

## Hypothesis 3: Same Person As A Broader Dario Pulgar Work-History Cluster

Evidence supporting:

- Page 8's HABITAT, NFB, Chile Films, and CITELCO sequence is distinctive.
- Other staged local notes treat `Dario Pulgar` work-history material as potentially connected to this CV cluster, especially where Chilean film work, Montreal/NFB, language ability, and HABITAT appear together.

Evidence against or limiting:

- The assigned conflict draft is page 8 only and does not itself compare the whole memoir/HABITAT cluster.
- Page 8 does not bridge from `Dario Pulgar` to `Dario Arturo Pulgar-Smith`.

Interpretation:

- The work-history cluster is a strong comparison target, but it should be proof-reviewed as a cluster before any canonical attachment.

Scores:

| metric | score | note |
|---|---:|---|
| identity_confidence | 0.74 | Distinctive chronology supports a same-person cluster, pending proof review. |
| conflict_severity | 0.34 | Low internal conflict; moderate risk if staged cluster evidence is over-promoted. |
| evidence_quality | 0.64 | Useful occupational sequence, but comparison remains staged. |
| conversion_confidence | 0.66 | Page 8 and related material have separate QA holds. |
| claim_probability | 0.74 | Probable same work-history identity cluster. |
| relevance | 0.90 | Relevant to resolving Dario Pulgar identity. |
| canonical_readiness | 0.26 | Hold pending cluster review and identity bridge. |

## Hypothesis 4: Same Person As Child Passenger Dario Pulgar, Age 11 In 1953

Evidence supporting:

- `wiki/people/dario-pulgar-child-passenger-age-11.md` records a Chilean child passenger named `Dario Pulgar`, age 11, student, on 1953-08-07.
- A child aged 11 in 1953 is chronologically compatible with secondary education in the 1950s and adult employment from 1970 onward.

Evidence against or limiting:

- Page 8 gives no age, birth year, passenger context, parents, sibling group, `Arturo`, or `Smith`.
- Chronological compatibility is not an identity bridge.

Interpretation:

- Possible, but not ready for merge or attachment.

Scores:

| metric | score | note |
|---|---:|---|
| identity_confidence | 0.48 | Chronology and surname are compatible only. |
| conflict_severity | 0.42 | Premature merge could collapse separate same-name people. |
| evidence_quality | 0.52 | Cross-source comparison lacks a direct bridge. |
| conversion_confidence | 0.64 | Passenger and CV clusters have separate evidence limits. |
| claim_probability | 0.46 | Possible, not probable enough for action. |
| relevance | 0.70 | Relevant anti-conflation check. |
| canonical_readiness | 0.10 | No merge or canonical attachment. |

## Hypothesis 5: Same Person As Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, Dario Pulgar Arriagada, Or Dario Pulgar A.

Evidence supporting:

- The names share `Dario` and `Pulgar`.
- Local staged evidence includes `Dario Jose Pulgar-Arriagada` in Geneva photograph metadata, `Dario J. Pulgar Arriagada` as a 1918 medico-cirujano title recipient, `Darío Pulgar Arriagada` in a 2000 expropriation notice, and `Dario Pulgar A.` as a 1928 medical surgeon passenger.

Evidence against or limiting:

- Page 8 does not contain `Jose`, `J.`, `Arriagada`, `Pulgar A.`, medical-surgeon evidence, Geneva Convention evidence, property/expropriation evidence, or parentage.
- The 1918 medico-cirujano and 1928 medical-surgeon contexts likely point to an older or separate identity cluster than a CV subject beginning listed employment in 1970.
- The Geneva photo evidence is source-metadata dependent and does not visibly identify the person in the converted page.

Interpretation:

- Name-only merging would be unsafe. Preserve these as separate or unresolved Pulgar-line hypotheses unless a proof-reviewed source explicitly bridges them.

Scores:

| metric | score | note |
|---|---:|---|
| identity_confidence | 0.12 | Only broad name overlap; middle name, surname, occupation, and chronology diverge. |
| conflict_severity | 0.78 | High risk of merging distinct generations and professions. |
| evidence_quality | 0.48 | Compared records are sparse or QA-held for identity. |
| conversion_confidence | 0.46 | Several compared sources have reread or image-identity issues. |
| claim_probability | 0.10 | Low from this page. |
| relevance | 0.88 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.04 | Do not attach or merge. |

## Hypothesis 6: Jose/Juana Parent Candidates Connect This Page-8 Subject To The Pulgar Line

Evidence supporting:

- Existing local context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Some staged birth-register notes preserve Pulgar/Jose/Juana family relationships, while also warning about image-sensitive readings and conversion conflicts.

Evidence against or limiting:

- Page 8 does not name Jose or Juana.
- Page 8 contains no parent, child, spouse, witness, declarant, household, or lineage statement.
- The Jose/Juana register clusters are themselves unresolved for some readings and do not bridge to the CV subject.

Interpretation:

- Jose/Juana candidates are a checklist for later Pulgar-line proof review only. They cannot be used to infer a relationship for page 8.

Scores:

| metric | score | note |
|---|---:|---|
| identity_confidence | 0.06 | No direct person or relationship bridge. |
| conflict_severity | 0.64 | Unsupported lineage attachment would create false relationships. |
| evidence_quality | 0.40 | Related register evidence remains conversion-sensitive. |
| conversion_confidence | 0.38 | Jose/Juana readings have unresolved QA; page 8 does not mention them. |
| claim_probability | 0.06 | Page 8 does not support a parent-candidate link. |
| relevance | 0.62 | Relevant only as a required Pulgar-line comparison. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate between CV `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`; high if merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, or `Dario Pulgar A.`.
- Name-variant conflict: page 8 supports only document-level `Dario Arturo Pulgar`; it does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.` variants.
- Relationship-conflict evidence: none on page 8. No Jose/Juana parent candidate or Alexander John Heinz relationship is stated.
- Chronology-conflict evidence: none within page 8's 1970-1982 employment sequence. Chronology cautions against merging the CV subject with earlier medical/Geneva/passenger `Dario Pulgar A.` and `Dario J./Jose Pulgar Arriagada` clusters without a bridge.
- Conversion and metadata conflict: page-8 text is usable for staged analysis, but canonical use is blocked by missing page-image QA and the `5f9286fc64f6` versus `56be215c030b` chunk/converted metadata mismatch.

## Ranked Hypotheses

| rank | hypothesis | probability | required next step |
|---:|---|---:|---|
| 1 | Page 8 belongs to document-level CV subject `Dario Arturo Pulgar` | 0.86 | Restore/locate page image, verify page continuity, and reconcile metadata. |
| 2 | Same person as broader staged `Dario Pulgar` work-history cluster | 0.74 | Compare proof-reviewed CV page 8 with proof-reviewed HABITAT/NFB/Chile Films evidence. |
| 3 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.62 | Require an explicit proof-reviewed bridge from `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`. |
| 4 | Same person as child passenger `Dario Pulgar`, age 11 in 1953 | 0.46 | Compare full passenger-list family context with identity-bearing CV pages. |
| 5 | Same as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, or `Dario Pulgar A.` | 0.10 | Preserve as separate or unresolved; do not merge by name alone. |
| 6 | Connected to Jose/Juana parent candidates | 0.06 | No action from page 8; revisit only if a source states parentage or a lineage bridge. |

## Recommended Next Action

Keep `research/_staging/conflicts/CONF-STAGE-CHUNK-5f9286fc64f6-P0008-01-conflict-candidates.md` on hold as a no-direct-conflict, identity-QA caution. Do not promote page-8 occupational facts to canonical pages yet.

The exact next proof-review step is targeted CV identity and QA review: locate or regenerate the page-8 rendered image, compare it against the converted transcription, verify the source title/page continuity across identity-bearing CV pages, and reconcile the `CHUNK-5f9286fc64f6-P0008-01` versus `CHUNK-56be215c030b-P0008-01` metadata mismatch. After that, compare the proof-reviewed page-8 HABITAT/NFB/Chile Films/CITELCO sequence to proof-reviewed `Dario Pulgar` work-history evidence. Only a source or accepted proof note explicitly bridging `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith` should authorize canonical attachment. Keep `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, `Dario Pulgar A.`, and Jose/Juana parent candidates separate unless later evidence provides a direct bridge.
