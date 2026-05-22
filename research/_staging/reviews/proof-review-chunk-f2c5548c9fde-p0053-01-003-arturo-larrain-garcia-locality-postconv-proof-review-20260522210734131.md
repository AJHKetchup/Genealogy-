---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260522210734131
task_id: proof-review:research/_staging/claims/chunk-f2c5548c9fde-p0053-01-003-arturo-larrain-garcia-locality.md
staged_draft: research/_staging/claims/chunk-f2c5548c9fde-p0053-01-003-arturo-larrain-garcia-locality.md
reviewed_claim_type: locality
reviewed_subject: "Arturo Larraín García"
reviewed_predicate: "was listed at locality"
reviewed_object: "Santiago"
source: "raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf"
source_packet: "research/_staging/source-packets/chunk-f2c5548c9fde-p0053-01-arturo-larrain-lavin-medical-directory.md"
converted_file: "raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-41-60.codex.md"
chunk: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dic-8fbd29c654/page-0053-chunk-01.md"
chunk_id: CHUNK-f2c5548c9fde-P0053-01
source_page_image_checked: unavailable
source_quality_score: 0.72
conversion_confidence_score: 0.63
evidence_quantity_score: 0.46
agreement_score: 0.84
identity_confidence_score: 0.78
claim_probability: 0.74
relevance_level: contextual
relevance_confidence: 0.80
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Arturo Larraín García Locality Santiago

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The chunk records a rendered page image at `raw/codex-conversion-jobs/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-41-60/page-images/page-0053.jpg`, but that file is not present in the conversion job directory, so the row cannot be visually reread under this task.
- The conversion method is Docling basic conversion with readability status `rough_ok`, and the chunk explicitly says conversion QA must compare the output with the rendered page image before research extraction.
- The claim is only a directory locality listing. It does not prove birth, death, residence duration, family relationship, or identity with any canonical Arturo Larraín García beyond the directory name string.

## Evidence Strengths

- The staged draft, source packet, chunk, and converted page all give the same converted table row: `| Larraín García, Arturo | Vicuña Mackenna 4, 7' Piso | Santiago |`.
- The locality `Santiago` appears in the same converted row as `Larraín García, Arturo`, so the claim has direct literal support if the conversion is accepted.
- The page context is an alphabetized national medical directory table of names, addresses, and localities. That source type is relevant for a medical-directory locality mention.
- No conflicting locality for this exact row was found in the reviewed staged draft, source packet, converted page excerpt, or chunk.

## Scored Judgment

- `source_quality_score: 0.72` - a dated national medical directory is reasonably good for a professional directory listing, but it is derivative directory evidence and not a vital or civil record.
- `conversion_confidence_score: 0.63` - the converted row is clear and internally consistent, but the absent page image prevents visual confirmation of name, row alignment, and locality.
- `evidence_quantity_score: 0.46` - one source row only; no independent corroborating source was reviewed for this task.
- `agreement_score: 0.84` - all reviewed staging materials agree on the row and locality; reduced because they all depend on the same unverified conversion.
- `identity_confidence_score: 0.78` - the directory row names `Larraín García, Arturo` directly, but this task reviewed no external identity-linking evidence to a canonical person.
- `claim_probability: 0.74` - probably supported as a directory-locality claim, pending visual reread of page 53.
- `relevance_level: contextual`; `relevance_confidence: 0.80` - useful professional locality context, not vital-event or relationship evidence.
- `canonical_readiness: hold_for_conversion_qa`.

## Next Action

Keep the claim in staging. Perform conversion QA or restore/render `page-0053.jpg` and visually reread the `Larraín García, Arturo` row to confirm the name, row alignment, address, and locality before any canonical promotion.
