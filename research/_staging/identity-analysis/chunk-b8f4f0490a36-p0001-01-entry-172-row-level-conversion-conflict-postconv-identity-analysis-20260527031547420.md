---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527031432119
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
conflict_type: row_level_conversion_conflict
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity Analysis: Entry 172 Pulgar/Arriagada Row-Control Conflict

## Blockers First

- The current converted Markdown still records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the assigned chunk and targeted image review identify physical row `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- The father field is certified by the latest staged QA only as `Jose del Carmen Pulgar`; the assigned chunk's terminal `S.` is not proof-ready.
- This entry does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or any direct connection between the 1888 child and later Dario identities.
- Existing wiki context contains separate Pulgar-line candidates and parent-name variants, including `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`; this staged draft does not prove that those Juana forms are the same person.
- No canonical merge, rename, parent-pair promotion, or Dario attachment is ready until proof review accepts the row-control QA and conversion-control reconciles or supersedes the stale/row-shifted converted Markdown.

## Literal Source Readings

From the staged source packet and targeted conversion QA note:

- Physical row: entry `172` on register page 58.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar`; suffix unresolved.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employed, resident at Calle de Valdivia.

Conflicting derivative reading from the current converted Markdown:

- Entry `172`: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth date 6 April 1888 at ten at night.

## Interpretation Boundary

The image-reviewed staged source packet and QA note support treating the Burgos/de la Cruz entry as a derivative row-control conflict for this task. They do not support silently editing the converted Markdown, treating `Pulgar S.` as certified, or attaching this record to a later Dario identity.

## Hypotheses And Evidence

### H1: Physical row 172 is the Pulgar/Arriagada birth entry

Evidence for:

- The staged conflict draft says the visible row number `172` aligns with the Pulgar/Arriagada row on the left page.
- The source packet states that direct image review found agreement for child name, sex, dates, place, mother, informant, and official signature.
- The assigned chunk transcribes row `172` as `Jose del Carmen Segundo Pulgar Arriagada`, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.

Evidence against:

- The current converted Markdown gives a different entry `172` for Burgos/de la Cruz.

Assessment:

- Ranked hypothesis: 1.
- Identity confidence: 0.91.
- Conflict severity: high.
- Evidence quality: 0.88.
- Conversion confidence: 0.55 overall because derivative files conflict; 0.90 for the image-reviewed row-control finding.
- Claim probability: 0.92 for the row-control claim.
- Relevance: direct, 0.99.
- Canonical readiness: not ready; hold for proof review and conversion QA reconciliation.

### H2: Current converted Markdown entry 172 is the controlling literal entry for this task

Evidence for:

- The converted Markdown is a derivative file for the same source path and labels the Burgos/de la Cruz text as entry `172`.

Evidence against:

- The assigned chunk for the same chunk id records the Pulgar/Arriagada row.
- The staged targeted QA note states that direct source-image review shows physical row `172` as Pulgar/Arriagada, not Burgos/de la Cruz.
- The staged conflict draft explicitly says the source image controls the staged evidence.

Assessment:

- Ranked hypothesis: 2.
- Identity confidence: 0.12.
- Conflict severity: high.
- Evidence quality: 0.35 for this derivative reading in this task.
- Conversion confidence: 0.20 for the converted Markdown row assignment.
- Claim probability: 0.10 as controlling evidence for this staged conflict.
- Relevance: direct to the conflict, 0.95.
- Canonical readiness: blocked.

### H3: `Jose del Carmen Pulgar` in the 1888 entry is the same father candidate as canonical `Jose del Carmen Pulgar`

Evidence for:

- Existing wiki page `wiki/people/jose-del-carmen-pulgar.md` has a stub for `Jose del Carmen Pulgar`.
- Existing promoted relationship context records `Jose del Carmen Pulgar` as probable parent of `Tulio Cesar Luis Jose` from an 1889 Los Anjeles birth register entry.
- The 1888 staged entry records a father named `Jose del Carmen Pulgar`, employed, resident at Calle de Colipi.

Evidence against:

- The staged draft explicitly says not to merge `Jose del Carmen Pulgar` with any existing father candidate based on this entry alone.
- The 1889 relationship context includes another mother form, `Juana de Dios Amagada de Pulgar`, not the exact 1888 mother form `Juana Arriagada de Pulgar`.
- The 1888 father suffix remains unresolved, and this note does not compare original images beyond the staged reviews.

Assessment:

- Ranked hypothesis: 3.
- Identity confidence: 0.62 as a candidate bridge, not a merge.
- Conflict severity: medium.
- Evidence quality: 0.76.
- Conversion confidence: 0.70 due to father suffix and row-control conflict.
- Claim probability: 0.55 for same-person possibility.
- Relevance: high, 0.90.
- Canonical readiness: not ready; requires proof-review comparison of the 1888 and 1889 entries, including age, residence, occupation, spouse/mother form, and father-name suffix.

### H4: `Juana Arriagada de Pulgar` in the 1888 entry is the same mother candidate as `Juana de Dios Amagada de Pulgar`

