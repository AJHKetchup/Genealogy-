---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525065839058
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Identity Conflict Analysis: Entry 172 Conversion Conflict

## Blockers

- Canonical promotion is blocked. The exact staged draft under review is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md`, and it reports a row-level conflict between the assigned converted Markdown and the assigned chunk/source-packet evidence.
- The assigned chunk/source packet identify entry 172 as the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`; the assigned converted Markdown currently records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 20 February 1888 in `Pellin`. This is a different identity cluster, not a spelling or name-variant issue.
- The father field inside the Pulgar/Arriagada row remains unresolved at the literal-reading level. Preserve all three readings until conversion QA: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- Do not merge the entry-172 father candidate with the existing `Jose del Carmen Pulgar` wiki page by name alone. The wiki page also carries a separate draft child link to `Tulio Cesar Luis Jose` from an entry-513 cluster, and that cluster has its own mother-surname and conversion limits.
- Do not merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` by family context or married-name similarity. Entry 172 supports `Juana Arriagada de Pulgar`; entry 513 context preserves `Juana de Dios Amagada/Amador/... de Pulgar` as a separate unresolved parent candidate.
- No Dario identity, Dario relationship, or Pulgar-line descent bridge is supported by this entry. The source row names no `Dario`, `Arturo`, `Smith`, `Jose` as a Dario middle name, medical title, passenger context, expropriation context, spouse, child, grandchild, or lineage statement.

## Literal Source Readings

- Staged conflict draft: entry 172 should be treated as a material row-level conversion conflict and held for conversion QA.
- Source packet for this task: the current chunk entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Assigned chunk: page 58, entry 172 gives registration date `Siete de Abril de mil ochocientos ochenta i ocho`, child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth date/time `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, birthplace `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- Assigned converted Markdown: page 58, entry 172 gives a different row: `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 20 February 1888 at 10 p.m. in `Pellin`.
- Prior reviewed notes in local staging preserve the same broad conflict and repeatedly require targeted conversion QA. Some older local notes report different wrong-row converted names; that variation reinforces that the derivative conversion state is unstable and should not control identity promotion.

## Interpretation Guardrails

- The civil birth-register source class would be strong evidence for birth identity and declared parent relationships after the controlling row is settled.
- In the current state, the strongest supported interpretation is not a promoted family fact; it is a hold-level conclusion that the Pulgar/Arriagada row is probable from the chunk/source-packet context but blocked by the assigned converted Markdown mismatch.
- Family-context hints may justify checking whether this Jose/Juana couple relates to later Pulgar-line Dario candidates, but they do not justify silent correction, merge, or canonical attachment.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Evidence supporting:

