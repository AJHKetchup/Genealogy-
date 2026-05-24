---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-3a644a5ca910-p0011-01-page-reference-and-signature-qa.md"
worker: postconv-identity-analysis-20260524214722639
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

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-3a644a5ca910-p0011-01-page-reference-and-signature-qa.md`.
- Page provenance is unresolved. The assigned chunk path/frontmatter uses `page_start: 11`, but the chunk body says `Page number: 14`; conversion-job `page-markdown/page-0014.md` contains the same `EL FUNDO LOS CUARTOS` article, while `page-markdown/page-0011.md` contains a different electricity and milk-processing article.
- The conversion manifest lists page images through page 18, including `page-0014.jpg`, but the local `page-images` directory currently contains only `page-0004.jpg`. No page 11 or page 14 image was available for visual reread in this task.
- The typed article line is transcribed as `DR DARIO PULGAR A,`; the signature note is transcribed as `DR. DARIO PULGARA`. This may be a no-space `Pulgar A.` reading, but it cannot be silently normalized without image review.
- The article says the subject inherited the fundo from `sus padres` around 1917, but it does not name father, mother, spouse, child, or relationship to Alexander John Heinz.
- Do not merge this evidence into `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, canonical `Dario Pulgar Arriagada`, adult/child passenger `Dario Pulgar` pages, or Jose/Juana parent candidates by name alone.

## Literal Source Readings

The source packet and assigned chunk preserve this article text:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

They separately preserve this signature reading:

```text
[handwritten signature] DR. DARIO PULGARA [/handwritten signature]
```

Literal reading only: the derivative text names `Dr Dario Pulgar A.` as owner of Fundo Los Cuartos, describes him as a distinguished physician of Concepcion, and says he inherited the property from unnamed parents around 1917. Interpretation kept separate: `PULGARA` may represent `Pulgar A.`, and `A.` may later prove to abbreviate a second surname, but this source does not prove `Arriagada`, `Arturo`, `Smith`, `Jose`, `Juana`, or any named parent.

## Evidence Supporting Each Hypothesis

### 1. Page-Local Subject: `Dr. Dario Pulgar A.`

Supporting evidence:

- The assigned chunk, source packet, aggregate converted file, and conversion-job `page-markdown/page-0014.md` all preserve the article body with `DR DARIO PULGAR A`.
- The same article describes this person as owner of Fundo Los Cuartos and a physician of Concepcion.
- The inheritance statement is relevant family/property context, but only as an unnamed-parent statement.

Conflicts and limits:

- The source citation is unstable until page 11 versus page 14 is reconciled.
- The page image needed to confirm the typed line, handwritten page number, and signature was unavailable locally.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong page-local typed name and role, weakened by page/signature QA. |
| conflict_severity | 0.48 | Moderate while held; high if promoted or merged prematurely. |
| evidence_quality | 0.62 | Direct derivative transcription from local converted/chunk files, but no image reread. |
| conversion_confidence | 0.50 | Body text agrees across derivatives; page reference and signature remain unresolved. |
| claim_probability | 0.80 | Probable that the page names a physician/property owner as `Dr Dario Pulgar A.`. |
| relevance | 1.00 | Directly relevant to the staged conflict draft. |
| canonical_readiness | 0.10 | Hold for conversion QA and identity bridge review. |

### 2. Signature `PULGARA` Refers To The Same Page-Local Person

Supporting evidence:

- The typed name and handwritten signature occur on the same article page in the derivative transcription.
- `PULGARA` is textually close to tightly spaced `PULGAR A`.
- The staged draft frames the issue as page/signature QA, not as proof of a separate person.

Conflicts and limits:

- No source image was available to decide whether the signature literally reads `Pulgara`, `Pulgar A.`, or another form.
- Promoting `Pulgara` as a separate surname or canonical variant could create a false duplicate or false alternate name.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Same-page context favors one person, exact literal form unresolved. |
| conflict_severity | 0.55 | Material name-variant risk for canonical pages. |
| evidence_quality | 0.48 | Derivative handwriting transcription only. |
| conversion_confidence | 0.34 | Signature is the lowest-confidence element. |
| claim_probability | 0.68 | Likely same page-local subject, not proof-ready as a variant. |
| relevance | 0.98 | Central to the staged draft. |
| canonical_readiness | 0.00 | No name-variant promotion yet. |

### 3. Same Older Medical Cluster As `Dario J. Pulgar Arriagada` / `Dario Jose Pulgar-Arriagada`

Supporting evidence:

- The article uses `Dr` and `facultativo de Concepcion`.
- Existing staged context includes a medical-title review task for `Dario J. Pulgar Arriagada` in a 2 September 1918 university session, and separate Pulgar-Arriagada identity work.
- `Pulgar A.` could eventually prove to abbreviate `Pulgar Arriagada`.

Conflicts and limits:

- This article does not print `Arriagada`, `Jose`, or `J.`.
- The current page/signature conflict must be resolved before a reliable identity bridge can be attempted.
- `A.` cannot be expanded to `Arriagada` from family context alone.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Medical context and `A.` are suggestive but indirect. |
| conflict_severity | 0.70 | Expanding `A.` without proof risks conflating older Pulgar clusters. |
| evidence_quality | 0.50 | Comparison evidence is useful but not directly bridging. |
| conversion_confidence | 0.45 | Page/signature QA remains unresolved. |
| claim_probability | 0.34 | Possible older medical hypothesis, not proved. |
| relevance | 0.92 | Required Pulgar-line comparison. |
| canonical_readiness | 0.02 | Preserve as hypothesis only. |

