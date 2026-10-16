# Proposal 017-GT-GA-gap, round 2

## Result

Target: Problem B (normalisation half of B1/B2), the bounded gap of integrated proposal 015: in the Poisson-limit class (Euclidean section, background gauge, one loop, `Lambda^2` term, replica (I), the two modes with `delta rho = 0`) `c_T = N_tot/6 - 4` against `c_A = N_tot/6`, `1/G_A - 1/G_T = 2 Lambda^2/pi`. This is a bounded no-go with sharpening; it closes nothing.

Within that class and for the stated tip domain: (i) the gauge parameter `alpha` of the connection sector does not move the gap: exact lemma `O_v Gr = Gr O_s - {J,.}` gives cancellation of `alpha` for every `alpha > 0` on `J = 0` backgrounds (conditional on domain, zero modes, common cutoff), and numerically (rational fits to `2e-3`, not derived) for `1/3 <= alpha <= 3` off shell; (ii) an EOM term in the gauge function only enlarges the gap (numerical, two backgrounds); (iii) Dirac content shifts the weight of `rho^2 X` to `1 - n_D/2` (zero at `n_D = 2`), but the gap then depends on the replica gluing: `4 - n_D` (antiperiodic polar-frame gluing), `4 - 2 n_D` (unrotated periodic gluing; at `n_D = 2`, `N_s = 6` both `c_T` and `c_A` vanish, an equality of vanishing `Lambda^2` coefficients, not a derivation), `3 - n_D` or `5 - n_D` (rotated vector). The gluing selected by the matrix state is a Problem A question and is not determined here.

| # | Avenue | Outcome | What was found |
|---|---|---|---|
| 1a | 't Hooft background gauge (SME 1) | bounded | Exact lemma; on `J = 0`, `a_1 = ((3+alpha)/6) rho R + rho^2 X`. Off shell about constant `Theta_bar`: TT `5/6 - (alpha-1)/24`, third mode `1/2 - (alpha-1)/8 + (alpha^2-1)/4` (rational fits, `<= 2e-3`, `alpha = 1/3..3`). `c_T(alpha) = (N_s+alpha-1)/6 - 11/3`, `c_A(alpha) = (N_s+alpha+1)/6` for the stated domain: gap 4 in the tested range. |
| 1b | EOM-proportional part | bounded | Remainder `((alpha^2-1)/2) rho|grad ln rho|^2` acts on the `delta rho != 0` mode only (numerical). |
| 1c | SME three-mode ratio test | corrected | Net ratio 3 at `alpha = 3` with gap still 4: the ratio is not a gauge-invariant diagnostic of `rho^2 X` (fit-dependent). |
| 1d | EOM term in gauge function | bounded | Adds `+c^2 rho^2 J.J`; lowers `c_T` at fixed `c_A` (numerical, two backgrounds). |
| 2a | Fermions, `b_total` (SME 2) | shifts | `a_1 = (4/6) rho R + (1/2) rho^2 X` per Dirac field; `b_total = 1 - n_D/2`; `n_D = 2` = 16 real components of the 10D content (identification). Yukawa couplings to the transverse matrices vanish on the background. |
| 2b | Fermions, gap, by gluing | shifts | Antiperiodic: `c_A(Dirac) = +1/3`, gap `4 - n_D` (zero at `n_D = 4`, `b = -1`; at `n_D = 2`: `c_T = 0`, `c_A = 2`). Periodic unrotated: `c_A(Dirac) = -2/3`, gap `4 - 2 n_D` (zero at `n_D = 2`, `c_T = c_A = 0`). Gluing: Problem A. |
| 2c | Torsion-coupled scalars `E = xi X` | bounded | Shifts the gap by `-4 xi`; no matrix origin. |
| 3a | Rotated vs unrotated connection cone (SME 4) | shifts | Gap `3` (`n<1`) or `5` (`n>1`) at `alpha=1`, bosonic content; not analytic at `n = 1`. |
| 3b | Kabat / centre choice (SME 3) | size only | Contact term `1` in these units (Solodukhin (126), (147)) against gap `4`: an order-of-magnitude observation; `alpha`- and domain-dependence of such terms not established. |
| 3c | Replica (II) (SME 5) | bounded | Equality at `N_s = 14 - 4 n_D`; at `n_D = 2`, `N_s = 6` both sides vanish. Not claimed physical. |

Where the missing ingredient sits: for bosonic content the gap is `4` times the weight of the cone-blind torsion-squared term `rho^2 X`, independent of `alpha` and `N_s` in the tested class; with fermions its value is fixed by the replica gluing, so the gluing and the next-order coefficients are the data to find.

Problem B stays OPEN. Nothing here derives `ass:EE`, stationarity, the map `Theta -> G`, a value or sign of `G_eff`, or the matrix origin of fermions.

## Changelog against r1
| Finding | Action in r2 |
|---|---|
| F1 (major) | Deleted the tip-domain justification ("a finite set of angular modes has a scale-free transverse trace") from the LaTeX, the Research section and row 3b. The text states the area coefficient `(3+alpha)/6` for the stated domain and that other domains are not examined (snippet (a)). Row 3b's "alpha-independent tip-local ambiguity of O(1)" is withdrawn; "Kabat cannot remove a gap of 4" is an order-of-magnitude observation (1 against 4). |
| F2 (major) | LaTeX: "numerical second-order evaluation", "values, matched by the rational forms", "rational fits to 2e-3, not derived; alpha = 1/3,...,3 only"; the gap `2 Lambda^2/pi` is stated for the tested range `1/3 <= alpha <= 3`, and "every alpha > 0" only on `J = 0` backgrounds under the stated conditions (snippet (b)); the TT-agrees-with-lemma sentence kept. Headline and claim table adjusted. |
| F3 (major) | LaTeX: periodic unrotated Dirac gluing reported (`c_A(Dirac) = -2/3`, gap `4 - 2 n_D`, zero at `n_D = 2` with `c_T = c_A = 0`, an equality of vanishing `Lambda^2` coefficients, not a derivation); antiperiodic gluing identified as the polar-frame/rotated-spinor prescription, not the unrotated pull-back; closing statement "2 for antiperiodic, 0 for periodic"; gluing assigned to Problem A; "numerology" dropped; r1's remark that periodic gluing "is not the replica of a state" withdrawn (snippet (c)). Decision 4 of r1 superseded. |
| F4 | Gradient map renamed `\mathrm{Gr}` (was `\mathcal G`, the backreaction tensor); EOM vector renamed `\mathfrak J_\nu` (was `E_\nu`; `E_f` stays the endomorphism). Neither macro occurs in `chapters/`; no doubly-subscripted new macro. |
| F5 | One clause added: the Yukawa couplings `\Gamma^i[\hat X_i,\Psi]` to the `N_s` transverse matrices vanish on the background and are dropped. |
| F6 | No edit (as the review states). |
| Avenues | "Remaining open step" replaced by the review's ranked avenues (most promising: next-order comparison per gluing; replica gluing from the matrix modular flow). Not explored here. |

