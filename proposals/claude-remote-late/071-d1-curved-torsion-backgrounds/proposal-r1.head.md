# Proposal 071-d1-curved-torsion-backgrounds, round 1

## Result

**What is established.**
1. **Exact backgrounds with curvature and torsion both nonzero.** In the first-order equivariant class, on left-invariant data with a *nonzero constant* connection `w_a^{cd}`, two explicit families solve the first two brackets of the matrix equation exactly, for symbolic parameters, with `R != 0` and `T != 0`. (i) A flat frame (`c = 0`, frame metric Minkowski) with `w = s k (x) B + m (x) N`, on the hyperbola `(m_1 - s)^2 - m_3^2 = s^2`. (ii) Time x Heisenberg (`[E_3,E_1] = kappa E_2`) with `w = k (x) (zeta N + x N')`. Here `k_a = (1,0,1,0)` is null, `B` is the boost in the 0-2 plane, and `N, N'` are null rotations fixing `n = -k`. Both families have rank-one, null-type curvature (`R_abcd R^abcd = 0`) with nonzero Ricci tensor `R_ab^{ae}`, which the torsion terms cancel in the first bracket. The third bracket holds: (ii) and the trace-free point of (i) need `t = 0`, and the general point of (i) has `F = -c t = 0`. This supplies the missing input that the frontier edge names: "a background with both R != 0 and T != 0 that solves the matrix equation (no source read supplies one)". The section values were also checked at the operator level, on the bundle, against the vector fields themselves.
2. **Linearised equations at `R != 0` on family (i).** These generalise (R1)/(R2) of the integrated 068 paragraph:
   - The translation labels still reduce exactly to the gauge-invariant order-zero operator `Q`, which now contains the connection. The labels carry a connection part `omega = -f w_I`.
   - (R1) fails: the connection equations depend on `h`.
   - The forty equations remain block-triangular in the variables `(f, omega')`. The 24-equation connection block `Y` has generic rank 18 and is not six copies of `Q`.
   - The kernel is the ten gauge directions. The diffeomorphism directions now need the term `omega = xi^c R_ca`.
3. **No gauge-invariant mass or gap on family (i)** (hazard F3 respected).
   - Every characteristic root found lies on a null cone shifted along `k`: `(q - alpha k)^2 = 0`, with `alpha` in a finite set (numerical).
   - The background has an exact boost-dilation symmetry, under which `w -> e^{-theta} w`. Because of it, the set of values of `q^2` on the characteristic variety is invariant under every positive rescaling. So no mass shell `q^2 = -m^2` is isolated, and the background has no invariant scale (rigorous, given the symmetry).
   - The non-derivative terms are nonzero, but they produce cone shifts, not masses.
   - Imaginary shifts give section values that grow along the null coordinate `k.y`. No norm is used, so no stability claim is made.

**What is not established.** None of this closes D1. The class, its algebra `A`, these backgrounds, the frame and its non-degeneracy are not selected by the matrix integral. There is no norm and no regulated trace, and everything is tree level and linear order. Family (ii) and the non-null survey solutions are not linearised. Problems D, F and N remain OPEN and PROGRAMME-CONDITIONAL.

## Target and status

- **Problem:** D (D1 route), `sec:status-D`. Ledger (appH L718-721): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2 ... D remains OPEN and the matrix-derived criterion is unmet."
- **Original target** (ch17 L330-343, L650-653, L712-716): derive local SO(3,1) from the matrix algebra and condensate, specify the `omega, A_mu, B` and ghost operators and the field content, and derive the existence and non-degeneracy of the locked frame.
- **Missing step** (appH L745-756): "derive the effective dynamics of the independent diagonal connection or retain it as unresolved field content. Generator counting alone does not settle its torsion or propagating modes." This package attacks the "torsion or propagating modes" item. It does so on the first backgrounds where the 068 reduction (R1) can fail, which is the gap named in the 068 review (avenue (c)).
- **Dependencies:** ch17 L650-653: D1 supplies the operators consumed by F. F gates N, and C is tied to F through `G_eff` (appH L712). D1 is the upstream gating problem, so it was attacked first, per the derivation-first directive.
- **Completion classification:** PROGRAMME-CONDITIONAL (unchanged).
- **Discrepancies between ch17 and appH:** none found for D. The CRITICAL PATH OPEN set at full-GR scope is A, B, C, D, E, F, G, N (8). H, I and J are OPEN and OPTIONAL (3). The total is 11 OPEN, and all are unchanged by this package.

