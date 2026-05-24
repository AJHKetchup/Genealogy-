---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-3a644a5ca910-p0011-01-page-reference-and-signature-qa.md"
worker: postconv-identity-analysis-20260524213826470
staged_draft: "research/_staging/conflicts/chunk-3a644a5ca910-p0011-01-page-reference-and-signature-qa.md"
subject: "El Fundo Los Cuartos page for Dr. Dario Pulgar A."
source_packet: "research/_staging/source-packets/chunk-3a644a5ca910-p0011-01-dario-pulgar-a-fundo-los-cuartos.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md"
chunk_id: "CHUNK-3a644a5ca910-P0011-01"
canonical_readiness: hold_for_conversion_qa_and_identity_bridge
---

# Identity/Conflict Analysis: Page Reference And Signature QA

## Blockers First

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-3a644a5ca910-p0011-01-page-reference-and-signature-qa.md`.
- Page provenance is not stable enough for promotion: the chunk path/frontmatter uses `page_start: 11`, but the chunk's page metadata says printed page `14`, and the conversion job's `page-markdown/page-0014.md` contains the `EL FUNDO LOS CUARTOS` article. `page-markdown/page-0011.md` is a different page about electricity and milk processing.
- The local conversion job's `page-images` directory contains only `page-0004.jpg`; no local page image for page 11 or page 14 was available for this analysis. This blocks visual reread of page number, typed name line, and signature.
- The typed article line is transcribed as `DR DARIO PULGAR A,`; the staged draft/source packet/chunk preserve a signature reading as `DR. DARIO PULGARA`, while the conversion job `page-markdown/page-0014.md` preserves it as `DR. DARIO PULGARA`. This may be a spacing artifact for `Pulgar A.`, but it cannot be silently normalized.
- The source states inheritance from unnamed parents around 1917, but it does not name Jose, Juana, a spouse, child, or relationship to Alexander John Heinz.
- Do not merge this item with `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, either 1953 Dario Pulgar passenger, or Jose/Juana parent candidates by name alone.

## Literal Source Readings

The assigned source packet and chunk give this body text:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

They separately preserve the handwritten signature as:

```text
[handwritten signature] DR. DARIO PULGARA [/handwritten signature]
```

Literal reading only: the article names `Dr Dario Pulgar A.` as owner of Fundo Los Cuartos, calls him a distinguished physician of Concepcion, and says he inherited the fundo from his parents around 1917. Interpretation kept separate: `PULGARA` may represent `Pulgar A.` with no spacing, and `A.` may eventually be an abbreviated second surname, but the current evidence does not prove `Arriagada`, `Arturo`, `Smith`, `Jose`, or any named parent.

## Hypotheses

### 1. Held Page-Local Subject: `Dr. Dario Pulgar A.`

Supporting evidence:

- The assigned chunk, aggregate converted file, and conversion job `page-markdown/page-0014.md` all place `DR DARIO PULGAR A` in the `EL FUNDO LOS CUARTOS` article.
- The same local article context describes the subject as a physician of Concepcion and owner of Fundo Los Cuartos.
- The article's inheritance language is meaningful context for later property/family review, while remaining limited to unnamed parents.

Conflicts and limits:

- Page citation is unstable because this task is keyed to page 11 while the content is printed/conversion page 14.
- The signature still needs visual QA before `PULGARA` is treated as an alternate name or corrected to `Pulgar A.`.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong page-local name and role, with unresolved page/signature QA. |
| conflict_severity | 0.48 | Moderate while held; high only if promoted or merged prematurely. |
| evidence_quality | 0.62 | Direct derivative transcription from a local source, but no image reread. |
| conversion_confidence | 0.50 | Body text agrees across derivatives; page reference and signature conflict lower confidence. |
| claim_probability | 0.80 | Probable that the page names a physician/property owner as `Dr Dario Pulgar A.`. |
| relevance | 1.00 | Directly relevant to the staged conflict draft. |
| canonical_readiness | 0.10 | Hold for conversion QA and identity bridge review. |

### 2. Signature `PULGARA` Is The Same Person As `Pulgar A.`

Supporting evidence:

- The typed name and handwritten signature occur on the same article page.
- `PULGARA` is visually and textually close to `PULGAR A`, and the staged draft itself flags this as a signature/name-form QA issue.
- Conversion job `page-markdown/page-0014.md` also records the signature as `DR. DARIO PULGARA`, supporting the need to preserve the literal derivative reading.

