# Proposal 054-lorentzian-fourier-observables, round 1

## Result

Target: 053's rank-1 open avenue for Problem E, the non-polynomial observables `Tr e^{i kappa A_0}`, timelike momentum first, in Definition (A) of the regulated Lorentzian integral at finite N with eps -> 0 taken first.

What is established (proofs below, numerics at N = 2 in `n2_runs.txt`):

1. **Fixed eps, any N (exact).** For every product O of traces of products of factors `e^{i kappa A_mu}` (one index mu per factor, complex kappa), `I_eps[O]` equals the same integral on `R_u` for every u < 2/3. This is 053's Stokes argument with polynomial growth replaced by `e^{c||A~||}`.
2. **(i) Complex momenta, eps -> 0 (N = 2 proved; N >= 3 conditional on 053's flat-direction bound and Z_E != 0).** Take 0 < u < 2/3. Put `kappa = K e^{3 pi i u/8}` on every mu = 0 factor and `kappa = K e^{-pi i u/8}` on every mu >= 1 factor, with K real. Then on R_u every factor is unitary, `|O| <= N^{n_tr}`, and dominated convergence gives `lim_{eps->0} I_eps[O] = I^{(u)}[O]`, the eps = 0 integral on R_u.
3. **(ii) Real momenta (exact, N = 2).** For real kappa != 0, the integrand of the formal "Euclidean value at phases" for `Tr e^{i kappa A_0}` is not integrable. The integrand grows like `sinh(|kappa| sin(3 pi/8) ||A~_0||_op)`, and the Euclidean weight has no moment of degree 14. So 053's polynomial statement does not extend to these observables in its form.
4. **(iii) Gaussian smearing in kappa (N = 2 proved; N >= 3 conditional as in (i)).** For `phi(kappa) = e^{-(kappa-kappa_0)^2/l^2}` with real kappa_0 and l > 0,
   `lim_{eps->0} int_R phi(kappa) <Tr e^{i kappa A_0}>_eps d kappa = int_{e^{i theta} R} phi(kappa) J(kappa) d kappa` for every 0 < theta < pi/4,
   where J is the limit function of (i). The same holds for A_j on the lines `e^{-i theta} R`, 0 < theta < pi/12.
5. **(iv) Analytic structure at N = 2 (proof sketched in full below).**
   - J(kappa), defined by the eps = 0 integral on R_u with u = 8 arg(kappa)/(3 pi), is holomorphic for 0 < arg kappa < 3 pi/4, with `|J| <= 2 [sin(4 arg kappa/3)]^{-27/2}`.
   - `F_E(t) := J(sqrt(t) e^{3 pi i/8})` is holomorphic on |arg t| < 3 pi/4. For t > 0 it equals the Euclidean characteristic function `<Tr e^{i sqrt(t) A~_0}>_E`.
   - For A_j the same construction gives `F_E(e^{i pi/4} kappa^2)`. Its real-kappa values lie inside the sector, so the smeared spacelike limit is `int_R phi(kappa) F_E(e^{i pi/4} kappa^2) d kappa`.
   - The timelike real-kappa values lie on the boundary ray arg t = -3 pi/4. Both cases read `F_E(e^{i pi/4} k.k)`, the timelike case reached from `k.k - i0`.

**What this means for E.** For these observables, this order of limits and gamma = 0, the regulated Lorentzian integral gives only analytic continuations of Euclidean data:
- at N = 2, values or line integrals of the continued Euclidean characteristic function F_E, which F_E on t > 0 determines;
- for N >= 3, conditionally, the eps = 0 integrals on R_u.

This sharpens 053's caveat. A "real-time reading by continuation" is exactly what the integral gives here, and the timelike case sits on the edge of the continuation domain established.

**What this does not do.**
- No pointwise statement at real timelike kappa. Whether F_E continues across arg t = -3 pi/4 is open.
- No boosted momenta, no holomorphy for N >= 3, no N -> infinity first, no gamma != 0, no Definitions (B) or (C).
- No signature, background, frame or fermion content is derived. Assumption ass:lorentzian stands.
- Problem E stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Target and status

- **Problem E**, Appendix H (`sec:status-E`, L1482-1513 of the working file, read in full). Ledger label verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature." Status paragraph: "Remains Assumption~\ref{ass:lorentzian}."
- **Chapter 17** (L394-399): "OPEN; CRITICAL PATH for the matrix-derived label. A scope that retains Assumption~\ref{ass:lorentzian} gives up the claim that Lorentzian signature is emergent or derived. Euclidean positivity and a formal Wick rotation do not select it; rotating because the infrared world is Lorentzian is not a derivation." Criterion item (L718): "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})." No discrepancy between the two sources.
- **Original target:** derive Lorentzian signature rather than retain it.
- **Dependencies:** none in the sequence. The package builds only on the 053 block (Definition (A), contours R_u, the flat-direction bound, the limit display).
- **Current critical-path set** (ch17 L695-722 criterion and Appendix H labels, re-read): A, B, C, D1, E, F, G-derived, N. H, I, J remain optional. This package touches E only.
- **Classification of this package:** PROGRAMME-CONDITIONAL sharpening of E. It does not derive the target.

## Source reading

**Digest + targeted reads. Not a full scan.** The proposal adds one conditional paragraph block to Appendix H. It changes no definition, assumption, scope sentence or status passage, so a full scan is not required under CLAUDE.md 3(c).

- `python scripts/make_digest.py --check` printed `DIGEST CURRENT`, `dirty-chapters: yes`, at the start of the task. Only `--check` was run.
- **Baseline change during the task.** The author committed `4973019` ("1"). It contains the 053 manuscript change (appH, bib) and an early draft of this folder's `n2_fourier.py`. After it, `git diff HEAD -- chapters bib` is empty. The working appH is 532576 bytes, sha256 `7a75554e...6aaa`, CRLF 3203, no bare LF. That is the accepted 053 output (review-r3). The digest's file hash for appH (`7a75554ef8cb`) equals the working file, so the digest describes the current chapters; only its head field predates 4973019. At hand-off `make_digest.py --check` prints `DIGEST STALE (head changed)` for that reason. The chapter bytes are the same as at the start of the task (`git diff HEAD -- chapters bib` is empty), and I did not regenerate the digest.
- **Read in full:**
  - appH L1-11 (appendix preamble);
  - appH L1482-1513 (all of Problem E, including the whole 053 block L1494-1510 and the Status paragraph L1512-1513);
  - ch17 L390-399 (Problem E) and L695-722 (criterion);
  - ch04 L316-332 (Assumption ass:lorentzian);
  - ch03 L136-150 (eq:Smatrix);
  - reports/sme-scout-20261102-after50.md in full;
  - proposals/053 review-r3, proposal-r3, appH_insert.tex, n2_reduced.py with output, n2_mc_check.py;
  - the tail of reports/ledger.md (031-053 entries);
  - MILESTONE.md.
- **Not relied on:** the author's Problem A text (appH L12-71), which this package neither cites nor touches.
- Unreadable files: none.

## Research and reasoning

### Choice of target

Two candidates were offered: the scout's R2 (semi-classical self-consistency of the commuting-fibre and CP^{1,2} x K classes against 2605.13294) and 053's rank-1 avenue (this package). I chose the second. The reasons are recorded under Decisions Taken. In short:
- It is about the integral itself, which the scout lists first among the things the loop avoids.
- It closes, within stated hypotheses, the one exception 053 left explicitly open.
- It could be done rigorously with the N = 2 machinery already reviewed.
- R2 would test supplied classes against a criterion whose equation numbers and warnings are second-hand. Its expected outcome is largely that paper's own claim.

The scout's programme-level point stands against this package too. It does not address selection or Problem A, and it does not derive signature. What it does is remove an open door that a reader of 053 could take for a route to a non-Euclidean datum, and it says exactly what kind of object the real-time Fourier mode is.

### Setting and notation

These are as in the 053 block:
- traceless Hermitian N x N matrices A_mu, mu = 0..9, eta = diag(-1, 1, ..., 1);
- S_b from eq:Smatrix with C = 0 and the IKKT Pfaffian;
- `I_eps[O] = int dA O Pf M e^{i S_b - eps sum Tr A_mu^2}` (Definition (A));
- `R_u: A_0 = e^{-3 pi i u/8} A~_0, A_i = e^{pi i u/8} A~_i`;
- the 053 facts Re(i S_b) = -sin(pi u/2) S_E on R_u, and the flat-direction bound `int dA~ (1+||A~||)^k |Pf M(A(u,A~))| e^{-c S_E} < infinity` for k < 14 (proved at N = 2, conditional for N >= 3);
- the limit display.

`<.>_eps = I_eps[.]/I_eps[1]`. J and F_E are new symbols, and so are K, kappa, theta, phi, l and n_tr. None collides with the 053 block, which uses k for a polynomial degree and sigma^a for Pauli matrices. The momentum is therefore kappa, not k, except in the single phrase `k^mu k_mu`.

### Step 0: Stokes at fixed eps for exponential observables (exact, any N)

On every R_{u'}, 0 <= u' <= u, each factor obeys `||e^{i kappa A_mu}||_op <= e^{|kappa| ||A~_mu||_op}`, and `|Tr M| <= N ||M||_op`. So `|O| <= N^{n_tr} e^{c ||A~||}` with c = sum of the |kappa|.

053's boundary term on the ball of radius R times [0, u] was a polynomial times `e^{-eps cos(3 pi u/4) R^2}`. It is now that times `e^{cR}`, which still tends to 0 for u < 2/3. Together with Re(i S_b) <= 0 along the homotopy, this gives `I_eps[O] = int_{R_u} ...` (exact).

At u = 0 and real kappa the observable is bounded, so `I_eps[O]` converges absolutely. For complex kappa it converges absolutely because of the Gaussian factor.

### Step 1, statement (i): complex momenta

- **Choice of momenta.** With `kappa = K e^{3 pi i u/8}` on mu = 0 factors, `kappa A_0 = K A~_0`. With `kappa = K e^{-pi i u/8}` on mu >= 1 factors, `kappa A_j = K A~_j`. Each factor is then `e^{iK A~_mu}` with A~_mu Hermitian, so it is unitary. Hence `|O| <= N^{n_tr}` on R_u, uniformly in eps.
- **Domination.** On R_u the eps-dependent factor has modulus `exp(-eps[cos(3 pi u/4) Tr A~_0^2 + cos(pi u/4) sum Tr A~_i^2]) <= 1` for u < 2/3. The rest is bounded by `N^{n_tr} |Pf M(A(u,A~))| e^{-sin(pi u/2) S_E}`, which is integrable by the 053 bound with k = 0.
- **Limit.** Dominated convergence gives `lim I_eps[O] = I^{(u)}[O]`. With 053's `lim I_eps[1] = e^{7 pi i (N^2-1)/4} Z_E != 0` (proved at N = 2, hypothesis for N >= 3), the ratios converge.
- **Status.** This is exact at N = 2 and conditional for N >= 3 exactly as 053 is.
- **u = 1.** The same construction at u = 1 is the Euclidean expectation value with real momenta K. For N >= 3, no relation between different u is claimed for these O.

### Step 2, statement (ii): real momenta, the formal Euclidean expression fails

At N = 2, A~_0 = a~.sigma/2 has eigenvalues `+-|a~|/2 = +-||A~_0||_op`, so `Tr e^{iz A~_0} = 2 cos(z ||A~_0||_op)`.

The identity `|cos(p+iq)|^2 = cos^2 p + sinh^2 q` is checked in `exact_checks.txt` (5). It gives `|Tr e^{iz A~_0}| >= 2|sinh(Im z ||A~_0||)|`. For `z = kappa e^{-3 pi i/8}` and kappa real, |Im z| = |kappa| sin(3 pi/8) > 0.

The Euclidean modulus at N = 2 is `|c_P| (det G~)^4 e^{-S_E}`:
- On R_1, `G = e^{i pi/4} G~`, so the 053 bound is an equality there.
- 053 states that this integral with `(1+||A~||)^k` converges exactly for k < 14, so `int ||A~||^14 (det G~)^4 e^{-S_E} = infinity`.
- The weight is SO(10) invariant and `||A~||^14` is bounded by a constant times `sum_mu |a~_mu|^14`. So `int |a~_0|^14 (...) = infinity`.
- Since `sinh x >= x^14/14!` for x >= 0, the integrand of the right-hand side of the limit display, with `O = Tr e^{i kappa A_0}`, is not integrable.

(This uses 053's sharpness statement, which is proved at N = 2.)

### Step 3, statement (iii): Gaussian smearing

- **Fubini at fixed eps.** At fixed eps, `int phi(kappa) I_eps[Tr e^{i kappa A_0}] d kappa = I_eps[Phi]`, with `Phi = int phi(kappa) Tr e^{i kappa A_0} d kappa = sqrt(pi) l Tr e^{i kappa_0 A_0 - l^2 A_0^2/4}`. The identity is checked symbolically in `exact_checks.txt` (1).
- **Bound on R_u.** With `alpha = 3 pi u/8` and lambda an eigenvalue of A~_0, `log|e^{i kappa_0 e^{-i alpha} lambda - l^2 e^{-2 i alpha} lambda^2/4}| = lambda (kappa_0 sin alpha - l^2 cos(2 alpha) lambda/4)`. Its maximum is `kappa_0^2 sin^2(alpha)/(l^2 cos 2 alpha)` (`exact_checks.txt` (2)). So `|Phi| <= sqrt(pi) l N exp(kappa_0^2 sin^2(alpha)/(l^2 cos 2 alpha))` on R_u for u < 2/3.
- **Limit.** By Step 0 and dominated convergence, `lim I_eps[Phi] = I^{(u)}[Phi]`.
- **Turning the kappa-line.** For fixed A~ on R_u, `kappa -> phi(kappa) Tr e^{i kappa e^{-i alpha} A~_0}` is entire. In the two sectors between R and `e^{i alpha} R`, |phi| decays like `exp(-cos(2 arg kappa)|kappa|^2/l^2 + O(|kappa|))` with `cos(2 arg kappa) >= cos 2 alpha > 0`, while the trace grows at most like `N e^{|kappa| ||A~_0||}`. So the arcs vanish and `Phi(A(u,A~)) = int_{e^{i alpha} R} phi(kappa) Tr e^{iK A~_0} d kappa` with `K = kappa e^{-i alpha}` real.
- **Swapping the integrals.** On the product (R_u) x (line), the integrand is bounded by `N |phi(kappa)| |Pf| e^{-sin(pi u/2) S_E}`, which is integrable. Fubini then gives `I^{(u)}[Phi] = int_{e^{i alpha} R} phi(kappa) I^{(u)}[Tr e^{i kappa A_0}] d kappa`.
- **Result.** Dividing by `I^{(u)}[1]` gives the display, with theta = alpha ranging over (0, pi/4).
- **Spacelike case.** For A_j the same steps hold with `alpha -> -beta = -pi u/8`, which ranges over (-pi/12, 0).
- **Status.** Exact at N = 2, conditional for N >= 3 as in (i). Negative kappa on the line is covered by (i) with K < 0, so evenness of J is not needed.

### Step 4, statement (iv): holomorphy and F_E at N = 2

**Facts used at N = 2.**
- `Pf M = c_P (det G)^4` for all complex A (053).
- Cauchy-Binet gives `|det G| <= det G~` for any row phases. `exact_checks.txt` (8) samples 20000 random points with u in (0, 2) and finds a maximal ratio of `1 - 4e-12`.
- Re(i S_b) = -sin(pi u/2) S_E on R_u for every u, which is positive damping for 0 < u < 2. `exact_checks.txt` (7) gives the general (alpha, beta) form `-lambda[P sin(2 alpha - 2 beta) + e2(W~) sin 4 beta]`, with `P = a~^T(tr W~ - W~)a~` (sympy).

So `I^{(u)}[Tr e^{i kappa A_0}]` with `kappa in e^{3 pi i u/8} R` is absolutely convergent for 0 < u < 2. Define J(kappa) as its ratio to `I^{(u)}[1]`, for 0 < arg kappa < 3 pi/4.

**Bound.** `|I^{(u)}[Tr]| <= 2 |c_P| int (det G~)^4 e^{-s S_E}` with s = sin(pi u/2). Scaling A~ -> s^{-1/4} A~ gives `s^{-(30+24)/4} = s^{-27/2}` times the Euclidean integral (`exact_checks.txt` (6)). Since `|I^{(u)}[1]| = |Z_E|` (053), `|J(kappa)| <= 2 [sin(4 arg kappa/3)]^{-27/2}`.

**Holomorphy.** Fix kappa_* with arg kappa_* = alpha_* in (0, 3 pi/4), and put beta_* = alpha_*/3.
- **Reduction to one exponential.** Write a = A_0's su(2) vector. The B-integrand at fixed a,
  `h(a) = int dB~ Pf e^{i S_b}` with `B = e^{i beta_*} B~`,
  is even in a, because G and a^T(tr W - W)a depend on a only through a a^T. In polar coordinates `a~ = r n`, the even function `2 cos(K r/2) h` integrates over R^3 to `int_{S^2} dn int_{-infinity}^{infinity} r^2 e^{iKr/2} h(r n) dr`.
- **The two half-lines.** Put the a-variable on `a = e^{-i phi_+} r n` for r > 0 and `a = e^{-i phi_-} r n` for r < 0, with `phi_+- = alpha_* -+ delta`. For kappa with |arg kappa - alpha_*| < delta/2, `|e^{i kappa z/2}| <= e^{-|kappa| |r| sin(delta/2)/2}`, where `z = e^{-i phi_+-} r` is the complex radial coordinate.
- **Domination.** Re(i S_b) <= -c S_E(|r| n, B~) with `c = min(sin 4 beta_*, sin(2 phi_+- - 2 beta_*)) > 0` for small delta, using the (alpha, beta) formula, since beta_* < phi_+- < beta_* + pi/2. Cauchy-Binet bounds the Pfaffian. So the integrand is dominated, uniformly in kappa near kappa_*, by an integrable function, and the integral is holomorphic in kappa there (Morera with Fubini).
- **Equality with J.** At each such kappa, the value equals the R_u integral defining J(kappa). First rotate each half-line from phi_+- to arg kappa with B fixed: in between, |e^{i kappa z/2}| <= 1 and the same domination holds. Then move the B-phase from beta_* to arg(kappa)/3 with the a-phase at arg kappa: the observable is unchanged and the domination holds.
- **Boundary terms.** These vanish along a sequence of radii R_n -> infinity. If R^3 M(R) >= c > 0 for all large R, where M(R) is the dominating function integrated over the sphere of radius R, then `int R^2 M dR` would diverge, contradicting integrability.

Hence J is holomorphic. `F_E(t) := J(sqrt(t) e^{3 pi i/8})`, with the principal root, is then holomorphic for |arg t| < 3 pi/4. For t > 0 (u = 1) it is `<Tr e^{i sqrt(t) A~_0}>_E`, the same for every A~_mu by SO(10) invariance of the N = 2 Euclidean weight. At N = 2 it is real for t > 0, and `F_E(conj t) = conj F_E(t)`. The exploratory runs in `grid_tests.txt` show this: at alpha = 1.6493 (u = 1.4) the values are the complex conjugates of those at alpha = 0.7069 (u = 0.6), on both grids.

**Spacelike case.** For A_j, j >= 1, the same steps with the j-row in polar coordinates (evenness: W is even in each row) give a holomorphic J_s on -pi/4 < arg kappa < 0. Its Euclidean ray arg kappa = -pi/8 gives F_E(K^2). By the identity theorem, `J_s(kappa) = F_E(e^{i pi/4} kappa^2)`.

As arg kappa runs over [-theta, 0], `arg(e^{i pi/4} kappa^2)` runs over `[pi/4 - 2 theta, pi/4]`, inside the sector. There F_E is holomorphic and bounded by the bound above, read through `arg kappa_t = (arg t + 3 pi/4)/2`. So the line in (iii) can be turned back to R, giving `lim (smeared) = int_R phi(kappa) F_E(e^{i pi/4} kappa^2) d kappa`.

**Timelike case and the k.k form.**
- For A_0, `J(kappa) = F_E(e^{-3 pi i/4} kappa^2)`. Real kappa corresponds to arg t = -3 pi/4, the boundary of the sector on which holomorphy is proved.
- With `k^mu = kappa delta^mu_0`, `k.k = -kappa^2`, and with `k^mu = kappa delta^mu_j`, `k.k = kappa^2`. Both cases are `F_E(e^{i pi/4} k.k)`.
- For the timelike case with arg kappa > 0 small, `k.k = |kappa|^2 e^{i(2 arg kappa - pi)}` approaches the negative axis from below, that is `k.k - i0` (`exact_checks.txt` (4)).

**Why the sector stops at 3 pi/4.** With independent phases per index mu, Re(action) > 0 requires `|theta_mu + theta_nu| < pi/4` for all pairs mu != nu. This caps the phase of the A_0 direction at 3 pi/8, that is |arg t| < 3 pi/4. The timelike Lorentzian point is the corner where both constraints are saturated. I do not claim this cap is a property of F_E. It is a property of the contour method, and whether F_E continues beyond it is the open step.

### Step 5: numerics at N = 2

The engine is `n2_fourier.py`, a re-implementation of 053's three-variable reduction:
- it adds the at-integral of `2cos(zeta |a~|)` against the anisotropic complex Gaussian times the Pfaffian polynomial;
- the radial integral is closed form, via the Kummer transformation;
- the angular rule is product Gauss-Legendre on one octant in (log theta, phi);
- it also handles the smeared observable (Gaussian shift of q) and moments.

The full checks are listed under Verification scripts.

**Results** (from `n2_runs.txt`; N = 2, lambda = 1/(4 g^2) = 1/2, D = 10 with det(G)^4; grid GF; all values are ratios on one contour and one grid).

**R1, Euclidean ray u = 1.**
- Z2 = -4.13282008e5 (1+i). This is twice 053's Z_E = -2.06641004e5 (1+i), as it should be, because the engine counts 2cos.
- Euclidean moments of |a~|^2 for n = 1..4: 1.02129224 (053: 1.02129224), 1.80000000, 4.78730737, 18.5625.
- F_E(K^2) = <Tr e^{iK A~_0}>_E is real:

  | K | F_E(K^2) | degree-6 Taylor polynomial |
  |---|---|---|
  | 0.25 | 1.98407888 | 1.98407888 |
  | 0.5 | 1.93675194 | 1.93675193 |
  | 1 | 1.75384770 | 1.75384416 |
  | 2 | 1.11627475 | 1.11540969 |
  | 3 | 0.33062281 | 0.30999407 |
  | 4 | -0.34839830 | -0.53624582 |

  The difference at K = 1 (3.5e-6) equals the first omitted term, 2 (K/2)^8/8! x 18.5625 = 3.6e-6.

**R2, ray u = 0.8 (alpha = 0.94248), eps = 0, beta = alpha/3 and alpha/2.**
- Z2/Z2_E = 1.00000000 on both.
- Moments for n = 1, 2, 3 are e^{3 pi i n(u-1)/4} times the Euclidean ones to 1e-8.
- J at K = 0.25, 0.5, 1, 2, 3 is 1.98580311+0.00721506i, 1.94347027+0.02850772i, 1.77798240+0.10853155i, 1.17586333+0.35460392i, 0.36990133+0.55829733i.
- The Taylor differences are 5.5e-11, 1.4e-8, 3.5e-6, 8.7e-4, 2.1e-2, the size of the omitted terms.
- The two beta values agree to 4.80e-11 (Cauchy in beta at fixed a-phase).

**R3, R_0.6 (alpha = 0.70686), statement (i).**
- Z2/Z2_E at eps = 0.1, 0.03, 0.01, 0.003, 0 is 0.47795205-0.29446995i, ..., 0.94230430-0.05425313i (eps = 0.01), ..., 1.00000000. The eps = 0.1 and eps = 0.01 values reproduce 053's Z/Z_E (0.4779520-0.2944699i, 0.9423043-0.0542531i) with an independent a-integration.
- At eps = 0, J(K e^{i alpha}) for K = 0.5, 1, 2 is 1.96230323+0.05108393i, 1.84722254+0.19771080i, 1.36525247+0.68817782i.
  - Moments: e^{3 pi i n(u-1)/4} times the Euclidean ones, to 1e-8 (n = 1, 2) and 4.4e-7 (n = 3).
  - Taylor differences at K = 0.25, 0.5, 1: 1.8e-10, 1.4e-8, 3.6e-6.
  - The 053-grid test at the same point (uniform 240x90x90, a different angular rule) gave 1.84721486+0.19769187i, a 2e-5 agreement.
- |<.>_eps - J|/eps for K = 0.5, 1, 2:

  | eps | K = 0.5 | K = 1 | K = 2 |
  |---|---|---|---|
  | 0.1 | 0.0761 | 0.2934 | 1.0137 |
  | 0.03 | 0.0723 | 0.2797 | 0.9785 |
  | 0.01 | 0.0713 | 0.2758 | 0.9681 |
  | 0.003 | 0.0709 | 0.2745 | 0.9645 |

  This is linear approach with a converging slope, a change of at most 2% between eps = 0.03 and 0.003.
- Stokes at eps = 0.1: the same complex kappa evaluated on R_0.4 gives 1.95470454+0.05153900i, 1.81788213+0.19813708i, 1.26530018+0.67112745i, against 1.95470611+0.05153832i, 1.81788827+0.19813459i, 1.26532288+0.67112061i on R_0.6. That is agreement to 2.4e-5, limited by the coarser conditioning of R_0.4. On R_0.4 the observable is not bounded, since arg kappa != 3 pi 0.4/8, and the regulator carries it.

**R4, statement (iii)** (kappa_0 = 1, 2; l = 1.5).
- Smeared limit on R_0.6:

  | eps | kappa_0 = 1 | kappa_0 = 2 |
  |---|---|---|
  | 0.1 | 6.19234814+1.54868425i | 7.04338947+4.33095763i |
  | 0.03 | 6.26566321+1.40429370i | 7.34674029+3.98312822i |
  | 0.01 | 6.28134052+1.36339916i | 7.41759479+3.87887314i |
  | 0.003 | 6.28631019+1.34918489i | 7.44074298+3.84210810i |
  | 0 | 6.28835996+1.34311120i | 7.45040387+3.82631845i |

  |difference|/eps converges, e.g. 2.2689, 2.1752, 2.1468, 2.1367 for kappa_0 = 1.
- At eps = 0 on R_0.5 the values are 6.28836006+1.34311188i and 7.45040371+3.82632040i: the same to 2e-6. This is Stokes at eps = 0 for a bounded observable.
- For orientation: `sqrt(pi) l x 2 = 5.317` is the smeared value of the constant 2, so the timelike smeared Fourier mode is an O(1) complex number with a phase.

**R5, grid check (GF2: about 1.6 times the nodes per direction; angular rule 56 x 12).**
- u = 1: Z2 ratio 1.00000000, max |F_E difference| 4.4e-11, moment ratios 1.00000000.
- R_0.6 at eps = 0: max |J difference| 5.6e-9, max |smeared difference| 2.7e-8.

So the GF values above are accurate to well below the differences quoted. The eps > 0 values were not repeated on GF2.

**What the numerics do not show.** They do not reach real kappa, because the eps = 0 contours there lose the damping. The modulus bound grows like `[sin(4 arg kappa/3)]^{-27/2}`, and at alpha = 0.5 (u = 0.42) four grids give J(e^{0.5 i}) spread over 8e-3, while at alpha = 0.9425 two independent uniform grids reproduce R2 to 1e-7 (`grid_tests.txt`, exploratory, scripts not kept). No numerical statement about the timelike edge is made.

### Literature checked

- **Searches (WebSearch, three queries).**
  - Lorentzian IKKT Wick rotation for Wilson-loop or `Tr e^{ikA}` observables.
  - Hatakeyama et al.
  - Lorentzian IIB Wilson loops with complex Langevin.
- **Findings.**
  - arXiv:2112.15368 (Anagnostopoulos, Azuma, Hatakeyama, Hirasawa, Ito, Nishimura, Papadoudis, Tsuchiya, "Relationship between the Euclidean and Lorentzian versions of the type IIB matrix model"). Per the search summary it is a complex Langevin study on a contour family parametrized by u, from 0 (Lorentzian) to 1 (Euclidean), and states equivalence without a constraint.
  - The 053 references, unchanged.
  - Wilson-loop Schwinger-Dyson work (Tsuchiya slides), which does not treat this question.
- **Not found.** I found no treatment of the eps -> 0 limit of the regulated Lorentzian integral for non-polynomial observables, of smeared Fourier modes, or of the analytic sector of the Euclidean characteristic function.
- **Status of these findings.** The 2112.15368 description is "not independently verified": I read the search summary, not the paper. No novelty is claimed beyond what these searches support.
- **Bibliography.** No new bib entries. The insert cites nothing new.

## Claim classification

| Claim | Class |
|---|---|
| Step 0: Stokes at fixed eps for products of exponential factors, u < 2/3, any N | established (053's argument with exponential-linear growth) |
| (i) eps -> 0 limit equals the eps = 0 integral on R_u for the stated complex momenta | established at N = 2; conditional for N >= 3 (053 flat-direction bound and Z_E != 0) |
| (i) the u = 1 member is the Euclidean expectation value with real momenta | established (identity of integrands) |
| (ii) the formal Euclidean value at phases is not integrable for real kappa != 0 | established at N = 2 (uses 053's sharpness statement, proved at N = 2) |
| (iii) smeared limit equals the line integral of J, any 0 < theta < pi/4; spacelike analogue | established at N = 2; conditional for N >= 3 as (i) |
| (iv) J holomorphic on 0 < arg kappa < 3 pi/4, with the bound 2 [sin(4 arg kappa/3)]^{-27/2} | established at N = 2 (proof given above in sketch form with all estimates named) |
| (iv) F_E holomorphic on \|arg t\| < 3 pi/4, equal to the Euclidean characteristic function for t > 0 | established at N = 2 |
| (iv) spacelike smeared limit is int_R phi(kappa) F_E(e^{i pi/4} kappa^2) d kappa | established at N = 2 |
| (iv) both cases read F_E(e^{i pi/4} k.k), timelike from k.k - i0 | established at N = 2 for axis momenta, in the sense of (i) and (iii) |
| real timelike kappa lies on the boundary ray of the proved sector | established (as a statement about the sector proved, not about F_E) |
| numerical values in `n2_runs.txt` | numerical |
| pointwise eps -> 0 limit at real timelike kappa; continuation of F_E across arg t = -3 pi/4 | unresolved |
| off-axis (boosted) momenta, N >= 3 holomorphy, N -> infinity first, gamma != 0, Definitions (B) and (C) | not stated / unresolved |
| IKKT fermion content, C = 0 | inputs, as in 053 |
| Lorentzian signature in NAMCG | unresolved; Assumption ass:lorentzian stands |

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

**One insertion. No existing text is changed.**
- **Placement.** Immediately before the Problem E Status paragraph, that is after the 053 block, which ends "Problem~E remains open and PROGRAMME-CONDITIONAL.".
- **Anchor.** It occurs exactly once, at line 1512 of the working file, with CRLF between the two lines (61 bytes, sha256 `a7c77412...26cc`, the same anchor bytes as 053 E2):

```latex
\paragraph{Status.}
Remains Assumption~\ref{ass:lorentzian}.
```

- **Byte form.** Insert the CRLF form of `appH_insert.tex` followed by one CRLF (blank line), so the block is separated from the 053 block above and the Status paragraph below by one blank line each.
- **Text kept.** All 053 text, including its closing caveat on non-polynomial observables, stays. That caveat remains true: it scopes the 053 paragraph, and the new block answers it for a stated class.
- **Hashes.** `apply_check.py` (report mode) verifies the baseline hash, the uniqueness of the anchor, ASCII/LF/no trailing whitespace, and prints the result hash. See `apply_check.txt`.

Full text of `appH_insert.tex` (ASCII, LF; 7677 bytes, sha256 `4f5c1301...5bd1`; CRLF form 7693 bytes, sha256 `c4c5b9e2...efcd`; expected result 540271 bytes, sha256 `28e8d36d...4f5b`, CRLF 3220, bare LF 0):

```latex
\paragraph{Fourier observables of the regulated integral (conditional for \(N\ge3\)).}
Keep the setting, Definition~(A) and the contours \(\mathcal R_u\) of the preceding paragraph, and let \(O\) be a product of \(n_{\mathrm{tr}}\) traces, each of a product of factors \(\mathrm e^{\mathrm i\kappa A_\mu}\) with a single index \(\mu\) and a constant \(\kappa\in\mathbb C\). For real \(\kappa\), \(\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\) is the Fourier mode of \(A_0\) with timelike momentum along the time axis that the regulator fixes. On \(\mathcal R_u\) such an \(O\) is bounded by \(N^{n_{\mathrm{tr}}}\mathrm e^{c\|\tilde A\|}\), with \(c\) the sum of the \(|\kappa|\), so for fixed \(\epsilon\) the Stokes argument above still gives \(I_\epsilon[O]\) on \(\mathcal R_u\) for every \(u<2/3\) (exact).

(i) \emph{Complex momenta.} Let \(0<u<2/3\), with \(\kappa=K\mathrm e^{3\pi\mathrm iu/8}\) in each factor with \(\mu=0\) and \(\kappa=K\mathrm e^{-\pi\mathrm iu/8}\) in each factor with \(\mu\ge1\), each \(K\) real. On \(\mathcal R_u\) every factor is then \(\mathrm e^{\mathrm iK\tilde A_\mu}\), which is unitary, so that \(|O|\le N^{n_{\mathrm{tr}}}\) there. The bound along the flat directions without the polynomial factor and dominated convergence give \(\lim_{\epsilon\to0^+}I_\epsilon[O]=I^{(u)}[O]\), the integral on \(\mathcal R_u\) at \(\epsilon=0\), and the ratios converge where the Euclidean partition function does not vanish. The same construction at \(u=1\) gives the Euclidean expectation value of \(O\) with every factor replaced by \(\mathrm e^{\mathrm iK\tilde A_\mu}\).

(ii) \emph{Real momenta.} For real \(\kappa\neq0\) the integrand on the right-hand side of the limit display above, with \(O=\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\), is not integrable at \(N=2\). There \(|\operatorname{Tr}\mathrm e^{\mathrm iz\tilde A_0}|=2|\cos(z\|\tilde A_0\|_{\mathrm{op}})|\ge2|\sinh(\operatorname{Im}z\,\|\tilde A_0\|_{\mathrm{op}})|\), which grows exponentially for \(z=\kappa\mathrm e^{-3\pi\mathrm i/8}\), while the modulus of the Euclidean weight is the integrand of the bound along the flat directions at \(u=1\), so that, since that integral converges exactly for \(k<14\), and by \(\mathrm{SO}(10)\) invariance, it has no moment of degree \(14\) in \(\|\tilde A_0\|_{\mathrm{op}}\). The polynomial result does not extend to these observables in that form.

(iii) \emph{Smearing in the momentum.} For \(\varphi(\kappa)=\mathrm e^{-(\kappa-\kappa_0)^2/\ell^2}\), with \(\kappa_0\) real and \(\ell>0\), one has \(\int_{\mathbb R}\varphi(\kappa)\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\mathrm d\kappa=\sqrt\pi\,\ell\operatorname{Tr}\mathrm e^{\mathrm i\kappa_0A_0-\ell^2A_0^2/4}\), which on \(\mathcal R_u\) is bounded by \(\sqrt\pi\,\ell N\exp\bigl(\kappa_0^2\sin^2(3\pi u/8)/(\ell^2\cos(3\pi u/4))\bigr)\) for \(u<2/3\). Write \(\mathcal J(\kappa)\) for the limit of \(\langle\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\rangle_\epsilon\) given by (i) for \(\kappa\in\mathrm e^{3\pi\mathrm iu/8}\mathbb R\). Dominated convergence on \(\mathcal R_u\), followed by turning the line of integration in \(\kappa\) for fixed \(\tilde A\) onto \(\mathrm e^{3\pi\mathrm iu/8}\mathbb R\), where the trace is bounded by \(N\) and \(\varphi\) still decays like a Gaussian, gives
\[
\lim_{\epsilon\to0^+}\int_{\mathbb R}\varphi(\kappa)\,\langle\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\rangle_\epsilon\,\mathrm d\kappa=\int_{\mathrm e^{\mathrm i\theta}\mathbb R}\varphi(\kappa)\,\mathcal J(\kappa)\,\mathrm d\kappa\qquad(0<\theta<\pi/4),
\]
and the same holds for \(A_j\), \(j\ge1\), with the lines \(\mathrm e^{-\mathrm i\theta}\mathbb R\), \(0<\theta<\pi/12\).

(iv) \emph{Analytic structure at \(N=2\).} At \(N=2\) the Cauchy--Binet bound of the preceding paragraph holds for every phase and \(\operatorname{Re}\mathrm iS_{\mathrm b}=-\sin(\pi u/2)\,S_{\mathrm E}\) holds on \(\mathcal R_u\) for \(0<u<2\), so the integral of (i) on \(\mathcal R_u\) defines \(\mathcal J(\kappa)\) for \(0<\arg\kappa<3\pi/4\), with \(u=8\arg\kappa/(3\pi)\), and \(|\mathcal J(\kappa)|\le2[\sin(4\arg\kappa/3)]^{-27/2}\). This function is holomorphic. The integrand is even in \(\tilde A_0\), so in polar coordinates for \(\tilde A_0\) the cosine may be replaced by one exponential along full radial lines, and the two halves of each line can be turned to phases slightly below and slightly above \(\arg\kappa\) with the phase of the \(\tilde A_i\) fixed; the integrand is then dominated uniformly for \(\kappa\) near a given point. Hence \(F_{\mathrm E}(t)=\mathcal J(\sqrt t\,\mathrm e^{3\pi\mathrm i/8})\) is holomorphic for \(|\arg t|<3\pi/4\), and for \(t>0\) it is the Euclidean characteristic function \(\langle\operatorname{Tr}\mathrm e^{\mathrm i\sqrt t\,\tilde A_0}\rangle_{\mathrm E}\), which by \(\mathrm{SO}(10)\) invariance is the same for every \(\tilde A_\mu\). For \(A_j\) the same steps give \(F_{\mathrm E}(\mathrm e^{\pi\mathrm i/4}\kappa^2)\) for \(-\pi/4<\arg\kappa<0\). Since \(\arg t=\pi/4\) lies inside the sector, the smeared limit for \(A_j\) in (iii) is \(\int_{\mathbb R}\varphi(\kappa)F_{\mathrm E}(\mathrm e^{\pi\mathrm i/4}\kappa^2)\,\mathrm d\kappa\). For \(A_0\) the line integrals in (iii) are integrals of \(F_{\mathrm E}(\mathrm e^{-3\pi\mathrm i/4}\kappa^2)\), and real \(\kappa\) corresponds to the boundary ray \(\arg t=-3\pi/4\). With \(k^\mu k_\mu=\mp\kappa^2\) for the two cases, both read \(F_{\mathrm E}(\mathrm e^{\pi\mathrm i/4}k^\mu k_\mu)\), the timelike case being reached from \(k^\mu k_\mu-\mathrm i0\). At \(N=2\) the reduction of the preceding paragraph, extended by the angular integral over \(\tilde A_0\), gives the following (numerical). On \(\mathcal R_u\) with \(u=0.6\) and \(u=0.8\) the ratios to \(I^{(u)}[1]\) of the integrals of \(\|\tilde A_0\|_{\mathrm{op}}^{2n}\), \(n=1,2,3\), are the Euclidean moments times \(\mathrm e^{3\pi\mathrm in(u-1)/4}\) to within \(5\times10^{-7}\) relative, and \(\mathcal J\) agrees with the polynomial of degree six in \(\kappa\) built from them to the size of the first omitted term for \(|\kappa|\le1\). For \(u=0.8\) two phases of the \(\tilde A_i\) give the same \(\mathcal J\) to \(5\times10^{-11}\). On \(\mathcal R_{0.6}\) the limits in (i) and (iii) are approached linearly in \(\epsilon\), the ratio of the difference to \(\epsilon\) changing by at most \(2\%\) between \(\epsilon=0.03\) and \(\epsilon=0.003\). The smeared limit at \(\epsilon=0\) is the same on \(\mathcal R_{0.5}\) and \(\mathcal R_{0.6}\) to \(3\times10^{-6}\).

For these observables, this order of limits and \(\gamma=0\), the regulated integral therefore gives at finite \(N\), conditionally for \(N\ge3\), the integrals at \(\epsilon=0\) on the contours \(\mathcal R_u\), and at \(N=2\) values of the continuation \(F_{\mathrm E}\) of the Euclidean characteristic function, or line integrals of them, which \(F_{\mathrm E}\) on \(t>0\) determines. The Euclidean value at phases is not available for real timelike \(\kappa\). This is no statement about \(\langle\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\rangle_\epsilon\) pointwise at real \(\kappa\) as \(\epsilon\to0\); about whether \(F_{\mathrm E}\) continues beyond \(\arg t=-3\pi/4\); about momenta off the coordinate axes, which combine matrices with different phases on \(\mathcal R_u\); about holomorphy for \(N\ge3\); about \(N\to\infty\) taken first; or about \(\gamma\neq0\) and Definitions~(B) and~(C). It does not derive a signature, a background, a frame or the fermion content, and Assumption~\ref{ass:lorentzian} is not discharged. Problem~E remains open and PROGRAMME-CONDITIONAL.
```

**Labels and citations.**
- `\ref{ass:lorentzian}`: defined once (ch04 L322). Verified by byte count over chapters/*.tex.
- No new labels, no new `\cite`, no `\eqref`.
- The insert refers to "the preceding paragraph", "the limit display above", "the bound along the flat directions" and "Definition~(A)" in the 053 block, which is the paragraph immediately above it. No hard-coded numbers.

**Stale passages elsewhere.**
- None. The 053 closing sentence ("This is no statement ... about non-polynomial observables such as ..., which grow on R_u, so that the domination above fails for them. It does not exclude a real-time reading obtained by continuation.") stays correct as a scope statement of that paragraph.
- ch04 L325 ("Dynamical emergence of this signature from a Euclidean matrix model is not proved") and ch17 L394-399 stand.

### `bib/namcg.bib`

No change.

## Verification scripts

All are in `proposals/054-lorentzian-fourier-observables/`. Outputs are saved as `.txt`.

- `n2_fourier.py`: the N = 2 engine (module). It is self-contained, does not import from 053, and uses a multiprocessing pool.
- `check_a_integral.py` -> `check_a_integral.txt`: the polar at-integral against direct 3D Gauss-Legendre quadrature, at four sample W and contours, for the specs cos (real and complex zeta), Gaussian-shifted cos and moments n = 1, 3. The maximal relative difference is 6.9e-7, and the Z spec agrees with the closed Gaussian-moment formula to 1e-8 or better.
- `exact_checks.py` -> `exact_checks.txt`: sympy checks of the smearing identity, the bound on R_u, the unitarity phases, the arguments of F_E and the k.k - i0 side, the |cos| inequality, the scaling exponent 27/2, and the (alpha, beta) form of Re(i S_b). It also gives the sampled Cauchy-Binet check for u in (0, 2).
- `n2_runs.py OUTFILE` -> `n2_runs.txt`: the numerical sections R1-R5. It refuses to overwrite its output.
- `grid_tests.txt`: saved output of exploratory grid tests (scratch scripts not kept). It is used only for the conditioning remark and is not relied on for any claim.
- `apply_check.py [OUT]` -> `apply_check.txt`: the report-mode insertion check. It writes only outside the repository if given a path, and refuses to overwrite.
- **Scratch build** (outside the repository): `git archive HEAD` (without proposals/reports) into the scratchpad, appH replaced by the `apply_check.py` output, then pdflatex, bibtex, pdflatex, pdflatex. The result is recorded directly below.

**Scratch build result.**
- **Tree.** `git archive HEAD` (4973019, without proposals/ and reports/) into the scratchpad. Its appH equals the working appH (sha256 `7a75554e...`).
- **Change.** appH was replaced by the `apply_check.py` output (540271 bytes, `28e8d36d...4f5b`).
- **Passes.** pdflatex, bibtex, pdflatex and pdflatex all exited 0 on a first version of the insert. After the final wording change (the moments sentence of (iv)), three further pdflatex passes on the final insert also exited 0. The bib is unchanged.
- **Log.**
  - 359 pages (053's build: 357).
  - 0 "undefined" lines in the log, no multiply-defined labels, no rerun warning.
  - No BibTeX warnings.
- **Rendering.** The only overfull box near the insert is at lines 1536-1540 of the new file, the Problem F ledger label, which was already there before the insertion. pdftotext of the new block shows it renders as intended.
- **Cleanup.** The repository was not touched. The scratch tree is outside it.

## Decisions Taken

1. **Target: 053's rank-1 avenue rather than the scout's R2.** Reasons:
   - (a) It concerns the integral itself, the first item the scout lists as avoided.
   - (b) It closes, for a stated class, the explicit "non-polynomial observables" exception of 053. This is the only place where 053 left a route to a non-Euclidean datum open by name.
   - (c) It could be done rigorously at N = 2 with reviewed machinery.
   - (d) R2 relies on a criterion whose equation numbers and warnings the scout read second-hand. Its expected result for CP^{1,2} is that paper's own claim (2605 Eq. 115), so it would need a separate source-verification effort. It also tests supplied classes. Its decision value is real and it stays queued (see Remaining open step).

   Rejected: doing both in one package, because they share no derivation.
2. **Observable class.** I took coordinate-axis momenta and products of traces of products of single-index exponentials, the largest class for which the contour makes every factor unitary. Boosted momenta are excluded and stated as such.
3. **Order of limits.** Fixed N, eps -> 0 first; in (iii), l and kappa_0 fixed while eps -> 0. gamma = 0, so 053's gamma statements are not extended here.
4. **Holomorphy only at N = 2.** For N >= 3 the radial evenness argument needs a spectral treatment of A_0 that I did not do. Statements (i) and (iii) do not need it.
5. **Numerics confined to the well-conditioned window** (u >= 0.5 for eps = 0 contours). The modulus bound `[sin(4 arg kappa/3)]^{-27/2}` against |J| = O(1) shows how much cancellation a direct evaluation near the real axis must carry. At u = 0.42 four grids give values spread over 8e-3 (`grid_tests.txt`). The pointwise real-kappa question is therefore left to a later package with a different method, and no pointwise claim is made.
6. **No bib entry for 2112.15368.** It is not needed for the insert, and I could not verify its content beyond a search summary.

## Milestone assessment

- **Candidate M2 (bounded no-go extension), not a breakthrough.** The manuscript (053 block) keeps open "non-polynomial observables such as Tr e^{ik^mu A_mu}". For the class stated, the package shows that the regulated Lorentzian integral with eps -> 0 first gives only analytic continuations of Euclidean data, and at N = 2 the continued Euclidean characteristic function.
- **Hypotheses of the bounded result:**
  - N = 2 proved, N >= 3 conditional;
  - IKKT content and C = 0 as inputs;
  - Definition (A) with the delta_{mu nu} Gaussian regulator;
  - eps -> 0 first and gamma = 0;
  - axis momenta, complex on the stated rays or Gaussian-smeared.
- **Why only bounded.** It does not exclude a pointwise real-time function at real timelike kappa, because that is the edge question. The gatekeeper decides whether this counts as M2 or as routine sharpening.
- No merged claim is found wrong (no M3). No label change (no M4). No core change (no M5).

## Status-label recommendation

- **Current critical-path list**, from ch17 L695-722 and the Appendix H labels: A, B, C, D1, E, F, G-derived, N.
- **Affected:** E only. Recommendation: unchanged (OPEN; CRITICAL PATH for the matrix-derived label; PROGRAMME-CONDITIONAL).

## Author decision needed

None for this package.

The scout's author-level question stands as recorded in the 053 ledger entry: what "Lorentzian signature derived" means when eta sits in the action. This package adds one piece of evidence relevant to it: with eta in the action and eps -> 0 first, the real-time Fourier modes along the axes are continuations of Euclidean ones.

## Remaining open step

**For the original target:** a derivation of Lorentzian signature, with Assumption ass:lorentzian discharged. Nothing here supplies it.

**Hypotheses the bounded result depends on, and the relaxation for each:**

| Hypothesis | Relaxation | Status here |
|---|---|---|
| Pointwise real timelike kappa | Edge regularity of F_E at arg t = -3 pi/4, or continuation across it | Open; numerically ill-conditioned by the direct method |
| N = 2 for (iv) | Spectral (eigenvalue) version of the radial argument for N >= 3 | Open |
| N >= 3 conditional for (i) and (iii) | Independent proof of 053's flat-direction bound | Open (as 053) |
| Axis momenta | Lorentz covariance of the eps -> 0 limit for non-polynomial O | Open; on R_u a boosted k.A mixes phases and is not unitary |
| eps -> 0 first | N -> infinity first | Open (053 rank 2) |
| gamma = 0 | gamma < 0 retained (likely as in 053), gamma > 0 (deformation) | Not treated |
| Definition (A) | Definitions (B) and (C) | Not treated |
| Continuation as "Euclidean data" | Whether the continuation has a positive real-time reading (Osterwalder-Schrader type) | Open |

**Ranked open avenues:**
1. **Edge regularity of F_E at N = 2.** Does F_E continue across arg t = -3 pi/4, and does the pointwise eps -> 0 limit at real timelike kappa exist and equal the boundary value? This decides whether a real-time Fourier mode exists as a function, and whether it carries singular (light-cone) structure. A method that avoids the cancellation is needed, for example an explicit one-variable representation of F_E (the radial marginal of A~_0) continued analytically.
2. **Positivity of the continuation.** Reflection positivity, in the form of 052's reflection statement, applied to the N = 2 Euclidean characteristic functions. If it holds, the continuation in (iv) would be a real-time reading with a Hilbert space. That is the NAMCG-favourable reading, and it keeps spacetime emergent.
3. **Boosted momenta,** that is Lorentz covariance of the non-polynomial limit.
4. **N >= 3:** the 053 bound and holomorphy.
5. **N -> infinity first,** from a controllable model.
6. **The scout's R2** (semi-classical self-consistency of the CP^{1,2} x K and commuting-fibre classes against 2605.13294), still queued as the class-level decision test. Order of limits for R2, given 053 and this package: the semi-classical regime must be posed either at fixed eps or with N -> infinity first. With eps -> 0 first at finite N, the expectation values covered by 053 (polynomial, degree < 14) and by this package reduce to Euclidean data or its continuation (proved at N = 2; for N >= 3 conditionally, and for the observables here only as R_u integrals). So a semi-classical test posed in that order would be a Euclidean test.

## Special instructions for the gatekeeper

- **Scope.** Do not let the insert or the record read as a derivation of signature, or as ruling out a real-time reading. The result realises a reading by continuation and leaves the pointwise timelike edge open.
- **Re-derive:**
  - the unitarity choice of phases on R_u;
  - the Step 0 boundary estimate;
  - the smearing bound `kappa_0^2 sin^2(alpha)/(l^2 cos 2 alpha)` and the turning of the kappa-line;
  - the scaling exponent 27/2;
  - the holomorphy argument: evenness, the bent half-lines, the domination constant `min(sin 4 beta_*, sin(2 phi_+- - 2 beta_*))`, and the boundary-term sequence argument;
  - the identification `J_s(kappa) = F_E(e^{i pi/4} kappa^2)` and the k.k - i0 side.
- **Statement (ii)** relies on 053's "converges exactly for k < 14" at N = 2. Please confirm that this is how the accepted 053 text is to be read (the Euclidean modulus equals the bound integrand on R_1).
- **Symbols.** The insert's "the bound along the flat directions, used without the polynomial factor" means 053's bound with k = 0. I avoided the letter k for momentum because the 053 block uses k for the degree. Check that no symbol in the insert collides (kappa, K, theta, phi, l, n_tr, J, F_E are new to that section).
- **Scan.** No full scan was done and none is claimed. Integration ordinal would be 52, not a 5th item. The insert changes no definition, assumption, scope or status passage.
- **Folder.** The integrable text is `appH_insert.tex` only.

**Process notes.**
- Tool calls were serial, except background jobs. Exploratory grid tests t5-t7 overlapped in time with each other and with the production run, which only slowed them. Their outputs are saved in `grid_tests.txt`.
- I tried to list those processes in order to stop them, and the classifier denied this. I did not try to route around the denial; the jobs ran to completion.
- `n2_fourier.py` in the folder is the final engine. HEAD 4973019 contains an early draft of it, committed by the author.
- No file outside `proposals/054-lorentzian-fourier-observables/` was written, apart from the session scratchpad. No git write command was run.
