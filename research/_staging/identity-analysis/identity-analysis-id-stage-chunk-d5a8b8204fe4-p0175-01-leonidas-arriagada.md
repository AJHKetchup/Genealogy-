---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
task_id: "identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md"
worker: postconv-identity-analysis-20260528213843790
staged_draft: "research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md"
subject: "Leonidas Arriagada"
output_scope: "research/_staging/identity-analysis/"
---

# Identity And Conflict Analysis: Leonidas Arriagada

## Blockers

1. Conversion QA blocker: the staged draft and source packet both report low conversion confidence and a `reread-page` need. The recorded page image path, `raw/codex-conversion-jobs/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-164-183/page-images/page-0175.jpg`, is not present in this workspace.
2. Identity bridge blocker: the assigned staged draft gives only the page-local name `Leonidas Arriagada` and the list role `Suplente` under `Historia i Jeografia`. It gives no age, residence, parent, spouse, child, birth, death, occupation outside the list role, or same-person bridge to any canonical person.
3. Institutional-boundary blocker: the source packet says page 174 carries `CHILLAN` and `LICEO DE NINAS`, while page 175 later begins `LICEO AMERICANO DE SENORITAS`; the exact institutional attachment for the `Historia i Jeografia` list should be confirmed on image reread before any claim is promoted.
4. Anti-conflation blocker: this note found no existing canonical `Leonidas Arriagada` person page. Broader local context includes `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Darío Pulgar Arriagada`, and Dario/Pulgar identity clusters, but the assigned page does not name Pulgar, Dario, Jose, Juana, Smith, or any family relationship.

## Evidence Reviewed

- Staged identity draft: `research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md`.
- Source packet: `research/_staging/source-packets/chunk-d5a8b8204fe4-p0175-01-leonidas-arriagada-historia-jeografia-suplente.md`.
- Assigned chunk: `raw/chunks/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-sess-5715d57272/page-0175-chunk-01.md`.
- Converted Markdown reference: `raw/converted/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-164-183.codex.md`.
- Canonical context checked: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

## Literal Source Reading

The staged draft quotes the assigned page as:

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

Interpretation kept separate: this supports only that the converted text reads a person named `Leonidas Arriagada` in a `Suplentes` list under `Historia i/¡ Jeografia`, pending image reread. It does not itself establish a family identity, a canonical person match, or a relationship.

## Hypotheses

### H1: Page-Local Person Named Leonidas Arriagada

Hypothesis: the staged draft refers to a page-local named person, `Leonidas Arriagada`, listed as a `Suplente` for `Historia i Jeografia`.

Evidence supporting:
- The staged identity draft, source packet, and assigned chunk all contain the same name line, `Leonidas Arriagada`, under `Historia ¡ Jeografía` and `Suplentes`.
- The name appears in a structured list of named persons, not as an inferred family label.

Conflicts and limits:
- The page image is unavailable in this workspace, and the source packet flags the page for reread.
- The subject heading uses OCR-like text `Historia ¡ Jeografía`; subject and institution should not be normalized silently.
- No canonical person page for `Leonidas Arriagada` was found in `wiki/people`.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Multiple local derivative files agree on the name, but no image reread is available. |
| conflict_severity | 0.22 | Low direct conflict; the main risk is over-promotion from weak conversion evidence. |
| evidence_quality | 0.48 | Derivative text is consistent, but page-image QA is missing. |
| conversion_confidence | 0.30 | Staged draft and source packet both mark conversion confidence low. |
| claim_probability | 0.58 | Probably a real page-local name line, not yet proof-ready. |
| relevance | 0.42 | Arriagada surname is relevant as a lead, but this page has no family-link evidence. |
| canonical_readiness | 0.05 | Do not promote until image QA and proof review. |

### H2: Same Person Or Duplicate Of A Known Arriagada/Pulgar-Arriagada Person

Hypothesis: `Leonidas Arriagada` is the same person as, or a duplicate of, a known local Arriagada/Pulgar-Arriagada person.

Evidence supporting:
- Broad surname overlap exists with local canonical and staged Pulgar-Arriagada context.

