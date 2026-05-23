---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260523211306688
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-dd34187523f5-p0007-01-dario-arturo-pulgar-identity-candidate.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-dd34187523f5-p0007-01-dario-arturo-pulgar-identity-candidate.md
review_status: hold
canonical_readiness: hold_for_identity_bridge_and_metadata_reconciliation
reviewed_at: 2026-05-23
---

# Proof Review: identity-analysis-chunk-dd34187523f5-p0007-01-dario-arturo-pulgar-identity-candidate

## Blockers

- The page-7 body does not name `Dario Arturo Pulgar`, `Pulgar-Smith`, `Smith`, `Pulgar-Arriagada`, any parent, spouse, child, grandchild, or relationship to Alexander John Heinz. The identity claim is therefore not page-local; it depends on document title/path and surrounding CV context.
- The referenced chunk path is available, but its current front matter and manifest identify the chunk as `CHUNK-e06b38a65156-P0007-01`, not `CHUNK-dd34187523f5-P0007-01`. The assigned staged draft and source packet use the older `dd34187523f5` identifier. This is a metadata/hash reconciliation blocker before canonical promotion.
- The source packet says `converted_sha256: dd34187523f58d828db93b1178665077de8f2b50a0aba08fb688642a0722edec`, while the current chunk manifest says `e06b38a651561ee30e6fa26f27590875dfaaafc7a460011ed784da1cd6b2efda`, and the current converted file hashes locally to `538f4f9d4e9e06ec394a3a36f56135c392dec995db8102af52a827493e0d677f`. The text appears usable, but provenance identifiers are not stable.
- The opening paragraph on page 7 is a continuation of the 1989-1991 SNC Lavalin/Egypt entry from page 6, so that continuation text should not be promoted as a standalone page-7 claim without page-continuity review.
- The staged draft's comparison to canonical `Dario Arturo Pulgar-Smith` remains plausible but unproved by this page. No surname-variant bridge or family relationship appears in the page text.

## Evidence Strengths

- The cited source packet, converted file, and chunk path are present and all point to `raw/sources/CV of Dario Arturo Pulgar.pdf` and source page 7.
- The page is typed, single-column CV text with no reported uncertain or illegible words and no visual regions.
- The page text directly supports the existence of CV employment entries for FAO in Ndola, Zambia in 1988-1989; CIDA in Ethiopia in 1988; Worldview International Foundation in Rome in 1986-1987; and independent communications consulting for CIDA in 1982-1985.
- No competing person name appears on the page. This lowers internal contradiction risk, but does not independently prove the CV subject's identity.

## Scored Judgment

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.72 | Curriculum vitae text is directly relevant for occupational history, but it is self-reported and undated. |
| conversion_confidence_score | 0.78 | The typed page is fully transcribed with no uncertainty flags; score is reduced for identifier/hash mismatch and page-continuation context. |
| evidence_quantity_score | 0.50 | Several employment entries are available, but the assigned identity question has only document-level metadata support on this page. |
| agreement_score | 0.68 | Staged draft, source packet, converted file title, and source path agree on the CV context; current chunk/converted hashes disagree with the staged identifiers. |
| identity_confidence_score | 0.62 | Probable document-level attribution to Dario Arturo Pulgar, but no page-local name or Pulgar-Smith bridge. |
| claim_probability | 0.60 | The page likely belongs to the Dario Arturo Pulgar CV packet, but the identity-candidate claim should remain held until metadata and identity bridge review are complete. |
| relevance_level | high | The page is directly relevant to a Dario Arturo Pulgar CV employment cluster. |
| relevance_confidence | 0.91 | Source packet and converted file context make the page relevant despite the missing page-body name. |
| canonical_readiness | 0.18 | Not ready for canonical attachment or merge; hold for identity bridge, page-continuity review, and identifier reconciliation. |

## Verification Notes

- Literal support confirmed: page 7 records CV employment chronology and duties for 1988-1989 FAO, 1988 CIDA/Ethiopia, 1986-1987 WIF/Rome, and 1982-1985 independent communications consulting/CIDA.
- Literal support not found: page 7 does not itself state the person is Dario Arturo Pulgar, Dario Arturo Pulgar-Smith, or any other named Pulgar candidate.
- Relationship jumps: no family relationship can be inferred from this page.
- Identity risk: moderate for attaching the page to `Dario Arturo Pulgar`; higher for attaching it to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana cluster without a separate reviewed bridge.
- Conflict assessment: no internal page conflict in the employment chronology; the main conflict is provenance/identifier instability plus surname-variant uncertainty.

## Next Action

Keep the staged identity analysis on hold. Reconcile the `dd34187523f5` versus `e06b38a65156` chunk/converted identifiers, then review an identity-bearing CV page or title/front-matter evidence to prove that the page-7 employment section belongs to Dario Arturo Pulgar. Separately require a reviewed bridge before attaching this CV page to canonical `Dario Arturo Pulgar-Smith` or merging with any other Pulgar-name candidate.