### 4. Same As `Dario Arturo Pulgar` Or Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- Broad name overlap exists: `Dario` and `Pulgar`.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is a family-supplied Pulgar-Smith profile and explicitly warns not to automatically merge similarly named Dario/Pulgar records.
- CV staging elsewhere uses `Dario Arturo Pulgar`, but those notes still require identity-bridge proof before attachment to canonical Pulgar-Smith.

Conflicts and limits:

- This article does not state `Arturo`, `Smith`, `Pulgar-Smith`, a CV context, Alexander John Heinz, spouse, child, or grandchild.
- The older physician/property context is not an identity bridge to the later CV/Pulgar-Smith cluster.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.80 | False attachment would contaminate a central family-supplied profile. |
| evidence_quality | 0.38 | Canonical context is real but not source-linked to this article. |
| conversion_confidence | 0.50 | Page QA cannot supply missing `Arturo`/`Smith` evidence. |
| claim_probability | 0.10 | Unsupported by this source. |
| relevance | 0.90 | Required anti-conflation check. |
| canonical_readiness | 0.00 | Do not attach to Pulgar-Smith or the CV subject. |

### 5. Same As Canonical `Dario Pulgar Arriagada` Legal-Notice Cluster

Supporting evidence:

- `Pulgar A.` could theoretically stand for `Pulgar Arriagada`.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` has separate reviewed evidence for a 5 December 2000 Serviu Region del Bio Bio expropriation notice naming Dario Pulgar Arriagada.

Conflicts and limits:

- The 2000 legal-notice context gives no age, profession, Fundo Los Cuartos link, inheritance statement, or direct bridge to this article.
- Older physician/property evidence and a 2000 legal notice should remain separate unless vital-date or property-chain proof resolves identity and chronology.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Only broad name/initial overlap. |
| conflict_severity | 0.82 | Serious chronology and duplicate-person risk if merged. |
| evidence_quality | 0.42 | Each source supports a narrow separate claim, not a bridge. |
| conversion_confidence | 0.50 | Current page QA remains open. |
| claim_probability | 0.08 | Low without property-continuity or vital evidence. |
| relevance | 0.82 | Relevant because of possible `A.` expansion. |
| canonical_readiness | 0.00 | Do not merge. |

### 6. Jose/Juana Parent Candidates Explain The Unnamed Parents

Supporting evidence:

- The article says the subject inherited Fundo Los Cuartos from `sus padres` around 1917.
- Existing wiki context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- This article names no father or mother.
- Existing Jose/Juana candidates belong to separate birth-register or relationship clusters. The canonical pages do not identify them as parents of this article's Dario.
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

- Same-person conflict: unresolved between page-local `Dr Dario Pulgar A.` and other Dario/Pulgar clusters. The strongest current conclusion is a held page-local physician/property owner.
- Duplicate-person risk: high if `PULGARA`, `Pulgar A.`, Pulgar-Arriagada, Pulgar-Smith, CV, passenger, or Jose/Juana clusters are merged by name or family context alone.
- Name-variant conflict: active. Current literal forms are `Dario Pulgar A.` and derivative-signature `Dario Pulgara`; neither `A. = Arriagada` nor `A. = Arturo` is proved.
- Relationship conflict: the article supports only unnamed parents by inheritance context. No Jose/Juana parent relationship is promotable.
- Chronology conflict: none within the article. Chronology becomes risky only if this older physician/property context is attached to later CV/Pulgar-Smith, passenger, or 2000 Arriagada contexts without a bridge.
- Conversion conflict: page reference is the strongest blocker. The task/chunk path says page 11, but the content aligns with printed/conversion page 14, and direct image review is unavailable locally.

## Ranked Hypotheses

| rank | hypothesis | probability | required proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Page-local subject is `Dr. Dario Pulgar A.`, owner of Fundo Los Cuartos and physician of Concepcion. | 0.80 | Resolve page 11 versus printed/conversion page 14 and visually reread page 14. |
| 2 | Signature `PULGARA` is a no-space/stylized reading of `Pulgar A.` for the same person. | 0.68 | Reread the signature from the source image; do not promote as a variant yet. |
| 3 | Same older medical cluster as `Dario J. Pulgar Arriagada` / possible `Dario Jose Pulgar-Arriagada`. | 0.34 | After conversion QA, run a separate identity-bridge proof review comparing full name, title, place, property, and chronology. |
| 4 | Same as canonical `Dario Arturo Pulgar-Smith` or staged CV `Dario Arturo Pulgar`. | 0.10 | Reject for promotion unless a reviewed local source explicitly bridges the physician/property owner to Arturo/Smith. |
| 5 | Same as later canonical `Dario Pulgar Arriagada` legal-notice person. | 0.08 | Do not merge; require vital-date or property-chain evidence. |
| 6 | Jose/Juana candidates are the unnamed parents. | 0.04 | No relationship action; require a source naming Dario's parents. |

## Recommended Next Action

Keep the staged conflict draft on hold for conversion QA. The exact next proof-review step is a page-reference and source-image reread for `El Aguila Nombre Grande Scan.pdf`: reconcile why `CHUNK-3a644a5ca910-P0011-01` points to page-start 11 while the content and conversion-job markdown identify printed/source page 14, restore or locate `page-0014.jpg`, and visually decide whether the typed line/signature read `DR DARIO PULGAR A`, `DR. DARIO PULGARA`, or another literal form.

After image QA, promote only narrow source-local claims if verified: confirmed name form, physician of Concepcion, ownership of Fundo Los Cuartos, inheritance from unnamed parents around 1917, and property description. Do not promote a canonical alternate name, merge, `Arriagada` expansion, `Arturo`/`Smith` attachment, or Jose/Juana parent relationship until a separate identity-bridge proof review supplies direct evidence.
