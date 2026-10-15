# Proposal 015-entropy-action-identity, round 1

## Result

Target: Problem B, route "entropy-action identity" of `reports/sme-route-B-DorauMuch-20261015-1052.md` (primary target, section 6). The computation is done for the operators of the integrated Poisson-limit paragraph (scalar `O_s`, internal-index connection `O_v`, ghost of weight -2; Euclidean, background gauge, diagonal heat kernel, one proper-time limit per sector, `ass:emergent-op`). No `S = A/4` and no external `G` is used. Every quantity below was computed or re-derived here, with scripts in this folder.

1. **Cone coefficient (derived, conditional).** For the replica built as the n-sheeted branched cover of the matrix chart `x` with all background fields pulled back (cone on `G` and on `g_rho` together, `rho` a regular density), the leading area term of every Laplace-type sector with bounded connection and endomorphism is the flat-cone term. It is independent of `omega` and `E`:
   `S = (A_G/48 pi) sum_s w_s tr 1_s Lambda_s^2`.
   The same proper-time limit in the effective action gives `1/(16 pi G) = sum_s w_s tr 1_s Lambda_s^2/(192 pi^2)` for the coefficient of `sqrt G R_G`. So `S = A_G/(4G)` with that `G`. The area coefficient of `eq:first-law` is therefore fixed by the operator and the cutoff (`A = 1/(12 pi)` per unit weighted fibre trace, the value already quoted in the Problem-F sector-sum paragraph). This is B2 at conditional scope, in the sense "area coefficient = Lambda^2 coefficient of `thm:Geff` for the same operators".
2. **Contact term, sector by sector.** For `E = E_0 + Q R_G` with the conical delta of `R_G` included, `Delta S = -(A_G/8 pi) sum_s w_s tr Q_s Lambda_s^2 = -2 pi A_G sum_s w_s tr Q_s <phi^2>_s` (`<phi^2> = Lambda^2/16 pi^2`). This reproduces the Susskind-Uglum / Solodukhin relation `S_BH = S_ent - Q` (Solodukhin Living Rev. eqs. (322)-(323), read in the source). With `(G, rho, dTheta)` as independent variables all three sectors have `Q = 0`: scalar, connection (`tr B = 0`, `tr B^2 = -X`) and ghost are bounded on the pulled-back cone.
3. **The "coefficient of R" is not a function of these operators alone (new).** The Weitzenboeck identity of the integrated torsion paragraph gives, for the scalar endomorphism, `E_s = (1/4) R_G + (1/16) T_{lmn}T^{lmn} + (1/8) T_{lmn}T^{mln}`. This was checked here at random two-jets of a closed `omega`, both signatures. In the variables `(G, torsion)` the scalar sector has `Q = 1/4`, and `A_{1,R}` is `-1/12` instead of `+1/6` per component: the sign flips. Totals: `N_tot/6` against `-N_tot/12`, with `N_tot = N_s + 2` as in the integrated paragraph. So the `A_{1,R,s}` of `thm:Geff` ("includes the specified endomorphism") is ambiguous for composite `G`.
4. **Cone on `G` only, or on `g_rho/rho` too (the requested choice; it matters).**
   - (I) Pull-back replica (`rho` regular): column `N_tot/6` above.
   - (II) Cone carried by a singular Poisson structure (`rho ~ r^{n-1}`): `E` has the delta `-(1/2) Box_G ln rho = pi (1-n) delta_Sigma`, a contact term with `Q = 1/4`. The first-order coefficient is `-1/12` per component: exact for scalar and ghost, and for the components of `a^mu` in the block class `Theta^{12}(x^1,x^2)`, `Theta^{34} = 1`. The ratio to (I) is `-1/2` in every sector, and it equals the torsion-basis coefficient. (I) is the replica of the same state; (II) changes the background with `n`. Only (I) is used for the identification in item 1.
5. **Obstruction (bounded no-go).**
   - Statement of the Ward identity for the tensor block. `ass:EE` with Jacobson's geometry requires `m_T = 0` and `G_T = G_A`, where `1/(16 pi G_T)` is the coefficient of the linearised Einstein form in the block's effective action and `1/(4 G_A)` is the coefficient of `delta A`. `thm:mT` uses the second condition implicitly, through the unit-coefficient cancellation of `E` in `eq:mass-identity`.
   - Result. In the Poisson-limit class the induced quadratic form on the two `delta rho = 0` modes is `(1 - N_tot/24) x (...)`, i.e. an Einstein term with `c_T = N_tot/6 - 4`, whereas the area coefficient is `c_A = N_tot/6`. Common cutoff: `1/G_A - 1/G_T = 2 Lambda^2/pi`. With the connection sector at its own limit: `2 Lambda_v^2/pi`. Both are independent of `N_s`. For scalar content alone, `G_T = G_A`.
   - Origin. The difference is the connection-sector term `rho^2 X` (bounded on the cone, so no entropy, but present in the quadratic form).
   - So the induced term supplies the Einstein structure but not the Newton constant that `G_T = G_A` requires, in this class and gauge, for every `N_s` and every positive `Lambda_v`.
   - Interaction with the 014 class. The tree-level response there is degree 0 in `h`: no Einstein structure at tree level at all.
6. **Prior-claim findings (flags, not label changes).**
   - (a) Appendix G, `sec:replica-cone`, says the cone result with "the prefactor identified from the Seeley--DeWitt coefficient that multiplies the deficit" is "the standard result" for any Laplace-type operator. This is false for `E` with explicit curvature coupling (item 2).
   - (b) The hypothesis list of `thm:mT` omits the coefficient equality `G_T = G_A` (item 5).
   - (c) `thm:Geff` leaves `A_{1,R,s}` basis-dependent for composite `G` (item 3).

Nothing here derives `ass:EE`, stationarity, the map `Theta -> G`, or any value or sign of `G_eff`. Problem B stays OPEN.

## Target and status

