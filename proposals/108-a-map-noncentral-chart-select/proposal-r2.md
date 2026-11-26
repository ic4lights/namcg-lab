# Proposal 108-a-map-noncentral-chart-select, round 2 (revision note — no new mathematics)

## Result
Round 1 verdict (review-r1.md, verbatim line): `VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3`.
All mathematical claims of the package were verified and independently re-derived by the gatekeeper ("Every
mathematical claim reproduces and independently re-derives ... the reproduction pack and all 17 manifest hashes
verify, the splice contract certifies exactly"); nothing in the round-1 mathematics is withdrawn. Round 2 adopts
the gatekeeper-staged corrected insert as the integration payload and records the F5 provenance fix. The sole
integration payload is now `insert-r2.tex` (3072 B / sha256/16 `180b005188c8268a` / 1 CRLF), a byte-for-byte copy
of the gatekeeper byte authority `scratch/gk108/insert-corrected-gk.tex` (adopted without retyping by
`adopt_r2_108.py`; `CANDIDATE MATCH True`). Against the current live appH (812227 / `698f38979140770d` / 3876)
the r2 splice gives computed POST **815301 / `316c7b6f549ed660` / 3878** — equal to the gatekeeper-certified
triple — with undo True and live appH unchanged (`simulate_apply_108_r2.out`; preview
`scratch/sim/appH_after_108_r2_preview.tex`). Problem A stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; the
package closes nothing new.

## Disposition of findings (all four insert substitutions adopted verbatim from the gatekeeper-staged bytes)
- **F1 (scalar-term clause, affine reading)** — adopted in `insert-r2.tex`:
  "possibly with state-independent scalar terms, the bivector of a state with one-point functions
  \(x^K=\omega(\hat X^K)\) equals \(c^{IJ}{}_Kx^K\) up to the constant contributed by the scalar terms,"
- **F2 (rank-2 extent parenthetical)** — adopted:
  "Where it is degenerate (rank \(2\) at every point of the fuzzy sphere, hence at every point of any
  four-coordinate embedding of a two-dimensional orbit),"
- **F3 (matrix-model condensate gap in the self-closing list)** — adopted:
  "at fixed bivector 1-jet, they do not exhibit a noncentral condensate of the matrix model of this book,
  they do not cover generic non-Lie-type condensates,"
- **F4 (width-measure parenthetical)** — adopted:
  "its coherent-state fluctuation has relative width exactly \(1/\sqrt j\) about the mean bivector, in the
  commutator-fluctuation-over-bivector-norm measure,"
These are exactly the four substitutions listed in review-r1.md "Corrected snippet"; the diff between
`insert-r1.tex` and `insert-r2.tex` contains nothing else (gatekeeper diff-verified; adopted as staged bytes,
so verbatim by construction). **F1–F5 dispositions come from the gatekeeper-staged byte authority verbatim** —
no wording was authored by the researcher in this round.

## F5 fix (documentation provenance, two sentences)
In this package the hygiene rerun is recorded as executed from the proposal-folder cwd
(`cd proposals/108-a-map-noncentral-chart-select && python -I hygiene_108_r2.py`), because the battery's H21
check echoes the file argument verbatim (`file=insert-r2.tex` is only reproducible with folder cwd and no path
argument). Everything else — the v3 battery, the simulate script, the v1/v2 failure-signature reproductions and
the previews — remains byte-identical when run from the repo root as originally stated in proposal-r1.md D9.
For r2 this is executed and recorded, not just stated: `hygiene_108_r2.out` (773 B / `e02de1598c85cf51`) was
produced from the folder cwd and reports `file=insert-r2.tex sha256/16=180b005188c8268a`, 21/21 PASS.

## F6 (informational) — acknowledged
The standard-textbook character of items 2–3 and the 1-jet scoping of "bivector-automorphism group" are
acknowledged; they match the existing claim-table scoping (items 6–8) and require no text change.

## No-new-mathematics statement
Round 2 introduces **no new mathematics, no claim-table change and no new numerals**: the four insert
substitutions record exactly the hypothesis/gap extents the round-1 claim table and Remaining-open-steps list
already state (per the gatekeeper's own Recommended disposition), the claim table of proposal-r1.md is
unchanged and still matches the adopted payload, and all numerals in this note are re-measured from disk or
quoted from review-r1.md.

## Status-label recommendation
Unchanged. Problem A: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (appH L16–17 verbatim). A.map / edge
`A.map.noncentral-chart-select`: untried -> attempted at integration (as in round 1). No label edit proposed.

## Milestone assessment
Routine revision round; no MILESTONE.md trigger (consistent with review-r1 "MILESTONE: none" and the 105/106/107
same-chain precedent).

## Author decision needed
None.

## Remaining open step
Unchanged from round 1 (review-r1 "Not established / still OPEN"): (1) NAMCG-matrix-model realization of a
noncentral condensate class; (2) a rank-4 nondegenerate 4-orbit instance; (3) the order-Θ² pullback selection on
the derived x-dependent background and whether the bivector 1-jet pins the embedding 2-jet inside the 20-dim
fiber; (4) the emergent reading of the leaf; (5) generic non-Lie-type condensates.

## Special instructions for the gatekeeper
Integration payload is `insert-r2.tex` ONLY; `insert-r1.tex`, `simulate_apply_108_r1c.*` and the r1 preview are
superseded inert provenance. Re-certify the splice from live bytes at integration (PIN rebuilt, no hard-coded
offset); expected POST against live 812227/`698f38979140770d`/3876 is 815301/`316c7b6f549ed660`/3878 (recomputed
independently in this round, equal to the gatekeeper certification). Nothing outside this proposal folder and
`scratch/sim/appH_after_108_r2_preview.tex` was written.
