---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
task_id: "identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md"
worker: postconv-identity-analysis-20260528215849685
staged_draft: "research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md"
subject: "Leonidas Arriagada"
output_scope: "research/_staging/identity-analysis/"
---

# Identity And Conflict Analysis: Leonidas Arriagada

## Blockers

1. Conversion QA remains the controlling blocker. The staged draft and source packet both mark conversion confidence low and report that QC requested a page reread. The recorded page image path, `raw/codex-conversion-jobs/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-164-183/page-images/page-0175.jpg`, is not present in this workspace.
2. The identity evidence is page-local only. The assigned staged draft gives `Leonidas Arriagada` as a `Suplente` under `Historia i/¡ Jeografia`, with no age, birth, death, residence, spouse, parent, child, sibling, or same-person bridge.
3. Institutional context is not proof-ready. The source packet says the surrounding converted pages place this list between `CHILLAN` / `LICEO DE NIÑAS` and the later heading `LICEO AMERICANO DE SEÑORITAS`; the exact institution should be verified from the page image before any role claim is promoted.
4. Do not attach this lead to Pulgar-line or Arriagada-family profiles by surname alone. The assigned draft does not name Pulgar, Dario, Arturo, Jose, Juana, Smith, Alexander, or any kinship relationship.

## Evidence Reviewed

- Assigned staged identity draft: `research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md`.
- Source packet: `research/_staging/source-packets/chunk-d5a8b8204fe4-p0175-01-leonidas-arriagada-historia-jeografia-suplente.md`.
- Assigned chunk: `raw/chunks/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-sess-5715d57272/page-0175-chunk-01.md`.
- Canonical context checked: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, plus repository search results for `Leonidas`, `Arriagada`, `Pulgar`, `Dario`, `Jose`, and `Juana`.

## Literal Source Reading

The staged draft quotes:

```text
## Historia ¡ Jeografía
...
Suplentes:
...
- » Leonidas Arriagada.
```

The source packet and assigned chunk preserve the fuller local sequence:

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

Interpretation: this supports only a converted-text reading that a person named `Leonidas Arriagada` appears in a `Suplentes` list under `Historia i/¡ Jeografia`. It does not establish family identity, kinship, or a bridge to an existing canonical page.

## Hypotheses

### H1: Page-Local Named Person

Hypothesis: the staged draft identifies a page-local person named `Leonidas Arriagada`, listed as a substitute/suplente in the relevant subject list.

Evidence supporting:
- The staged identity draft, source packet, and chunk all agree on the name line `Leonidas Arriagada`.
- The name appears in a structured personnel list, not as a family-context inference.

Conflicts and limits:
- Page image reread is unavailable, so the exact reading and institutional boundary are not certified.
- The subject heading includes OCR-like `¡` for `i`; normalization should wait for QA.
- No canonical `Leonidas Arriagada` page was found.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Consistent derivative readings support a page-local name, but no image QA is available. |
| conflict_severity | 0.22 | Direct conflict is low; the risk is premature promotion. |
| evidence_quality | 0.48 | Useful derivative text, weak because the page was flagged for reread. |
| conversion_confidence | 0.30 | Staged draft/source packet mark conversion confidence low; image path is absent. |
| claim_probability | 0.58 | Plausible name-line claim, not proof-ready. |
| relevance | 0.42 | Arriagada surname is a useful lead, not a relationship proof. |
| canonical_readiness | 0.05 | Hold for conversion QA and proof review. |

### H2: Duplicate Or Same Person As Existing Arriagada/Pulgar-Arriagada Profile

Hypothesis: `Leonidas Arriagada` is the same person as, or a duplicate of, an existing Arriagada or Pulgar-Arriagada canonical/staged person.

Evidence supporting:
- Only broad surname context: `Arriagada` appears elsewhere in Pulgar/Arriagada family work.

Evidence against:
- Checked canonical pages concern different named people: `Juana Arriagada de Pulgar`, `Darío Pulgar Arriagada`, and `Dario Arturo Pulgar-Smith`.
- The assigned draft gives no date-of-birth, residence, family role, spouse, parent, child, occupation outside the page list, or other bridge data.
- The `Dario Arturo Pulgar-Smith` canonical page explicitly warns that similar Dario/Pulgar/Pulgar-Arriagada records require identity review before attachment.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No bridge beyond broad surname overlap. |
| conflict_severity | 0.60 | Meaningful conflation risk if surname overlap is overused. |
| evidence_quality | 0.18 | Evidence is mostly negative/contextual. |
| conversion_confidence | 0.30 | Same base-page QA weakness. |
| claim_probability | 0.02 | Same-person or duplicate claim is unsupported. |
| relevance | 0.36 | Worth a future double-check only after image QA. |
| canonical_readiness | 0.00 | No merge, rename, or attachment. |

