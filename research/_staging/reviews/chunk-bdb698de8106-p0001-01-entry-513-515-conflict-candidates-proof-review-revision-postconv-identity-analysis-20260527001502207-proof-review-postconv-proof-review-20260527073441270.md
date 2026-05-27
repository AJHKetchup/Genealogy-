---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527073441270
task_id: proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-analysis-20260527001502207.md
staged_draft: research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-analysis-20260527001502207.md
reviewed_claim_type: identity_conflict_analysis
reviewed_subject: "Entries 513 and 515, Los Angeles birth register, 1889"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_packet: "research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526232219797.md"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md"
chunk_id: CHUNK-bdb698de8106-P0001-01
source_page_image_checked: false
source_quality_score: 0.82
conversion_confidence_score: 0.30
evidence_quantity_score: 0.62
agreement_score: 0.55
identity_confidence_score: 0.40
claim_probability: 0.88
relevance_level: high
relevance_confidence: 0.98
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entries 513 And 515 Conflict Candidates

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The staged draft under review is `research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-analysis-20260527001502207.md`, and it correctly remains a conflict-analysis note rather than a promotable claim set.
- The converted file and chunk agree with each other, but the staged draft and source packet preserve prior image-review disagreement in identity-controlling fields. That disagreement prevents canonical promotion from the derivative text alone.
- Entry 513 cannot yet support a child identity, parent-child relationship, person merge, or lineage bridge. The held fields include the child name/sex, mother surname, and father/declarant profession.
- The literal derivative mother reading is `Juana de Dios Amador de Pulgar`, while the staged draft preserves an `Amagada`-style concern and warns against normalizing that concern into `Arriagada` without targeted crop-level QA.
- Entry 515 remains a row-boundary control item only. It does not provide Pulgar family evidence and should not be used to reconcile or promote Entry 513.
- This review did not perform external research and did not edit raw sources, converted Markdown, chunks, source packets, or canonical wiki pages.

## Evidence Strengths

- The source class is strong: a civil birth-register page for Los Angeles, La Laja, Chile, 1889, register page 172, entries 513-515.
- The referenced source packet is available and explicitly recommends `hold_for_conversion_qa`, matching the staged draft's conclusion.
- The converted file and assigned chunk are available and agree on the derivative transcription for Entry 513: child text `Isolina del Carmen / Jose`, sex `Masculino`, father `Jose del Carmen Pulgar`, mother `Juana de Dios Amador de Pulgar`, and declarant `Jose del C. Pulgar`, role `Padre`.
- The converted file and assigned chunk also agree on the derivative transcription for Entry 515: child `Rosa Elvira del Carmen` and father/declarant `Pedro Pablo Leiva`.
- The staged draft uses Dario/Pulgar-line comparisons as anti-conflation guardrails only. That treatment is appropriate because this draft does not name Dario, Arturo, Smith, Alexander John Heinz, or a direct bridge to those identities.

## Scored Judgment

- `source_quality_score: 0.82` - civil birth registration is a strong primary source class, reduced because this review verified the local derivative files and source packet, not a fresh paleographic reading from the image.
- `conversion_confidence_score: 0.30` - the derivative files agree with each other, but the staged draft and source packet report unresolved prior image-review conflicts in fields that control identity.
- `evidence_quantity_score: 0.62` - one staged identity analysis, one source packet, the converted file, and the chunk were reviewed; sufficient to evaluate the hold recommendation, insufficient to settle the row readings.
- `agreement_score: 0.55` - converted file, chunk, and source packet align on the literal derivative text, but agreement is materially lowered by preserved conflicts over the child name/sex, mother surname, profession, and Entry 515 boundary.
- `identity_confidence_score: 0.40` - confidence is moderate that Entry 513 is Pulgar-relevant at the row level, but exact child identity, mother identity, and relationship attachment remain below proof level.
- `claim_probability: 0.88` - the claim that the staged draft should remain held for conversion QA is strongly supported by the reviewed local files.
- `relevance_level: high`; `relevance_confidence: 0.98` - this review directly concerns the assigned staged draft and its Pulgar-relevant conflict candidates.
- `canonical_readiness: hold_for_conversion_qa`.

## Review Judgment

The staged identity analysis is supported as a conflict/hold note. The safest present conclusion is procedural: Entries 513 and 515 require targeted conversion QA before any atomic claim, relationship, merge, or canonical wiki update can be made.

Entry 513 may be Pulgar-relevant because the derivative row names `Jose del Carmen Pulgar` and `Jose del C. Pulgar`, but the child endpoint and mother surname are not reliable enough for promotion. Entry 515 should remain only a boundary check to prevent spillover into Entry 513.

## Next Action

Run targeted conversion QA against the source image for Entry 513 child name and sex, birth row fields, father/declarant name and profession, mother surname, and Entry 515 row boundary. After QA produces either a stable transcription or explicit uncertainty markers, rerun proof review on each atomic person and relationship claim before any canonical action.
