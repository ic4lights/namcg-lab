# Proposal 035-connection-entropy, round 1

## Result
Bounded, conditional, non-closing. Hypotheses: those of 029-033 (Poisson limit, one loop, alpha=1, completed replica with Omega_delta and uniform E_delta, totally geodesic Sigma, first order in 1-n, plane-wave modes with delta-rho=0 about constant (A)SD Theta-bar, W coefficient only), plus the classes named below.

1. **B-R1 (independent connection, Lorentz-Lie Noether charge).** The tau-Omega term is quadratic in the bundle curvature, so its cross term with a delta Omega_delta = 2 pi (1-n) H delta_Sigma dx1^dx2 is kappa_X tr(H Omega_12) (24 pi units; normalisation fixed by the 033 gap 2-n_D at H=J_12, reproduced). The Jacobson-Mohd charge Q = -kappa n^{ab} ^ dL/dOmega^{ab} (regular frame, momentum map trivial because there is no Chern-Simons term) is this cross term with H = J_12 and no other generator, because the Killing binormal lies only in the normal plane. Result: it reproduces kappa_X tau_Omega exactly. It is linear in Omega^{12}_{12}, assigns -2 kappa_X to the W coefficient, and does not supply the missing 2 kappa_X. If the internal so(4) is not tied to the frame (pure internal gauge field) the charge at xi=0 vanishes and the assigned W coefficient is 0 (gap 4 kappa_X). Dong/Camps K^2 terms: the contortion-like mixed components of the bundle connection need not vanish on a totally geodesic Sigma, but K^2 is O(amplitude^2) and cannot change the O(amplitude) W coefficient.
2. **B-R2 (composite Omega = Omega[Theta]).** The delta part of any curvature with codimension-2 support is H delta^2 dx1^dx2 with H the holonomy, here H = flux of grad(delta Theta_{mu nu}) through a small circle. Exact computation for Theta^{12}=e^{-l1}, Theta^{34}=e^{-l2} (`diag_family_holonomy.py`): Omega_12,delta = 2 pi (1-n)(c_a J_12 + c_b J_34), R_1212 = -2 pi eps c_a, R_{a3a3}=R_{a4a4} = -pi eps c_b. Cone angle fixes c_a=1; c_b is a free profile datum and makes the Sigma metric singular at O(eps) unless c_b=0. On the modes, tr(J_34 Omega_12) = +2W - R_Sigma (SD) or -2W + R_Sigma (ASD) (`pairing_modes.py`). So the Omega^2 part reaches -4 kappa_X in W only for H = J_12 - chi J_34 (chirality opposite to Theta-bar, chi=+1 SD). With all deltas in the weighted a_2 cross term (`metric_delta_pairing.py`; reproduces 033 gap 2-n_D at c_b=0):
   gap = N_tot(c_a/10 - c_b/15 - 1/10) + kappa_X(4 - 2 c_a + 2 chi c_b) -> with c_a=1: -N_tot c_b/15 + 2 kappa_X (1 + chi c_b).
   The kappa_X part closes at c_b = -chi, but then the N_tot part is nonzero (the warp deltas spoil the metric Wald matching), and the required c_b is chirality-dependent and content-dependent (c_b = -2 kappa_X/(2 chi kappa_X - N_tot/15)). Matrix structure does not force c_b: it is free profile data. No content-independent profile closes the gap in the diagonal family. Special case c_b=-1 (rho regular, c_a+c_b=0): on SD Theta-bar the kappa_X gap closes and N_tot/15 remains; on ASD gap = N_tot/15 + 4 kappa_X. Not fitted; reported as a map.