### H3: Pulgar-Line Identity Bridge

Hypothesis: this `Leonidas Arriagada` mention helps identify or connect `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or Jose/Juana parent candidates.

Evidence supporting:
- Only broad family-context relevance from the Arriagada surname.

Evidence against:
- The assigned draft does not name `Dario`, `Darío`, `Arturo`, `Jose`, `Pulgar`, `Pulgar-Smith`, `Pulgar-Arriagada`, `Juana`, or any kinship.
- `Dario Arturo Pulgar-Smith` is currently family-supplied as Alexander John Heinz's maternal grandfather and has an anti-auto-merge note.
- `Darío Pulgar Arriagada` is represented by a separate 2000 expropriation-event cluster.
- `Juana Arriagada de Pulgar` and `Jose del Carmen Segundo Pulgar Arriagada` belong to separate register evidence and are not connected to this 1918 Leonidas listing by the assigned draft.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.01 | No Pulgar-line identifier appears. |
| conflict_severity | 0.72 | High risk if this is used to collapse unrelated Pulgar/Arriagada identities. |
| evidence_quality | 0.10 | No direct support for the bridge. |
| conversion_confidence | 0.30 | Even a clean reread would not create a Pulgar bridge by itself. |
| claim_probability | 0.01 | Unsupported. |
| relevance | 0.20 | Surname context can guide later searching, not claims. |
| canonical_readiness | 0.00 | Blocked for any Dario-line promotion. |

## Required Pulgar-Line Comparison

| Candidate | Result | Reason |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Do not attach; probability 0.01. | Canonical context is family-supplied maternal-grandfather evidence; assigned draft does not name Dario, Arturo, Smith, Alexander, or kinship. |
| `Dario Arturo Pulgar` | Do not attach; probability 0.01. | Dario Arturo Pulgar staged contexts are separate Dario records; this page names only Leonidas Arriagada. |
| `Dario Jose Pulgar-Arriagada` | Do not attach; probability 0.01. | No Dario, Jose, Pulgar, or Pulgar-Arriagada text appears in the assigned draft. |
| `Dario/Darío Pulgar Arriagada` | Do not attach; probability 0.01. | The canonical page is a separate 2000 property-notice cluster with no bridge to this 1918 list entry. |
| `Jose del Carmen Pulgar` | Do not attach; probability 0.01. | Existing Jose context belongs to separate register evidence; this draft does not name Jose or Pulgar. |
| `Juana Arriagada de Pulgar` | Keep separate; probability 0.02. | Shared surname only. This draft names Leonidas and gives no relationship to Juana. |
| `Juana de Dios Amagada/Arriagada de Pulgar` candidates | Keep separate; probability 0.01. | These belong to separate register/conflict work and are not named or bridged here. |

Exact next proof-review step needed: first run targeted conversion QA for page 175 to certify the name, subject heading, and institutional boundary. Only after that, run a narrow proof review for a page-local `Leonidas Arriagada` role/listing claim. A separate identity-bridge proof review would be required before any comparison to Pulgar-line or Jose/Juana parent candidates could be promoted.

## Conflict Summary

- Same-person conflict: none proven.
- Duplicate-person risk: low for `Leonidas Arriagada`, but moderate if a new canonical page is created before conversion QA.
- Name-variant conflict: no evidence supports treating `Leonidas Arriagada` as a variant of any Dario, Jose, Juana, or Pulgar name.
- Relationship conflict: no relationship is stated; kinship attachment would be unsupported.
- Chronology conflict: none direct. The 1918 source date is separate from 1888 register, 1953 passenger, family-supplied Pulgar-Smith, and 2000 property-notice contexts.

## Overall Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Best supported only as a page-local named person. |
| conflict_severity | 0.34 | No active same-person conflict, but over-attachment risk exists. |
| evidence_quality | 0.48 | Consistent derivative evidence without image verification. |
| conversion_confidence | 0.30 | Low; page image unavailable and reread requested. |
| claim_probability | 0.58 | Name-line claim is plausible but held. |
| relevance | 0.42 | Useful Arriagada lead, not family proof. |
| canonical_readiness | 0.05 | Hold; no promotion or merge. |

## Recommended Next Action

Run targeted conversion QA for source page 175 when the rendered page image is available. The QA should certify whether the name reads `Leonidas Arriagada`, whether the subject heading should read `Historia i Jeografia`, and which institution the list belongs to. Do not create or attach a canonical family identity, relationship, Dario-line bridge, Jose/Juana parent link, merge, or rename from this staged draft.
