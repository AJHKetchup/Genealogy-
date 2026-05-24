---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-3a644a5ca910-p0011-01-page-reference-and-signature-qa.md"
worker: postconv-identity-analysis-20260524214301603
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
- Page provenance is unresolved. The assigned chunk/frontmatter uses `page_start: 11`, but the chunk's page metadata says page `14`, and the staged draft reports that conversion-job `page-markdown/page-0014.md` contains this same `EL FUNDO LOS CUARTOS` article while `page-markdown/page-0011.md` contains a different electricity/milk-processing article.
- The page image needed for a source-image reread was not available locally according to the staged source packet; the local `page-images` directory was reported to contain only `page-0004.jpg`. This blocks visual confirmation of page number, typed name, and signature.
- Literal derivative readings differ in a way that affects identity: the typed article gives `DR DARIO PULGAR A,` while the signature note gives `DR. DARIO PULGARA`. Do not normalize `PULGARA` to `Pulgar A.` without image QA.
- The article says the subject inherited the fundo from `sus padres` around 1917, but it names no father, mother, spouse, child, or relation to Alexander John Heinz.
- Do not merge this evidence into `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, 1953 adult/child `Dario Pulgar` passenger pages, or Jose/Juana parent candidates by name alone.

## Literal Source Readings

The assigned source packet and chunk preserve the article line as:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

The same staged evidence preserves the signature note as:

```text
[handwritten signature] DR. DARIO PULGARA [/handwritten signature]
```

Literal reading only: the article names a `Dr Dario Pulgar A.` as owner of Fundo Los Cuartos, calls him a distinguished physician of Concepcion, and says he inherited the property from unnamed parents around 1917. Interpretation kept separate: `PULGARA` may be a no-space or misread `Pulgar A.`, but the current evidence does not prove `Arriagada`, `Arturo`, `Smith`, `Jose`, or any named parent.

## Hypotheses And Evidence

### 1. Page-Local Subject: `Dr. Dario Pulgar A.`

Supporting evidence:

- The chunk, source packet, and aggregate converted file agree that the article body contains `DR DARIO PULGAR A`.
- The same article describes this person as a physician of Concepcion and owner of Fundo Los Cuartos.
- The inheritance statement is source-local context for later property/family review, but only as unnamed-parent evidence.

Conflicts and limits:

- Citation/page reference is unstable because the task is keyed to page 11 while the article aligns with printed/conversion page 14.
- The signature reading remains unresolved and cannot become a canonical alternate name yet.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong page-local typed name and role, weakened by page/signature QA. |
| conflict_severity | 0.48 | Moderate while held; high if promoted or merged prematurely. |
| evidence_quality | 0.62 | Direct derivative transcription from a local source, but no image reread. |
| conversion_confidence | 0.50 | Body text agrees across derivatives; page reference and signature are unresolved. |
| claim_probability | 0.80 | Probable that the page names a physician/property owner as `Dr Dario Pulgar A.`. |
| relevance | 1.00 | Directly relevant to the staged conflict draft. |
| canonical_readiness | 0.10 | Hold for conversion QA and identity bridge review. |

### 2. Signature `PULGARA` Refers To The Same Person As `Pulgar A.`

Supporting evidence:

- The typed name and signature note occur on the same article page.
- `PULGARA` is textually close to tightly spaced `PULGAR A`.
- The staged draft itself frames this as a page/signature QA issue, not as proof of two different people.

Conflicts and limits:

- No page image was available for visual reread.
- Promoting `Pulgara` as a surname or separate person could create a false name variant or duplicate.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Same-page context favors one person, exact literal form unresolved. |
| conflict_severity | 0.55 | Material name-variant risk for canonical pages. |
| evidence_quality | 0.48 | Derivative handwriting transcription only. |
| conversion_confidence | 0.34 | Signature is the lowest-confidence element. |
| claim_probability | 0.68 | Likely same page-local subject, not proof-ready as a variant. |
| relevance | 0.98 | Central to the staged draft. |
| canonical_readiness | 0.00 | No variant promotion. |

### 3. Same Older Medical Cluster As `Dario J. Pulgar Arriagada` Or `Dario Jose Pulgar-Arriagada`

Supporting evidence:

- The article uses `Dr` and `facultativo de Concepcion`.
- Existing staged Pulgar-line context includes medical/professional `Dario J. Pulgar Arriagada` / `Dario Jose Pulgar-Arriagada` hypotheses.
- `Pulgar A.` could eventually prove to abbreviate `Pulgar Arriagada`.

Conflicts and limits:

- This article does not print `Arriagada`, `Jose`, or `J.`.
- The page/signature issue must be resolved before any identity bridge.
- `A.` cannot be expanded by family context alone.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Medical context and `A.` are suggestive but indirect. |
| conflict_severity | 0.70 | Expanding `A.` without proof risks conflating clusters. |
| evidence_quality | 0.50 | Comparison evidence is useful but not a direct bridge. |
| conversion_confidence | 0.45 | Current page QA remains unresolved. |
| claim_probability | 0.34 | Possible older medical hypothesis, not proved. |
| relevance | 0.92 | Required Pulgar-line comparison. |
| canonical_readiness | 0.02 | Preserve as hypothesis only. |

### 4. Same As `Dario Arturo Pulgar` Or Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- Broad name overlap exists: `Dario` and `Pulgar`.
- Canonical `Dario Arturo Pulgar-Smith` is a family-supplied Pulgar-line profile and explicitly warns against automatic attachment of similar Dario/Pulgar records.
- Staged CV work elsewhere uses `Dario Arturo Pulgar`, but that cluster still requires an identity bridge to Pulgar-Smith.

Conflicts and limits:

- This article does not state `Arturo`, `Smith`, `Pulgar-Smith`, a CV context, Alexander John Heinz, spouse, child, or grandchild.
- The older physician/property context is not itself an identity bridge to the CV/Pulgar-Smith cluster.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.80 | False attachment would contaminate a central family-supplied profile. |
| evidence_quality | 0.38 | Canonical context is real but not source-linked here. |
| conversion_confidence | 0.50 | Page QA cannot supply missing `Arturo`/`Smith` evidence. |
| claim_probability | 0.10 | Unsupported by this source. |
| relevance | 0.90 | Required anti-conflation check. |
| canonical_readiness | 0.00 | Do not attach to Pulgar-Smith or CV subject. |

### 5. Same As Canonical `Darío Pulgar Arriagada`

Supporting evidence:

- `Pulgar A.` could theoretically stand for `Pulgar Arriagada`.
- The canonical `Darío Pulgar Arriagada` page has separate evidence for a 2000 Serviu Región del Bío Bío expropriation notice.

Conflicts and limits:

- The 2000 legal-notice evidence gives no age, profession, Fundo Los Cuartos connection, inheritance statement, or bridge to this article.
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
- Existing wiki context includes Jose/Juana Pulgar-line candidates, including `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- This article names no father or mother.
- Existing Jose/Juana candidates belong to separate birth-register clusters with their own proof-review constraints.
- Family-context hints justify a later targeted double-check, not a parent-child promotion.

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