Unchanged from r1: the exact lemma, the numerics, all scripts (`gap_periodic.py` and output added), the anchor, the labels. `appH_insert.tex` is identical to the LaTeX block below (checked by script).

## Target and status

Problem B (`sec:status-B`): Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL (appH, ch17 `sec:ch17-done`, `reports/ledger.md` agree; no discrepancy found). Chapter 17 critical-path set at the matrix-derived scope: A, B, C, D1, E, F, G-derived, N (H, I, J optional). Original target of B: derive fixed-volume tensor-block stationarity from the microscopic action, `Assumption~ass:EE` no longer an assumption, non-conformal tensor block included, without `ass:dictionary`. This package addresses the `G_T = G_A` gap only. Dependencies: F, A, C, D1 (and 015's replica (I)). Classification: PROGRAMME-CONDITIONAL.

Dependency on 015: 015 is integrated (ledger: commit 333c282). The text below goes after 015's two paragraphs in `sec:status-B` and uses their notation (`c_T`, `c_A`, the unit `-(Lambda^2/32 pi^2) rhobar^2 p_eta^2 (1-N_tot/24) M`, the replica table).

## Source reading

Digest + targeted reads. `scratch/digest.md` has head `4858b51` (current HEAD), `dirty-chapters: no`, but `python scripts/make_digest.py --check` printed `DIGEST STALE`; I therefore read the sources directly.

Read in full: `proposals/015-entropy-action-identity/proposal-r2.md` and `review-r1.md`; `reports/sme-scout-gap-GT-GA-20261015.md`; `CLAUDE.md`, `MILESTONE.md`; ledger tail; appH `sec:status-B` (header through the end of 015's paragraphs) and the Presentation-A Poisson-limit paragraphs (scalar, frame, connection sector, quadratic form, beyond quadratic order), ch17 `sec:ch17-order` and `sec:ch17-done`, ch02 (fermions "not treated"), ch03 (action, `S_matter`), ch16 (fermion remark). Not read: ch01, ch04-ch15, ch18, appA-appG, appI-appL (no full scan; no full-scan claim). Proposal 016 not read beyond the ledger entry.

Literature (checked this session):
- Solodukhin, Living Rev. Rel. 14, 8 (arXiv:1104.3712): text of the arXiv PDF extracted; read Section 3.14-3.16 (Eqs. (126)-(130), (132)-(137), (145)-(151)). Verified: `S(s,d) = D_s(d) A/(6(d-2)(4 pi)^{(d-2)/2} eps^{d-2})` with weight 1/2 for fermions, `D_{1/2}(4) = 2` for Dirac; vector `a_1 = (D_1/6 - 1) R` (the extracted text prints the fraction on two lines), `D_1 = d-2`; fermion `a_1 = -D_{1/2} R/6`; the statement that the non-minimal terms `X^{(s)}` contribute negatively to `G` and not to the entropy. Equation numbers are those of the arXiv PDF.
- Steinacker, arXiv:2303.08012 (JHEP 05 (2023) 129): arXiv abstract page fetched. Abstract: maximally supersymmetric IKKT model, `M^{3,1} x K`, Einstein-Hilbert action at one loop, Newton constant set by the Kaluza-Klein scale. Content beyond the abstract not verified; not used for any number.
- Casini-Huerta-Rosabal, arXiv:1312.1183 (PRD 89, 085012) and Donnelly-Wall, arXiv:1506.05792 (PRD 94, 104053): arXiv abstract pages fetched (abstract level). Used only qualitatively.
- Kabat hep-th/9503016, Larsen-Wilczek, Fursaev-Miele: not opened; their results enter only through Solodukhin.
- Nielsen arXiv:1109.2699, de Alwis arXiv:2511.12864: not opened, not used.
- Standard facts used without source check: real components of the minimal spinor in `D = 10` is 16 (`= 2` Dirac); Euclidean zeta/Hurwitz identities (`Sum_m |m+theta| = -B_2({theta})`).

## Research and reasoning

### 0. Machinery and validation

Setting as in the Poisson-limit paragraph: Euclid `eta = delta`; `Theta = Theta_bar + eps T sin(p.x)`, `T^{mu nu} = -(q^mu u^nu - u^mu q^nu)`, `q = Theta_bar p`; `D_mu f = {x_mu, f} = Theta^{mu rho} d_rho f`; operators act on `L^2(rho d^4x)`, `O' = rho^{1/2} O rho^{-1/2}`. `hk_lib.py` builds `O'` symbolically (exact rationals; Laurent series in `z = e^{ip.x}`, truncated at `eps^2`). `hk_eval.py` evaluates the second-order heat trace at `s = 1` (Duhamel: `-int tr[e^{-A} V_2] + (1/2) int_0^1 dt int sum_{n=+-1} tr[V_{-n}(k+nP) e^{-tA(k+nP)} V_n(k) e^{-(1-t)A(k)}]`) on a Gauss-Hermite grid in the variable `q = Theta_bar k`, with exact closed-form exponentials `e^{-x(q^2 - kappa q q^T)}`, and extracts the `lam^2` (a_0) and `lam^4` (a_1) coefficients of `p -> lam p` by a Cauchy contour in `lam`. The quadratic forms are reduced on the quotient `u ~ q` and given relative to `rhobar^2 p^2 M` (script output "eig").

Validation against 015 / merged text: scalar `a_1`: `(-1/24, -1/24, -1/8) = (1/6)(-1/4,-1/4,-3/4)`; connection sector at `alpha = 1`: `(5/6, 5/6, 1/2) = (4/6)(-1/4,-1/4,-3/4) + 1`; the gauge residual `|S q|/|S|` is `1e-15`; the `a_0` forms scale as `(3 + alpha^2)/4` (table below). Two backgrounds (`a0, b0 = 4, 9/4` and `3, 4/3`, different `p`): A and B agree with the direction-independent values.

### 1. Exact intertwining lemma (established identity)

Let `(G phi)_nu = D_nu phi`, `E_nu = D_mu Theta_{mu nu}` (called `J_nu` in the manuscript text), `O_s = -D_mu D_mu`, `O_v a_nu = -D_mu D_mu a_nu - 2 {Theta_{nu l}, a_l}` (the Feynman-gauge operator of the integrated Poisson-limit paragraph), and `O_kappa = O_v - kappa G G^dagger` (`G^dagger a = -D_mu a_mu`), the operator of the gauge-fixing weight `(1/(2 alpha)) rho (D.a)^2`, `kappa = 1 - 1/alpha` (derivation: the tree quadratic form is `D a D a - (D.a)^2 - 2Y`, `Y = a_mu {Theta_{mu nu}, a_nu}`; with `-2Y` as in the merged text it reduces to `O_v` at `alpha = 1`).

Facts for every Poisson bivector: (i) `D_mu` is a derivation of `{,}` (Jacobi); (ii) `[D_mu, D_nu] = {Theta_{mu nu}, .}`; (iii) `D_mu` is anti-self-adjoint on `L^2(rho d^4x)` because `d_r(rho Theta^{mu r}) = 0`. Then
- `G^dagger G = O_s`.
- `[D_mu D_mu, D_nu] = D_mu {Theta_{mu nu}, .} + {Theta_{mu nu}, D_mu .}` and `D_mu {Theta_{mu nu}, phi} = {D_mu Theta_{mu nu}, phi} + {Theta_{mu nu}, D_mu phi}`. So `O_v G phi - G O_s phi = -{E_nu, phi} - 2 {Theta_{mu nu}, D_mu phi} - 2 {Theta_{nu l}, D_l phi}`. The last two terms cancel (`Theta_{nu l} = -Theta_{l nu}`): **`O_v G = G O_s - {E_nu, .}`.**

`check_intertwining.py` verifies, in exact rational arithmetic at a point, for `Theta = (psi^* omega_bar)^{-1}` with polynomial `psi` (Jacobi residual 0, `d_r(rho Theta^{n r}) = 0`), a nonzero `E` (`-1.11, 0.41, -0.53, -0.003`) and a polynomial `phi`: the residual of the identity is exactly `0` in all four components.

At linear order about `Theta_bar`: `E_nu = -eps cos(p.x) (M u)_nu`, `M = q^2 delta - q q`, the tree-level kernel (`check_linear_EOM.py`, symbolic). So the defect `W = {E,.}` is proportional to the tree-level Poisson-limit equation of motion (014's/ch03's kernel `M`).

Consequence (conditional on a global `E = 0` and the usual domain/zero-mode conventions): `L^2 = Ran G + ker G^dagger`, both invariant under `O_kappa`; `O_kappa|_{Ran G} = (1-kappa) O_s`, `O_kappa|_{ker G^dagger} = O_v`; hence `Tr e^{-s O_kappa} = Tr e^{-s O_v} - Tr e^{-s O_s} + Tr e^{-s(1-kappa) O_s}`. With the pointwise form `sqrt|G| (R_G/6 - E_s) = rho R[g_rho]/6` of the integrated paragraph, the integrated `a_1` of the connection sector on `E = 0` backgrounds is `(4/6 + (alpha-1)/6) rho R[g_rho] + rho^2 X`. (`alpha` multiplies the scalar `a_1` since `Tr e^{-s' O_s}`, `s' = s/alpha`, has `(4 pi s')^{-2} s' a_1`.) So on `E = 0` the coefficient of `rho^2 X` is `1` for all `alpha`.

### 2. Off shell about constant `Theta_bar`: the 't Hooft family (numerical; closed forms match)

Connection-sector `a_1` eigenvalues (unit `rhobar^2 p^2 M`; script output `analyze_forms.out.txt`; TT = degenerate pair, "third" = the `delta rho != 0` mode):

| bg | `kappa` | `alpha` | TT num | TT `5/6-(alpha-1)/24` | third num | third `1/2-(alpha-1)/8+(alpha^2-1)/4` |
|---|---|---|---|---|---|---|
| A | -2 | 1/3 | 0.86081 | 0.86111 | 0.36109 | 0.36111 |
| A | -1 | 1/2 | 0.85415 | 0.85417 | 0.37500 | 0.37500 |
| A | -1/2 | 2/3 | 0.84721 | 0.84722 | 0.40277 | 0.40278 |
| A | 0 | 1 | 0.83333 | 0.83333 | 0.49999 | 0.50000 |
| A | 1/2 | 2 | 0.79167 | 0.79167 | 1.12500 | 1.12500 |
| A | 2/3 | 3 | 0.7508 | 0.7500 | 2.2512 | 2.2500 |
| B | -1 | 1/2 | 0.85415 | 0.85417 | 0.37483 | 0.37500 |
| B | 0 | 1 | 0.83333 | 0.83333 | 0.50000 | 0.50000 |
| B | 1/2 | 2 | 0.79167 | 0.79167 | 1.12501 | 1.12500 |

A least-squares quadratic fit in `alpha` (six values, background A) gives `e_TT = 0.8746 - 0.0409 alpha - 3e-4 alpha^2` and `e_3 = 0.37498 - 0.12497 alpha + 0.24999 alpha^2`. A run at `alpha = 4` (`n = 16`) did not converge (the grid scale for `e^{-(1-kappa) q^2}`) and is not used (kept in `outputs/`). The closed forms are rational guesses matched to `2e-3` or better, not derived; the TT form agrees with the exact on-shell lemma, which supports it analytically; the third-mode offset `(alpha^2-1)/4` is a numerical fit.

The `a_0` check (third mode of the `lam^2` form relative to `alpha = 1`): `0.8125, 0.8611, 1.7500, 3.000` against `(3+alpha^2)/4`, for `alpha = 1/2, 2/3, 2, 3` (two backgrounds).

Reading. In the basis `{rho R[g_rho], rho^2 X, rho|grad ln rho|^2}` (at quadratic order `rho^2 X = -4 rho R - 4 rho|grad ln rho|^2` by the merged text, so only two combinations are visible; the split uses the exact on-shell coefficient `(3+alpha)/6` of `rho R`): `b = 1` and `c(alpha) = (alpha^2-1)/2`. Equivalently the quadratic data are `c1 = -4 e_TT` and `c2 = 2(e_3 - 3 e_TT) = -4 + (alpha^2-1)/2` for the connection sector (scalars and ghosts have `c2 = 0`).
- The TT eigenvalue (hence `c_T`) contains no EOM-proportional shift in this family; the EOM-proportional (gauge-dependent) part lives on the `delta rho != 0` mode, where `E = -eps cos(.) M u` does not vanish on the mode and multiplies a vector `~ q (p.u)`.
- Totals (scalars `N_s`, connection, ghost `-2`): `c_T(alpha) = (N_s + alpha - 1)/6 - 11/3`.

Cone coefficient (conditional): the replica of 015 on the cover with constant `Theta_bar` has `E = 0` identically, so the same lemma gives `Tr_n e^{-s O_kappa}` = (3 scalar-like components + one longitudinal scalar with `s -> s(1-kappa)`); the area term of the longitudinal sector is `alpha` times the scalar one: `c_A(connection) = (3+alpha)/6`, `c_A = (N_s + alpha + 1)/6`. The conditions: the domain at `Sigma` (the gradient of a regular scalar mode need not lie in the componentwise-regular vector domain: Kabat/Donnelly-Wall subtlety), the continuation in `n`, and a common proper-time cutoff on `O_kappa` for action and replica. For the stated domain (longitudinal sector = image of the regular scalar domain) `c_A - c_T = 4` for the tested range `1/3 <= alpha <= 3` (off-shell numerics) and, on `E = 0` backgrounds under the conditions above, for every `alpha > 0`. **Withdrawn from r1:** the claim that a different tip domain shifts `c_A` by an `alpha`-independent amount (review finding 1): a shift `delta_perp` of the transverse constant in the longitudinal sector is multiplied by the parallel factor `alpha`, and a vector-versus-scalar domain also changes the non-minimal operator's transverse trace by a `kappa`-dependent amount. Other tip domains are not examined.

Remark (regulator): if the replica and the action used different effective cutoffs for the longitudinal sector (e.g. a momentum cutoff for one and a proper-time cutoff on `O_kappa` for the other) the gap would acquire `alpha`-dependence; with one cutoff on the same operator (the 015 prescription) it does not. A mismatch of regulators is a tuning, not a derivation.

SME diagnostic (correction): the scout's "pure Einstein needs `b = 0`, ratio 3" assumes a form spanned by `rho R` and `rho^2 X`. For `alpha != 1` a third structure `rho|grad ln rho|^2` appears, ratio 3 is reached at `alpha = 3` while the gap stays 4.

### 3. EOM term in the gauge function (numerical)

`F = D.a + c E.a`, `alpha = 1` (`E` is the background EOM; `F = D.a` when `E = 0`): `O_c = O_v + c[E_nu div - D_nu(E.)] + c^2 E_nu E_mu`; the Faddeev-Popov operator is `-D_mu D_mu - c E_mu D_mu` (non-self-adjoint; heat trace by the same Duhamel formula). Results (unit `rhobar^2 p^2 M`): connection sector shift `+c^2 q^2/(4 p^2)`, ghost per unit weight `-c^2 q^2/(8 p^2)` on all three modes (uniform), `q^2/p^2 = 10.787` (A) and `7.713` (B); `c = 1/2, 1, 2` in A, `c = 1` in B, all matching to `3e-5`. With weight `-2` the total shift is `c^2 q^2/(2 p^2)`, i.e. `Delta(sqrt|G| tr(R/6 - E)) = +c^2 rho^2 E_nu E_nu` at this order. Sign: `E` real, so the shift is positive, `c_T` decreases, the gap increases; an imaginary `c` would make the gauge-fixing weight non-positive. The shift is isotropic only for `a0 = b0`. Cross terms `E.V` with a first-derivative vector `V` are `q^2 (u.p)(..)`-type and vanish on the TT modes for `V ~ p` (since `delta rho ~ p.u = 0`); vectors `V ~ K p` are not tested (they would not preserve the degeneracy of the TT pair for anisotropic `Theta_bar`).

### 4. Fermionic content (SME 2)

Fermion action `int rho Psibar gamma^mu D_mu Psi` (Poisson limit of `Tr Psibar Gamma^mu [X_mu, Psi]`; `D_mu` anti-self-adjoint, so `i D-slash` is symmetric): `O_f = -(gamma^mu D_mu)^2 = O_s - (1/2) gamma^{mu nu} {Theta_{mu nu}, .}`. Matching `-2 B^sigma d_sigma` gives `beta^sigma = (1/4) gamma^{mu nu} (N^sigma)_{mu nu}`, `(N^sigma)_{mu nu} = Theta^{rho sigma} d_rho Theta_{mu nu}`, the spinor lift of the vector `B^sigma = (1/2) N^sigma_{ab} J^{ab}`. Index ratio: `tr_vec B^2 = -|N|^2`, `tr_Dirac beta^2 = -|N|^2/2` (`dynkin_check.py`), and `-4|N|^2/2 = -2|N|^2` for the 16-dimensional Weyl half of the 10D spinor restricted to `so(4)`. With no explicit `R` in `E_f` in the variables `(G, rho, d Theta)`: `a_1 = (4/6) rho R[g_rho] + (1/2) rho^2 X`. Numerical check (`hk_eval.py dirac`, both backgrounds): eigenvalues `(1/3, 1/3, 0) = (4/6)(-1/4,-1/4,-3/4) + 1/2`.

Statistical weight: Dirac `Gamma = -ln det_C(i D-slash) = -(1/2) ln det O_f` (weight `-1` over 4 complex components); 10D Majorana-Weyl (16 real) `Gamma = -ln Pf = -(1/4) ln det_16 O_f` (weight `-1/2` over 16 real components); both give `b_f = -1` for the 16 real components (`dynkin_check.py`: `-1/2 x (+2)`). So `b_total = 1 - n_D/2` and `N_s + 2 - 4 n_D` multiplies `rho R/6`.

Sum rule (condition, not derivation): `b_total = 0` iff the index sum of the fermions equals that of the vector, i.e. `n_D = 2`. In the extended-coordinate setting `N_s = D - 4` (Definition `def:matrix-coords-ext`), the SUSY Yang-Mills minimal spinors in `D = 4, 6, 10` (4, 8, 16 real components; standard counts) give `b = 3/4, 1/2, 0`: supersymmetry alone does not give `b = 0`, the `D = 10` content does. Nothing in the displayed bosonic action (ch03; ch02: fermions "not treated") forces it. Bosonic content cannot cancel `b`: every bosonic field has `b >= 0` (`b = 0` for minimal scalars, `1` for the connection); torsion-coupled scalars `E = xi X` shift `b` by `-xi` and have no matrix origin.

Area side: for the fermion replica the Cartesian-frame components acquire the phase `(-1)^{n+1}` (antiperiodic in the polar frame). Zeta evaluation (`cone_twist_zeta.py`; `B_2({theta})/(2n)` per transverse component for monodromy `theta`, `(1 - n d_n)[C(n) - n C(1)]` at `n = 1`): scalar `1/6`; spinor component (`theta = (n+1)/2`) `-1/12` on `n < 1` (`5/12` on `n > 1`); vector component rotated with the angle (`theta = n`) `-1/3` on `n < 1` (`2/3` on `n > 1`). The `n < 1` branch reproduces the standard facts: ratio `-1/2` of a spinor component (Dirac = 2 scalars, Solodukhin (126)-(127)) and `-2/3 = (D_1-6)/6` for rotated Maxwell with ghosts (Solodukhin (147)). The non-analyticity at `n = 1` is the continuation ambiguity; the `n < 1` branch is the one that reproduces the known fermion value and is used for fermions (they have no unrotated alternative with antiperiodic gluing), `n > 1` is reported.

So, for the antiperiodic polar-frame gluing (spinor index transported with the replica rotation, phase `(-1)^{n+1}` on Cartesian components), `c_A(Dirac) = +1/3` per field with weight `-1`: `c_A = (N_s + alpha + 1)/6 + n_D/3`. For the unrotated periodic gluing of the Cartesian components (the gluing 015 uses for `a^mu`) `c_A(Dirac) = -2/3` = its `rho R` coefficient `(4/6)(-1)`, `c_A = (N_s+alpha+1)/6 - 2 n_D/3` and `c_A - c_T = 4 - 2 n_D` (`gap_periodic.py`). With `c_T = (N_s + alpha - 1)/6 + 4 n_D/3 - 11/3`: `c_A - c_T = 4 - n_D` (rotated vector: `3 - n_D` on `n < 1`, `5 - n_D` on `n > 1`). Third-mode test `c2 = alpha^2/2 + 2 n_D - 9/2`: `c2 = 0` at `n_D = 2, alpha = 1`; gap `0` at `n_D = 4` (`c2 = +4` there).

`gap_table.py`, `gap_periodic.py` output: `D = 10` content (`N_s = 6`, `n_D = 2`, `alpha = 1`): `N_s + 2 - 4 n_D = 0`, `c_T = 0`, `c2 = 0`; `c_A = 2` (antiperiodic, gap 2) or `c_A = 0` (periodic, gap `0`). The periodic case is `0 = 0` between vanishing `Lambda^2` coefficients, not a derivation of `G_T = G_A`; r1's remark that periodic gluing 'is not the replica of a state' is withdrawn as unsupported: which gluing the matrix state selects is a Problem A question (modular flow), not decided here. Positivity: `c_T(n_D = 4, alpha = 1) = N_s/6 + 5/3 > 0`.

Reading of the SME SUSY caveat: confirmed that the `Lambda^2` tensor coefficient `c_T` vanishes at `D = 10` content (and `b = 0` there). The area coefficient is `2` for antiperiodic and `0` for periodic gluing: the comparison is `2 vs 0` or `0 = 0` according to a gluing this package does not determine.

### 5. Frame and centre choice (bounded)

Rotated vs unrotated (item 3a above): the state is invariant under the combined rotation (coordinates in the `Sigma`-transverse plane and, through `Theta_bar`, the internal index: `D_mu -> R^{-1}_{mu tau} D_tau`), so a modular-flow replica rotates the internal index; at integer `n` both gluings agree and they differ in the continuation (`n < 1` vs `n > 1`). 015's unrotated choice is the integer-cover pullback; the answer is not decided by this package.

Contact term and the scout's magnitude: Solodukhin (126) gives `S_ent = D_1/6` (units where a scalar is `1/6`), Eq. (147) gives `c_ind = D_1/6 - 1`: the Kabat contact term is `-1` in these units, i.e. `6` scalar units, not the `1/6` assumed in the scout; I did not read Donnelly-Wall's text beyond the abstract, so I do not claim their "one negative scalar" statement maps to `1`. Both the contact term and the CHR centre ambiguity are boundary-local (CHR abstract). Their size relative to the gap is an order-of-magnitude observation (Kabat contact `1` against gap `4`), not a theorem; their `alpha`-dependence for the non-minimal operator is not established (review finding 1), and they are not examined further. The gauge-sector area coefficient itself is `alpha`-dependent (`(3+alpha)/6`), consistent with CHR's statement that the entropy depends on the partial gauge fixing.

Also: the scout's replica (II) equality at `N_tot = 16` is reproduced (not claimed physical); with fermions it generalises to `N_s = 14 - 4 n_D`; at `n_D = 2` it is `N_s = 6` where both sides vanish identically (the `(II)` coefficient is `-(N_s + 2 - 4 n_D)/12`). Replica (II) stays unused.

### 6. What this says

`c_A - c_T` is `alpha`-independent because the `alpha`-dependent pieces are the longitudinal scalar tower in both the action and the cone. For bosonic content the remaining gap is `4` times the total index weight of the bounded, torsion-squared invariant `rho^2 X`; with fermions it depends on the replica gluing (`4 - n_D`, `4 - 2 n_D`, `3 - n_D`, `5 - n_D`). The missing ingredient is therefore either (i) a derived statement about which functional of `Theta` plays the role of the quadratic action whose metric response defines `T^op` (the bounded `rho^2 X` is a frame-dependent, non-Lorentz-invariant structure; Problem D1/F), or (ii) fermionic-type content together with a derivation of the replica gluing (Problem A, modular flow), or (iii) the next coefficient in the `D = 10` content where the `Lambda^2` tensor coefficient vanishes (and, for periodic gluing, the area coefficient too).

## Claim classification

| Claim | Class |
|---|---|
| `Gr^dagger Gr = O_s`, `O_v Gr = Gr O_s - {J,.}` | established identity (algebra + exact check at a point; independently re-verified in review r1) |
| `J^{(1)} = -eps cos (M u)` | established (symbolic) |
| `Tr e^{-s O_kappa}` decomposition and `a_1 = ((3+alpha)/6) rho R + rho^2 X` on `J = 0` | conditional (global `J = 0`, domains, zero modes, common cutoff) |
| Off-shell TT and third-mode eigenvalues | numerical; rational fits to `2e-3`, not derived; `alpha = 1/3..3`; TT agrees with the exact lemma |
| Gap `2 Lambda^2/pi`: tested range `1/3 <= alpha <= 3`; every `alpha>0` only on `J = 0` under the stated conditions | numerical / conditional |
| Cone coefficient `(3+alpha)/6` | conditional on the stated tip domain; other domains not examined |
| EOM-term gauge function shift `+c^2 rho^2 J^2` | numerical (two backgrounds, three `c`) |
| Dirac `a_1`, `b_total = 1 - n_D/2` | established algebra (`dynkin_check.py`) + numerical |
| `n_D = 2` as the 16 real components of the `D = 10` model | input / identification |
| `c_A(Dirac) = +1/3`, gap `4 - n_D` | conditional on antiperiodic polar-frame gluing, `n<1` branch |
| `c_A(Dirac) = -2/3`, gap `4 - 2 n_D`, `0 = 0` at `n_D = 2` | conditional on unrotated periodic gluing; equality of vanishing coefficients, not a derivation |
| Rotated vector cone, gap `3 - n_D` / `5 - n_D` | conditional, continuation-dependent |
| Torsion-coupled scalars | input (no matrix origin) |
| Replica gluing selected by the matrix state | unresolved (Problem A) |
| Value, sign, existence of `G_eff`; `ass:EE`; stationarity; the map `Theta -> G` | unresolved |

## Proposed changes

One file, `chapters/appH-microscopic-proofs.tex`; no label added or changed; no bibliography change (keys `Solodukhin2011`, `IKKT1997` exist once in `bib/namcg.bib`). `\mathrm{Gr}` and `\mathfrak J` do not occur in `chapters/`. Anchor, verified to occur exactly once (`grep -cF`): the last sentence of the 015 block, "... they give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open." (appH line 179), followed by `\section{Problem C: conformal mode and Cassini}` (once, line 181). Insert the two paragraphs after the anchor sentence and before that section; nothing is replaced. Labels used: `rem:ch3-trace-quadratic`, `eq:O-eta`, `ass:EE` (each defined once); `\LUV` defined at `namcg-book7.tex` line 54. The block was compiled in a scratch copy outside the repository (amsmath, amssymb, `\LUV`, stub `\cite/\eqref/\ref`): no error. `appH_insert.tex` is identical to the block below (CRLF in the file; the integrator normalises). 015's own "do not treat ... fermions or additional scalars" remains accurate for 015's paragraphs.

```latex
\paragraph{Gauge parameter and gauge function in the comparison of \(G_T\) with \(G_A\) (conditional; not closure).}
Keep the setting, the class and the normalisation of the two preceding paragraphs. Write \(e_i\) for the contribution of a sector of weight \(w_i\) to the bracket \(1-N_{\mathrm{tot}}/24\) of the preceding paragraph, so that \(\sum_iw_ie_i\) is the net eigenvalue on the two modes with \(\delta\rho=0\) and \(c_T=-4\sum_iw_ie_i\); a scalar component has \(e=-\tfrac1{24}\) there and \(-\tfrac18\) on the mode with \(\delta\rho\neq0\). Let \(D_\mu=\{x_\mu,\cdot\}\), anti-self-adjoint on \(L^2(\rho\,\mathrm d^4x)\), \((\mathrm{Gr}\varphi)_\nu=D_\nu\varphi\), and \(\mathfrak J_\nu=D^\mu\Theta_{\mu\nu}\), the Poisson limit of the tree-level equation of motion; for the perturbation of the quadratic-form paragraph \(\mathfrak J_\nu=-\epsilon\cos(p\cdot x)\,(Mu)_\nu\), with \(M=q^2\eta-qq\) the kernel of Remark~\ref{rem:ch3-trace-quadratic}. The background gauge \(\tfrac1{2\alpha}\rho\,(D_\mu a^\mu)^2\), \(\alpha>0\), \(\kappa=1-1/\alpha\), leaves the ghost operator unchanged and replaces \(\mathcal O_v\) by the non-minimal operator \(\mathcal O_\kappa=\mathcal O_v-\kappa\,\mathrm{Gr}\mathrm{Gr}^\dagger\), with principal symbol \(q^2\mathbb I-\kappa\,qq^{T}\); one proper-time cut-off on \(\mathcal O_\kappa\) serves the effective action and the replica, and the normalisation of the gauge-fixing weight is local and carries no two-derivative term.

For every Poisson bivector \(\mathrm{Gr}^\dagger\mathrm{Gr}=\mathcal O_s\) and \(\mathcal O_v\mathrm{Gr}=\mathrm{Gr}\mathcal O_s-\{\mathfrak J_\nu,\cdot\}\): the commutator terms are fixed by \([D_\mu,D_\nu]=\{\Theta_{\mu\nu},\cdot\}\) and the Leibniz property of \(D_\mu\) on the bracket, and the \(\{\Theta_{\mu\nu},\cdot\}\) coupling of \(\mathcal O_v\) cancels them up to \(\mathfrak J\) (checked in exact arithmetic for a nonlinear bivector). Hence for \(\mathfrak J=0\), \(\mathcal O_\kappa\mathrm{Gr}=(1-\kappa)\mathrm{Gr}\mathcal O_s\), the longitudinal sector is the scalar operator with proper time rescaled by \(1-\kappa\), and up to zero modes \(\operatorname{Tr}e^{-s\mathcal O_\kappa}=\operatorname{Tr}e^{-s\mathcal O_v}+\operatorname{Tr}e^{-s(1-\kappa)\mathcal O_s}-\operatorname{Tr}e^{-s\mathcal O_s}\). The integrated \(\LUV^2\) density of the connection sector is then \(\tfrac{3+\alpha}6\,\rho R[g_\rho]+\rho^2X\) on such backgrounds, with the coefficient \(1\) of \(\rho^2X\) independent of \(\alpha\). On the replica cover with constant \(\bar\Theta\) the same intertwining, with the domain at \(\Sigma\) for which the longitudinal sector is the image of the regular scalar domain, gives the area coefficient \(\tfrac{3+\alpha}6\) for the connection sector in the units \(c\) of the table above, equal to the coefficient of \(\rho R[g_\rho]\). This depends on that choice of domain; other choices are not examined.

About constant \(\bar\Theta\), with \(\mathfrak J\neq0\), a numerical second-order evaluation of the heat trace (momentum-space Duhamel expansion, Gauss--Hermite quadrature, contour extraction of the \(p^4\) coefficient; it reproduces the scalar value above, the \(\alpha=1\) values \(\tfrac56\) and \(\tfrac12\) of the connection sector, and the weight \(3+\alpha^2\) of the \(\LUV^4\) term) gives for the connection sector the values, matched by the rational forms, \(\tfrac56-\tfrac{\alpha-1}{24}\) on the two modes with \(\delta\rho=0\) and \(\tfrac12-\tfrac{\alpha-1}8+\tfrac{\alpha^2-1}4\) on the mode with \(\delta\rho\neq0\) (\(\alpha=\tfrac13,\tfrac12,\tfrac23,1,2,3\) in one background, \(\tfrac12,1,2\) in another; rational fits to \(2\times10^{-3}\), not derived; \(\alpha=\tfrac13,\dots,3\) only). The two modes with \(\delta\rho=0\) thus show the \(\alpha\)-dependence of the \(\mathfrak J=0\) result, and the remainder, \(\tfrac{\alpha^2-1}2\rho|\nabla\ln\rho|^2_{g_\rho}\), acts on the mode with \(\delta\rho\neq0\) only. With scalar and ghost sectors independent of \(\alpha\), \(c_T(\alpha)=\tfrac{N_s+\alpha-1}6-\tfrac{11}3\) and the replica coefficient is \(c_A(\alpha)=\tfrac{N_s+\alpha+1}6\), so \(1/G_A-1/G_T=2\LUV^2/\pi\) for the tested range \(\tfrac13\le\alpha\le3\); on backgrounds with \(\mathfrak J=0\) and under the conditions above the \(\alpha\)-dependence cancels in the difference for every \(\alpha>0\). The TT value agrees with the exact lemma on \(\mathfrak J=0\) backgrounds. For \(\alpha\neq1\) the form is not spanned by \(\rho R[g_\rho]\) and \(\rho^2X\); the third-mode to \(\delta\rho=0\) ratio of a term \(c\,\rho R[g_\rho]\) is \(3\), and the net form attains this ratio at \(\alpha=3\), where the gap is unchanged, so that ratio does not diagnose the coefficient of \(\rho^2X\) outside the Feynman gauge. A gauge function \(D_\mu a^\mu+c\,\mathfrak J_\mu a^\mu\) (\(\alpha=1\), ghost operator \(-D_\mu D_\mu-c\mathfrak J_\mu D_\mu\)) adds \(c^2\rho^2\mathfrak J_\nu\mathfrak J_\nu\) to the density of the connection and ghost sectors together at quadratic order about \(\bar\Theta\), that is \(c^2q^2/(2p_\eta^2)\) to the eigenvalue on all three modes (two backgrounds, \(c=\tfrac12,1,2\)); this lowers \(c_T\) at fixed \(c_A\) and depends on the direction of \(p\) unless \(\bar\Theta\) is isotropic. Gauge functions with other first-derivative vectors are not examined.

\paragraph{Fermionic content and the connection-sector cone in the comparison of \(G_T\) with \(G_A\) (conditional; not closure).}
The displayed action is bosonic. Add \(n_D\) Dirac fields with action \(\int\rho\,\bar\Psi\gamma^\mu D_\mu\Psi\), the Poisson limit of \(\operatorname{Tr}\bar\Psi\Gamma^\mu[\hat X_\mu,\Psi]\), and the connection gauge \(\alpha=1\); the Yukawa couplings \(\Gamma^i[\hat X_i,\Psi]\) to the \(N_s\) transverse matrices vanish on the background and are dropped. The operator \(\mathcal O_f=-(\gamma^\mu D_\mu)^2=\mathcal O_s-\tfrac12\gamma^{\mu\nu}\{\Theta_{\mu\nu},\cdot\}\) has the form~\eqref{eq:O-eta} on \(G\) with \(\omega_\sigma=-\tfrac12\partial_\sigma\ln\rho\,\mathbb I+\beta_\sigma\), \(\beta^\sigma=\tfrac14\gamma^{\mu\nu}\Theta^{\rho\sigma}\partial_\rho\Theta_{\mu\nu}\), the spinor lift of \(\mathcal B^\sigma\), and \(\operatorname{tr}\beta_\sigma\beta^\sigma=-\tfrac12X\) over four components (the vector value is \(-X\)); it contains no explicit curvature, so \(\sqrt{|G|}\operatorname{tr}(\tfrac16R_G-E_f)=\tfrac46\rho R[g_\rho]+\tfrac12\rho^2X\), with eigenvalues \(\tfrac13,\tfrac13,0\) on the three modes (two backgrounds). The statistical weight is \(-1\) per Dirac field (\(\Gamma=-\tfrac12\ln\det\mathcal O_f\) over four complex components). The coefficient of \(\rho^2X\) of the whole content is therefore \(1-n_D/2\): the weight of a field is its index under the rotation generated by \(\mathcal B_\sigma\), and it vanishes for \(n_D=2\), the sixteen real components of the ten-dimensional maximally supersymmetric matrix model~\cite{IKKT1997} with the Poisson background along four coordinates and \(N_s=6\). No symmetry of the displayed action forces this. For \(n_D\) fields \(c_T=\tfrac{N_s+\alpha-1}6+\tfrac{4n_D}3-\tfrac{11}3\). With the antiperiodic polar-frame condition, which gives the Cartesian-frame components the phase \((-1)^{n+1}\), the area coefficient of a Dirac field is that of two scalar components, \(+\tfrac13\) (Equations~(126)--(127) of~\cite{Solodukhin2011}; the zeta-function evaluation of the twisted cone gives \(-\tfrac12\) times the scalar value per component on the branch \(n<1\)). Then \(c_A=\tfrac{N_s+\alpha+1}6+\tfrac{n_D}3\) and \(c_A-c_T=4-n_D\). This gluing transports the spinor index with the replica rotation; it is not the unrotated pull-back gluing used above for \(a^\mu\). With unrotated periodic gluing of the Cartesian components the area coefficient of a Dirac field is \(-\tfrac23\), equal to its coefficient of \(\rho R[g_\rho]\), and \(c_A-c_T=4-2n_D\), which vanishes at \(n_D=2\) with \(c_T=c_A=0\): an equality of vanishing \(\LUV^2\) coefficients, not a derivation. The \(\rho^2X\) coefficient vanishes at \(n_D=2\); for antiperiodic gluing \(c_A-c_T=2\) there and equality needs \(n_D=4\), where \(\rho^2X\) has coefficient \(-1\). The gluing selected by the matrix state is not determined here. For \(n_D=2\), \(N_s=6\) one has \(N_s+2-4n_D=0\), \(c_T=0\) and \(c_A=2\): the \(\LUV^4\) and \(\LUV^2\) tensor coefficients vanish, and the area coefficient is \(2\) for antiperiodic and \(0\) for periodic gluing.

If the internal index of \(a^\mu\) is rotated with the replica angle, as for a vacuum invariant under the combined rotation, the area coefficient of the connection sector at \(\alpha=1\) is \(-\tfrac13\) on the branch \(n<1\) and \(\tfrac53\) on \(n>1\) instead of \(\tfrac23\); with the ghosts these are \(-\tfrac23\), which is \((D_1(4)-6)/6\) of Equation~(147) of~\cite{Solodukhin2011}, and \(\tfrac43\), instead of \(\tfrac13\); this function of \(n\) is not analytic at \(n=1\), and the gap is \(3-n_D\) or \(5-n_D\). These statements are for the Poisson-limit operators, the \(\LUV^2\) term, one loop, the quadratic form about constant \(\bar\Theta\) on the two modes with \(\delta\rho=0\), the gauge families and the replica prescriptions stated. They do not derive the content, the fermion coupling, the gluing or the rotation of the internal index, which belong to Problem~A, Assumption~\ref{ass:EE} or the modular flow; they do not treat Moyal corrections, gauge functions beyond those stated, \(\Phi\)--\(a\) mixing, or the Kaluza--Klein sector. Problems~B, C, D, F and~G remain open.
```

Stale passages elsewhere: none found. ch17 and the ledger: unchanged.

## Verification scripts

As in r1 (all in this folder: `hk_lib.py`, `hk_eval.py`, `analyze_forms.py`, `check_intertwining.py`, `check_linear_EOM.py`, `dynkin_check.py`, `cone_twist_zeta.py`, `gap_table.py`, `verify_anchors_labels.sh`; outputs `*.out.txt`, raw numerics in `outputs/`, `forms/`). New in r2: `gap_periodic.py` -> `gap_periodic.out.txt` (sympy: antiperiodic gap `4 - n_D`, periodic gap `4 - 2 n_D`; at `N_s = 6`, `n_D = 2`, `alpha = 1`: `c_T = 0`, `c_A = 2` antiperiodic, `0` periodic). `verify_anchors_labels.sh` re-run (anchor sentence and `\section{Problem C...}` each once). Scratch compile of `appH_insert.tex` as above. These are checks, not proofs. Known weakness: the grid does not resolve `alpha >= 4`.

## Decisions Taken

1. `G_T` stays on the two `delta rho = 0` modes (015's choice).
2. Gauge family: non-minimal 't Hooft family directly, one cutoff on `O_kappa`.
3. EOM term in the gauge function kept as the test of an EOM-proportional change.
4. (Revised from r1.) Fermion gluing: the antiperiodic polar-frame and the unrotated periodic results are both reported, neither selected; r1's choice of the antiperiodic one as 'the replica of a state' is withdrawn because the matrix state's gluing is not derived. This favours the full-GR derivation by locating the open input in Problem A's modular flow rather than assuming it.
5. Rotated vs unrotated connection cone: both reported.
6. Not in the manuscript block: centre-choice/edge-mode discussion, replica (II), torsion-coupled scalars, the `D = 4, 6` SUSY counts.
7. No Kabat / Donnelly-Wall / CHR citation in the text.
8. Notation: `\mathrm{Gr}` for the gradient map and `\mathfrak J` for the EOM vector (finding 4); no structural change.

## Milestone assessment

M2 (bounded no-go, narrowly): the gauge parameter and Dirac content at the `Lambda^2` order do not close `G_T = G_A` in the stated class; the periodic-gluing `0 = 0` is a vanishing of both coefficients, not a closure. No breakthrough claimed.

## Status-label recommendation

None. Problem B: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (F and A also unchanged). Chapter 17 critical-path set A, B, C, D1, E, F, G-derived, N unchanged. No label edit in the LaTeX.

## Author decision needed

None. Spacetime stays emergent: the frame is the emergent coframe built from `Theta`; no external metric, `G` or `S = A/4`.

## Remaining open step (ranked avenues; to be queued by the orchestrator, not explored here)

Not derived: `ass:EE`, stationarity of the tensor block, the map to the emergent metric, a value or sign of `G_eff`. Hypotheses of the no-go: Poisson limit; Euclidean section; one loop; `Lambda^2` order; tensor block = `delta rho = 0` modes of `a^mu`; stated tip domain; gluing as stated; constant `Theta_bar`; linear gauge families. Relaxed here: Feynman gauge, no fermions. Not relaxed: the others.

1. **Next order (log / `a_2`, Moyal) in the `D = 10` content, for each gluing.** At `n_D = 2`, `N_s = 6`: `c_T = 0` for all gluings, `c_A = 0` (periodic) or `2` (antiperiodic). The first non-vanishing coefficient on both sides must be compared per gluing. Most promising.
2. **Replica gluing and internal-index rotation from the matrix modular flow** (Problem A sub-lemma). Decides between `4 - n_D`, `4 - 2 n_D`, `3 - n_D`; needs the non-analyticity at `n = 1` resolved.
3. **Tensor-block identification** (`Phi`-`a` mixing; torsion irreducible parts of `rho^2 X`, linking D1).
4. **Explicit non-constant `J = 0` Poisson backgrounds**, to test the lemma's domain and tip conditions directly (signature input from Problem E).
5. **Other gauge functions** (vectors `~ K grad ln rho`, anisotropic `Theta_bar`, Vilkovisky-DeWitt terms, `alpha >= 4` with a better grid).
6. **Tip domain and edge modes for the non-minimal operator**: the effect on `c_A` may be `alpha`-dependent (review finding 1); Kabat and centre shifts not shown small.
7. **Tree-level (014) class, Moyal and curved backgrounds.**
Torsion-coupled scalars have no matrix origin and are unranked.

## Special instructions for the gatekeeper

- Do not read this as closing B or B2; no special value (`n_D = 4`, `alpha = 3`, `n_D = 2` periodic) implies `G_T = G_A`.
- Check that the block states: numerical/fit wording and the range `1/3..3`; `every alpha>0` only on `J = 0`; the tip domain as an assumption with others not examined; both gluings with the periodic `0 = 0` labelled non-derivation; gluing assigned to Problem A; the Yukawa clause; consistent renamed symbols (`Gr`, `J`; `E_f` is the endomorphism only).
- Re-run if desired: `python gap_periodic.py`, `sh verify_anchors_labels.sh`, `check_intertwining.py`.
- The `D = 10` identification (`n_D = 2`, `N_s = 6`) is an input.
