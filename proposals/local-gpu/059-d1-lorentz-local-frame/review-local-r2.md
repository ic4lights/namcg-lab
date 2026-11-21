VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

Gatekeeper, local r2 review, remote/claude, 2026-11-21. Saved here by the orchestrator. The gatekeeper's check script is gk_chk_local_r2.py.

Source reading: digest + targeted reads (appH L713-760, L1505-1597, L1735-1737; ch17 D1; ch03 L245-295; ch04 L75-185; ch10). The full scan is deferred.

## Checks
- Option (b) is confirmed by hand and with sympy.
  - S_12 = +xi is CORRECT for the stated lift and orientation; -xi violates (I). The earlier -xi is the same field written in psi' = -psi. It was not merged, so there is no prior-claim error.
  - T=F=0, R=-1, Ric=+delta, t_a=0.
- Ghost = -Laplacian on S^2, l(l+1) with multiplicity 2l+1. Redundancy Sum x_i rho~_i = -S_12.
- New claims:
  - The derivation lemma is correct but needs *-closure (see m1).
  - The su(2) and so(5) truncations hold.
  - The Peter-Weyl compression holds.
  - The fuzzy redundancy identity is exact.
  - The fuzzy sphere has no frame index.
  - The Lorentzian finite-N no-go holds: so(3,1) is simple and non-compact, so it is represented trivially and D_a=0.
- Scripts: 21 and 31 PASS, identical output.
- apply_and_build: pre 4ea0ee0f... / post b6ce7529..., 404 pp, BUILD CLEAN.
- Citations:
  - HattoriSekoTsuchiya2026 checked against arXiv/PTEP.
  - Elitzur1975 and FradkinShenker1979 abstracts checked. The FS end page is not independently verified.
- Placement: end of Problem D. The status sentence follows the L1531/L1570 pattern.
- M1-M3 and m1-m4 from the earlier review are closed.
- Derivation-first: keep all the new content. It redirects the finite-N D1 route to Krein spaces.

## Findings
- m1 (required). Replace "So every \(\mathrm{ad}\,\hat X_a\) that preserves \(\mathcal A\) vanishes on it, and no base of positive dimension is realised." with
  "So, for \(\mathcal A\) closed under the adjoint, as the functions on \(Z\) are, every \(\mathrm{ad}\,\hat X_a\) that preserves \(\mathcal A\) vanishes on it; in any case a finite-dimensional commutative algebra has finite spectrum, so no base of positive dimension is realised."
- m2 (required). Replace "this is the fact behind the statement in" with "the same fact for \(\mathfrak{so}(4,1)\supset\mathfrak{so}(3,1)\) underlies the statement in".
- m3 (optional). Write "\tfrac12\sum_i\{X_i,\mathcal L_iF\}=(2\hbar_{\mathrm{eff}})^{-1}[\sum_iX_i^2,F]=0" for parallelism.
- m4 (optional). In the so(5) sentence, state T=F=0 and R=-(dd-dd) explicitly, and drop "Checked in dimensions 4, 5 and 20".

## Disposition
- Researcher r3: m1 and m2, plus m3 and m4 if adopted. Then a gatekeeper re-check and the full scan.
- No label change. D/D1 stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- Ranked avenues:
  1. Krein form (relax h2), using the framework at L1583-1593.
  2. A noncommutative coefficient algebra.
  3. Euclidean so(5) (gated on E).
  4. N -> infinity with a regulated trace.
  5. Approximate relations.
