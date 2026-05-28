---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d5a8b8204fe4-P0175-01-page-image-missing-qa.md"
agent: "postconv-identity-analysis-20260528213844970"
staged_draft: "research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d5a8b8204fe4-P0175-01-page-image-missing-qa.md"
subject: "Leonidas Arriagada"
chunk_id: CHUNK-d5a8b8204fe4-P0175-01
source_packet: "research/_staging/source-packets/chunk-d5a8b8204fe4-p0175-01-leonidas-arriagada-historia-jeografia-suplente.md"
chunk: "raw/chunks/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-sess-5715d57272/page-0175-chunk-01.md"
converted_file: "raw/converted/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-164-183.codex.md"
source: "raw/sources/Anales de la Universidad de Chile, Session of the Council of Public Instruction, September 1918..pdf"
page_reference: "source page 175"
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Leonidas Arriagada Page-Image QA Hold

## Blockers First

1. Page-image verification is blocked. The assigned staged draft reports that page 175 was flagged for `reread-page`, and the recorded rendered page image path is not present locally: `raw/codex-conversion-jobs/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-164-183/page-images/page-0175.jpg`.
2. Conversion confidence is low for promotion. The chunk is Docling `rough_ok`, but the subject heading appears with OCR noise as `Historia ¡ Jeografía` in the chunk, while staged notes normalize the intended reading to `Historia i Jeografia`.
3. The exact school/institution boundary is not proof-ready. The source packet reports surrounding context from `CHILLAN` / `LICEO DE NIÑAS` before page 175 and `LICEO AMERICANO DE SEÑORITAS` later on page 175, but the boundary needs image reread before a promoted role claim.
4. No same-person, duplicate-person, name-variant, relationship, or chronology conclusion can be promoted from this draft. The assigned source gives a page-local named-person listing only and does not state age, residence, parents, spouse, children, or later-life identity continuity.

## Literal Source Readings

- Staged conflict draft reviewed: `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d5a8b8204fe4-P0175-01-page-image-missing-qa.md`.
- Source packet reviewed: `research/_staging/source-packets/chunk-d5a8b8204fe4-p0175-01-leonidas-arriagada-historia-jeografia-suplente.md`.
- Chunk reviewed: `raw/chunks/ca753b8b14-anales-de-la-universidad-p0164-0183-anales-de-la-universidad-de-chile-sess-5715d57272/page-0175-chunk-01.md`.

Literal text preserved in the staged draft and source packet:

```text
Suplentes:

don Apolinario Puga.

- » Leonidas Arriagada.
```

Literal text in the chunk places that line under:

```text
## Historia ¡ Jeografía
```

Interpretation kept separate: the likely intended heading is `Historia i Jeografia`, and the role is likely a `Suplentes` listing, but both the heading and the exact institutional section require page-image QA before proof review or promotion.

## Hypotheses And Evidence

### H1: Page-Local Named Person, Leonidas Arriagada

Evidence supporting:

- The staged draft, source packet, chunk, claim draft, relationship review, and identity draft all preserve the same page-local name: `Leonidas Arriagada`.
- The line appears in a list structure with `Suplentes`, after `don Apolinario Puga`, under the subject heading rendered as `Historia ¡ Jeografía`.
- Local search found no existing canonical `Leonidas Arriagada` person page and no other staged identity-analysis note for this exact person outside the assigned page-175 staging set.

Evidence limiting:

- The page image is missing, so the exact name reading remains unverified.
- The listing supplies no age, residence, kinship, or biographical identifiers beyond the page-local role/list position.
- The institution boundary must be checked before any role claim is promoted.

Rank: strongest and only source-local hypothesis. Claim probability: 0.62 pending image reread. Identity confidence: 0.54 as a page-local person only.

### H2: Same Person As Another Arriagada Or Pulgar-Arriagada Person

Evidence supporting:

- The surname `Arriagada` overlaps with existing canonical and staged Pulgar-Arriagada context, including `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Darío Pulgar Arriagada`, and multiple Dario/Pulgar-Arriagada staging clusters.

Evidence against or limiting:

