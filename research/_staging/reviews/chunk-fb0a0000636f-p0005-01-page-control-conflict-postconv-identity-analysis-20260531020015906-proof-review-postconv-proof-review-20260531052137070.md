---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531052137070
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020015906.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020015906.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531010209483.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: blocked
---

# Proof Review: CV Page 5 Page-Control Conflict

## Blockers First

1. Canonical promotion is blocked because the assigned chunk and conversion-job page Markdown preserve incompatible page-5 readings. The assigned chunk has a 1979-1970 work-history page ending with `EDUCATION`; `page-markdown/page-0005.md` has a 1999-1997 consulting-work page.
2. The recorded original source PDF is absent at `raw/sources/CV of Dario Arturo Pulgar.pdf`, so the physical source page cannot be checked in this proof-review pass.
3. No rendered page-5 image was found under the conversion-job tree. Only page Markdown, visuals JSON, and a work order for page 5 are present.
4. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for the same chunk path with conflicting character counts and SHA-256 values.
5. Current observed hashes do not match recorded metadata: the converted file hashes to `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`, while the manifest/frontmatter records `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`; the current chunk hashes to `D6EA4F611EE03000C11CBBA63246E95B55F8A421FCBC87D0D667E91F5C8D0B8D`, matching neither duplicated manifest entry.
6. Page 5 does not state parents, spouse, children, `Smith`, `Jose`, `Juana`, `Arriagada`, or Alexander John Heinz. Any same-person, family, or relationship claim remains unsupported by this page.

## Evidence Strengths

- The staged draft's main conclusion is supported: this is a derivative-integrity/page-control conflict, not a promotion-ready identity event.
- The assigned chunk plainly supports the local existence of the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO transcription.
- The conversion-job page Markdown plainly supports the competing 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting, 1997-1998 Klohn Crippen, and SNC Lavalin transcription.
- The source packet accurately flags the absent source file, duplicate manifest metadata, observed hash drift, and high uncertainty about which derivative controls physical page 5.
- The source title/path and surrounding conversion context make the document relevant to a `Dario Arturo Pulgar` CV cluster, but that is document-level context only.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 4/10 |
| conversion_confidence_score | 1/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 |
| identity_confidence_score | 5/10 for document-level `Dario Arturo Pulgar` context from title/path; 2/10 for same as `Dario Arturo Pulgar-Smith`; 1/10 for `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or Jose/Juana parent attachment |
| claim_probability | 0.96 that the local derivative conflict exists; 0.32 that the assigned-chunk 1979-1970 text controls physical page 5; 0.32 that the conversion-job 1999-1997 text controls physical page 5; 0.02 for any page-5 family relationship claim |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | blocked |

## Review Finding

The staged draft is supported as a hold/block analysis. The available verification context proves that two incompatible page-5 derivative readings exist and that the files needed to adjudicate physical page control are missing or internally inconsistent.

No literal source support was found for attaching this page-5 evidence to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, Jose/Juana parent candidates, or Alexander John Heinz. The only defensible identity statement from this review is that the document metadata/title points to a `Dario Arturo Pulgar` CV cluster, subject to conversion QA.

## Next Action

Hold for conversion QA. Restore or regenerate the original PDF/page-5 image, reconcile duplicate manifest entries for `CHUNK-fb0a0000636f-P0005-01`, recompute and record current hashes, and certify the controlling page-5 transcription before promoting any work-history claim. After page control is repaired, run a separate identity-bridge proof review before attaching any accepted CV claim to a canonical person.
