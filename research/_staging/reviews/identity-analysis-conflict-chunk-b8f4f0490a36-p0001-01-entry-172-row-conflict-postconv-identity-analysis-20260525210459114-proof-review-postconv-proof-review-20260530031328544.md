---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530031328544
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-postconv-identity-analysis-20260525210459114.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-postconv-identity-analysis-20260525210459114.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conflict

## Blockers First

1. Keep this item on hold. The assigned chunk and assigned converted Markdown disagree materially for entry 172: the chunk gives `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the converted Markdown gives `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
2. The referenced source image path and the manifest page-image path were not available on disk during this review. Because direct visual verification could not be completed, this review cannot certify the controlling row or father-field reading.
3. Do not promote any child identity, birth event, parent-child relationship, parent merge, same-person merge, or Dario-line bridge from this draft. The disagreement changes the child, parents, birth date/place, informant, and family line.
4. The father field remains unresolved. The next QA pass must decide whether the visible source supports `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
5. No reviewed text in this task names Dario, Arturo, Smith, Dario Jose, or Dario Pulgar Arriagada. Any bridge from this entry to those identity clusters remains unsupported.

## Evidence Strengths

- The staged identity-analysis draft correctly treats the problem as a row-level conversion conflict rather than a name variant or duplicate-person problem.
- The source packet and conflict draft both flag the same blocker and recommend `hold_for_conversion_qa`.
- The chunk is internally coherent for a Pulgar/Arriagada civil birth row on page 58, entry 172, including registration date, child name, birth details, parents, residence, and informant.
- The converted Markdown is also internally coherent, but it is incompatible with the chunk for the same entry number. This confirms the need for targeted conversion QA before any canonical use.
- Civil birth registration would be a high-quality source type if the controlling row were visually certified.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the underlying civil birth register type; 5/10 usable in this task because the image was unavailable for direct review |
| conversion_confidence_score | 3/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 across assigned chunk and assigned converted Markdown; 7/10 among staged draft, source packet, conflict draft, and chunk for the existence of a Pulgar/Arriagada hypothesis |
| identity_confidence_score | 6/10 for the Pulgar/Arriagada row as a staged hypothesis; 2/10 for any canonical identity conclusion; 0.5/10 for any Dario-line bridge from this item |
| claim_probability | 0.68 that the staged Pulgar/Arriagada reading is the intended row needing QA; 0.15 that the Burgos/de la Cruz reading controls this assigned source; 0.05 or lower for same-person/relationship claims beyond the stated row |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold analysis. Its central warning is correct: derivative files assigned to the same entry number conflict in ways that would attach the wrong child and parents if promoted prematurely.

This review does not certify the literal source reading because the referenced image files were unavailable. The safest proof judgment is therefore not to revise names or relationships, but to preserve the conflict and require targeted conversion QA against the visible source.

## Next Action

Run targeted conversion QA for register page 58, entry 172 using the source image or recovered page image. QA should identify the controlling row, explain why the converted Markdown and chunk diverged, and certify the father-field reading. After that, rerun proof review before any canonical claim, relationship, identity merge, or Dario-line comparison is promoted.
