---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531041745891
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003129113.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003129113.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530234356813.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: CV Page-Control Identity Hold

## Blockers First

1. Do not promote any page-5 occupational, residence, travel, education, or chronology claim from this staged draft. The assigned `page-0005-chunk-01.md` contains 1979-1970 work-history text, while the conversion-job `page-markdown/page-0005.md` and rough Docling discovery for page 5 contain 1999-1997 consulting-work text.
2. The assigned chunk's 1979-1970 text aligns with rough Docling discovery for page 8, not rough Docling discovery for page 5. Docling discovery is not evidence-grade, but it reinforces that the assigned chunk is not reliable page-5 control evidence.
3. The referenced raw source file `raw/sources/CV of Dario Arturo Pulgar.pdf` was not available in this workspace check, and no `page-images/page-0005.jpg` or `extracted-images/page-0005.jpg` exists under the referenced conversion job. I could not verify the visible source page directly.
4. Do not attach this staged evidence to canonical `Dario Arturo Pulgar-Smith` or to any Pulgar-Arriagada/Jose/Juana relationship cluster. The reviewed page body does not state `Pulgar-Smith`, `Pulgar-Arriagada`, parents, spouse, children, grandchildren, birth data, or another direct identity bridge.

## Evidence Strengths

- The source packet accurately reports the core page-control conflict, duplicate chunk-manifest entries, observed hash drift, and missing page image problem.
- The assigned chunk and source packet consistently preserve the same 1979-1970 work-history text beginning with United Nations Centre for Human Settlements (HABITAT) and ending with CITELCO plus an `EDUCATION` heading.
- The conversion-job page Markdown and rough Docling page 5 discovery consistently preserve a different 1999-1997 consulting-work page beginning with PROFONANPE and including TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The staged identity analysis is correct to keep the canonical identity and relationship questions on hold rather than treating document title/name overlap as proof.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 4/10 |
| conversion_confidence_score | 2/10 for the assigned page-5 chunk; 7/10 that a page-control conflict exists |
| evidence_quantity_score | 4/10 |
| agreement_score | 2/10 for page-5 control; 8/10 between page-markdown and rough discovery that page 5 is the 1999-1997 text |
| identity_confidence_score | 6/10 for document-level CV subject `Dario Arturo Pulgar`; 4/10 for same person as canonical `Dario Arturo Pulgar-Smith`; 1/10 for Pulgar-Arriagada/Jose/Juana merges from this page |
| claim_probability | 0.95 that the staged item should remain on hold for conversion QA; 0.20 for any page-5 occupational claim from the assigned chunk; 0.40 for attachment to canonical `Dario Arturo Pulgar-Smith`; 0.05 for any family relationship claim |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold_for_conversion_qa / not_ready |

## Review Finding

The staged analysis is supported in its main conclusion: this is not ready for canonical promotion. The strongest review finding is a conversion-control blocker, not an identity proof. Local derivatives conflict over which text controls physical page 5, and the assigned chunk appears to be displaced page text rather than settled page-5 evidence.

The document title and staging metadata make `Dario Arturo Pulgar` a plausible document-level CV subject, but the reviewed page text does not independently name him. It also does not provide a bridge to `Dario Arturo Pulgar-Smith`, Pulgar-Arriagada candidates, or Jose/Juana parent candidates.

## Next Action

Keep this item on `hold_for_conversion_qa`. Restore or inspect the raw PDF/page image, certify the controlling transcription for physical page 5, repair the duplicate manifest/hash drift, then rerun proof review against the certified page text. After page control is resolved, perform a separate identity-bridge review before attaching any CV claims to a canonical person page.
