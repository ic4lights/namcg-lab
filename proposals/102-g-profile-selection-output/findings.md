# Item 102 — exact Dirichlet statistics of rho_p: findings for the write-up agent

> PROVENANCE: written verbatim from the FIX-102 dispatch's completion handback (the agent reported
> its Write of findings.md was blocked by the harness; the orchestrator persisted the returned
> content without edit). Numbers below were verified by the orchestrator to match
> `s4_dirichlet_rho_direct.out` (41 lines, live sha8 7b293544; the handback's "sha8 17544b9f" is a
> pipe/EOL artifact — manifest and citations must use live bytes).

## Route statement

Exact statistics of the moment-map obstruction factor rho_p = p! h_p(p) (h_p the complete homogeneous symmetric polynomial; rho_2 = 1 + s_2 with s_2 = sum p_i^2, sigma := s_2 = 1/D_eff) on the unit-trace profile simplex p = (p_1..p_D), p_i >= 0, sum p_i = 1 (W = 1), under the flat Dirichlet(1,...,1) weight, D SYMBOLIC. Per the manuscript this flat member is the Haar-frame pushforward of the named frame measure and the uniform-profile slot pushforward (chapters/appH-microscopic-proofs.tex L3191: "the pushforward of the slot law under p is exactly (D-1)!/(G(sum_i p_i/g_i)^D) ... at uniform input the weight is relabelling-symmetric and flat"; "the Haar measure pushes forward ... to the flat exchangeable weight on the simplex") and the flat member of the named fixed-trace beta family at a = 1, beta = 0 (L3193: "Two endpoints of the preceding paragraph sit in the family at a = 1, beta = 0: the flat Haar frame weight, and the slot pushforward at uniform profile"). The obstruction factor, rho_2 - 1 = 1/D_eff and the partition form rho_p = sum_{lambda |- p} (p!/z_lambda) prod (s_k/W^k)^{m_k} are L3177; the uniform floor prod_{k=1}^{p-1}(1+k/D) is L3179. L3195 records flat Dirichlet moments at D=3 only as a numerical confirmation; this item supplies the closed forms at general D (exact, symbolic), upgrading that numerics.

Script: `s4_dirichlet_rho_direct.py`, output `s4_dirichlet_rho_direct.out` (41 lines, live sha8 7b293544), run from repo root `python -I proposals/102-g-profile-selection-output/s4_dirichlet_rho_direct.py`, exit code 0, final line `ALL CHECKS PASS`.