- Problem B (`sec:status-B`, appH l. 41-140). Status OPEN; priority CRITICAL PATH; completion PROGRAMME-CONDITIONAL. ch17 (l. 121-137, 704-707) agrees: "fixed-algebra first-law identity is established, but not the required stationarity"; closure needs `ass:EE` no longer assumed, non-conformal tensor-block variations, a specified map `g0 -> g`, and no use of an existing metric or of `ass:dictionary`. No discrepancy between appH, ch17 and the ledger (`reports/ledger.md`). The ch17 critical-path set (A, B, C, D1, E, F, G-derived, N) is unchanged.
- Original target of B: derive `delta S_D = 0` at fixed volume for the non-conformal tensor block, with the area term and the map to the emergent metric. This package addresses only two sub-items of the SME decomposition: B2 (the area coefficient) and the normalisation half of B1. It does not touch B3 or the stationarity itself.
- Dependencies: F (operators, `ass:emergent-op`), A (map), C and D1 (blocks).
- Completion classification of this package: PROGRAMME-CONDITIONAL.

## Source reading

Full scan of every file in `chapters/` (ch01-ch18, appA-appL, all of appH l. 1-2410), done because the package edits an appG claim and adds a sentence to a ch07 remark. Appendices C, D, E and I (phenomenology) were read, but are not load-bearing here.
- Digest: `python scripts/make_digest.py --check` printed `DIGEST STALE`. I did not run `make_digest.py`, because it writes outside my folder. All claims below rest on direct reads.
- Also read: `CLAUDE.md`, `MILESTONE.md`, `reports/ledger.md`, the SME route map in full, `proposals/005-F-presentationA-EH/` scripts (one for conventions), the 014 appH paragraphs.
- Not read: other proposals' review files.
- Literature actually read: Solodukhin, Living Rev. Rel. 14, 8 (arXiv:1104.3712): extracted PDF text, eqs. (70), (142)-(144), (318)-(323). Jacobson, arXiv:1505.04753: extracted text, eqs. (21)-(27) and the definition of `delta A|_V`.

## Research and reasoning

### 1. Setting and conventions
`O_s f = -rho^{-1} d_mu(rho K^{mu nu} d_nu f)`, `K = G^{-1}`, `sqrt|G| = rho^2`, `g_rho^{mu nu} = rho K^{mu nu}`.
- `operator_identities.py` verifies (random point, 4D unimodular diagonal `g_rho` of two variables): `O_s = -D^2 + E`, `D = nabla + omega`, `omega = -(1/2) d ln rho`, `E = -(1/2) Box_G ln rho + (1/4)|d ln rho|^2_G`, and `sqrt|G|(R_G/6 - E) = rho R[g_rho]/6`; residuals ~1e-16.
- Connection sector: `(B^sigma)^mu_nu = eta^{mu a} Theta^{r sigma} d_r Theta_{a nu}`; `tr B = 0` and `tr(B_s B^s) = -X` pointwise (both signatures). So `sqrt|G| tr(R/6 - E_v) = (4/6) rho R[g_rho] + rho^2 X`, as in the integrated paragraph. The index of `a^mu` is the internal matrix index (no Christoffel in the Poisson-limit action), so there is no Levi-Civita rotation of the fibre around a cone.

### 2. Cone coefficient and the common regulator
Flat-cone term. For a 2D cone of angle `2 pi n` the heat trace is `Sum_m (1/2) int_0^T e^{-t} I_{nu_m}(t) dt`, with `nu_m = |m|/n`, `t = r^2/2s`.
- Without any regularisation (direct summation, `cone_checks.py` Part 3): `Tr_n - n Tr_1 = -0.125000000000` at `n = 2` and `-0.222222222222` at `n = 3`, equal to `(1/12)(1/n - n)`.
- Mellin/zeta route (Part 1): `int e^{-t} I_nu t^{mu-1} dt` has the closed form quoted in the script (numerical check to 1e-9), continued to `mu = 1`, value `-nu`; `Sum_m |m|/n -> -1/(6n)`. Then `(1 - n d_n)` at `n = 1` gives `1/6`.
- With `ln Z = (1/2) int_{eps^2} ds/s Tr K`: `S = A/(48 pi eps^2)` per real component. The induced action, `-(1/2) int ds/s (4 pi s)^{-2} s (R/6)`, gives `1/G_ind = 1/(12 pi eps^2)`. So `S = A/(4 G_ind)` exactly (Part 2). This reproduces Solodukhin eqs. (318)-(320): `1/G = N/(12 pi eps^2)`, `S = N A/(48 pi eps^2)`.
- The sector formula has the weights `w_s`, the fibre traces and the per-sector `Lambda_s`; the proper-time limit is common to both sides sector by sector (it is the same `s_min,s` in `eq:W-again` and in the replica). A local cutoff `f(rho)` is evaluated at `Sigma` on the cone side and inside the integral on the action side; the leading terms agree.
- Boundedness. A potential or connection that is smooth in the chart `x` and lifted to the cover is bounded in the `G` norm. It gives no delta in `Box_G ln rho`, since the flux of a bounded vector field through a small circle vanishes. Its contribution to the area term is suppressed by `s V` (log-term order). I take this as the standard statement for bounded `E, omega`; I did not prove a uniform remainder estimate for non-smooth lifted potentials.

### 3. Contact term
- `E = xi R_G` with `R_sing = 4 pi (1-n) delta`: `Tr K` gains `-(1-n) xi A/(4 pi s)`; `(1 - n d_n)(1-n)|_{n=1} = 1`, hence `Delta S = -xi A/(8 pi eps^2)`. With `<phi^2> = int_{eps^2} ds (4 pi s)^{-2} = 1/(16 pi^2 eps^2)`: `-Delta S = Q = 2 pi xi A <phi^2>` (script, Part 2).
- This is `S_BH = S_ent - Q` of Solodukhin eqs. (322)-(323) (read in the source). Solodukhin's text before (142)-(144) states that the mismatch arises "when the Riemann tensor appears explicitly in the action of quantum field"; he stresses that the delta-in-`R` entropy has no statistical meaning. Kabat's contact term concerns the Levi-Civita vector (Ricci in `E`); `hep-th/9503016` verified at abstract level only and not used here, since the `a^mu` index is internal.
- Susskind-Uglum, PRD 50, 2700: record verified (Crossref, arXiv abs); abstract-level only.

