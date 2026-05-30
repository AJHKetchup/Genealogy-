---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-a485f4030ce7-p0005-01-dario-cv-subject-postconv-identity-analysis-20260524105549321.md
worker: postconv-proof-review-20260530212613776
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-a485f4030ce7-p0005-01-dario-cv-subject-postconv-identity-analysis-20260524105549321.md
review_status: hold
canonical_readiness: not_ready
created: 2026-05-30
---

# Proof Review: ID-STAGE-CHUNK-a485f4030ce7-P0005-01 Dario CV Subject

## Blockers

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-a485f4030ce7-p0005-01-dario-cv-subject-postconv-identity-analysis-20260524105549321.md`.
- The staged draft and source packet identify `chunk_id` as `CHUNK-a485f4030ce7-P0005-01`, but the referenced chunk file now has front matter `CHUNK-fb0a0000636f-P0005-01`. The chunk manifest also uses `fb0a0000636f`, not `a485f4030ce7`.
- The referenced chunk path exists and contains the HABITAT/NFB/Chile Films/CITELCO work-history transcription, but the current job page file `raw/codex-conversion-jobs/.../page-markdown/page-0005.md` contains different page-5 text beginning with `1999`, `National Trust Fund for Protected Areas in Peru (PROFONANPE)`, and `Television Trust for the Environment (TVE)`.
- The chunk manifest lists duplicate entries for page 5 pointing to the same chunk path with different character counts and checksums. This supports the staged draft's conversion/provenance QA concern.
- The page image referenced by the source packet and work order, `raw/codex-conversion-jobs/.../page-images/page-0005.jpg`, is not present locally. The source PDF path `raw/sources/CV of Dario Arturo Pulgar.pdf` is also not present locally, so I could not visually or PDF-text spot-check the assigned page against the source.
- Page-local identity remains absent in the reviewed chunk text. The work-history page does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Pulgar-Smith`, `Pulgar-Arriagada`, parents, spouse, children, grandchildren, or Alexander John Heinz.
- Do not promote this staged identity analysis, merge identities, or attach the page-5 work-history facts to a canonical person page until the missing source/page image and chunk-id/page-content mismatch are resolved.

## Evidence Strengths

- The staged draft, source packet, and converted document title all identify the broader source as `CV of Dario Arturo Pulgar`, so document-level attribution to a Dario Arturo Pulgar CV is plausible.
- The referenced chunk file is readable and contains coherent typed CV-style work-history entries for `1979 - 1982` HABITAT in Nairobi, `1974 - 1978` National Film Board of Canada in Montreal, `1972 - 1973` Chile Films in Santiago, and `1970 - 1972` CITELCO in Santiago, followed by `EDUCATION`.
- The staged draft correctly treats the identity claim as document-level rather than page-local, and correctly avoids a relationship or same-person conclusion for `Dario Arturo Pulgar-Smith`.
- The staged draft's hold recommendation is directionally supported by the local evidence. The blocker is stronger than a routine spot-check concern because the referenced image/source is unavailable and the local page-5 conversion artifacts disagree.

## Scored Judgment

| metric | score | note |
| --- | ---: | --- |
| source_quality_score | 0.42 | CV source would be a relevant self-reported occupational source, but the source PDF is unavailable locally for this review. |
| conversion_confidence_score | 0.25 | The chunk text is clear, but chunk ids, converted hashes, manifest entries, and page-5 artifacts conflict; no page image/source check was possible. |
| evidence_quantity_score | 0.38 | There is one staged chunk plus packet/converted metadata; no independent identity-bearing page evidence was available. |
| agreement_score | 0.30 | Staged draft, packet, and chunk agree on the intended Dario CV context, but manifest and page-markdown artifacts materially disagree. |
| identity_confidence_score | 0.45 | Document-level identity as a Dario Arturo Pulgar CV is plausible; page-local identity and Pulgar-Smith bridge are unsupported. |
| claim_probability | 0.40 | Probable that the chunk belongs somewhere in a Dario Arturo Pulgar CV work-history cluster, but not reliable enough for canonical attachment from this artifact set. |
| relevance_level | high | If provenance is repaired, the chunk is relevant to occupational and residence/activity claims for the CV subject. |
| relevance_confidence | 0.82 | The work-history content is genealogically useful, but only after source/page alignment is verified. |
| canonical_readiness | 0.05 | Not ready due to missing source/page image, chunk-id/hash mismatch, duplicate manifest entries, and no page-local identity bridge. |

## Claim-Level Review

| claim or hypothesis | support | probability | disposition |
| --- | --- | ---: | --- |
| The reviewed chunk is CV work-history evidence for a document titled `CV of Dario Arturo Pulgar` | Supported by title/metadata and chunk content, not by a visible page-source check | 0.62 | hold for conversion QA |
| Page 5 itself names Dario Arturo Pulgar | Not supported; the reviewed chunk body does not print the subject's name | 0.02 | reject for page-local claim |
| The CV subject is the same person as canonical `Dario Arturo Pulgar-Smith` | Name similarity and staged candidate only; no page-local bridge | 0.35 | hold, separate identity-bridge review needed |
| The page supports parent, spouse, child, grandchild, or Alexander John Heinz relationship claims | No relationship language in the reviewed chunk | 0.00 | reject for this source page |
| The page supports merging with Pulgar-Arriagada or Dario Pulgar A. candidates | No `Jose`, `J.`, `Arriagada`, `A.`, medical, diplomatic, passenger, property, or parentage bridge in the chunk | 0.03 | reject for this source page |

## Next Action

Hold this staged draft. Restore or locate the original source PDF and rendered page image, then reconcile the `a485f4030ce7` versus `fb0a0000636f` converted hashes/chunk ids and the duplicate page-5 manifest entries. After the page-source alignment is verified, create a separate identity-bridge review before attaching any work-history facts to `wiki/people/dario-arturo-pulgar-smith.md` or any Pulgar-Arriagada candidate.

