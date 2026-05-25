---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525071814524
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: 0.12
---

# Identity And Conflict Analysis: Entry 172 Pulgar/Arriagada

This note analyzes the staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md`.

## Blockers First

- Conversion blocker: the assigned chunk and source packet support entry 172 as a Pulgar/Arriagada birth registration, while the assigned converted Markdown transcribes entry 172 as a different child and different parents. This is a row-level or file-assignment conflict, not a name variant.
- Father-name blocker: the father field must remain unresolved among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted source-image QA resolves the final mark or suffix.
- Relationship blocker: no father-child, mother-child, parental-pair, or canonical person attachment from this staged draft should be promoted until conversion QA reconciles or supersedes the converted Markdown.
- Duplicate-person blocker: `Juana Arriagada de Pulgar` must not be silently merged with `Juana de Dios Amagada de Pulgar`; existing wiki/staged context treats those as separate or unresolved Jose/Juana parent candidates.
- Pulgar-line blocker: this entry-172 evidence does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar-Arriagada, Dario Pulgar Arriagada, or Dario Pulgar A. It cannot bridge or merge any Dario-line identity by name or family context alone.

## Evidence Boundary

Evidence reviewed locally:

- Staged conflict draft named above.
- Staged source packet `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md`.
- Assigned chunk `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Assigned converted Markdown `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Conversion follow-up task `research/_staging/tasks/conversion-review-note-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md`.
- Existing canonical wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, `Dario Arturo Pulgar-Smith`, and `Dario Pulgar Arriagada`.

No external research was used.

## Literal Readings Kept Separate

Assigned chunk/source-packet reading:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth date/time/place: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.` in the chunk, with staged QA preserving possible outcomes `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Mother field: `Juana Arriagada de Pulgar`.
- Parents' domicile: `Calle de Colipi` / `Calle de Colipi` with accent/spelling left to QA.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employee, resident at `Calle de Valdivia`.

Assigned converted Markdown reading:

- Entry number: `172`.
- Child: `Jose Francisco`.
- Birth date/time/place: 20 February 1888, 10 p.m., `Pellin`.
- Father: `Oswaldo Gomez`.
- Mother: `Rosario de la Cruz de la Maza`.
- Informant: `Oswaldo Gomez`.

Interpretation:

- These are mutually incompatible row-level readings for the same assigned entry number and page reference. The current identity analysis cannot select the controlling literal reading without targeted conversion QA.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Hypothesis: the controlling source row for entry 172 is the Pulgar/Arriagada row naming child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.

Supporting evidence:

- The assigned chunk directly transcribes entry 172 with the Pulgar/Arriagada child and parents.
- The staged source packet summarizes the same row and flags the assigned converted Markdown as a derivative row-level conflict.
- Existing canonical wiki pages already contain low-confidence/probable evidence snapshots for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` from earlier entry-172 staging.

Conflicts:

- The assigned converted Markdown records a completely different entry 172.
- The father-name ending is unresolved.
- Some earlier local conflict notes mention other derivative competing readings for entry 172, reinforcing that this chunk has a history of conversion instability.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Strong within the assigned chunk/source packet, but not proof-ready because the assigned converted Markdown conflicts materially. |
| conflict_severity | 0.93 | Different child, father, mother, birth date/place, and informant. |
| evidence_quality | 0.58 | Staged chunk and source packet are specific, but conversion conflict prevents treating them as final proof. |
| conversion_confidence | 0.42 | Mixed: the chunk is detailed, while the assigned converted file is incompatible. |
| claim_probability | 0.64 | Probable as a staged hypothesis only, pending targeted image QA. |
| relevance | 0.98 | Directly relevant to entry 172 and Pulgar/Arriagada identity. |
| canonical_readiness | 0.12 | Hold for conversion QA before any promotion. |

## Hypothesis 2: The Assigned Converted Markdown Is A Different Row, Page, Or File State