Evidence for:

- Both names appear in Pulgar parent contexts in existing wiki/research materials.
- Both are styled as married-name forms ending `de Pulgar`.
- Existing wiki context has `Juana Arriagada de Pulgar` as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`, while a separate relationship page has `Juana de Dios Amagada de Pulgar` as probable mother of `Tulio Cesar Luis Jose`.

Evidence against:

- The surnames/name strings differ materially: `Arriagada` versus `Amagada`, with `de Dios` present in one form and absent in the other.
- The staged draft says not to equate `Juana Arriagada de Pulgar` with any other Juana variant from this entry alone.
- No current staged evidence provides an explicit same-person bridge.

Assessment:

- Ranked hypothesis: 4.
- Identity confidence: 0.38.
- Conflict severity: medium.
- Evidence quality: 0.62.
- Conversion confidence: 0.76 for the literal 1888 mother name, lower for cross-record identity.
- Claim probability: 0.30 for same-person identity.
- Relevance: high, 0.88.
- Canonical readiness: not ready; requires proof review focused on Juana-name variants across the 1888 and 1889 parent entries.

### H5: 1888 child `Jose del Carmen Segundo Pulgar Arriagada` is a direct identity bridge to Dario identities

Evidence for:

- The child has Pulgar/Arriagada surnames, which overlap with later Pulgar-line materials.
- Existing wiki and staging context include `Darío Pulgar Arriagada`, `Dario Jose Pulgar-Arriagada`, `Dario Arturo Pulgar`, and `Dario Arturo Pulgar-Smith` as separate Pulgar-line candidates.

Evidence against:

- The 1888 child is named `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.
- No birth date, parent, spouse, child, residence-continuity, or record-chain evidence in this staged draft links the 1888 child to a Dario identity.
- Existing `Dario Arturo Pulgar-Smith` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to merge similarly named Pulgar records without identity review.
- `Dario Arturo Pulgar` CV evidence is document-level occupational evidence and does not state parentage or a Pulgar-Arriagada bridge.
- `Dario Jose Pulgar-Arriagada` photograph staging is held because the image itself does not visibly name him.
- `Dario Pulgar-Arriagada` 1929 convention listing gives a name and public role but no family relationship.
- Canonical `Darío Pulgar Arriagada` currently has a 2000 expropriation-notice event only and no family relationship.

Assessment:

- Ranked hypothesis: 5.
- Identity confidence: 0.08.
- Conflict severity: low for this entry, high if used for a merge.
- Evidence quality: 0.20 for any Dario bridge from this staged draft.
- Conversion confidence: 0.00 for Dario linkage because no Dario is named in the entry.
- Claim probability: 0.05.
- Relevance: cautionary, 0.80.
- Canonical readiness: blocked; requires a separate identity-bridge proof review, not a name-overlap inference.

## Required Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather. No evidence in the staged entry links him to `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar`.
- `Dario Arturo Pulgar`: Staged CV packets identify a document-level subject through source title and CV continuity. Those packets support occupational chronology only and repeatedly require a separate bridge before attaching to `Dario Arturo Pulgar-Smith`.
- `Dario Jose Pulgar-Arriagada`: The staged photograph packet depends on source path/title context and is held for conversion QA/source metadata verification; it does not prove identity from visible text or provide relationships.
- `Dario/Darío Pulgar Arriagada`: The 1929 convention listing names `M. Dario Pulgar-Arriagada, Capitaine du Service de Santé`; the canonical `Darío Pulgar Arriagada` page has a 2000 expropriation-notice fact. Neither source supplies parentage or a bridge to the 1888 child.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar` is a plausible parent-candidate bridge across 1888 and 1889 Pulgar entries but not merge-ready. `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are separate literal readings until proof review resolves whether they are variants, errors, or distinct people.

## Conflict Summary

- Same-person conflict: unresolved for Jose parent candidates; unresolved and currently weak for Juana parent variants.
- Duplicate-person conflict: possible duplicate handling may eventually be needed for `Jose del Carmen Pulgar`, but this entry alone cannot decide it.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`; `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: derivative Burgos/de la Cruz converted text conflicts with image-reviewed Pulgar/Arriagada parent-child evidence.
- Chronology conflict: none identified within the Pulgar/Arriagada row itself; later Dario materials are not chronologically bridged to this 1888 child.

## Recommended Next Action

1. Proof review the exact staged conflict draft, source packet, and targeted conversion QA note for row-control acceptance.
2. Conversion-control should reconcile, replace, or annotate the current converted Markdown so entry `172` no longer silently conflicts with the image-reviewed Pulgar/Arriagada row.
3. After row-control acceptance, run a focused parent-identity proof review comparing the 1888 `Jose del Carmen Pulgar`/`Juana Arriagada de Pulgar` entry against the 1889 `Jose del Carmen Pulgar`/`Juana de Dios Amagada de Pulgar` context.
4. Keep all Dario identities separate until a dedicated identity-bridge review supplies dates, relationships, records, or explicit source assertions tying one of them to this parent/child cluster.
