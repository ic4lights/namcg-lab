# findings-r1.md — 077-g-selrule-copyinv (round 3 evidence state, researcher #3)

Target (from 076 review-r2, ranked avenue 1): criterion / bounded negation for which
matrix-state ensembles realize COPY-INVARIANCE of the momenta at leading semiclassical
order. Statistics used throughout (defined in-script): on the 2q signed nonzero
eigenvalues e of the edge charge Q~, D = max_k (e_{(k+1)q-1} - e_{kq})/max|e| (q-fold
multiset/tiling violation); U_2 = Tr Q~^4/(2q (Tr Q~^2/(2q))^2) - 1 (4th-moment
signature excess; 0 iff exact tiling). Ensemble: su(2) irrep dim N, cap rank M = N/2,
Theta = cap projector, 3 flavors, X~ = I_q (x) X, Theta~ = I_q (x) Theta, iid standard
complex-Gaussian Hermitian momenta unless stated. All numbers below are copied verbatim
from the shipped .out files (see manifest.md). No manuscript text proposed.

## A. Exact (finite-N) criterion — the mult-2 case is exactly solved; exact tiling is measure-zero but nonempty

1. Lemma 1 (s5, PASS, hash 08e83e0f): in the rank-1 edge-datum family the coincident
   charge factorizes exactly as Q~ = -2i(U R^+ - R U^+), U = I_q (x) |u), R qN x q, so
   rank Q~ <= 2q and the nonzero spectrum equals that of the 2q x 2q pencil
   T = -2i[[C0^+, Z0],[-I_q, -C0]], C0 = U^+R, Z0 = R^+R. Verified: FULL charpoly
   identity charpoly(Q~) - charpoly(T) == 0 exactly for q=2,N=2 (3 trials); symbolic
   top-5 charpoly-coefficient identities (q=2, N=3 and N=2, 3 substitutions each,
   u-components in R: True); numeric nonzero-spectrum dev 2.31e-14 (q=2,N=5) and
   2.66e-14 (q=3,N=4); range projection deviation 2.05e-14 / 5.35e-15.
   Convention pins (debug_conventions, hash 6b89217a): R_{xy} = w_{xy} exact to 7.87e-14
   (the transpose alternative fails at 3.55e+01); T real to 1.72e-15; nz spectrum of
   Qs vs Re eig(T) 4.44e-15. The OLD round-1 s5 block formula was non-Hermitian
   (max|Q - Q^H| = 5.29e+00) - documented superseded.
   [Classification: established identity/derivation (factorization is an algebraic
   identity; charpoly reduction is standard linear algebra given it), numerically
   verified at the tested sizes.]

2. Lemma 2 (s5, PASS): for q=2 block-diagonal pairs the charpoly coefficients are
   t^1: 4*rho, t^0: -4*rim**2 - 4*rre**2 (rho, rim, rre = Re/Im data of the edge rows),
   Re(alpha) invisible in both coefficients, roots -2 Im(alpha) +- 2(Im^2 alpha +
   |w_perp|^2)^{1/2} (the appH 'Row length' formula). EXACT mult-2 (double root pair)
   holds iff Im(alpha_1) = Im(alpha_2) AND |w_perp,1|^2 = |w_perp,2|^2.
   [Classification: established derivation at q=2 (symbolic coefficients + numeric
   verification). General q: same mechanism expected, NOT derived. Unresolved for q>2.]