- The assigned draft names `Leonidas Arriagada`, not Juana, Jose, Dario, Pulgar, Pulgar-Arriagada, Pulgar-Smith, or any parent candidate.
- The source does not state a family relationship, residence, birth date, occupation beyond the list role, or any bridge to Pulgar-line records.
- Shared surname alone is not probative, especially where existing canonical pages already preserve separate Pulgar-Arriagada identities and warn against attachment by name alone.

Rank: weak surname-only hypothesis. Claim probability: 0.03 for any same-person or family attachment from this draft alone. Identity confidence: 0.02 for merging or attaching to another Arriagada/Pulgar-Arriagada person.

### H3: Same Person Or Direct Bridge To Pulgar-Line Dario Candidates

Required comparison because existing wiki context includes Pulgar-line candidates:

- `Dario Arturo Pulgar-Smith`: canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly cautions that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records need identity review before attachment. This staged draft does not name Dario, Arturo, Smith, Pulgar, or a relationship to Alexander John Heinz.
- `Dario Arturo Pulgar`: local staged CV/Habitat contexts use this name, but the assigned page-175 source does not mention a CV, Habitat, work history, or `Dario Arturo Pulgar`.
- `Dario Jose Pulgar-Arriagada`: local staged photo/ICRC contexts use this form, but the assigned source does not name Dario Jose or Pulgar-Arriagada.
- `Dario/Dario Pulgar Arriagada`: existing staged/canonical context includes `Darío Pulgar Arriagada` and related name variants, but the assigned source names `Leonidas Arriagada` only.
- Jose/Juana parent candidates: canonical context includes `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`; the assigned source does not name any Jose or Juana candidate and states no parent-child relationship.

Rank: unsupported for this staged draft. Claim probability: 0.00 to 0.01 for direct attachment from this evidence alone. Exact next step before any attachment would be a separate identity-bridge proof review using direct evidence that names both the page-local `Leonidas Arriagada` and the proposed Pulgar-line person or relationship.

## Conflicts

- Same-person conflict: none established; the only safe treatment is a page-local `Leonidas Arriagada` lead.
- Duplicate-person risk: low if held as a page-local lead; high if merged with Arriagada or Pulgar-Arriagada persons by surname alone.
- Name-variant conflict: none proved. The source does not provide variant forms for Leonidas. It does contain OCR noise in the subject heading, not a person-name variant.
- Relationship conflict: none stated. The companion relationship draft correctly records no family relationship stated.
- Chronology conflict: none from this source alone. Chronology would become a conflict only if this 1918 school/personnel listing were attached to a later or earlier person without a direct bridge.
- Conversion conflict: material blocker. Page image unavailable and reread required before promotion.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| identity confidence, page-local Leonidas Arriagada | 0.54 | Repeated derivative/staged text agrees on the name, but image verification is missing and identifiers are sparse. |
| identity confidence, same as another Arriagada/Pulgar-line person | 0.02 | Only surname overlap; no direct bridge. |
| conflict severity | 0.58 | No genealogical contradiction, but conversion QA materially blocks promotion. |
| evidence quality | 0.42 | Local derivative evidence is consistent, but it is unverified against the missing page image. |
| conversion confidence | 0.30 | `rough_ok`, reread requested, image missing, OCR noise in heading. |
| claim probability, narrow role/listing claim after QA | 0.62 | The converted/chunk text supports the line, but the page image must confirm spelling, heading, and section boundary. |
| claim probability, relationship or identity bridge | 0.01 | No relationship or bridge is stated. |
| relevance | 0.45 | Relevant as an Arriagada name lead and conversion-QA item; low direct genealogical value until verified. |
| canonical readiness | 0.10 | Hold for conversion QA; do not promote identity, relationship, or canonical page changes. |

## Recommended Next Action

Run targeted conversion QA/proof-review follow-up for `CHUNK-d5a8b8204fe4-P0175-01`: locate or regenerate the rendered page-175 image, compare it against the converted text and chunk, and certify the exact spelling of `Leonidas Arriagada`, the `Suplentes` grouping, the `Historia i Jeografia` heading, and the controlling institution section. If confirmed, promote only a narrow role/listing claim. Do not merge with or attach to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, Jose/Juana parent candidates, or any other Arriagada person without a later source that supplies a direct identity or relationship bridge.
