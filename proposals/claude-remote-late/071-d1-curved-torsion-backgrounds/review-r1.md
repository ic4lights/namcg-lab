VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR (non-load-bearing, merged 068 L1623) | PROGRESS: first | OPEN: 0/2

Gatekeeper r1 review, remote/claude, 2026-11-21. Saved here by the orchestrator. The gatekeeper's check scripts are in this folder as gk071_*.py.

Source reading: digest plus targeted reads (appH L715-760 and L1513-1629; ch17 D1 and the order). ch10 was not read. The full scan is still owed.

## Verified
- All scripts give identical output. apply_and_build: pre d8d8b678, post a73760f2, 414 pp, clean.
- Operator-level check built independently from L1519. Families (i) and (ii) are exact solutions, including the order-zero part. F = -c.t is confirmed.
- Curvature is rank one on N, so R^2 = 0. Ricci is cancelled by torsion.
- Checked by hand:
  - F = -c.t
  - the diffeo direction omega = xi^c R_ca
  - the label reduction to Q
  - triangularity
  - the boost-dilation argument, which is RIGOROUS and independent of convention
- With unrounded alpha (+-sqrt3 + {0, +-i, 2i}; {-i/2, -3i/2, -5i/2}), the converse is clean at BOTH points: sigma ratio ~1e-16 against a control of >= 2e-4.

## Findings
1. MAJOR, connection sign convention. The scripts use D = E + 1/2 w S, but the manuscript's L1519 gives -1/2 omega S, so w = -omega. Signed values flip (T trace, R_13, the alpha sets). The solution sets, invariants and the no-mass result are unaffected. Fix with A.
2. MAJOR, the "weak converse" is an s2 rounding bug (alpha rounded to 1.73). Fix s2 to use unrounded alpha, re-run, apply B, and withdraw the Jordan reading.
3. minor, survey: one stored solution is not unimodular; t and the third bracket were not examined. Fix with C.
4. minor, family (ii): needs (zeta,x) != (0,0); also say t=0, so the third bracket holds. Fix with D.
5. minor, PRIOR-CLAIM-ERROR (non-load-bearing), merged 068 text at appH L1623: "for vartheta=-1/2" should be "+1/2" under L1519. Fix with E, re-verified with v4 under the sign map.
6. cosmetic: an s1 print label shows -sqrt3 s where the value is +sqrt3 s.
7. informational: the gatekeeper's intended non-solution control, Heisenberg w = +-kB (kappa=1), is an exact solution with R^2 = -4. So the ansatz is wider than (ii). Account for this in the proposal and in the avenue ranking.

## Snippets
A. Replace "but give the connection constant components \(\omega_a{}^{cd}=w_a{}^{cd}\) in this frame." with:
"but give the connection constant components \(w_a{}^{cd}\) in this frame, normalised so that the first-order part of \(\mathbb D_a\) at \(u=1\) is \(E_a+\tfrac12w_a{}^{cd}\mathcal S_{cd}\), the sign of the fluctuation \(\tfrac12\omega_a{}^{cd}\mathcal S_{cd}\) below; in the coordinate form of the paragraph on local \(\mathrm{SO}(3,1)\) inside the unitary group this is \(e_a{}^\mu\omega_\mu{}^{cd}=-w_a{}^{cd}\)."

B. Replace the converse sentence with:
"Conversely the forty equations drop rank at random complex points of each of these cones (numerical; the relative smallest singular value is about \(10^{-16}\) at both points, against at least \(10^{-4}\) at random points off the cones)."
Use the re-run numbers.

C. Replace "with \(\mathsf c\) free, solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) were found on algebras with a two-dimensional abelian derived algebra (numerical, not a classification)" with:
"with \(\mathsf c\) free, solutions of the first two brackets with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) were found on algebras with a two-dimensional abelian derived algebra, not all unimodular, for which the order-zero field and the third bracket are not examined (numerical, not a classification)"

D. Replace "with \(w_a{}^{cd}=k_a(\zeta N^{cd}+xN'^{cd})\). The torsion is trace-free," with:
"with \(w_a{}^{cd}=k_a(\zeta N^{cd}+xN'^{cd})\) and \((\zeta,x)\neq(0,0)\). The torsion is trace-free, so \(\mathsf t=0\) and the third bracket holds,"

E. appH L1623: replace "for \(\vartheta=-\tfrac12\)" with "for \(\vartheta=\tfrac12\)".

## Scope
- Exact: existence of (i) and (ii); F = -c.t; the label reduction; the triangular form; the gauge formula.
- Bounded no-go (rigorous), on the flat-frame null family: no isolated mass shell and no invariant scale.
- Positive existence input plus operator content. It does not derive SO(3,1), the frame, non-degeneracy or the selection.
- No label change. D, F, N stay OPEN. Not a breakthrough.

Avenues, ranked:
1. Backgrounds that carry the scale kappa: (ii) in oscillator sectors, and the exact Heisenberg w=kB with R^2 != 0.
2. The c-free survey solutions, once checked.
3. A norm for the imaginary cone shifts.
4. Nonlinear and one-loop.
5. Non-constant connections.

## Disposition
r2: apply A-E, fix s2, withdraw the Jordan reading, re-verify v4 for E, and produce new hashes. Then the full scan.
