# Proposal 029-cone-log-coefficient, round 2

## Changelog (r1 to r2; review-r1 AWRR, OPEN 0/2, no PRIOR-CLAIM-ERROR)
- F1 (major): appended the review's scoping sentences to paragraph 1; stated that the mismatch is for the fixed-state replica only, is about coefficients and not G_eff; smooth replica gives zero on both sides; state selection not derived; contact and edge-mode terms (not included) shift the R_Sigma coefficient and could cancel the difference.
- F2 (major): replaced "-sigma_3 2 pi a delta" by the convention-free "spin term gamma^{12} Omega_12 of (gamma^mu D_mu)^2, Omega_12=[D_1,D_2], whose part supported on Sigma is attractive in the component where it is positive"; tau_Omega is defined with the same Omega. The weight -(1/2) S_2 tr(gamma^{12} Omega_12) is unchanged. (In the research text below, "(gamma D)^2 = D^2 - sigma_3 F_12, delta -sigma_3 2 pi a" was a convention-dependent intermediate; with D = d - iA, sigma_3 = -i gamma^{12}, Omega=-iF the Pauli term is +sigma_3 F and the delta is +sigma_3 2 pi a delta; the final formula is convention-free.)
- F3: renamed calT -> tau_Omega, calS -> sigma_log in the block (r1 research text below keeps the old names).
- F4: defined R_ii, R_ijij, R_Sigma = R - 2R_ii + R_ijij (totally geodesic).
- F5: a = 11/360 cited as an input: Eq. (275) of Solodukhin2011, after Duff, not re-derived.
- F6: single closing sentence "Problem B remains open and PROGRAMME-CONDITIONAL."
- F7: flat_landau_ab.py last print relabelled (now prints -S_2, matching tot) and states that the attractive-channel assignment is an input checked by hand; output regenerated.
- appH_insert.tex equals the block below exactly. Anchor re-verified unique (see Proposed changes). Compile check: scratch copy outside the repo, 0 errors (stub: \cite stubbed, \LUV defined).
- "Remaining open step" replaced by the review's ranked avenues.

## Result
Target: Problem B (with A, F): the A-side (replica/cone) logarithmic coefficient at the IKKT content (N_s, n_D) = (6, 2), the counterpart of 026's T-side zero. A conditional structural result. It closes nothing.

1. **Reduction (established, exact in the class).** The fixed-state replica pulls the same background back to every sheet, so Tr rho^n is a sum over Z_n twist phases e^{2 pi i k/n} of the single-sheet problem with a flat flavour vortex of flux a_k = k/n at Sigma (bosonic k integer; Dirac k = -(n-1)/2..(n-1)/2). This gives an exact, regular, n-analytic description (the sums are Bernoulli power sums, analytic in n) for the fixed-state replica with the less singular Dirac extension. The non-analytic index |n-1|/(2n) of 024 belongs to the singular-rho (smooth) cone and is not involved.
2. **Omega-term (derived; checked against exact spectra).** For periodic twists the bundle-curvature term is -B_3(a)/3 times tr(i Omega_12) per component, and sum_k B_3(k/n) = 0 (multiplication theorem). For Dirac blocks the spin-delta term -sigma_3 2 pi a delta of (gamma D)^2 plus the less singular extension gives, after the symmetric sum over k,
 T_1^Omega = -(1/2) S_2 tr(gamma^{12} Omega_12), S_2 = sum_k a_k^2 = (n^2-1)/(12 n),
 and E-linear weight -(1/2) c_B per component (the +1/3 Dirac area coefficient). Verified in `flat_landau_ab.py` against the exact Landau-Aharonov-Bohm tower sums (C_1 = a(a-1)/2, linear coefficient -B_3(a)/3, flagged-channel shifts a and -a^2 / b and +b^2, S_2 for N = 1..5, dS_2/dn = 1/6).
3. **Assembly.** With eq (70) of Solodukhin for scalar-type components and the Dirac a = 11/360 as the geometric input at first order in n-1,
 24 pi S = (4/3) R + 2 R_ii - 2 R_ijij + 2 W - 12 e + (3/2) X' - T,
 (`assemble_check.py`; symbolic). On SD/ASD backgrounds (W = 0, e = R_G/6): 24 pi S = (3/2) X' - T.
