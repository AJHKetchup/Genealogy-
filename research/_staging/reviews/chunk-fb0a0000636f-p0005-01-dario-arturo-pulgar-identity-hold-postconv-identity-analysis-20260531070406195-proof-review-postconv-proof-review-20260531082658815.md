---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531082658815
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-dario-arturo-pulgar-identity-hold-postconv-identity-analysis-20260531070406195.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-dario-arturo-pulgar-identity-hold-postconv-identity-analysis-20260531070406195.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531045753452.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
canonical_readiness: hold
---

# Proof Review: Dario Arturo Pulgar Page-5 Identity Hold

## Blockers

1. Physical page control is not established. The recorded source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent in this workspace, so the physical page cannot be checked directly from the raw source.
2. The page-5 derivative texts disagree materially. The assigned chunk contains 1979-1982 HABITAT/Nairobi, 1974-1978 National Film Board of Canada/Montreal, 1972-1973 Chile Films/Santiago, and 1970-1972 CITELCO/Santiago. The conversion-job page Markdown for page 5 instead contains 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen/SNC Lavalin entries.
3. Conversion integrity is blocked. The source packet reports recorded-to-observed SHA256 drift, and direct hash checks confirm the current converted file and chunk do not match the recorded hashes in the chunk front matter/manifest. The chunk manifest also lists the same page-5 chunk id twice with different character counts and hashes.
4. The page body does not identify the person. It does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or any parent/spouse/child relationship.
5. No relationship or surname-variant claim is proved. This evidence supports only a hold-level question about whether a CV titled for `Dario Arturo Pulgar` belongs to the same person as `Dario Arturo Pulgar-Smith`; it does not support changing the source reading or attaching lineage.

## Evidence Strengths

- The staged draft accurately preserves the hold posture and does not promote the identity or occupational claims.
- The source packet, converted document title, and source path consistently describe the broader source as a CV of `Dario Arturo Pulgar`.
- The assigned chunk is internally coherent as a CV work-history page if later certified as the controlling physical page transcription.
- The competing derivative page is explicit enough to show that the conflict is substantive, not a minor transcription variation.
- The staged draft correctly separates document-level metadata from page-body proof and relationship proof.

## Scored Judgment

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 4/10 | A CV can be useful for work-history claims, but here the raw source is absent and only derivative text is available. |
| conversion_confidence_score | 2/10 | Page-control conflict, hash drift, and duplicate manifest entries block reliance on either page-5 reading. |
| evidence_quantity_score | 3/10 | Multiple local derivatives were checked, but they are conflicting derivatives rather than independent controlled evidence. |
| agreement_score | 2/10 | Metadata agrees on a CV title, while the actual page-5 content disagrees sharply. |
| identity_confidence_score | 6/10 document-level `Dario Arturo Pulgar`; 3/10 for `Dario Arturo Pulgar-Smith`; 1/10 for Pulgar-Arriagada/Jose/Juana hypotheses | The title/path support a document-level subject, but the page body supplies no identity bridge or family relationship. |
| claim_probability | 0.65 document-level CV attribution; 0.20 page-5 occupational claims; 0.30 attachment to `Dario Arturo Pulgar-Smith`; 0.05 or lower for Pulgar-Arriagada or parentage claims | Probability is held down by missing page control and absent identity-bearing text. |
| relevance_level | high | The reviewed draft is directly about this staged identity and this CV page. |
| relevance_confidence | 0.90 | The local files are plainly relevant even though proof value is blocked. |
| canonical_readiness | hold | Do not promote, merge, rename, or attach to canonical people/families. |

## Review Finding

The staged draft is supported as a hold. The checked files justify preserving `Dario Arturo Pulgar` as a document-level candidate identity from metadata, but not as a controlled page-level claim and not as a bridge to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana relationship cluster.

The hard transcription boundary should remain intact: asking whether this CV belongs to Dario is reasonable, but changing a source reading to a fuller surname variant or attaching family relationships would be unsupported by the visible page text and unsafe while page 5 has competing derivative readings.

## Next Action

Keep the staged draft on hold. The next action is conversion QA: restore or regenerate authoritative access to physical page 5, compare it against both derivative readings, and repair the converted/chunk manifest and hash drift. After physical page control is certified, run a separate identity-bridge proof review before attaching any accepted page-5 work-history claim to a canonical person page.
