# Proposal 031-edge-contact-log, round 1

## Result
Target: Problems B and A, the logarithmic area-side coefficient at (N_s,n_D)=(6,2) with contact and edge terms. Conditional; closes nothing.

1. **Calibration (established by script).** The Fursaev-Solodukhin delta cross-term rule (Solodukhin 1104.3712 Eqs. (55)-(59), read in the PDF) applied to the a_2 coefficient reproduces Eq. (70) for smooth E, and for the Hodge Maxwell operator (E_delta = Ricci delta, Omega_delta = 2 pi (1-n) J delta) gives (1/pi)[-(31/360) R_Sigma + W/20]: ratios 62 and 12 to the conformal scalar, and -62/90 on S^4/S^2 (= M0 -122/90, Ricci delta +1, Riemann delta -1/3). The Kabat/Donnelly-Wall contact at log order is -(R_Sigma - R_ii)/(24 pi); its -R_Sigma/(24 pi) part is the DW edge density (DW Sec. VII, Eqs. (82), (97)-(98), read). `delta_completion_calibration.py`.
2. **Dirac weights checked.** Demanding the Dirac a=11, c=6 and Weyl covariance fixes (x,y,z)=(-1/2,1,1/2), exactly the 029 Z_n values. So a=11/360 is an output, not a separate input. `dirac_anomaly_check.py`.
3. **Correction of the scope of 029's example.** On the rotation-invariant SD family (random polynomial data, 18 exact points, not proved): X'=(3/2)g, tau_Omega=R_Sigma+(3/4)g, g=|grad_Sigma ln rho|^2, so 24 pi sigma_fs=(3/2)g-R_Sigma. "Euler density" holds only where g=2R_Sigma (the 029 example). The identity (3/2)X'-tau=2R_Sigma fails for generic members. `rot_family_fit.py`, `general_sd_identity.py`.
4. **Origin of the fixed-state value.** With all sectors periodic and no deltas the coefficient vanishes for every Poisson bivector at (6,2) (N_tot=0, weighted a_1=0). sigma_fs is exactly (antiperiodic - periodic) Dirac. `dirac_anomaly_check.py`.
5. **Contacts of the smooth family, computed.** On Theta^{12}=1/f, Theta^{34}=1 (021 family), scalar, connection and Dirac data contain (1/2) Lap_0 ln f with the same coefficient in all components: E_delta = -pi(1-n) delta_Sigma uniformly (the Q=1/4 contact of 021), and the connection curvature Omega_12 contains +2 pi (1-n) J delta_Sigma (J rotation of the internal normal plane). `smooth_family_deltas.py`.
6. **Cancellation.** With C_b = log cross term of that uniform E_delta on the 8 bosonic components and C_Omega = tr(J Omega^v_12)/(24 pi): 24 pi(sigma_fs + C_b) = -tau_Omega identically (weights, N_tot=0), and tr_V(J Omega^v)=tau_Omega for any so(4)-valued connection ((1/2,1/2) vs (1/2,0)+(0,1/2)). Hence sigma_fs + C_b + C_Omega = 0, verified at random generic closed omega (non-chiral, J != 0; `identity_general_jets.py`), on the SD family (`contacts_summary.py`) and on the non-SD J=0 family d(h Lambda^3), W != 0 (`nonsd_total.py`). On the 029 example C_b + C_Omega = -R_Sigma/(12 pi) exactly: the answer to the question posed. Neither E_delta alone (-3R_Sigma/16pi) nor Omega_delta alone (5R_Sigma/48pi) does it. A Herzog-Nishioka term removing E_delta (HN Eqs. (7.1)-(7.2), (5.20), read) leaves 3g/(32 pi). Trace-uniform and Hodge (normal-block) E_delta coincide on J=0 families, differ for generic jets.
7. **Edge modes proper.** Generalising DW (Sec. VI A) to a totally geodesic Sigma with coupling w(x) gives S_edge = -(1/4pi)(R_Sigma/6 - (1/2)Lap ln w - (1/4)|grad ln w|^2) (heat check `edge_heat_check.py`; a_1 of -w^-1 div(w grad) verified symbolically and on a torus). With w = rho^-1 (from the Poisson-limit action: rho K K F F, sqrt G = rho^2) sigma_fs + S_edge != 0 for every w=rho^k (g coefficient (1+k^2)/16 pi > 0). So the DW edge entropy of the symplectic U(1) does not cancel; the cancelling object is the geometric contact (E_delta, Omega_delta), not equal to DW's edge density. Caveat: axion-type coupling (on SD backgrounds the quadratic action involves only F^-) is not treated; the gradient coefficient is uncontrolled, the Euler part -chi/6 is not.
8. Ghost: scalar operator, no delta. Dirac: no gauge freedom, no edge mode; adding FS deltas on top of the Z_n result would double count (periodic+FS deltas reproduces only the R_ii, R_ijij anomaly coefficients, not R).

## Target and status
Problem B (sec:status-B): OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; A: OPEN, CRITICAL PATH. Chapter 17 critical set A,B,C,D1,E,F,G-derived,N (as in 029; not re-read in full this round). Original target (B): derive tensor-block stationarity and the area term/G relation. This package supplies none of it; it locates the missing log-order ingredient (conditional G_A=G_T at log order for a covariant replica). No label discrepancy found.

## Source reading
Digest + targeted reads (digest stale: dirty tree, accepted). Read: appH lines 142-247 and 1756-1875, 029 proposal-r2/review-r2, 024 proposal-r2, SME scout R-B2/R-B4, MILESTONE.md. Opened PDFs: Donnelly-Wall 1506.05792 (Secs. I, III B-C, IV-VII), Herzog-Nishioka 1610.02261 (Sec. 7, (5.20)), Solodukhin 1104.3712 ((55)-(59), (70), (82)). Fursaev-Solodukhin hep-th/9501127 abstract only (record verified; not cited in the block). Anomaly ratios 62:12 are checked against DW Eq. (85) for a; c=12 relative to the scalar is the standard value, not independently verified. Kabat BH=EE for spinors: abstract only (from 024).

