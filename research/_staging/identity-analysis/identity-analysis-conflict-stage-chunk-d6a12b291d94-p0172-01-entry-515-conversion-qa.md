---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d6a12b291d94-P0172-01-entry-515-conversion-qa.md
staged_draft: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d6a12b291d94-P0172-01-entry-515-conversion-qa.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
referenced_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
available_chunk_checked: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
page_reference: page 172; entry 515
canonical_readiness: hold
---

# Identity And Conflict Analysis: Entry 515 Conversion QA

## Blockers

- The staged conflict draft reports a source-visibility problem, not a resolved alternate identity: the derivative text supports `Rosa Elvira del Carmen`, father `Pedro Pablo Leiva`, and mother `Carmen Fuentes`, but proof review states that the available PNG is cropped before the mother field can be verified.
- The exact chunk path referenced by the staged draft and source packet, `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md`, was not present in this checkout. I checked the converted file and the available same-content chunk at `page-0001-chunk-01.md` without editing either file.
- Entry 515 has nearby staged conflict history. Other staged notes for page 172 preserve alternate readings such as `Pedro Pablo Neira`, `Carmen Leiva`, `Carmen Ulloa`, and a different child-name reading. Those conflicts are not proof of a corrected reading for this task, but they raise duplicate-person and relationship-conflict risk if any entry-515 person is promoted from derivative text alone.
- No external research was performed. No raw source, converted Markdown, chunk, or canonical wiki page was edited.

## Literal Source And Derivative Readings

From the staged conflict draft:

```text
Nombre. Rosa Elvira del Carmen
Nombre del padre. Pedro Pablo Leiva
Nombre de la madre. Carmen Fuentes
```

From the source packet proof-review concern: entry 515 is cut off at the bottom of the available PNG; the entry context and father/declarant area appear partly visible, but the mother field for `Carmen Fuentes` is not visible in the reviewed image area.

From the converted file and available chunk checked in this review: entry 515 reads `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`; the available converted table does not itself visibly establish `Carmen Fuentes` in the entry-515 row, while the staged claim file for the mother preserves the derivative reading `Carmen Fuentes` and explicitly holds it for conversion QA.

## Hypothesis 1: Same Entry, Derivative Mother Claim Is Overstated

Hypothesis: the staged conflict draft concerns one birth-register entry, page 172 entry 515, and the real conflict is derivative transcript completeness versus image visibility for the mother field.

Supporting evidence:

- The staged conflict draft, source packet, converted file, and available chunk all identify page 172 entry 515 as the target.
- The proof review for the combined child-parents relationship states that the visible source supports entry context and appears to support `Pedro Pablo Leiva`, but not the mother field.
- The staged mother claim already has `promotion_recommendation: hold_for_conversion_qa`.

Conflicts and limits:

- The mother identity `Carmen Fuentes` is derivative-only in the reviewed evidence layer.
- The converted file's completeness statement is inconsistent with proof-review visibility findings for the bottom of entry 515.
- Nearby staged reviews preserve materially different entry-515 readings, so no identity endpoint should be promoted from this derivative layer alone.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Strong page/entry alignment, but endpoints remain partly unverified. |
| conflict_severity | 0.76 | A mother identity and combined child-parents relationship would be materially wrong if the derivative reading is unsupported. |
| evidence_quality | 0.58 | Civil register is strong source type, but the relevant image area is incomplete. |
| conversion_confidence | 0.48 | Conversion confidence is reduced by cropped-image review and conflicting staged variants. |
| claim_probability | 0.55 | Plausible but not source-visible enough for the mother claim. |
| relevance | 0.95 | Directly addresses the assigned staged conflict. |
| canonical_readiness | 0.10 | Hold for conversion QA. |

## Hypothesis 2: Father Is Pedro Pablo Leiva

Hypothesis: the father/declarant in entry 515 is `Pedro Pablo Leiva`, and this is a stronger identity endpoint than the mother endpoint.

Supporting evidence:

- The converted derivative text reads `Nombre del padre. Pedro Pablo Leiva`.
- The proof review for the child-father relationship states that the father column and compareciente column visibly support `Pedro Pablo Leiva` and identify him as `Padre`.
- The staged father claim gives higher confidence than the mother claim and remains held chiefly because the full row is cropped.

Conflicts and limits:

- Other staged conflict drafts for page 172 preserve image-review concerns that the surname may be closer to `Neira`. That is a material identity conflict, not a name variant to normalize silently.
- The child full name is only partly image-verified in this task, so even the stronger father relationship should wait for full-row QA.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Father/declarant has stronger visible support than the mother field. |
| conflict_severity | 0.62 | Leiva/Neira would create a material duplicate-person or wrong-parent conflict. |
| evidence_quality | 0.66 | Direct civil-register evidence, but incomplete row. |
| conversion_confidence | 0.68 | Locally consistent in the d6a12b evidence set, weaker across nearby staged variants. |
| claim_probability | 0.73 | Likely within this staged evidence set, still held. |
| relevance | 0.90 | Father identity affects the entry-515 relationship scope. |
| canonical_readiness | 0.30 | Not ready until complete row and surname are image-checked. |

## Hypothesis 3: Mother Is Carmen Fuentes

Hypothesis: the mother in entry 515 is `Carmen Fuentes`, as stated in the staged conflict draft and staged mother claim.

Supporting evidence:

- The staged conflict draft and staged mother claim preserve derivative support for `Nombre de la madre. Carmen Fuentes`.
- The staged mother claim gives additional derivative attributes: Chilean, housework, and domicile at Calle San Joaquin.

Conflicts and limits:

- The proof-review finding is explicit that the mother field is not visible in the available PNG area reviewed.
- The converted file and available chunk checked here do not independently resolve the mother field in the visible text reviewed for this task.
- Nearby staged variants include `Carmen Leiva` and `Carmen Ulloa`; those are not adopted here, but they reinforce that the mother endpoint is unstable.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Name exists in staged derivative claim, but not image-verified. |
| conflict_severity | 0.82 | Wrong mother identity would create a serious relationship conflict. |
| evidence_quality | 0.34 | Derivative-only for the disputed field. |
| conversion_confidence | 0.32 | Cropped-image blocker directly affects this field. |
| claim_probability | 0.40 | Possible, not proved. |
| relevance | 0.96 | Central to the staged conflict. |
| canonical_readiness | 0.00 | Do not promote. |

## Hypothesis 4: Alternate Entry-515 Identities Or Name Variants

Hypothesis: nearby staged readings such as `Pedro Pablo Neira`, `Carmen Leiva`, `Carmen Ulloa`, or a different child-name reading represent either alternate conversion attempts for the same entry or separate duplicate-person risks caused by OCR/vision instability.

Supporting evidence:

- Existing staged conflict and review notes for the same page family preserve Leiva/Neira and Fuentes/Leiva/Ulloa disagreements.
- Those notes consistently recommend hold or conversion QA rather than canonical promotion.

Conflicts and limits:

- This assigned staged draft does not itself establish `Neira`, `Carmen Leiva`, or `Carmen Ulloa` as corrected readings.
- Family or same-page context can justify a double-check only; it cannot silently replace `Carmen Fuentes` or `Pedro Pablo Leiva`.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Alternate readings are warning signals, not resolved identities here. |
| conflict_severity | 0.78 | If promoted separately, variants could create duplicate or wrong-parent persons. |
| evidence_quality | 0.42 | Based on staged QA notes, not a new source reading. |
| conversion_confidence | 0.28 | Variant instability shows conversion risk. |
| claim_probability | 0.25 | Possible alternate readings need targeted proof review. |
| relevance | 0.80 | Important for preventing duplicate-person creation. |
| canonical_readiness | 0.00 | Do not promote or merge. |

## Pulgar-Line Anti-Conflation Check

The assigned conflict is not a Dario Pulgar conflict. However, the same converted page includes entry 513 for a Pulgar family row, and existing canonical wiki context contains Pulgar-line stubs. This review therefore treats Pulgar context as an anti-conflation check only.

Compared candidates:

- `Dario Arturo Pulgar-Smith`: canonical family-supplied maternal-grandfather page; no evidence in entry 515 links him to `Rosa Elvira del Carmen`, `Pedro Pablo Leiva`, or `Carmen Fuentes`.
- `Dario Arturo Pulgar`: staged CV/work-history subject in other materials; no evidence in entry 515.
- `Dario Jose Pulgar-Arriagada` and `Dario/Dario Pulgar Arriagada`: separate Pulgar-line candidates in other staged/canonical context; no evidence in entry 515.
- Jose/Juana parent candidates: entry 513 and existing wiki pages include `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada`; they concern Pulgar-line records, not the entry-515 Leiva/Fuentes candidate.

Ranked Pulgar hypotheses for this assigned draft:

| rank | hypothesis | probability | next proof-review step |
| ---: | --- | ---: | --- |
| 1 | Pulgar names are same-page or existing-wiki context only, not entry-515 identities. | 0.92 | Keep entry 515 separate from Pulgar-line pages unless a future source explicitly links the families. |
| 2 | Entry 515 has a collateral connection through witness `Santiago Fuentes` or same-register proximity. | 0.08 | Double-check only if a future local source states a relationship; do not infer from proximity. |
| 3 | Entry 515 should attach to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada. | 0.01 | No promotion step available from this evidence; require an explicit identity-bearing bridge source. |

## Conflict Summary

- Same-person conflict: unresolved only within entry-515 endpoints. `Pedro Pablo Leiva` is stronger than `Carmen Fuentes`; neither should be merged with alternate Leiva/Neira/Fuentes/Leiva/Ulloa variants by name alone.
- Duplicate-person risk: high if separate canonical people are created from `Carmen Fuentes`, `Carmen Leiva`, or `Carmen Ulloa` before the mother field is image-verified; moderate for `Pedro Pablo Leiva` versus `Pedro Pablo Neira`.
- Name-variant conflict: Leiva/Neira and Fuentes/Leiva/Ulloa are material surname conflicts, not harmless spelling variants.
- Relationship conflict: combined child-parents relationship is blocked because the mother field is not visible in the reviewed image area.
- Chronology conflict: none identified within the entry-515 date context. The issue is source visibility and identity endpoint reliability, not chronological impossibility.

## Overall Scores

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.55 | Entry identity is clear; person endpoints are unevenly supported. |
| conflict_severity | 0.80 | Disputed parent identity affects canonical family structure. |
| evidence_quality | 0.52 | Strong source class, weak visibility for the disputed field. |
| conversion_confidence | 0.43 | Conversion output conflicts with image-review completeness findings and nearby variants. |
| claim_probability | 0.52 | Father likely; mother and combined relationship not proved. |
| relevance | 0.96 | Directly responsive to the staged conflict draft. |
| canonical_readiness | 0.05 | Hold; no canonical promotion from this analysis. |

## Recommended Next Action

Hold the staged conflict and run targeted conversion QA against a complete source image or continuation image for page 172 entry 515. The exact proof-review step needed next is image-level reread of the full entry-515 row, focused on the child full-name field, the father/declarant surname, and the complete mother field. After that reread, revise the staged claims to the source-visible reading or promote only the narrower claim components that the complete image directly supports.