Hypothesis: the assigned converted Markdown's `Jose Francisco` / `Oswaldo Gomez` / `Rosario de la Cruz de la Maza` entry is not a variant of the Pulgar/Arriagada row, but a mismatched row, page, or conversion state.

Supporting evidence:

- The converted Markdown differs in every identity-bearing field from the chunk/source-packet row.
- The staged conflict draft explicitly classifies the issue as `row_level_conversion_conflict`.
- The conversion follow-up task requires reconciliation or supersession of the assigned converted Markdown.

Conflicts:

- The converted Markdown is still the assigned converted file in the metadata, so it cannot simply be ignored by an identity worker.
- No authorized conversion QA result in this task has selected which row controls.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | The mismatch pattern is too broad for a normal name variant. |
| conflict_severity | 0.95 | Full row-level replacement risk. |
| evidence_quality | 0.62 | Multiple local staging files recognize the same conflict. |
| conversion_confidence | 0.30 | The assigned conversion layer is unreliable for entry 172 until QA. |
| claim_probability | 0.78 | More likely a conversion/file-row problem than a true identity variant. |
| relevance | 1.00 | This is the central staged conflict. |
| canonical_readiness | 0.05 | No canonical promotion until the conversion layer is fixed. |

## Hypothesis 3: `Jose del Carmen Pulgar S.` Is A Name Variant Or Suffix For `Jose del Carmen Pulgar`

Hypothesis: `Jose del Carmen Pulgar S.` may be the same father candidate as canonical/staged `Jose del Carmen Pulgar`, with `S.` representing a visible surname initial, abbreviation, flourish, or unresolved mark.

Supporting evidence:

- The chunk gives `Jose del Carmen Pulgar S.` in the father field.
- The staged conflict draft says to preserve all three QA outcomes: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical `Jose del Carmen Pulgar` is a stub with separate draft child evidence for `Tulio Cesar Luis Jose`; it does not resolve the entry-172 suffix.

Conflicts:

- The father field is not yet source-proofed at a final literal level.
- The assigned converted Markdown names a different father.
- Name overlap with other Jose/Pulgar records is not enough to merge father candidates or children.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.55 | Plausible, but the suffix/mark is exactly the unresolved point. |
| conflict_severity | 0.76 | Affects father identity and relationship promotion. |
| evidence_quality | 0.50 | Staged evidence is specific but not settled. |
| conversion_confidence | 0.38 | The father field needs targeted image QA. |
| claim_probability | 0.57 | Likely a father-name variant candidate, not ready as final identity. |
| relevance | 0.96 | Directly relevant to the entry-172 parental claim. |
| canonical_readiness | 0.10 | Hold until father-field QA and proof review. |

## Hypothesis 4: `Juana Arriagada de Pulgar` Is The Mother In This Entry

Hypothesis: if the Pulgar/Arriagada row controls, the mother is `Juana Arriagada de Pulgar`.

Supporting evidence:

- The assigned chunk and source packet name `Juana Arriagada de Pulgar` as mother in entry 172.
- Existing canonical `Juana Arriagada de Pulgar` has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from earlier entry-172 staging.

Conflicts:

- The converted Markdown names `Rosario de la Cruz de la Maza` as mother for its entry 172 row.
- Existing wiki/staged context also has `Juana de Dios Amagada de Pulgar` in a different entry-513 cluster; that person/name must remain separate from `Juana Arriagada de Pulgar` unless a later proof review proves a duplicate or conversion error.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Well supported within the Pulgar/Arriagada row hypothesis. |
| conflict_severity | 0.88 | Competing mother identity in converted Markdown. |
| evidence_quality | 0.57 | Specific but dependent on row-level QA. |
| conversion_confidence | 0.43 | Mixed because the assigned converted file conflicts. |
| claim_probability | 0.66 | Probable only if QA accepts the Pulgar/Arriagada row. |
| relevance | 0.97 | Direct mother-candidate evidence. |
| canonical_readiness | 0.12 | Hold pending conversion QA. |

