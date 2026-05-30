---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530070103602
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527025657315.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527025657315.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conflict

## Blockers First

1. Keep this item on hold. The assigned chunk and staged source packet support the Pulgar/Arriagada row for entry `172`, but the current converted Markdown and conversion job page Markdown support a materially different Burgos/de la Cruz entry `172`.
2. The source image referenced by the staged draft and manifest was not present in this checkout at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and the manifest's `page-images/page-0001.png` path was also absent. This review therefore cannot independently certify the visible row-control finding from image inspection.
3. Do not promote the father suffix `S.`. The chunk includes `Jose del Carmen Pulgar S.`, while the source packet and targeted QA note certify only `Jose del Carmen Pulgar` and explicitly leave the terminal mark unresolved.
4. Do not promote any same-person bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`. None of the checked local evidence for this entry names Dario, Arturo, or Smith.
5. Do not merge parent candidates from this row into other Jose/Juana stubs or variants. The checked evidence supports only a local candidate father named `Jose del Carmen Pulgar` and a local candidate mother named `Juana Arriagada de Pulgar`, with broader identity still unproved.

## Evidence Strengths

- The assigned chunk transcribes physical entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged source packet and targeted conversion QA note agree with the chunk's Pulgar/Arriagada row for the child, mother, dates, place, and informant, while limiting the father reading to `Jose del Carmen Pulgar`.
- The converted Markdown and conversion job page Markdown are internally consistent with each other for a different entry `172`: `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m.
- The staged identity analysis correctly treats this as a row-control/conversion conflict rather than a name variant or a promoted family relationship.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the underlying civil birth register type; 5/10 for this review because the image file was unavailable for direct inspection |
| conversion_confidence_score | 4/10 overall because the chunk/source-packet track and converted-file/page-markdown track materially disagree |
| evidence_quantity_score | 5/10 for one civil register row plus derivative review notes; insufficient for broader identity bridges |
| agreement_score | 4/10 overall; high agreement within the Pulgar/Arriagada staged packet/chunk track, high agreement within the Burgos/de la Cruz converted-file track, but low agreement between tracks |
| identity_confidence_score | 7/10 for a local Pulgar/Arriagada row candidate if the targeted image QA is accepted; 2/10 for any broader same-person or family bridge outside this row |
| claim_probability | 0.72 that the staged draft correctly identifies a serious row-control conflict; 0.60 that physical entry `172` is Pulgar/Arriagada pending direct image recheck; 0.10 or lower for Dario-related identity claims |
| relevance_level | high |
| relevance_confidence | 0.90 for Pulgar-line review risk; 0.20 for direct Dario identity relevance |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold-level proof review finding. It accurately describes a severe derivative conflict between the assigned chunk/source-packet interpretation and the current converted Markdown. Because the source image and page image were not available locally, this review does not independently validate the visual assertion that physical row `172` is the Pulgar/Arriagada row; it accepts that only as a staged QA assertion requiring conversion-control resolution or a focused image recheck.

The only claim that should survive this review is that entry `172` has a material row-level conflict requiring hold. No identity merge, relationship claim, Dario bridge, father suffix, or parent-candidate merge is canonically ready.

## Next Action

Hold for conversion QA. Reconcile or supersede the converted Markdown/page Markdown against the source image, preferably with a focused crop of entry `172`; separately decide whether the father field ends at `Jose del Carmen Pulgar` or contains an unresolved terminal mark. After conversion-control resolves the row, run a separate identity-bridge review before connecting this entry to any canonical Pulgar, Arriagada, Smith, Jose, Juana, or Dario person page.