4. **On the rotation-invariant SD example** (three points of Sigma, exact rationals, `a_side_sd.py`), (3/2) X' - T = 2 R_Sigma = -(4/3) R_G, so S = R_Sigma/(12 pi): the pure-curvature terms cancel and a nonvanishing Euler-type density of Sigma remains. The T side (coefficient of ln Lambda in the induced action, proportional to integral rho^2 S_4) is zero there, as is the first variation of integral rho^2 S_4 along the smooth replica (S_4 >= 0 vanishes). So the fixed-state replica shows a G_T versus G_A mismatch at log order on these backgrounds, parallel to c_A = 2 versus c_T = 0 at Lambda^2. The identity (3/2) X' - T = 2 R_Sigma is observed at three points, not proved.

Not claimed: any statement for the first-order smooth replica beyond the vanishing above; edge modes; finite terms; non-chiral J = 0 backgrounds numerically (general formula only).

## Target and status
Problem B (`sec:status-B`): OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; ch17 critical set A, B, C, D1, E, F, G-derived, N. Original target: derive fixed-volume stationarity of the tensor block, the area term and its relation to the emergent metric. This package addresses the G_T versus G_A comparison at logarithmic order (026 avenue 2). Dependencies A, F, C, D1. Classification: PROGRAMME-CONDITIONAL. No discrepancy found.

## Source reading
Digest + targeted reads (digest reported STALE because of the dirty tree, accepted by instruction). Read in full: appH `sec:status-B` (015-026 text), 026 proposal-r2 and review-r2, SME scout `second-variation-20261017` (R-B2). Not read: other chapters; no full-scan claim. Literature (downloaded PDFs, text extracted with pdftotext): Solodukhin 1104.3712 Eq. (70), (82), (126), (136)-(137) read and the sphere check done (below); Fursaev-Miele hep-th/9605153 (abstract and Sec. 2: only the first coefficient A_1, i.e. the area term, for spins 1/2, 1, 3/2, 2; no a_2^Sigma for spinors); Bianchi et al. 2104.01220 (title/abstract/contents only: monodromy defects of conformal scalars and Dirac fermions, defect central charges; not used quantitatively); Hanisch-Pfaeffle-Stephan and Pfaeffle-Stephan not opened. No new BibTeX; keys `Solodukhin2011`, `FursaevMiele1997`, `CasiniHuerta2009` exist.

## Research and reasoning
**(a) Replica as vortex sum.** For integer n, Psi_j(theta) = Psi(theta + 2 pi j) on the n-cover, diagonalise the cyclic matrix: Phi_k(2 pi) = e^{2 pi i k/n} Phi_k(0) on one sheet, exact because the background is identical on every sheet. For the vector and ghost sectors the Cartesian gluing is unrotated, so the phases are common (scalar-type). For Dirac the Cartesian components carry the common factor (-1)^{n+1}, giving k half-shifted, as in 019. The conical singularity of G is thereby traded for a flat U(1) vortex on a smooth sheet; no use is made of the cone metric.

**(b) Dimension counting.** The s^0 surface term has dimension two on Sigma: R, R_ii, R_ijij, tr E, and the linear bundle term tr(Omega_12-weighted). E and Omega enter only linearly. E is linear by Duhamel; for the Omega term the flat model is a uniform field B with flux a: H_m = -d_r^2 - r^{-1} d_r + (l/r - B r/2)^2, l = m - a, exact levels B(2k + 1 + |l| - l). First order in B gives T_1/B = sum_m l_m F(nu_m), F = -nu/2 (finite part of the Bessel integral), which is -B_3(a)/3 for the regular domain. `flat_landau_ab.py` confirms C_1 and the linear term from the exact tower sums with the flux-dependent cutoff shift.

**(c) Dirac.** (gamma D)^2 = D^2 - sigma_3 F_12 with sigma_3 = -i gamma^{12}; the attractive channel (sigma_3 a > 0) takes the reversed Bessel order, joining the lowest tower: flagged shifts (const, linear) = (|a|, -a|a|). Summing over the symmetric set a_k, the block traces cancel except for tr(sigma_3 i Omega): sum_k sigma flag (-a|a|) = -S_2 (checked N = 2..5). Hence T_1^Omega = -(1/2) S_2 tr(gamma^{12} Omega_12) and T_1^E = -(1/2) S_2 tr E. For the Levi-Civita spin connection, tr(gamma^{12} Omega_12) = -2 R_1212, so the spin-curvature coupling is nonzero: the claim "Omega-terms vanish" holds for the periodic sectors only. This is the Omega-dependent piece asked for in target 1; no published a_2^Sigma contains it (Fursaev-Miele treat only A_1).

