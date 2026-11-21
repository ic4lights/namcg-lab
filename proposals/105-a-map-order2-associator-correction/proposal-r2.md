# Proposal 105 round 2 - C6 sentence replacement per review-r1 (single revision)

Date 2026-11-21. Branch local/gpu. Item 105, Problem A (edge A.map), proposed integration ordinal 35.
Basis: `review-r1.md` (FINAL gatekeeper verdict: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none |
FLAGS: none | PROGRESS: flat). The review's sole gating finding (MAJOR, finding 1) required replacing
one sentence of the insert line; the review states the exact replacement under "## Corrected snippet"
and its disposition is "Revise then integrate" with "nothing else in the package changes". This round
applies exactly that. No other claim, derivation, number, or file content of the package changes; the
mathematics of round 1 (C1a-C9, kappa=+1, bounded C6 no-go) is unchanged and was independently
re-derived by the gatekeeper in round 1.

## The single change
Old sentence (span 1218:1483 of `insert-r1.tex`, 265 B):

> In the five-structure natural ansatz built from contractions of the products \(\Theta\Theta\) and \(\Theta\partial\Theta\) of order \(\le2\) per slot, no jet-universal \(B_2\) solves \(A_2=\delta B_2\) at closed jets, so the natural-universal question remains open.

New sentence (gatekeeper verbatim, 546 B, extracted programmatically from the review's ```latex fence - never retyped):

> Within the explicitly enumerated five-structure ansatz of bidifferential operators of order \(\le2\) per slot built from fixed \(\Theta\Theta\) and \(\Theta\partial\Theta\) contraction types with coefficients independent of the \(\Theta\)-jets, no \(B_2\) in this class solves \(A_2=\delta B_2\) at all closed 1-jets; Kontsevich's formality theorem supplies a natural jet-dependent correction for every smooth Poisson bivector, so what remains open here is not the existence of a general natural correction but its selection by the matrix theory.

This fixes both limbs of finding 1: the no-go is now tied to the explicitly enumerated five structures
with jet-independent coefficients (the class actually tested by `s1b_order2_coboundary.py`, `col_struct`),
and what "remains open" is scoped to selection by the matrix theory, with the general existence result
recorded as settled (Kontsevich formality, name-level attribution verified by the gatekeeper at abstract
level, arXiv q-alg/9709040). Reference basis per review-r1: no \cite added; no Dolgushev/math/0410417
(struck - wrong identifier), no Cattaneo-Felder, no De Wilde-Lecomte anywhere in the insert
(forbidden-string asserts in both `mk_artifacts.py` and `mk_r2_sentence_check.py`).

## r2 artifacts (see manifest.md)
- `insert-r2.tex` 2130 B, sha256/16 e46c9870 - byte-identical to the gatekeeper candidate
  `scratch/gk105/insert_r2_candidate.tex` (asserted in the generator before writing); one CRLF-terminated
  ASCII line; braces 9/9; no \label/\ref/\eqref/\cite.
- `mk_artifacts.py` 12946 B, sha256/16 5ac31bb9 - now extracts the sentence from `review-r1.md` at
  generation time and emits `insert-r2.tex`; `findings.md` regenerates byte-identical to r1
  (8495 B, 6011658e). `insert-r1.tex` (7c6fd752) retained on disk as superseded provenance, not rewritten.
- `mk_r2_sentence_check.py` 2386 B, sha256/16 21cb9a21 - standalone span-splice check (run this round:
  CANDIDATE MATCH: True).
- `hygiene_105.py`/.out retargeted to r2 (847c0d9c / f87747a6): HYGIENE PASS on `insert-r2.tex`
  (appH live 805839 / 21163962 / 3870, PIN count 1, macros all pre-existing in appH).
- `simulate_apply_105.py`/.out retargeted to r2 (e22dc522 / 43485c94): BEFORE 805839/21163962e4f7f514/3870;
  sentence occurrences 1; PIN 80 B count 1; AFTER(simulated) **807971 / 53c1c478ae1a79ff / 3872**
  (asserted against the review-r1 r2 contract); simulated POST byte-identical to the gatekeeper preview
  `scratch/gk105/appH_after_r2_preview.tex`; live `chapters/appH-microscopic-proofs.tex` untouched
  (805839 / 21163962e4f7f514 / 3870 re-printed by the script).

## Integration contract (unchanged anchor, r2 payload)
Insert `insert-r2.tex` (+ blank CRLF) at the verified PIN: after the 058-paragraph closing
"they do not derive Assumption~\ref{ass:dictionary}." (preceded by "the sharp diamond cutoff, so")
and before "\paragraph{Missing step.}" of sec:status-A in `chapters/appH-microscopic-proofs.tex`.
PIN unique (count 1) in the live tree. Expected POST: size 807971, sha256/16 53c1c478ae1a79ff,
3872 CRLF - valid only for these exact r2 bytes. No status/priority/completion-label change:
Problem A remains OPEN / CRITICAL PATH for the matrix-derived label / PROGRAMME-CONDITIONAL;
the paragraph closes nothing and derives neither ass:dictionary nor the half-sided inclusion.

## Provenance note (death #43)
The round-2 researcher died mid-edit (tool-echo; generator untouched on disk). It left
`mk_r2_sentence_check.py` and had verified the splice reproduces the candidate. The orchestrator then
applied the retarget of `mk_artifacts.py`/`hygiene_105.py`/`simulate_apply_105.py` mechanically: the new
sentence enters only via programmatic extraction from `review-r1.md` (the gatekeeper's own verbatim text);
no new mathematics was authored in this round. All r2 numbers above are from this session's re-runs.
