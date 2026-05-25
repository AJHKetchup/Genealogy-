---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md"
worker: postconv-identity-analysis-20260525091345273
staged_conflict_draft: "research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md"
subject: "Dr. Dario Pulgar A. / DR. DARIO PULGARA"
source_packet: "research/_staging/source-packets/chunk-4177939279cb-p0011-01-el-aguila-fundo-los-cuartos-dario-pulgar-a.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md"
chunk_id: "CHUNK-4177939279cb-P0011-01"
page_reference: "assigned source page 11; chunk Page Metadata says printed page 14"
analysis_status: hold_for_conversion_qa_and_identity_bridge
canonical_readiness: hold
---

# Identity And Conflict Analysis: Page Reference And Signature QA

## Blockers First

- The exact staged conflict draft analyzed here is `research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md`.
- The assigned chunk is `page-0011-chunk-01.md`, but its Page Metadata says printed page `14`; the source packet says no local page-0011 image was found for the requested reread.
- The typed article reads `DR DARIO PULGAR A,` while the signature is transcribed as `[signature] DR. DARIO PULGARA [/signature]`. This is a conversion/name-form conflict, not proof of a separate surname or separate person.
- The article says Dario inherited Fundo Los Cuartos from his parents around 1917, but it does not name Jose, Juana, or any parent candidate.
- Existing Pulgar-line context contains separate or unresolved clusters for `Dario Arturo Pulgar-Smith`, staged CV `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, adult/child `Dario Pulgar` passenger candidates, and Jose/Juana parent candidates. This draft cannot merge them by name alone.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged drafts, reviewed notes, or canonical wiki pages were edited.

## Literal Source Reading

The staged source packet and referenced chunk transcribe the typed article as:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL ANO 1917
```

The same chunk separately transcribes the bottom-right signature as:

```text
[signature] DR. DARIO PULGARA [/signature]
```

Literal reading: the page-local evidence identifies `DR DARIO PULGAR A` as the owner of Fundo Los Cuartos, describes him as a distinguished physician of Concepcion, says he inherited the fundo from unnamed parents around 1917, and gives property details. The signature reading is unresolved.

Interpretation kept separate: `PULGARA` may be a tight or stylized `Pulgar A.` signature, a true name variant, or a transcription issue. The current evidence does not expand `A.` to `Arriagada`, `Arturo`, `Jose`, or `Smith`.

## Hypothesis 1: Held Page-Local Subject `Dr. Dario Pulgar A.`

Supporting evidence:

- The typed article gives the clearer page-local name form `DR DARIO PULGAR A`.
- The source packet and chunk agree that the article describes this person as owner of Fundo Los Cuartos and as a physician of Concepcion.
- The article's inheritance and property details support a narrow family-history lead, but not a named-parent relationship.

Conflicts and limits:

- The page-reference conflict blocks citation integrity: assigned page 11 versus printed page 14.
- The signature reading remains lower confidence than the typed article line.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | The typed line directly names the subject; exact signature form and page reference remain unresolved. |
| conflict_severity | 0.36 | Low if held narrowly; material if promoted with wrong page or name form. |
| evidence_quality | 0.64 | Direct local transcription, single source, derivative pending page-image reread. |
| conversion_confidence | 0.48 | Body text is usable, but page image, page reference, and signature QA are unresolved. |
| claim_probability | 0.80 | Probable that the article names `Dr Dario Pulgar A.` as the property owner/physician. |
| relevance | 1.00 | Directly answers the staged conflict draft. |
| canonical_readiness | 0.10 | Hold for conversion QA; no canonical promotion yet. |

## Hypothesis 2: Signature Is `Pulgar A.` Rather Than Distinct `Pulgara`

Supporting evidence:

- The typed article's `PULGAR A` provides a page-local explanation for the signature's final `A`.
- The staged conflict draft itself preserves the uncertainty that `PULGARA` may be `Pulgar A.` with tight spacing.
- Prior local page-14 analyses for the same article family treat the same signature pattern as a visual reread issue, not as established evidence for a distinct surname.

Conflicts and limits:

- The chunk currently transcribes the signature as `DR. DARIO PULGARA`.
- No local page image was available to resolve handwriting, spacing, or punctuation.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | More likely one page subject/signature than a separate identity, but still unverified. |
| conflict_severity | 0.48 | Moderate because silent normalization would erase a visible transcription conflict. |
| evidence_quality | 0.54 | Good internal contextual clue, weak handwriting verification. |
| conversion_confidence | 0.34 | Signature is the exact low-confidence element. |
| claim_probability | 0.68 | Probable, pending visual proof review. |
| relevance | 0.98 | Central to the assigned name-reading conflict. |
| canonical_readiness | 0.05 | Do not promote as an alternate name until reread. |

