---
type: identity_conflict_analysis
status: completed
role: identity_researcher
worker: postconv-identity-analysis-20260527232849089
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-evidence-extraction-20260527222756266.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-row-control-postconv-evidence-extraction-20260527222756266.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260527222756266.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Current Conversion Conflict

## Blockers First

1. Canonical promotion is blocked by a material row-control conflict. The referenced staged conflict draft says the original image and assigned chunk support physical entry `172` as the Pulgar/Arriagada row, while the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
2. The father field must remain bounded. The row-control packet stages the father as `Jose del Carmen Pulgar`; the chunk includes a possible trailing `S.`, but this analysis does not certify that suffix or expand it into another person.
3. No same-person merge is ready for `Jose del Carmen Pulgar`. Existing canonical wiki context has a `Jose del Carmen Pulgar` page, but this staged draft supplies only an entry-172 father reading, not enough proof that the father is the same canonical person represented in other rows.
4. No Juana merge is ready beyond the exact row reading `Juana Arriagada de Pulgar`. Do not silently correct or merge her with other Juana candidates from family context or adjacent Pulgar work.
5. No Dario-line bridge is present. The staged draft, source packet, converted file, chunk, reviewed notes, and existing wiki context do not connect entry `172` to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, or Dario passenger clusters.

## Literal Source Readings

The current row-control source packet gives the image-reviewed entry `172` reading as:

| Field | Bounded reading |
|---|---|
| Registration date | `Siete de Abril de mil ochocientos ochenta i ocho` |
| Child | `Jose del Carmen Segundo Pulgar Arriagada` |
| Sex | `Hombre` |
| Birth date/time | `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde` |
| Birth place | `Calle de Valdivia` |
| Father | `Jose del Carmen Pulgar` |
| Mother | `Juana Arriagada de Pulgar` |
| Declarant | `Ernesto Herrera L.`, present at the birth |

The current converted Markdown conflicts with that row-control reading by assigning entry `172` to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m. in `En esta`.

## Hypotheses And Evidence

### Hypothesis 1: Physical Entry 172 Is The Pulgar/Arriagada Birth Row

Supporting evidence:

