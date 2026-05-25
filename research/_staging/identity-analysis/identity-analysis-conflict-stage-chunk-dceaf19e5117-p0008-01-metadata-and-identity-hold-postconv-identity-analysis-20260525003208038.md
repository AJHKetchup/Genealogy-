---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-dceaf19e5117-p0008-01-metadata-and-identity-hold.md"
worker: postconv-identity-analysis-20260525003208038
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

- Exact staged draft reviewed: `research/_staging/conflicts/chunk-dceaf19e5117-p0008-01-metadata-and-identity-hold.md`.
- Page 8 does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Pulgar-Smith`, `Smith`, `Dario Jose`, `Pulgar-Arriagada`, `Arriagada`, `Jose`, `Juana`, Alexander John Heinz, or any family relationship.
- Attribution to `Dario Arturo Pulgar` is document-level, from `CV of Dario Arturo Pulgar.pdf`, the converted-file title, staged identity candidate, and source packet. It is not a literal page-body name reading.
- The staged draft and source packet cite `CHUNK-dceaf19e5117-P0008-01`, converted SHA `dceaf19e511728a6cacce6d03293232ed56641d0485aa2eabf44020e36edc942`, and page-8 chunk path `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0008-chunk-01.md`.
- Current workspace check found the cited page-8 chunk path absent. The current chunk directory has page 4, 5, 6, 7, and 9 chunks, but no page 8 chunk. The current chunk manifest records converted SHA `b2e036516c17cf6c253a84554ca9fccd71944e51ff46121a8549b9ec6904a7a3`, while the staged draft reports earlier live hashes and older `7bf5ff6de7d9` lineage.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns against automatic merge/attachment for similarly named Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith records.

## Literal Source Readings

The staged draft and source packet support these page-8 work-history readings:

- `1979 - 1982`: United Nations Centre for Human Settlements (HABITAT), Nairobi, Kenya, Development Support Communications Officer.
- `1974 - 1978`: National Film Board of Canada (NFB), Montreal, Canada, Audio Visual Consultant.
- `1972 - 1973`: Chile Films, Santiago, Chile, General Manager Distribution and Exhibition, Head of International Department.
- `1970 - 1972`: Cine, Television y Comunicaciones (CITELCO), Santiago, Chile, Producer.

The converted Markdown also contains the same page-8 sequence and a final `EDUCATION` heading. This supports work-history content only. It does not state birth, death, parent, spouse, child, sibling, grandparent, household, or other kinship data.

## Hypothesis 1: Document-Level CV Evidence For Dario Arturo Pulgar

Supporting evidence:

- The source title/path is `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The source packet states that page 8 continues Dario Arturo Pulgar's CV work history.
- The converted file title is `CV of Dario Arturo Pulgar pages 4-9`.
- The visible page-8 content is occupational chronology consistent with a CV continuation.

Conflicts and cautions:

- Page 8 itself does not name the CV subject.
- The cited current page-8 chunk is missing.
- The staged SHA/chunk lineage and current manifest do not agree.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.76 | Probable document-level attribution; no page-body name. |
| conflict_severity | 0.66 | Provenance conflict blocks reliable citation/promotion. |
| evidence_quality | 0.58 | Useful staged and converted text, weakened by missing chunk. |
| conversion_confidence | 0.50 | Text is readable in derivatives, but chunk/hash state is unresolved. |
| claim_probability | 0.78 | Probable after conversion QA as document-level CV evidence. |
| relevance | 0.95 | Directly relevant to the assigned staged draft. |
| canonical_readiness | 0.20 | Hold until conversion/provenance QA is complete. |

## Hypothesis 2: Same Person As Dario Arturo Pulgar-Smith

Supporting evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` names `Dario Arturo Pulgar-Smith`.
- The staged draft lists that canonical page as a candidate.
- `Dario Arturo Pulgar` overlaps strongly with the canonical preferred name except for `Smith`.

Conflicts and cautions:

- Page 8 does not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, family position, birth/death data, spouse, child, or any other identity bridge.
- The canonical page is family-supplied and cautions against automatic attachment of similarly named Pulgar records.
- A document-title `Dario Arturo Pulgar` attribution cannot by itself prove the `Pulgar`/`Pulgar-Smith` name variant.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Plausible local candidate, but unproved by this page. |
| conflict_severity | 0.72 | False canonical attachment would be material. |
| evidence_quality | 0.42 | Name overlap only, no bridge on page 8. |
| conversion_confidence | 0.50 | Conversion state still blocks page-level promotion. |
| claim_probability | 0.45 | Active hypothesis, not a conclusion. |
| relevance | 0.96 | This is the staged canonical candidate. |
| canonical_readiness | 0.05 | Not ready from this page alone. |

## Hypothesis 3: Same Person As Dario Jose Pulgar-Arriagada

Supporting evidence:

- The Pulgar-line instruction requires comparison because the workspace contains Pulgar-Arriagada identity clusters.
- There is broad Dario/Pulgar name-family overlap only.

Conflicts and cautions:

- Page 8 does not state `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, parents, spouse, residence, age, birth information, or another marker linking the CV subject to a Pulgar-Arriagada person.
- Existing Jose/Juana and Pulgar-Arriagada evidence belongs to separate staged/canonical clusters and cannot be imported by family-context hint alone.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Name-family overlap only. |
| conflict_severity | 0.78 | High same-name conflation risk. |
| evidence_quality | 0.20 | No direct support in page 8. |
| conversion_confidence | 0.50 | Page-8 QA issue does not create this bridge. |
| claim_probability | 0.08 | Unsupported by assigned evidence. |
| relevance | 0.84 | Required anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not merge or promote. |

