---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526215206449
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173959405.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173959405.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md
conflict_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
referenced_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.86
conversion_confidence_score: 0.34
evidence_quantity_score: 0.72
agreement_score: 0.48
identity_confidence_score: 0.56
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.98
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- The exact staged draft reviewed is `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173959405.md`.
- Canonical readiness is `hold_for_conversion_qa`. The current converted Markdown and the referenced chunk disagree on the controlling row for entry `172`.
- The converted file records entry `172` as a Burgos/de la Cruz row for child `José Miguel`, born 6 April 1888, with father/informant `Oswaldo Burgos` and mother `Concepcion de la Cruz`.
- The referenced chunk and source packet record entry `172` as a Pulgar/Arriagada row for child `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- This conflict changes every identity-bearing field: child name, birth date/time/place, father, mother, informant, and relationship candidates. Treat dependent claims as hold/revise, not as promotable evidence.
- The father field is not proof-certified beyond the visible-name problem already flagged by the source packet. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as unresolved variants until targeted conversion QA records the visible reading.
- No Dario, Arturo, Smith, spouse, descendant, or lineage bridge appears in the reviewed entry materials. Do not attach this draft to any Dario/Pulgar canonical identity by surname context alone.

## Evidence Strengths

- The source type is strong: an 1888 Los Angeles/La Laja civil birth register page, normally high value for birth, parent, informant, and residence claims once row control is settled.
- The staged draft accurately preserves the material row-level conflict and recommends hold rather than promotion.
- The referenced chunk, source packet, and conflict draft agree with each other on the Pulgar/Arriagada reading for entry `172`.
- The current converted Markdown is available and directly demonstrates the competing Burgos/de la Cruz reading, so the conflict is specific and verifiable rather than speculative.
- The staged draft appropriately treats existing wiki pages and same-surname clusters as context only, not as independent proof.

## Scored Judgment

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil birth-registration source image is a high-quality source type for identity and relationship facts, but the review depends on derivative row readings until targeted image QA settles the conflict. |
| conversion_confidence_score | 0.34 | Conversion confidence is low because the current converted Markdown and the assigned chunk give mutually exclusive entry-172 rows. |
| evidence_quantity_score | 0.72 | The staged draft, conflict draft, source packet, chunk, and converted file are all available; the quantity is enough to identify the problem but not to resolve it canonically. |
| agreement_score | 0.48 | The chunk/source-packet/conflict layer agrees internally, but the current converted file disagrees on all core identity fields. |
| identity_confidence_score | 0.56 | The Pulgar/Arriagada identity hypothesis is better supported by the assigned chunk/source packet, but row-control and father-field uncertainty prevent proof-level identity confidence. |
| claim_probability | 0.62 | Probable that the Pulgar/Arriagada row is the intended staged claim layer, but not ready as a canonical birth or parent-child claim until conversion QA certifies the controlling row. |
| relevance_level | high | The reviewed materials directly concern the assigned staged identity-analysis draft and entry-172 conflict. |
| relevance_confidence | 0.98 | All checked local files reference the same chunk id, source image, converted file, and entry number. |
| canonical_readiness | hold_for_conversion_qa | Do not promote any identity, event, relationship, merge, or canonical page update from this draft. |

## Claim Review

- Entry `172` as a Pulgar/Arriagada birth registration: hold. The chunk and source packet give direct support, but the current converted file gives a different row for the same entry number. Claim probability: 0.62.
- Child identity `Jose del Carmen Segundo Pulgar Arriagada`: hold. Supported by the referenced chunk/source packet, contradicted by the converted file's `José Miguel` reading. Claim probability: 0.60.
- Father identity `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.`: hold_for_field_qa. The base name is supported in the chunk/source packet, but the trailing `S.` or mark is not certified. Claim probability: 0.54.
- Mother identity `Juana Arriagada de Pulgar`: hold. Supported by the Pulgar/Arriagada layer, but dependent on row-control certification. Claim probability: 0.58.
- Burgos/de la Cruz row as controlling entry `172`: hold/revise. It is present in the current converted file, but contradicted by the assigned chunk/source packet and conflict draft. Claim probability: 0.30.
- Dario/Pulgar bridge or canonical identity merge: unsupported. The reviewed entry materials do not name or directly connect a Dario/Arturo/Smith identity. Claim probability: 0.03.

## Next Action

Run targeted conversion QA against the source image, referenced chunk, current converted Markdown, source packet, and conflict draft. The QA note should decide which row controls entry `172` and certify the father-field reading only to the visible extent. After that, rerun proof review before promoting any child identity, birth fact, parent-child relationship, same-person decision, merge, or wiki-page attachment.