- The staged conflict draft explicitly identifies the image-reviewed row as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`.
- The assigned chunk transcribes entry `172` with the Pulgar/Arriagada child, the 8 March 1888 birth at `Calle de Valdivia`, and the same parent names.
- Prior proof review for the same row-control problem held canonical promotion but accepted the bounded Pulgar/Arriagada row as the likely physical entry `172` reading.

Contrary or limiting evidence:

- The current converted Markdown gives a different child and parent set for entry `172`; that derivative conflict must be resolved or explicitly preserved before canonical promotion.
- The father suffix after `Pulgar` remains unresolved at suffix level.

Scores:

| Score type | Score | Rationale |
|---|---:|---|
| identity_confidence | 0.84 | Strong for the bounded child identity in physical entry `172`; not a broader merge. |
| conflict_severity | 0.94 | The converted and row-controlled readings name different children, parents, dates, and places. |
| evidence_quality | 0.86 | Direct civil registration row plus staged image-reviewed packet and prior proof-review context. |
| conversion_confidence | 0.68 | Chunk and row-control packet align, but the live converted Markdown is materially mismatched. |
| claim_probability | 0.84 | Physical entry `172` probably records the Pulgar/Arriagada child and stated parents. |
| relevance | 0.95 | Directly relevant to Pulgar/Arriagada family evidence and anti-conflation. |
| canonical_readiness | 0.35 | Hold until conversion-control/proof review resolves the derivative mismatch. |

### Hypothesis 2: Converted Entry 172 Is A Burgos/de la Cruz Birth Row

Supporting evidence:

- The current converted Markdown literally records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Contrary or limiting evidence:

- The staged conflict draft and row-control packet treat this as stale, row-shifted, or from a different page/image set.
- The assigned chunk for the same chunk id transcribes entry `172` as the Pulgar/Arriagada row, not the Burgos/de la Cruz row.
- No identity or relationship merge between the Burgos/de la Cruz child and the Pulgar/Arriagada child is supported.

Scores:

| Score type | Score | Rationale |
|---|---:|---|
| identity_confidence | 0.12 | This may be a real row elsewhere, but not the controlled physical entry `172` for this task. |
| conflict_severity | 0.94 | It directly conflicts with the row-controlled evidence. |
| evidence_quality | 0.30 | Derivative converted text only, contradicted by row-control packet and chunk. |
| conversion_confidence | 0.18 | Low for this source identity because the conversion is the conflict under review. |
| claim_probability | 0.14 | Not probable as the controlling entry `172` row for this staged task. |
| relevance | 0.70 | Relevant mainly as anti-conflation and conversion-QA evidence. |
| canonical_readiness | 0.05 | Do not promote from this task. |

### Hypothesis 3: Entry 172 Father Is The Existing `Jose del Carmen Pulgar` Person

Supporting evidence:

- The row-control packet's bounded father reading is `Jose del Carmen Pulgar`.
- The existing canonical page `wiki/people/jose-del-carmen-pulgar.md` represents a same-name Pulgar candidate with other family links in draft/reviewed context.

Contrary or limiting evidence:

- This staged draft does not supply age, spouse proof, birth/death data, or a cross-row proof argument that would prove the entry-172 father is the same canonical person.
- The possible trailing `S.` in the chunk remains unresolved and cannot be used to infer an identity variant.

Scores:

| Score type | Score | Rationale |
|---|---:|---|
| identity_confidence | 0.52 | Plausible same-name father candidate, not proved. |
| conflict_severity | 0.46 | Moderate duplicate-person risk if merged without proof. |
| evidence_quality | 0.66 | Direct name in the row, but no independent identity bridge. |
| conversion_confidence | 0.68 | Same conversion limits as the row-control packet. |
| claim_probability | 0.55 | Probable that a `Jose del Carmen Pulgar` is father; not ready as a canonical same-person claim. |
| relevance | 0.88 | Direct parent candidate. |
| canonical_readiness | 0.30 | Hold for proof-reviewed parent identity bridge. |

### Hypothesis 4: Entry 172 Mother Is The Existing `Juana Arriagada de Pulgar` Person

Supporting evidence:

- The row-control packet names the mother as `Juana Arriagada de Pulgar`.
- Existing canonical page `wiki/people/juana-arriagada-de-pulgar.md` already carries entry-172-derived evidence for this mother/child context.

Contrary or limiting evidence:

- This note cannot promote or merge; it only evaluates the staged conflict draft.
- The row does not prove identity with any other Juana candidate. Nearby family-context hints can justify later comparison, not silent correction.

Scores:

| Score type | Score | Rationale |
|---|---:|---|
| identity_confidence | 0.72 | Strong for the row's mother name; moderate for canonical same-person attachment because promotion is blocked. |
| conflict_severity | 0.50 | Moderate risk from Juana-name variants in nearby Pulgar material. |
| evidence_quality | 0.78 | Direct row reading, but dependent on conversion-control resolution. |
| conversion_confidence | 0.68 | Row-control confidence is useful, live conversion still conflicts. |
| claim_probability | 0.76 | The mother in physical entry `172` is probably `Juana Arriagada de Pulgar`. |
| relevance | 0.92 | Direct parent candidate. |
| canonical_readiness | 0.40 | Hold until row-control conflict is resolved or explicitly accepted. |

### Hypothesis 5: Entry 172 Bridges To Dario-Line Identities

Compared identities:

- `Dario Arturo Pulgar-Smith`: canonical family-supplied page identifies him as Alexander John Heinz's maternal grandfather and warns against automatic merges with similarly named Pulgar clusters.
- `Dario Arturo Pulgar`: staged CV packets use document-level subject attribution for a CV, but those packets do not derive from this birth row.
- `Dario Jose Pulgar-Arriagada` and `Dario J. Pulgar Arriagada`: local staged packets include photograph/source-title metadata and a 1918 medical-title name line, but no parent, child, birth date, or same-person bridge to entry `172`.
- `Dario/Dario Pulgar Arriagada`: existing wiki context includes a separate `Dario Pulgar Arriagada` expropriation event and other official-list clusters, not this entry-172 child.
- Jose/Juana parent candidates: entry `172` names `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, but does not state a Dario child, spouse, descendant, or lineage link to a Dario person.

