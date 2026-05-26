---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260526014145001
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Row-control blocker: the staged conflict draft identifies a material conflict between the assigned chunk/source packet, which read entry 172 as a Pulgar/Arriagada birth row, and the current converted Markdown, which reads entry 172 as a Burgos/de la Cruz birth row. This blocks all canonical claims from this entry.
- Father-name blocker: even if the Pulgar/Arriagada row is confirmed, the father field still needs targeted QA to certify whether the visible source supports `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Identity-bridge blocker: entry 172 does not name Dario. It cannot by itself connect Jose/Juana parent candidates, Jose del Carmen Segundo Pulgar Arriagada, Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío J. Pulgar Arriagada, Dario/Darío Pulgar Arriagada, or the passenger-list Dario Pulgar candidates.
- Canonical-context blocker: existing canonical pages already contain held or low-confidence evidence derived from entry 172. Because this draft is specifically a row-level conversion conflict, no new canonical promotion, merge, relationship, or name-variant conclusion should be made until conversion QA resolves the controlling row.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Canonical wiki context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/dario-pulgar-adult-passenger-age-64.md`, and `wiki/people/dario-pulgar-child-passenger-age-11.md`.

## Literal Source Readings

### Pulgar/Arriagada Reading

- The staged conflict draft and source packet read entry 172 as child `Jose del Carmen Segundo Pulgar Arriagada`, male.
- They read registration date as 7 April 1888 and birth as 8 March 1888, about 3 p.m., at Calle de Valdivia.
- They read father as `Jose del Carmen Pulgar S.` in the source packet/staged draft, with the conflict draft requiring QA on the exact father-field extent.
- They read mother as `Juana Arriagada de Pulgar`.
- They read informant as `Ernesto Herrera L.`, present at the birth.

### Burgos/de la Cruz Reading

- The current converted Markdown reads entry 172 as child `Jose Miguel`, male.
- It reads birth as 6 April 1888, about 10 p.m., place `En esta`.
- It reads father as `Oswaldo Burgos`, mother as `Concepcion de la Cruz`, and informant as `Oswaldo Burgos`.

## Interpretation Kept Separate

- If the Pulgar/Arriagada row is confirmed, it would support a birth-registration cluster for `Jose del Carmen Segundo Pulgar Arriagada` and possible parent candidates `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The confirmed row would not automatically identify any Dario-line person. It would only create family-context evidence that may justify a later double-check against independently reviewed Pulgar-line identity bridges.
- If the Burgos/de la Cruz row is confirmed, the Pulgar/Arriagada claims from this chunk/source packet should remain unpromoted or be superseded in staging.

## Hypotheses And Scores

| Rank | Hypothesis | Evidence Supporting | Conflicts / Limits | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | Entry 172 is a Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | Staged conflict draft, source packet, and referenced chunk all preserve the Pulgar/Arriagada row with consistent child, mother, date, place, and informant details. Earlier reviewed local context also cautions that entry 172 visibly supports a Pulgar/Arriagada row. | Current converted Markdown gives an incompatible Burgos/de la Cruz row for the same entry number, so conversion QA must decide the controlling row. Father suffix/detail remains unresolved. | 0.72 |
| 2 | Entry 172 is a Burgos/de la Cruz row for `Jose Miguel`. | Current converted Markdown reads entry 172 as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`. | This conflicts with the staged source packet and chunk, which are more directly aligned with the current assigned conflict task. No Pulgar-line identity conclusions can be drawn if this row controls. | 0.28 |
| 3 | `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` is the father in the Pulgar/Arriagada row. | Pulgar/Arriagada reading names a father in that form. Canonical `Jose del Carmen Pulgar` exists as a stub with a separate child link to `Tulio Cesar Luis Jose`, showing there are Jose parent-candidate materials in local context. | Exact suffix is not settled. Same-name parent candidates must not be merged without a proof-reviewed bridge. | 0.60 if row 1 controls; 0.00 if row 2 controls |
| 4 | `Juana Arriagada de Pulgar` is the mother in the Pulgar/Arriagada row. | Pulgar/Arriagada reading names mother as `Juana Arriagada de Pulgar`; canonical stub has low-confidence entry-172 evidence for child `Jose del Carmen Segundo Pulgar Arriagada`. | Existing wiki also has `Juana de Dios Amagada de Pulgar` as a separate Juana-like parent candidate for another child. Do not collapse Juana candidates by name similarity. | 0.68 if row 1 controls; 0.00 if row 2 controls |
| 5 | Entry 172 supplies evidence for `Dario Arturo Pulgar-Smith`. | Only indirect family-context relevance: shared Pulgar surname and local maternal Pulgar-Smith line. | The entry does not name Dario, Arturo, Smith, Pulgar-Smith, spouse, child, grandchild, or Alexander John Heinz. Canonical page explicitly requires identity review before attaching Dario/Pulgar records. | 0.05 |
| 6 | Entry 172 supplies evidence for document-level `Dario Arturo Pulgar`. | Only indirect Pulgar surname context. | No Dario or Arturo name appears in the entry-172 readings. Existing CV materials require a separate identity bridge even for Dario Arturo Pulgar to Dario Arturo Pulgar-Smith. | 0.04 |
| 7 | Entry 172 supplies evidence for `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Dario/Darío Pulgar Arriagada`. | The Pulgar/Arriagada surname pattern is a possible family-context hint only. | Entry 172 names Jose del Carmen Segundo, not Dario; it does not expand a `J.` initial, prove a Dario given name, or bridge to the 1918 medical-title or 2000 expropriation clusters. | 0.03 |
| 8 | Entry 172 supplies evidence for adult or child passenger-list `Dario Pulgar` candidates. | Shared surname only. | No passenger, travel, age, residence, or Dario identity data appears in entry 172. | 0.01 |

