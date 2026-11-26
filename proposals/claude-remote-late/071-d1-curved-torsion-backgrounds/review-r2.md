VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

Gatekeeper r2 review, remote/claude, 2026-11-22. Saved by the orchestrator. The gatekeeper's exact check is gk071r2_exact.py (in this folder).

Source reading: digest plus targeted reads (appH L715-758, L1513-1533, L1609-1629; ch17 D1). Full scan still owed.

## Checks
- All scripts reproduce. make_insert_r2 rebuilds the insert byte-identically. apply_and_build_r2: pre d8d8b678, post c1a880e5 (753073 B), 414 pp, clean, all anchors unique (including L1623).
- Independent exact check, symbolic in all parameters at an exact Lorentz u, using the literal L1519 fields:
  - wider Heisenberg family: all three brackets hold, including the order-zero part;
  - t = (a/2,0,a/2,0), F_13 = a kappa/2, R_13 = kappa(aB+zeta N+x N');
  - T^2 = 2kappa^2, R^2 = -4a^2kappa^2, scalar 0.
- By hand:
  - R^2 and the scalar (0 on all families). The r1 value "-2sm_1" was a non-scalar; it is corrected.
  - F != 0 is allowed by the class, and the third bracket holds.
- Sign map omega = -w confirmed. The alpha sets are correct in the snippet-A normalisation.
- Snippet B numbers verified: off-cone 2.8e-5 to 3.0e-2.
- Edit E verified: vartheta = +1/2 matches. The 068 cones, multiplicities, chains and ranks are unchanged.
- r1 findings 1-7: all closed.
- The no-mass result is correctly scoped to family (i). No gap claim is made on the wider family.

## Findings
1. minor: "For a != 0 ... R^2 != 0" is false at kappa = 0. Require chi kappa != 0.
2. minor: the parameter a clashes with the frame index a. Rename it to chi (unused in Section D).
3. informational, proposal only: the "first exact solution with R^2 != 0" claim is false in general (L1527 has Schwarzschild, Kasner, dS at T=0). Keep the qualifier "left-invariant, constant connection, T != 0" in any record.
4. informational: "a gap is not excluded by symmetry" is an avenue rationale, not a result.

## Corrected snippets
H, replacing the whole added sentence:
On the algebra of (ii) the wider ansatz \(w_a{}^{cd}=k_a(\chi B^{cd}+\zeta N^{cd}+xN'^{cd})\) solves all three brackets for all real \(\kappa,\chi,\zeta,x\): \(\mathsf T_{ac}{}^c=\chi\,k_a\), the only nonzero pair of \(\mathsf F\) is \(\mathsf F_{13}=\tfrac12\chi\kappa\), the only nonzero pair of \(\mathsf R\) is \(\mathsf R_{13}{}^{cd}=\kappa(\chi B^{cd}+\zeta N^{cd}+xN'^{cd})\), and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\), \(\mathsf R_{ab}{}^{ab}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\) (exact for the section values; for the operators on the bundle at random Lorentz \(u\), including the order-zero part, residual below \(10^{-15}\)). For \(\chi\kappa\neq0\) it is an exact solution with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) on a unimodular algebra.

SC2: replace `its extension with \(a\neq0\)` with `its extension with \(\chi\neq0\)`.

## Scope
- Exact: families (i) and (ii), and the wider Heisenberg family; the invariants; the sign map; the corrected 068 value.
- Bounded no-go on family (i) only.
- No label change. D, F, N OPEN. Not a breakthrough.

Avenues:
1. Linearise the wider family at chi kappa != 0 in the Heisenberg oscillator sectors (Landau-level shifts, growth bound).
2. The c-free survey.
3. A norm for the cone shifts.
4. Nonlinear and one-loop.
5. Non-constant connections.

## Disposition
- r3: apply H and SC2, regenerate the insert and the hashes.
- Then the full scan.
- Expected next verdict: ACCEPT.
