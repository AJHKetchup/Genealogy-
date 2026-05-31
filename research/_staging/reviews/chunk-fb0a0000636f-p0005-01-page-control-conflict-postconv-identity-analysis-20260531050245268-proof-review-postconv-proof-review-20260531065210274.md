---
type: proof_review_note
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531065210274
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531050245268.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531050245268.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
review_decision: hold
source_quality_score: 0.25
conversion_confidence_score: 0.15
evidence_quantity_score: 0.25
agreement_score: 0.10
identity_confidence_score: 0.20
claim_probability: 0.25
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: blocked
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers First

1. The staged draft is correct to block canonical promotion: page 5 has unresolved page-control conflict between the conversion-job page Markdown and the assigned chunk.
2. The controlling source image/PDF could not be verified. `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent, the manifest's staged PDF copy is absent, and the manifest's `page-images/page-0005.jpg` is absent.
3. The derivative texts disagree materially. `page-markdown/page-0005.md` gives 1999-1997 consulting entries, while `page-0005-chunk-01.md` gives 1979-1970 work-history entries ending at `EDUCATION`.
4. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts and hashes for the same chunk path, so the chunk identity and content version are not stable enough for proof reliance.
5. The page body, in either derivative version, does not literally name Dario Arturo Pulgar or any proposed canonical identity variant. Attachment to a person rests only on document title/path continuity.
6. No same-person merge, name-variant normalization, parent/child/spouse relationship, or chronology claim is supportable for canonical use from this page until conversion QA certifies the controlling page and an identity-bearing bridge is reviewed.

## Evidence Strengths

- The converted aggregate file title and metadata consistently identify the document set as `CV of Dario Arturo Pulgar pages 4-9`, with source path `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The reviewed staged conflict draft accurately reports the central conflict between a 1999-1997 page-5 reading and a 1979-1970 page-5 reading.
- The reviewed chunk manifest independently supports the metadata-instability concern by listing duplicate `CHUNK-fb0a0000636f-P0005-01` entries with different `chars` and `sha256` values.
- The conflict is highly relevant to identity and chronology work because either derivative page could produce plausible CV work-history claims, but the current evidence cannot decide which page text controls.

## Scored Judgment

- `source_quality_score`: 0.25. The named source is a relevant CV, but the local raw PDF, staged PDF copy, and rendered page image are unavailable for this review.
- `conversion_confidence_score`: 0.15. Two derivative transcriptions conflict and the controlling image is missing.
- `evidence_quantity_score`: 0.25. There is enough derivative evidence to identify a conflict, but not enough primary/visual evidence to resolve it.
- `agreement_score`: 0.10. The page-level derivatives disagree on the basic contents of page 5.
- `identity_confidence_score`: 0.20. Document title/path continuity points toward Dario Arturo Pulgar, but neither derivative page body names the subject.
- `claim_probability`: 0.25. The claim that page-5 work history can be attached to the CV subject is plausible but unproved while page control is unresolved.
- `relevance_level`: high.
- `relevance_confidence`: 0.90.
- `canonical_readiness`: blocked.

## Review Finding

The staged draft's hold recommendation is supported. Its uncertainty language is appropriate and should not be strengthened into a transcription correction or identity conclusion. The only verified conclusion is that page-5 evidence is conflicted and cannot support canonical work-history, identity-merge, name-variant, or relationship claims at this time.

## Next Action

Hold this staged draft for conversion QA. Restore or regenerate an authoritative page-5 image or source PDF, compare it against both derivative readings, repair the duplicated chunk manifest/hash drift, and then rerun proof review on the certified page-5 transcription before any canonical promotion.