3. Measure-zero + fragility (s1, PASS, 4e8b8ad6): exact mult-q events (nu < 1e-7) in
   6000 iid draws: 0; #nz != 2q events: 0; generic nu median 0.6868, min 0.1190.
   Base D(Q~(0)) = 1.28e-16; along an explicit perturbation direction, nu/t =
   0.8137, 0.8134, 0.8112, 0.7865 for t = 1e-4..1e-1 -> tiling violation is FIRST
   ORDER (linear, stable plateau) in generic perturbations.
   [Classification: established numerical fact for the tested iid Gaussian product
   ensemble at the tested N,q; supports "exact copy-invariance is not typical in any
   absolutely continuous ensemble".]

4. Nonempty null cone (s1 (d)): there is an explicit Hermitian momentum perturbation
   (in the range of the charge map, edge-block residual 1.252e-15, |dQ~| = 2.331e-14)
   with nu(Q~ + dQ~) = 1.084e-15, while the generic t=1 deviation is D = 0.4886.
   [Classification: established numerical fact (one explicit instance): the exact
   copy-invariant set is nonempty but thin (codim >= 1, first-order repelled by
   generic ensembles).]

## B. Leading semiclassical order: copy-invariance holds GENERICALLY for the iid/Gram-concentrating class, with explicit rates; it FAILS at O(1) for scale-mismatched classes

5. Universality + rates (s2 round-3b, PASS, 917ac53b / out 7469a471): coincident iid
   at q=2: D = 0.2986, 0.2120, 0.1415, 0.1176 at N = 50,100,200,400 (slope -0.461);
   U_2-1 = 0.1027, 0.0484, 0.0223, 0.0143 (slope -0.965) -> D = O(N^-1/2),
   U_2-1 = O(N^-1). Fixed-q window at N=400, q in {2,3,4,5,6,8,10} (5 events):
   D 0.0986-0.1898, U_2 0.0113-0.0155, all inside thresholds. Researcher #1's dense
   full-grid run (out.r1-fail, 183ba3f8) covers q up to 16 at N=400, 8 events:
   D 0.0992-0.1994, U_2 0.0132-0.0160 - bounded, no O(1) growth (this refutes the
   round-1 "breakdown at q ~ N^(1/3)" claim). N=200 control run (out.r3a-N200,
   93bf0513): D(q=10) = 0.2639 vs 0.1869 at N=400 - ratio 1.41 ~ sqrt(2), consistent
   with the N^-1/2 level; this quantifies the finite-N sensitivity of the 0.25 window.
   [Classification: conditional results (numerical, within the iid complex-Gaussian
   Hermitian momentum ensemble, fixed coincident cap geometry, q <= 16 tested at
   N=400).]

6. Negative control, copy-tempering (s2, same out): per-copy momentum variance scales
   (1, 1.6) on the SAME coincident geometry: D = 0.4147, 0.4113, 0.3946 at
   N = 120,240,480 (slope -0.036); U_2-1 = 0.2226, 0.2126, 0.2003 (slope -0.076) ->
   an O(1) inter-copy variance mismatch keeps the leading-order tiling violation
   O(1): it does NOT decay with N. [Classification: established numerical fact within
   the tempered-product class. This is the leading-order NEGATION for mismatched
   scale classes.]

7. Block-diagonal criterion (s3, PASS, c6138fcd): with independent per-copy momenta
   and variance scales tau: tau = (1,1): D = 0.2168, 0.1555, 0.0997, 0.0893
   (N = 60..480), slope -0.448 (tiling at leading order); tau = (1,1.6): D = 0.2921,
   0.2790, 0.2639, 0.2420, slope -0.090 (persistent O(1)); fully correlated copies
   (Pi_2 = Pi_1 a.s.): max D over all N and events = 0.00e+00 (EXACT tiling - the 076
   C1 mechanism); partial correlation c: D(N=480) = 0.0662 (c=0.00), 0.0825 (c=0.50),
   0.0254 (c=0.90), 0.0074 (c=0.99). Leading-order criterion in the coherence-free
   class: tiling <=> copy-temperality tau_1 = ... = tau_q; exact tiling <=> degenerate
   support (e.g. a.s.-equal momenta). [Classification: conditional results (numerical)
   with the exact-equality case (c) an established instance.]

8. Gram-concentration criterion + mixture negation (s4b, PASS, a59637bf): iid edge-row
   Gram concentration defect decays: 0.4759, 0.3920, 0.3130 at N = 100,200,400
   (slope -0.302); CV-0.4 lognormal per-copy scale mixture: 0.8070, 0.7732, 0.7908
   (slope -0.015), all > 0.5 -> the Gram-concentration criterion fails at leading
   order for scale mixtures: state selection has O(1) teeth outside the matched-scale
   class, matching 6 and 7 at charge level. [Classification: conditional results
   (numerical, tested mixture). Note: measured iid slope -0.302 is inside the
   [-0.9,-0.25] window but is NOT the ~-1/2 of the charge-level statistic; the
   pooled/median Gram-defect decays more slowly than the older header claim suggested -
   the corrected per-event statistic is the shipped one.]

9. Exact-tiling unreachability by norms alone + Im-alpha subleading-ness (s6, PASS
   after window fix, 32e2f1e2 / out 525f0828): |alpha|/|w_perp| = 0.1113, 0.0882,
   0.0511, 0.0395 at N = 60..480 (slope -0.527); rel-dev of the leading eigenvalue
   scale vs 2|w_perp| = 0.0024, 0.0014, 0.0006, 0.0004 (slope -0.903); D_exact
   (block-diagonal 2-copy, iid matched-scale rows) = 0.1317, 0.1118, 0.0805, 0.0536
   (slope -0.436), min 0.054 = 5.4e10 x the 1e-12 tiling threshold -> EXACT tiling is
   never approached by equalizing the row norms: the Im(alpha) equality (Lemma 2's
   second condition) is what fails, and it fails at an O(1)-in-signature level at
   every finite N. But D_exact decays ~ M^-1/2 and the leading-order signature
   U_2-1 = 0.02343, 0.01879, 0.00785, 0.00391 (slope -0.901 = O(1/N)) -> the
   Im-alpha column is subleading and invisible at leading semiclassical order: only
   the norm-equality condition has leading-order teeth.
   [Classification: conditional results (numerical, matched-scale iid row data). The
   round-3 script change (rel-dev window) corrected an internal inconsistency: the
   rel-dev is quadratic in the small ratio (slope ~ 2 x -1/2 = -1), measured -0.903
   vs |alpha|/|w| slope -0.527; numbers byte-unchanged by the fix.]

## C. The fixed-q window, extended (s2b, FAIL = the one genuine threshold finding)

10. z-path equivalence (s2b, PASS internally): (z0) full-Q~ vs T nonzero spectrum dev
    1.59e-12 (q=2,N=40) and 1.02e-12 (q=3,N=30); (z1) median D full-path vs z-path
    ratio 1.003 (q=2,N=120) and 0.978 (q=3,N=60) -> the ensemble reduction used by
    (a)/(b) is distributionally sound. (a) fixed-q N-window: slopes -0.531 (q=4,
    N = 64,128,256), -0.499 (q=8, 256..1024), -0.509 (q=16, 1024..4096), -0.496
    (q=32, 4096,8192): D decays ~ N^-1/2 uniformly in q ~ N^{1/2} along the grid
    N ~ q^2..16q^2. (b) along-q at N=1024: D = 0.1051, 0.1132, 0.1258, 0.1303, 0.1351
    for q = 4,8,16,32,64 (along-q exponent 0.093), U_2 = 0.0061, 0.0055, 0.0058,
    0.0059, 0.0058.
11. FAILED threshold, pinned (s2b ok_c: "U_2 < 0.05 at all (a),(b) points"): max U_2
    = 0.0859 at (q=4, N=64) = 4q^2; second offender 0.0549 at (q=4, N=128) = 8q^2.
    Every other point is <= 0.0253 (q=8@256: 0.0253, q=16@1024: 0.0059, q=32@4096:
    0.0015). Within q=4: 0.0859 -> 0.0549 -> 0.0184 at N = 64 -> 128 -> 256, slope
    ~ -1.09 (consistent with O(1/N)). Diagnosis (round 3): NOT a convention or
    normalization bug (z0/z1 pass; debug_conventions pins the conventions; the same
    code reproduces 1.003/0.978 equivalence ratios): the 0.05 level, calibrated for
    the large-N points, is genuinely missed at the two smallest-N points. Corrected
    factual claim: U_2 < 0.05 holds for N >= 16q^2 (q = 4..32) and at all (b) points;
    it fails for N <= 8q^2 at q = 4 (D still passes every point). The threshold was
    NOT changed; the script is left FAIL as the finding's carrier, with per-point
    U_2 medians now printed (report-only edit, hash 4eebfb72 vs pre-edit .bak3
    b3a02705).

## D. Determinism / reproduction pack

- s1, s3, s4b, s5 re-run from scratch round 3: outputs BYTE-IDENTICAL to shipped outs
  (.det.out files kept; sha8 pairs 79d342dc, 4562707e, 6194df6f, 9a04f362).
- s2 sections (a) and (a-control) byte-reproduce researcher #1's full-grid run; (b)
  differs by design (events 8->5, same seed stream start) - r1 numbers preserved in
  out.r1-fail.
- s6: same seed, table byte-unchanged across the window fix (525f0828).
- Re-run command for every script is in manifest.md; every script prints its own
  threshold table and a final 'PASS <tag>' line (s2b: FAIL by design, finding 11).

## E. What remains unestablished for G.selrule-copyinv

- NEITHER the criterion NOR the negation is closed as a theorem. What is established
  is a bounded, largely numerical picture: (i) an exact finite-N criterion only at
  q=2 (Lemma 2; general q open); (ii) sufficient-condition-type evidence - iid /
  Gram-concentrating matched-scale ensembles realize copy-invariance AT LEADING
  ORDER ONLY with rates D = O(N^-1/2), U_2-1 = O(1/N), uniform through q = O(N^{1/2})
  tested to q = 64; (iii) bounded negations - tempered/mixed-scale product classes
  retain O(1) leading-order violation (s2 control, s3 tau=(1,1.6), s4b mixture), and
  exact tiling is measure-zero and norm-unreachable for iid classes (s1, s6) while
  realized exactly in the fully-correlated (076 C1) family.
- Open steps: the general-q exact mult criterion (q>2); analytic (proof-level) status
  of the rank-reduction + concentration statements beyond tested sizes/ensembles
  (rates are numerical); necessity direction of the Gram-concentration criterion
  (sufficiency direction is what concentration tests support); the q > 16 dense-matrix
  regime is only covered by the z-path (q<=64) - growth beyond q ~ N^{1/2} untested
  (Frenkel fixed-q condition respected by all claims); other field content /
  backgrounds / flavor structures; and the bridge FROM "the charge ensemble tiles to
  leading order for generic ensembles" TO the 076 problem-G statement (two-sided +-
  reading, mixed multiplicities, the state-selection mechanism for the actual NAMCG
  ensemble). Nothing here closes or re-labels Problem G; all results are consistent
  with (and quantify) the 076 (H1')+copy-invariance conditional stack.