### 4. Basis dependence
`verify_E_torsion.py`: random closed `omega = omega_bar + dA` (A polynomial, degrees 2-3, exact rational coefficients), `e = eta^{-1} omega^T`, `G = omega eta^{-1} omega^T`, `rho = |Pf omega|`. Two-jets at the origin give `|E_s - (R_G/4 + T^2/16 + T T'/8)| ~ 1e-16` (Euclid) and `~ 2e-11` on the large Lorentz sample; `V - d ln rho` vanishes. This independently confirms the Weitzenboeck formula quoted in the torsion paragraph (derived there "by direct computation"). Hence `Q_s = 1/4` in the torsion variables, while `X = T_{lmn}T^{lmn}` has no `R_G`. The table in the proposed text is reproduced by `sector_table.py`.

### 5. Which geometry carries the cone
- (I) is the replica of `Tr rho_D^n` for the Poisson-limit fluctuation theory on the matrix chart; it is the only one that is the same state replicated.
- (II) block class, Euclid `eta = delta`: `Theta^{12} = 1/f(x^1,x^2)`, `Theta^{34} = 1` (a Poisson bivector for any `f`). Then `G_perp = f^2 delta`, `rho = f`, and `f = |z|^{n-1}` makes `G` a product cone of angle `2 pi n`. `rho ~ r^{n-1}`, and `g_rho` is conical of angle `pi(n+1)` and warped along `Sigma`. In `u = r^n/n`: `omega_u = -(1/2) alpha d ln u`, `alpha = (n-1)/n`, `E = -(1/2) Box ln rho + (1/4)|d ln rho|^2 = pi(1-n) delta + (alpha^2/4)/u^2`. The radial operator of `O_s` in the Hilbert space weighted by `rho` is `-d_u^2 - (1/(n u)) d_u + m^2/(n u)^2`. With `phi = u^{alpha/2} chi` this is the Bessel equation of index `nu_m = sqrt(m^2 + ((n-1)/2)^2)/n` (checked symbolically by hand; the script uses the index). Two self-adjoint branches at `m = 0` (exponents `0` and `alpha`); `phi` regular as a lift from the unbranched chart selects `J_{-nu_0}`, which gives `+(n-1)/(4n)` at first order. (The other branch would give `5/12` instead of `-1/12`.)
- First-order coefficient `F'(1)`. Direct summation: scalar `+0.08333`, connection component `+0.08333`, against `-0.16667` for (I). In terms of `S`-coefficients: `-1/12` against `+1/6`, ratio `-1/2`. Cross-check (Part 4): the local `a_1` with `R_sing/6 - E_sing` gives the same ratio.
- Connection component in the block class: `O_v a^+ = O_s a^+ + 2i c.d a^+` with `c^sigma = Theta^{r sigma} d_r Theta_{12}` azimuthal. The flux term gives angular `(m+a)^2 - (3/4)a^2` with `a = n-1`; the `m != 0` modes cancel at first order (`Sum_{m != 0}|m + a| = 2 zeta(-1)`), and `m = 0` equals the scalar. The `O((n-1)^2)` terms carry `ln` at second order only and do not affect `(1 - n d_n)` at `n = 1`.
- (II) is not claimed physical: it gives a negative coefficient. It corresponds to the smooth-coframe regularisation, equivalent to the torsion-basis Wald-type coefficient.

### 6. Reduction lemma and the normalisation half of B
- Jacobson (arXiv:1505.04753, read): eq. (22) `delta A|_{V,lambda} = -(Omega_{d-2} l^d/(d^2-1))(G_00 + lambda g_00)`, eq. (23) total variation, eq. (24) tensor equation from "all points and all timelike unit vectors", eq. (27) `G = 1/(4 hbar eta)`, i.e. `8 pi G = 2 pi/(hbar eta)`.
- A symmetric `C` with `C(u,u) = 0` on an open set of `u` vanishes. So `eq:first-law-zero` for all diamonds and `xi` directions is `G^{(1)}_{mu nu}[h] = 8 pi G_A <T^op_{mu nu}>[h]` mod `eta_{mu nu}`, with `eta = 1/(4G_A)` the coefficient of `delta A`.
- With the Fierz-Pauli structure of `eq:Top-improved`, a response `Z_T (E - m_T^2 T)` and `E = -2 G^{(1)}` (the convention fixed in the Problem-C paragraph of appH), equality of the `E` terms and of the `T` terms are separate conditions: `m_T = 0` and `G_T = G_A` in the sense of the proposed text. `thm:mT` obtains `m_T = 0` after cancelling the Einstein terms with unit coefficients (`eq:Top-improved` against `eq:deltaA-G`). The identification `h = T` of `eq:h-is-T` (dimensionless metric perturbation against a canonically normalised field with unit FP coefficient) makes the relative normalisation a convention that cannot, as written, be checked. This is the hidden premise. It is not the area-to-`G_eff` identification, which `eq:deltaA-G` states as conditional.
- Sign of the stress response relative to Jacobson's convention: ch07 Exercise 4 already flags it; not fixed here.

### 7. TT comparison
- `tt_quadratic_forms.py`, independent of the integrated 005 scripts: `Theta = Theta_bar + eps T`, `a^mu = u^mu cos(p.x)`, `K`, `rho`, `g_rho` built directly, curvature of `g_rho` from `Gamma`/`Riemann` with `d_mu = p_mu d_theta` (spectral derivative, Richardson in `eps`).
- Eigenvalues relative to `M = q^2 delta - q q` on the 3-dim quotient, divided by `rho_bar^2 p^2`: `rho R[g_rho]`: `-1/4, -1/4, -3/4`; `rho^2 X`: `1, 1, 1`. This confirms the integrated numbers. In addition, the eigenvector with `-3/4` is the one with `delta rho != 0` (script column), so the two `-1/4` modes are the `delta rho = 0` modes.
- Induced `Lambda^2` density `-(Lambda^2/32 pi^2) [ (N_tot/6) rho R[g_rho] + rho^2 X ]`. This is the integrated one-loop result (connection `(4/6) R + X`, ghost `-(2/6) R`, scalar `(1/6) R` each). Eigenvalue on a TT-type mode: `-N_tot/24 + 1`. Matching it to `c rho R[g_rho]` (eigenvalue `-c/4`): `c_T = N_tot/6 - 4`. `sector_table.py` gives `1/G_A - 1/G_T = 2 Lambda^2/pi` (common cutoff), `2 Lambda_v^2/pi` (separate), independent of `N_s`; scalar-only content gives zero.
- Caveats. This is the background-field Feynman operator of the integrated paragraph. Off-shell quadratic forms are gauge dependent, and the cone coefficient `N_tot` also includes the ghost count. Whether the ghost-weighted replica sum is the entropy of a physical algebra (edge modes of gauge sectors) is not addressed. The 3rd mode (`delta rho != 0`) is not used.