## Source reading

- **Mode:** digest + targeted reads. `make_digest.py --check` printed `DIGEST CURRENT`. The digest flags `dirty-chapters: yes`, because appH and bib are uncommitted from the 068/069 integrations. The live appH sha256 is `d8d8b678...9180`, which matches the dispatch.
- **Read in full:**
  - appH L715-760 (the Problem D ledger, the missing step and the opening);
  - appH L1496-1630: the conjugate-coordinate frame-index paragraph, the class paragraph, the pairing/commutant paragraph, the one-loop/reflected-form paragraph, the 059 compact toy, the locked-frame composite, and the 068 paragraph;
  - ch17 L328-371 (Problem D) and L645-716 (order and criteria);
  - ch10 L1-310 (groups, locking, eq:dressed-omega, prop:B-torsion-free).
- **Labels used and verified** (each defined once in `chapters/*.tex`): `eq:Smatrix`, `ass:frame-lock`, `ass:nondeg`, `ass:lorentzian`, `ass:local-lorentz`, `ass:EFT-a2`, `ch:vierbein-emergence`.
- **Other sources read:** the 068 proposal folder (core.py and tools.py, copied here as `core068.py`/`tools068.py`), its review-r2-final, `reports/pathfinder/plan-2026-11-21b.md`, and the frontier edge `D1.R-T-nonzero-backgrounds` (used as a pointer only).
- **No full scan.** This package changes no definition, assumption, scope statement or status passage.

## Research and reasoning

### 1. Class reduction for left-invariant data with constant connection
- **Setup.** Take a 4-dim Lie group with `[E_a,E_b] = c_ab^d E_d` and constant connection components `w_a^{cd}`. Then `Om_ab^c = w_a^{cd} eta_db`, `T = -c - Om + Om^T` and `R_ab^f_c = Om Om - Om Om - c Om`. These are constants. The brackets reduce to polynomial equations (bg.py):
  - `B1 = -nabla^a T_ab^e + T T + R_ab^{ae}`;
  - `B2 = nabla^a R - T R`, where `nabla` acts algebraically through `Om`.
- **Operator-level check (s0).** The formulas were checked independently on the bundle, which is embedded in `G x GL(4)`. There `S_cd` acts on the first index of `u` and `D_a = u_a^b(E_b + (u Om_b) d/du)`. The check covers four things:
  - the first relation;
  - `T(u)` and `R(u)` read off from `[D_a,D_b]`, compared with the Lorentz-rotated section values;
  - the vector field `eta^{ac}[D_c,[D_a,D_b]]` at random Lorentz `u`;
  - a control (random `W`, not a solution), which gives a residual of 78-140.
- **Hermiticity.** For trace-free torsion `t = 0`. Otherwise `t_a = 1/2 T_ac^c` (constant section values). Since `[V_a+t_a, V_b+t_b] = [V_a,V_b] + V_a t_b - V_b t_a`, we get `F_ab = nabla_a t_b - nabla_b t_a + T_ab^c t_c`. With constant components, `nabla_a t_b = Om_ab^c t_c`, so `F_ab = (Om_ab^c - Om_ba^c + T_ab^c) t_c = -c_ab^c t_c`, which is zero on a flat frame. The `t` part enters only the third bracket.

### 2. Search and exact families
- **Least-squares survey (s3, numerical).**
  - Flat frame, `eta`: 59 of 60 starts converge and 56 of them have `R != 0`, all with `R_abcd R^abcd = 0` (to `3e-15`).
  - Flat frame, Euclidean: no start converges. This is numerical, not a proof. A trace identity was tested and `tr B1` is not sign-definite.
  - With `c` free and Jacobi imposed: 4 stored solutions on algebras with a 2-dim abelian derived algebra. Three of them have `R_abcd R^abcd != 0` (`-7e-4`, `9e-4`, `-4e-3` at `|R| ~ 0.1`).
