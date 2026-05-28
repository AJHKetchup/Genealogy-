---
type: identity_conflict_analysis
status: draft
worker: postconv-identity-analysis-20260528220337106
task_id: "identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md"
role: identity_researcher
staged_draft: "research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md"
subject: "Leonidas Arriagada"
chunk_id: CHUNK-d5a8b8204fe4-P0175-01
source_packet: "research/_staging/source-packets/chunk-d5a8b8204fe4-p0175-01-leonidas-arriagada-historia-jeografia-suplente.md"
promotion_recommendation: do_not_promote
canonical_readiness: 0.05
---

# Identity And Conflict Analysis: Leonidas Arriagada

## Blockers First

1. Page-image QA blocker: the assigned staged draft and source packet both report that QC requested `reread-page`; the rendered page image path recorded in the chunk is not present locally. This run also found `raw/codex-conversion-jobs/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-164-183/page-images/page-0175.jpg` absent.
2. Evidence-control blocker: the literal evidence is derivative converted/chunk text only. The heading has an OCR/orthography issue (`Historia ¡ Jeografia` for expected `Historia i Jeografia`), so the subject heading and institutional boundary need image certification before any role claim is promoted.
3. Identity-bridge blocker: the staged identity draft names only `Leonidas Arriagada` as a `Suplente`. It gives no age, birth, death, residence, parent, spouse, child, occupation outside the list role, or same-person bridge.
4. Anti-conflation blocker: local wiki context includes Arriagada/Pulgar names, but this staged draft does not name `Pulgar`, `Dario`, `Arturo`, `Jose`, `Juana`, `Smith`, Alexander John Heinz, or any relationship. Do not attach this mention to Pulgar-line people by surname association.

## Reviewed Evidence

- Staged identity draft: `research/_staging/identity/ID-STAGE-CHUNK-d5a8b8204fe4-P0175-01-leonidas-arriagada.md`.
- Source packet: `research/_staging/source-packets/chunk-d5a8b8204fe4-p0175-01-leonidas-arriagada-historia-jeografia-suplente.md`.
- Assigned chunk: `raw/chunks/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-sess-5715d57272/page-0175-chunk-01.md`.
- Converted file cited by the staged draft: `raw/converted/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-164-183.codex.md`.
- Canonical wiki context searched/reviewed by name: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, `wiki/sources/user-family-knowledge-2026-05-20.md`, and related index/search hits.

## Literal Reading

The staged identity draft preserves this converted reading:

```text
## Historia ¡ Jeografia
...
Suplentes:
...
- » Leonidas Arriagada.
```

The source packet and assigned chunk preserve the broader same list:

```text
## Historia ¡ Jeografia

Propietarios:

don Samuel Zenteno.

- » Moises Gonzalez R.

dona Amalia Melo de Oviedo.

Suplentes:

don Apolinario Puga.

- » Leonidas Arriagada.
```

Interpretation kept separate: this derivative text supports only a possible page-local person named `Leonidas Arriagada` listed as a substitute/suplente under the `Historia i/¡ Jeografia` subject heading. It does not establish kinship, a duplicate identity, or a canonical family attachment.

## Hypotheses

### H1: Page-Local Leonidas Arriagada

Hypothesis: the staged draft refers to a page-local named person, `Leonidas Arriagada`, listed as a `Suplente` for `Historia i Jeografia`.

Evidence supporting H1:

- The staged identity draft, source packet, and assigned chunk all contain the same name line, `Leonidas Arriagada`.
- The name appears in a structured list section with `Propietarios` and `Suplentes`, which is coherent with the staged interpretation of a list role.
- No direct contradiction to the name line was found in the reviewed local staged/canonical context.

Evidence limiting H1:

- The page image is unavailable in this workspace, so the name and surrounding layout have not been visually certified.
- The converted text has heading noise (`¡`), and the source packet notes uncertainty about the exact institution boundary on page 175.
- There is no genealogical identifier beyond the name and role/list placement.

Rank: best supported, but held. Claim probability 0.55 from derivative text; promotion probability 0.05 until image QA.

### H2: Same Person As Existing Arriagada Or Pulgar-Arriagada Candidate

Hypothesis: `Leonidas Arriagada` is the same person as, or a duplicate of, an existing local Arriagada/Pulgar-Arriagada person.

Evidence supporting H2:

