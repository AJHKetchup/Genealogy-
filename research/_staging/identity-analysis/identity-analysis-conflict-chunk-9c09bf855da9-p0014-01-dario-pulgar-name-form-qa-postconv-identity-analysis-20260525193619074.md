---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-name-form-qa.md"
worker: postconv-identity-analysis-20260525193619074
staged_draft: "research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-name-form-qa.md"
subject: "Dr Dario Pulgar A."
source_packet: "research/_staging/source-packets/chunk-9c09bf855da9-p0014-01-el-aguila-fundo-los-cuartos-dario-pulgar.md"
source_path: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0014-chunk-01.md"
chunk_id: "CHUNK-9c09bf855da9-P0014-01"
canonical_readiness: hold_for_conversion_qa_and_identity_bridge
---

# Identity/Conflict Analysis: Dario Pulgar Name Form QA

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/conflict-chunk-9c09bf855da9-p0014-01-dario-pulgar-name-form-qa.md`.
- The controller/source packet explicitly requests reread-page conversion QA before promotion. The job directory currently contains only `page-images/page-0004.jpg`; no local `page-0014.jpg` is available for independent visual review of the page-14 name line or signature.
- The literal derivative readings are not fully settled: typed body `DR DARIO PULGAR A` versus handwritten signature note `[Handwritten signature: DR. DARIO PULGARA]`.
- The page does not state `Arturo`, `Smith`, `Pulgar-Smith`, `Jose`, `J.`, full `Arriagada`, named parents, spouse, children, birth date, death date, or relationship to Alexander John Heinz.
- The inheritance phrase names only unnamed parents: `sus padres`. It cannot identify Jose/Juana parent candidates without a separate source.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, or canonical wiki pages were edited.

## Literal Evidence

From the staged conflict draft: literal support is `DR DARIO PULGAR A; [Handwritten signature: DR. DARIO PULGARA]`, with conversion confidence `low_to_medium`.

From the staged source packet and chunk:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

The chunk also preserves:

```text
[Handwritten signature: DR. DARIO PULGARA]
```

Literal reading: the derivative text supports a page-local person named in print as `Dr Dario Pulgar A.`, described as a distinguished physician of Concepcion and owner of Fundo Los Cuartos, inherited from unnamed parents around 1917. The signature reading is a watch item, not a controlled name variant yet.

## Hypothesis 1: Page-Local `Dr Dario Pulgar A.`

Evidence for:

- The staged draft, source packet, converted file, and chunk all preserve the typed article form `DR DARIO PULGAR A`.
- The same page links this person to Fundo Los Cuartos, Concepcion, and an inheritance from unnamed parents around 1917.
- Same-page context makes it probable that the article body and the bottom signature refer to the same page-local person, even though the signature reading needs visual QA.

Evidence against or limits:

- No visual reread of page 14 has confirmed the typed spacing or signature.
- The page does not expand `A.` or provide cross-source identity anchors.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.76 | Strong derivative agreement for the page-local subject, reduced by missing image reread. |
| conflict_severity | 0.36 | Low if kept page-local; higher if `A.` is expanded or merged. |
| evidence_quality | 0.62 | Direct article text, but derivative and single-source. |
| conversion_confidence | 0.48 | Body text is plausible; signature/name form remains low-to-medium. |
| claim_probability | 0.82 | Probable narrow claim for `Dr Dario Pulgar A.` as owner/physician. |
| relevance | 1.00 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.16 | Hold for page-image QA and identity bridge. |

## Hypothesis 2: Signature Is A Spacing Variant Of `Pulgar A.`

Evidence for:

- `PULGAR A` and `PULGARA` are visually and transcriptionally close.
- The staged draft itself frames the issue as separated surname plus initial versus a rendered `Pulgara` form.
- Same-page placement and matching `Dr Dario` context favor one person rather than two people.

Evidence against or limits:

- The signature is handwritten and not independently checked.
- `Pulgara` should not be promoted as a real surname variant unless visual reread confirms it.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Same-page context supports a spacing/signature issue, but image proof is absent. |
| conflict_severity | 0.52 | False variant promotion could create duplicate-person noise. |
| evidence_quality | 0.44 | Depends on derivative handwritten reading. |
| conversion_confidence | 0.30 | Signature is the weakest evidence point. |
| claim_probability | 0.62 | More likely than a distinct `Pulgara` surname, pending reread. |
| relevance | 0.96 | Central name-form conflict. |
| canonical_readiness | 0.04 | Do not promote as variant yet. |

## Hypothesis 3: Same Older Medical/Arriagada Cluster

Candidate scope: `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, and unhyphenated/accented `Dario/Darío Pulgar Arriagada`.

Evidence for:

- `Pulgar A.` could abbreviate `Pulgar Arriagada`.
- The page describes a doctor/physician; local staged context includes a `Dario Pulgar-Arriagada, Capitaine du Service de Santé` official-listing candidate and other older medical/Geneva/Pulgar-Arriagada watch items.
- The property/inheritance context is chronologically more plausible for an older professional Dario than for later unbridged CV pages.

Evidence against or limits:

