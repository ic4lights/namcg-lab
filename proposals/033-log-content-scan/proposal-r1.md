# Proposal 033-log-content-scan, round 1

## Result
Bounded, conditional, non-closing. First log-order comparison with nonzero values, off (N_s, n_D) = (6,2). N_tot = N_s+2-4 n_D, kappa_X = 1 - n_D/2, abar_1 = sum_i w_i tr(R/6 - E_i) = N_tot (R/6 - e) + kappa_X X' (weighted a_1 density = the Lambda^2-order density). Units 1/24 pi, totally geodesic Sigma.

1. **Closed forms, general content (exact; 20 sampled points, all families of 026/029/031; `content_scan.py`).**
   - Periodic (no deltas): 24 pi sigma_per = abar_1 - (N_tot/30)(R_Sigma - 3W).
   - Completed (031 contacts on every sector): 24 pi sigma_cmp = -(1/2) abar_1 + kappa_X tau_Omega - (N_tot/30)(R_Sigma - 3W).
   - Fixed state: 24 pi sigma_fs = 24 pi sigma_cmp + (3/2) abar_1^bos - tau_Omega. The offset from sigma_cmp is bosonic only, so independent of n_D.
2. **Dirac lemma (exact, symbolic: `dirac_lemma_symbolic.py`, also at 20 points).** With the Z_n weights (x,y,z) = (-1/2, 1, 1/2) of 029, antiperiodic Dirac = periodic Dirac + Fursaev-Solodukhin cross term of the uniform E_delta (Q = 1/4) + the Omega_delta cross term with J -> gamma^12/2. The contact normalisation is computed from the cross-term rule, not fitted. So contacts = -(3/2) abar_1 + kappa_X tau_Omega for every content: proportional to the Lambda^2-order data (weighted a_1, weighted Dynkin index). This explains why 031 was an equality of zeros, and that the three log coefficients differ off (6,2) only through abar_1 and tau_Omega.
3. **Rotation-invariant SD family.** sigma_cmp = (kappa_X - N_tot/30) R_Sigma = (28 - N_s - 11 n_D)/30 R_Sigma for every content, with the g-dependence of 029/031 cancelling; sigma_fs = sigma_cmp - R_Sigma + (3/2) g. The coefficient of sigma_cmp vanishes on the line N_s + 11 n_D = 28, which contains (6,2).
4. **T-side weighted a_2.** a_2^tot = (N_s-2) s + v - n_D d = N_tot s + (v' - n_D d'), with v' = v-4s, d' = d-4s. On SD/ASD points and the sampled J=0 non-SD points (15 of 20, exact) d' = v'/2, so a_2^tot = N_tot s + kappa_X v'. It vanishes there only for N_tot = kappa_X = 0, i.e. only at (6,2). On the non-chiral points the quartic remainder is 026's S_4(n_D).
5. **Variable-independent c-type comparison (new).** About constant SD or ASD Theta-bar, on the delta-rho = 0 plane-wave modes:
   - second order: v - 4s = (1/12) tr Omega^2 and d - 4s = (1/2)(v - 4s) (`quad_check.py`, exact at 2 cubic potentials, eps = 1/1000);
   - X^(1) = 0;
   - (1/12) tr Omega^2 = -(1/3) C^2 (6 modes per chirality, `tt_gap.py`), so kappa_C^T = N_tot/120 - kappa_X/3;
   - first order: tau_Omega^(1) = -R_ijij = -2W + R_Sigma (first-order formulas checked against the jet code, eps = 1e-5, `lin_validate.out.txt`);
   - Wald universality by the cross-term rule: a quadratic action kC C^2 + kE E_4 + kR R^2 gives entropy density 12 kC W + 12 kE R_Sigma + 12 kR R (reproduces eq. (70) for the scalar).

   Gap = (coefficient of W on the A side) - 12 kappa_C^T:

   | replica | gap | Lambda^2 gap c_A - c_T (appH) |
   |---|---|---|
   | periodic | 4 - 2 n_D | 4 - 2 n_D |
   | fixed state | 4 - n_D | 4 - n_D |
   | completed | 2 - n_D | -N_tot/4 + 4 kappa_X |

   - All gaps are independent of N_s.
   - Periodic and completed vanish on n_D = 2 for every N_s, with both sides nonzero for N_s != 6. This is the universal N_tot x (conformal scalar) counting. It tests neither G nor the index-weighted sector.
   - Fixed state vanishes on n_D = 4.
   - At (6,2) the fixed-state gap is 2, as at Lambda^2.