### 8. Cross-check with 014
In the CP^{1,2} level-one class the tree-level response is algebraic of degree 0 in `h` and `E[h] != const x T`; so condition `G_T = G_A` has no tree-level Einstein structure to act on. An induced term would have to supply it. That is the same structure of obstruction as item 5, in a different operator class; no quantitative link is claimed. The SME's low-confidence pointer ("014's cancelling loop term vs `1 - N_tot/24`") is not examined: the two classes differ (level-one fibre amplitudes vs Poisson gauge sector about constant `Theta_bar`).

### 9. What the no-go depends on, and what relaxes it (no-go bounded by its hypotheses)
Hypothesis class: Poisson limit; Euclid section; four matrix coordinates; bosonic content of the integrated paragraph (`N_s` real scalars plus gauge sector plus ghosts); Feynman background gauge; one-loop; `Lambda^2` term only; replica = pulled-back cover; quadratic form about constant `Theta_bar` on `delta rho = 0` modes.
Within-core relaxations that could restore `G_T = G_A`:
- content (fermions, extra scalars with torsion-squared endomorphism terms), which could cancel the `rho^2 X` term on the TT modes;
- the gauge-fixing (non-minimal gauges, non-Laplace type);
- Moyal corrections at the cutoff;
- `Phi`-`a` mixing and the Presentation-B frame coupling;
- a different identification of the tensor block than the `delta rho = 0` modes of `a^mu`;
- curved or non-constant backgrounds.
None of these is excluded here.

### 10. Risk flag (not examined)
The area-law premise of the cone term for a matrix-regularised region is not guaranteed (Karczmarek, Sabella, Garnier, arXiv:1310.8345, abstract-level only, via the SME report; not read by me). The replica here is that of the Poisson-limit QFT on the chart; whether it is the entropy of the matrix algebra is Problem A.

## Claim classification

| Claim | Class |
|---|---|
| Flat-cone coefficient `(1/12)(1/n - n)` and `S = A/48 pi eps^2` per component; `A/4G_ind` identity for `Q = 0` | established (standard; reproduced numerically to 1e-12 at `n = 2, 3` and symbolically; Solodukhin (70), (318)-(320)) |
| Contact term `Delta S = -2 pi tr Q <phi^2> A` | established (script; matches Solodukhin (322)-(323)) |
| Replica (I): `S = (A_G/48 pi) sum w tr 1 Lambda^2` for the Poisson-limit operators; equals the `Lambda^2` coefficient of `thm:Geff` with `Q = 0` | conditional (Poisson limit, Euclid, background gauge, bounded `E, omega` on the pulled-back cover, chosen replica) |
| `E_s = R_G/4 + T^2/16 + TT'/8`; `tr B^2 = -X` | established identities (numerical to rounding on random samples) |
| `A_{1,R,s}` basis dependence (sign flips) | conditional on the class; established there |
| (II): `-1/12` per component, factor `-1/2` | conditional (block class, regular branch at `m = 0`); exact summation for scalar and component; second-order `ln` terms ignored |
| TT eigenvalues `-1/4, -3/4; 1` and `c_T = N_tot/6 - 4` | established computation (independent of 005 code), conditional on the class and gauge |
| `1/G_A - 1/G_T = 2 Lambda_v^2/pi`, independent of `N_s` | conditional (same) |
| Reduction: `ass:EE` with Jacobson geometry requires `m_T = 0` and `G_T = G_A` | conditional on Jacobson's tensor-equation step, on the FP structure of `eq:Top-improved`, and on reading `T^op` as the metric response of the quadratic action |
| That `thm:mT` hides `G_T = G_A` | established (reading of ch07: unit coefficients and `h = T`) |
| Whether the ghost-weighted cone sum is a physical entropy; edge modes | unresolved |
| `ass:EE`, off-shell stationarity, map `Theta -> G`, `G_eff` value/sign | unresolved (not touched) |

## Proposed changes

All three items are conditional and scoped. No label is touched. New labels: none. Labels verified to exist (searched in `chapters/`): `sec:status-F`, `sec:status-B`, `ass:emergent-op`, `thm:Geff`, `eq:universal-R`, `eq:first-law`, `eq:first-law-zero`, `eq:deltaA-G`, `eq:Top-improved`, `eq:mass-identity`, `prop:ward`, `ass:EE`, `thm:mT`, `eq:W-again`. `\LUV` is used in appH. Text is for CRLF files (the integrator normalises).

### Item 1: appH, Section `sec:status-B`
Insert two paragraphs after the "Replica insertion identity" paragraph.
- Anchor (occurs once, l. 139-140): "...Those inputs are not supplied by the displayed microscopic\naction. Problems~B, C, D, F and~G remain open."
- Kept: everything before and after. New text goes between that sentence and `\section{Problem C: conformal mode and Cassini}`.
- Justification for placing it in `sec:status-B` rather than before `\section{Problem G}`: the content concerns the area coefficient of `eq:first-law` and the Ward-identity normalisation (B), the existing Problem-B section already contains the replica paragraph, and the Problem-F paragraphs are cross-referenced by `\ref{sec:status-F}`. The Problem-F facts it uses (operators, torsion identity) are not restated.

