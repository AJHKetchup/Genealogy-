---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260524192430696
task_id: "identity-analysis:research/_staging/conflicts/chunk-7bf5ff6de7d9-p0008-01-no-conflict-candidate.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-7bf5ff6de7d9-p0008-01-no-conflict-candidate.md"
source_packet: "research/_staging/source-packets/chunk-7bf5ff6de7d9-p0008-01-cv-dario-arturo-pulgar-work-history.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0008-chunk-01.md"
chunk_id: "CHUNK-7bf5ff6de7d9-P0008-01"
page_reference: "page 8"
analysis_status: hold
canonical_readiness: hold_for_identity_bridge_and_proof_review
---

# Identity/Conflict Analysis: CHUNK-7bf5ff6de7d9-P0008-01

## Blockers First

- This note analyzes exactly `research/_staging/conflicts/chunk-7bf5ff6de7d9-p0008-01-no-conflict-candidate.md` and its referenced local context. No external research was performed.
- Page 8 does not print a personal name in the literal body. Attribution to `Dario Arturo Pulgar` comes from the source title/path, source packet, converted-file title, and CV continuity, not from the page text itself.
- The current chunk file path referenced by the draft has front-matter drift: its body is page 8 of the CV, but the chunk front matter now records `chunk_id: CHUNK-8a2aa5e638cf-P0008-01` and `converted_sha256: 8a2aa5e...`, while the staged draft/source packet use `CHUNK-7bf5ff6de7d9-P0008-01` and `converted_sha256: 7bf5ff6d...`. Treat this as a proof-review metadata blocker before canonical promotion.
- Page 8 supports a work-history chronology, not a relationship, birth, death, parentage, spouse, child, or grandchild claim.
- The page does not state `Pulgar-Smith`, `Smith`, `Dario Jose`, `Dario J.`, `Pulgar-Arriagada`, `Dario Pulgar A.`, any Jose/Juana parent candidate, or any relationship to Alexander John Heinz.
- Existing canonical `wiki/people/dario-arturo-pulgar-smith.md` warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records should be attached only after identity review. This page alone is not that bridge.
- Do not promote the staged conflict draft as a genealogy fact. Keep it as a QA/identity-scope marker.

## Literal Source Reading

Staged conflict draft:

- Type: `conflict_candidate`.
- Subject: `Dario Arturo Pulgar work-history chronology on CV page 8`.
- Conflict type: `no_internal_conflict_noted`.
- Literal support: non-overlapping dated entries for 1979-1982 HABITAT, 1974-1978 NFB, 1972-1973 Chile Films, and 1970-1972 CITELCO.
- Recommendation: `do_not_promote`.

Referenced source packet:

- `research/_staging/source-packets/chunk-7bf5ff6de7d9-p0008-01-cv-dario-arturo-pulgar-work-history.md`.
- Source identity: `Dario Arturo Pulgar`, identified by the source title and CV continuity.
- Conversion confidence: high; the packet says the converted chunk reports complete transcription and no uncertain or illegible text.
- QA concern: final proofing should verify page continuity, role titles, place names, and accented Spanish names.

Referenced chunk:

- `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0008-chunk-01.md`.
- Literal transcription gives:
  - `1979 - 1982`, United Nations Centre for Human Settlements (HABITAT), Nairobi, Kenya, Development Support Communications Officer.
  - `1974 - 1978`, National Film Board of Canada (NFB), Montreal, Canada, Audio Visual Consultant.
  - `1972 - 1973`, Chile Films, Santiago, Chile, General Manager Distribution and Exhibition, Head of International Department.
  - `1970 - 1972`, Cine, Television y Comunicaciones (CITELCO), Santiago, Chile, Producer.
- The page ends with `EDUCATION`.
- The chunk says there are no uncertain or illegible words and that the page is transcribed in full.

Interpretation kept separate: the page is strong typed CV work-history evidence for the document-level subject after proof review confirms continuity. It is weak standalone identity evidence and does not itself resolve canonical attachment.

## Hypothesis 1: Page 8 Belongs To Document-Level CV Subject Dario Arturo Pulgar

Evidence supporting:

