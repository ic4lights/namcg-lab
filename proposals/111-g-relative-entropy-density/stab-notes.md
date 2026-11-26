# stab-notes (numeric stabilization pass 4, 2026-11-22)

## Resolutions made
1. Double-counting (confirmed, fixed prior pass + Test D here): entropy_from_G sums
   s(nu) over DISTINCT modes nus(G); Test D's c_b previously summed ln(2 sinh(h/2))
   over symplectic_spectrum (2N values) giving c_b = 2*c0 -> stale FAIL A3/D-class
   artifact. Now c_b uses nus(G); D1 agrees to 1e-12 (0.814120352312 both sides).
2. Imag-assert policy: A_of_G split into A_of_G_raw (complex, no assert) + wrapper
   asserting max|Im| <= IMAG_RELTOL*(max|Re|) + 1e-12 with IMAG_RELTOL = 1e-6
   (replaces dead pass's absolute 1e-8 assert that crashed at mu=0.01 N=12).
   Measured leak max|Im|/(1+max|Re|) [stab_probe1/3.py, scalars]:
     (31,0.05,8) 1.39e-07 | (41,0.01,6) 3.92e-10 | (31,0.2,8) 5.37e-07
     (41,0.01,12) 1.29e-03 | (49,0.05,12) 8.7e-05 | mu=0.3: N=8 2.4e-06, N=12 5.2e-04
   Leak grows with the NUMBER of near-pure cut modes (any mu), not only small mu:
   h(nu)=ln((nu+.5)/(nu-.5)) is unresolvable in double precision once true
   nu_min-0.5 falls below the eig floor (measured nu_min-0.5 = 5.7e-12 at
   (31,0.05,8) already at the floor). This is a resolution limit, not noise at a
   tolerable scale: no clipping was added (clipping cannot restore resolved h);
   instead the certified grid is bounded by the leak assert and enforced there.
3. Dropping Im A0 (leak <= 1e-6) is anchored twice on Fock-feasible cuts:
   A1 covariance round-trip rho(A0) -> G matches G0 to <= 1e-6 abs, and A4 Fock
   entropy vs spectral entropy <= 1e-6 abs (tests A1-A4, B lines).
4. Near-pure regime (mu=0.01, N=12 and all N>=12 sampled): documented exclusion
   S1 in battery (prints leak, checks it exceeds tol by >100x as tripwire), NOT
   certified, NOT asserted inside A_of_G.
5. Test B n=3: nmax 9 -> 11. relcov at seed 3 fell 3.19e-02 -> 1.40e-02
   [stab_probe4.py], confirming Fock-truncation origin; tolerance kept at 3e-2
   (tightened grid, checks unchanged).
6. Comparison-logic artifact from first death: every check now compares abs diff
   to abs tol and prints both on one line; battery prints RESULTS count and
   exits with explicit FAIL lines otherwise (no crash paths: raw route for
   diagnostic leaks, asserts only on certified inputs).

## Certified grid (run_modular.out, ALL CHECKS PASS, 18 checks)
- Test A (Fock-anchored, nmax=12): (L,mu,N) = (17,0.70,1), (19,0.40,2), (23,0.25,3)
- Test B (Fock-anchored random, nmax 20/12/11): n=1,2,3 x seeds 1,2,3
- Test C positivity: 12 random physical covariances (n<=4) + certified cuts
  (31,0.05,8), (31,0.20,8), (27,0.05,6), leak <= 1e-6, minEig(A0) = 3.185e-01, 1.075e+00, 3.584e-01
- Excluded (documented, S1): mu=0.01 N=12 and any cut with >~8 near-pure modes.

## Reproduce
python -I check_modular.py   (from this folder; ~90 s; expect final line ALL CHECKS PASS)
Probes: stab_probe1.py (imag magnitudes), stab_probe3.py (mu x N leak sweep),
stab_probe4.py (nmax truncation scaling). Quarantined dead-pass files untouched.

## Manifest (sha1-10, bytes)
52497c0c45 8018 _common.py
cd982322f9 4628 check_modular.py
7247af5bf4 2250 run_modular.out