## Hypothesis 5: The Converted Markdown Family Is A Separate Identity Cluster

Hypothesis: `Jose Francisco`, `Oswaldo Gomez`, and `Rosario de la Cruz de la Maza` are a separate family cluster present somewhere in the source/conversion history, not duplicate names for the Pulgar/Arriagada family.

Supporting evidence:

- The names, birth date/place, and informant in the converted Markdown form a coherent non-Pulgar row.
- None of the converted Markdown identity fields are plausible spelling variants of the Pulgar/Arriagada row.

Conflicts:

- The converted Markdown places this family under entry 172, the same entry number assigned to the Pulgar/Arriagada row in the chunk.
- This task did not run conversion or inspect the source image, so it cannot locate the Gomez/de la Maza row.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | The converted row reads as a separate family, not variants. |
| conflict_severity | 0.90 | Same entry number currently points to two incompatible families. |
| evidence_quality | 0.46 | Evidence exists only as conflicted derivative conversion text in this analysis. |
| conversion_confidence | 0.25 | Needs conversion QA to determine source location or error. |
| claim_probability | 0.70 | Likely separate if the converted text came from a real row. |
| relevance | 0.86 | Relevant as the competing identity cluster. |
| canonical_readiness | 0.03 | Do not promote from this conflict context. |

## Pulgar-Line Anti-Conflation Comparison

### Dario Arturo Pulgar-Smith

Evidence:

- Canonical page `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and identifies him as Alexander John Heinz's maternal grandfather.
- That page explicitly warns not to automatically merge similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review.

Application to this staged draft:

- Entry 172 does not name Dario Arturo Pulgar-Smith or state a relationship to Alexander John Heinz.
- A broad Pulgar surname context justifies later lineage review only after the entry-172 row is proof-reviewed.

Scores: identity_confidence 0.04; conflict_severity 0.82; evidence_quality 0.34; conversion_confidence 0.42; claim_probability 0.03; relevance 0.55; canonical_readiness 0.00.

### Dario Arturo Pulgar

Evidence:

- Existing staging contains CV and work-history clusters for `Dario Arturo Pulgar`, generally held for identity-bridge review before attachment to `Dario Arturo Pulgar-Smith`.

Application to this staged draft:

- Entry 172 does not name Dario Arturo Pulgar.
- No birth date, parent, child, occupation, or residence bridge in this draft connects the 1888 child or parents to the CV subject.

Scores: identity_confidence 0.03; conflict_severity 0.80; evidence_quality 0.30; conversion_confidence 0.42; claim_probability 0.02; relevance 0.50; canonical_readiness 0.00.

### Dario Jose Pulgar-Arriagada

Evidence:

- Existing staged source packets use `Dario Jose Pulgar-Arriagada` in photo/archive metadata contexts, with some source-availability and visual-identification caveats.

Application to this staged draft:

- Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose Pulgar-Arriagada.
- Shared `Pulgar Arriagada` surname pattern is not an identity bridge.

Scores: identity_confidence 0.05; conflict_severity 0.86; evidence_quality 0.32; conversion_confidence 0.42; claim_probability 0.03; relevance 0.58; canonical_readiness 0.00.

### Dario Pulgar-Arriagada / Dario Pulgar Arriagada

Evidence:

- Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` records a `Dario Pulgar Arriagada` expropriation/legal-notice event on 2000-12-05.
- Other staged records mention `Dario Pulgar-Arriagada` in medical or Chile listing contexts.

Application to this staged draft:

- Entry 172 does not name Dario or a 2000 legal/property context.
- A person born in 1888 as `Jose del Carmen Segundo Pulgar Arriagada` is not automatically the same as any later `Dario Pulgar Arriagada`; the given names differ and the chronology is not bridged.

