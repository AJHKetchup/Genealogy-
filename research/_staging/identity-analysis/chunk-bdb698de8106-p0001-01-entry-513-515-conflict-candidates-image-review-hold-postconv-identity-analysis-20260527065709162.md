---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260527065709162
task_id: identity-analysis:research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-image-review-hold-postconv-evidence-extraction-20260527045039396.md
staged_draft: research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-image-review-hold-postconv-evidence-extraction-20260527045039396.md
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260527045039396.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
created: 2026-05-27
canonical_readiness: hold
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 513-515 Pulgar Row Hold

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-image-review-hold-postconv-evidence-extraction-20260527045039396.md`.
- No external research was performed. Evidence is limited to the assigned staged draft, referenced source packet, converted file/chunk, reviewed local notes, and existing canonical wiki pages.
- Entry 513 has unresolved identity-controlling conversion conflict. The converted file/chunk reads child name `Isolina del Carmen` / `Jose` and sex `Masculino`; the image-review packet says the child name appears to begin `Pulgar Rosa ...` with following given-name lines uncertain, while sex still reads `Masculino`.
- Entry 513 mother surname is not stable. Converted reading: `Juana de Dios Amador de Pulgar`. Image-review reading: `Juana de Dios Ama[?]gar` or `Ama[?]gada de Pulgar`. This packet does not justify normalizing to `Amador`, `Amagada`, or `Arriagada`.
- Entry 513 birth field is conflicted: converted `El mismo veinte dos ... a las cuatro de la manana`; image-review `Junio veinte i dos ... a las cuatro i media de tarde`.
- Entry 515 is a separate lower row and is useful only as a row-boundary control for this task.
- The assigned draft does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, Dario/Dario Pulgar Arriagada, or Alexander John Heinz. No Dario-line attachment is supported from this draft.

## Hypothesis 1: Entry 513 Is A Held Pulgar Registration Lead

Literal evidence:

- The source packet says entry 513 father reads `Jose del Carmen Pulgar`; declarant reads `Jose del C. Pulgar`, `Padre`, age `Cuarenta i siete Anos`, profession `Agricultor`, domicile `Calle Colon`.
- The converted file/chunk also records father/declarant as `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, profession `Agricultor`, and domicile `Calle Colon`.

Interpretation:

- This is the leading hypothesis. Entry 513 is probably Pulgar-relevant, but the child identity, mother identity, and birth details are not promotable until targeted conversion QA resolves or explicitly marks the disputed fields.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.58 | Father/declarant Pulgar context is plausible; exact people remain unsettled. |
| conflict_severity | 0.86 | Child name, mother surname, and birth time affect core identity and relationship claims. |
| evidence_quality | 0.62 | Civil-register evidence is relevant, but the decisive readings are disputed. |
| conversion_confidence | 0.28 | Assigned packet rates conversion confidence low. |
| claim_probability | 0.64 | Probable Pulgar row; not proof-ready for exact person facts. |
| relevance | 0.98 | Directly matches the assigned conflict draft. |
| canonical_readiness | 0.08 | Hold for conversion QA and later proof review. |

## Hypothesis 2: Father/Declarant May Match Existing Jose Del Carmen Pulgar

Literal evidence:

- Assigned draft and source packet both preserve `Jose del Carmen Pulgar` / `Jose del C. Pulgar` as father/declarant readings.
- Existing `wiki/people/jose-del-carmen-pulgar.md` is a stub with a draft child link to `Tulio Cesar Luis Jose` from related staged evidence.

Interpretation:

- Same-person identity is plausible, but the existing stub cannot be used to settle this row's child name or mother surname. Attachment should wait until conversion QA and focused proof review.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.55 | Name and role align; row remains held. |
| conflict_severity | 0.70 | Premature attachment could propagate wrong child or spouse/mother context. |
| evidence_quality | 0.54 | Local evidence only; canonical page is draft-backed. |
| conversion_confidence | 0.30 | Father/declarant is stronger than other fields but still in a conflicted row. |
| claim_probability | 0.52 | Plausible candidate, not proved. |
| relevance | 0.92 | Direct Jose parent-candidate comparison. |
| canonical_readiness | 0.12 | No canonical edit or promotion supported. |

## Hypothesis 3: Mother Candidate Is Juana De Dios Ama[?]gar / Ama[?]gada De Pulgar

Literal evidence:

- Converted file/chunk reads `Juana de Dios Amador de Pulgar`.
- Image-review packet reads `Juana de Dios Ama[?]gar` or `Ama[?]gada de Pulgar`.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a stub with draft relationship evidence from a related held register cluster.

Interpretation:

- `Juana de Dios Amagada de Pulgar` is a candidate comparison only. The assigned packet requires the uncertainty marker to remain visible.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.42 | Given-name and `de Pulgar` context align; surname is unresolved. |
| conflict_severity | 0.82 | A wrong maternal surname would create duplicate-person and relationship errors. |
| evidence_quality | 0.48 | Relevant but letter-level uncertainty controls the result. |
| conversion_confidence | 0.22 | Mother surname is one of the stated low-confidence fields. |
| claim_probability | 0.44 | Possible same person as the Amagada stub, not proof-ready. |
| relevance | 0.94 | Direct Juana parent-candidate comparison. |
| canonical_readiness | 0.06 | Hold; do not merge or attach. |

## Hypothesis 4: Arriagada Cluster Is A Double-Check Lead Only

Literal evidence:

- Existing `wiki/people/juana-arriagada-de-pulgar.md` and `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` belong to a separate staged register cluster.
- The assigned draft does not confirm `Arriagada` and does not name `Jose del Carmen Segundo Pulgar Arriagada`.

Interpretation:

- Similar Pulgar/Jose/Juana context justifies later comparison after row QA. It does not justify silently correcting `Ama[?]gada` to `Arriagada` or merging clusters.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.18 | Context similarity only. |
| conflict_severity | 0.78 | Conflation could collapse different mothers, children, or register entries. |
| evidence_quality | 0.44 | Local evidence is relevant but not bridging. |
| conversion_confidence | 0.22 | The possible surname bridge is exactly the disputed field. |
| claim_probability | 0.16 | Review lead only. |
| relevance | 0.78 | Relevant because existing wiki context includes Jose/Juana candidates. |
| canonical_readiness | 0.02 | No merge, rename, or attachment supported. |

## Hypothesis 5: Dario Arturo Pulgar-Smith / Dario Arturo Pulgar Connection

Literal evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and warns not to automatically merge similarly named Pulgar records.
- Local CV analyses treat `Dario Arturo Pulgar` as a document-level subject needing identity-bridge proof before attachment to `Dario Arturo Pulgar-Smith`.
- The assigned entry 513-515 draft contains no Dario, Arturo, Smith, descendant, or lineage statement.

Interpretation:

- This is a low-confidence lineage lead only. The exact next proof-review step would be, after entry 513 conversion QA, a separate lineage proof review from confirmed entry 513 identities to later Pulgar generations, then a separate bridge from `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct Dario evidence in the assigned source. |
| conflict_severity | 0.80 | Premature attachment would create unsupported ancestor-line claims. |
| evidence_quality | 0.38 | Broad Pulgar context only. |
| conversion_confidence | 0.28 | Entry 513 identities are unsettled. |
| claim_probability | 0.06 | Very low from this source alone. |
| relevance | 0.66 | Required Pulgar-line guardrail. |
| canonical_readiness | 0.00 | No canonical action supported. |

## Hypothesis 6: Same As Dario Jose Pulgar-Arriagada Or Dario/Dario Pulgar Arriagada

Literal evidence:

- Canonical `wiki/people/dar-o-pulgar-arriagada.md` currently contains a 2000 expropriation-event claim for `Dario Pulgar Arriagada`.
- Staged notes also contain `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, and `Dario Pulgar-Arriagada` candidates, generally held for identity-bridge review.
- The assigned conflict draft has no Dario given name, no Arturo, no Dario Jose, and no confirmed `Arriagada` surname.

Interpretation:

- Unsupported from this draft. These names must remain separate hypotheses until a proof-reviewed source bridges them by more than surname or family-context similarity.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.02 | No direct Dario or confirmed Arriagada evidence. |
| conflict_severity | 0.86 | Name-only merge risk is high across separate generations and sources. |
| evidence_quality | 0.34 | Compared Dario clusters are not bridged by this draft. |
| conversion_confidence | 0.22 | Possible surname similarity is unresolved. |
| claim_probability | 0.02 | Not probable from current evidence. |
| relevance | 0.60 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Keep separate. |

## Conflicts

- Same-person conflict: unresolved. Entry 513 father/declarant may match an existing Jose stub, but no same-person merge is proof-ready.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar`; high if the current held row is used to force a child, mother, or Dario-line identity.
- Name-variant conflict: child readings include converted `Isolina del Carmen` / `Jose` versus image-reviewed `Pulgar Rosa ...`; mother readings include `Amador`, `Ama[?]gar`, and `Ama[?]gada`. `Arriagada` remains only a comparison lead.
- Relationship conflict: entry 513 cannot support a promoted parent-child relationship until the child identity and mother surname are settled. Entry 515 remains row-boundary evidence only.
- Chronology conflict: no Dario-line chronology can be evaluated from this source because no Dario identity appears. The entry 513 birth date/time itself is a conversion conflict.

## Ranked Hypotheses

| rank | hypothesis | probability | next step |
|---:|---|---:|---|
| 1 | Registration-scoped hold for entry 513 | 0.64 | Targeted conversion QA before proof review. |
| 2 | Jose father/declarant may match existing Jose stub | 0.52 | Revisit after row QA confirms child and parent fields. |
| 3 | Mother may be Juana de Dios Ama[?]gar / Ama[?]gada de Pulgar | 0.44 | Preserve uncertainty; compare only after surname QA. |
| 4 | Nearby Arriagada cluster is a double-check lead | 0.16 | Do not normalize or merge; compare later only if QA supports it. |
| 5 | Dario Arturo Pulgar-Smith / Dario Arturo Pulgar lineage lead | 0.06 | Requires separate lineage proof after entry 513 QA. |
| 6 | Same as Dario Jose / Dario or Dario Pulgar Arriagada | 0.02 | Unsupported; keep separate. |

## Recommended Next Action

Keep the assigned staged draft on `hold_for_conversion_qa`. Do not promote facts, create or attach relationships, merge people, rename pages, or attach this register page to any Dario/Pulgar canonical identity.

The exact next step is targeted conversion QA against the source image for entry 513: settle or explicitly uncertainty-mark the child-name field, birth month/day/time, father/declarant form, mother surname, and row boundaries. After that, run a focused proof review comparing any confirmed Jose/Juana/child readings against `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada` before any broader Dario-line proof review.
