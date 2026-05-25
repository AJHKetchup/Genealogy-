---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525092627833
task_id: "identity-analysis:research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md"
staged_draft: "research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md"
subject: "Dr. Dario Pulgar A. / DR. DARIO PULGARA"
source_packet: "research/_staging/source-packets/chunk-4177939279cb-p0011-01-el-aguila-fundo-los-cuartos-dario-pulgar-a.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md"
chunk_id: "CHUNK-4177939279cb-P0011-01"
page_reference: "assigned source page 11; chunk Page Metadata says printed page 14"
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Page Reference And Signature QA

## Blockers First

- The exact staged draft reviewed here is `research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md`.
- Page reference is unresolved: the task and chunk path are keyed to page 11, while the chunk body, converted aggregate, and handwritten marginalia identify the article as printed page 14.
- The page image needed for visual reread was not available to the staged extraction workers. This blocks verification of both the typed `PULGAR A` spacing and the handwritten-signature reading transcribed as `DR. DARIO PULGARA`.
- The page does not state `Arturo`, `Smith`, `Jose`, `J.`, `Arriagada`, `Pulgar-Smith`, birth date, spouse, child, grandchild, or named parents.
- The phrase `heredo de sus padres` is literal inheritance context only. It does not identify Jose or Juana parent candidates.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged conflict drafts, reviewed notes, or canonical wiki pages were edited.

## Literal Source Reading

