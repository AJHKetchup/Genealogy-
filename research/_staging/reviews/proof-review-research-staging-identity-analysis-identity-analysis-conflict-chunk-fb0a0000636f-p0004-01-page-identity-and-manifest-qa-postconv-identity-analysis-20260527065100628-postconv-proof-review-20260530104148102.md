---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527065100628.md
worker: postconv-proof-review-20260530104148102
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527065100628.md
review_status: hold
canonical_readiness: hold_for_page_control_manifest_qa_and_identity_bridge
source_quality_score: 0.46
conversion_confidence_score: 0.27
evidence_quantity_score: 0.42
agreement_score: 0.29
identity_confidence_score: 0.58
claim_probability: 0.47
relevance_level: high
relevance_confidence: 0.95
---

# Proof Review: Identity Analysis for CHUNK-fb0a0000636f-P0004-01

## Blockers

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527065100628.md`.
- The referenced source packet and current chunk contain 1982-1989 CV work-history text, but the current page-4 section in the converted file contains materially different 2000 IBRD / Bolivia, Peru and 1999-2000 Antamina / Huarmey, Peru entries.
- The page image needed for visible-source verification was unavailable: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg` is not present in this workspace.
- The chunk manifest lists `CHUNK-fb0a0000636f-P0004-01` twice for the same page/path with different character counts and hashes. The current on-disk chunk hash is `C8536868C8F59D4340EB31173302F11866A5475823353B2409109B0574980F15`, matching neither manifest hash.
- The current converted-file hash is `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`, while the chunk front matter records converted hash `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`.
- The reviewed page/chunk body does not literally print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Arriagada`, Jose/Juana parent candidates, Alexander John Heinz, or any parent, spouse, child, grandchild, or other kinship relationship.
- Same-person attachment to canonical `Dario Arturo Pulgar-Smith` remains plausible but unproved from this evidence. No canonical merge, relationship claim, or work-history promotion is supported while page control is unresolved.

## Evidence Strengths

- The staged draft correctly treats the matter as a hold rather than a promotion-ready identity or relationship proof.
- The source packet, converted file, chunk, chunk manifest, and source metadata are locally available and all point to the same source PDF path and source SHA-256.
- The source packet explicitly warns that its 1982-1989 derivative text should not be promoted until source-prep/conversion QA reconciles the page-control conflict.
- The staged draft keeps anti-conflation boundaries intact by not merging `Dario Arturo Pulgar` with `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Darío Pulgar Arriagada`, `Dario Pulgar A.`, or Jose/Juana parent candidates by name overlap alone.

## Scored Judgment

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.46 | The underlying source is a named CV PDF with a stable source SHA-256, but the specific page image needed to verify page 4 is missing. |
| conversion_confidence_score | 0.27 | Current page-4 conversion and derivative chunk text disagree; duplicate manifest entries and hash mismatches remain unresolved. |
| evidence_quantity_score | 0.42 | Several local metadata layers exist, but they conflict on the page body and provide no standalone identity or kinship statement. |
| agreement_score | 0.29 | The source packet and chunk agree with each other on 1982-1989 text, but they disagree with current page-4 conversion and manifest/hash control. |
| identity_confidence_score | 0.58 | Document-level attribution to `Dario Arturo Pulgar` is plausible from file/source metadata; identity with Pulgar-Smith is not proved by this page. |
| claim_probability | 0.47 | The hold judgment is supported; page-specific occupational claims and same-person claims are not promotion-ready. |
| relevance_level | high | The staged draft directly addresses the assigned page identity and manifest QA conflict. |
| relevance_confidence | 0.95 | All reviewed verification files point to the same assigned chunk/source-packet conflict. |
| canonical_readiness | hold_for_page_control_manifest_qa_and_identity_bridge | Requires page-image restoration or reread, manifest reconciliation, and separate identity-bridge proof before canonical use. |

## Claim-Level Review

The staged draft's main proof judgment is supported: keep this identity/conflict analysis on hold and do not promote page-4 work-history facts, identity merges, or relationship claims.

The narrow claim that the derivative chunk belongs to the document-level CV subject `Dario Arturo Pulgar` is plausible only through source title, source path, and document continuity. The page body itself is unnamed, and the page-control evidence is contradicted by the current page-4 conversion.

The same-person hypothesis for canonical `Dario Arturo Pulgar-Smith` remains a hold. The reviewed material does not provide the `Smith` surname, a family relationship, a date/place bridge, or another direct identity bridge.

## Next Action

Keep this staged identity analysis on hold. Restore or regenerate the page-4 image, reconcile the duplicate chunk manifest entries and current hash mismatches, and rerun conversion QA to determine which physical page controls the 1982-1989 text. After page control is resolved, run a separate identity-bridge review before attaching any CV work-history claims to a canonical person.