- The staged draft and source packet agree that the current chunk supports `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
- The chunk gives coherent same-row birth, registration, parent, residence, informant, and official details for the Pulgar/Arriagada entry.
- Earlier local proof-review notes judged the Pulgar/Arriagada row probable but blocked by conversion QA.

Evidence against or limiting:

- The assigned converted Markdown records an entirely different entry-172 identity cluster.
- The father-name suffix remains unresolved.

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.76 | Probable row identity from chunk/source-packet agreement, reduced by converted-file conflict. |
| conflict_severity | 0.92 | Different child, parents, birth date, and place. |
| evidence_quality | 0.86 | Civil register evidence class is strong once transcription is stable. |
| conversion_confidence | 0.42 | Derivative conversion and chunk disagree at row level. |
| claim_probability | 0.82 | Probable as a hold-level row-identification claim, not a promoted fact. |
| relevance | 0.95 | Directly relevant to Pulgar/Arriagada parent candidates. |
| canonical_readiness | 0.18 | Hold for conversion QA. |

## Hypothesis 2: Entry 172 Is The Converted-File Non-Pulgar Row

Evidence supporting:

- The assigned converted Markdown currently transcribes entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, with a Pellin birth event.

Evidence against or limiting:

- The staged draft, source packet, chunk, and prior local review context treat this as the conflicting row, not the controlling Pulgar/Arriagada row.
- The non-Pulgar row has no name, parent, residence, or chronology overlap with the Pulgar/Arriagada child-parent cluster except the entry number and same registration date context.

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | It is a real derivative transcript reading, but weak as the identity for this staged Pulgar/Arriagada task. |
| conflict_severity | 0.92 | Mutually exclusive row-level identity facts. |
| evidence_quality | 0.45 | Converted Markdown is derivative and contradicted by the assigned chunk/source packet. |
| conversion_confidence | 0.30 | This is the conflict source. |
| claim_probability | 0.20 | Low probability as the correct identity for this Pulgar/Arriagada staged task. |
| relevance | 0.80 | Relevant as the blocking conflict. |
| canonical_readiness | 0.05 | Do not promote. |

## Hypothesis 3: Father Candidate Is `Jose del Carmen Pulgar`

Evidence supporting:

- The chunk father field reads `Jose del Carmen Pulgar S.`, and the source packet preserves the alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- The existing `wiki/people/jose-del-carmen-pulgar.md` page has the same core name, but currently only shows a separate draft child link to `Tulio Cesar Luis Jose`.

Evidence against or limiting:

- The exact final suffix or mark after `Pulgar` is unresolved.
- Same-name overlap is not enough to merge the entry-172 father candidate with the existing Jose page or with the entry-513 father/declarant candidate.
- The entry-172 father has Pulgar/Arriagada context; the entry-513 cluster has separate unresolved mother-surname and child-name issues.

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Strong for the core father name in entry 172, lower for matching any existing Jose page. |
| conflict_severity | 0.58 | Suffix and cross-entry same-person risk are meaningful but not row-destroying. |
| evidence_quality | 0.78 | Direct register parent field, blocked by conversion disagreement. |
| conversion_confidence | 0.44 | Father suffix and converted-file mismatch remain unresolved. |
| claim_probability | 0.72 | Core father-name lead is probable; exact canonical identity is not. |
| relevance | 0.92 | Central parent candidate. |
| canonical_readiness | 0.20 | Hold until QA and proof review. |

## Hypothesis 4: Mother Candidate Is `Juana Arriagada de Pulgar`

Evidence supporting:

- The staged draft, source packet, and chunk all name the mother as `Juana Arriagada de Pulgar`.
- The existing `wiki/people/juana-arriagada-de-pulgar.md` page already carries a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from this entry-172 cluster.

Evidence against or limiting:

- Canonical attachment remains unsafe while the entry-level converted Markdown points to another family.
- `Juana Arriagada de Pulgar` should not be silently normalized into or merged with `Juana de Dios Amagada de Pulgar`; those are different staged name forms from different entry clusters.

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Strong within the chunk/source-packet row, blocked by conversion conflict. |
| conflict_severity | 0.64 | Main risk is cross-cluster Juana conflation plus row-level conversion mismatch. |
| evidence_quality | 0.80 | Direct mother field in a civil register row. |
| conversion_confidence | 0.44 | Converted-file mismatch prevents promotion. |
| claim_probability | 0.78 | Probable as a staged mother candidate, not promotion-ready. |
| relevance | 0.94 | Central parent candidate. |
| canonical_readiness | 0.22 | Hold until QA and proof review. |

## Hypothesis 5: Same As Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Evidence supporting:

- Existing wiki context preserves a family-supplied canonical person `Dario Arturo Pulgar-Smith`, and local staged CV/Habitat work discusses a separate `Dario Arturo Pulgar` or `Dario Pulgar` work-history cluster.
- Pulgar-line context makes this entry worth preserving as a possible ancestor-line lead after proof review.

Evidence against or limiting:

- Entry 172 names no `Dario`, `Arturo`, `Smith`, `Pulgar-Smith`, grandchild, spouse, child of Dario, or other identity bridge.
- The canonical Dario page explicitly warns not to attach similarly named Pulgar/Pulgar-Arriagada records without identity review.
- A 1888 child named `Jose del Carmen Segundo Pulgar Arriagada` cannot be treated as Dario Arturo by name evidence from this entry.

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No direct identity bridge to Dario Arturo or Pulgar-Smith. |
| conflict_severity | 0.78 | High duplicate-person risk if attached by surname/family context alone. |
| evidence_quality | 0.30 | Evidence is contextual only for this hypothesis. |
| conversion_confidence | 0.42 | Underlying entry still blocked by QA. |
| claim_probability | 0.04 | Not supported from this source. |
| relevance | 0.70 | Required Pulgar-line anti-conflation check. |
| canonical_readiness | 0.00 | Do not attach or merge. |

## Hypothesis 6: Same As Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, Dario Pulgar-Arriagada, Dario Pulgar Arriagada, Or Dario Pulgar A.

Evidence supporting:

- Local context contains separate staged and canonical Dario/Pulgar/Arriagada candidates, including `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar A.`, and canonical `Darío Pulgar Arriagada`.
- The entry-172 child has the surnames `Pulgar Arriagada`, which makes this a legitimate anti-conflation checkpoint.

Evidence against or limiting:

- Entry 172 does not name Dario in any form.
- Entry 172 does not provide medical, military-health-service, Geneva, passenger, property, expropriation, or adult chronology anchors.
- Existing proof-review notes for `Dario J. Pulgar Arriagada` warn against expanding `J.` or merging Dario clusters without separate bridge evidence.

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.07 | Only surname overlap; no given-name or chronology bridge. |
| conflict_severity | 0.82 | High risk of false merge across Dario/Pulgar/Arriagada clusters. |
| evidence_quality | 0.28 | Contextual comparison only. |
| conversion_confidence | 0.42 | Entry-level QA remains unresolved. |
| claim_probability | 0.05 | Not supported from this entry. |
| relevance | 0.78 | Required Pulgar-line anti-conflation check. |
| canonical_readiness | 0.00 | Do not attach or merge. |

## Hypothesis 7: Jose/Juana Parent Candidates Across Entry 172 And Entry 513 Are The Same Couple

Evidence supporting:

- Local wiki and staging include `Jose del Carmen Pulgar` and two Juana married-name candidates in Pulgar birth-register contexts.
- Entry 172 and entry 513 both involve a father candidate named `Jose del Carmen Pulgar` or abbreviation-compatible forms.

Evidence against or limiting:

- Entry 172 mother is `Juana Arriagada de Pulgar`; entry 513 context preserves `Juana de Dios Amagada de Pulgar` or conflicting/uncertain variants.
- Entry 172 and entry 513 are separate register entries with separate child candidates and separate conversion/proof-review issues.
- No current reviewed note proves that `Juana Arriagada de Pulgar` equals `Juana de Dios Amagada de Pulgar`, or that both entries share the same parental couple.

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.36 | Possible for Jose; weak for the Juana/couple identity. |
| conflict_severity | 0.70 | Mother-name conflict and cross-entry merge risk are substantial. |
| evidence_quality | 0.52 | Multiple local leads, but no settled bridge. |
| conversion_confidence | 0.40 | Both clusters retain conversion sensitivities. |
| claim_probability | 0.30 | Plausible research lead only. |
| relevance | 0.90 | Important for parent-candidate management. |
| canonical_readiness | 0.08 | Hold; do not merge. |

## Conflict Summary

- Same-person conflict: unresolved for the entry-172 father candidate versus existing `Jose del Carmen Pulgar`; unresolved and currently weak for the parent-pair comparison with entry 513.
- Duplicate-person risk: high if `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` are split without QA; also high if the existing Jose page absorbs the entry-172 father without proof review.
- Name-variant conflict: `Jose del Carmen Pulgar S.` may be a suffix/mark variant or a misread; `Juana Arriagada de Pulgar` is not proved to be a variant of `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: child-parent claims for `Jose del Carmen Segundo Pulgar Arriagada` are plausible from the chunk but must stay staged because the converted Markdown records different parents for entry 172.
- Chronology conflict: no internal chronology problem in the Pulgar/Arriagada row, but cross-cluster Dario and entry-513 comparisons have no proved bridge.
- Dario conflict: this entry supplies no same-person evidence for `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar A.`, or canonical `Darío Pulgar Arriagada`.

