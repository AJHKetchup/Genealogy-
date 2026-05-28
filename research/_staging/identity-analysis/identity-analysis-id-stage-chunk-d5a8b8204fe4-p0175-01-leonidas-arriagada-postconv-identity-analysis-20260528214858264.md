---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
task_id: "identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md"
worker: postconv-identity-analysis-20260528214858264
staged_draft: "research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md"
subject: "Leonidas Arriagada"
output_scope: "research/_staging/identity-analysis/"
---

# Identity And Conflict Analysis: Leonidas Arriagada

## Blockers

1. Conversion QA blocks promotion. The staged draft and source packet both mark conversion confidence as low and report a requested `reread-page`. The referenced page image path, `raw/codex-conversion-jobs/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-164-183/page-images/page-0175.jpg`, is not present in this workspace.
2. Identity bridge evidence is absent. The assigned staged draft supplies only the page-local name `Leonidas Arriagada` and a list role, `Suplente`, under `Historia i/¡ Jeografia`; it gives no age, birth, death, residence, spouse, parent, child, or same-person bridge.
3. Institutional context is not proof-ready. The source packet reports that page 174 carries `CHILLAN` and `LICEO DE NINAS`, while page 175 later begins `LICEO AMERICANO DE SENORITAS`; the exact institution for this list must be confirmed by image QA before any role/listing claim.
4. Anti-conflation is required. Existing local wiki context includes Arriagada and Pulgar-Arriagada people, but this staged draft does not name Pulgar, Dario, Arturo, Jose, Juana, Smith, Alexander John Heinz, or any kinship relationship.

## Evidence Reviewed

- Staged draft: `research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md`.
- Source packet: `research/_staging/source-packets/chunk-d5a8b8204fe4-p0175-01-leonidas-arriagada-historia-jeografia-suplente.md`.
- Assigned chunk: `raw/chunks/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-sess-5715d57272/page-0175-chunk-01.md`.
- Converted file reference: `raw/converted/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-164-183.codex.md`.
- Canonical pages checked for local conflict context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

## Literal Source Reading

The staged draft quotes the assigned page:

```text
## Historia ¡ Jeografía
...
Suplentes:
...
- » Leonidas Arriagada.
```

The source packet and assigned chunk preserve the same local sequence:

```text
## Historia ¡ Jeografía

Propietarios:

don Samuel Zenteno.

- » Moisés González R.

doña Amalia Melo de Oviedo.

Suplentes:

don Apolinario Puga.

- » Leonidas Arriagada.
```

Interpretation kept separate: this derivative reading supports only a possible page-local person named `Leonidas Arriagada` in a `Suplentes` list under `Historia i/¡ Jeografia`, pending image reread. It does not establish family identity, a canonical match, or a relationship.

## Hypotheses

### H1: Page-Local Leonidas Arriagada

Hypothesis: the staged draft refers to a page-local named person, `Leonidas Arriagada`, listed as a `Suplente` for `Historia i/¡ Jeografia`.

Evidence supporting:

- The staged draft, source packet, assigned chunk, and converted reference all contain the same name line in the same subject/list context.
- The name appears as a personal name in a structured personnel list, not as a family relationship inference.

Conflicts and limits:

- The page image is unavailable in this workspace, and reread-page QA is explicitly requested.
- `Historia ¡ Jeografia` appears to contain OCR/orthographic noise; normalization to `Historia i Jeografia` should wait for QA.
- No canonical `Leonidas Arriagada` page was found in the local wiki context reviewed here.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Multiple local derivative files agree on the name, but no page-image proof is available. |
| conflict_severity | 0.20 | No direct same-person conflict; primary risk is over-promotion. |
| evidence_quality | 0.48 | Derivative evidence is consistent but not image-verified. |
| conversion_confidence | 0.30 | Staged materials mark the conversion low confidence. |
| claim_probability | 0.58 | The name-line claim is plausible but held pending QA. |
| relevance | 0.42 | Arriagada surname is a useful lead, but this page lacks family-link evidence. |
| canonical_readiness | 0.05 | Not ready for canonical promotion or person creation. |

### H2: Same Person Or Duplicate Of A Known Arriagada/Pulgar-Arriagada Person

Hypothesis: `Leonidas Arriagada` is the same person as, or a duplicate of, an existing local Arriagada/Pulgar-Arriagada identity.

Evidence supporting:

- Only broad surname context: `Arriagada` appears in existing Pulgar-Arriagada work.

Evidence against:

