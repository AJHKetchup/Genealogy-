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
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-child-name-sex-postconv-proof-review-20260522063230567.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-child-name-sex.md` | `hold` | Keep this claim on hold for conversion QA. Reconcile entry 513's child-name field against the source image and corrected transcription, then rerun proof review or revise the staged claim before any canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-father-name-postconv-proof-review-20260522063401351.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-father-name.md` | `hold` | Keep this claim on hold for conversion QA. Reconcile entry 513 in the assembled converted Markdown against the source image and assigned chunk, then rerun proof review or revise the staged claim before canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-mother-name-postconv-proof-review-20260522064750997.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-mother-name.md` | `hold` | Keep this claim on hold for conversion QA. Reconcile entry 513's full transcription against the source image, preserve the mother name as a literal register reading, and rerun proof review or revise the staged claim before canonical promotion. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-513-registration-date-postconv-proof-review-20260522064922812.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-513-registration-date.md` | `hold` | Resolve or formally annotate the chunk-versus-converted-file conflicts for entry 513, then promote this date claim with the literal wording preserved as source support. No change to the source transcription is recommended from this review. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-514-birth-date-place-postconv-proof-review-20260522065232478.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-514-birth-date-place.md` | `hold` | Keep this claim on hold for a targeted image QA pass on entry 514's child name, birth date/time, and `Lugar` field. If QA confirms the assigned chunk reading, revise or promote later using the literal source-supported wording and preserve uncertainty on the unusual street spelling unless the visible source fully settles it. |
| `research/_staging/reviews/proof-review-research-staging-claims-claim-chunk-3d3ab761209f-p0001-01-514-child-name-sex-postconv-proof-review-20260522065407022.md` | `research/_staging/claims/claim-chunk-3d3ab761209f-p0001-01-514-child-name-sex.md` | `hold` | Keep this claim on hold for targeted image QA of entry 514's child-name field. If a crop or corrected transcription confirms `Aviles`, rerun proof review or revise the staged claim with that visible support. If `Aviles` remains unsupported, revise the claim subject/literal support to the source-visible name form before any canonical promotion. |

When revising, do not edit raw sources, converted Markdown, chunks, or page Markdown. Write new or updated staged drafts and/or conversion-review correction notes that preserve the disagreement between derivative transcripts and image-reviewed evidence. If the evidence remains blocked, keep `promotion_recommendation: hold_for_conversion_qa` and make the blocker explicit.


## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- Source packets must be Markdown files under `research/_staging/source-packets/` with YAML frontmatter including `type: source_packet`, `status: draft`, source identity fields, chunk/page references, and `promotion_recommendation`.
- Atomic claim drafts that may become canonical must be individual Markdown files under `research/_staging/claims/` with YAML frontmatter including `type: claim`, `claim_type`, `subject`, `predicate`, `object`, `source`, `source_packet`, `chunk`, `chunk_id`, `page_reference`, `confidence`, and `promotion_recommendation`. A grouped claim overview can be written as an extra note, but not instead of promotable atomic claim files.
- Relationship candidates that may become tree links must be individual Markdown files under `research/_staging/relationships/` with YAML frontmatter including `type: relationship_candidate`, `relationship_type`, `person_a`/`person_b` or `child`/`parents`, `source_packet`, `confidence`, and `promotion_recommendation`. If no relationship is stated, write a negative-evidence note with `promotion_recommendation: do_not_promote`.
- Use `promotion_recommendation: promote_after_review` only for drafts that can be promoted after proof review. Use `hold_for_conversion_qa`, `revise_before_review`, or `do_not_promote` for anything that should not flow to the tree yet.
- No canonical wiki pages are edited by this extraction task.