## Ranked Hypotheses

| rank | hypothesis | probability | required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada` | 0.82 | Targeted conversion QA must reconcile/supersede the converted Markdown against the source image and chunk. |
| 2 | Entry 172 mother candidate is `Juana Arriagada de Pulgar` | 0.78 | After conversion QA, proof-review the mother-name and child-mother relationship before any canonical update. |
| 3 | Entry 172 father candidate is core `Jose del Carmen Pulgar` with unresolved suffix | 0.72 | Conversion QA must record `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`, then proof-review father identity. |
| 4 | Entry-172 Jose/Juana pair overlaps with entry-513 Jose/Juana candidates | 0.30 | Separate identity proof review comparing proof-reviewed entry-172 and entry-513 parent fields; do not merge before both rows are stabilized. |
| 5 | Assigned converted Markdown's non-Pulgar row is the correct row for this staged Pulgar task | 0.20 | Conversion QA should identify whether this is a wrong-row/file-assignment transcript or a superseded conversion. |
| 6 | Same as Dario Jose / Dario J. / Dario Pulgar-Arriagada / Dario Pulgar A. clusters | 0.05 | No promotion step from this entry; revisit only if a proof-reviewed lineage source connects the register child/parents to a Dario candidate. |
| 7 | Same as Dario Arturo Pulgar-Smith or Dario Arturo Pulgar | 0.04 | No promotion step from this entry; require an explicit proof-reviewed identity/lineage bridge. |

## Recommended Next Action

Keep this staged conflict and all dependent child, parent, relationship, and parent-candidate claims at `hold_for_conversion_qa`.

Exact next step: run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`, register page 58, entry 172. QA must decide whether the controlling row is the Pulgar/Arriagada row, reconcile or supersede the assigned converted Markdown, preserve source-visible spellings, and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review on the child identity, birth facts, father claim, mother claim, child-parent relationships, and parental-pair clue. Only after those reviews should any canonical wiki update, parent-candidate merge, or Dario-line bridge review be considered.