## Conflict Analysis

- Same-person conflict: unresolved only at the level of possible future Pulgar-line bridges. This entry does not currently support a same-person conclusion for any Dario candidate.
- Duplicate-person risk: high if `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar` are merged by name resemblance without source-visible identity links.
- Name-variant conflict: the entry may involve a father-name variant or suffix (`Pulgar` versus `Pulgar S.`), but this is a conversion/reading issue, not a proven identity variant.
- Relationship conflict: the Pulgar reading would support child-parent relationships for Jose del Carmen Segundo with Jose/Juana candidates; the Burgos reading would support an entirely different child-parent set. These cannot both be promoted for entry 172.
- Chronology conflict: the competing rows give different birth dates and times for different children: 8 March 1888 at about 3 p.m. versus 6 April 1888 at about 10 p.m. This is a row-control conflict rather than a same-child chronology discrepancy.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.35 | High confidence that there are named identity candidates, but low confidence for canonical attachment until row control is resolved. |
| conflict_severity | 0.95 | The row conflict changes child, parents, birth date/time/place, and informant. |
| evidence_quality | 0.70 | Staged packet and chunk are internally coherent, but current converted Markdown contradicts them. |
| conversion_confidence | 0.42 | Conversion confidence remains held because the authoritative converted Markdown and assigned chunk disagree at row level. |
| claim_probability | 0.30 | No entry-derived claim should be promoted while the controlling row is unresolved. |
| relevance | 0.82 | Highly relevant to Pulgar/Arriagada staging if the Pulgar row controls; only weakly relevant to Dario-line identity. |
| canonical_readiness | 0.00 | Hold. No canonical fact, relationship, merge, or name variant is ready. |

## Ranked Conclusion

The strongest local hypothesis is that the assigned chunk/source packet preserve a Pulgar/Arriagada row for entry 172, but the active converted Markdown preserves a conflicting Burgos/de la Cruz row for the same entry number. That row-control issue is prior to all identity analysis.

For Pulgar-line comparison, preserve these clusters separately: `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada` / `Darío J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, adult and child passenger-list `Dario Pulgar`, `Jose del Carmen Pulgar` / possible `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`. Entry 172 does not prove any Dario identity or Dario relationship.

## Recommended Next Action

Run targeted conversion QA for `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` against the current converted Markdown and chunk, limited to deciding the controlling row for entry 172 and certifying the father-field visible extent. After that, rerun proof review on the narrow entry-172 claims before any canonical action.

Exact proof-review gate after QA: review only the certified row-level claims for child name, sex, registration date, birth date/time/place, father name, mother name, and informant. Open a separate identity-bridge review before linking any resulting Pulgar/Arriagada family-context evidence to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, or any Dario passenger candidate.