6. **Why the completed gap is 2 kappa_X.** tr Omega^2 is twice the Levi-Civita value on these modes. At fixed first jet the second jet of Omega^v has 33 independent components against 20 for Riemann (45 random second jets, exact rank: dR rank 20, dOmega rank 33, joint 33; `omega_riemann_full.out.txt`). The Omega_delta cross term sees tau_Omega only. This is the log-order analogue of the rho^2 X term at Lambda^2, which enters the quadratic form but no entropy.

## Target and status
Problem B (sec:status-B): Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL. Problem A likewise (dictionary only). Chapter 17 critical set A, B, C, D1, E, F, G-derived, N. Original target (B): derive tensor-block stationarity and the area term / G relation. This package supplies none of it. It computes the content dependence of the log-order comparison and locates the mismatch. No discrepancy found in the labels.

## Source reading
Digest + targeted reads (DIGEST CURRENT at start; chapters dirty by accepted 025-031). Read in full: appH 142-255 (B blocks 015-031); 031 proposal-r2 and review-r2; 029 proposal-r2; the 026 `geom.py`, `chk_S_formula.py`, `chk_a2_quartic.py`, `sd_content_scan.py`; 031 calibration and Dirac scripts. Not a full scan. Literature: Solodukhin 1104.3712 (Living Rev. Relativity 14 (2011) 8), record verified now. Eq. (70) is used only through the 029/031 calibrations (scalar eq. (70) reproduced by `delta_completion_calibration.py`, and re-derived by the cross-term rule in the c-type section). No new source; no new BibTeX (key Solodukhin2011 exists).

## Research and reasoning
- **Dirac lemma and N_tot.** The Dirac contacts and the uniform E_delta give -(3/2) times the weighted a_1; the Omega_delta gives the weighted Dynkin index times tau_Omega (vector 1, Dirac -1 x 1/2). The `content_scan.py` checks use independent piecewise per-component formulas and compare with the closed forms at every point (all zero, 20 points).
- **Where the match lives.** The completed coefficient equals the cross-term (Wald-type) value of the T-side a_2 with E -> Q R (Q = 1/4, all sectors incl. Dirac) and Omega -> Riemann-delta. That equality is by construction. It is not an independent verification of G_T = G_A.
- **Independent probe.** The plane-wave test reads the T side from the quadratic action about flat Theta-bar, with no variable choice. It gives the content-independent-in-N_s gaps above.
- **Parallel with Lambda^2.** The numerology 4b (periodic) and 4 - n_D (fixed state) at both orders is computed, not derived. A common origin is conjectured: linearised vector sector = Maxwell-like with F-type Omega.
- **Hypotheses inherited from 029/031.** Imported prescription S_BH = S_ent - Q; delta universality (delta content only from Theta^12 = 1/f, Theta^34 = 1); Dirac hybrid (antiperiodic gluing); n < 1 branch and first order in 1-n; Wald-type (G, torsion) reading for the E-sector (E_s = R/4 + T^2 terms, Weitzenboeck identity, no gradient of T); alpha = 1; Yukawas dropped; totally geodesic Sigma; one proper-time limit. Added here: constant (A)SD Theta-bar, delta-rho = 0 modes, W coefficient only.
- **Fork list (no-go is a fork).** Mismatch = 2 kappa_X (completed), 4 - n_D (fixed state). Avenues:
  1. Nonzero kappa_X means the T quadratic form has a non-Riemannian part (Omega = R + nabla T). Relaxation: variable-independent entropy (Dong / Iyer-Wald with the extra fields as dynamical) rather than the cross-term rule. Not done.
  2. Absorb the 33 vs 20 excess by an additional edge or contact term, 2 kappa_X W. Its natural source is a delta in nabla T; test on the smooth family with the exact Aharonov-Bohm heat trace (needs |1-n| terms).
  3. Fixed-state gap (+n_D, +4 kappa_X) equals the Lambda^2 one: a common replica choice (gluing) would fix both orders. Test whether a single choice (antiperiodic Dirac plus an Omega contact) closes both.
  4. N_s-independence: no scalar sector can repair the gap. Only kappa_X (n_D, vector) enters. Option: other field content (extra vectors / KK towers) shifts kappa_X and N_tot independently.
  5. Euler-type (a) coefficient: invisible to the quadratic form. Needs the global-coframe statement (E_4 = d(CS)). Not treated.
  6. delta-rho != 0 mode, non-chiral Theta-bar (G not conformally flat) and the n > 1 branch.