**(d) Geometric part of the Dirac term.** Written as T_1(torsionful) = T_1(Levi-Civita) + L_E[E_f - R/4] + L_Omega[Omega_f - Omega_LC], with the Levi-Civita term taken at first order in n-1 from the universal Dirac log coefficient a = 11/360 (sphere -11/90; for W != 0 also c = 1/20, not needed on SD). Per Dirac field: Delta S_D = -(1/48 pi)[tr E_f - R + T + R_ijij]. Scalar-type: S_B = (1/24 pi)(R/6 - E) - Q/(720 pi), Q = R_ii - 2 R_ijij.

**(e) Checks of eq (70).** `assemble_check.py`: c_B' = -2 pi/3, d_B' = pi/45 reproduce S_B; for the conformal scalar on S^4 branched along a great S^2 the coefficient of ln Lambda is -1/90 = -4a with a = 1/360 (this tests d_B). The structure R_ii - 2 R_ijij = R_Sigma - 3 W has a : c = 1 : 3, as for the scalar. Dirac: a = 11/360 is an input, not a check.

**(f) Evaluation.** `a_side_sd.py` uses the 026 library (copied) for Dirac/vector/scalar data on the SD example, Sigma = {x1 = x2 = 0}: e = R/6 and W = 0 verified; X' and T = tr(gamma^{12} Omega^chart_12) G^{11} computed from the library Omega; result in item 4.

**Hypotheses of the result and relaxations (no-go-is-a-fork).** H1 Sigma totally geodesic (fixed plane of an isometry) - relax: K terms (Dowker; need extrinsic-curvature coefficients). H2 fixed-state replica with less singular extension - relax: singular-rho cone (non-analytic, branches of 024), componentwise-regular domain, intermediate flux f (c_A(f) = c_A - f(N_s+2)/4 gave 2 - 2f; log analogue not computed). H3 geometric Dirac part from a = 11/360 and eq (70) - relax: independent spindle spectra. H4 contact/edge terms of the vector (Kabat/Donnelly-Wall) and Dirac edge modes absent - relax: add them; they change the R_Sigma coefficient. H5 antiperiodic gluing from a quasi-free state with rotational modular flow - relax: periodic gluing (which gives a different weight). H6 one loop, alpha = 1, Yukawas dropped. What each gave: H2 smooth replica gives 0 = 0; fixed-state gives the Euler density; H4 not explored.

## Claim classification
| Claim | Class |
|---|---|
| Replica = Z_n sum of vortex problems; analytic in n for fixed-state | established (exact, in class) |
| Omega term periodic sectors: -B_3/3, sums to zero | established (exact Landau-AB sums) |
| Dirac Omega and E weights, S_2 | established (exact sums; the extension is an assumption: conditional) |
| Geometric Dirac part from a = 11/360 | input |
| eq (70) | input, partially checked (sphere) |
| 24 pi S formula | conditional on inputs |
| (3/2)X' - T = 2 R_Sigma on SD example | numerical-exact at three points; not proved |
| G_T != G_A at log order for fixed-state replica on SD | conditional |
| smooth replica S = 0 on SD | established given S_4 >= 0 and 026 |
| state, extension, edge modes, G_eff | unresolved |

## Proposed changes
One file `chapters/appH-microscopic-proofs.tex`. Anchor: the paragraph "Next order at N_s = 6, n_D = 2 ..." (026), whose last sentence is "They compute no logarithmic coefficient of the cone (area) side ... Problems~B, C, D, F and~G remain open." (the substring "no logarithmic coefficient of the cone (area) side" occurs once, checked); insert after that paragraph, before `\section{Problem C: conformal mode and Cassini}`. Nothing replaced. Stale: that 026 sentence ("compute no logarithmic coefficient of the cone side") stays true of the 026 block itself; no edit. Labels used: none new, no `\ref`. Citation `Solodukhin2011` exists. The block equals `appH_insert.tex` and compiles in a stub document outside the repo (0 errors; `\cite` unresolved only in the stub).

