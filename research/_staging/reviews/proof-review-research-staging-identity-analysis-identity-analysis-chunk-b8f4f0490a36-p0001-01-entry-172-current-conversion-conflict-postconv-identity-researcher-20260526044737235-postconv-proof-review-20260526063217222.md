---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526063217222
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044737235.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044737235.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: blocked
review_decision: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged draft is materially supported as a conflict analysis, but the underlying conversion state remains unresolved: the referenced chunk transcribes entry 172 as a Pulgar/Arriagada birth row, while the referenced converted Markdown transcribes entry 172 as a Burgos/de la Cruz row.
2. The current converted Markdown cannot support the Pulgar/Arriagada child, parent, birth-date, birthplace, informant, or relationship claims. Those claims are supported by the chunk and visible source image, not by the current converted file.
3. This proof review is not a source-transcription correction pass. The visible image appears to support the Pulgar/Arriagada row at entry 172, but targeted conversion QA still needs to retire or supersede the mismatched converted Markdown and certify the father-field reading.
4. The father name/suffix remains a transcription-risk point. Do not promote `Jose del Carmen Pulgar S.` as certain, merge it into `Jose del Carmen Pulgar`, or normalize it to another person without QA certification.
5. No Dario-line bridge, same-person merge, duplicate-person merge, parent merge, or canonical relationship promotion is ready from this staged draft.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044737235.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source is a civil birth register image with a visible table row for entry 172, so the source type is strong for birth, parent-name, registration-date, and informant facts once the transcription layer is reconciled.
- The chunk and source packet agree on the Pulgar/Arriagada reading for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth on 1888-03-08 at about 3 p.m., place `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- Direct image inspection in this review supports the broad Pulgar/Arriagada row assignment for entry 172 and does not support the Burgos/de la Cruz row at that visible position.
- The staged draft correctly treats existing same-cluster wiki pages as context rather than independent corroboration.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil registration image is a strong original-source class for the facts at issue, though image readability and table alignment still require careful QA. |
| conversion_confidence_score | 0.32 | The chunk and visible image align broadly, but the current converted Markdown gives a different row for the same entry number. |
| evidence_quantity_score | 0.48 | One source image plus two derivative transcription layers; useful but not enough to resolve the row-control conflict without QA. |
| agreement_score | 0.42 | Chunk/source packet/image agree broadly with each other, but the referenced converted Markdown conflicts on every identity-bearing field. |
| identity_confidence_score | 0.60 | Pulgar/Arriagada is the better-supported visible-row hypothesis, but the conversion conflict blocks proof-ready identity confidence. |
| claim_probability | 0.64 | The staged draft's hold-for-QA conclusion is probable and well supported; individual canonical facts remain below promotion threshold. |
| relevance_level | high | Directly relevant to Jose/Juana/Pulgar/Arriagada identity and relationship candidates; only anti-conflation context for Dario identities. |
| relevance_confidence | 0.88 | The names and row context make the Pulgar/Arriagada relevance clear, while Dario relevance is indirect and low. |
| canonical_readiness | blocked | Conversion QA must resolve the controlling row and father-field reading before canonical promotion. |

## Claim And Identity Risk

- Literal support: the staged draft accurately reports that the chunk and converted Markdown conflict. The page image supports the chunk's broad Pulgar/Arriagada placement for visible entry 172, but the current converted file does not.
- Uncertainty: father-field suffix and exact transcription remain unresolved; this review should not convert visual impressions into canonical wording.
- Source reliability: high source class, low current conversion reliability because derivative outputs disagree.
- Relationship jumps: parent-child and spouse/parent-candidate relationships are plausible only if QA confirms the Pulgar/Arriagada row; they are not ready for promotion.
- Identity risk: high if the Pulgar row is merged into existing Jose/Juana pages or any Dario-line identity by name proximity alone.
- Conflict severity: high because the competing rows imply different children, parents, dates, places, and informants.

## Next Action

Hold for targeted conversion QA. The next worker should reconcile the page image, chunk, source packet, and current converted Markdown for `CHUNK-b8f4f0490a36-P0001-01`, decide the controlling entry-172 row, and certify the father field only to the visible extent. After that, rerun proof review for child identity, birth facts, father claim, mother claim, and parent-child relationships before any canonical promotion.