- **Sparse/ansatz search.** It found two clean families. Both are verified exactly by `s1_backgrounds.py` (sympy, symbolic in `s, m1, m3 / tau, kappa, zeta, x`).
  - **(i)** Ansatz `w = s k B + m N`, `m = (0,m1,0,m3)`. Here `B2 == 0` identically and `B1 ∝ m1^2 - 2 m1 s - m3^2`. The rational parametrisation is `m1 = s(1+(tau+1/tau)/2)`, `m3 = s(tau-1/tau)/2`. Then:
    - `R_ab^{cd}` takes values on the line of N, has rank 1, with entries `s m1`, `s m3`; so `R != 0` iff `s != 0` and `m != 0`;
    - `R_abcd R^abcd = 0`, `T_abc T^abc = 0`, `R_ab^ab = -2 s m1`;
    - the trace is `(s+m1) k`, which is trace-free at `tau = -2+sqrt3`, i.e. `m = (0,-s,0,sqrt3 s)`;
    - the Ricci tensor is nonzero.
  - **(ii)** Heisenberg family. The general `k (x) X` ansatz leaves the second bracket equal to `k_2 kappa X (x)` (four linear forms). Solving those forms for `k = (1,0,1,0)` gives `X in span(N, N', B)`. Every `B1` entry then also vanishes for `X = zeta N + x N'`, which is exact for symbolic `kappa, zeta, x`. Then:
    - the only nonzero curvature pair is `R_13^{cd} = kappa(zeta N + x N')`;
    - `T_abc T^abc = 2 kappa^2`, the torsion is trace-free, and `RR = R_ab^ab = 0`.
- **Explored avenue: isotropic backgrounds** (x1, x1b; exact).
  - Flat frame with the general SO(3)-invariant constant connection `w_i = alpha J_i + beta K_i`: `B1_00 = 3 s beta^2`, so `beta = 0`, and then `B1_ii = -6 alpha^2`, so there is no solution.
  - R x S^3 with static isotropic torsion: `B1_00` forces `beta = 0`, and then `-2 kappa^2/a^2 + 6 kappa alpha/a - 6 alpha^2 = 0` has negative discriminant, so there is no real solution. In particular the totally antisymmetric "lambda-connections" of a bi-invariant metric fail.
  - The time-dependent flat FLRW ansatz with `alpha = 0` reduces to `beta' = -s beta^2` and `a''/a = 3 beta^2 + 3 beta H + 2 H^2` (Lorentzian). The second and first brackets are consistent (a Noether identity), so local real solutions exist, but they are singular at finite `t` and are not pursued. This is recorded only in the proposal, not in the insert.

### 3. Linearisation on family (i) (s2; `core068.M_op`)
`core068.M_op` is the 068 linearisation of the closed bracket formulas. It accepts any constant `cbar, wbar`.

**(a) Gauge kernel.** The gauge directions must include `omega_a^{de} = xi^c R_ca^{de}` for diffeomorphisms. The derivation is `[xi^c D_c, D_a] = -(D_a xi^c) D_c + xi^c(-T_ca^e D_e + 1/2 R_ca^{de} S_de)`. Without this term `|M G| ~ 4-12`; with it `|M G| ~ 3e-15`. At generic real `q` the rank is 30 and the kernel is spanned by `G`.

**(b) (R1) fails.** `|dB2/dh| ~ 9-10` at the samples, against exactly 0 on the 068 Heisenberg background.

**(c) Generalised (R2).**
- The translations `∂_I` commute with `D_a` and `S` (constant coefficients).
- At `u = 1`, `∂_I = D_I - vert(w_I)`, and the vertical field of right multiplication by `Om_I` equals `1/2 w_I^{cd} S_cd`.
- So the fluctuation `1/2{f_a, ∂_I}` has section values `h_a^c = -f_a δ^c_I` and `omega = -f_a w_I`.
- The adjoint compatibility `E_b[1/2{f,C}] = 1/2{E_b[f],C}` (appH pairing paragraph) maps it to the operator `(Qf)_b ∂_I`, whose bracket components are `B1 = (Qf) δ_I` and `B2 = -(Qf) w_I`.
- `Q` is the linearised third bracket, with `nabla` containing `w`.
- Numerically the residual is 2e-15 for both points of (i), at 3 random `q` each.

**(d) Block-triangular form.** This follows from (c) exactly. In `x' = (f, omega')`, with `f^I = -h^I` and `omega' = omega - h^I w_I`, and outputs `g^I = B1^I`, `B2' = B2 + B1^I w_I`, the label image `u_I(g)` has `B2' = -g w_I + g w_I = 0`. Hence `dB2'/df = 0` (numerically 5e-15). The 24x24 block `Y` has rank 18: 6 rotation directions project into it.

