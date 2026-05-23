---
type: proof_review
role: claim_reviewer
status: complete
worker: postconv-proof-review-20260523144712217
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_at: 2026-05-23
source_quality_score: 0.86
conversion_confidence_score: 0.64
evidence_quantity_score: 0.68
agreement_score: 0.58
identity_confidence_score: 0.46
claim_probability: 0.90
relevance_level: critical
relevance_confidence: 0.97
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Page 172 Identity Candidates

## Blockers

- Canonical readiness is **hold_for_conversion_qa**. Page 172 and entries 513-515 are relevant, but the staged identity draft is not reliable enough for canonical person, relationship, duplicate, or Dario/Pulgar-line promotion.
- The staged draft contains stale file-availability statements. It reports the referenced `page-0172-chunk-01.md` as missing and an alternate `page-0001-chunk-01.md` as available. In this rerun, `page-0172-chunk-01.md` exists and `page-0001-chunk-01.md` is absent.
- Metadata remains inconsistent. The source packet and staged draft cite `CHUNK-4127185dc97c-P0172-01`; the restored chunk currently identifies itself as `CHUNK-d6a12b291d94-P0172-01`. The source packet also cites converted sha `4127185dc97c...`, while the restored chunk cites converted sha `d6a12b291d94...`; the current converted-file hash checked in this review is `E17DA442A810171D5D0C72B49EEA0DF0D94E9DB2987AF8786BDD52E958708C31`.
- The staged draft's literal-support section is stale against the restored converted file/chunk and visible page image. It says entry 513 is `Isidoro del Carmen Diaz`; the restored conversion/chunk read `Tulio Cesar Luis Jose`, father/declarant `Jose del Carmen Pulgar`, and mother `Juana de Dios Amagada de Pulgar`. The source image visibly supports a Pulgar-row reading, but some child-name and maternal-surname letters still warrant field-level QA.
- Entry 514 has a material father-field risk. The restored conversion/chunk read child `Rigoberto Juan Bautista`, mother/declarant `Mercedes Riquelme`, and father `Belisario Riquelme`; the visible image is compatible with the source packet's caution that the father field may be closer to `se ignora`. Do not promote a father relationship from this draft.
- Entry 515 has a material surname/parentage risk. The restored conversion/chunk read father/declarant `Pedro Pablo Leiva` and mother `Carmen Fuentes`; the visible image appears closer to a `Neira` surname in the father/declarant area. Do not promote a Leiva or Neira identity from this draft until conversion QA settles the row.
- The Dario/Pulgar comparison remains only an anti-conflation guardrail. The reviewed page does not name Dario or Arturo and does not prove a bridge to `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.

## Evidence Strengths

- The source image is a direct civil birth-register page. It visibly supports page `172`, year `1889`, the Los Anjeles/La Laja heading, and entries `513`, `514`, and `515`.
- The restored converted file and restored chunk now agree with each other on the main table transcription, so the previous missing-chunk blocker has been partly resolved.
- The staged draft's central judgment, `hold_for_conversion_qa`, is supported. The remaining conflicts concern proof readiness and identity risk, not whether the page belongs in the evidence set.
- Some narrow row participants are plausible at source level: entry 513 father/declarant appears to be `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, and entry 514 mother/declarant appears to be `Mercedes Riquelme`. These should remain row-level candidates, not canonical merges.

## Scores

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil registration image is direct evidence for the entries; scan contrast and handwriting still limit some fields. |
| conversion_confidence_score | 0.64 | Restored conversion and chunk agree, but source-packet cautions and visible image review leave material name/surname/father-field risks. |
| evidence_quantity_score | 0.68 | Reviewed the assigned staged draft, source packet, converted file, restored chunk, and page image; no external corroborating sources were used. |
| agreement_score | 0.58 | Strong agreement on page identity and some participants; disagreement remains between staged draft, metadata, source-packet cautions, and visible image readings. |
| identity_confidence_score | 0.46 | Page/entry identity is strong; exact person identities and relationships for entries 513-515 remain unsettled. |
| claim_probability | 0.90 | The claim that this draft should remain on hold for conversion QA is highly probable. |
| relevance_level | critical | The unresolved fields affect identity creation, relationship promotion, and possible conflation with Pulgar-line candidates. |
| relevance_confidence | 0.97 | The reviewed files and image are the exact assigned page-172 evidence set. |
| canonical_readiness | hold_for_conversion_qa | Resolve chunk/checksum drift and field-level transcription conflicts before promotion. |

## Judgment

The staged identity draft is supportable as a hold/risk note, not as proof of the named people. The restored page-172 chunk removes the earlier missing-file condition, but it also shows the staged draft is stale and must be revised or superseded before any canonical use.

Claim probability is high only for the procedural claim: keep this identity analysis on **hold_for_conversion_qa**. Probability is lower for any specific identity or relationship claim, especially entry 514 father identity and entry 515 Leiva/Neira surname.

## Next Action

Revise or supersede the staged draft to match the restored chunk and current metadata, then run targeted field-level conversion QA against the source image for entry 513 child name and maternal surname, entry 514 father field, and entry 515 father/declarant surname. After those readings are settled, review separate atomic claims before any canonical person or relationship promotion.