Scores: identity_confidence 0.04; conflict_severity 0.88; evidence_quality 0.35; conversion_confidence 0.42; claim_probability 0.02; relevance 0.60; canonical_readiness 0.00.

### Jose/Juana Parent Candidates

Evidence:

- Existing wiki pages preserve `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` as separate or unresolved local candidates.
- Entry-172 staging supports `Juana Arriagada de Pulgar` as mother of `Jose del Carmen Segundo Pulgar Arriagada`, but the relationship is blocked by conversion QA.
- Entry-513 staging supports a different child cluster involving `Juana de Dios Amagada de Pulgar`, with its own surname-reading conflict.

Application to this staged draft:

- `Juana Arriagada de Pulgar` is directly relevant to entry 172.
- `Juana de Dios Amagada de Pulgar` is anti-conflation context only; do not merge her with `Juana Arriagada de Pulgar`.
- `Jose del Carmen Pulgar` is directly relevant as the father candidate, but the exact suffix/mark remains unresolved.

Scores: identity_confidence 0.58; conflict_severity 0.82; evidence_quality 0.52; conversion_confidence 0.40; claim_probability 0.56; relevance 0.96; canonical_readiness 0.10.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | The staged conflict is a row-level conversion/file-assignment conflict, not a name variant. | 0.78 | Targeted conversion QA against the source image for register page 58, entry 172; reconcile or supersede the assigned converted Markdown. |
| 2 | Entry 172 controls as the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.64 | Source-image QA must confirm the row, child name, birth date/place, mother, informant, and page/entry alignment. |
| 3 | Father candidate is `Jose del Carmen Pulgar`, with unresolved final mark/suffix. | 0.57 | Proof review must choose `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` from source-visible evidence. |
| 4 | Mother candidate is `Juana Arriagada de Pulgar` for this entry. | 0.66 conditional on Hypothesis 2 | Promote only after row QA; keep separate from `Juana de Dios Amagada de Pulgar`. |
| 5 | Converted Markdown `Jose Francisco` / `Oswaldo Gomez` / `Rosario de la Cruz de la Maza` is a separate identity cluster or conversion artifact. | 0.70 | Conversion QA should determine whether this row exists elsewhere in the image/source or is an erroneous conversion state. |
| 6 | Entry 172 supplies a bridge to Dario Arturo Pulgar-Smith or Dario Arturo Pulgar. | 0.03 | No promotion step from this draft; revisit only after accepted lineage evidence directly connects the confirmed Jose/Juana cluster to a Dario identity. |
| 7 | Entry 172 supports merger with Dario Jose Pulgar-Arriagada, Dario Pulgar-Arriagada, or Dario Pulgar Arriagada. | 0.03 | Preserve separate; require direct full-name, date, family, occupation, residence, or source-continuity evidence before comparison. |

## Conflict Summary

- Same-person conflict: unresolved for entry-172 father `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`; do not decide without image QA.
- Duplicate-person conflict: high risk if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar` based on partial name/surname similarity.
- Name-variant conflict: `Pulgar S.` may be a suffix, abbreviation, or uncertain mark; preserve all readings.
- Relationship conflict: father/mother relationships for `Jose del Carmen Segundo Pulgar Arriagada` are dependent on the unresolved row-level conversion conflict.
- Chronology conflict: no direct chronology conflict inside the Pulgar/Arriagada row, but the Dario comparison is not chronologically or genealogically bridged by this 1888 birth entry.

## Recommended Next Action

Keep all dependent entry-172 claims, relationships, identity candidates, and canonical updates at `hold_for_conversion_qa`.

Exact next step: run targeted conversion QA against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` for register page 58, entry 172. The QA result must reconcile or supersede `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`, confirm the controlling row, and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review for the child identity, birth facts, father claim, mother claim, child-parent relationships, and Jose/Juana anti-conflation before any canonical promotion or Pulgar-line Dario comparison.