## Research and reasoning
See Result. Key derivation: 24 pi sigma_fs = 2R - 12e + (3/2)X' - tau (general, from the weights; equals 029's expression with W). Bosonic uniform E_delta cross term = -2R + 12e - (3/2)X' (60 R trE_delta + 360 tr(E E_delta), tr E_pos,v = 4e - X'). Sum = -tau. tr_V(J Omega)=tau by representation theory. T side: the 026 log term rho^2 S_4 contains no curvature of G in (G, torsion) variables, so a Wald-type entropy of it vanishes (conditional on that reading); on chiral backgrounds S_4=0 independently.
Hypotheses and relaxations: (i) contacts are imported into the fixed-state class (they are the smooth/torsion reading of 021); relax: done for the smooth family's delta parts; (ii) first order in 1-n, n<1 branch (024: n>1 differs at Lambda^2); open; (iii) non-delta singular first-order parts of the smooth family (b ~ eps/r) not included; (iv) Dirac in the smooth family also carries E_delta, Omega_delta, but its Z_n result already encodes them; (v) totally geodesic Sigma; (vi) Lambda^2: with the same Q contacts on the 8 bosonic comps c_A=0=c_T; with the vector contact alone c_A=1.

## Claim classification
| Claim | Class |
|---|---|
| FS delta rule reproduces eq (70), Maxwell a=62, c=12, sphere -62/90 | established (script) |
| Dirac weights reproduce a, c | established (script) |
| X'=(3/2)g, tau=R_Sigma+(3/4)g on rotation-invariant SD family | numerical-exact, not proved |
| sigma_fs = Dirac(anti - per) | established (algebra) |
| E_delta, Omega_delta of smooth family | established (symbolic, first-order delta parts) |
| sigma_fs + C_b + C_Omega = 0 | established algebra given inputs; checked at generic jets |
| G_A=G_T at log order | conditional on replica prescription and Wald-type T side |
| DW edge density with coupling w | conditional (no axion mixing) |
| matrix state selects this replica | unresolved |

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`. Insert the block of `appH_insert.tex` after the 029 paragraph, whose last sentence is "Problem~B remains open and PROGRAMME-CONDITIONAL." (occurs once, checked) and before `\section{Problem C: conformal mode and Cassini}`. Nothing replaced. 029's sentence "The cone logarithmic coefficient is then an Euler density ..." stays true for the example; the block states the limit. Citation keys Solodukhin2011, DonnellyWall2016, HerzogNishioka2016 exist; no new `\ref`/`\label`; no BibTeX needed. Block compiled in a stub outside the repo (0 errors, `\LUV` defined); 0 TAB bytes (checked with Python).

The block is the content of `appH_insert.tex`.

## Verification scripts
In `proposals/031-edge-contact-log/` (outputs `*.out.txt`): delta_completion_calibration.py; dirac_anomaly_check.py; rot_family_fit.py, general_sd_identity.py, rot_family_identity.py; contacts_summary.py; nonsd_total.py (needs nonsd_family.py, sector_data.py); identity_general_jets.py; smooth_family_deltas.py; edge_heat_check.py; lc_convention_check.py (conventions of Omega, J, E_G fixed against Levi-Civita). Libraries copied from 029. smooth_family_deltas output lists Hessian coefficients; read Omega_12 entries (Omega^1_2=-Lap l, Omega^2_1=+Lap l).

## Decisions Taken
Used first-order FS cross terms (not Bessel) as the log-order contact calculus, because it is calibrated on Maxwell; computed the smooth family's deltas rather than assuming them; reported the DW edge density as a separate, non-cancelling object; reported the Lambda^2 interplay rather than hiding it.

## Milestone assessment
Candidate M1-adjacent (consistency, not derivation): an exact, parameter-free cancellation at log order identifying the missing ingredient (bundle-curvature delta of the connection plus Q contacts), with a self-correction of 029's reading of its example. Imported contacts and the replica selection remain unproved, so I do not claim a breakthrough; gatekeeper decides.

## Status-label recommendation
None. A, B, C, D1, E, F, G-derived, N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
None. Spacetime stays emergent (G, rho, b from Theta).

## Remaining open step
Not derived: stationarity of the tensor block, the replica/state selected by the matrix model, G_eff. Ranked: (1) n>1 branch and non-delta singular first-order terms of the smooth replica; (2) prove X'=(3/2)g, tau=R_Sigma+(3/4)g and the E-distribution equality; (3) T-side Wald entropy of rho^2 S_4 for non-chiral backgrounds; (4) statistical (edge) meaning of the contact for the symplectic U(1) with axion-type coupling; (5) non-totally-geodesic Sigma; (6) content scan (R_Sigma coefficient vanishes along N_s+11 n_D=28 for SD, a-anomaly balance); (7) a_3 KK route.

## Special instructions for the gatekeeper
- Do not read the result as G_A=G_T in general: it is for a covariant replica with imported/computed delta contacts, first order, n<1 branch, totally geodesic Sigma, (6,2), and a Wald-type T side.
- Re-run `identity_general_jets.py` and `smooth_family_deltas.py` (central); check the J and Omega sign conventions via `lc_convention_check.py`.
- The DW edge density is not claimed to be the contact; the gradient term is uncontrolled.
- The sentence on the Lambda^2 coefficient (c_A=0=c_T) rests on 021's Q contacts, not on a new derivation.