```latex
\paragraph{Replica cone coefficient of the Poisson-limit operators and the area term of the first law (conditional; not closure).}
Keep the setting of the Presentation~A Poisson-limit paragraphs of Section~\ref{sec:status-F}: four matrix coordinates, the Poisson limit, the Euclidean section \(\eta=\delta\), the scalar operator \(\mathcal O_s\), the connection operator \(\mathcal O_v\) acting on the internal index of \(a^\mu\) in background gauge, the ghost operator of weight \(-2\), \(G=\rho\,g_\rho\) with \(\sqrt{|G|}=\rho^2\), Assumption~\ref{ass:emergent-op}, and one proper-time limit \(s_{\min,s}=\LUV_s^{-2}\) per sector, shared by the effective action and the replica entropy. Only the \(\LUV_s^2\) term is compared, for constant \(\LUV_s\); neither a value of \(G_{\mathrm{eff}}\) nor the relation \(S=A/4G\) is assumed.

\emph{Replica on the matrix chart.} Let \(Z_n\) be the partition function on the \(n\)-sheeted cover of the chart \(x\), branched over a two-surface \(\Sigma\), with every background field (\(\Theta\), hence \(G\), \(g_\rho\), \(\rho\), the connections and the endomorphisms) pulled back. Then \(G\) and \(g_\rho\) are conical with the same angle \(2\pi n\) and \(\rho\) is a regular density of the chart: the cone is on \(G\) and \(g_\rho\) together. For a Laplace-type sector whose connection and endomorphism stay bounded on the cover, the leading surface term of the heat trace is the flat-cone term~\cite{Solodukhin2011},
\[
  \operatorname{Tr}e^{-s\mathcal O}\big|_n-n\operatorname{Tr}e^{-s\mathcal O}\big|_1
  =\operatorname{tr}\mathbb I\;\frac1{12}\Bigl(\frac1n-n\Bigr)\frac{A_G(\Sigma)}{4\pi s}+O(s^0),
\]
independent of the connection and of the endomorphism. The fibre index of \(\mathcal O_v\) is internal, so the fibre is not rotated around \(\Sigma\) by a Levi-Civita holonomy. With \(S=(1-n\partial_n)(\ln Z_n-n\ln Z_1)|_{n=1}\) and \(\ln Z_n=\tfrac12\sum_sw_s\int\mathrm{d}s\,s^{-1}\operatorname{Tr}e^{-s\mathcal O_s}\),
\[
  S=\frac{A_G(\Sigma)}{48\pi}\sum_sw_s\operatorname{tr}\mathbb I_s\,\LUV_s^2
\]
(the \(\mu_s^2\) terms of Theorem~\ref{thm:Geff} subtracted). The same limits in Equation~\eqref{eq:universal-R} give, for the coefficient of \(\int\sqrt{G}\,R_G\) when the endomorphisms carry no explicit curvature, \(1/(16\pi G)=\sum_sw_s\operatorname{tr}\mathbb I_s\,\LUV_s^2/(192\pi^2)\). Hence \(S=A_G(\Sigma)/(4G)\) with that \(G\): for these operators the coefficient of \(\delta A\) in Equation~\eqref{eq:first-law} is the \(\LUV^2\) coefficient of Theorem~\ref{thm:Geff}, \(A=1/(12\pi)\) per unit weighted fibre trace as in the sector-sum paragraph of Section~\ref{sec:status-F}, and it is determined by the operators and the cutoff.

\emph{Contact term.} If an endomorphism is \(E_s=E_{0,s}+Q_sR_G\) and \(R_G\) is continued onto the cone with its conical delta, the heat trace gains \(-(1-n)\operatorname{tr}Q_s\,A_G/(4\pi s)\) and the entropy changes by \(-\tfrac{A_G}{8\pi}\sum_sw_s\operatorname{tr}Q_s\LUV_s^2=-2\pi A_G\sum_sw_s\operatorname{tr}Q_s\langle\phi^2\rangle_s\), \(\langle\phi^2\rangle_s=\LUV_s^2/(16\pi^2)\). This is the contact term of Susskind and Uglum~\cite{SusskindUglum1994}, \(S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q\) in Equations~(322)--(323) of~\cite{Solodukhin2011}, with \(S_{\mathrm{BH}}\) built from the coefficient \(\operatorname{tr}(\tfrac16-Q_s)\) of Theorem~\ref{thm:Geff}. With \((G,\rho,\partial\Theta)\) as independent variables, the scalar endomorphism \(E_s=-\tfrac12\Box_G\ln\rho+\tfrac14|\partial\ln\rho|_G^2\), the connection endomorphism with \(\operatorname{tr}E_v=4E_s+\operatorname{tr}(B_\sigma B^\sigma)\), \(\operatorname{tr}B_\sigma=0\), \(\operatorname{tr}(B_\sigma B^\sigma)=-X\), and the ghost operator \(-\mathcal O_s\) all have \(Q=0\) and are bounded on the pulled-back cover, so the contact term vanishes sector by sector.

\emph{Dependence on the independent variables.} The Weitzenb\"ock identity quoted in the paragraph on the torsion invariant gives \(E_s=\tfrac14R_G+\tfrac1{16}T_{\lambda\mu\nu}T^{\lambda\mu\nu}+\tfrac18T_{\lambda\mu\nu}T^{\mu\lambda\nu}\) and \(\operatorname{tr}(B_\sigma B^\sigma)=-T_{\lambda\mu\nu}T^{\lambda\mu\nu}\) (the first checked at random two-jets of a closed \(\omega\), for both signatures). With the coframe torsion in place of \(\partial\Theta\) as independent variable, the scalar operator has \(Q_s=\tfrac14\), and its coefficient \(\mathcal A_{1,R,s}\) is \(\tfrac16-\tfrac14=-\tfrac1{12}\) per component instead of \(\tfrac16\), of opposite sign. The coefficient \(\mathcal A_{1,R,s}\) of Theorem~\ref{thm:Geff} is therefore not a function of these operators alone. With \(N_{\mathrm{tot}}=N_s+2\) as in the Poisson-limit paragraph, the weighted coefficient \(c\) of \(\sqrt G\,R_G\) in \(\operatorname{tr}(R_G/6-E)\) is:
\begin{center}
\begin{tabular}{@{}lcc@{}}
\toprule
sector (weight) & \(c\) in \((G,\rho,\partial\Theta)\) & \(c\) in \((G,\text{torsion})\)\\
\midrule
\(N_s\) scalar components & \(N_s/6\) & \(-N_s/12\)\\
connection, 4 components & \(2/3\) & \(-1/3\)\\
ghost, weight \(-2\) & \(-1/3\) & \(1/6\)\\
total & \(N_{\mathrm{tot}}/6\) & \(-N_{\mathrm{tot}}/12\)\\
\bottomrule
\end{tabular}
\end{center}

\emph{Which geometry carries the cone.} The first column is the replica entropy above, \(S=(\LUV^2A_G/8\pi)\,c\), with \(\rho\) regular. The cone on \(G\) can instead be carried by the Poisson structure: for \(\Theta^{12}=1/f(x^1,x^2)\), \(\Theta^{34}=1\), one has \(G_\perp=f^2\delta\) and \(\rho=f\), and \(f=|z|^{n-1}\) makes \(G\) conical of angle \(2\pi n\) with \(\rho\propto r^{n-1}\) singular, \(g_\rho\) singular, and torsion unbounded, \(|T|^2\propto(n-1)^2/u^2\) at proper distance \(u\) from \(\Sigma\). Then \(E_s\) contains \(-\tfrac12\Box_G\ln\rho=\pi(1-n)\delta_\Sigma\), a contact term with \(Q=\tfrac14\), and \(\mathcal O_s\) reduces to a Bessel problem of index \(\sqrt{m^2+((n-1)/2)^2}/n\). With the branch regular at \(m=0\), the first-order coefficient is that of the second column, for the scalar and ghost and for the components of \(a^\mu\) in this block class (checked by direct summation over the angular modes and against the local \(a_1\) with the delta functions). The two choices differ by the factor \(-\tfrac12\) in every sector. The first is the replica of the same state, since \(\operatorname{Tr}\rho_D^n\) is built on the cover of the same background; the second changes the background with \(n\) and corresponds to a smooth-coframe reading of the induced action. Only the first is used in the identification above.

\paragraph{Normalisation of the tensor kinetic term against the area coefficient (conditional; not closure).}
Assume Equation~\eqref{eq:first-law-zero} for every small diamond, every unit timelike direction of \(\xi\) and the fixed-volume variations of the tensor block, with the geometry of Equation~\eqref{eq:deltaA-G} in the form of~\cite{Jacobson2016}, in which \(\delta A|_V\) is proportional to \(G^{(1)}_{00}[h]\), and write \(1/(4G_A)\) for the coefficient of \(\delta A\). A symmetric tensor whose contraction with every timelike unit vector vanishes is zero, so the condition is the tensor equation \(G^{(1)}_{\mu\nu}[h]=8\pi G_A\,\delta\langle T^{\mathrm{op}}_{\mu\nu}\rangle[h]\) up to a term proportional to \(\eta_{\mu\nu}\). For a tensor block with the Fierz--Pauli structure of Equation~\eqref{eq:Top-improved} this requires both \(m_T=0\) and \(G_T=G_A\), where \(1/(16\pi G_T)\) is the coefficient with which the quadratic action whose metric response defines \(T^{\mathrm{op}}\) carries the linearised Einstein form. The second condition is not implied by the first, by the identification of the area prefactor with the coefficient of Theorem~\ref{thm:Geff}, or by Proposition~\ref{prop:ward}: it equates the coefficient of the quadratic term of the block with the coefficient of the area term.

In the class of the Poisson-limit paragraphs, about a constant \(\bar\Theta\), the induced \(\LUV^2\) quadratic form on the two modes with \(\delta\rho=0\) is \(-\tfrac{\LUV^2}{32\pi^2}\bar\rho^{2}p_\eta^2\,(1-N_{\mathrm{tot}}/24)\,\mathcal M\), with \(\mathcal M\) the tree-level kernel of Remark~\ref{rem:ch3-trace-quadratic}. A term \(c\,\rho R[g_\rho]\) has eigenvalue \(-c/4\) on these modes, so the form is that of an Einstein term with \(c_T=N_{\mathrm{tot}}/6-4\), whereas the area coefficient above is \(c_A=N_{\mathrm{tot}}/6\). With a common cutoff \(1/G_T=(N_{\mathrm{tot}}-24)\LUV^2/(12\pi)\) and \(1/G_A=N_{\mathrm{tot}}\LUV^2/(12\pi)\); with the connection sector at its own limit \(\LUV_v\), \(1/G_A-1/G_T=2\LUV_v^2/\pi\), independent of \(N_s\). The difference is the term \(\rho^2X\) of the connection sector, which is bounded on the replica cover and contributes no entropy but contributes to the quadratic form; for scalar content alone \(G_T=G_A\). In this class and gauge the induced term therefore has the Einstein structure but not the coefficient that \(G_T=G_A\) requires, for every \(N_s\) and every \(\LUV_v>0\).

These statements are for the Poisson-limit operators of the preceding paragraphs at one loop, for the \(\LUV^2\) term, the replica above and the background gauge stated. They do not derive Assumption~\ref{ass:EE}, fixed-volume stationarity of the tensor block, or the identification of \(G\) with the emergent metric (Assumption~\ref{ass:emergent-op}); they do not treat the tree-level term (of lower order in momentum and not of Einstein form), fermions or additional scalars, Moyal corrections at the cutoff, the mixing of \(\Phi\) with \(a^\mu\), edge modes or the interpretation of the ghost-weighted sum as an entropy, or the logarithmic terms; the off-shell quadratic form is gauge dependent; and they give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open.
```

