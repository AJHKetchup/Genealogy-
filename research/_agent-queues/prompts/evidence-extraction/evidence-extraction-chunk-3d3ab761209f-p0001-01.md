# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md`
- Converted source: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk manifest: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/manifest.json`
- Original source: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Page range: 1-1
- Staging area: `research/_staging`


## Proof Review Revision Context

Previous proof review found staged outputs for this chunk were not yet promotion-ready. Use these notes as revision context, not as authority to alter source text.

| Review | Staged draft | Readiness | Requested follow-up |
| --- | --- | --- | --- |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-birth-date-time-postconv-proof-review-20260522062707498.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-birth-date-time.md` | `hold` | Keep this claim on hold for conversion QA. Reconcile the source image, assigned chunk, and assembled converted Markdown for entry 513, then rerun proof review or revise the staged claim from the corrected transcription before any canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-birth-place-postconv-proof-review-20260522063058226.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-birth-place.md` | `hold` | Keep this claim on hold until conversion QA reconciles entry 513 across the source image, assigned chunk, and assembled converted Markdown. After that QA pass, this birth-place claim can likely be promoted or revised with the same literal place spelling if the corrected entry still identifies the subject as Jose Luis Pulgar Amagada. |
| `research/_staging/reviews/proof-review-research-staging-conflicts-chunk-3d3ab761209f-p0001-01-conflict-candidates.md` | `research/_staging/conflicts/CHUNK-3d3ab761209f-P0001-01-conflict-candidates.md` | `hold` | Restore or regenerate the source/page image, then visually verify record 514's father field, witness surname, and street name; record 515's `Neira` emendation; and the bottom crop. After image review, promote only the verified negative-evidence conflict note and preserve unresolved readings as QA limitations. |
| `research/_staging/reviews/proof-review-research-staging-relationships-rel-chunk-3d3ab761209f-p0001-01-513-father-postconv-proof-review-20260522051431650.md` | `research/_staging/relationships/rel-chunk-3d3ab761209f-p0001-01-513-father.md` | `hold` | Run conversion QA on entry 513 against the source image, focusing on the child name/surname, mother's surname, birth date, and whether the child should be represented as `José Luis Pulgar Amagada` or revised to the visibly supported reading. After that QA pass, revise this staged relationship if the child identity changes; otherwise retain `José del Carmen Pulgar` as the father only with the reconciled child name. |
| `research/_staging/reviews/proof-review-research-staging-relationships-rel-chunk-3d3ab761209f-p0001-01-513-mother-postconv-proof-review-20260522051653641.md` | `research/_staging/relationships/rel-chunk-3d3ab761209f-p0001-01-513-mother.md` | `hold` | Run conversion QA on entry 513 against the source image, focusing on the child name/surname and the mother field reading `Amagada` versus `Amador`. After the transcription is reconciled, revise this staged relationship if either endpoint changes; otherwise retain the mother-child claim with the confirmed literal spelling. |
| `research/_staging/reviews/proof-review-research-staging-relationships-rel-chunk-3d3ab761209f-p0001-01-514-father-negative-evidence-postconv-proof-review-20260522051910359.md` | `research/_staging/relationships/rel-chunk-3d3ab761209f-p0001-01-514-father-negative-evidence.md` | `hold` | Route the conversion conflict for QA against the page image. After the converted file/chunk disagreement is resolved, keep the entry as negative evidence for no stated father and separately review any identity or parent-child claims for Mercedes Riquelme and Juan Bautista Riquelme Aviles before canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-relationships-rel-chunk-3d3ab761209f-p0001-01-514-mother-postconv-proof-review-20260522052043541.md` | `research/_staging/relationships/rel-chunk-3d3ab761209f-p0001-01-514-mother.md` | `hold` | Run conversion QA on entry 514 against the source image, focusing on the child name, father field, and street/place readings. After the transcription conflict is resolved, revise this staged relationship if the child endpoint changes; otherwise retain the mother-child claim with the confirmed literal spelling. |
| `research/_staging/reviews/proof-review-research-staging-relationships-rel-chunk-3d3ab761209f-p0001-01-515-father.md` | `research/_staging/relationships/rel-chunk-3d3ab761209f-p0001-01-515-father.md` | `hold_for_conversion_qa` | Reconcile the converted Markdown for entry 515 against the source image. After conversion QA, this relationship can be reconsidered for canonical promotion as a civil-register parent-child claim for `Laura de la Cruz Neira Ulloa` and `Pedro Pablo Neira`, preserving the `Neira=emendado= / vale=` note as source-context evidence. |

When revising, do not edit raw sources, converted Markdown, chunks, or page Markdown. Write new or updated staged drafts and/or conversion-review correction notes that preserve the disagreement between derivative transcripts and image-reviewed evidence. If the evidence remains blocked, keep `promotion_recommendation: hold_for_conversion_qa` and make the blocker explicit.


## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
