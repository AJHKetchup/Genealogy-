---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260525190042006
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. Do not promote any child identity, parent-child relationship, parent-pair clue, Dario-line comparison, or Jose/Juana merge from this staged draft yet.
- The assigned converted file and the assigned chunk do not agree on entry 172. The chunk and source packet record `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`; the converted file currently records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- The staged identity-analysis draft repeats an earlier derivative-conflict wording that says the converted file records `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`. That exact wording is not supported by the converted file currently present in this workspace. The larger row-level conflict remains real, but the review should not preserve the unsupported Gomez/de la Cruz wording as a literal finding.
- The visible page image supports the Pulgar/Arriagada row for register entry 172 more strongly than the converted file does, but this proof-review task should not rewrite the conversion. A targeted conversion QA note should reconcile or supersede the stale/mismatched converted Markdown and chunk lineage.
- The father-name ending after `Pulgar` remains uncertain enough for canonical use. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` as QA alternatives unless a later source-image QA note certifies the visible reading.

## Evidence Strengths

- The source image, chunk, conflict draft, and source packet all point to entry 172 on page 58 as a Pulgar/Arriagada birth registration, not as a Dario-line identity event.
- The chunk gives a coherent civil birth registration: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`.
- A civil birth register is a high-reliability source type for birth, parent, and registration facts when the row assignment and transcription are stable.
- The staged identity analysis correctly rejects any direct bridge from this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. No such person is named in the entry.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration birth record with a visible source image is strong in principle. |
| conversion_confidence_score | 0.42 | Source image and chunk align on the Pulgar/Arriagada row, but the converted file in the assigned chain describes a different entry 172. |
| evidence_quantity_score | 0.62 | One direct register entry plus derivative chunk/source-packet support; no independent corroborating source for identity linkage. |
| agreement_score | 0.48 | Chunk, source packet, conflict draft, and visible image broadly agree; converted Markdown and some staged conflict wording disagree. |
| identity_confidence_score | 0.67 | Moderate confidence for the child-parent cluster within this row only; low confidence for any broader person merge. |
| claim_probability | 0.74 | Probable that the visible entry 172 is the Pulgar/Arriagada birth row, but not ready for canonical claim creation until conversion QA resolves the file-chain conflict. |
| relevance_level | 0.86 | Highly relevant to Pulgar/Arriagada parent-candidate work if QA confirms the row. |
| relevance_confidence | 0.80 | The surnames and parent-child structure are visibly relevant; relevance to Dario-specific identities is not established. |
| canonical_readiness | 0.12 | Hold for conversion QA, then rerun proof review before promotion. |

## Proof Judgment

The staged draft's main conclusion is sound: this is a row-level conversion/file-assignment conflict, not a minor spelling variant or a safe identity merge. The draft is too permissive only where it treats the earlier `Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz` wording as the current converted-file text. The current converted file instead says `Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz`. Either way, it conflicts materially with the chunk and with the visible source image for the Pulgar/Arriagada row.

Current proof status: `hold_for_conversion_qa`. The Pulgar/Arriagada reading is likely enough to preserve as staged evidence, but not enough to promote while the conversion chain contains contradictory derivative text.

## Next Action

Run targeted conversion QA against the source image, converted Markdown, chunk, and source packet. The QA note should explicitly state the controlling reading for entry 172 and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical claim, relationship, parent merge, or Dario-line comparison is promoted.