Remark~\ref{rem:ch3-trace-quadratic} exists in ch03 (label verified in my read: `\label{rem:ch3-trace-quadratic}` at line 450). I used `\mathcal M` there named M in remark: they write \mathcal M_{\alpha\beta}. ✓.

### Item 2: appG, Section `sec:replica-cone`
- Anchor (unique, l. 24-26): "with the prefactor identified from the Seeley--DeWitt coefficient\nthat multiplies the deficit. This is the standard result used in\nChapter~6 and Appendix~B. The conditional heat-kernel identity of Theorem~\ref{thm:Geff}".
- Replaces only the two sentences from "with the prefactor identified" through "Appendix~B."; the equation above and "The conditional heat-kernel identity of Theorem..." onward stay.

```latex
with the prefactor given by the Seeley--DeWitt coefficient that multiplies the
deficit. This is the standard cone computation for operators whose
endomorphism contains no explicit curvature coupling, on a replica geometry on
which the connection and the endomorphism stay bounded. For
\(E=E_0+QR\) the replica entropy differs from
\(\operatorname{Area}(\Sigma)/(4G_{\mathrm{eff}})\), with \(G_{\mathrm{eff}}\) the
curvature coefficient of Theorem~\ref{thm:Geff}, by a contact term proportional
to \(\operatorname{tr}Q\), and for operators built from a composite metric the
curvature coefficient depends on the independent variables chosen
(Section~\ref{sec:status-B}). Chapter~\ref{ch:entanglement-equilibrium} and
Appendix~\ref{app:modular} use \(1/(4G_{\mathrm{eff}})\) as the name of the
coefficient of \(\delta A\).
```
Stale in the same file: Section "Status" (l. 53-54) "The area term in \(S_D\) is the standard heat-kernel result." Left unchanged: it follows the replaced sentence and adds no derivation claim; a gatekeeper may prefer "is the standard heat-kernel term for the operators of Section~\ref{sec:replica-cone}". I recommend leaving it.