```latex
\paragraph{Cone logarithmic coefficient at \(N_s=6\), \(n_D=2\) on the fixed-state replica (conditional; not closure).}
Keep the setting of the preceding paragraph and the fixed-state replica with antiperiodic Dirac gluing and the less singular extension. Let \(\Sigma\) be the fixed plane of a rotation under which \(\Theta\) is invariant, so that \(\Sigma\) is totally geodesic for \(G\). With unit normals \(n_i\) to \(\Sigma\), write \(R_{ii}=R_{\mu\nu}n^\mu_in^\nu_i\) and \(R_{ijij}=R_{\mu\nu\rho\sigma}n^\mu_in^\nu_jn^\rho_in^\sigma_j\) (sums over \(i,j\)), and \(R_\Sigma\) for the intrinsic scalar curvature of \(\Sigma\), so that \(R_\Sigma=R-2R_{ii}+R_{ijij}\) for totally geodesic \(\Sigma\). The pulled-back background is the same on every sheet, so \(\operatorname{Tr}\rho^n\) is the sum over the twist phases \(e^{2\pi\mathrm ik/n}\) of the single-sheet problem with a flat flavour vortex of flux \(a_k=k/n\) at \(\Sigma\) (integer \(k\) for the bosonic sectors, \(k=-\tfrac{n-1}2,\dots,\tfrac{n-1}2\) for the Dirac fields). For a Laplace-type sector \(-\nabla^2+E\) the \(s^0\) surface term is linear in the dimension-two data. For a component with a periodic phase it is the scalar term of Equation~(70) of~\cite{Solodukhin2011}, \(c_B(n)\operatorname{tr}(\tfrac R6-E)+d_B(n)(R_{ii}-2R_{ijij})\) with \(c_B=\tfrac\pi3\tfrac{1-n^2}n\) and \(d_B=-\tfrac\pi{180}\tfrac{(1-n^2)(1+n^2)}{n^3}\), and it has no term in the bundle curvature, because every periodic twist acts as a common phase and the sum of the Bernoulli polynomials \(B_3(k/n)\) in the linear coefficient vanishes. For a Dirac field the common phase is accompanied by the spin term \(\gamma^{12}\Omega_{12}\) of \((\gamma^\mu D_\mu)^2\), with \(\Omega_{12}=[D_1,D_2]\), whose part supported on \(\Sigma\) is attractive in the component where it is positive; the less singular extension then gives the \(E\)-linear weight \(-\tfrac12c_B\) per component and a term \(-\tfrac12\sum_ka_k^2\operatorname{tr}(\gamma^{12}\Omega_{12})\) with \(\sum_ka_k^2=(n^2-1)/(12n)\) and \(\Omega_{12}\) the bundle curvature in the normal plane (from the exact Landau--Aharonov--Bohm spectrum; the terms odd in \(a\) cancel in the symmetric sum over \(k\)). The remaining geometric part of the Dirac term is fixed at first order in \(n-1\) by the value \(a=11/360\) of the Dirac field (Equation~(275) of~\cite{Solodukhin2011}, after Duff; not re-derived here), which gives \(-\tfrac{11}{90}\) for a sphere. With one proper-time limit, the coefficient of \(\ln\LUV\) in the replica entropy is \(\int_\Sigma\sigma_{\log}\), where, with \(X'=-\operatorname{tr}(b_\sigma b^\sigma)\) in the vector sector, \(	au_\Omega=\operatorname{tr}(\gamma^{12}\Omega^{f}_{12})\) the normal-plane curvature of the Dirac connection, with the same \(\Omega_{12}=[D_1,D_2]\), \(e\) the scalar endomorphism of the preceding paragraph and \(W=W_{ijij}\) the Weyl projection,
\[
  24\pi\,\sigma_{\log}=\tfrac43R_G+2R_{ii}-2R_{ijij}+2W-12\,e+\tfrac32X'-\tau_\Omega .
\]
On the self-dual and anti-self-dual backgrounds, \(W=0\) and \(e=R_G/6\), so that \(24\pi\sigma_{\log}=\tfrac32X'-\tau_\Omega\). At three sampled points of \(\Sigma\) for the rotation-invariant self-dual example above this equals \(2R_\Sigma\), twice the intrinsic curvature of \(\Sigma\) (exact rational arithmetic; not proved), so that \(\sigma_{\log}=R_\Sigma/12\pi\). The cone logarithmic coefficient is then an Euler density of \(\Sigma\) with nonvanishing local value. The coefficient \(\propto\int\rho^2\mathcal S_4\) of the induced action vanishes on these backgrounds, and so does the first variation of \(\int\rho^2\mathcal S_4\) along the smooth replica, because \(\mathcal S_4\ge0\) vanishes there. The two sides therefore differ at logarithmic order, as coefficients, for the fixed-state replica on these backgrounds; this is a statement about the fixed-state replica only and not about \(G_{\mathrm{eff}}\). The first-order smooth replica of the preceding paragraphs gives zero on both sides, and which replica the matrix state selects is not derived here. Contact and edge-mode terms of the connection and Dirac sectors, which are not included, shift the coefficient of \(R_\Sigma\) and could cancel the difference.

These statements are for the Poisson-limit operators, the Euclidean section, one loop, \(\alpha=1\), \(N_s=6\), \(n_D=2\), the totally geodesic \(\Sigma\), the fixed-state replica and one common proper-time limit. They use Equation~(70) of~\cite{Solodukhin2011} and the Dirac coefficient \(a=11/360\) as inputs, do not treat finite terms, edge modes, other extensions, higher orders in \(n-1\), or the non-self-dual \(\mathfrak J=0\) backgrounds beyond the general formula, and give no value or sign of \(G_{\mathrm{eff}}\). Problem~B remains open and PROGRAMME-CONDITIONAL.
```

