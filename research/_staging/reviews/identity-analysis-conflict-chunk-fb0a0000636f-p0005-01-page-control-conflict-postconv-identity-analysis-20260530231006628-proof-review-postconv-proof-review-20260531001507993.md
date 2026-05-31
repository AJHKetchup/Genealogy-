---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260531001507993
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231006628.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231006628.md
review_status: hold
canonical_readiness: hold_for_conversion_qa_not_ready
source_quality_score: 0.55
conversion_confidence_score: 0.25
evidence_quantity_score: 0.45
agreement_score: 0.20
identity_confidence_score: 0.40
claim_probability: 0.88
relevance_level: direct
relevance_confidence: 0.97
---

# Proof Review: Page-Control Conflict For CHUNK-fb0a0000636f-P0005-01

## Blockers

- Source visibility is blocked. `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent in this checkout, and the referenced rendered page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is also absent, so the physical page cannot be visually checked.
- Page control is unresolved. The assigned chunk and source packet transcribe page 5 as a 1979-1970 work-history page, while `page-markdown/page-0005.md` transcribes the same page number as a 1999-1997 work-history page.
- Provenance control is weak. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for the same path/page with different character counts and hashes, and the source packet records a mismatch between the converted hash in the chunk metadata and the observed converted-file hash.
- Identity support is document-level only. The page-5 derivative text reviewed here does not independently name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or a parent/spouse/child relationship.
- Relationship and merge claims are unsupported. This staged draft cannot resolve Jose/Juana parent candidates, Pulgar-Arriagada candidates, passenger-list Dario candidates, or a merge between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231006628.md`.
- Source packet: `research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md`.
- Assigned chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`.
- Conversion job page Markdown: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`.
- Chunk manifest: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json`.
- Conversion job manifest: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/manifest.json`.

No external research was performed. No raw source, converted Markdown, chunk, source packet, or canonical wiki page was edited.

## Scored Judgment

| metric | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.55 | A CV can be useful direct evidence for occupational chronology, but the source PDF and rendered page are unavailable for this review. |
| conversion_confidence_score | 0.25 | Two incompatible derivative transcriptions claim page 5, and manifest/hash metadata is inconsistent. |
| evidence_quantity_score | 0.45 | There are multiple local derivatives, but they are not independent source confirmations and disagree materially. |
| agreement_score | 0.20 | Agreement exists within the chunk/source-packet pair and within the page-markdown/job-manifest pair, but not across the controlling evidence chain. |
| identity_confidence_score | 0.40 | Document title supports a Dario Arturo Pulgar subject label, but page-local identity is absent and no bridge to Pulgar-Smith or Pulgar-Arriagada is proved. |
| claim_probability | 0.88 | High probability that the staged draft's `hold_for_conversion_qa` / `not_ready` judgment is correct; no promoted occupational or identity claim exceeds hold threshold. |
| relevance_level | direct | The reviewed files are the exact staged draft and referenced page-control evidence. |
| relevance_confidence | 0.97 | The conflict is directly about the assigned chunk and page 5. |
| canonical_readiness | hold_for_conversion_qa_not_ready | Do not promote, attach, merge, or use for canonical work-history, identity, or relationship claims until page control is certified. |

## Evidence Strengths

- The staged draft accurately identifies a severe page-control conflict: the assigned chunk contains `1979 - 1982` HABITAT, `1974 - 1978` National Film Board of Canada, `1972 - 1973` Chile Films, and `1970 - 1972` CITELCO entries.
- The competing `page-markdown/page-0005.md` file does contain different page-5 content beginning with `1999` PROFONANPE and Television Trust for the Environment entries, followed by 1998-1999 and 1997-1998 consultant entries.
- The source packet's cautious framing is supported: it treats the page as held for conversion QA and states that neither derivative page-5 body supplies family relationship evidence or a canonical identity attachment.
- The review outcome is well aligned with the available evidence: this is a conversion/provenance conflict, not a promoted genealogical fact.

## Literal Support And Limits

The local derivatives support only the existence of competing transcriptions for the same page label. They do not support choosing the 1979-1970 text over the 1999-1997 text, or the reverse, because the visible source page is unavailable.

The document-level title `CV of Dario Arturo Pulgar` is relevant but insufficient to prove that the page-5 work-history entries belong to canonical `Dario Arturo Pulgar-Smith` or to any Pulgar-Arriagada candidate. No parent, spouse, child, household, or kinship statement appears in the reviewed page-5 derivatives.

## Next Action

Keep this staged draft on hold. Conversion/source-prep QA must restore or locate the authoritative source PDF or rendered page image for page 5, visually determine which derivative transcription controls the physical page, and repair or regenerate the duplicated manifest/hash chain before any proof review can promote page-5 claims.

After page control is certified, rerun proof review for the surviving page-5 occupational claims and perform a separate identity-bridge review before attaching any CV evidence to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío/Dario Pulgar Arriagada`, any passenger-list Dario candidate, or Jose/Juana relationship clusters.
