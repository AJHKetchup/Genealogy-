---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531082915169
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-dario-arturo-pulgar-identity-hold-postconv-identity-analysis-20260531065431265.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-dario-arturo-pulgar-identity-hold-postconv-identity-analysis-20260531065431265.md"
staged_identity_draft: "research/_staging/identity/chunk-fb0a0000636f-p0005-01-dario-arturo-pulgar-identity-hold-postconv-evidence-extraction-20260531045753452.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531045753452.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: blocked
---

# Proof Review: Dario Arturo Pulgar CV Page 5 Identity Hold

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-dario-arturo-pulgar-identity-hold-postconv-identity-analysis-20260531065431265.md`.

## Blockers First

1. Keep the item on hold. The assigned chunk's page-5 text begins with 1979-1982 HABITAT/Nairobi, while the conversion-job page Markdown for page 5 begins with 1999 PROFONANPE/TVE and 1998-1999 Arca Consulting/European Commission. These cannot both be the controlling physical page-5 transcription.
2. Source control is blocked. `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent at the recorded path in this workspace, so this review cannot compare either derivative reading against the physical PDF/page image.
3. Hash and manifest control are blocked. The converted file and chunk hashes observed locally differ from the recorded hashes, and the chunk manifest lists the same page-5 chunk id twice with different char counts and hashes.
4. Do not promote an identity bridge to `wiki/people/dario-arturo-pulgar-smith.md`. The page body does not print `Dario Arturo Pulgar-Smith`, `Smith`, birth details, family relationships, Alexander John Heinz, or other bridge evidence.
5. Do not merge or connect this item to `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, Jose/Juana parent candidates, or any family relationship. None of those names or relationships appear in the reviewed page-body text.

## Evidence Strengths

- The source packet, staged identity draft, converted document title, and source path all identify the broader document as `CV of Dario Arturo Pulgar`.
- The assigned chunk is a plausible CV work-history page and is internally legible, listing HABITAT, National Film Board of Canada, Chile Films, and CITELCO entries.
- The staged identity analysis correctly treats the page-body identity support as weak and recommends `hold_for_conversion_qa`.
- The canonical `Dario Arturo Pulgar-Smith` page explicitly warns not to attach similarly named Dario/Pulgar records without identity review, matching the conservative handling here.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 3/10 for this review pass because the source is a CV but the physical PDF is absent at the recorded path |
| conversion_confidence_score | 1/10 because page-control, hash, and duplicate-manifest conflicts are unresolved |
| evidence_quantity_score | 2/10 for identity; document-title evidence exists, but page-local identity and family evidence are absent |
| agreement_score | 2/10 because the derivative page-5 readings materially disagree |
| identity_confidence_score | 5/10 for document-level `Dario Arturo Pulgar` subject attribution; 3/10 for same person as `Dario Arturo Pulgar-Smith`; 1/10 or lower for Pulgar-Arriagada/Jose/Juana relationship claims |
| claim_probability | 0.58 that the broader CV source concerns `Dario Arturo Pulgar`; 0.30 that this page can be attached to canonical `Dario Arturo Pulgar-Smith`; 0.05 or lower for Pulgar-Arriagada/Jose/Juana identity or relationship claims |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | blocked; hold for conversion/page-control QA and later identity-bridge review |

## Review Finding

The staged draft is supported as a hold, not as promotion-ready evidence. The only reasonably supported identity statement is document-level: the source title and converted document title identify a CV of `Dario Arturo Pulgar`. The reviewed page body does not independently name the subject or prove that this document subject is the family-supplied canonical `Dario Arturo Pulgar-Smith`.

The page-control conflict is the controlling issue. Because the local converted file contains both the 1999-1997 consulting sequence and the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence under page-5 contexts, and because the source PDF is absent, no canonical claim should be promoted from this page now.

## Next Action

Hold for conversion/page-control QA. Restore or verify authoritative access to `raw/sources/CV of Dario Arturo Pulgar.pdf` or a rendered page-5 image, compare the physical page against the competing derivative readings, repair manifest/hash drift through the conversion workflow, and then run a separate identity-bridge review before attaching any accepted CV work-history claim to `wiki/people/dario-arturo-pulgar-smith.md`.