- Same-person conflict: unresolved between page-local `Dr Dario Pulgar A.` and other Dario/Pulgar clusters. The best current identity is a held page-local physician/property owner.
- Duplicate-person risk: high if `PULGARA`, `Pulgar A.`, Pulgar-Arriagada, Pulgar-Smith, CV, passenger, or Jose/Juana clusters are merged by name or family context alone.
- Name-variant conflict: active. Current literal forms are `Dario Pulgar A.` and derivative-signature `Dario Pulgara`; neither `A. = Arriagada` nor `A. = Arturo` is proved.
- Relationship conflict: the article supports only unnamed parents by inheritance context. No Jose/Juana parent relationship is promotable.
- Chronology conflict: none within the article. Chronology becomes risky only if the older physician/property context is attached to later CV/Pulgar-Smith, passenger, or 2000 Arriagada contexts without a bridge.
- Conversion conflict: page reference is the strongest blocker. The task/chunk path says page 11, but the content aligns with printed/conversion page 14; direct image review is unavailable locally.

## Ranked Hypotheses

| rank | hypothesis | probability | required proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Page-local subject is `Dr. Dario Pulgar A.`, owner of Fundo Los Cuartos and physician of Concepcion. | 0.80 | Resolve page 11 versus printed/conversion page 14 and visually reread page 14. |
| 2 | Signature `PULGARA` is a no-space/stylized reading of `Pulgar A.` for the same person. | 0.68 | Reread the signature from the source image; do not promote as a variant yet. |
| 3 | Same older medical cluster as `Dario J. Pulgar Arriagada` / possible `Dario Jose Pulgar-Arriagada`. | 0.34 | After conversion QA, run a separate identity bridge proof review comparing full name, title, place, and chronology. |
| 4 | Same as canonical `Dario Arturo Pulgar-Smith` or staged CV `Dario Arturo Pulgar`. | 0.10 | Reject for promotion unless a reviewed source explicitly bridges the physician/property owner to Arturo/Smith. |
| 5 | Same as later canonical `Darío Pulgar Arriagada` legal-notice person. | 0.08 | Do not merge; require vital-date or property-chain evidence. |
| 6 | Jose/Juana candidates are the unnamed parents. | 0.04 | No relationship action; require a source naming Dario's parents. |

## Recommended Next Action

Keep the staged conflict draft on hold for conversion QA. The exact next proof-review step is a page-reference and source-image reread task for `El Aguila Nombre Grande Scan.pdf`: reconcile why `CHUNK-3a644a5ca910-P0011-01` points to page-start 11 while the content and conversion-job markdown identify printed/source page 14, restore or locate the page 14 image, and visually decide whether the typed line and signature read `DR DARIO PULGAR A`, `DR. DARIO PULGARA`, or another literal form.

After that, promote only narrow source-local claims if verified: confirmed name form, physician of Concepcion, ownership of Fundo Los Cuartos, inheritance from unnamed parents around 1917, and property description. Do not promote a canonical alternate name, merge, `Arriagada` expansion, `Arturo`/`Smith` attachment, or Jose/Juana parent relationship until a separate identity-bridge proof review supplies direct evidence.
