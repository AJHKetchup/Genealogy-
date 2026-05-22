---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522105106563
task_id: proof-review:research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
staged_draft: research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
relationship_type: child_parent
child_claimed: Isolina del Carmen Jose
parents_claimed:
  - Jose del Carmen Pulgar
  - Juana de Dios Amador de Pulgar
source_quality_score: 0.90
conversion_confidence_score: 0.35
evidence_quantity_score: 0.45
agreement_score: 0.20
identity_confidence_score: 0.20
claim_probability: 0.25
relevance_level: high
relevance_confidence: 0.65
canonical_readiness: hold
---

# Proof Review: REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents

## Blockers

- The exact staged relationship, `Isolina del Carmen Jose` as child of `Jose del Carmen Pulgar` and `Juana de Dios Amador de Pulgar`, is not literally supported by the available verification set.
- The draft's referenced chunk path, `page-0001-chunk-01.md`, is unavailable. The same chunk directory contains `page-0172-chunk-01.md`, but that available chunk has a different chunk id (`CHUNK-4127185dc97c-P0172-01`) and should not be silently substituted for promotion.
- The staged draft's literal support says `Nombre. Isolina del Carmen Jose`, but the reviewed converted file and available chunk transcribe entry 513 as `Isidoro del Carmen Diaz`, male. This conflicts with the staged child identity.
- The source packet records an image-QA conflict for entry 513, noting the image appears closer to a child name beginning with `Pulgar` and a masculine sex, not the staged `Isolina del Carmen Jose`.
- Direct image review confirms that entry 513 is a civil birth registration and that the parent column visibly supports `Jose del Carmen Pulgar` and `Juana de Dios Amador`/`de Pulgar` at high confidence, but the child name is not visibly `Isolina del Carmen Jose`. The visible child field appears masculine and difficult, with a surname/name structure closer to the source-packet QA note than to the staged claim.

## Evidence Strengths

- Source quality is strong: the source is a contemporaneous civil birth register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, entry 513.
- The parent fields are the strongest part of the evidence. The image and derivative transcription both support father `Jose del Carmen Pulgar`; the mother field supports `Juana de Dios Amador`, with the image also showing a following `de Pulgar` reading.
- The entry's sex field is visibly masculine, which helps identify a major conflict with the staged female-appearing child name.
- The source packet appropriately flags the conversion/transcription conflict and already recommends holding for conversion QA.

## Scored Judgment

- `source_quality_score`: 0.90. A civil birth register is a high-quality primary source for child-parent relationships.
- `conversion_confidence_score`: 0.35. The conversion, staged draft, source packet QA, and image do not agree on the child name for entry 513.
- `evidence_quantity_score`: 0.45. There is one directly relevant register entry, but the asserted child identity is unstable.
- `agreement_score`: 0.20. Parent names largely agree, but the child name and chunk identity/path materially conflict.
- `identity_confidence_score`: 0.20. The claimed child identity `Isolina del Carmen Jose` is not established from the reviewed materials.
- `claim_probability`: 0.25. The record likely supports a child-parent event involving Jose del Carmen Pulgar and Juana de Dios Amador, but not the staged child identity as written.
- `relevance_level`: high. The source is directly relevant to a child-parent relationship if the entry is correctly transcribed.
- `relevance_confidence`: 0.65. Relevance is high, but confidence is reduced by the unresolved child-name and chunk-reference conflicts.
- `canonical_readiness`: hold. Do not promote until conversion QA reconciles the child name, sex, chunk id/path, and source-packet/draft mismatch.

## Next Action

Hold this relationship candidate for conversion QA. Ask QA to reconcile entry 513 directly against the page image, especially the child field and sex field, and to repair the stale chunk reference before any proof promotion. The parent fields may be reused only after the child identity is re-established from the visible source or a corrected, reviewed conversion.