### Item 3: ch07, remark "What the theorem does not hide"
- Anchor (unique): "borrows a geometric identity used in Jacobson's argument. The\n  theorem is therefore a compatibility statement:".
- Insert after "argument." the following; the rest of the remark is kept.
```latex
The cancellation of the Einstein-operator terms
in~\eqref{eq:mass-identity} also uses that the coefficient of
\(\mathcal E_{\mu\nu}\) in the stress response~\eqref{eq:Top-improved}
equals the coefficient of \(\mathcal E_{\mu\nu}\) in the area
term~\eqref{eq:deltaA-G}; this equality of two coefficients is an input of the
theorem in addition to \(m_T=0\), and the identification of the area prefactor
with \(\Geff\) (Section~\ref{sec:status-B}) does not supply it.
```
Chapter~\ref{ch:entanglement-equilibrium} and `app:modular` labels exist (`ch:entanglement-equilibrium` verified; `app:modular` verified in appB l. 2).

### Item 4: bibliography (integrator adds)
```bibtex
@article{Solodukhin2011,
  author  = {Solodukhin, Sergey N.},
  title   = {Entanglement Entropy of Black Holes},
  journal = {Living Reviews in Relativity},
  volume  = {14},
  number  = {1},
  pages   = {8},
  year    = {2011},
  doi     = {10.12942/lrr-2011-8},
  eprint  = {1104.3712},
  archivePrefix = {arXiv}
}

@article{SusskindUglum1994,
  author  = {Susskind, Leonard and Uglum, John},
  title   = {Black hole entropy in canonical quantum gravity and superstring theory},
  journal = {Physical Review D},
  volume  = {50},
  pages   = {2700--2711},
  year    = {1994},
  doi     = {10.1103/PhysRevD.50.2700},
  eprint  = {hep-th/9401070},
  archivePrefix = {arXiv}
}
```
Verification: Solodukhin, Crossref record (title, journal, volume 14, issue 1, article 8, year 2011) and arXiv PDF text read for the cited equations. Susskind-Uglum, Crossref (volume, pages, authors, 1994) and arXiv abstract. `Jacobson2016` is already in `bib/namcg.bib`. Kabat (arXiv:hep-th/9503016) is not cited in the manuscript text.

### Stale passages elsewhere
- appG, "Status" sentence (see item 2): left; not stale after item 2.
- ch08, Theorem `thm:Geff` and "Endomorphism and threshold terms": "\(A_{1,R,s}\) includes the specified endomorphism" does not state the dependence on the independent variables for a composite metric. Not edited here: a Problem-F item (the physical G_eff normalisation is the replica or the graviton-propagator coefficient, not the coefficient of R in an unspecified basis). Recommended follow-up with the next Problem-F package.
- ch06, `eq:first-law` text ("is only a name"): consistent, unchanged.
- ch17, Problem B and F paragraphs: unchanged; no label is affected.

## Verification scripts

All in `proposals/015-entropy-action-identity/`; each writes a `.out.txt` next to it. Run with `python <script>`.
- `cone_checks.py` (+ `cone_checks.out.txt`). (1) Mellin transform of `e^{-t} I_nu` (closed form vs numerics, continuation to `-nu`); zeta-regularised `Tr K_n - n Tr K_1 = (1-n^2)/(12 n)`; `(1 - n d_n)` gives 1/6. (2) `S = A/48 pi eps^2`, `1/G_ind = 1/12 pi eps^2`, `S = A/4G_ind`; contact term `-xi A/8 pi eps^2 = -2 pi xi A <phi^2>`; `S_cone - S_BH = Q`. (3) Direct numerical heat-trace sum (no regularisation): `D_I(2) = -0.125000000000`, `D_I(3) = -0.222222222222`; first-order `F'(1)`: (I) `-0.16667`; (II) scalar `0.08333`; (II) block-class connection component `0.08333`. (4) Local `a_1` with `R_sing` and `E_sing = pi(1-n) delta`: ratio `-1/2`, `c = 1/4`.
- `operator_identities.py` (+ `.out.txt`). `O_s = -D^2 + E`; `sqrt|G|(R_G/6 - E) = rho R[g_rho]/6` (random point, residual ~1e-16); `tr B = 0`, `tr(B_s B^s) = -X` (both signatures).
- `verify_E_torsion.py` (+ `.out.txt`). `E_s = R_G/4 + T^2/16 + TT'/8` on random closed-`omega` two-jets, both signatures (residual ~1e-16; one large Lorentz sample 2e-11).
- `tt_quadratic_forms.py` (+ `.out.txt`). Independent recomputation of the phase-averaged second-order forms of `rho R[g_rho]` and `rho^2 X` about constant `Theta_bar`; eigenvalues relative to `M` (`-1/4, -1/4, -3/4` and `1, 1, 1`); identifies the `-3/4` mode as the `delta rho != 0` mode; gauge residual `|M q|` ~1e-6.
- `sector_table.py` (+ `.out.txt`). Sector table; `c_T = N_tot/6 - 4`; `1/G_A - 1/G_T`; scalar-only equality.
These are checks, not proofs; the reasoning is in "Research and reasoning".

