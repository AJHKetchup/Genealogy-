---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/chunk-7d3991a78bc8-p0001-01-entry-172-identity-candidates.md
staged_draft: research/_staging/identity/chunk-7d3991a78bc8-p0001-01-entry-172-identity-candidates.md
source_packet: research/_staging/source-packets/chunk-7d3991a78bc8-p0001-01-entry-172-image-reread-pulgar-arriagada.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md
chunk_id: CHUNK-7d3991a78bc8-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Identity Candidates

## Blockers

- The staged identity draft and source packet report an image-reviewed Pulgar/Arriagada reading for entry 172, but the assigned converted Markdown and chunk still transcribe the same entry as a Bunster/de la Maza birth. This is a controlling conversion conflict.
- No person merge, canonical attachment, or fact promotion should proceed from `CHUNK-7d3991a78bc8-P0001-01` until conversion QA corrects, supersedes, or retires the derivative Bunster/de la Maza reading.
- The father is readable in the source packet as `Jose del Carmen Pulgar`, but any final suffix or additional name component remains unclear. Do not normalize this to `Jose del Carmen Pulgar S.` or merge him with other Jose Pulgar candidates without a targeted parent-identity proof review.
- The mother in this draft is `Juana Arriagada de Pulgar`. Existing local context also has `Juana de Dios Amagada de Pulgar` and other `Juana de Dios ... de Pulgar` readings. Those are not silently equivalent.
- This entry does not name Dario. It cannot by itself bridge `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar` to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth

Hypothesis: Entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`; the Bunster/de la Maza cluster is a derivative transcription or row-assignment error.

Literal source readings:

- Staged draft: image-reviewed candidate child is `Jose del Carmen Segundo Pulgar Arriagada`; father candidate is `Jose del Carmen Pulgar`; mother candidate is `Juana Arriagada de Pulgar`; informant is `Ernesto Herrera L.`; official is `Emilio Riquelme V.`
- Source packet: the image reread supports registration date 7 April 1888, birth date/time 8 March 1888 at 3 p.m., birthplace `Calle de Valdivia`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- Existing canonical context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` and `wiki/people/juana-arriagada-de-pulgar.md` already contain prior entry-172 Pulgar/Arriagada evidence, but those pages depend on earlier staging and should not be expanded from this conflicted derivative until QA is complete.

Interpretation:

- This is the leading identity hypothesis because the image-reviewed draft and source packet directly support the Pulgar/Arriagada cluster.
- The conclusion remains staged, not promotion-ready, because the assigned derivative text has not been reconciled.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.88 | Strong for the image-reviewed entry-172 identity cluster; reduced by the unreconciled derivative contradiction. |
| conflict_severity | 0.92 | Competing readings disagree on child, parents, birth date/time, birthplace, informant, and official. |
| evidence_quality | 0.82 | Civil birth register image reread is strong, but this note relies on staged/reviewed local evidence and does not perform new conversion. |
| conversion_confidence | 0.35 | Low for the assigned derivative transcript while it conflicts with the image reread. |
| claim_probability | 0.86 | High probability that Pulgar/Arriagada is the correct entry-172 cluster. |
| relevance | 0.96 | Critical to Pulgar-line parent-child staging and false-positive prevention. |
| canonical_readiness | 0.18 | Hold for conversion QA before promotion or canonical expansion. |

## Hypothesis 2: Entry 172 Is The Bunster/de la Maza Birth

Hypothesis: Entry 172 records `Jose Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`; the Pulgar/Arriagada reading belongs to another row, page, or source assignment.

Literal source readings:

- Converted Markdown and assigned chunk transcribe entry 172 as `Jose Miguel`, male, born 26 March 1888 at 10 p.m., father `Oswaldo Bunster`, mother `Amelia de la Maza`, informant `Oswaldo Bunster`, official `Camilo Luis osorio`.
- The staged identity draft labels this as literal only in the assigned derivative text and states that the source image does not support that identity cluster for entry 172.

Interpretation:

- This is a weak hypothesis under current staged evidence. It should be retained only as a conversion-conflict hypothesis until QA determines whether the derivative transcript has a row/source assignment problem.
- Do not create or promote Bunster/de la Maza people from this source while this conflict remains unresolved.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.22 | Supported by disputed derivative text only. |
| conflict_severity | 0.92 | Acceptance would reverse every core Pulgar/Arriagada identity claim. |
| evidence_quality | 0.30 | Derivative support is contradicted by image-reviewed staging. |
| conversion_confidence | 0.20 | Current conversion confidence for this reading is poor. |
| claim_probability | 0.16 | Plausible only if the image-reread assignment is later shown wrong. |
| relevance | 0.70 | Relevant as a guardrail against false promotion. |
| canonical_readiness | 0.02 | Not ready; do not promote. |

