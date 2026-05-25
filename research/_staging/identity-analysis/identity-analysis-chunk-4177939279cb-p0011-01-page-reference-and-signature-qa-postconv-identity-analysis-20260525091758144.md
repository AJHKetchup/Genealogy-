---
type: identity_conflict_analysis
status: hold
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md"
worker: postconv-identity-analysis-20260525091758144
staged_conflict_draft: "research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md"
subject: "Dr. Dario Pulgar A. / DR. DARIO PULGARA"
source_packet: "research/_staging/source-packets/chunk-4177939279cb-p0011-01-el-aguila-fundo-los-cuartos-dario-pulgar-a.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md"
chunk_id: "CHUNK-4177939279cb-P0011-01"
page_reference: "assigned source page 11; chunk Page Metadata says printed page 14"
canonical_readiness: hold_for_conversion_qa_and_identity_bridge
---

# Identity/Conflict Analysis: Page Reference And Signature QA

## Blockers First

- Exact staged draft reviewed: `research/_staging/conflicts/chunk-4177939279cb-p0011-01-page-reference-and-signature-qa.md`.
- Page citation is unstable: assignment and source packet use source page 11, while the chunk Page Metadata and handwritten marginalia report printed page 14.
- The manifest lists `page-images/page-0011.jpg` and `page-images/page-0014.jpg`, but both files are absent in the current workspace. I did not regenerate images or rerun conversion.
- The typed article reads `DR DARIO PULGAR A`; the converted signature line reads `DR. DARIO PULGARA`. This is a source-reading/name-form conflict, not proof of a separate person or stable surname variant.
- The article says Dario inherited from `sus padres` around 1917, but it does not name Jose, Juana, or any parent candidate.
- This draft does not state Arturo, Smith, Jose, J., Arriagada, Pulgar-Smith, spouse, child, grandchild, birth, or death. No merge, relationship, canonical attachment, or name expansion is supported from this page alone.

## Literal Source Readings

- Staged source packet and chunk: `EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A, DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE FUNDO ALLA POR EL ANO 1917`.
- Staged source packet and chunk: `[signature] DR. DARIO PULGARA [/signature]`.
- Page metadata: printed page `14`; publication `EL AGUILA`; date header `ENERO - FEBRERO`.

Interpretation boundary: `PULGARA` may be a close-spaced or stylized `Pulgar A.`, a true signature variant, or a conversion/transcription issue. The current evidence does not justify expanding `A.` to `Arriagada` or `Arturo`.

## Hypotheses

| Rank | Hypothesis | Probability | Evidence supporting | Conflicts and limits |
| ---: | --- | ---: | --- | --- |
| 1 | Held page-local subject is `Dr. Dario Pulgar A.` | 0.80 | Clear typed article line; same page ties him to Fundo Los Cuartos, physician status in Concepcion, and unnamed-parent inheritance. | Page image absent; assigned page 11 vs printed page 14 unresolved; no full identity bridge. |
| 2 | Signature `PULGARA` likely represents `Pulgar A.` or a spacing/transcription issue for the same page-local person. | 0.68 | Typed `PULGAR A` appears on the same page; staged draft itself flags tight spacing/transcription as a live explanation. | Signature is the low-confidence element and needs visual reread. |
| 3 | Same older medical/property candidate as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` / `Dario Pulgar Arriagada`. | 0.36 | `Dr.` and `facultativo de Concepcion` are compatible with local staged medical-title contexts; `A.` could be an Arriagada lead. | This page does not print Jose, J., or Arriagada; no same-person proof. |
| 4 | Signature literally establishes `Dario Pulgara` as a distinct name form. | 0.16 | The derivative transcription preserves `DR. DARIO PULGARA`. | No image proof; typed text gives a stronger alternate explanation; no canonical support for a separate Pulgara identity. |
| 5 | Same person as `Dario Arturo Pulgar` or canonical `Dario Arturo Pulgar-Smith`. | 0.10 | Shared `Dario Pulgar` name elements; canonical Pulgar-Smith page is relevant local context. | No Arturo, Smith, Pulgar-Smith, Alexander John Heinz, CV, or family bridge appears here. |
| 6 | Jose/Juana parent candidates explain the unnamed parents. | 0.04 | The article says he inherited from his parents. Existing wiki context has Jose/Juana Pulgar-line candidates. | Parents are unnamed; no relationship, vital, property-chain, or probate bridge. |

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Good confidence for a page-local `Dr. Dario Pulgar A.`; low confidence for fuller identity attachment. |
| conflict_severity | 0.72 | High if promoted with wrong page, wrong signature reading, or name-only merge. |
| evidence_quality | 0.54 | Direct local transcription and source packet, but derivative and blocked by missing page image. |
| conversion_confidence | 0.42 | Typed body is more stable; signature and page reference remain unresolved. |
| claim_probability | 0.78 | Probable narrow claim that the article names `Dr Dario Pulgar A.` as the Fundo Los Cuartos owner/physician. |
| relevance | 1.00 | Directly addresses the assigned staged conflict. |
| canonical_readiness | 0.05 | Hold for conversion QA and identity bridge; do not promote. |

## Conflict Findings

- Name-variant conflict: active. `Pulgar A.` and `Pulgara` must remain separate literal readings until image proof review.
- Same-person conflict: unresolved outside the page-local subject. Do not merge with Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or any passenger/legal-notice cluster by name alone.
- Relationship conflict: no named parents are supported. `sus padres` is only an unnamed-parent clue.
- Chronology conflict: none within the page. Chronology risk appears only if this older physician/property-owner context is attached to later CV/Habitat or 2000 Arriagada contexts without bridge evidence.
- Duplicate-person risk: high if `Pulgara` is promoted as a new person or if `A.` is silently expanded to `Arturo` or `Arriagada`.

## Recommended Next Action

Keep the staged conflict on `hold_for_conversion_qa`. The exact next step is targeted page-image proof review for the source image corresponding to assigned source page 11 and printed page 14: reconcile the page reference, then reread the typed name and bottom-right signature. After that, run a separate identity-bridge review before any promotion to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or any Jose/Juana parent relationship.