Supporting evidence:

- The surname cluster `Pulgar Arriagada` is family-relevant and justifies anti-conflation comparison.

Contrary or limiting evidence:

- Entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.
- No reviewed local evidence in this task connects the 1888 child or parents to any Dario identity.
- Name overlap and family context are insufficient for a same-person, duplicate-person, or relationship claim.

Scores:

| Score type | Score | Rationale |
|---|---:|---|
| identity_confidence | 0.03 | No direct Dario identity bridge appears in the reviewed materials. |
| conflict_severity | 0.82 | High risk if Dario identities are merged or attached by surname context alone. |
| evidence_quality | 0.20 | Only negative/anti-conflation context for Dario from this source. |
| conversion_confidence | 0.68 | Row-control limits apply, but Dario is absent either way. |
| claim_probability | 0.02 | A Dario bridge from this entry is unsupported. |
| relevance | 0.58 | Relevant as a Pulgar-line guardrail, not as direct evidence. |
| canonical_readiness | 0.00 | Do not promote any Dario bridge from this entry. |

## Conflict Summary

| Conflict type | Finding |
|---|---|
| same-person | `Jose del Carmen Segundo Pulgar Arriagada` and converted `Jose Miguel` should not be treated as the same child. |
| duplicate-person | Existing Jose/Juana wiki pages are plausible context, but entry `172` needs proof-reviewed parent identity attachment before any duplicate merge. |
| name-variant | `Jose del Carmen Pulgar` must not be expanded using the unresolved possible `S.` suffix. `Juana Arriagada de Pulgar` must not be corrected into other Juana variants. |
| relationship-conflict | Pulgar/Arriagada parents conflict with Burgos/de la Cruz parents in the derivative converted Markdown; preserve as a conversion conflict, not a family relationship conflict to merge. |
| chronology-conflict | Pulgar/Arriagada row gives birth 1888-03-08 and registration 1888-04-07; converted Burgos/de la Cruz row gives birth 1888-04-06. This supports row mismatch rather than a chronology correction. |

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
|---:|---|---:|---|
| 1 | Physical entry `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.84 | Conversion-control or proof-review should explicitly accept the image-reviewed row-control packet over the stale converted Markdown before narrow promotion. |
| 2 | Entry `172` mother is `Juana Arriagada de Pulgar`, with no merge to other Juana variants. | 0.76 | After row-control acceptance, promote only the exact mother relationship/name reading; run separate Juana identity comparison before any merge. |
| 3 | Entry `172` father is `Jose del Carmen Pulgar`, with unresolved suffix omitted from claims. | 0.55 | After row-control acceptance, proof-review the father field boundary and run a parent identity bridge before attaching to an existing Jose page. |
| 4 | Converted Burgos/de la Cruz text is controlling for this source identity. | 0.14 | Do not promote; route to conversion-control as derivative mismatch. |
| 5 | Entry `172` bridges to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada. | 0.02 | No promotion step from this entry; require a separate proof-reviewed source naming compatible Dario identity anchors and lineage/identity evidence. |

## Recommended Next Action

Hold canonical promotion for this staged conflict draft. The exact next step is scoped conversion-control/proof review for `CHUNK-b8f4f0490a36-P0001-01` that explicitly reconciles the live converted Markdown against the source image, assigned chunk, and row-control source packet. If accepted, promote only narrow entry-172 facts for `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` without suffix, mother `Juana Arriagada de Pulgar`, and the stated birth details. Do not merge with `Jose Miguel`, `Oswaldo Burgos`, `Concepcion de la Cruz`, any Dario-line person, or any Jose/Juana candidate without a later proof-reviewed identity bridge.
