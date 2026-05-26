---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526000138249
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
conflict_type: row_level_conversion_conflict
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold
created: 2026-05-26
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Row-control blocker: the staged conflict draft, referenced source packet, assigned chunk, and current converted Markdown do not agree on the family recorded in entry 172.
- Promotion blocker: do not promote child identity, birth date/time/place, sex, parent names, parent-child relationships, parent identity merges, or Pulgar-line comparisons from this entry until targeted conversion QA decides the controlling entry-172 row.
- Father-name blocker: the assigned chunk reads `Jose del Carmen Pulgar S.`, while the source-packet visual check says only the beginning `Jose del Carmen Pulgar` is clear enough for this pass; QA must decide `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Dario-line blocker: this entry does not name Dario, Arturo, Smith, Dario Jose, Dario J., Dario Pulgar Arriagada, a spouse, or a later descendant. It cannot bridge to any Dario candidate by surname context alone.
- Existing-wiki blocker: canonical stubs already contain generated evidence derived from this entry for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`; those entries should remain treated as dependent on the unresolved conversion conflict, not as independent proof.

## Literal Readings

Assigned chunk/source-packet reading:

- Registration date: 7 April 1888.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: 8 March 1888 at 3 p.m., `Calle de Valdivia`.
- Father: chunk reading `Jose del Carmen Pulgar S.`; visual-review packet holds the suffix unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employee, resident at `Calle de Valdivia`.

Current converted Markdown reading:

- Registration date: 7 April 1888.
- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: 6 April 1888 at 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

Interpretation: these are incompatible row readings. They should not be normalized into one family, one child, or one set of parents.

## Hypotheses

| Rank | Hypothesis | Supporting evidence | Conflicts and limits | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | The staged conflict draft and source packet both report source-image/chunk support for the Pulgar/Arriagada row; the assigned chunk gives matching child, birth, mother, father, and informant details. | The current converted Markdown gives a wholly different Burgos/de la Cruz row; father suffix remains unresolved. | 0.76 |
| 2 | Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | The current converted Markdown directly transcribes entry 172 with `Jose Miguel`, `Oswaldo Burgos`, and `Concepcion de la Cruz`. | The assigned chunk and source-packet visual check contradict this reading for the assigned source image; no Pulgar relevance follows if this row controls. | 0.20 |
| 3 | The converted file/chunk pipeline has a row or page-control mismatch. | The disagreement spans child name, parents, birth date/time, place, and informant, which is larger than a name-variant issue. | Identity analysis cannot fix conversion artifacts; targeted conversion QA is required. | 0.84 |
| 4 | The entry-172 father is the same person as existing `wiki/people/jose-del-carmen-pulgar.md`. | The entry-172 father candidate begins `Jose del Carmen Pulgar`; the wiki has a same-name stub tied to another child, `Tulio Cesar Luis Jose`. | Same name is insufficient; the other wiki evidence appears tied to a different register entry and a different Juana candidate. | 0.34 |
| 5 | The entry-172 mother is existing `wiki/people/juana-arriagada-de-pulgar.md`. | The assigned chunk/source packet name `Juana Arriagada de Pulgar`, and the wiki stub already contains entry-172-derived generated evidence. | The wiki evidence is not independent of this disputed entry; still blocked by row-control QA. | 0.68 |

## Pulgar-Line Comparison

`Dario Arturo Pulgar-Smith`: the canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly cautions against attaching similarly named records without identity review. Entry 172 does not name Dario Arturo Pulgar-Smith, Smith, Alexander John Heinz, or a descendant chain. Same-person probability from this entry alone: 0.01.

`Dario Arturo Pulgar`: staged CV context supports a document-level CV subject named `Dario Arturo Pulgar`, but entry 172 is an 1888 birth-register row for either a Pulgar/Arriagada child or a Burgos/de la Cruz child. No CV, occupation-continuity, age, residence, parentage bridge, or family relationship connects this entry to the CV subject. Attachment probability from this entry alone: 0.02.

`Dario Jose Pulgar-Arriagada`: existing staged photograph/source contexts may use that name, but entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. Shared Pulgar/Arriagada surname elements are not proof of same person. Same-person probability from this entry alone: 0.03.

`Dario/Dario Pulgar Arriagada`: existing staged/canonical context includes Dario Pulgar Arriagada, Dario J. Pulgar Arriagada, Dario Pulgar A., and a canonical Dario Pulgar Arriagada expropriation-event stub. Entry 172 gives no Dario given name, no `J.` abbreviation, no medical/title/property context, and no chronology bridge. Same-person probability from this entry alone: 0.03.

Jose/Juana parent candidates: under the Pulgar/Arriagada hypothesis, the entry directly supports page-local parent candidates `Jose del Carmen Pulgar`/`Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. Existing wiki context also has `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` as parents of `Tulio Cesar Luis Jose`. These are duplicate-person and relationship-conflict watch items, not merge-ready identities.

## Conflict Types

- Same-person conflict: unresolved for the entry-172 father versus existing `Jose del Carmen Pulgar`; not supported for any Dario candidate.
- Duplicate-person conflict: possible duplicate or related Jose/Juana parent clusters, but no merge by name alone.
- Name-variant conflict: father field may be `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or uncertain; `Juana Arriagada de Pulgar` should not be silently equated with `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: Pulgar/Arriagada parent-child cluster versus Burgos/de la Cruz parent-child cluster.
- Chronology conflict: 8 March 1888 at 3 p.m. versus 6 April 1888 at 10 p.m.; both cannot be promoted as one child's birth event.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Moderate-high for a page-local Pulgar/Arriagada cluster, reduced by the unresolved row-control conflict. |
| conflict_severity | 0.95 | The conflict changes child, parents, birth date/time, place, and informant. |
| evidence_quality | 0.78 | Civil birth registration is strong evidence, and the source packet reports visual checking, but final conversion QA is still missing. |
| conversion_confidence | 0.35 | The current converted Markdown and assigned chunk materially disagree. |
| claim_probability | 0.76 | Pulgar/Arriagada is the stronger working hypothesis for the assigned staged draft, not a promotion-ready fact. |
| relevance | 0.92 | Directly relevant to Pulgar/Arriagada parent-child staging; only indirect Dario-line relevance. |
| canonical_readiness | 0.00 | Hold for conversion QA and proof review before any canonical action. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md` on `hold_for_conversion_qa`.

Exact next proof-review/promotion step: run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`, page 58, entry 172, comparing the source image, assigned chunk, and converted Markdown. QA must decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and must certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, proof-review the child identity, birth facts, father claim, mother claim, informant claim, and parent-child relationship candidates. Then run a separate Jose/Juana parent-candidate comparison before any duplicate-person merge. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` unless a later reviewed identity bridge supplies direct continuity evidence.
