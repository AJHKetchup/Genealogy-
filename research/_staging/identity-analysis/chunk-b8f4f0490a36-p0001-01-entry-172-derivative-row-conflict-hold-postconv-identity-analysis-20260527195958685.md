---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: "postconv-identity-analysis-20260527195958685"
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Derivative Row Conflict

## Blockers

1. The referenced raw source image and job page image are absent in this checkout, so this worker cannot independently re-inspect row `172`.
2. The assigned chunk/source packet and the current converted Markdown still describe mutually incompatible entry-172 families. The chunk/source packet read a Pulgar/Arriagada child; the converted Markdown reads a Burgos/de la Cruz child.
3. The father field is not ready for suffix normalization. The assigned chunk reads `Jose del Carmen Pulgar S.`, while later staged row-certification notes restrict the certified reading to `Jose del Carmen Pulgar` and leave any terminal mark unresolved.
4. No evidence reviewed for this assigned draft names `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` in entry `172`. Any Dario-line attachment would be a surname/family-context inference, not a literal source reading.
5. Canonical pages already contain some entry-172-derived facts and relationship snapshots, but this analysis does not promote, merge, rename, or correct canonical material.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md`.
- Held source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Reviewed/staged notes for the same conflict family, including prior proof reviews and row-control notes under `research/_staging/reviews/` and `research/_staging/tasks/`.
- Existing canonical context under `wiki/people/` for Dario Arturo Pulgar-Smith, Darío Pulgar Arriagada, Jose del Carmen Segundo Pulgar Arriagada, Jose del Carmen Pulgar, Juana Arriagada de Pulgar, Juana de Dios Amagada de Pulgar, and Dario Pulgar passenger stubs.

No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, or canonical wiki pages were edited.

## Literal Readings

| Evidence item | Literal reading | Use in this analysis |
| --- | --- | --- |
| Assigned chunk | Entry `172`: `Jose del Carmen Segundo Pulgar Arriagada`, male; registered 7 April 1888; born 8 March 1888, 3 p.m., Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.` | Supports a Pulgar/Arriagada row hypothesis, with father suffix unresolved. |
| Held source packet | Repeats the assigned chunk's Pulgar/Arriagada row and explicitly flags derivative conflict. | Supports holding the family-relevant evidence for conversion QA. |
| Current converted Markdown | Entry `172`: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. | Supports a conflicting derivative-row hypothesis, not a name variant of the Pulgar row. |
| Staged row-certification notes | Prior workers report image-level row control in favor of the Pulgar/Arriagada row and certify father only to `Jose del Carmen Pulgar`. | Useful reviewed/staged context, but this worker did not re-view the absent source image. |

## Hypotheses

### H1: Entry 172 Is The Pulgar/Arriagada Birth Row

The best supported working hypothesis is that physical entry `172` on register page 58 is the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, child of a father beginning `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.

Supporting evidence:

- The assigned chunk and held source packet agree on the Pulgar/Arriagada row.
- Prior staged row-control notes for this same source family report targeted image review in favor of the Pulgar/Arriagada row.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` reflect entry-172-derived candidate evidence, showing this row has already been treated as family-relevant in the workspace.

Limits:

- This worker could not inspect the source image because it is absent.
- The current converted Markdown remains materially incompatible.
- The father suffix must remain unresolved: `Jose del Carmen Pulgar`, not silently expanded to `Jose del Carmen Pulgar S.` for promotion.

Scores:

| Dimension | Score / value |
| --- | ---: |
| identity_confidence | 0.66 |
| conflict_severity | 0.90 |
| evidence_quality | 0.62 |
| conversion_confidence | 0.36 |
| claim_probability | 0.76 |
| relevance | 0.93 |
| canonical_readiness | hold_for_conversion_qa |

### H2: Entry 172 Is The Burgos/de la Cruz Row

This hypothesis treats the current converted Markdown as controlling: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.

Supporting evidence:

- The converted Markdown directly assigns those names to entry `172`.

Conflicts:

- The assigned chunk and held source packet read a different family, child, birth date, place wording, parents, and informant.
- Prior staged row-certification notes treat the converted Markdown as stale, row-shifted, or sourced from a different image/page.
- The staged conflict draft correctly warns not to promote the Burgos/de la Cruz reading as controlling entry `172` without later image review.

Scores:

| Dimension | Score / value |
| --- | ---: |
| identity_confidence | 0.22 |
| conflict_severity | 0.90 |
| evidence_quality | 0.25 |
| conversion_confidence | 0.24 |
| claim_probability | 0.18 |
| relevance | 0.55 |
| canonical_readiness | not_ready |

### H3: Jose del Carmen Pulgar Parent Candidate

This hypothesis treats `Jose del Carmen Pulgar` as the likely father candidate if H1 is accepted after QA.

Supporting evidence:

- The assigned chunk's father field begins `Jose del Carmen Pulgar`.
- Later staged row-certification notes explicitly certify the father only as `Jose del Carmen Pulgar`, with any terminal suffix unresolved.
- The canonical `Jose del Carmen Pulgar` page exists and has separate Pulgar-line relationship context, but not enough from this assignment to merge or expand relationships.

Conflicts and limits:

- The chunk's `S.` suffix cannot be converted into a stable surname or abbreviation without proof review.
- This entry does not identify his parents, spouse beyond the mother field, or any Dario-line connection.

Scores:

| Dimension | Score / value |
| --- | ---: |
| identity_confidence | 0.58 |
| conflict_severity | 0.72 |
| evidence_quality | 0.60 |
| conversion_confidence | 0.36 |
| claim_probability | 0.70 |
| relevance | 0.86 |
| canonical_readiness | hold_for_conversion_qa |

