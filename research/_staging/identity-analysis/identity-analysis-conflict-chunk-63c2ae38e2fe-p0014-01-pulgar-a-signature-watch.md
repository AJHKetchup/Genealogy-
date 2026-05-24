---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md"
worker: postconv-identity-analysis-20260524174350308
staged_conflict_draft: "research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md"
subject: "Dr. Dario Pulgar A."
source_packet: "research/_staging/source-packets/chunk-63c2ae38e2fe-p0014-01-dario-pulgar-los-cuartos.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0014-chunk-01.md"
chunk_id: "CHUNK-63c2ae38e2fe-P0014-01"
page_reference: "source page 14"
analysis_status: hold_for_conversion_qa_and_identity_bridge
canonical_readiness: hold
---

# Identity And Conflict Analysis: Pulgar A. Signature Watch

## Blockers First

- The exact staged conflict draft analyzed here is `research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md`.
- Do not promote the signature reading. The staged conflict draft and source packet both preserve a reread-page concern, and the source packet says no page image for page 14 was found in the conversion job directory during extraction.
- There is a provenance/version caution: the staged conflict draft and source packet cite `CHUNK-63c2ae38e2fe-P0014-01`, while the referenced chunk frontmatter currently reads `CHUNK-dfc1ae4668c1-P0014-01` with converted SHA `dfc1ae4668c174a269b4b42e42ed66169bc0b7019e0fe6e9a38a9b5e7dfdeb3e`.
- The typed article line is transcribed as `DR DARIO PULGAR A,`; the visual note transcribes the handwritten signature as `DR. DARIO PULGARA`. This is a conversion/name-form conflict, not proof of a separate surname.
- The page states inheritance from unnamed parents around 1917, but it does not name Jose, Juana, or any parent candidate.
- Existing local Pulgar context preserves separate or unresolved clusters for `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, adult/child `Dario Pulgar` passenger candidates, and Jose/Juana parent candidates. This draft cannot merge them by name alone.

## Literal Source Reading

The referenced source packet quotes the typed article:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

It separately quotes the handwritten signature as:

```text
[Handwritten signature in blue ink:] DR. DARIO PULGARA
```

Literal reading: page 14 names `DR DARIO PULGAR A` in the article, describes him as a physician of Concepcion, says he inherited Fundo Los Cuartos from his parents around 1917, and has a bottom-right handwritten signature currently transcribed as `DR. DARIO PULGARA`.

Interpretation kept separate: `PULGARA` may be a compressed or stylized `Pulgar A.` signature. The current local evidence does not prove a surname `Pulgara`, does not expand `A.` to `Arriagada`, and does not identify the unnamed parents.

## Hypothesis 1: Signature Is `Pulgar A.` Rather Than Distinct `Pulgara`

Supporting evidence:

- The typed body gives the clearer name form `DR DARIO PULGAR A`.
- The staged conflict draft itself says the handwritten `PULGARA` may be `Pulgar A.` with a stylized or closely spaced final initial.
- A separate local page-14 reread task asks reviewers to decide whether the source reads `DR DARIO PULGAR A`, `DR. DARIO PULGARA`, another form, or an abbreviation.

Conflicts and limits:

- No page image was available during extraction for this staged source packet, so the handwriting cannot be settled here.
- The referenced chunk currently preserves the signature as `DR. DARIO PULGARA`, so the conflict must remain visible until visual reread.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Clear typed body supports `Dario Pulgar A.` as the page subject; exact signature form remains unresolved. |
| conflict_severity | 0.34 | Low if held as a QA caution; higher only if promoted as a separate surname. |
| evidence_quality | 0.62 | Direct page transcription but derivative, single-source, and image-reread blocked. |
| conversion_confidence | 0.42 | Typed line is usable; signature and chunk-id/provenance mismatch lower confidence. |
| claim_probability | 0.72 | Probable that the signature represents the same `Pulgar A.` subject, not a distinct person. |
| relevance | 1.00 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.10 | Not ready; requires page-image proof review. |

## Hypothesis 2: `PULGARA` Is A Literal Distinct Name Form

Supporting evidence:

- The referenced chunk and source packet both transcribe the bottom-right signature as `DR. DARIO PULGARA`.
- The conflict draft properly preserves the visual note instead of silently normalizing it.

Conflicts and limits:

- The typed article's `PULGAR A` is stronger page-local identity evidence than the unresolved handwriting transcription.
- No local canonical or reviewed context found here supports `Pulgara` as a separate surname/person for this article.
- Treating `PULGARA` as canonical would likely create a false duplicate-person or name-variant conflict.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Based only on unresolved handwriting transcription. |
| conflict_severity | 0.70 | Promoting it could create an unsupported name variant or duplicate identity. |
| evidence_quality | 0.30 | Needs direct visual confirmation. |
| conversion_confidence | 0.22 | Signature is the exact low-confidence element. |
| claim_probability | 0.16 | Possible literal reading, but weaker than `Pulgar A.` interpretation. |
| relevance | 0.96 | Central to this conflict draft. |
| canonical_readiness | 0.00 | Do not promote. |

## Hypothesis 3: Same Older Medical/Property Candidate As `Dario Jose Pulgar-Arriagada` Or `Dario J. Pulgar Arriagada`

Supporting evidence:

- `Pulgar A.` could eventually prove to abbreviate `Pulgar Arriagada`, but this is only an interpretation.
- Local staged context includes `Darío J. Pulgar Arriagada` receiving a medical-surgeon title in 1918 and `Dario Pulgar-Arriagada` listed as Captain of the Health Service in a 1929 Chile convention context.
- The page 14 article describes `Dr Dario Pulgar A.` as a physician of Concepcion and owner of Fundo Los Cuartos, a professional context compatible with an older medical cluster.

Conflicts and limits:

- Page 14 does not spell `Arriagada`, `Jose`, or `J.`.
- The `Dario Jose Pulgar-Arriagada` photograph packet identifies the person from filename/source context rather than visible text and remains on conversion QA hold.
- The 1918 medical-title evidence supports only `Darío J. Pulgar Arriagada`; it does not expand `J.` or bridge to Fundo Los Cuartos.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Medical context and `A.` are suggestive, but no full-name bridge exists. |
| conflict_severity | 0.68 | High conflation risk if `A.` is expanded without proof. |
| evidence_quality | 0.48 | Some local staged evidence is strong for its own narrow claims; the bridge is weak. |
| conversion_confidence | 0.46 | Page 14 and photograph metadata have QA holds; 1918 title reread is stronger but not bridging. |
| claim_probability | 0.34 | Plausible older professional hypothesis, not proved. |
| relevance | 0.90 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | No merge or name expansion. |

## Hypothesis 4: Same Person As `Dario Arturo Pulgar` Or Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The names share `Dario` and `Pulgar`.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` represents a family-supplied maternal-grandfather identity and explicitly warns not to attach Dario/Pulgar/Pulgar-Arriagada records without identity review.
- Existing CV staging preserves a document-level `Dario Arturo Pulgar` cluster as a possible but unproved bridge to `Dario Arturo Pulgar-Smith`.

