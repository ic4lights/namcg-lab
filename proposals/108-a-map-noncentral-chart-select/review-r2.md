[Orchestrator note 2026-11-21: round-2 diff review by the same gatekeeper instance that authored review-r1 (fable, aacd11b884c0145d7), ordinal 38 chain. Digest + targeted reads (full scan due at ordinal 40). Protocol 5: byte-authority chain re-verified, r2 artifacts rerun, F1-F5 re-verified. Saved verbatim.]

---

VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
Round 2 adopts my round-1 staged byte authority verbatim, closes all five findings, reproduces byte-for-byte under my own reruns, and my independent splice certifies the POST triple exactly — integrate `insert-r2.tex` as-is.

## Source reading
digest + targeted reads (full scan not performed: ordinal 38, due 40; per protocol 5 I re-read every changed artifact plus review-r1.md and the refreshed manifest; unchanged content relied on from my r1 full-package read this session). Read in full this round: `proposal-r2.md` (5753 / `2a84a51c3a188e61`), `manifest.md` (r2), `insert-r2.tex`, `simulate_apply_108_r2.py`, `adopt_r2_108.py`, `hygiene_108_r2.py` (diffed vs r1), both r2 `.out` files, `review-r1.md` on disk (`e1dd88b79f8be127`). No unreadable files.

## Claim under review
Unchanged from round 1 (byte-proven untouched): scalarity dichotomy; Lie-type derived bivector with the fuzzy-sphere instance; Sp(4) chart 1-jet torsor with so(3) 1-jet automorphism gauge; rank obstruction; finite-N 't Hooft-block dependence — all for the stated abstract hypothesis classes only. Target: Problem A, `chapters/appH-microscopic-proofs.tex` L16–17 verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." Status: OPEN. Priority: CRITICAL PATH. Edge `A.map.noncentral-chart-select`: untried → attempted at integration; closes nothing.

## Checks performed
Directly verified this round (all `python -I`):
1. **Byte-authority chain closed.** `insert-r2.tex` = 3072 B / `180b005188c8268a` / 1 CRLF and byte-equal to `scratch/gk108/insert-corrected-gk.tex`. Stronger than the required fence-diff: applying exactly my four staged substitutions to `insert-r1.tex` reconstructs `insert-r2.tex` byte-for-byte, so nothing else changed.
2. **Reproduction pack rerun.** `hygiene_108_r2.py` from folder cwd: 21/21 PASS, H01 CRLF=1, H15/H16 PASS, H20 bytes=3072, H21 `file=insert-r2.tex sha256/16=180b005188c8268a`; my capture byte-identical to shipped `.out` (773 / `e02de1598c85cf51`). `simulate_apply_108_r2.py` from repo root: PRE 812227/`698f38979140770d`/3876, payload triple asserted, PIN count 1 offset 14892, POST computed 815301/`316c7b6f549ed660`/3878 = my certification (loud-flag guard present), delta +3074/+2, undo True, POST PIN count 1, live unchanged; byte-identical to shipped `.out`. Source read: read-only on `chapters/`, writes only `scratch/sim/`.
3. **Independent re-certification.** My own splice of live bytes + `insert-r2.tex` → 815301 / `316c7b6f549ed660` / 3878, byte-equal to both `scratch/gk108/gk_post_preview_r1_corrected.tex` and `scratch/sim/appH_after_108_r2_preview.tex`; my undo restores live bytes; live appH re-measured after all runs: 812227 / `698f38979140770d` / 3876 (unchanged).
4. **Manifest:** 26/26 listed entries re-hashed, all match. `hygiene_108_r2.py` differs from r1 only in header comments plus one code line (default `fname` r1→r2); the 21 checks are otherwise identical. `adopt_r2_108.py` / `mk_hygiene_r2_108.py`: one write site each, confined to the proposal folder; adopt driver asserts my candidate triple and control-byte cleanliness before writing, prints CANDIDATE MATCH.
5. **Rule-7 numerals in `proposal-r2.md`:** every numeric token is a disk-measured triple/count I re-measured myself or a reference quoted from review-r1.md. No new mathematics-side numerals.

Not rerun this round (disclosed): v3 battery and v1/v2 provenance reruns — code hashes re-confirmed identical to what I reran and reproduced byte-for-byte in r1 this session.

## Findings
none (blocking: 0; major: 0).
Round-1 closures, with adopted text quoted from the byte-verified payload: **F1** — "possibly with state-independent scalar terms ... equals \(c^{IJ}{}_Kx^K\) up to the constant contributed by the scalar terms" (matches claim-table item 4 affine scoping). **F2** — "rank \(2\) at every point of the fuzzy sphere, hence at every point of any four-coordinate embedding of a two-dimensional orbit" (matches my exact generic-rank-2 sympy result). **F3** — "they do not exhibit a noncentral condensate of the matrix model of this book" now in the self-closing list, adjacent to the 't Hooft-block material. **F4** — "in the commutator-fluctuation-over-bivector-norm measure". **F5** — `proposal-r2.md` records the hygiene rerun as folder-cwd (H21-echo explanation) and everything else as repo-root; I verified both executions myself, byte-identically. **F6** — undisturbed: the four-substitution diff touched no standard-textbook/1-jet scoping text.
Informational, non-gating: `manifest.md` line 3 says "post-ordinal-38 state", but its own live triple (812227) is the pre-38 state; a mislabel, numerically self-consistent. Integrator should re-anchor from live bytes (the script already does).

## Scope of what is established
Unchanged from round 1: established (for the stated abstract hypothesis classes) — the scalarity dichotomy and its trace-forced vanishing of scalar commutators in finite dimension; the Lie-type affine bivector with the fuzzy-sphere instance; the Sp(4) 1-jet torsor and exact so(3)/SO(3) bivector-1-jet automorphism gauge; the rank-2 obstruction for two-dimensional orbits; the finite-N 't Hooft-block bivector values at K=5, 8. Conditional/mechanism-level: out-of-class chart resolution via noncentral condensates. Still OPEN (unchanged, and no label touched or proposed): NAMCG-matrix-model realization of a noncentral condensate class; a rank-4 nondegenerate 4-orbit instance; order-Θ² pullback selection and the 20-dim fiber 2-jet question; the emergent reading of the leaf; generic non-Lie-type condensates. Problem A remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. Spacetime remains emergent throughout; no status, priority or completion label is changed by the payload or proposed.

## Recommended disposition
Integrate as-is. **Sole payload: `proposals/108-a-map-noncentral-chart-select/insert-r2.tex`** (3072 B / sha256-16 `180b005188c8268a` / 1 CRLF). Integrator: rebuild the PIN "does not close Problem~A.\r\n\r\n\paragraph{Missing step.}" from current live bytes (no hard-coded offset), expect PIN count 1; PRE 812227/`698f38979140770d`/3876 → **certified POST 815301 / `316c7b6f549ed660` / 3878**; verify POST PIN count 1, then run `scripts/build_check.py`. `insert-r1.tex`, the r1 simulate family and the r1 preview are inert provenance — do not integrate them.
**Milestone reasoning (one sentence):** no M1–M5 trigger — a bounded conditional mechanism that closes no critical-path target and changes no label, per the 105/106/107 same-chain precedent and review-r1's own "MILESTONE: none".

## Corrected snippet
Not needed — the adopted payload is my staged corrected text byte-for-byte.