Evidence against:
- Existing canonical Arriagada/Pulgar-Arriagada pages checked here concern `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, and `Darío Pulgar Arriagada`, not Leonidas.
- The assigned draft does not provide dates, places beyond broad source context, relatives, occupation beyond `Suplente`, or any direct link to the Pulgar family.
- The canonical `Dario Arturo Pulgar-Smith` page explicitly warns against attaching similarly named Dario/Pulgar/Pulgar-Arriagada records without identity review; this Leonidas page is even less connected because it does not name Dario or Pulgar.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No same-person bridge beyond a broad surname-family lead. |
| conflict_severity | 0.60 | Moderate risk if someone merges by Arriagada/Pulgar-Arriagada context alone. |
| evidence_quality | 0.18 | Evidence is only negative/contextual for this hypothesis. |
| conversion_confidence | 0.30 | Same low conversion confidence as the base record. |
| claim_probability | 0.02 | Same-person or duplicate-person claim is not supported. |
| relevance | 0.36 | Worth a future double-check only after image QA. |
| canonical_readiness | 0.00 | No merge, rename, or relationship promotion. |

### H3: Dario-Line Identity Bridge

Hypothesis: the `Leonidas Arriagada` mention provides a bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or related Dario/Pulgar candidate clusters.

Evidence supporting:
- Only broad family-context relevance: the surname `Arriagada` appears in local Pulgar-Arriagada work.

Evidence against:
- The staged draft does not name `Dario`, `Darío`, `Arturo`, `Jose`, `Pulgar`, `Pulgar-Smith`, `Pulgar-Arriagada`, Alexander John Heinz, spouse, child, parent, residence, birth, death, or any other bridge identifier.
- `Dario Arturo Pulgar-Smith` is represented from family-supplied knowledge as Alexander John Heinz's maternal grandfather, with an explicit caution not to auto-merge similar Dario/Pulgar records.
- `Darío Pulgar Arriagada` has a separate 2000 expropriation-notice event and no parent, birth, or relationship bridge to this 1918 Leonidas list entry.
- Existing Jose/Juana parent candidates are separate Pulgar register clusters; this page does not name Jose or Juana.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.01 | No Dario-line identifier appears in the assigned draft. |
| conflict_severity | 0.72 | High risk if used to collapse unrelated Arriagada/Pulgar-Arriagada identities. |
| evidence_quality | 0.10 | No direct evidence for this hypothesis. |
| conversion_confidence | 0.30 | Base page still requires QA, but even a clean reading would not create a Dario bridge. |
| claim_probability | 0.01 | Dario-line attachment is unsupported. |
| relevance | 0.20 | Surname context permits only a future search lead, not a claim. |
| canonical_readiness | 0.00 | Blocked for any Dario-line promotion or merge. |

## Required Pulgar-Line Comparison

| Candidate | Result | Reason |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Do not attach; probability 0.01. | Canonical page is family-supplied maternal-grandfather context; assigned draft does not name Dario, Arturo, Smith, Alexander, or kinship. |
| `Dario Arturo Pulgar` | Do not attach; probability 0.01. | Staged CV contexts use Dario Arturo Pulgar as a document-level subject; this page names only Leonidas Arriagada. |
| `Dario Jose Pulgar-Arriagada` | Do not attach; probability 0.01. | No Dario, Jose, or Pulgar-Arriagada name appears in the assigned draft. |
| `Dario/Darío Pulgar Arriagada` | Do not attach; probability 0.01. | Canonical `Darío Pulgar Arriagada` is a separate 2000 property-notice cluster; this 1918 list entry has no bridge. |
| `Jose del Carmen Pulgar` | Do not attach; probability 0.01. | Existing canonical Jose context is a Pulgar parent candidate from separate register evidence; this draft does not name Jose or Pulgar. |
| `Juana Arriagada de Pulgar` | Keep separate; probability 0.02. | Exact surname `Arriagada` overlaps, but this draft names Leonidas and gives no relationship to Juana. |
| `Juana de Dios Amagada de Pulgar` | Keep separate; probability 0.01. | Name differs and belongs to a separate Tulio/entry-513 context; this draft gives no bridge. |

Required next proof-review step: after page-image conversion QA verifies the name and institutional context, run a narrow proof review for a page-local `Leonidas Arriagada` role/listing claim only. A separate identity-bridge proof review would be required before comparing him as kin or same person with any Pulgar-line or Arriagada/Pulgar-Arriagada canonical person.

## Conflict Summary

- Same-person conflict: none proven. No existing canonical `Leonidas Arriagada` page was found.
- Duplicate-person risk: low for Leonidas specifically, moderate if a new canonical page is created before conversion QA.
- Name-variant conflict: `Historia ¡ Jeografía` is a conversion/orthography concern, not a person-name variant. No evidence supports treating `Leonidas Arriagada` as a variant of any Dario, Jose, or Juana name.
- Relationship conflict: no relationship is stated in the assigned draft. Any kinship attachment would be unsupported.
- Chronology conflict: no direct chronology conflict. The assigned source date is 1918-09, while reviewed Dario/Pulgar contexts include separate 1888 register, 1953 passenger, family-supplied, and 2000 property-notice contexts; no bridge ties them together.

## Overall Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Best supported only as a page-local named person. |
| conflict_severity | 0.34 | No active same-person conflict, but over-attachment risk exists. |
| evidence_quality | 0.48 | Consistent derivative evidence without page-image verification. |
| conversion_confidence | 0.30 | Low; page image unavailable and reread requested. |
| claim_probability | 0.58 | The name-line claim is plausible but held. |
| relevance | 0.42 | Useful Arriagada lead, not family proof. |
| canonical_readiness | 0.05 | Hold; no promotion or merge. |

## Recommended Next Action

Run targeted conversion QA for source page 175 when the rendered page image is available. The QA should certify whether the name reads `Leonidas Arriagada`, whether the subject heading should be transcribed as `Historia i Jeografia`, and which institution the list belongs to. After that, run proof review only for a narrow role/listing claim. Do not create or attach a canonical family identity, relationship, Dario-line bridge, Jose/Juana parent link, merge, or rename from this staged draft.