Method (correct path only): rho_p via the partition (Newton) form with the unit-trace substitution x_1 = s_1 = 1 imposed before averaging; then E[prod_k s_k^{m_k}] obtained by grouping the multi-indices of s_{k_1}...s_{k_r} into equality patterns (set partitions of the factor list into b equal-index blocks), each pattern contributing D!/(D-b)! times the standard Dirichlet(1^D) monomial moment of the block-sum exponent profile, E prod_i p_i^{a_i} = (D-1)!/(D+A-1)! prod a_i!^{m} (this moment function is reused verbatim from s3b's `dirichlet_monomial_moment`, which is correct).

## Exact results (verbatim from s4_dirichlet_rho_direct.out)

- `p=1: rho_1 = 1 exactly on the unit trace simplex; E[rho_1] = 1 (explicit)`
- `rho_2 = 1 + s_2 and rho_3 = 1 + 3 s_2 + 2 s_3 verified from partition form (unit trace)`
- `p=2: E[rho_2] = (D + 3)/(D + 1)` (CHECK `E[rho_2] == 1 + 2/(D+1)`: True)
- `p=3: E[rho_3] = (D**2 + 9*D + 26)/((D + 1)*(D + 2))` (CHECK `E[rho_3] == 1 + 6/(D+1) + 12/((D+1)(D+2))`: True)
- `p=4: E[rho_4] = (D**3 + 18*D**2 + 131*D + 426)/((D + 1)*(D + 2)*(D + 3))`
- `CHECK E[rho_2] - floor(2,D) == (D-1)/(D(D+1)):` True (p=3, p=4 differences also printed, factored, each with factor (D-1) and positive numerator)
- `E[sigma]   = 2/(D + 1)`; `E[sigma^2] = 4*(D + 5)/((D + 1)*(D + 2)*(D + 3))`; `Var[sigma] = 4*(D - 1)/((D + 1)**2*(D + 2)*(D + 3))`. Positivity: numerator 4*(D-1); `numerator(D+2) = 4*D + 4` has all positive coefficients, so numerator > 0 for D >= 2; denominator > 0 for D >= 1; `Var(1) = 0` (sigma = 1 deterministically at D=1). Hence Var[sigma] > 0 for all D >= 2. (Contrast: [r2 correction per review-r1 Finding 2] the buggy s3b path's Var line is in fact nonnegative for every integer D >= 1 — the earlier "negative at small D" claim was wrong; s3b's Check-I/II expectations equal the true values divided by D, and its gap line is floor - E_true, sign-flipped relative to E - floor.)
- Rates: `D * E[sigma] -> 2`; `D^3 * Var[sigma] -> 4`, i.e. Var[sigma] ~ 4/D^3; sigma - E[sigma] -> 0 in L2 at rate D^{-3/2} (centred fluctuation; the uncentred L2 decay of sigma itself is at rate D^{-1}, ‖sigma‖_2 ~ 2/D) [r2 correction per review-r1 Finding 1]; E[rho_p] -> 1.
- Monte Carlo (seed 102, 400000 exponential rows normalized to the simplex; corroboration, not proof), all 9 means within 1% (worst rel.dev 8.19e-04):
  D=3: rho_2 1.500214 / 1.500000 / 1.42e-04; rho_3 3.101110 / 3.100000 / 3.58e-04; sigma 0.500214 / 0.500000 / 4.27e-04.
  D=6: rho_2 1.285480 / 1.285714 / 1.82e-04; rho_3 2.070316 / 2.071429 / 5.37e-04; sigma 0.285480 / 0.285714 / 8.19e-04.
  D=24: rho_2 1.079983 / 1.080000 / 1.54e-05; rho_3 1.258405 / 1.258462 / 4.49e-05; sigma 0.079983 / 0.080000 / 2.08e-04.
- Pointwise pin (h-recursion h[n] += h[n-1]*p_i, 40 random rational profiles, p=2..5): `pointwise pin 1 <= rho_p <= 1+(p!-1)sigma ... equality rho_2 - 1 = sigma: True`. The pin is pointwise on the simplex, hence also in mean: 1 <= E[rho_p] <= 1 + (p!-1) E[sigma]. Mean pin at fixed D (exact values): D=3: E[rho_2]=1.500000 = ub 1.500000 (pin sharp at p=2), E[rho_3]=3.100000 < ub 3.500000, E[rho_4]=8.400000 < ub 12.500000; D=6: 1.285714 = 1.285714; 2.071429 < 2.428571; 4.119048 < 7.571429; D=24: 1.080000 = 1.080000; 1.258462 < 1.400000; 1.581880 < 2.840000.

## Claim classification (rule 6)

- Established-in-repo reproductions: rho_p definition, partition form, D_eff, rho_2 - 1 = 1/D_eff (appH L3177); uniform floor and equality case (appH L3179; reproduced exactly in `s2_uniform_rho_r2.out`, "ALL EXACT CHECKS PASS", floor rho_p = prod_{k=1}^{p-1}(1+k/D), D=2..5 p=1..6 — cite that file for the floor equality); flat simplex measure as Haar-frame pushforward / a=1,beta=0 family member (appH L3191, L3193).
- In-folder exact computations (sympy, D symbolic, checked in s4 .out): the four E[rho_p] closed forms, the three sigma moments and Var factorization/positivity, the limits and 4/D^3 rate, the corrected E[rho_2] - floor = (D-1)/(D(D+1)), the mean-pin relations. The Dirichlet monomial moment consumed is the standard one, stated explicitly in the script.
- MC corroboration: the 9 printed means (corroboration, not proof).
- `s1_frame_identities.out`: cited ONLY as frame-identity corroboration (Parseval/row-level/iid errors ~1e-15, truncated-frame rho_2 vs floor at N=6,8,12); no Dirichlet content taken from it.
- Not claimed: that the flat Dirichlet statistics select any profile, or that the flat measure is produced by the matrix integral of the core action (appH L3191/L3193: the deformation origin "is not established"; the frame side "supplies no state and no selection mechanism").

## What s3b's buggy path actually returned (identification, cheap)

Culprit: `E_of_power_sum_monomial` in `s3b_dirichlet_rho_stats.py`. Two defects: (a) falling factorial `(D-1)!/(D-b)!` instead of the correct `D!/(D-b)!` for assigning b equal-index blocks to D slots; (b) Check-I averaged `rho_partition_expr(p)` without imposing the unit-trace substitution x_1 = 1, so its "E[rho_1]" was E[s_1] of the non-normalized partition form and its "E[rho_2]" was E[s_1^2] + E[s_2] under the wrong countings. With defect (a) the one-block case gives E[rho_1] = 1 * (1/D) = 1/D — the printed artifact — and E[s_1^2] + E[s_2] = (D+1)/(D(D+1)) + 2/(D(D+1)) = (D+3)/(D(D+1)) — its printed "E[rho_2]" exactly. s4 replaces both defects and the correct values survive the MC check.

## OPEN list (carry into the write-up / later rounds)

1. s3b printed wrong values, verbatim from `s3b_dirichlet_rho_stats.out`: `p=2: E[rho_p] = (D + 3)/(D*(D + 1))` and `E[rho_2] - floor(2,D) = -(D - 1)/(D*(D + 1))` (true mean floor gap is +(D-1)/(D(D+1)), confirmed True in s4), and its gap line sign-flipped relative to E - floor (s3b expectations = true values / D; [r2 correction per review-r1 Finding 2]: its Var line is nonnegative for all D >= 1 — the earlier "negative at small D" claim was wrong); all s3b Check-I/Check-II numbers are superseded by s4. Do not cite s3b numbers. (s3b's pin block and MC block were sound; its MC rho_2 at D=3 = 1.500214 already matched the corrected exact 1.5.)
2. s1 degenerate inf rows: at lc=8, N=32 (`s1_frame_identities.out` lines 39, 49) the truncated-frame rows print `offdiag/minDiag inf  profile spread inf` (a slot variance underflows to zero in the truncated basis; RuntimeWarning divide-by-zero at s1 lines 76-77). Corroboration use only; flag when citing s1 numbers.
3. Do these Dirichlet statistics touch Problem G missing steps (i)-(iv) (appH L3119ff) or the profile-selection question? Honest answer: no. They characterize the measure on profile space (what rho_p-statistics average to under the flat member of the named family); they do not select the actual profile of a given matrix. appH L3189 ("no weight on profile space ... produced by the core"), L3191 ("no weight on profile space beyond the profile data already supplied"), L3193 ("it supplies no state, its origin in the matrix integral is not established") govern. The content is an exact-statistics supplement to the measure characterizations at L3177/L3191/L3193/L3195 (upgrading L3195's D=3 numerical flat-Dirichlet confirmation to closed symbolic forms), leaving steps (i)-(iv) unchanged and closing nothing.
4. E[rho_4] and the p>=3 mean-pin gaps are printed but not yet used anywhere; a later package may relate E[rho_p] - floor to E[sigma]-data at general p if useful.

## Reproduction pack

- Re-run from repo root: `python -I proposals/102-g-profile-selection-output/s4_dirichlet_rho_direct.py`
- Expected invariants: exit 0; final line `ALL CHECKS PASS`; four `CHECK ... : True` lines; `Var[sigma] = 4*(D - 1)/((D + 1)**2*(D + 2)*(D + 3))`; `D^3 * Var[sigma] -> 4`; all 9 MC rel.devs <= 1e-2 (worst 8.19e-04). Requires sympy + numpy; seeds fixed (default_rng(102), random.seed(102)).
