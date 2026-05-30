---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530231622087
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold
---

# Proof Review: CV Page-Control Conflict for CHUNK-fb0a0000636f-P0005-01

## Blockers First

1. Do not promote page-5 work-history claims from this draft yet. The assigned chunk for page 5 contains the `1979 - 1982` through `1970 - 1972` HABITAT/NFB/Chile Films/CITELCO sequence, but the conversion job `page-markdown/page-0005.md` contains a different `1999` through `1997-1998` PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence.
2. The source PDF and page image needed for visual verification are unavailable in this checkout: `raw/sources/CV of Dario Arturo Pulgar.pdf` and the expected `page-images/page-0005.jpg` both tested absent.
3. The source packet records converted-file hash drift, and the chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` with different metadata. This blocks choosing either derivative transcript as controlling source text.
4. No checked page-5 derivative text names `Smith`, parents, spouse, children, Alexander John Heinz, Jose/Juana candidates, or a kinship relationship. Name or family expansion would be an identity jump from this item.

## Evidence Strengths

- The staged draft accurately identifies a real page-control conflict between the assigned chunk and the conversion job page Markdown.
- The assigned chunk is internally coherent CV text and contains readable work-history entries for HABITAT, National Film Board of Canada, Chile Films, and CITELCO.
- The conversion job page Markdown is also internally coherent CV text and contains readable work-history entries for PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The aggregate converted file contains both disputed text sequences, which supports the staged draft's assessment that this is likely a conversion/page-control problem rather than a proved identity conflict.
- The staged draft correctly keeps same-person attachment to canonical `Dario Arturo Pulgar-Smith` and anti-conflation candidates such as `Dario/Dario Jose/Dario Arturo/Dario Arriagada` on hold.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 for the underlying CV type if source control is restored; 2/10 for this review because the source PDF and page image are absent |
| conversion_confidence_score | 2/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 between controlling page derivatives; 7/10 that all checked derivatives are plausible CV material |
| identity_confidence_score | 5.5/10 for document-level `Dario Arturo Pulgar` from title/context only; 2.5/10 for attachment to canonical `Dario Arturo Pulgar-Smith`; 1/10 for attachment to `Dario Jose Pulgar-Arriagada` or `Darío Pulgar Arriagada` |
| claim_probability | 0.45 that the assigned chunk's 1979-1970 sequence is controlling page 5; 0.50 that the conversion job page Markdown's 1999-1997 sequence is controlling page 5; 0.70 that both sequences belong somewhere in the same CV but page/chunk control is corrupted; 0.05 for any kinship claim from this page |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold / not ready |

## Review Finding

The staged draft is supported as a hold for conversion QA. Literal support exists for two mutually inconsistent page-5 transcriptions in derivative files, but the visible source needed to adjudicate them is missing. Because the page body does not repeat the full document subject name or provide family identifiers, this evidence cannot safely attach the page to `Dario Arturo Pulgar-Smith`, merge any Pulgar identity clusters, or support Jose/Juana/Alexander relationship claims.

## Next Action

Keep this item on hold for conversion QA. Restore or regenerate the source PDF/page image, repair or reconcile the duplicate manifest entries and hash drift, then compare the visible physical page 5 against the two derivative transcripts. After page control is resolved, rerun proof review for narrow work-history claims and handle any canonical identity bridge in a separate review using source text that actually names or links the identity.
