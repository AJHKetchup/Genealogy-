---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530031113011
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205450696.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205450696.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
qa_note: "research/_staging/tasks/conversion-review-note-chunk-b8f4f0490a36-p0001-01-entry-172-image-reread.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict

This review checks the staged draft named above against the referenced source packet, chunk, converted Markdown, and conversion review note. No external research was performed.

## Blockers First

1. Keep this item on `hold_for_conversion_qa`. The assigned chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, while the current converted Markdown reads entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. That is a row-level or assignment-level conflict, not a spelling variant.
2. The source image could not be independently inspected in this proof review. The source path recorded in the packet and manifest was not found locally, and the conversion job folder contains no page image file. Therefore this review can validate agreement and conflict among local derivative files, but cannot certify the visible handwriting.
3. Do not promote child identity, birth facts, parent claims, child-parent relationships, parent-pair clues, or Dario-line identity bridges from this staged draft. The controlling row remains unresolved.
4. Do not normalize the father field to `Jose del Carmen Pulgar S.` or to `Jose del Carmen Pulgar` as a canonical fact. The chunk gives `Jose del Carmen Pulgar S.`, while the QA note says the final `S.` is not clearly visible on image reread.
5. Do not merge or bridge any Dario/Pulgar identities from this item. The Pulgar/Arriagada derivative reading does not name Dario, Arturo, Smith, spouse, child, adult residence, passenger data, or any later-life bridge.

## Evidence Strengths

- The source packet accurately preserves the conflict and recommends `hold_for_conversion_qa`.
- The chunk and source packet agree with each other on a Pulgar/Arriagada entry: child `Jose del Carmen Segundo Pulgar Arriagada`, registration date 7 April 1888, birth date/time 8 March 1888 at 3 p.m., birthplace Calle de Valdivia, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The converted Markdown clearly conflicts with that reading by assigning entry 172 to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth date/time 6 April 1888 at 10 p.m., and place `En esta`.
- The prior conversion review note supports the Pulgar/Arriagada child and mother reading while explicitly preserving uncertainty over the father suffix after `Pulgar`.
- The staged draft correctly treats the issue as a scored conflict and blocks canonical promotion.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 7/10 for the civil birth register as a source type; reduced here because this reviewer could not inspect the source image locally |
| conversion_confidence_score | 3/10 because the converted Markdown and assigned chunk disagree at row level |
| evidence_quantity_score | 4/10 because there is one relevant source event plus multiple derivative notes, but no independent image check in this review |
| agreement_score | 3/10 overall; chunk, source packet, and QA note favor the Pulgar/Arriagada reading, but the current converted Markdown materially disagrees |
| identity_confidence_score | 5.5/10 for the narrow proposition that the intended family-relevant row is Pulgar/Arriagada; 1/10 or lower for any Dario identity bridge |
| claim_probability | 0.60 for the Pulgar/Arriagada row controlling entry 172; 0.25 for the Burgos/de la Cruz converted-row reading controlling; 0.05 for any Dario bridge from this item |
| relevance_level | high for Pulgar/Arriagada parent research; low for Dario identity resolution |
| relevance_confidence | 0.80 for Pulgar/Arriagada relevance if the chunk/QA reading controls; 0.15 for Dario-line relevance |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold. Its central blocker is real: the local derivative files do not agree on which row is entry 172. The prior QA note helps explain why the Pulgar/Arriagada reading is plausible, but this proof review cannot independently certify the handwriting because the referenced image is unavailable at the recorded path.

The staged draft is also right to reject relationship jumps and identity merges. Even if the Pulgar/Arriagada row is later certified, this source would support only a birth registration and named parents for the child in that row. It would not by itself connect the record to any Dario Arturo, Dario Jose, Smith, or passenger-list candidate.

## Next Action

Run targeted conversion QA with access to the actual page image. The QA should decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and should certify the father field only as the visible source supports it: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before staging or promoting any child, parent, relationship, or identity-bridge claim.