Conflicts and limits:

- Without the page image, the analysis cannot decide whether the signature is `Pulgara`, `Pulgar A.`, or another form.
- Promoting `Pulgara` as a separate surname could create a false duplicate person.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Same-page context favors one person, exact name form unresolved. |
| conflict_severity | 0.55 | Name-variant risk is material for canonical pages. |
| evidence_quality | 0.48 | Derivative handwriting transcription only. |
| conversion_confidence | 0.34 | Signature is the lowest-confidence element. |
| claim_probability | 0.68 | Likely same page-local subject, not proof-ready as a variant. |
| relevance | 0.98 | Central to the staged draft. |
| canonical_readiness | 0.00 | No name-variant promotion yet. |

### 3. Same Older Medical/Property Cluster As `Dario J. Pulgar Arriagada` Or `Dario Jose Pulgar-Arriagada`

Supporting evidence:

- The article uses `Dr` and `facultativo de Concepcion`.
- Existing staged medical-title evidence names `Darío J. Pulgar Arriagada` under `Médicos-Cirujanos` in a 2 September 1918 session, with high confidence for that narrow name/title line.
- `Pulgar A.` could later prove to abbreviate `Pulgar Arriagada`.

Conflicts and limits:

- This article does not print `Arriagada`, `Jose`, or `J.`.
- The page reference/signature issue must be resolved before any identity-bridge comparison.
- `Dario Jose Pulgar-Arriagada` remains a separate local hypothesis unless a reviewed source explicitly bridges the names.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Medical context and `A.` are suggestive but not direct. |
| conflict_severity | 0.70 | Expanding `A.` without proof risks conflating name clusters. |
| evidence_quality | 0.50 | Comparison evidence is useful but not bridging. |
| conversion_confidence | 0.45 | Current page QA remains unresolved. |
| claim_probability | 0.34 | Possible older medical hypothesis, not proved. |
| relevance | 0.92 | Required Pulgar-line comparison. |
| canonical_readiness | 0.02 | Preserve as hypothesis only. |

### 4. Same As `Dario Arturo Pulgar` Or Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- Broad name overlap exists: `Dario` and `Pulgar`.
- The canonical `Dario Arturo Pulgar-Smith` page represents Alexander John Heinz's maternal grandfather from family-supplied knowledge and explicitly warns against automatic attachment of similar Dario/Pulgar records.
- CV staging elsewhere uses the document-level form `Dario Arturo Pulgar`, but still requires an identity bridge to the canonical Pulgar-Smith page.

Conflicts and limits:

- This article does not state `Arturo`, `Smith`, `Pulgar-Smith`, a CV context, Alexander John Heinz, spouse, child, or grandchild.
- The older physician/property/inheritance context is not an identity bridge to the CV/Pulgar-Smith cluster.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.80 | False attachment would contaminate the central family-supplied profile. |
| evidence_quality | 0.38 | Canonical context is real but not source-linked here. |
| conversion_confidence | 0.50 | Page QA cannot supply missing `Arturo`/`Smith` evidence. |
| claim_probability | 0.10 | Unsupported by this source. |
| relevance | 0.90 | Required anti-conflation check. |
| canonical_readiness | 0.00 | Do not attach to Pulgar-Smith or CV subject. |

### 5. Same As Canonical `Darío Pulgar Arriagada` Legal-Notice Cluster

Supporting evidence:

- `Pulgar A.` could theoretically stand for `Pulgar Arriagada`.
- The canonical `Darío Pulgar Arriagada` page has a separate 2000 Serviu Región del Bío Bío expropriation-event evidence snapshot.

Conflicts and limits:

- The 2000 legal-notice page gives no age, profession, Fundo Los Cuartos connection, inheritance statement, or bridge to this article.
- Older physician/property evidence and a 2000 legal notice should remain separate unless a vital-date or property-chain proof resolves chronology and identity.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Only broad name/initial overlap. |
| conflict_severity | 0.82 | Serious chronology and duplicate-person risk if merged. |
| evidence_quality | 0.42 | Each source supports a narrow separate claim, not a bridge. |
| conversion_confidence | 0.50 | Current page QA remains open; 2000 notice is separate. |
| claim_probability | 0.08 | Low without property-continuity or vital evidence. |
| relevance | 0.82 | Relevant because of possible `A.` expansion. |
| canonical_readiness | 0.00 | Do not merge. |