The referenced chunk and source packet transcribe the article body as naming:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL ANO 1917
```

The same conversion-derived materials transcribe the bottom-right handwritten signature as:

```text
[signature] DR. DARIO PULGARA [/signature]
```

Literal reading: the converted page says Fundo Los Cuartos belonged to `DR DARIO PULGAR A`, describes him as a distinguished medical professional of Concepcion, and says he inherited the fundo from unnamed parents around 1917. The converted signature note says `DR. DARIO PULGARA`, but that reading is unverified until image reread.

Interpretation kept separate: `PULGARA` may be a true signature form, a tight-spacing rendering of `Pulgar A.`, or a conversion/transcription artifact. The current evidence does not prove what `A.` stands for.

## Hypothesis 1: Page-Local `Dr. Dario Pulgar A.` Candidate

Hypothesis: the safest supported identity is a page-local person named in the article as `Dr. Dario Pulgar A.`, associated with Fundo Los Cuartos, Concepcion, and inheritance from unnamed parents.

Supporting evidence:

- The staged conflict draft, source packet, chunk, and converted aggregate agree that the typed article names `DR DARIO PULGAR A`.
- The article gives role/context: owner of Fundo Los Cuartos, `facultativo de Concepcion`, inherited the fundo from parents around 1917.
- This conclusion does not require expanding the initial or merging with any existing canonical profile.

Conflicts and limits:

- The task page key is page 11 while the content is printed page 14.
- The signature reading remains unverified.
- The article does not provide a full second surname or family relationship bridge.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.76 | Strong local agreement on the typed article name; image QA still pending. |
| conflict_severity | 0.42 | Moderate because the conflict is mostly page/name-form unless merged prematurely. |
| evidence_quality | 0.60 | Direct article text, but only through conversion-derived local materials. |
| conversion_confidence | 0.48 | Body text is consistent; page-reference and signature QA are unresolved. |
| claim_probability | 0.78 | Probable narrow page-local identification as `Dr Dario Pulgar A.`. |
| relevance | 1.00 | Directly addresses the assigned conflict draft. |
| canonical_readiness | 0.12 | Hold for conversion QA before promotion or identity bridge. |

## Hypothesis 2: Typed And Signature Forms Refer To One Person

Hypothesis: `DR DARIO PULGAR A` in the typed article and `DR. DARIO PULGARA` in the signature note refer to the same page-local person, with the signature likely affected by spacing or transcription.

Supporting evidence:

- Both name forms appear in the same article/page context.
- `Pulgar A.` and `Pulgara` are visually plausible near-readings when a final initial follows the surname closely.
- Prior local notes on the same El Aguila page treat this as a name-form watch rather than two separate people.

Conflicts and limits:

- The signature was not visually reread from the page image.
- A true `Pulgara` form cannot be excluded from derivative text alone.
- Even if the forms refer to one page-local person, that does not identify the full canonical person.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Same-page context supports one person, but the signature is not proof-reviewed. |
| conflict_severity | 0.50 | Moderate risk of false name variant or duplicate if promoted as-is. |
| evidence_quality | 0.45 | Derivative transcription only for the handwritten signature. |
| conversion_confidence | 0.36 | The exact disputed reading is the conversion-sensitive part. |
| claim_probability | 0.68 | Probable same page-local person, not proof-ready. |
| relevance | 0.96 | Central to the assigned signature/name conflict. |
| canonical_readiness | 0.08 | No canonical variant until image review. |

## Hypothesis 3: Same Older Medical Candidate As `Dario Pulgar A.` / Adult Medical Passenger Cluster

Hypothesis: the Fundo Los Cuartos subject may be the same older medical Dario represented elsewhere in local staging as `Dario Pulgar A.` or adult `Dario Pulgar` with medical occupation.

Supporting evidence:

- This page says `Dr Dario Pulgar A.` and `facultativo de Concepcion`.
- Local prior identity notes preserve an older medical/passenger cluster for `Dario Pulgar A.` and adult `Dario Pulgar`.
- Inheritance around 1917 is chronologically compatible with an adult professional by the late 1920s, but this is only context.

Conflicts and limits:

- This page gives no age, birth date, passenger-list context, or full second surname.
- Compared passenger and medical records have their own proof-review and image-QA limitations.
- The 1953 passenger context contains distinct adult and child `Dario Pulgar` entries, so name-only collapse is unsafe.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.50 | Medical title and initial align with an older cluster, but no bridge exists. |
| conflict_severity | 0.68 | Premature merge could conflate separate Dario Pulgar records. |
| evidence_quality | 0.46 | Indirect comparison across staged notes. |
| conversion_confidence | 0.42 | Current page and comparison records remain QA-sensitive. |
| claim_probability | 0.44 | Plausible working hypothesis only. |
| relevance | 0.90 | Important duplicate-person comparison. |
| canonical_readiness | 0.04 | No merge or canonical attachment. |

## Hypothesis 4: Same As `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada`

Hypothesis: `Dr Dario Pulgar A.` is a shortened form of `Dario Jose Pulgar-Arriagada` or `Dario J. Pulgar Arriagada`.

Supporting evidence:

- The initial `A.` could stand for `Arriagada`.
- The title `Dr.` and `facultativo` context are compatible with older medical/professional Pulgar-Arriagada leads preserved in local staging.

Conflicts and limits:

- The article does not print `Jose`, `J.`, or `Arriagada`.
- Existing `Dario Jose Pulgar-Arriagada` contexts are treated in local notes as metadata/title dependent or otherwise held unless an image/source line visibly identifies the person.
- `PULGARA` is not proof that `A.` means `Arriagada`.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Suggestive initial and profession only. |
| conflict_severity | 0.74 | High risk if an abbreviation is silently expanded. |
| evidence_quality | 0.38 | Compared evidence is indirect or held. |
| conversion_confidence | 0.38 | The decisive name form is not visually verified. |
| claim_probability | 0.28 | Live but unproved hypothesis. |
| relevance | 0.88 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | Preserve separately until direct bridge proof. |

## Hypothesis 5: Same As `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith`

Hypothesis: the page-local `Dr Dario Pulgar A.` is the same person as staged CV subject `Dario Arturo Pulgar` or canonical family-supplied `Dario Arturo Pulgar-Smith`.

Supporting evidence:

- Broad name overlap: `Dario Pulgar`.
- The canonical `Dario Arturo Pulgar-Smith` page exists as a family-supplied maternal-line person and explicitly flags Dario/Pulgar records for identity review before attachment.
- Local CV staging uses the document-level name `Dario Arturo Pulgar`.

Conflicts and limits:

- This page does not state `Arturo`, `Smith`, `Pulgar-Smith`, CV/work-history context, Alexander John Heinz, spouse, child, or grandchild.
- Existing CV/Pulgar-Smith analyses hold that bridge pending identity-bearing evidence.
- The older physician/property context should not be attached to the Pulgar-Smith profile by name alone.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.80 | Wrong attachment would place older property/medical evidence on a family-supplied person. |
| evidence_quality | 0.28 | No identity bridge in the assigned draft. |
| conversion_confidence | 0.42 | Conversion QA does not solve the identity gap. |
| claim_probability | 0.10 | Low from current local evidence. |
| relevance | 0.86 | Required because Pulgar-Smith is a central canonical candidate. |
| canonical_readiness | 0.00 | Do not attach to Pulgar-Smith or CV subject. |

## Hypothesis 6: Same As Canonical `Darío Pulgar Arriagada`

Hypothesis: this `Dr Dario Pulgar A.` is the same person as canonical `wiki/people/dar-o-pulgar-arriagada.md`, currently represented by a 2000 Serviu Región del Bío Bío expropriation event.

Supporting evidence:

- Broad name overlap: `Dario/Darío Pulgar`.
- `A.` could stand for `Arriagada`.

Conflicts and limits:

- The 2000 canonical page gives no age, occupation, Fundo Los Cuartos link, parentage, or property-chain bridge to this article.
- If the page-local doctor belongs to the older 1928/1953 medical cluster, a 2000 same-person merge would create serious chronology risk unless estate/vital evidence explains it.
- The current article does not mention Chiguayante, Serviu, expropriation, heirs, or successors.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Name/initial overlap only. |
| conflict_severity | 0.82 | High chronology and duplicate-person risk. |
| evidence_quality | 0.22 | No bridging fact between contexts. |
| conversion_confidence | 0.42 | `A.` is unresolved and cannot drive the merge. |
| claim_probability | 0.05 | Very low without property-chain or vital-date proof. |
| relevance | 0.72 | Required anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not merge. |

## Hypothesis 7: Jose/Juana Parent Candidates Are The Unnamed Parents

Hypothesis: the unnamed parents in the inheritance phrase can be identified as existing Jose/Juana parent candidates.

Supporting evidence:

- The article literally says Dario inherited Fundo Los Cuartos from `sus padres`.
- Existing wiki/staged context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- The article names neither parent.
- The existing Jose/Juana pages are separate birth-register or relationship contexts and do not identify this Dario as a child.
- Family-context hints justify a future check of property, probate, or vital records; they do not justify a parent-child promotion.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | No named-parent evidence. |
| conflict_severity | 0.70 | High risk of unsupported relationship creation. |
| evidence_quality | 0.20 | Only an unnamed-parent phrase on this page. |
| conversion_confidence | 0.50 | The phrase is relatively stable, but specific parent identity is absent. |
| claim_probability | 0.03 | Not supported for any named Jose/Juana candidate. |
| relevance | 0.76 | Required because the article mentions parents. |
| canonical_readiness | 0.00 | No relationship action supported. |

## Conflicts

- Same-person conflict: unresolved between page-local `Dr Dario Pulgar A.` and older medical/passenger Pulgar candidates.
- Duplicate-person risk: high if this item is merged into `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, canonical `Darío Pulgar Arriagada`, or 1953 adult/child passenger candidates by name alone.
- Name-variant conflict: the typed article supports only `Dario Pulgar A.`; the converted signature supports only an unverified watch reading `Dario Pulgara`. The page does not prove `A. = Arriagada`, `A. = Arturo`, or a separate `Pulgara` surname.
- Relationship conflict: `sus padres` is an unnamed-parent inheritance clue. It does not support Jose/Juana parent attachment.
- Chronology conflict: no direct contradiction within this page. Chronology becomes risky if the page-local doctor is merged with later CV/Pulgar-Smith or 2000 Arriagada clusters without vital-date/property-chain proof.
- Conversion conflict: page 11 assignment versus printed page 14 and missing image proof block canonical use.