- This page does not state `Arriagada`, `Jose`, or `J.`.
- Existing Pulgar-Arriagada evidence must be compared through proof-reviewed name, role, date, occupation, and chronology, not by an initial alone.
- The 2000 `Darío Pulgar Arriagada` legal-notice context remains especially risky for chronology/property conflation unless a property-chain, estate, or vital-date bridge is found.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.36 | Plausible comparison only; no explicit expansion appears here. |
| conflict_severity | 0.74 | High risk if `A.` is silently expanded to Arriagada. |
| evidence_quality | 0.46 | Indirect local context plus page-local medical title. |
| conversion_confidence | 0.42 | Depends on the unresolved `Pulgar A.`/signature read. |
| claim_probability | 0.32 | Live hypothesis, not proved. |
| relevance | 0.92 | Required Pulgar-line comparison. |
| canonical_readiness | 0.02 | No merge or canonical attachment. |

## Hypothesis 4: Same As `Dario Arturo Pulgar` Or `Dario Arturo Pulgar-Smith`

Evidence for:

- The names share `Dario Pulgar`.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is an existing family-supplied Pulgar-line profile, and staged CV work uses document-level `Dario Arturo Pulgar`.

Evidence against or limits:

- This page does not say `Arturo`, `Smith`, `Pulgar-Smith`, or Alexander John Heinz.
- Existing canonical context explicitly warns not to attach Dario/Pulgar/Pulgar-Arriagada records to `Dario Arturo Pulgar-Smith` without identity review.
- Local proof reviews of CV pages keep the bridge from document-level `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith` on hold; this page does not supply that bridge.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.80 | High risk of false attachment to the family-supplied canonical person. |
| evidence_quality | 0.30 | No page-local bridge evidence. |
| conversion_confidence | 0.46 | Name-form QA does not solve the missing Arturo/Smith bridge. |
| claim_probability | 0.10 | Unsupported on current evidence. |
| relevance | 0.90 | Required central Pulgar comparison. |
| canonical_readiness | 0.00 | Do not attach. |

## Hypothesis 5: Named Jose/Juana Parent Candidates Explain `Sus Padres`

Evidence for:

- The article says the fundo was inherited from `sus padres` around 1917.
- Existing wiki/staging context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` or uncertain Juana variants.

Evidence against or limits:

- The page does not name either parent.
- Existing Jose/Juana candidates belong to separate register-derived contexts and have their own conversion/proof-review limits.
- Family-context hints justify a later property, probate, or vital-record check; they do not justify a parent-child promotion from this page.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No named parent evidence. |
| conflict_severity | 0.68 | Unsupported parent attachment would create relationship conflicts. |
| evidence_quality | 0.24 | Only an unnamed-parent phrase. |
| conversion_confidence | 0.54 | Inheritance phrase is more stable than the signature, but still derivative. |
| claim_probability | 0.04 | No specific Jose/Juana identity is supported. |
| relevance | 0.72 | Relevant as an anti-conflation and future-check item. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflicts

- Same-person conflict: unresolved between page-local `Dr Dario Pulgar A.` and older medical/Pulgar-Arriagada candidates.
- Duplicate-person risk: high if this item is merged into `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or Jose/Juana parent clusters by name or family context alone.
- Name-variant conflict: active and narrow. The page supports a watch between `Pulgar A.` and `Pulgara`; it does not prove `A. = Arriagada`, `A. = Arturo`, or `Pulgara` as a surname.
- Relationship conflict: the source supports only unnamed parents. No Jose/Juana parent relationship is supported.
- Chronology conflict: none within this page-local claim. Chronology becomes material if the older physician/property context is merged with the 2000 legal-notice Arriagada cluster or later CV/Pulgar-Smith cluster without vital-date or property-chain proof.

## Ranked Hypotheses

| rank | hypothesis | probability | required next step |
| ---: | --- | ---: | --- |
| 1 | Page-local `Dr Dario Pulgar A.` owner/physician subject | 0.82 | Reread page 14 image and confirm typed name, punctuation, and signature. |
| 2 | `Pulgara` is a spacing/transcription artifact for `Pulgar A.` | 0.62 | Visual signature proof review before any variant claim. |
| 3 | Same older medical/Pulgar-Arriagada cluster (`Dario Jose`, `Dario J.`, `Dario/Darío Pulgar Arriagada`) | 0.32 | Separate identity bridge review using full names, roles, dates, occupation, and chronology after page QA. |
| 4 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.10 | Require a reviewed source explicitly connecting this doctor/Fundo Los Cuartos subject to the CV/Pulgar-Smith identity. |
| 5 | Named Jose/Juana parent candidates explain `sus padres` | 0.04 | Require a source naming Dario's parents and bridging them to this inheritance/property context. |

## Recommended Next Action

Keep this staged conflict on hold. The exact next proof-review step is targeted conversion QA for `CHUNK-9c09bf855da9-P0014-01`: locate or regenerate the page-14 image without editing conversion outputs, then visually decide whether the printed article reads `DR DARIO PULGAR A`, `DR DARIO PULGARA`, or another form, and whether the bottom signature reads `DR. DARIO PULGARA`, `DR. DARIO PULGAR A.`, or another form.

After QA, promote only the narrow literal claim if confirmed: `El Aguila` page 14 describes `Dr Dario Pulgar A.` as a distinguished physician of Concepcion and owner of Fundo Los Cuartos, inherited from unnamed parents around 1917. Do not merge people, expand `A.`, attach named parents, rename canonical pages, or promote facts to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or Jose/Juana candidates until a separate proof-reviewed identity bridge exists.