### 6. Jose/Juana Parent Candidates Explain The Unnamed Parents

Supporting evidence:

- The article says the subject inherited Fundo Los Cuartos from `sus padres` around 1917.
- Existing local context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- This article names no father or mother.
- Existing Jose/Juana candidates belong to separate birth-register clusters with their own conversion and relationship-review issues.
- Family-context hints justify a targeted double-check, not a parent-child promotion.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No named parent evidence. |
| conflict_severity | 0.66 | Unsupported parent assignment would create relationship conflicts. |
| evidence_quality | 0.28 | Only an unnamed-parent phrase plus separate local context. |
| conversion_confidence | 0.42 | Inheritance phrase is derivative and page QA remains open. |
| claim_probability | 0.04 | Named Jose/Juana relationship is not supported. |
| relevance | 0.74 | Relevant because the article mentions parents. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person conflict: unresolved between page-local `Dr Dario Pulgar A.` and other Dario/Pulgar clusters. The best narrow identity is the page-local physician/property owner.
- Duplicate-person risk: high if `PULGARA`, `Pulgar A.`, Pulgar-Arriagada, Pulgar-Smith, CV, passenger, or Jose/Juana clusters are merged by name or family context alone.
- Name-variant conflict: active. The current literal forms are `Dario Pulgar A.` and derivative-signature `Dario Pulgara`; neither `A. = Arriagada` nor `A. = Arturo` is proved.
- Relationship conflict: the article supports only unnamed parents by inheritance context. No Jose/Juana parent relationship is promotable.
- Chronology conflict: no internal chronology conflict on the page. Chronology becomes risky only if this older physician/property context is attached to later CV/Pulgar-Smith, passenger, or 2000 Arriagada contexts without a bridge.
- Conversion conflict: page reference is the strongest blocker. The task/chunk path says page 11, but the content aligns with printed/conversion page 14; the page image needed for direct review is absent locally.

## Ranked Hypotheses

| rank | hypothesis | probability | next action |
| ---: | --- | ---: | --- |
| 1 | Page-local subject is `Dr. Dario Pulgar A.`, owner of Fundo Los Cuartos and physician of Concepcion. | 0.80 | Resolve page 11 versus printed/conversion page 14 and visually reread page 14. |
| 2 | Signature `PULGARA` is a no-space/stylized reading of `Pulgar A.` for the same person. | 0.68 | Reread the signature from the source image; do not promote as a variant yet. |
| 3 | Same older medical cluster as `Dario J. Pulgar Arriagada` / possible `Dario Jose Pulgar-Arriagada`. | 0.34 | After conversion QA, run a separate identity bridge proof review comparing full name, title, place, and chronology. |
| 4 | Same as canonical `Dario Arturo Pulgar-Smith` or staged CV `Dario Arturo Pulgar`. | 0.10 | Reject for promotion unless a reviewed source explicitly bridges the physician/property owner to Arturo/Smith. |
| 5 | Same as later canonical `Darío Pulgar Arriagada` legal-notice person. | 0.08 | Do not merge; require vital-date or property-chain evidence. |
| 6 | Jose/Juana candidates are the unnamed parents. | 0.04 | No relationship action; require a source naming Dario's parents. |

## Recommended Next Action

Keep the staged conflict draft on hold for conversion QA. The exact next proof-review step is a page-reference and image-reread task for `El Aguila Nombre Grande Scan.pdf`: reconcile why `CHUNK-3a644a5ca910-P0011-01` points to page-start 11 while the content and conversion job page-markdown identify printed/source page 14, restore or locate the page 14 image, and visually decide whether the typed line/signature read `DR DARIO PULGAR A`, `DR. DARIO PULGARA`, or another literal form.

After that, promote only narrow source-local claims if verified: confirmed name form, physician of Concepcion, ownership of Fundo Los Cuartos, inheritance from unnamed parents around 1917, and property description. Do not promote a canonical alternate name, merge, `Arriagada` expansion, `Arturo`/`Smith` attachment, or Jose/Juana parent relationship until a separate identity-bridge proof review supplies direct evidence.