## Claim classification
| Claim | Class |
|---|---|
| closed forms sigma_per, sigma_cmp, sigma_fs | established algebra, given 029/031 inputs (checked at 20 exact points) |
| Dirac lemma | established (symbolic), given the Z_n weights |
| sigma_cmp = (kappa_X - N_tot/30) R_Sigma on rot-SD | numerical-exact (11 points), not proved |
| a_2^tot = N_tot s + kappa_X v' on chiral points | numerical-exact (15 points) |
| tr Omega^2 = -4 C^2, tau^(1) = -R_ijij, the gaps | numerical-exact on modes tested (12 modes); constant (A)SD background |
| 33 vs 20 components | exact rank, 45 samples |
| equality of gaps with Lambda^2 gaps | computed coincidence; origin conjectured |
| which replica the matrix model selects; G_eff | unresolved |

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`. Insert the block of `appH_insert.tex` after the 031 paragraph ending "Problem~B stays open and PROGRAMME-CONDITIONAL." (once, line 254, rechecked) and before `\section{Problem C: conformal mode and Cassini}`, separated by one blank line. Nothing replaced. Cite key Solodukhin2011 exists. No new \label or \ref. 0 TAB, 0 CR, no control chars (checked); compiled in a scratch copy outside the repo (stub preamble, \cite stubbed, \LUV defined): 0 errors. The block is `appH_insert.tex` (identical text); not repeated here to avoid divergence.

## Verification scripts
In `proposals/033-log-content-scan/` (outputs `*.out.txt`): `collect.py` (data.json, 20 points); `content_scan.py` (identities, closed forms, rot-SD, T side); `dirac_lemma_symbolic.py`; `lin_lib.py`, `lin_test.py` (validation against jets: `lin_validate.out.txt`); `tt_test.py` (modes, kappa_J = -1/3, tau + R_ijij = 0); `tt_gap.py` (gaps); `quad_check.py` (v-4s, d-4s at second order); `omega_vs_riemann.py`, `omega_riemann_map.py`, `tau_second_jet.py`, `omega_riemann_full.py`, `omega_riemann_rank.py` (Omega^v vs Riemann ranks). Libraries copied from 031. The T-side ratio and exact-rank outputs are as saved.

## Decisions Taken
- Chose the plane-wave W coefficient as the variable-independent probe, over the (G,torsion) Wald reading, because the latter is tautological with the contact completion.
- Kept the block conditional, with no label edit, and stated the Euler-coefficient limitation.
- Left unresolved the origin of the Lambda^2/log gap coincidence.

## Milestone assessment
Routine. A structural result (log-order contacts proportional to Lambda^2 data; gap table), not a derivation of any critical-path step. Not a breakthrough.

## Status-label recommendation
None. A, B, C, D1, E, F, G-derived, N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
None. Spacetime stays emergent.

## Remaining open step
Variable-independent entropy of the log action including the nabla T excess (avenues 1-2); replica / state selection (3); non-chiral background and delta-rho != 0 mode (6); Euler coefficient (5); G_eff and tensor-block stationarity (original target).

## Special instructions for the gatekeeper
- The gaps are for the Weyl (W) coefficient on delta-rho = 0 plane waves about constant (A)SD Theta-bar only. Do not read them as G_A = G_T or as information on G_eff.
- The "completed = Wald" statement is by construction (cross-term rule); the independent content is the Dirac lemma and the plane-wave gaps.
- Re-run `tt_gap.py`, `content_scan.py`, `dirac_lemma_symbolic.py`. The `omega_riemann_full` rank was computed from `omega_riemann_full.pkl` with `omega_riemann_rank.py`.
- Check that "Euler-density invisible" and the 33-vs-20 statement stay scoped to the first jet fixed.