## Verification scripts
In `proposals/029-cone-log-coefficient/` (outputs `*.out.txt`; libraries copied from 026: jetlib, geom, lib, common, sd_family):
- `flat_landau_ab.py`: exact Landau-AB tower sums: C_1, linear B coefficient, Dirac flagged-channel shifts, S_2 for N = 1..5, dS_2/dn.
- `assemble_check.py`: c_B', d_B', S_B normalisation, scalar sphere -1/90, symbolic 24 pi S and its SD reduction.
- `a_side_sd.py`: sector data on the SD example at three points of Sigma; e = R/6, W = 0, and (3/2)X' - T = 2 R_Sigma.
These are checks, not proofs. Note: a Python `__pycache__` may exist in the folder.

## Decisions Taken
1. Chose the Z_n flavour-vortex description over the cone-with-spin description (exact, n-analytic, makes the Omega coupling explicit).
2. Used a = 11/360 as the geometric Dirac input rather than a new spindle computation; spindle x R^2 and S^4 branched spectra are queued as the independent check.
3. Restricted to totally geodesic Sigma and SD backgrounds for the evaluation; the formula is stated generally.
4. Smooth replica treated through 026 (S_4 >= 0 has zero first variation); no new regularised-cone computation.

## Milestone assessment
M2-type (bounded structural result plus mismatch at log order, conditional on two literature inputs). Not a breakthrough: the result is a mismatch for the fixed-state replica, nothing is closed, and the key identity is checked at three points only.

## Status-label recommendation
None. A, B, C, D1, E, F, G-derived, N remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Author decision needed
None. Spacetime stays emergent (G, rho, b built from Theta).

## Remaining open step
Not derived: stationarity of the tensor block, map to the emergent metric, any value or sign of G_eff, which replica the matrix state selects. Ranked open avenues:
1. Edge-mode and contact terms (H4): Kabat vector contact (-1 in the 024 units), Dirac edge modes, Herzog-Nishioka-type terms. Compute whether they shift the R_Sigma coefficient enough to cancel 2R_Sigma; most likely site of G_A = G_T.
2. Prove (3/2)X' - tau_Omega = 2R_Sigma on self-dual backgrounds (Weitzenboeck identity); evaluate on the non-BPS d(h Lambda^3) family (needs c = 1/20, W != 0).
3. Log analogue of the intermediate-flux replica c_A(f), and the smooth replica's own log coefficient beyond the S_4 >= 0 argument.
4. Independent spindle-spectra check (S^2_n x R^2, branched S^4) of the Dirac geometric part and of the sign of the Omega term.
5. Relax H1: non-totally-geodesic Sigma with extrinsic-curvature terms.
6. Rotated-gluing vector branch of 024 (non-analytic at n=1).
7. The a_3 Kaluza-Klein route of 026.

## Special instructions for the gatekeeper
- Do not read the result as G_T != G_A in general: it is for the fixed-state replica, totally geodesic Sigma, SD example, with inputs eq (70) and a = 11/360.
- Re-check: sign of the Dirac Omega term (flat check fixes it; Levi-Civita relation tr(gamma^{12}Omega_12) = -2 R_1212 is algebra), the use of one reflection-symmetric k set, the claim that periodic sectors have no Omega term, and the 24 pi S bookkeeping in `assemble_check.py`.
- Solodukhin Eq. (70)/(82) read in the extracted PDF text (Greek letters lost in extraction; structure matches the scout quote) and sphere-checked; a = 11/360 and c = 1/20 are standard values not re-derived here.