### H4: Juana Arriagada de Pulgar Parent Candidate

This hypothesis treats `Juana Arriagada de Pulgar` as the likely mother candidate if H1 is accepted after QA.

Supporting evidence:

- The assigned chunk and held source packet read the mother field as `Juana Arriagada de Pulgar`.
- Existing canonical `Juana Arriagada de Pulgar` context includes a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts and limits:

- The current converted Markdown's mother is `Concepcion de la Cruz`, so conversion-control conflict blocks promotion from this assignment.
- The name form may be a married-style name; this record alone should not merge her with other Juana candidates by name similarity.
- `Juana de Dios Amagada de Pulgar` in canonical context is a separate candidate from other entry-513 evidence and should not be merged with `Juana Arriagada de Pulgar` from entry `172`.

Scores:

| Dimension | Score / value |
| --- | ---: |
| identity_confidence | 0.62 |
| conflict_severity | 0.72 |
| evidence_quality | 0.61 |
| conversion_confidence | 0.36 |
| claim_probability | 0.73 |
| relevance | 0.88 |
| canonical_readiness | hold_for_conversion_qa |

### H5: Dario-Line Same-Person Or Ancestral Bridge

This hypothesis asks whether entry `172` can be linked to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or the existing Dario Pulgar passenger/directory clusters.

Supporting evidence:

- Only broad family-context hints exist: the Pulgar surname and Arriagada surname are relevant to the workspace's Pulgar-line research.
- Canonical pages show separate Dario candidates: family-supplied `Dario Arturo Pulgar-Smith`, legal-notice `Darío Pulgar Arriagada`, and passenger-list `Dario Pulgar` stubs.

Conflicts and limits:

- Entry `172` does not name Dario or Arturo.
- The child in H1 is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario/Jose Dario.
- The evidence gives no birth-year, relationship chain, spouse, residence bridge, occupation bridge, or later-life identifier connecting this child or parents to the Dario candidates.
- Dario Arturo Pulgar-Smith is family-supplied as Alexander John Heinz's maternal grandfather; Darío Pulgar Arriagada is a 2000 legal-notice subject; Dario Pulgar passenger stubs are separate age-based passenger identities. None can be merged or attached from entry `172`.

Ranking:

| Candidate | Rank | Probability from this evidence | Required next proof step |
| --- | ---: | ---: | --- |
| No Dario bridge from entry `172` | 1 | 0.92 | Keep Dario comparisons as anti-conflation notes only. |
| Dario Arturo Pulgar-Smith same as any entry-172 person | 4 | 0.03 | Separate identity-bridge proof review using identity-bearing Dario records and a documented parent/child chain. |
| Dario Arturo Pulgar same as any entry-172 person | 4 | 0.04 | Review identity-bearing CV/title/front/contact/signature pages and compare to canonical Pulgar-Smith context. |
| Dario Jose Pulgar-Arriagada / Jose Dario Pulgar Arriagada same as entry-172 child | 3 | 0.08 | Locate a source that explicitly names the same person with both Jose/Dario forms plus parents or birth details. |
| Dario/Dario Pulgar Arriagada legal/directory/passenger cluster same as entry-172 child | 4 | 0.05 | Separate proof review tying name, date, place, family, and chronology across the legal/directory/passenger records. |

## Conflicts

- Same-person conflict: The Pulgar/Arriagada child and the Burgos/de la Cruz child cannot be treated as the same person. They differ in name, parents, birth date, and family cluster.
- Duplicate-person risk: Existing canonical pages for entry-172-derived people may represent premature or low-confidence promotion while the current assigned conflict remains unresolved. This analysis does not alter those pages.
- Name-variant risk: `Jose del Carmen Pulgar S.` should not be normalized to a fuller identity or surname without suffix QA. `Juana Arriagada de Pulgar` should not be merged with `Juana de Dios Amagada de Pulgar` by visual/name similarity.
- Relationship conflict: Parent-child relationships from entry `172` are plausible under H1 but blocked by derivative conflict and father suffix uncertainty.
- Chronology conflict: H1 gives birth on 8 March 1888; H2 gives birth on 6 April 1888. These are incompatible row readings, not a simple date variant.

## Overall Scores

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Moderate for Pulgar/Arriagada as the likely target row; low for any broader merge or Dario bridge. |
| conflict_severity | 0.90 | The conflict changes child identity, parents, birth date, and family cluster. |
| evidence_quality | 0.60 | Civil-register evidence is strong in principle, but this worker lacks the source image and derivatives conflict. |
| conversion_confidence | 0.34 | The current converted Markdown conflicts with the assigned chunk, held packet, and prior staged row-control notes. |
| claim_probability | 0.76 | The central claim that this evidence must remain held for conversion QA is strongly supported. |
| relevance | 0.91 | High for Pulgar/Arriagada row control and parent candidates; low for Dario attachment. |
| canonical_readiness | hold_for_conversion_qa | No canonical promotion, merge, rename, or relationship update should proceed from this assignment. |

## Recommended Next Action

Keep this staged conflict at `hold_for_conversion_qa`. The exact next proof-review or promotion step is a targeted proof review that explicitly accepts or rejects the staged row-certification notes for physical entry `172`, reconciles the assigned chunk against the current converted Markdown, and fixes the father-field boundary as one of: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

Only after that review should any entry-172 child identity, parent-child relationship, parent-page attachment, or source-packet promotion be considered. Dario-line attachment requires a separate identity-bridge proof review with direct Dario-bearing evidence and should not be inferred from this entry.
