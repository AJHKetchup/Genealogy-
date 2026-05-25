---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md"
worker: postconv-identity-analysis-20260525092214268
staged_conflict_draft: "research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md"
subject: "Dr. Dario Pulgar A. / DR. DARIO PULGARA"
source_packet: "research/_staging/source-packets/chunk-4177939279cb-p0011-01-el-aguila-fundo-los-cuartos-dario-pulgar-a.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md"
chunk_id: "CHUNK-4177939279cb-P0011-01"
page_reference: "assigned source page 11; chunk Page Metadata says printed page 14"
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Page Reference And Signature QA

## Blockers First

- This note analyzes exactly `research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md`.
- The page citation is not proof-ready: the staged draft and source packet assign source page 11, while the referenced chunk's Page Metadata and handwritten marginalia say printed page 14.
- The handwritten signature cannot be normalized yet. The typed article line reads `DR DARIO PULGAR A,`; the converted signature line reads `[signature] DR. DARIO PULGARA [/signature]`.
- No local page-0011 image was available during the prior extraction, so the core signature/page reread remains unresolved.
- The article says the named man inherited the fundo from `sus padres`, but it does not name Jose, Juana, Arriagada, Smith, Arturo, or Jose as a given-name component.
- Do not merge this page-local subject into `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, or Jose/Juana parent candidates by name or family context alone.

## Literal Source Reading

The referenced source packet and chunk support this typed article reading:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL ANO 1917
```

The same chunk separately preserves the signature transcription:

```text
[signature] DR. DARIO PULGARA [/signature]
```

Literal claim: a page-local `Dr Dario Pulgar A.` is described as owner of Fundo Los Cuartos, a distinguished physician of Concepcion, and someone who inherited the fundo from unnamed parents around 1917.

Interpretation kept separate: `PULGARA` may be a tight `Pulgar A.`, a true handwritten name variant, or a transcription error. This draft does not itself expand `A.` to `Arriagada`, `Arturo`, `Jose`, or `Smith`.

## Hypothesis 1: Page-Local Subject Is `Dr. Dario Pulgar A.`

Supporting evidence:

- The typed body line gives the clearest name form: `DR DARIO PULGAR A`.
- The source packet and chunk agree on the article's main subject and property/physician context.
- The signature conflict can be held without splitting the page subject.

Conflicts and limits:

- Page reference conflict blocks citation promotion.
- The signature line remains lower confidence than the typed body line.
- The article contains no vital facts, relatives by name, spouse, child, or later identity bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong page-local typed name; exact signature and page reference unresolved. |
| conflict_severity | 0.42 | Moderate while held; high if promoted with the wrong page or name form. |
| evidence_quality | 0.64 | Direct local derivative transcription from one source, pending image reread. |
| conversion_confidence | 0.48 | Body text is medium; signature/page citation are low until QA. |
| claim_probability | 0.80 | Probable that the article names `Dr Dario Pulgar A.` as owner/physician. |
| relevance | 1.00 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.10 | Hold for conversion QA and identity-bridge review. |

## Hypothesis 2: Signature Reads `Pulgar A.` Rather Than Distinct `Pulgara`

Supporting evidence:

- The typed line's `PULGAR A` is a local explanation for a signature that may visually compress the surname and initial.
- The staged conflict draft explicitly preserves this as a likely possibility.

Conflicts and limits:

- The current converted signature text literally says `PULGARA`.
- No page image was available to verify spacing, punctuation, or handwriting.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Likely one page subject/signature, but visually unverified. |
| conflict_severity | 0.50 | Silent normalization would erase the visible conflict. |
| evidence_quality | 0.54 | Strong internal clue, weak handwriting confirmation. |
| conversion_confidence | 0.34 | The signature is the low-confidence element. |
| claim_probability | 0.68 | Probable but not proof-ready. |
| relevance | 0.98 | Central to the assigned conflict. |
| canonical_readiness | 0.05 | Do not promote as an alternate name yet. |

## Hypothesis 3: `PULGARA` Is A Distinct Literal Name Form

Supporting evidence:

- The chunk and source packet both preserve the signature as `DR. DARIO PULGARA`.
- The staged draft leaves open a true signature variant.

Conflicts and limits:

- No reviewed or canonical context found here establishes `Pulgara` as a separate Pulgar-line surname or person.
- The typed body line is stronger for the page subject than the unresolved handwritten signature.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Depends on unresolved handwriting transcription only. |
| conflict_severity | 0.72 | High if promoted as a separate person or canonical variant. |
| evidence_quality | 0.28 | Needs direct image confirmation. |
| conversion_confidence | 0.22 | Signature reading is explicitly held for QA. |
| claim_probability | 0.16 | Possible, weaker than `Pulgar A.`. |
| relevance | 0.94 | Direct name-reading issue. |
| canonical_readiness | 0.00 | Do not promote. |

## Hypothesis 4: Same Older Medical/Property Candidate As `Dario Jose Pulgar-Arriagada` Or `Dario/Dario Pulgar Arriagada`

Supporting evidence:

- `Pulgar A.` could eventually be an abbreviation for an Arriagada surname, but that is not literal here.
- Local staged tasks mention medical-context variants such as `Dario Pulgar-Arriagada` and `Dario J. Pulgar Arriagada`; the `Dr.` and Concepcion physician context makes an older medical comparison relevant.

Conflicts and limits:

- This draft does not spell `Arriagada`, `Jose`, or `J.`.
- The current task is a page/signature QA hold, not a complete identity bridge.
- A property-owner/inheritance-around-1917 context cannot be attached to an Arriagada cluster without a separate proof-reviewed bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Profession and `A.` are suggestive, not sufficient. |
| conflict_severity | 0.70 | High risk if `A.` is expanded without source support. |
| evidence_quality | 0.50 | Separate local evidence may be useful, but this bridge is weak. |
| conversion_confidence | 0.46 | This page's key name/page elements remain unsettled. |
| claim_probability | 0.34 | Plausible older medical hypothesis only. |
| relevance | 0.90 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | Preserve unresolved; no merge. |

## Hypothesis 5: Same Person As `Dario Arturo Pulgar` Or Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- Name overlap: `Dario` and `Pulgar`.
- The canonical `Dario Arturo Pulgar-Smith` page is a family-supplied profile and explicitly warns not to merge similarly named source clusters without identity review.
- Staged CV materials identify a document-level `Dario Arturo Pulgar`, but those pages require their own identity bridge before canonical attachment.

Conflicts and limits:

- This article does not say `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, or any descendant relationship.
- The 1917 inheritance/physician/property context is not, by itself, evidence for the later CV or family-supplied Pulgar-Smith identity.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.78 | Wrong attachment would contaminate the central family profile. |
| evidence_quality | 0.42 | Family context exists, but is not source-linked to this page. |
| conversion_confidence | 0.46 | Reread may settle this page's name, not the Arturo/Smith bridge. |
| claim_probability | 0.10 | Low on current evidence. |
| relevance | 0.92 | Required because Pulgar-Smith is existing wiki context. |
| canonical_readiness | 0.01 | Do not attach. |

## Hypothesis 6: Same As Canonical `Darío Pulgar Arriagada`

Supporting evidence:

- `A.` might later prove to abbreviate `Arriagada`.
- The canonical stub `wiki/people/dar-o-pulgar-arriagada.md` exists and carries a 5 December 2000 expropriation event.

Conflicts and limits:

- The canonical stub gives no physician title, Fundo Los Cuartos link, parent/inheritance bridge, or vital-date evidence.
- A 2000 property/legal event and an article describing inheritance around 1917 require chronology and property-continuity proof before same-person treatment.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.16 | Possible abbreviation only; no direct bridge. |
| conflict_severity | 0.82 | Serious chronology/property-context conflation risk. |
| evidence_quality | 0.46 | Each source supports separate narrow claims only. |
| conversion_confidence | 0.50 | The canonical event is clearer than this signature, but unbridged. |
| claim_probability | 0.12 | Low without vital or property-continuity evidence. |
| relevance | 0.84 | Required comparison because of possible `A.` expansion. |
| canonical_readiness | 0.02 | Do not merge. |

## Hypothesis 7: Jose/Juana Parent Candidates Are The Unnamed Parents

Supporting evidence:

- The article literally says the subject inherited the fundo from `sus padres`.
- Existing local wiki context includes Jose/Juana Pulgar-line candidates: `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- This article names no parent.
- The Jose/Juana pages are separate register-derived clusters with their own conversion/proof limits.
- No specific Jose/Juana relationship can be promoted from `sus padres`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | No named-parent evidence on this page. |
| conflict_severity | 0.66 | Assigning named parents would create unsupported relationships. |
| evidence_quality | 0.32 | Related parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.38 | This page and related register readings each need separate QA. |
| claim_probability | 0.04 | No specific Jose/Juana parent identity is supported here. |
| relevance | 0.72 | Relevant because the article mentions parents. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflicts

- Page-reference conflict: assigned source page 11 versus chunk Page Metadata/handwritten marginalia printed page 14.
- Name-variant conflict: typed `Dario Pulgar A.` versus converted signature `Dario Pulgara`.
- Same-person conflict: unresolved beyond page-local `Dr Dario Pulgar A.`.
- Duplicate-person risk: high if merged by name alone with Pulgar-Smith, staged CV `Dario Arturo Pulgar`, Arriagada variants, passenger stubs, or Jose/Juana clusters.
- Relationship conflict: `sus padres` supports unnamed parents only.
- Chronology conflict: inheritance around 1917 and physician/property-owner context require careful separation from later CV/Habitat/passenger/2000 Arriagada contexts.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Held page-local subject `Dr. Dario Pulgar A.` | 0.80 | Reread source image and reconcile assigned page 11 versus printed page 14. |
| 2 | Signature is a stylized/tight `Pulgar A.` for the same subject | 0.68 | Verify signature spacing and punctuation from the page image. |
| 3 | Same older medical/property candidate as `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada` | 0.34 | Require explicit full-name, title, property, or relationship bridge after page QA. |
| 4 | Signature literally establishes `Pulgara` as a distinct name form | 0.16 | Treat as QA caution only until visual proof review. |
| 5 | Same as canonical `Darío Pulgar Arriagada` | 0.12 | Require vital-date or property-continuity proof; no merge now. |
| 6 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.10 | Require a reviewed bridge from this older physician/property claim to CV/Pulgar-Smith evidence. |
| 7 | Jose/Juana parent candidates explain the unnamed parents | 0.04 | Require a source naming Dario's parents; no relationship action now. |

## Recommended Next Action

Keep the staged draft on `hold_for_conversion_qa`. The exact next step is page-image proof review for `CHUNK-4177939279cb-P0011-01`: locate the original/rendered image corresponding to assigned source page 11 and printed page 14, reconcile the citation, and reread both the typed name line and bottom-right signature.

After that QA, run a separate identity-bridge review before any promotion. The bridge review should compare the confirmed source reading first against older medical/property candidates and Arriagada variants, and only separately against staged `Dario Arturo Pulgar`, canonical `Dario Arturo Pulgar-Smith`, canonical `Darío Pulgar Arriagada`, passenger stubs, and Jose/Juana parent candidates. No canonical page, source output, chunk, or conversion file should be changed from this draft.
