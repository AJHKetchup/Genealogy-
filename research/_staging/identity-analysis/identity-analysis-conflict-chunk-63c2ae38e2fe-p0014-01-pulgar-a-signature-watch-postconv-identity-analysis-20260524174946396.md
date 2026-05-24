---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md"
worker: postconv-identity-analysis-20260524174946396
staged_conflict_draft: "research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md"
subject: "Dr. Dario Pulgar A."
source_packet: "research/_staging/source-packets/chunk-63c2ae38e2fe-p0014-01-dario-pulgar-los-cuartos.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0014-chunk-01.md"
chunk_id: "CHUNK-63c2ae38e2fe-P0014-01"
page_reference: "source page 14"
analysis_status: hold_for_conversion_qa
canonical_readiness: do_not_promote
---

# Identity And Conflict Analysis: Pulgar A. Signature Watch

## Blockers First

- This note analyzes the exact staged draft `research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md`.
- Do not promote the signature reading. The staged draft and source packet both report low confidence for the exact handwritten form because the queue requested `reread-page` and no page image for page 14 was found in the conversion job directory during extraction.
- There is a provenance mismatch to resolve before proof review: the staged draft/source packet cite `CHUNK-63c2ae38e2fe-P0014-01`, while the referenced chunk frontmatter currently reads `CHUNK-dfc1ae4668c1-P0014-01`.
- The article body names `DR DARIO PULGAR A`; the handwritten signature is transcribed as `DR. DARIO PULGARA`. This is a name-form/conversion conflict, not proof of a separate surname or duplicate person.
- The article says the subject inherited Fundo Los Cuartos from unnamed parents around 1917. It does not name Jose, Juana, Arturo, Smith, Arriagada, or any relationship.
- Existing local Pulgar context keeps `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, and Jose/Juana parent candidates as separate or unresolved clusters. This staged conflict cannot merge them by name alone.

## Literal Source Reading

The source packet quotes the page-local article as:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

The same packet separately records:

```text
[Handwritten signature in blue ink:] DR. DARIO PULGARA
```

Literal reading: page 14 supports a held, page-local subject named `Dr Dario Pulgar A.`, a physician of Concepcion, owner of Fundo Los Cuartos, with inheritance from unnamed parents around 1917. Interpretation kept separate: `PULGARA` may be a compressed or stylized `Pulgar A.` signature, but this must be checked against the page image.

## Hypothesis 1: `PULGARA` Is A Stylized Or Compressed `Pulgar A.`

Supporting evidence:

- The clearer typed article line reads `DR DARIO PULGAR A`.
- The staged conflict draft itself warns that the handwritten `PULGARA` may be `Pulgar A.` with a stylized or closely spaced final initial.
- The source packet describes the same article subject and signature location; there is no second named Pulgar person on the page.

Conflicts and limits:

- The derivative chunk currently preserves the signature as `DR. DARIO PULGARA`.
- No page image was available during extraction, so this remains an unresolved conversion/name-form watch.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Strong page-local alignment between article name and signature context; exact handwriting unresolved. |
| conflict_severity | 0.35 | Low if held as QA caution; material only if promoted as a separate name. |
| evidence_quality | 0.62 | Direct local transcription, but derivative and single-source. |
| conversion_confidence | 0.42 | Typed article is usable; signature and chunk-id mismatch reduce confidence. |
| claim_probability | 0.72 | Most likely current explanation for the `PULGARA` reading. |
| relevance | 1.00 | Directly addresses the assigned conflict. |
| canonical_readiness | 0.10 | Requires page-image proof review before any promotion. |

## Hypothesis 2: `PULGARA` Is A Literal Distinct Name Form

Supporting evidence:

- The chunk and source packet both transcribe the handwritten signature as `DR. DARIO PULGARA`.
- The staged conflict draft properly preserves the reading rather than normalizing it.

Conflicts and limits:

- The typed body has the stronger identity form `DR DARIO PULGAR A`.
- No reviewed local wiki or staged context found here supports `Pulgara` as a separate surname/person for this article.
- Promotion as a distinct name could create an unsupported duplicate-person or alternate-name conflict.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Rests on the lowest-confidence visual element. |
| conflict_severity | 0.70 | High risk if promoted as a distinct identity or surname. |
| evidence_quality | 0.30 | Needs direct image review. |
| conversion_confidence | 0.22 | Signature is the exact problem area. |
| claim_probability | 0.16 | Possible literal reading, but weaker than `Pulgar A.`. |
| relevance | 0.96 | Central to the staged conflict. |
| canonical_readiness | 0.00 | Do not promote. |

## Hypothesis 3: Same Older Medical/Property Candidate As `Dario Jose Pulgar-Arriagada` Or `Darío J. Pulgar Arriagada`

Supporting evidence:

- `Pulgar A.` could later prove to abbreviate `Pulgar Arriagada`, but this is only a hypothesis.
- Local staged context includes `Darío J. Pulgar Arriagada` as a `Médico-Cirujano` in a 1918 University of Chile session and `Dario Jose Pulgar-Arriagada` in 1929 ICRC/Geneva photograph metadata.
- A 1928 passenger-list source packet names `Dario Pulgar A.`, age 39, occupation `Medical Surgeon`, which is professionally compatible with the page-14 `facultativo de Concepcion` subject, but that packet is also on conversion QA hold.
- A hospital-history source packet lists `Darío Pulgar Arriagada` in a Concepcion hospital directors/subrogantes appendix.

Conflicts and limits:

- Page 14 does not spell `Arriagada`, `Jose`, or `J.`.
- Photograph identity for `Dario Jose Pulgar-Arriagada` is supplied by file/source title metadata, not visible text.
- The 1918, 1928, 1929, hospital, and Fundo Los Cuartos records need a reviewed identity bridge before any same-person claim.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.40 | Profession, place, and `A.` are suggestive, not conclusive. |
| conflict_severity | 0.68 | Expanding `A.` without proof would conflate clusters. |
| evidence_quality | 0.50 | Multiple local clues, but several are held for QA and none bridges identity. |
| conversion_confidence | 0.46 | Mixed: 1918 task is stronger; page 14 and passenger/photo packets need reread. |
| claim_probability | 0.36 | Plausible older medical/property hypothesis. |
| relevance | 0.92 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | No merge or name expansion. |

## Hypothesis 4: Same Person As Document-Level `Dario Arturo Pulgar` Or Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The names share `Dario` and `Pulgar`.
- The canonical page `wiki/people/dario-arturo-pulgar-smith.md` records a family-supplied maternal-grandfather identity and explicitly cautions against automatic attachment of Dario/Pulgar/Pulgar-Arriagada records.
- Local CV staging preserves `Dario Arturo Pulgar` as a document-level subject requiring identity-bridge review before attachment to the canonical Pulgar-Smith page.

Conflicts and limits:

- Page 14 does not state `Arturo`, `Smith`, `Pulgar-Smith`, family relationship to Alexander John Heinz, CV facts, spouse, child, or grandchild.
- The page-14 subject appears as an older Concepcion physician/property owner with inheritance around 1917; the CV/Pulgar-Smith cluster is not bridged by this draft.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.78 | Wrong attachment would contaminate a central canonical family page. |
| evidence_quality | 0.42 | Family-supplied page exists but does not connect to this source. |
| conversion_confidence | 0.44 | Reread may settle `Pulgar A.`, not `Arturo` or `Smith`. |
| claim_probability | 0.12 | Low on present local evidence. |
| relevance | 0.92 | Required Pulgar-line anti-conflation check. |
| canonical_readiness | 0.01 | Do not attach. |

## Hypothesis 5: Same As Later Canonical `Darío Pulgar Arriagada`

Supporting evidence:

- `Pulgar A.` might eventually expand to `Pulgar Arriagada`.
- The existing canonical page `wiki/people/dar-o-pulgar-arriagada.md` holds a narrow 2000-12-05 expropriation event for `Darío Pulgar Arriagada`.

Conflicts and limits:

- The 2000 expropriation page has no age, profession, Fundo Los Cuartos, parent, inheritance, or Concepcion physician bridge.
- A same-person merge would create a serious chronology caution unless vital dates or property-continuity evidence proves it.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.16 | Only possible surname expansion/name overlap. |
| conflict_severity | 0.80 | High chronology and property-context conflation risk. |
| evidence_quality | 0.46 | Separate narrow claims exist, not an identity bridge. |
| conversion_confidence | 0.50 | The later canonical event is clearer than the page-14 signature. |
| claim_probability | 0.12 | Unlikely without vital-date/property-continuity proof. |
| relevance | 0.82 | Relevant because of possible `A.` expansion. |
| canonical_readiness | 0.02 | Do not merge. |

## Hypothesis 6: Jose/Juana Parent Candidates Explain `Sus Padres`

Supporting evidence:

- Page 14 literally says `Dr Dario Pulgar A.` inherited the fundo from `sus padres` around 1917.
- Existing wiki/staged context includes Jose/Juana candidates: `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- Page 14 names no parent.
- The Jose/Juana candidates belong to separate birth-register/relationship clusters with their own proof and conversion issues.
- Family context supports only a targeted double-check, not a relationship claim.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | No named parent evidence on page 14. |
| conflict_severity | 0.66 | Parent assignment would be unsupported. |
| evidence_quality | 0.32 | Parent evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.38 | Related register context remains separately qualified. |
| claim_probability | 0.04 | Only unnamed-parent inheritance is supported. |
| relevance | 0.72 | Relevant because the article mentions parents. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person conflict: unresolved. The safest subject label is held page-local `Dr Dario Pulgar A.`.
- Duplicate-person risk: high if `PULGARA` is promoted as a separate person, or if page 14 is merged by name alone with Pulgar-Smith, Arturo, Jose/Arriagada, later Arriagada, passenger, medical, or parent clusters.
- Name-variant conflict: page 14 supports only a conflict between typed `Dario Pulgar A.` and converted signature `Dario Pulgara`; it does not prove `Arriagada`, `Arturo`, `Jose`, or `Smith` variants.
- Relationship conflict: the article supports only unnamed parents; no Jose/Juana parent relationship is promotable.
- Chronology conflict: the adult physician/property owner context and inheritance around 1917 make an older medical/property candidate plausible, but they caution against unreviewed attachment to later CV/Pulgar-Smith or 2000 Arriagada contexts.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Exact next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Signature is `Pulgar A.`/same page-local subject, not distinct `Pulgara` | 0.72 | Reread source page 14 image and verify signature spacing against the typed line. |
| 2 | Same older medical/property candidate as `Dario Jose Pulgar-Arriagada` / `Darío J. Pulgar Arriagada` / `Dario Pulgar A.` passenger-medical cluster | 0.36 | After page-14 reread, run a separate identity-bridge proof review using full name, occupation, age, Concepcion/hospital/property context, and dates. |
| 3 | Signature literally reads a distinct `Pulgara` name form | 0.16 | Hold only as a QA caution until visual proof review confirms the letters. |
| 4 | Same as later canonical `Darío Pulgar Arriagada` expropriation person | 0.12 | Require vital-date or property-continuity evidence before any merge. |
| 5 | Same as document-level `Dario Arturo Pulgar` or canonical `Dario Arturo Pulgar-Smith` | 0.12 | Require a reviewed identity bridge to `Arturo`/`Smith`; do not attach from this draft. |
| 6 | Jose/Juana candidates are the unnamed parents | 0.04 | Require a source naming this Dario's parents; do not infer from `sus padres`. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md` on hold as a proof-review caution. The exact next step is a page-image reread of source page 14 from `raw/sources/El Aguila Nombre Grande Scan.pdf`, plus a provenance audit reconciling the staged `CHUNK-63c2ae38e2fe-P0014-01` reference with the current chunk frontmatter `CHUNK-dfc1ae4668c1-P0014-01`.

If that review confirms the reading, promote only narrow claims for the verified name form, physician of Concepcion description, Fundo Los Cuartos ownership, and inheritance from unnamed parents around 1917. Do not promote a canonical alternate name, `Pulgara` surname, person merge, `Arriagada` expansion, `Arturo`/`Smith` attachment, or Jose/Juana parent relationship from this staged conflict draft.