Conflicts and limits:

- Page 14 does not state `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, spouse, child, grandchild, CV facts, or family relationship.
- The page 14 subject appears as an older Concepcion physician/property owner with inheritance around 1917; this does not bridge to the CV/Pulgar-Smith cluster.
- Existing CV proof reviews keep canonical attachment on hold pending an explicit identity-bearing bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.78 | Wrong attachment would contaminate the central family-supplied profile. |
| evidence_quality | 0.42 | Family context is real but not source-linked to this page. |
| conversion_confidence | 0.44 | Reread may settle `Pulgar A.` but not `Arturo` or `Smith`. |
| claim_probability | 0.12 | Low without an identity bridge. |
| relevance | 0.92 | Required Pulgar-line anti-conflation check. |
| canonical_readiness | 0.01 | Do not attach to Pulgar-Smith or CV subject. |

## Hypothesis 5: Same As Later `Dario/Darío Pulgar Arriagada` Legal-Notice Candidate

Supporting evidence:

- `Pulgar A.` might eventually be an abbreviated `Pulgar Arriagada`.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` holds a narrow 2000-12-05 expropriation event naming `Darío Pulgar Arriagada`.

Conflicts and limits:

- The legal-notice candidate has no age, profession, Fundo Los Cuartos connection, or parent/inheritance bridge.
- A prior local analysis warns that older medical/passenger chronology compared to a 2000 event creates a severe chronology caution unless vital dates prove exceptional longevity or a different property-transfer explanation.
- Page 14 does not spell `Arriagada`; the signature issue cannot carry this merge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.16 | Only possible abbreviation/name overlap. |
| conflict_severity | 0.80 | Serious chronology and property-context conflation risk. |
| evidence_quality | 0.46 | Each source supports separate narrow claims, not same-person identity. |
| conversion_confidence | 0.50 | The 2000 notice is clearer than the page-14 signature, but no bridge exists. |
| claim_probability | 0.12 | Unlikely on present evidence. |
| relevance | 0.82 | Relevant because of possible `A.` expansion. |
| canonical_readiness | 0.02 | Do not merge. |