## Hypothesis 3: `PULGARA` Is A Literal Distinct Name Form

Supporting evidence:

- The chunk and source packet both preserve `[signature] DR. DARIO PULGARA [/signature]`.
- The staged draft properly leaves open whether this is a true signature variant.

Conflicts and limits:

- No existing wiki or reviewed context found here supports `Pulgara` as a separate Pulgar-line surname/person.
- The typed body is stronger for the page subject than the unresolved signature transcription.
- Promoting `Pulgara` would likely create an unsupported duplicate-person or name-variant conflict.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Based only on unresolved handwriting transcription. |
| conflict_severity | 0.72 | High if promoted as a separate person or canonical name variant. |
| evidence_quality | 0.28 | Requires direct image confirmation. |
| conversion_confidence | 0.22 | The signature is explicitly held for QA. |
| claim_probability | 0.16 | Possible but weaker than the `Pulgar A.` interpretation. |
| relevance | 0.94 | Directly relevant to the staged conflict. |
| canonical_readiness | 0.00 | Do not promote. |

## Hypothesis 4: Same Older Medical/Property Candidate As `Dario Jose Pulgar-Arriagada` Or `Darío J. Pulgar Arriagada`

Supporting evidence:

- `Pulgar A.` could eventually prove to abbreviate `Pulgar Arriagada`, but that is only an interpretation.
- Local reviewed/staged context includes a 2 September 1918 medical-title source packet naming `Darío J. Pulgar Arriagada` under `Médicos-Cirujanos`; that narrow name/title reading has high conversion confidence.
- The `El Aguila` article's `Dr.`/`facultativo de Concepcion` context is compatible with an older medical candidate.

Conflicts and limits:

- This draft does not spell `Arriagada`, `Jose`, or `J.`.
- `Dario Jose Pulgar-Arriagada` photograph/metadata contexts remain identity-sensitive and do not bridge this article by themselves.
- The current proof problem is page/signature QA, not a full-name identity bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.40 | Medical context and `A.` are suggestive; explicit full-name bridge is absent. |
| conflict_severity | 0.70 | High risk if `A.` is expanded to `Arriagada` or `J.` to `Jose` without proof. |
| evidence_quality | 0.50 | The 1918 title reading is strong for its own claim; the bridge remains weak. |
| conversion_confidence | 0.52 | Comparison source is stronger than this signature/page-reference draft. |
| claim_probability | 0.36 | Plausible older professional hypothesis, not proved. |
| relevance | 0.90 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | Preserve as unresolved; no merge. |

## Hypothesis 5: Same Person As `Dario Arturo Pulgar` Or Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The names share `Dario` and `Pulgar`.
- Canonical `Dario Arturo Pulgar-Smith` is a family-supplied maternal-grandfather profile and explicitly warns against attaching similarly named records without identity review.
- Staged CV context identifies `Dario Arturo Pulgar` as a document-level subject, but keeps the bridge to `Dario Arturo Pulgar-Smith` on hold.

Conflicts and limits:

- This draft does not state `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, spouse, child, grandchild, CV facts, or family relationship.
- The article's adult physician/property-owner/inheritance-around-1917 context fits an older medical lead more readily than the later CV/Habitat cluster, but that is interpretive.
- Family context can justify a later double-check; it cannot normalize `Pulgar A.` to `Pulgar-Smith`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.78 | Wrong attachment would contaminate the central Pulgar-Smith profile. |
| evidence_quality | 0.42 | Canonical family context is real but not source-linked here. |
| conversion_confidence | 0.46 | Reread may settle the page name but not the Arturo/Smith bridge. |
| claim_probability | 0.10 | Low on current local evidence. |
| relevance | 0.92 | Required because Pulgar-Smith is a central existing Dario profile. |
| canonical_readiness | 0.01 | Do not attach to Pulgar-Smith or CV subject. |

## Hypothesis 6: Same As Canonical `Darío Pulgar Arriagada`

Supporting evidence:

- `A.` might eventually stand for `Arriagada`.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` currently carries a narrow 5 December 2000 expropriation event for `Darío Pulgar Arriagada`.

Conflicts and limits:

- The 2000 stub gives no age, physician title, Fundo Los Cuartos link, or parent/inheritance bridge.
- Older medical/passenger analyses warn that direct attachment to a 2000 `Darío Pulgar Arriagada` candidate creates a serious chronology caution unless vital-date or property-continuity evidence is found.
- This draft does not spell `Arriagada`; the signature conflict cannot carry this merge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.16 | Possible abbreviation only; no bridge and chronology caution. |
| conflict_severity | 0.82 | Serious risk of chronology/property-context conflation. |
| evidence_quality | 0.46 | Each source supports separate narrow claims, not same-person identity. |
| conversion_confidence | 0.50 | The 2000 notice is clearer than this signature, but no bridge exists. |
| claim_probability | 0.12 | Low without vital-date or property-continuity proof. |
| relevance | 0.84 | Required comparison because of possible `A.` expansion. |
| canonical_readiness | 0.02 | Do not merge with the canonical Arriagada stub. |

## Hypothesis 7: Jose/Juana Parent Candidates Explain The Unnamed Parents

Supporting evidence:

- The article literally says Dario inherited Fundo Los Cuartos from `sus padres` around 1917.
- Existing local context includes Jose/Juana Pulgar-line candidates including `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- This article names no parent.
- Existing Jose/Juana clusters are separate register/relationship contexts with their own conversion and proof-review limits.
- No relationship can be promoted from the phrase `sus padres` beyond unnamed parents.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | No named-parent evidence on this page. |
| conflict_severity | 0.66 | Assigning named parents would create unsupported relationship claims. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.38 | Related register readings and this page/signature need separate QA. |
| claim_probability | 0.04 | No specific Jose/Juana relationship is supported. |
| relevance | 0.72 | Relevant because the source mentions parents and the Pulgar-line rule requires the check. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflicts

- Page-reference conflict: high. The assigned source page is 11, while the chunk Page Metadata and handwritten marginalia report printed page 14.
- Name-variant conflict: moderate-high. The typed article supports `Dario Pulgar A.`; the signature is transcribed as `Dario Pulgara`. Do not treat `Pulgara`, `Arriagada`, `Arturo`, `Jose`, or `Smith` as proved variants from this draft.
- Same-person conflict: unresolved. The page supports only a held `Dr Dario Pulgar A.` page-local subject until visual QA.
- Duplicate-person risk: high if this candidate is merged into `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, or passenger stubs by name alone.
- Relationship conflict: the page states unnamed parents only; no Jose/Juana parent relationship is promotable.
- Chronology conflict: inheritance around 1917 and adult physician/property-owner context may fit an older medical cluster, but cautions against unreviewed attachment to later CV/Pulgar-Smith or 2000 Arriagada contexts.
- Conversion-confidence conflict: medium for the typed article text, low for the handwritten signature and page-specific citation until the original page image is reread.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Next action |
| ---: | --- | ---: | --- |
| 1 | Held page-local subject `Dr. Dario Pulgar A.` | 0.80 | Reread source image and reconcile assigned page 11 versus printed page 14. |
| 2 | Signature is a stylized/tight `Pulgar A.` for the same subject | 0.68 | Verify signature spacing and punctuation against the page image. |
| 3 | Same older medical/property candidate as `Dario Jose Pulgar-Arriagada` or `Darío J. Pulgar Arriagada` | 0.36 | Preserve unresolved; require explicit full-name or identity-bearing bridge after page QA. |
| 4 | Signature literally establishes `Pulgara` as a distinct name form | 0.16 | Hold as QA caution only; do not promote. |
| 5 | Same as canonical `Darío Pulgar Arriagada` | 0.12 | Do not merge; require vital-date/property-continuity proof. |
| 6 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.10 | Do not attach; require a reviewed source linking this older physician/property claim to the CV/Pulgar-Smith identity. |
| 7 | Jose/Juana parent candidates explain the unnamed parents | 0.04 | No relationship action; require a source naming Dario's parents. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md` on `hold_for_conversion_qa`. Do not promote the page-specific citation, signature, canonical alternate name, person merge, `A.` to `Arriagada` expansion, `Arturo`/`Smith` attachment, or Jose/Juana parent relationship from this draft.

The exact next proof-review step is page-image conversion QA for `CHUNK-4177939279cb-P0011-01`: locate the rendered/original image corresponding to the assigned source page 11 and the printed page 14, reconcile the page reference, then reread the typed name line and bottom signature to decide whether the source reads `DR DARIO PULGAR A`, `DR. DARIO PULGARA`, a stylized `Pulgar A.`, or another literal form. Only after that should a separate Pulgar identity-bridge review compare the confirmed reading first against the older medical cluster (`Dario Pulgar A.` passenger, 1953 adult `Dario Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`) and only separately against `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith`, canonical `Darío Pulgar Arriagada`, and Jose/Juana parent candidates.
