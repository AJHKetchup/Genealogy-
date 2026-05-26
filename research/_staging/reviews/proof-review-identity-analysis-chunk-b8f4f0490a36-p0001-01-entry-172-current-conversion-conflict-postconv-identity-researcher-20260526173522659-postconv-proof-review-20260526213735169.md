---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526213735169
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173522659.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173522659.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-26
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers

1. Canonical readiness is blocked by a material row-level conversion conflict. The assigned chunk and local page image support entry `172` as the Pulgar/Arriagada row, while the current converted Markdown records entry `172` as a Burgos/de la Cruz row.
2. The two readings are not same-person variants. They conflict on child name, birth date/time/place, father, mother, informant, and official/register context.
3. The father field in the Pulgar/Arriagada reading remains below proof-review precision. The chunk gives `Jose del Carmen Pulgar S.`, while the source packet preserves the trailing letter or mark as unresolved.
4. No relationship, duplicate-person, merge, or Dario-line bridge should be promoted from this staged draft. It cannot safely attach entry `172` to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or the existing Jose/Juana parent stubs without targeted conversion QA.

## Evidence Strengths

- The staged draft accurately identifies the controlling issue as a row-control conflict rather than a normal identity-variant problem.
- The assigned chunk gives a complete Pulgar/Arriagada row for entry `172`: `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 about 3 p.m. at Calle de Valdivia, with father transcribed as `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet independently preserves the same Pulgar/Arriagada evidence and explicitly reports direct image review, while holding the father-field suffix as unresolved.
- Local page image inspection supports the staged draft's high-level conclusion that entry `172` is visually aligned with the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the current converted Markdown.
- The current converted Markdown is still relevant evidence because it is the assigned converted file, but its row content is incompatible with the chunk and page image for this task.

## Scored Judgment

| Metric | Score / level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a strong direct source, but review is constrained by derivative disagreement and no new transcription correction may be made here. |
| conversion_confidence_score | 0.34 | The assigned chunk and image agree at a row level, but the current converted Markdown records a different entry `172`, making the conversion package unreliable until QA resolves row control. |
| evidence_quantity_score | 0.70 | Review used staged draft, chunk, converted Markdown, source packet, conflict note, and page image; enough to score the conflict, not enough to promote claims. |
| agreement_score | 0.38 | Chunk, source packet, conflict note, and image agree broadly with Pulgar/Arriagada; converted Markdown materially disagrees. |
| identity_confidence_score | 0.61 | Pulgar/Arriagada identity is probable if the chunk/image controls, but identity proof remains held by the conversion conflict and father-field uncertainty. |
| claim_probability | 0.63 | The claim that entry `172` is the Pulgar/Arriagada birth registration is more likely than the converted Markdown reading in this verification context, but not promotion-ready. |
| relevance_level | high | The record directly affects Pulgar/Arriagada child and parent candidates and anti-conflation review for Dario-line clusters. |
| relevance_confidence | 0.88 | Pulgar and Arriagada terms are explicit in the chunk/source packet and visible row context; relevance is strong even though identity conclusions are held. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until targeted conversion QA certifies the controlling row and father-field reading. |

## Literal Support And Limits

- Supported for review context: assigned chunk/source packet/page image alignment favors a Pulgar/Arriagada entry `172`.
- Supported only with uncertainty: father field may be `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`; proof review should not select one beyond visible support without QA.
- Not supported: any claim that the Pulgar/Arriagada child is Dario, Arturo, Smith-linked, or the same person as a later `Darío Pulgar Arriagada` candidate.
- Not supported: reconciling `Jose Miguel` Burgos/de la Cruz with `Jose del Carmen Segundo Pulgar Arriagada` as one identity.

## Next Action

Run targeted conversion QA against the source image, assigned chunk, current converted Markdown, source packet, and conflict note. The QA output should decide which row controls entry `172` and certify the father field only to the visible extent. After that, rerun proof review before any canonical claim, relationship, merge, duplicate-person decision, or wiki update.
