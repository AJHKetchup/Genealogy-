---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260531103534217
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
staged_draft_reviewed: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
source_packet_checked: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md
converted_file_checked: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk_checked: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conversion_page_checked: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
review_status: hold
canonical_readiness: not_ready
created: 2026-05-31
---

# Proof Review: Page-Control Conflict For CHUNK-fb0a0000636f-P0005-01

## Blockers

- The staged draft is correctly held because physical page control is unresolved. The assigned chunk for `CHUNK-fb0a0000636f-P0005-01` contains the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence, while the conversion-job `page-markdown/page-0005.md` contains the 1999-1997 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence.
- The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with different character counts and recorded hashes, and the observed hashes for both the aggregate converted file and assigned chunk differ from the recorded metadata in the packet/chunk.
- Local `page-images/page-0005.jpg` is unavailable in the conversion-job folder, so this review cannot adjudicate the physical page from the image.
- The staged draft needs a precision revision if reused: it says the "current aggregate converted file" contains the 1979-1970 text, but the checked aggregate file contains both the 1999-1997 page-5 section and a later duplicate page section with the 1979-1970 text. This strengthens the page-control/duplicate-section concern and does not make either occupational sequence promotion-ready.
- No page-local body text names `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, parent candidates, spouse, child, grandchild, or Alexander John Heinz. Subject attribution is only document-level from the source title/path and metadata.

## Scores

| measure | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.62 | A CV is relevant but self-authored/derivative, and the physical page image is unavailable for this review. |
| conversion_confidence_score | 0.12 | Page-control conflict, duplicate manifest rows, missing local page image, and hash mismatches block reliance on either page-5 derivative. |
| evidence_quantity_score | 0.38 | There are multiple derivative texts and metadata records, but they conflict on the controlling page content. |
| agreement_score | 0.18 | Assigned chunk and conversion-job page Markdown disagree materially; aggregate file includes both sequences. |
| identity_confidence_score | 0.45 | Document-level title supports a Dario Arturo Pulgar CV, but page-local identity and canonical Pulgar-Smith bridge are absent. |
| claim_probability | 0.20 | The claim that this draft should be held is high-probability, but any occupational/person claim from page 5 is low-probability until page control is repaired. |
| relevance_level | high | The CV subject and Pulgar surname are family-relevant, and the conflict affects potential work-history evidence. |
| relevance_confidence | 0.90 | The source title and staged packet clearly concern the Pulgar CV workflow. |
| canonical_readiness | not_ready | Do not promote occupational, identity, or relationship claims from this staged draft. |

## Evidence Strengths

- The draft's main conclusion, `hold` / `not_ready`, is directly supported by the packet, assigned chunk, conversion-job page Markdown, aggregate file, and manifest.
- The assigned chunk clearly transcribes the 1979-1970 occupational sequence, including HABITAT in Nairobi, NFB in Montreal, Chile Films in Santiago, and CITELCO in Santiago.
- The conversion-job page Markdown clearly transcribes a different page-5 sequence beginning with 1999 PROFONANPE in Peru and continuing through TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The source packet accurately identifies the identity limitation: the source title names the CV subject as Dario Arturo Pulgar, but the assigned page body does not independently restate the full name.
- The draft appropriately rejects relationship jumps. No parent, spouse, child, grandchild, or Alexander John Heinz relationship is stated in the reviewed page derivatives.

## Review Judgment

The staged identity/conflict analysis is supportable as a hold note, with one precision issue about the aggregate converted file containing both competing sequences rather than only the 1979-1970 sequence. That issue does not undermine the hold decision; it makes the page-control conflict more concrete.

No canonical identity merge is justified from this evidence. Document-level `Dario Arturo Pulgar` may be relevant to `Dario Arturo Pulgar-Smith`, but the reviewed page materials do not provide a literal bridge to `Pulgar-Smith`, to any Pulgar-Arriagada candidate, or to Jose/Juana parent clusters.

## Next Action

Keep this item on hold for conversion QA. Re-render or restore physical page 5 from `raw/sources/CV of Dario Arturo Pulgar.pdf`, compare the visible page directly against the assigned chunk and `page-markdown/page-0005.md`, then repair the aggregate file/chunk manifest/hash metadata before any proof review promotes page-5 occupational claims or attaches them to a canonical person.