3. **B-R3 (R_Sigma residue).** On the 17 totally geodesic sampled points (all 033 families; `tau_decomposition.py`, rank 5, exact): tau_Omega = R_Sigma - 2W + (a_1^v - X'/2), a_1^v = 2R/3 - 4e + X'. So the explicit R_Sigma term has universal coefficient 1 (Gauss-Bonnet density of Sigma, topological after integration over closed Sigma), the W term is the Levi-Civita one, and all non-metric content of tau_Omega is in the Lambda^2-order densities (a_1, X'), which are genuine non-topological densities. In the completed coefficient the R_Sigma coefficient is kappa_X - N_tot/30 = alpha_Rsig(comp) of 033 (matches the Levi-Civita/Wald a-type value; no a-type gap in the completed replica). In the fixed-state replica the extra -tau_Omega gives a content-independent Euler offset -R_Sigma plus (3/2)a_1^bos - ... X'-type non-topological terms; the 029 proportionality sigma_log = R_Sigma/12pi holds only where X' = 3g/2 with g = 2R_Sigma, i.e. is family-specific. Classification: R_Sigma part Euler-type (a-type); the gap 2 kappa_X is c-type (Weyl), carried by the mixed-chirality (Ricci-like) block of Omega which doubles for the composite connection. The statement that the T-side Euler coefficient equals the Levi-Civita value rests on Chern-Weil (Euler form of any SO(4) connection on V=TM differs from E_4 by an exact form) and is not verified here beyond the Sigma-side match.
4. **Forks (ranked, open).** (i) other delta classes: off-diagonal equivariant Theta (Burgers/vortex parts give delta' terms; dipole pairing with R_{a3bc}); (ii) non-chiral Theta-bar and delta-rho != 0 modes; (iii) edge-mode/contact terms of the connection sector shifting the Omega coefficient (Donnelly-Wall type) specifically by -2 kappa_X W; (iv) the composite functional's entropy from a smooth-cone replica rather than the cross-term rule (exact AB heat trace, |1-n| terms, n>1); (v) O(h^2) Dong K^2 with contortion K; (vi) finite-n/fixed-state versions of the gap 4-n_D.

## Target and status
Problem B (sec:status-B): Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL. Original target: derive tensor-block stationarity and the area/G relation. Not supplied. No discrepancy among Appendix H, Chapter 17 and the ledger found. Critical set per current agenda A, B, C, D1, E, F, G-derived, N; unchanged.

## Source reading
Digest + targeted reads (digest stale: dirty-chapters from accepted 032/033 integrations, expected). Read in full: appH lines 41-274 (Problem B including 029/031/033 blocks), 033 review-r2 and proposal-r2, SME scout 20261018, 033 scripts geom.py, lin_lib.py, tt_gap.py, sector_data.py, 031 smooth_family_deltas.py. Not a full scan. Literature: Jacobson-Mohd (arXiv 1507.01054, PRD 92, 124010, DOI 10.1103/PhysRevD.92.124010) and Elgood-Ortin-Perenniguez (arXiv 2012.14892, JHEP05(2021)110, DOI 10.1007/JHEP05(2021)110) records verified via arXiv and Crossref (authors, journal; the SME's "Meessen" is wrong, authors are Elgood, Ortin, Pereniguez). Equation numbers (46-49, 6.1, 6.2, 7.3) were NOT re-read; I rely on the abstract-level statement that the charge is the combined diffeo+Lorentz Noether charge, and derive the cross-term structure myself. Hung-Myers-Smolkin and Frolov-Fursaev not opened; not used. No BibTeX proposed; the insert cites nothing.

## Research and reasoning
- Cross-term rule: delta a_2 = (1/360) tr[... + 60 Omega^{mu nu} Omega_delta,mu nu + 4 Riem.Riem_delta - 4 Ric.Ric_delta + ...]; on the modes R, E^(1) vanish. 24 pi sigma = 3 N_tot Phi_metric + kappa_X tr(H' Omega_12), Phi_metric = (1/90)[(c_a-c_b) R_ijij - c_a K - c_b P]. The factor 3 and the unit of H' are calibrated against the scalar periodic value -(1/30)(R_Sigma - 3W) and the 029 tau-Omega weight; the c=(1,0) output reproduces the 033 completed gap 2-n_D for both chiralities (non-trivial check).
- Holonomy argument: b_sigma = Theta-bar^{rho sigma} d_rho delta Theta, so the circulation is the flux of the normal derivative of delta Theta_{mu nu}; the exact symbolic result confirms it.
- Why independent-connection Noether gives only J_12: lambda_xi = grad xi is a rotation in the normal plane (regular frame), so n^{ab} has no J_34 component; the Euler density's charge would be the swapped pairing tr(J_34 Omega_34).
- The independent connection is an auxiliary bookkeeping variable; spacetime is emergent; no background metric is introduced.
- No-go hypothesis list and relaxations are in Result item 4.

## Claim classification
| Claim | Class |
|---|---|
| B-R1: Noether charge = kappa_X tau_Omega (H=J_12) | established (algebra), given the tied-frame hypothesis |
| untied internal group gives zero charge | established (standard), conditional on that hypothesis |
| H = c_a J_12 + c_b J_34 and the Riemann deltas for the diagonal family | established (symbolic, all orders, `diag_family_holonomy.out.txt`) |
| tr(J_34 Omega_12) = -+(2W - R_Sigma) on SD/ASD modes | numerical-exact (8 modes each) |
| gap(c_a,c_b) formula | conditional on applying the cross-term rule to warp deltas (extension of the cone rule, not derived) |
| no content-independent profile closes the gap | conditional, diagonal family only |
| tau_Omega = R_Sigma - 2W + a_1^v - X'/2 | numerical-exact at 17 totally geodesic points, not proved |
| T-side Euler coefficient = Levi-Civita value | conjecture (Chern-Weil argument sketched, not verified) |
| which holonomy the matrix state selects | unresolved |

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`: insert the block of `proposals/035-connection-entropy/appH_insert.tex` (3 paragraphs-worth, one `\paragraph`) after the 033 paragraph and immediately before `\section{Problem C: conformal mode and Cassini}` (line 275, unique). The closing sentence "Problem~B stays open and PROGRAMME-CONDITIONAL." occurs twice in the file (031 and 033 paragraphs), so the anchor is the `\section{Problem C` line, not that sentence; one blank line before the insert. Nothing replaced. No `\label`/`\ref`/`\cite` added. Scratch compile outside the repo (article, amsmath/amssymb): 0 errors; build products deleted. 0 TAB, ASCII only, LF (integrator converts to CRLF). `\mathcal J`, `\epsilon`, `\operatorname` standard.

## Verification scripts
In `proposals/035-connection-entropy/`: `pairing_modes.py` (+`.out.txt`): tr(J_ab Omega_12) on SD/ASD modes, tau_01 = -R_ijij; `metric_delta_pairing.py` (+out): gap(c_a,c_b), c=(1,0) reproduces 2-n_D; `diag_family_holonomy.py` (+out): exact Omega_12 and Riemann deltas for the diagonal family; `tau_decomposition.py` (+out) with `data.json` (copied from 033): tau decomposition; `lin_lib.py`, `lib.py` copied from 033. Generators J_13 etc. in pairing_modes output do not fit (W,R_Sigma): not SO(2)-scalars, excluded by equivariance.

## Decisions Taken
- Treated B-R1 as an equivalence statement (cross term = Noether charge) rather than a new term; favours a clean conditional record over an inflated claim.
- Extended the cross-term rule to warp deltas to test B-R2, flagged as an extension; chose the diagonal equivariant family because it is the exact computable class and contains the 029 cone.
- Did not add Chern-Weil claims to the manuscript block.
- Rejected fitting c_b to the target.

## Milestone assessment
Routine. A precise bounded obstruction and classification; no critical-path step derived. Not a breakthrough.

## Status-label recommendation
None. Problem B remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; A, C, D1, E, F, G-derived, N unaffected.

## Author decision needed
none

## Remaining open step
Select the holonomy/delta content of the Poisson cone from the matrix state (off-diagonal classes, non-chiral Theta-bar, delta-rho != 0, smooth-cone replica) and decide whether edge/contact terms supply -2 kappa_X W; derive the T-side Euler coefficient globally. The tensor-block stationarity and G relation remain untouched.

## Special instructions for the gatekeeper
Do not accept as stated: any claim that c_b is selected by the matrix model, that Chern-Weil fixes the T-side a-type coefficient (conjecture), or the literature equation numbers (not re-read). Re-check: the c=(1,0) reproduction of 2-n_D, the exact diag-family output, the cross-term extension to warp deltas, and that the anchor is the `\section{Problem C` line (the status sentence is not unique). Scope: diagonal family, completed replica, W coefficient, first order. No closure claimed.