## Hypothesis 3: Entry 172 Parents Match Other Jose/Juana Pulgar Candidates

Hypothesis: The father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar` may be the same parent couple, or partly the same parent cluster, as other local Jose/Juana Pulgar candidates.

Literal source readings:

- Entry 172 source packet names father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- `wiki/people/jose-del-carmen-pulgar.md` has a draft child link to `Tulio Cesar Luis Jose` from another staged relationship, not from this exact staged draft.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` has a draft child link to `Tulio Cesar Luis Jose`; this is not the same literal name as `Juana Arriagada de Pulgar`.
- Local conversion-review notes for other entries mention father `Jose del Carmen Pulgar` and a mother line beginning `Juana de Dios ... de Pulgar`, with maternal surname uncertainty.

Interpretation:

- The repeated father name is enough to justify a targeted identity review, especially if ages, residences, occupations, and child chronology align after QA.
- The mother names are not yet equivalent. `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and any `Juana de Dios ... de Pulgar` candidate must remain distinct unless a proof-review note resolves the literal surname/given-name variants and explains the identity bridge.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.54 | Plausible father-name overlap; weaker mother-name equivalence. |
| conflict_severity | 0.55 | Premature parent merging could combine separate families. |
| evidence_quality | 0.58 | Useful local staged/canonical context, but incomplete identity bridge. |
| conversion_confidence | 0.40 | Entry 172 is blocked; related Jose/Juana entries also contain QA-sensitive readings. |
| claim_probability | 0.50 | Possible but unresolved by this entry alone. |
| relevance | 0.84 | Important for Pulgar-line structure and duplicate-person control. |
| canonical_readiness | 0.12 | Hold for parent-candidate proof review. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merging with similarly named Pulgar records. Entry 172 does not name Dario Arturo or Pulgar-Smith.
- `Dario Arturo Pulgar`: Existing staged CV context concerns a document-level Dario Arturo Pulgar identity. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar.
- `Dario Jose Pulgar-Arriagada`: Existing staged photograph/context material names Dario Jose Pulgar-Arriagada. Entry 172 shares Pulgar/Arriagada surname elements but has a different given-name string and no Dario evidence.
- `Dario/Darío Pulgar Arriagada`: Existing canonical context has a `Darío Pulgar Arriagada` event in 2000. Entry 172 is an 1888 birth registration for a child named Jose del Carmen Segundo, so it is not direct evidence for that Dario identity.
- Ranked identity impact: (1) direct: `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`; (2) indirect Pulgar-line context: other Jose/Juana parent candidates; (3) no present merge basis: any Dario identity cluster.

## Conflicts

- Same-entry conflict: Pulgar/Arriagada image-reread cluster versus Bunster/de la Maza derivative cluster. Severity: critical.
- Duplicate-person risk: high if Bunster/de la Maza candidates are promoted from this source; moderate if Jose/Juana parent candidates are merged across entries without proof review.
- Name-variant risk: moderate for `Jose del Carmen Pulgar` versus possible suffix variants; moderate for `Juana Arriagada de Pulgar` versus `Juana de Dios ... de Pulgar`; low for Dario variants within this entry because no Dario name appears.
- Relationship-conflict risk: high until conversion QA confirms which entry-172 reading controls.
- Chronology-conflict risk: low inside the Pulgar/Arriagada reading; high between competing readings because they give different birth dates and places.

## Recommended Next Action

Keep `research/_staging/identity/chunk-7d3991a78bc8-p0001-01-entry-172-identity-candidates.md` on `hold_for_conversion_qa`.

Exact next proof-review or promotion step: perform conversion QA reconciliation for `CHUNK-7d3991a78bc8-P0001-01`, correcting or retiring the Bunster/de la Maza derivative transcript if the source image controls as `Jose del Carmen Segundo Pulgar Arriagada`; also settle whether the father has a visible suffix after `Jose del Carmen Pulgar`.

After conversion QA, run focused proof review for the entry-172 child identity, birth event, father relationship, mother relationship, and parent-candidate identity question. Do not attach this entry to any Dario identity unless a later identity-bridging source supplies direct evidence.