## Hypothesis 6: Jose/Juana Parent Candidates Explain `Sus Padres`

Supporting evidence:

- The article literally says `Dr Dario Pulgar A.` inherited the fundo from `sus padres` around 1917.
- Existing wiki context includes separate Jose/Juana Pulgar-line candidates, including `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Conflicts and limits:

- Page 14 names no parent.
- The Jose/Juana materials are separate birth-register/relationship clusters with their own conversion and confidence issues.
- Family-context hints justify a targeted double-check, not a silent correction or parent assignment.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | No named parent evidence on this page. |
| conflict_severity | 0.66 | Assigning named parents would create unsupported relationship claims. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.38 | Page 14 and related register contexts need separate QA. |
| claim_probability | 0.04 | Only unnamed-parent inheritance is supported. |
| relevance | 0.72 | Relevant because the article mentions parents. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person conflict: unresolved. The page supports only a held `Dr Dario Pulgar A.` page-local subject until reread.
- Duplicate-person risk: high if the signature `PULGARA` is promoted as a separate person or if `Dario Pulgar A.` is merged with Pulgar-Smith, Arturo, Jose/Arriagada, later Arriagada, passenger, or parent clusters by name alone.
- Name-variant conflict: the typed body supports `Dario Pulgar A.`; the signature is currently `Dario Pulgara` in the conversion. Do not treat `Pulgara`, `Arriagada`, `Arturo`, `Jose`, or `Smith` as proved variants from this draft.
- Relationship conflict: the source states only unnamed parents; no Jose/Juana parent relationship is promotable.
- Chronology conflict: page 14's inheritance around 1917 and adult physician/property-owner context may fit an older medical cluster, but it cautions against unreviewed attachment to later CV/Pulgar-Smith or 2000 Arriagada contexts.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Next action |
| ---: | --- | ---: | --- |
| 1 | Signature is `Pulgar A.`/same page-local subject, not a distinct `Pulgara` identity | 0.72 | Reread page 14 image and verify typed line plus signature spacing. |
| 2 | Same older medical/property candidate as `Dario Jose Pulgar-Arriagada` or `Dario J. Pulgar Arriagada` | 0.34 | Preserve as unresolved; require full-name or identity-bearing bridge. |
| 3 | Signature literally reads a distinct `Pulgara` name form | 0.16 | Hold only as a QA caution until visual proof review. |
| 4 | Same as later `Dario/Darío Pulgar Arriagada` legal-notice candidate | 0.12 | Do not merge; require vital-date/property-continuity proof. |
| 5 | Same as `Dario Arturo Pulgar` or canonical `Dario Arturo Pulgar-Smith` | 0.12 | Do not attach; require a reviewed identity bridge to Arturo/Smith. |
| 6 | Jose/Juana parent candidates explain the unnamed parents | 0.04 | No relationship action; require a source naming Dario's parents. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-63c2ae38e2fe-p0014-01-pulgar-a-signature-watch.md` on hold as a proof-review caution. The exact next proof-review step is a page-image reread of source page 14 from `raw/sources/El Aguila Nombre Grande Scan.pdf`, with a provenance audit reconciling the staged `CHUNK-63c2ae38e2fe-P0014-01` reference against the current chunk frontmatter `CHUNK-dfc1ae4668c1-P0014-01`.

During that review, decide only the narrow reading: whether the typed line and signature support `DR DARIO PULGAR A`, `DR. DARIO PULGARA`, a stylized `Pulgar A.`, or another literal form. If confirmed, promote only narrow claims for the verified name form, Concepcion physician description, ownership of Fundo Los Cuartos, and inheritance from unnamed parents around 1917. Do not promote a canonical alternate name, person merge, `Arriagada` expansion, `Arturo`/`Smith` attachment, or Jose/Juana parent relationship from this staged conflict draft.