- The canonical pages checked concern `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, and `Dario/Dario Pulgar Arriagada`; none name Leonidas.
- The assigned draft provides no date of birth, residence, parent, spouse, child, occupation beyond list role, or other identifier tying Leonidas to those people.
- Local Dario/Pulgar pages warn against attaching similarly named clusters without identity review; this staged draft has even less bridge evidence because it does not name Pulgar or Dario.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No same-person evidence beyond broad surname overlap. |
| conflict_severity | 0.58 | Moderate risk if merged by surname/family context alone. |
| evidence_quality | 0.18 | Evidence for this hypothesis is contextual and mostly negative. |
| conversion_confidence | 0.30 | Same base page QA limitation applies. |
| claim_probability | 0.02 | Same-person or duplicate-person claim is unsupported. |
| relevance | 0.36 | Worth retaining as a future search lead only after QA. |
| canonical_readiness | 0.00 | No merge, rename, or relationship promotion. |

### H3: Dario-Line Bridge

Hypothesis: the `Leonidas Arriagada` mention bridges to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or related Jose/Juana parent candidates.

Evidence supporting:

- Only broad family-context relevance: the surname `Arriagada` appears in Pulgar-Arriagada materials.

Evidence against:

- The staged draft does not name Dario, Arturo, Jose, Juana, Pulgar, Pulgar-Smith, Pulgar-Arriagada, Alexander John Heinz, spouse, child, parent, or any bridge identifier.
- `Dario Arturo Pulgar-Smith` is represented from family-supplied knowledge as Alexander John Heinz's maternal grandfather and carries an explicit caution against automatic merges with similar Dario/Pulgar clusters.
- `Dario/Dario Pulgar Arriagada` is represented in the local wiki by a separate 2000 expropriation-notice event, with no bridge to a 1918 Leonidas list entry.
- Jose/Juana parent candidates belong to separate birth-register clusters; this page does not name Jose or Juana.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.01 | No Dario-line identifier appears in the assigned draft. |
| conflict_severity | 0.72 | High risk if used to collapse unrelated Arriagada/Pulgar-Arriagada identities. |
| evidence_quality | 0.10 | No direct evidence supports this hypothesis. |
| conversion_confidence | 0.30 | Base page remains low-confidence, but even a clean reading would not prove a Dario bridge. |
| claim_probability | 0.01 | Dario-line attachment is unsupported. |
| relevance | 0.20 | Surname context permits only a future lead, not a claim. |
| canonical_readiness | 0.00 | Blocked for any Dario-line promotion or merge. |

## Required Pulgar-Line Comparison

| Candidate | Rank/Probability | Result |
| --- | ---: | --- |
| `Dario Arturo Pulgar-Smith` | 0.01 | Do not attach. Canonical page is family-supplied maternal-grandfather context; this draft does not name Dario, Arturo, Smith, Alexander, or kinship. |
| `Dario Arturo Pulgar` | 0.01 | Do not attach. Staged CV contexts use this as a document-level subject; this page names only Leonidas Arriagada. |
| `Dario Jose Pulgar-Arriagada` | 0.01 | Do not attach. No Dario, Jose, or Pulgar-Arriagada wording appears in the assigned draft. |
| `Dario/Dario Pulgar Arriagada` | 0.01 | Do not attach. Existing local context is a separate 2000 property-notice cluster with no bridge. |
| `Jose del Carmen Pulgar` | 0.01 | Do not attach. Existing Jose context is a Pulgar parent candidate from separate register evidence; this draft does not name Jose or Pulgar. |
| `Juana Arriagada de Pulgar` | 0.02 | Keep separate. The surname overlaps, but the assigned draft names Leonidas and gives no relationship to Juana. |
| `Juana de Dios Amagada de Pulgar` | 0.01 | Keep separate. Name and record cluster differ; no bridge is present. |

Exact proof-review step needed next: after page-image conversion QA verifies the line and institutional context, run a narrow proof review for only the page-local role/listing claim that `Leonidas Arriagada` was listed as `Suplente` under `Historia i/¡ Jeografia`. A separate identity-bridge proof review would be required before any comparison as kin, same person, duplicate, or name variant with Pulgar-line or Arriagada/Pulgar-Arriagada canonical people.

## Conflict Summary

- Same-person conflict: none proven. No local canonical `Leonidas Arriagada` page was found.
- Duplicate-person risk: low for Leonidas specifically, moderate if a new canonical page is created before conversion QA.
- Name-variant conflict: none supported. `Historia ¡ Jeografia` is a subject-heading conversion issue, not a person-name variant.
- Relationship conflict: none in the literal source. Any kinship attachment would be unsupported.
- Chronology conflict: none directly. The assigned source date is 1918-09; reviewed Pulgar contexts include separate 1888 register, 1953 passenger, family-supplied, and 2000 property-notice evidence, but no bridge ties those contexts to Leonidas.

## Overall Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Best supported only as a page-local named person. |
| conflict_severity | 0.34 | No active same-person conflict, but over-attachment risk exists. |
| evidence_quality | 0.48 | Consistent derivative evidence without page-image verification. |
| conversion_confidence | 0.30 | Low; page image unavailable and reread requested. |
| claim_probability | 0.58 | Name-line claim is plausible but held. |
| relevance | 0.42 | Useful Arriagada lead, not family proof. |
| canonical_readiness | 0.05 | Hold; no promotion, merge, rename, or relationship attachment. |

## Recommended Next Action

Run targeted conversion QA for source page 175 when the rendered page image is available. QA should certify whether the name reads `Leonidas Arriagada`, whether the subject heading should be transcribed as `Historia i Jeografia`, and which institution the list belongs to. After QA, run proof review only for the narrow role/listing claim. Do not create or attach a canonical family identity, relationship, Dario-line bridge, Jose/Juana parent link, merge, or rename from this staged draft.
