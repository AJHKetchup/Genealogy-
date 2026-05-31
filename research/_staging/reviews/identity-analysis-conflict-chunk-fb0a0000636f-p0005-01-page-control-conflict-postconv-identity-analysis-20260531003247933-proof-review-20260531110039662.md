---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
worker: postconv-proof-review-20260531105953173
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_competing_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
page_reference: page 5
review_status: hold
canonical_readiness: not_ready
created: 2026-05-31
---

# Proof Review: Page 5 CV Identity/Conflict Analysis

## Blockers

- The staged draft is supported as a page-control conflict, not as promotion-ready person or work-history proof. The assigned chunk and current aggregate converted file contain the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence, while the conversion-job page Markdown for `page-0005.md` contains the competing 1999-1997 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence.
- The page image needed to choose the controlling physical page-5 transcription is unavailable locally. `page-images/page-0005.jpg` and `extracted-images/page-0005.jpg` both tested absent, even though the source manifest records a page-5 image path and hash.
- Hash/provenance control is broken. The chunk manifest records converted SHA-256 `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, but the observed converted-file SHA-256 is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`. The observed page-5 chunk SHA-256 is `d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d`, while the manifest has duplicate `CHUNK-fb0a0000636f-P0005-01` rows with different recorded hashes and character counts.
- The page body does not identify a person by full name. `Dario Arturo Pulgar` is supported only by document-level title/path metadata, not by either competing page-5 body.
- No reviewed page-5 material states `Pulgar-Smith`, `Pulgar-Arriagada`, spouse, child, grandchild, parent, Alexander John Heinz, Jose, or Juana. Any identity merge or relationship claim from this page would be a relationship jump.

## Evidence Scores

| metric | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.62 | A CV can be useful first-person or subject-level evidence, but this review could not inspect the physical page image and the page-control chain is broken. |
| conversion_confidence_score | 0.15 | Two derivative transcriptions conflict for the same page, the page image is absent, and hashes do not match recorded metadata. |
| evidence_quantity_score | 0.42 | There is enough derivative evidence to prove a provenance conflict and hold decision, but not enough verified evidence to prove a page-5 occupational claim. |
| agreement_score | 0.18 | The assigned chunk and aggregate converted file agree with each other, but they disagree with `page-markdown/page-0005.md` and the physical image is not available to arbitrate. |
| identity_confidence_score | 0.35 | Document-level attribution to Dario Arturo Pulgar is plausible from the source title, but page-local identity evidence is absent and no bridge to Pulgar-Smith is present. |
| claim_probability | 0.30 | Probability is low for any promoted page-5 work-history claim because page control is unresolved; probability is high only that a conversion conflict exists. |
| relevance_level | high | The CV is family-relevant and page-5 content would be useful once controlled. |
| relevance_confidence | 0.90 | The source title and source packet make the Dario/Pulgar relevance clear, despite the page-local identity gap. |
| canonical_readiness | not_ready | Hold for conversion QA and separate identity-bridge review before canonical use. |

## Evidence Strengths

- The staged draft accurately reports the central conflict: the assigned derivative chunk contains `1979 - 1982` United Nations Centre for Human Settlements (HABITAT), `1974 - 1978` National Film Board of Canada, `1972 - 1973` Chile Films, and `1970 - 1972` Cine, Television y Comunicaciones (CITELCO).
- The competing conversion-job page Markdown for the same page number visibly begins with `1999` and contains PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture entries.
- The source packet's hold recommendation is directly supported by the observed derivative disagreement, duplicate manifest rows, missing page image, and hash mismatches.
- The staged draft correctly separates document-level subject attribution from page-body transcription. It does not treat the source title as if the page itself printed the full identity.

## Claim Review

- Page-control claim: supported. The review confirms a material page-control/provenance conflict for page 5.
- Occupational claims from the 1979-1970 derivative: hold. The text is present in the assigned chunk and aggregate converted file, but it cannot be treated as controlling physical page 5 without the missing image or a repaired conversion chain.
- Occupational claims from the 1999-1997 derivative: hold. The text is present in `page-markdown/page-0005.md`, but it conflicts with the assigned chunk and current aggregate converted file.
- Identity claim that document-level `Dario Arturo Pulgar` is canonical `Dario Arturo Pulgar-Smith`: not ready. Name similarity and source title relevance are not enough; no page-local bridge states `Smith`, family relationships, dates, or other identity anchors.
- Relationship claims to Alexander John Heinz, parents, spouse, children, Jose/Juana candidates, or Pulgar-Arriagada candidates: unsupported by the reviewed page-5 materials.

## Next Action

Hold for conversion QA. Restore or re-render physical page 5 from `raw/sources/CV of Dario Arturo Pulgar.pdf`, compare the image directly against the assigned chunk and `page-markdown/page-0005.md`, reconcile the duplicate manifest entries and hash mismatches, and certify one controlling page-5 transcription.

After page-control repair, run a separate identity-bridge proof review before attaching any page-5 CV claims to `wiki/people/dario-arturo-pulgar-smith.md` or to any Pulgar-Arriagada/Jose/Juana cluster. No canonical promotion is recommended from this review.