- The surname `Arriagada` overlaps with canonical/staged local context, including `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, and `Dario/Dario Pulgar Arriagada`.

Evidence against H2:

- The given name `Leonidas` does not match `Juana`, `Jose`, `Dario`, `Arturo`, or the canonical `Dario Arturo Pulgar-Smith` identity.
- The staged draft does not state a family relationship, residence, birth date, occupation bridge, parent/child link, spouse, or other identifier that would connect this person to any reviewed canonical Arriagada/Pulgar person.
- No canonical `Leonidas Arriagada` page was found in `wiki/people`.

Rank: unsupported as a merge/duplicate. Claim probability 0.03; canonical readiness 0.00.

### H3: Pulgar-Line Bridge

Hypothesis: this page-local `Leonidas Arriagada` mention helps identify or connect one of the Pulgar-line candidates named in the controller contract.

Required explicit Pulgar-line comparison:

| Candidate | Ranking From This Staged Draft | Reason |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Do not attach; probability 0.01. | Canonical page is family-supplied maternal-grandfather context; this staged draft names only `Leonidas Arriagada`. |
| `Dario Arturo Pulgar` | Do not attach; probability 0.01. | Staged CV contexts use this name as a document subject; this page has no Dario, Arturo, CV, or biographical bridge. |
| `Dario Jose Pulgar-Arriagada` | Do not attach; probability 0.01. | No `Dario`, `Jose`, or `Pulgar-Arriagada` string appears in the assigned draft. |
| `Dario/Dario Pulgar Arriagada` | Do not attach; probability 0.01. | Existing local context includes `Dario/Dario Pulgar Arriagada` variants, but the assigned page names only `Leonidas Arriagada`. |
| `Jose del Carmen Pulgar` parent candidate | Do not attach; probability 0.00. | No Jose or parent statement appears. |
| `Juana Arriagada de Pulgar` parent candidate | Do not attach; probability 0.02. | Surname overlap only; no Juana, mother, spouse, or parent-child statement appears. |
| `Juana de Dios Amagada de Pulgar` parent candidate | Do not attach; probability 0.00. | No Juana/de Dios/Amagada/Pulgar parent evidence appears. |

Exact proof-review step needed next: first run targeted conversion QA for source page 175 to certify the page image reading and institutional boundary. Any later Pulgar-line attachment would require a separate identity-bridge proof review citing direct evidence that names both `Leonidas Arriagada` and the proposed Pulgar-line person or relationship. This staged draft cannot supply that bridge.

## Conflicts

- Same-person conflict: none established. The only supported identity treatment is a page-local `Leonidas Arriagada` lead.
- Duplicate-person conflict: no canonical `Leonidas Arriagada` page was found; duplicate risk is future-facing if a page is created before conversion QA.
- Name-variant conflict: none established for the person name. The heading `Historia ¡ Jeografia` is a conversion/heading issue, not a `Leonidas Arriagada` name variant.
- Relationship conflict: none stated in the assigned draft. Do not infer kinship from the Arriagada surname.
- Chronology conflict: none testable from this evidence. The source date is September 1918, but no age, life dates, or event chronology are stated for Leonidas.
- Conversion conflict: material hold. The chunk records a page image path, but the image is absent locally and the source packet records `conversion_confidence: low`.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Identity confidence, page-local `Leonidas Arriagada` | 0.55 | Multiple derivative staged records agree on the name line, but image QA is missing and identifiers are sparse. |
| Identity confidence, same as any reviewed Pulgar-line person | 0.01 | No direct name, relationship, or chronology bridge. |
| Conflict severity | 0.70 | High promotion risk because missing page-image QA and surname overlap could invite false attachment. |
| Evidence quality | 0.35 | Coherent derivative text, but no visual certification and no independent identifiers. |
| Conversion confidence | 0.25 | Staged draft/source packet mark low confidence; page image absent; heading has OCR noise. |
| Claim probability, narrow role/listing after QA | 0.55 | Plausible from derivative text only. |
| Claim probability, genealogical relationship | 0.00 | No relationship is stated. |
| Relevance to family tree | 0.15 | Arriagada surname is locally relevant, but no family bridge appears. |
| Canonical readiness | 0.05 | Not ready for canonical page, relationship, merge, or promoted fact. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-d5a8b8204fe4-P0175-01`: locate or regenerate the rendered page-175 image, compare it against the chunk and converted Markdown, and certify the exact spelling of `Leonidas Arriagada`, the `Suplentes` grouping, the `Historia i Jeografia` heading, and the controlling institution section. If certified, send only a narrow page-local role/listing claim to proof review. Do not create, merge, rename, or attach any canonical family identity, Pulgar-line bridge, Jose/Juana parent link, or relationship from this staged draft.