## Decisions Taken

1. **Replica geometry.** Decision: (I) pulled-back replica (cone on `G` and `g_rho` together, `rho` regular) is the replica used for B2. Report (II) as the alternative with its numbers. Reason: `Tr rho_D^n` is the same state replicated; (II) changes the background with `n`, gives a negative coefficient and is a smooth-coframe regularisation of the action. Rejected: adopting (II), or treating the choice as immaterial (it changes the coefficient by `-1/2`).
2. **Location of new appH text.** Decision: `sec:status-B`, after the replica paragraph. Reason: the result is about the area coefficient of `eq:first-law` and the Ward-identity normalisation. Rejected: before `\section{Problem G}` (reserved for the Presentation-A/F series).
3. **appG and ch07 edits.** Decision: replace one appG sentence and add one ch07 sentence, because they are the two prior claims affected; ch06 unchanged. Full scan done. Rejected: leaving appG's unconditional "standard result", which is false for `E` with curvature coupling (a PRIOR-CLAIM flag), and silently editing ch06.
4. **Definition of `G_T`.** Decision: by the TT modes with `delta rho = 0` (gauge-invariant structure `M`), not by the full quadratic form, because the `delta rho != 0` mode has `3/4` instead of `1/4`. Rejected: a trace over all three modes.
5. **No `Kabat` citation.** The `a^mu` index is internal, not a Levi-Civita vector; the contact term here is Q-type from `R_G` or `Box ln rho`.
6. **Hypothesis class stated explicitly** (Research section 9), with within-core relaxations listed instead of presenting the obstruction as conclusive.
7. **Gauge.** Only the Feynman background gauge (Laplace type) is treated; other gauges are listed as a relaxation, not computed.

## Milestone assessment

- M1: no (B2 is only conditional; stationarity, the map and `ass:EE` are untouched; the "match" is the standard Sakharov-type identity for `Q = 0`).
- M2: yes, bounded no-go: in the 005/Poisson-limit class the induced term cannot satisfy `G_T = G_A` for any `N_s` and any positive `Lambda_v` (hypothesis class in Research section 9).
- M3: narrow, candidate (gatekeeper to decide). (a) appG's unconditional "standard result" (false for curvature-coupled `E`); (b) the `thm:mT` hypothesis list omits `G_T = G_A`; (c) `thm:Geff`'s `A_{1,R,s}` is variable-dependent for composite `G`. None changes a label, none is load-bearing for a numerical claim.
- Not a breakthrough; no critical-path step is derived.

## Status-label recommendation

None. Critical-path set (ch17 sec:ch17-done): A, B, C, D1, E, F, G-derived, N. B remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; F remains OPEN as well. No label edit appears in any block above.

## Author decision needed

None. (No label, scope or core change; spacetime stays emergent: the cone is on the emergent `G`, and nothing fundamental is added.)

## Remaining open step

Not derived: stationarity `delta S_D = 0` for the tensor block (B1), the matrix-to-emergent map (B3, A), and `ass:EE` itself. Not examined: the tree-level term and its interplay with the induced term; fermions, extra scalars and other gauges that could change the TT balance; Moyal corrections at the cutoff; edge modes and the ghost-weighted entropy; the logarithmic (`a_2`) terms and their cone partners (expected to match by the same argument with `a_2^Sigma`; not computed); positivity checks (Fisher information, N); an area-law test for matrix regularisation (the SME's risk flag). Natural next package: determine whether content or gauge can cancel the `rho^2 X` term on the TT modes (a condition on content, not a derivation), or whether `G_T = G_A` can be obtained from a derived extra stress in the CP^{1,2} class.

## Special instructions for the gatekeeper

- Do not read this as closing B or B2 in the sense of ch17. The "match" is the Sakharov-type identity for operators with no curvature coupling in the chosen variables; the TT result is a bounded obstruction. No `S = A/4` or external `G` enters; the cone is on the emergent `G` (Assumption `ass:emergent-op`).
- Re-run all five scripts. Re-derive: the cone coefficient `(1/12)(1/n - n)` and `(1 - n d_n)`; `Delta S = -2 pi tr Q <phi^2> A`; `E_s = R/4 + torsion^2`; the relation `c_T = N_tot/6 - 4`; the Jacobson-based reduction (check eqs. (22)-(24), (27) in arXiv:1505.04753).
- Points likely to be contested and their status:
  - (a) the "bounded on the pulled-back cover" step (no uniform remainder estimate for lifted smooth potentials is given; only the first-order argument);
  - (b) the regular branch at `m = 0` in (II) (another self-adjoint extension gives `5/12`, and the matching with the local `a_1` supports the chosen one);
  - (c) whether the weighted ghost sum is a physical entropy, and gauge dependence of the quadratic form; I flag both and do not claim them;
  - (d) the sign convention of the stress response relative to Jacobson (ch07 Exercise 4 already flags this); the proposed text states the equality of coefficients, not signs.
- PRIOR-CLAIM flags to adjudicate: appG sentence (item 2), ch07 hypothesis list (item 3), `thm:Geff` `A_{1,R,s}` (not edited).
- Check CRLF handling and the new labels (none added); the citation keys `Solodukhin2011`, `SusskindUglum1994` need the BibTeX of item 4 (verified as stated; Kabat not cited).
- The gatekeeper should confirm the full-scan claim: every file under `chapters/` (ch01-ch18, appA-appL incl. all of appH) was read by me; appendices C, D, E and I (phenomenology) only for the absence of conflicting statements.