**(e) Roots.** `char_roots` (068 tools) was run along `q = (t, kvec)` for 4 `kvec`, with two random compressions. Every root satisfies `q^2/(2 k.q) = alpha`, constant across lines.
- At the trace-free point (`s = 1`): `alpha in {±√3, ±√3 ± i, ±√3 + 2i}`; `Q` gives `±√3` only; `Y` carries all of them.
- At `tau = 1` (`m = (0,2,0,0)`): `alpha in {-i/2, -3i/2, -5i/2}`; `Q` gives `-3i/2`.
- Converse (rank drop at random complex points of each cone, sigma_30/sigma_1): about 1e-16 at `tau = 1`, against 1e-3 at control points, so it is clean there. At the trace-free point the ratio is 3e-10 to 5e-5, against 1e-4 to 3e-3 at control points. The separation is weak there, consistent with defective (Jordan) roots, and the insert says so.

**(f) Boost-dilation symmetry** (exact, by hand; numerical 1e-16).
- Under `exp(theta B)`, `n` has eigenvalue `-1`, so `k_a -> e^{-theta} k_a` and `[B,N] = -N`, i.e. `N -> e^{-theta} N`. `B` and `m` (which lives in the 1-3 plane) are fixed. Hence `w -> e^{-theta} w`.
- `D -> lambda D` is a symmetry of the cubic homogeneous equation. On the flat frame it is `w -> lambda w` together with `y -> y/lambda`, so `V(lambda w) = lambda V(w)` for the characteristic set `V`.
- Combined with Lorentz covariance `V(L w) = L V(w)`, this gives `V = e^{±theta} L_theta V`, so `{q^2 : q in V}` is invariant under every positive rescaling.
- Consequence: if `q^2 = -m^2` occurs, so does `-lambda^2 m^2` for all `lambda > 0`. There is no isolated mass shell and no invariant gap scale. This is the precise sense of "no gauge-invariant mass" claimed, and it does not rest on the numerical roots.

**F3 hazard.** `M(0) != 0`: the non-derivative terms are present. By (e) and (f) they do not create a mass. The imaginary `alpha` are of the form `e^{beta k.y}`, which looks like a local boost weight. That reading is not claimed as a removal, because after the pure-gauge local boost `exp(s (k.y) B)` the `N` term becomes `y`-dependent.

**Comparison with the original target.** The result gives the operator content (`Q` with connection, the `Y` block, the gauge kernel) on the first `R != 0`, `T != 0` backgrounds. It also shows that this null family neither gaps nor reorganises the torsion/Lorentz modes into massive ones. It does not derive SO(3,1), the frame, the selection of the class, or a norm, so the D1 target remains open.

**Literature.** No new citations. The bracket formulas and the class come from the integrated paragraphs, whose citations (HKK 2006, FHKK 2007) were not re-verified here. No literature result is imported.

## Claim classification

| Claim | Class |
|---|---|
| (i), (ii) solve brackets 1-2 for symbolic parameters; invariants as listed | established (exact, sympy, s1) |
| Section values match the operator relations on the bundle; matrix-equation vector field vanishes | numerical (s0, residual < 1e-13; control 1e2) |
| `F = -c t` for constant section values, hence third bracket holds on (i) | established (by hand) |
| Survey counts; no Euclidean flat solution; RR != 0 solutions on solvable algebras | numerical, not a classification (s3) |
| Isotropic static and flat isotropic no-go (in the stated ansatz) | established (exact, x1/x1b), recorded in proposal only |
| Gauge kernel = 10 directions with `xi R` term | numerical (s2 (a)); the formula for the gauge directions is established (by hand) |
| (R1) fails at R != 0 | numerical (s2 (b)) |
| Translation-label reduction to Q with connection part | established by adjoint compatibility + commutation; numerical check 2e-15 |
| Block-triangular form, rank-18 connection block | the triangularity is established (follows from the label identity); the rank is numerical |
| Roots on shifted cones with the stated alpha | numerical (s2 (d), (f)); converse clean at tau = 1, weak at the trace-free point |
| Boost-dilation symmetry; no isolated mass shell / no invariant scale on (i) | established (by hand, given the symmetry; numerical check of the symmetry) |
| No stability statement for imaginary shifts | scope statement |
| Selection of the class/backgrounds, frame, non-degeneracy, norm | unresolved |
