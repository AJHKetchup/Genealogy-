---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d5a8b8204fe4-P0175-01-page-image-missing-qa.md"
worker: postconv-identity-analysis-20260528214858907
staged_draft: "research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d5a8b8204fe4-P0175-01-page-image-missing-qa.md"
subject: "Leonidas Arriagada"
output_scope: "research/_staging/identity-analysis/"
---

# Identity And Conflict Analysis: Leonidas Arriagada Page-Image QA Hold

## Blockers

1. Conversion QA blocker: the assigned staged conflict draft is explicitly a `conversion_qa_blocker`. It reports that the page was flagged for `reread-page` and that the recorded page image path is not present locally.
2. Evidence-control blocker: the assigned conflict draft's literal support is only the converted-text reading `Suplentes:` followed by `don Apolinario Puga.` and `- » Leonidas Arriagada.` The original page image has not been certified in this task.
3. Institutional-boundary blocker: the source packet notes page 174 context for `CHILLAN` / `LICEO DE NIÑAS` and page 175 later beginning `LICEO AMERICANO DE SEÑORITAS`; the exact school section controlling the `Historia i Jeografia` list must be confirmed by page-image QA.
4. Identity-bridge blocker: this source gives only a page-local name and list role. It gives no age, residence, birth, death, parent, spouse, child, sibling, household, or direct bridge to any existing canonical Arriagada, Pulgar, or Pulgar-Arriagada person.
5. Anti-conflation blocker: no canonical `Leonidas Arriagada` person page was found in the reviewed wiki context. Existing canonical Pulgar/Arriagada pages concern separate identities and source clusters.

## Evidence Reviewed

- Assigned staged conflict draft: `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d5a8b8204fe4-P0175-01-page-image-missing-qa.md`.
- Source packet: `research/_staging/source-packets/chunk-d5a8b8204fe4-p0175-01-leonidas-arriagada-historia-jeografia-suplente.md`.
- Assigned chunk: `raw/chunks/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-sess-5715d57272/page-0175-chunk-01.md`.
- Staged identity note: `research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md`.
- Staged claim and relationship context: `research/_staging/claims/chunk-d5a8b8204fe4-p0175-01-001-leonidas-arriagada-historia-jeografia-suplente.md` and `research/_staging/relationships/chunk-d5a8b8204fe4-p0175-01-no-family-relationship-stated.md`.
- Existing canonical context checked by local search: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

## Literal Source Reading

The assigned staged conflict draft quotes:

```text
Suplentes:

don Apolinario Puga.

- » Leonidas Arriagada.
```

The assigned chunk preserves the wider converted sequence:

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

Interpretation kept separate: this supports only a low-confidence page-local reading that a person named `Leonidas Arriagada` appears in a `Suplentes` list under a converted `Historia ¡ Jeografía` heading. It does not establish kinship, duplicate identity, a family-line bridge, or canonical attachment.

## Hypotheses

### H1: Page-Local Named Person, Leonidas Arriagada

Evidence supporting:

- The conflict draft, source packet, assigned chunk, staged identity note, staged claim, and staged relationship note all preserve the same page-local name `Leonidas Arriagada`.
- The name appears in a structured list of named personnel rather than as an inferred family label.
- Local wiki search found no existing canonical `Leonidas Arriagada` person page, reducing immediate duplicate-page conflict but not eliminating future duplicate risk.

Conflicts and limits:

- The page image is missing, and the staged conflict draft explicitly says promotion is blocked by conversion control.
- The heading `Historia ¡ Jeografía` contains an OCR-like character issue; the expected `Historia i Jeografia` reading should not be silently normalized until QA.
- The institution/school section boundary remains uncertain.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Repeated local derivative/staged files agree on the name, but image reread is missing. |
| conflict_severity | 0.25 | No direct identity conflict; main risk is premature promotion from low-confidence conversion text. |
| evidence_quality | 0.46 | The derivative evidence is consistent but not image-certified. |
| conversion_confidence | 0.25 | The assigned staged draft reports low confidence and missing page image. |
| claim_probability | 0.55 | Plausible page-local name/role reading, not proof-ready. |
| relevance | 0.40 | Useful Arriagada lead, but no family relationship evidence. |
| canonical_readiness | 0.05 | Hold for conversion QA and proof review. |

### H2: Same Person Or Duplicate Of A Known Arriagada/Pulgar-Arriagada Person

Evidence supporting:

- The surname `Arriagada` overlaps with existing local Pulgar-Arriagada context.

Evidence against:

- Reviewed canonical pages for `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Darío Pulgar Arriagada`, and `Dario Arturo Pulgar-Smith` describe separate source clusters and do not name `Leonidas Arriagada`.
- The assigned staged conflict draft does not provide dates, family members, residence, profession beyond the list role, or other bridge identifiers.
- The staged relationship note for this chunk reports no stated family relationship.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No same-person bridge beyond surname overlap. |
| conflict_severity | 0.55 | Moderate anti-conflation risk if attached by surname alone. |
| evidence_quality | 0.18 | Evidence for this hypothesis is contextual and mostly negative. |
| conversion_confidence | 0.25 | Base page still lacks image QA. |
| claim_probability | 0.02 | Same-person or duplicate claim is unsupported. |
| relevance | 0.32 | Worth retaining as a double-check lead only. |
| canonical_readiness | 0.00 | No merge, rename, relationship, or canonical claim. |