## Ranked Hypotheses

| rank | hypothesis | probability | required next step |
| ---: | --- | ---: | --- |
| 1 | Page-local `Dr. Dario Pulgar A.` candidate | 0.78 | Reconcile page 11/page 14 and visually reread the typed article line. |
| 2 | Typed `PULGAR A` and signature `PULGARA` refer to the same page-local person | 0.68 | Image proof review of the bottom-right signature and spacing. |
| 3 | Same older medical candidate as `Dario Pulgar A.` / adult medical passenger cluster | 0.44 | After page QA, compare with proof-reviewed age, occupation, and full-name evidence. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` | 0.28 | Require explicit full-name or source-context bridge. |
| 5 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.10 | Require a reviewed identity-bearing source connecting this doctor/property subject to the CV/Pulgar-Smith profile. |
| 6 | Same as canonical `Darío Pulgar Arriagada` | 0.05 | Require vital-date or property-chain proof resolving chronology. |
| 7 | Existing Jose/Juana candidates are the unnamed parents | 0.03 | Require a source naming this Dario's parents. |

## Recommended Next Action

Keep the staged conflict draft on `hold_for_conversion_qa`. The exact next proof-review step is a targeted page-reference and image reread for `CHUNK-4177939279cb-P0011-01`: reconcile why the assigned source page is 11 while the converted/chunk content is printed page 14, then visually verify the typed `DR DARIO PULGAR A` line and the handwritten signature before any name-form or page-specific claim is promoted.

After that, run a separate identity-bridge proof review comparing the confirmed page-local person first against older medical `Dario Pulgar A.` / adult medical `Dario Pulgar` evidence, then against `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada`, then separately against `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, canonical `Darío Pulgar Arriagada`, and Jose/Juana parent candidates. Do not merge, rename, expand `A.`, attach to Pulgar-Smith, or promote named parent relationships from this draft alone.