- The source path is `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The source packet states that page 8 continues the curriculum vitae of `Dario Arturo Pulgar`.
- The converted file title is `CV of Dario Arturo Pulgar pages 4-9`.
- The page layout is a coherent reverse-chronological CV work-history continuation.
- There is no competing personal name or conflicting chronology in the page body.

Evidence limiting:

- The literal page body is unnamed.
- The current chunk front matter has chunk-id/hash drift against the staged draft/source packet.
- A proof reviewer still needs to confirm page continuity and page-image/source-PDF correspondence.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong document-level attribution, but no page-local name and metadata drift requires review. |
| conflict_severity | 0.16 | No internal conflict; risk is over-attachment. |
| evidence_quality | 0.72 | Clear typed CV text plus source-packet context, limited by document-level identity. |
| conversion_confidence | 0.82 | Text reports complete transcription; metadata drift and final image review remain blockers. |
| claim_probability | 0.84 | Work entries probably belong to the local CV subject. |
| relevance | 0.98 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.36 | Ready only for proof review, not canonical promotion. |

## Hypothesis 2: Same Person As Canonical Dario Arturo Pulgar-Smith

Evidence supporting:

- `Dario Arturo Pulgar` and `Dario Arturo Pulgar-Smith` share the distinctive given-name pair and `Pulgar` surname element.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is the known family-supplied maternal-grandfather page in this line.
- Existing local CV tasks identify `Dario Arturo Pulgar-Smith` as the likely canonical candidate to test.

Evidence limiting:

- Page 8 does not state `Smith` or `Pulgar-Smith`.
- Page 8 does not state Alexander John Heinz, a grandchild relationship, or any family relationship.
- Family-supplied context can prompt bridge review but cannot silently convert `Pulgar` into `Pulgar-Smith`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Plausible name overlap, but unproved by page 8. |
| conflict_severity | 0.40 | Wrong attachment would assign a substantial career chronology to the wrong person. |
| evidence_quality | 0.52 | Mainly name/context overlap plus canonical family-supplied anchor. |
| conversion_confidence | 0.82 | The page text is readable but not identity-bridging. |
| claim_probability | 0.57 | Possible, not proven. |
| relevance | 0.96 | Central candidate for future promotion. |
| canonical_readiness | 0.18 | Hold for identity-bridge proof review. |

## Hypothesis 3: Same Person As Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada / Dario Pulgar A.

Evidence supporting:

- The broader workspace contains staged and canonical Pulgar-line records with name forms such as `Dario Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, and `Dario Pulgar A.`.
- These clusters share broad `Dario` and `Pulgar` elements.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` contains a separate life-fact snapshot for `Dario Pulgar Arriagada`.

Evidence limiting:

- Page 8 does not state `Jose`, `J.`, `Arriagada`, or `Pulgar A.`.
- Page 8 describes communications and film work from 1970-1982, not a medical-service, diplomatic, passenger, birth-register, or 2000 property/expropriation context.
- Name overlap alone is not sufficient and creates a high duplicate-person/merged-generation risk.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Broad name overlap only. |
| conflict_severity | 0.78 | Name-only merging could collapse distinct Pulgar clusters. |
| evidence_quality | 0.48 | Comparison context exists but is separate from this page. |
| conversion_confidence | 0.50 | Page 8 is clear; compared clusters have independent review status. |
| claim_probability | 0.10 | Low from this staged draft. |
| relevance | 0.86 | Required anti-conflation comparison. |
| canonical_readiness | 0.03 | Do not merge or attach. |

## Hypothesis 4: Direct Relationship To Jose/Juana Parent Candidates

Evidence supporting:

- Existing Pulgar-line context includes Jose/Juana candidates such as `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Those names are relevant to Pulgar-line anti-conflation checks.

Evidence limiting:

- Page 8 contains no Jose or Juana name.
- Page 8 contains no parent, mother, father, spouse, child, household, lineage, birth-register, or declarant language.
- Existing Jose/Juana records are separate source clusters and cannot be used to infer page-8 identity or relationships.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No direct bridge appears. |
| conflict_severity | 0.60 | Premature lineage attachment would create unsupported relationships. |
| evidence_quality | 0.38 | Relevant only as exclusionary context. |
| conversion_confidence | 0.40 | Jose/Juana readings have separate QA histories; page 8 itself is not about them. |
| claim_probability | 0.04 | Not supported by this page. |
| relevance | 0.60 | Anti-conflation only. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`; high if merged by name alone with Pulgar-Arriagada clusters.
- Name-variant conflict: page 8 supports only document-level `Dario Arturo Pulgar`; it does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.` as variants.
- Relationship-conflict evidence: none. No parent, spouse, child, grandchild, Jose/Juana candidate, or Alexander John Heinz relationship appears on page 8.
- Chronology-conflict evidence: none within the page-8 work sequence. The dated entries are sequential/non-overlapping: 1970-1972, 1972-1973, 1974-1978, 1979-1982.
- Conversion/metadata conflict: the page text appears stable, but the staged `7bf5ff6de7d9` identifiers differ from the current chunk front matter's `8a2aa5e638cf` identifiers. Resolve before promotion.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Canonical Readiness | Required Next Step |
| ---: | --- | ---: | ---: | --- |
| 1 | Page 8 belongs to document-level CV subject `Dario Arturo Pulgar`. | 0.84 | 0.36 | Proof review page continuity, source image/PDF, and metadata drift. |
| 2 | CV subject is same person as canonical `Dario Arturo Pulgar-Smith`. | 0.57 | 0.18 | Separate identity-bridge proof review from an identity-bearing CV page or accepted local bridge source. |
| 3 | CV subject belongs to a staged Dario Pulgar work-history/Habitat cluster but remains unpromoted. | 0.55 | 0.16 | Review the identity-bearing Habitat/CV bridge evidence together before canonical attachment. |
| 4 | Same person as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`. | 0.10 | 0.03 | Do not merge; require an explicit proof-reviewed bridge naming compatible identity anchors. |
| 5 | Directly linked to Jose/Juana parent candidates. | 0.04 | 0.01 | No action from this page; keep as anti-conflation context only. |

## Recommended Next Action

Hold the staged conflict draft as a valid `no internal conflict noted` QA marker. Do not promote it as a canonical conflict or biography fact.

Next proof-review step: reconcile the staged `CHUNK-7bf5ff6de7d9-P0008-01` identifiers with the current chunk front matter, confirm page 8 against the rendered PDF/page image, and review an identity-bearing CV page that explicitly connects the CV subject `Dario Arturo Pulgar` to any canonical person. Only after that should the 1970-1982 occupational entries be considered for promotion, especially to `wiki/people/dario-arturo-pulgar-smith.md`.