### H3: Dario-Line Or Jose/Juana Parent-Candidate Bridge

Evidence supporting:

- Only broad surname context: `Arriagada` appears in Pulgar-line research elsewhere in the workspace.

Evidence against:

- The assigned conflict draft does not name `Dario`, `Darío`, `Arturo`, `Jose`, `Juana`, `Pulgar`, `Pulgar-Smith`, or `Pulgar-Arriagada`.
- The canonical `Dario Arturo Pulgar-Smith` page cautions that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review; this draft does not even contain those names.
- Existing Jose/Juana parent candidates arise from separate birth-register clusters, not this 1918 educational personnel list.

Scores:

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.01 | No Dario-line or Jose/Juana bridge identifier appears. |
| conflict_severity | 0.70 | High risk if used to collapse unrelated Arriagada/Pulgar-line identities. |
| evidence_quality | 0.10 | No direct evidence supports the bridge. |
| conversion_confidence | 0.25 | Page QA is unresolved, but even a clean reading would not create the bridge. |
| claim_probability | 0.01 | Unsupported from this evidence. |
| relevance | 0.18 | Surname context is only a future search lead. |
| canonical_readiness | 0.00 | Blocked for any Pulgar-line or parent-candidate promotion. |

## Required Pulgar-Line Comparison

| Candidate | Rank | Result |
| --- | ---: | --- |
| `Leonidas Arriagada` as a page-local person | 1 | Plausible lead only; hold for page-image QA. |
| `Dario Arturo Pulgar-Smith` | Unsupported | Do not attach; probability 0.01. This draft does not name Dario, Arturo, Smith, Alexander John Heinz, or kinship. |
| `Dario Arturo Pulgar` | Unsupported | Do not attach; probability 0.01. Local Dario Arturo Pulgar contexts are separate; this draft names only Leonidas Arriagada. |
| `Dario Jose Pulgar-Arriagada` | Unsupported | Do not attach; probability 0.01. No Dario, Jose, Pulgar, or Pulgar-Arriagada name appears here. |
| `Dario/Darío Pulgar Arriagada` | Unsupported | Do not attach; probability 0.01. The canonical Darío Pulgar Arriagada context is a separate 2000 property-notice cluster with no bridge to this 1918 list. |
| `Jose del Carmen Pulgar` | Unsupported | Do not attach; probability 0.01. This draft does not name Jose or Pulgar. |
| `Juana Arriagada de Pulgar` | Unsupported surname-only lead | Keep separate; probability 0.02. Shared surname only; no relationship is stated. |
| `Juana de Dios Amagada de Pulgar` | Unsupported | Keep separate; probability 0.01. Different name form and separate source context. |

Exact next proof-review step before any Pulgar-line attachment: a separate identity-bridge proof review must cite direct evidence that names both the page-local `Leonidas Arriagada` and the proposed Pulgar-line person or relationship. The assigned staged conflict draft cannot supply that bridge.

## Conflict Summary

- Same-person conflict: none established. Best supported treatment is a page-local `Leonidas Arriagada` lead.
- Duplicate-person conflict: no existing canonical `Leonidas Arriagada` page was found; future duplicate risk remains if a page is created before conversion QA.
- Name-variant conflict: none established for the person name. `Historia ¡ Jeografía` is a conversion/heading issue, not a `Leonidas Arriagada` name variant.
- Relationship conflict: none stated. The staged relationship note reports no parent, spouse, child, sibling, household, or family relationship.
- Chronology conflict: none established. The source context is September 1918; reviewed Pulgar-line canonical/staged contexts are separate and unbridged.

## Overall Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Best supported only as a page-local named person. |
| conflict_severity | 0.36 | No active identity conflict, but anti-conflation risk exists. |
| evidence_quality | 0.46 | Consistent derivative/staged evidence, missing page-image control. |
| conversion_confidence | 0.25 | Low; assigned draft says page image is missing and reread is required. |
| claim_probability | 0.55 | The page-local name/role reading is plausible but not promotable. |
| relevance | 0.40 | Relevant as an Arriagada lead, not as family proof. |
| canonical_readiness | 0.05 | Hold; do not promote, merge, rename, or attach relationships. |

## Recommended Next Action

Run the exact conversion-QA/proof-review follow-up requested by the staged conflict draft: locate or regenerate the rendered page-175 image for `CHUNK-d5a8b8204fe4-P0175-01`, compare it against the chunk and converted Markdown, and certify the spelling of `Leonidas Arriagada`, the `Suplentes` role, the `Historia i Jeografia` heading, and the controlling institution section. If certified, promote only a narrow page-local role/listing claim. Do not attach this staged draft to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, Jose/Juana parent candidates, or any other Arriagada person without a later direct identity or relationship bridge.