## Hypothesis 4: Same Person As Dario/Dario Pulgar Arriagada

Supporting evidence:

- Existing wiki context includes `wiki/people/dar-o-pulgar-arriagada.md`, a separate Dario Pulgar Arriagada identity cluster.
- There is broad Dario/Pulgar name-family overlap only.

Conflicts and cautions:

- Page 8 does not state `Arriagada`, a property/legal notice, Chiguayante, an address, age, relatives, or any other bridge to that cluster.
- The page-8 work history concerns 1970-1982 communications, film, and development roles.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Broad name overlap only. |
| conflict_severity | 0.76 | High duplicate-person/conflation risk. |
| evidence_quality | 0.18 | No direct bridge. |
| conversion_confidence | 0.50 | Conversion state remains unrelated to this identity. |
| claim_probability | 0.06 | Unsupported by assigned evidence. |
| relevance | 0.82 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Preserve separately. |

## Hypothesis 5: Jose/Juana Parent Candidates Are Implicated

Supporting evidence:

- Existing wiki context includes Jose/Juana Pulgar-line candidates such as `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and cautions:

- Page 8 contains no parent names, no birth record, no household, no spouse, no child, and no Jose/Juana text.
- Existing Jose/Juana candidates are tied to other records and children, not this CV page.
- Family-context hints can justify a later double-check only after a separate identity-bearing bridge; they cannot supply a relationship here.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.00 | No parent evidence on page 8. |
| conflict_severity | 0.58 | Unsupported parent inference would be misleading. |
| evidence_quality | 0.05 | No relevant literal support. |
| conversion_confidence | 0.50 | Conversion state does not create relationship evidence. |
| claim_probability | 0.00 | Not supported. |
| relevance | 0.65 | Required anti-conflation check. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person/name-variant risk: high if `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, and Jose/Juana parent clusters are merged by name or family context alone.
- Relationship conflict: no relationship is stated on page 8.
- Chronology conflict: no internal conflict in the 1970-1982 work-history sequence; cross-cluster chronology comparison is unsafe until identity bridges are proof-reviewed.
- Conversion/provenance conflict: material blocker because the staged draft, source packet, current manifest, and current chunk directory do not agree.

## Ranked Outcome

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Page 8 is document-level work-history evidence for `Dario Arturo Pulgar`. | 0.78 | Reconcile converted/chunk/hash lineage and restore or regenerate a current page-8 chunk. |
| 2 | CV subject may be canonical `Dario Arturo Pulgar-Smith`. | 0.45 | Run identity-bridge proof review using an identity-bearing CV page or accepted local bridge. |
| 3 | Same as `Dario Jose Pulgar-Arriagada`. | 0.08 | Preserve separately; require direct identity anchors. |
| 4 | Same as `Dario/Dario Pulgar Arriagada`. | 0.06 | Preserve separately; require direct identity anchors. |
| 5 | Supports Jose/Juana parent candidates. | 0.00 | No parent or relationship action from this page. |

## Recommended Next Action

Keep the staged draft on `hold_for_conversion_qa`. Do not promote the page-8 work-history claims and do not attach them to `wiki/people/dario-arturo-pulgar-smith.md` yet.

Exact next proof-review or promotion step: perform conversion/provenance QA for `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md` and the chunk manifest; reconcile the conflicting SHA/chunk lineage; restore or regenerate `page-0008-chunk-01.md`; and proof-review page 8 against the source PDF/page image. Only after that should a separate identity-bridge proof review decide whether document-level `Dario Arturo Pulgar` attaches to canonical `Dario Arturo Pulgar-Smith`. Keep Pulgar-Arriagada and Jose/Juana parent candidates separate unless a direct, proof-reviewed bridge names compatible identity anchors.
