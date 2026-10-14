# Proposal 002-auto-target (induced Weyl pole, Problem N), round 1

## Result

This is a conditional reduction of Problem N together with a bounded no-go. It does not close N.

Work inside the manuscript's conditional, truncated heat-kernel identity (Theorem `thm:Geff`, eq. `eq:W-expand`). Use the
Appendix A continuation and common proper-time limits `LUV, mu`. The induced one-loop action then fixes how the
four-derivative coefficients compare with the induced Einstein-Hilbert coefficient. Three results follow.

1. **Local truncation (established within the stated truncation).** The induced Lorentzian Weyl coefficient of `eq:W4` is
   `c_W = W_C L/(32 pi^2)`, with `L = ln(LUV^2/mu^2)` and `W_C = sum_s w_s c_{C,s}` the weighted `C^2` coefficient of the
   traced `a_2`. The flat-space spin-2 quadratic form of `R/(16 pi G) + c_W C^2 + c_R R^2` is proportional to
   `k^2 (1 - 32 pi G c_W k^2)`. So there is an extra spin-2 pole whose residue has the opposite sign to the graviton's, at
     `m_2^2 = -1/(32 pi G_eff c_W) = -Upsilon LUV^2 / L`,   with   `Upsilon := pi/(G_eff W_C LUV^2)`.
   - If `G_eff W_C > 0`, the pole is a **tachyonic ghost**. In `eq:stelle` notation, `alpha = -2 c_W < 0`.
   - It lies below the cutoff exactly when `L > Upsilon`.
   - Take `1/G_eff` from the universal `a_1` term alone. Then `Upsilon = A_1/(2 W_C)`, which does not depend on `LUV`.
     For minimally coupled real scalars, `Upsilon = 10` for every `N_0 > 0`. The ghost is then below `LUV` once
     `LUV/mu > e^5`.
   - The spin-0 pole is healthy: `m_0^2 = 1/(96 pi G c_R)`, which is `2 LUV^2/L` for minimally coupled scalars.
   - Consequence: within the manuscript's own local truncation, the Weyl correction relative to the Einstein term is
     `(L/Upsilon) k^2/LUV^2`, not `k^2/LUV^2`. Compositeness alone does not put the extra spin-2 pole above `LUV`.
     Where the pole sits relative to `LUV` is set by a ratio of weighted traces and by `L`.
2. **Momentum-resolved form factor (conditional).** The fixed-`mu` local form does not apply at `mu << |k| << LUV`. There,
   for massless sectors, `L` is replaced by `ln(LUV^2/k^2) + delta_W`. The spin-2 factor becomes
   `F(x) = 1 - (x/Upsilon)(ln(1/x) + delta_W)`, with `x = k^2/LUV^2`.
   - Its principal-sheet zeros are `x = -Upsilon / W_j(-Upsilon e^{-delta_W})`, `j in {0,-1}` (Lambert W branches).
   - `F` has no zero in the disc `|k^2| < LUV^2` exactly when `Upsilon > Upsilon_*(delta_W)`. This is a numerical
     finding, cross-checked by an argument-principle count.
   - `Upsilon_*(0) = pi/2`, exactly: the zeros cross the unit circle at `x = +-i`.
   - `Upsilon_*(delta_W) = delta_W` for `delta_W >= 1` (numerical).
   - For `Upsilon = 10` the condition is `-9.58 < delta_W < 10`.
3. **Consequence for Problem N.** Within this truncation, "no ghost pole below `LUV`" is a numerical condition on
   `(Upsilon, delta_W)`. Both are Problem-F outputs, and the condition is decided at `|k| ~ LUV`, where the derivative
   expansion is not controlled. It does not follow from the metric being composite. N remains OPEN. Its missing step is
   now sharpened to computing `W_C`, `G_eff` (hence `Upsilon`), and `delta_W`, and controlling the form factor near `LUV`.

## Target and status

- **Problem N** (Appendix H `sec:status-N`, lines 1836-1860; Chapter 17, lines 497-513 and 724-728).
  - Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. Appendix H and
    Chapter 17 agree on this.
  - Original target (Ch. 17): derive from the matrix path integral, not from Stelle's action `eq:stelle`, that the graviton
    two-point function has no propagating Ostrogradsky ghost for `p < LUV`. This must hold for the values of `alpha` and
    `G_eff` computed in Problem F, and the region of those values must be stated. A result valid only for a truncated or
    imposed expansion leaves Assumption `ass:EFT-a2` in place.
  - Dependencies: Problem F (values of `G_eff` and `a_2` coefficients), and through F also Problems D1, C and A
    (dictionary). Chapter 17 orders N after F.
  - Appendix H status sentence currently: "Remains Assumption~\ref{ass:EFT-a2}. No computation is recorded."
- **Classification of this package:** PROGRAMME-CONDITIONAL. It is not DERIVED. It uses the Presentation-B heat-kernel
  truncation, assumed sector content, a continuation convention, and an extrapolated form factor.
- **Current critical-path set**, re-derived from `sec:ch17-done` (lines 697-729) and checked against each Appendix H ledger
  label: A, B, C, D1, E, F, G-derived and N are all OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. H, I and J are OPTIONAL.
  No discrepancy between Chapter 17 and Appendix H.
- **Discrepancy flagged (notation, not status).** The symbol `alpha` has three meanings:
  - the coefficient of `a_2[g]` in `eq:W-again-9` and `eq:W-through-2`;
  - the Weyl coefficient in `eq:stelle`;
  - the ECG reduced coupling `alpha = -16 pi G beta_ECG` (Ch. 13 and Appendix H, Problem J).

  N's target refers to "the values of `alpha` and `G_eff` computed in Problem F", which is ambiguous. The proposed text
  avoids the problem by working with `c_W, c_R` of `eq:W4` and stating `alpha = -2 c_W` explicitly for `eq:stelle`.

## Source reading

**Full scan.** I read the digest first (`DIGEST CURRENT`, chapters-hash d3558e44b583da45, dirty-chapters: no). Then I read
in full all 30 current `chapters/*.tex` files:
- ch01–ch18 (ch09 all 385 lines, ch17 all 787 lines);
- appA–appL (appH all 1869 lines, read in ranges 1-340, 340-1099, 1099-1498, 1499-1833, 1830-1869).

A full scan is required because the package edits a status passage: the appH Problem N "Status" sentence. No file was
unreadable. I also read `bib/namcg.bib` entries for `Vassilevich2003` and `Stelle1977`, `MILESTONE.md`, `CLAUDE.md` and
`reports/ledger.md` (empty). I checked `proposals/001-full-gr-scope/proposal-r2.md` (unreviewed). It concerns a
full-GR-criterion scope edit, is unrelated to N, and this package does not build on it.

Passages relied on:
- Ch. 8: `eq:ch8-sector-sum`, `eq:W-again`, `eq:s-limits`, `eq:W-expand`, `eq:universal-R`, `thm:Geff`, `eq:W-EH`,
  `eq:Geff-structure`.
- Appendix A: `eq:appA-a2`, `eq:appA-Wexp`, and the continuation convention `S_E = -i S_L`, `t = -i tau` at lines 158-170.
- Ch. 9: `eq:W4`, `eq:GB`, `eq:stelle`, `ass:EFT-a2` and lines 141-145.
- Appendix H, Problem C: the `S_EH^(2) = (1/16 pi G)(1/4) h E[h]` normalization, lines 259-270.
- Appendix H, Problem F: Hermitian block `Q = 0`, lines 1201-1230 and 1395-1423.
- Ch. 16: line 139-143 (ghost pole below `LUV` listed as a killer).
- Ch. 2: curvature conventions, `eq:riemann`.

## Research and reasoning

### R1. Induced coefficients (from the manuscript's identity)

By `eq:W-expand`, with common limits:

`W_E ⊃ -(1/(32 pi^2)) ∫ sqrt(g) [ A_1 (LUV^2 - mu^2) R_E + L sum_s w_s a_{2,s} ]`, where `A_1 := sum_s w_s A_{1,R,s}`.

Rewriting the curvature part of `a_2` (`eq:appA-a2`) in the basis `{C^2, R^2, E_GB}` gives
`(Riem^2 - Ric^2)/180 = C^2/120 - E_GB/360 + 0·R^2`. So for a real scalar sector with `E = E_0 + Q R`:
- the `C^2` coefficient is `tr I/120`;
- the `R^2` coefficient is `(1/2) tr(1/6 - Q)^2`.

Both are checked in `check_induced_pole.py`. For non-scalar sectors, `E^2` (via Ricci-dependent `E`) and `F^2` (bundle
curvature) also feed `C^2` and `R^2`, so `W_C`, `W_R` must be defined as the full weighted coefficients.

Continuation: Appendix A uses `S_E = -i S_L`, `t = -i tau`, and maps the vacuum term with `L_L = -L_E`. With curvature
scalars continued without a sign (mostly-plus Wick rotation), this gives:
- `1/(16 pi G_eff) = A_1 (LUV^2 - mu^2)/(32 pi^2)`. This is the manuscript's `C_R^E = -1/(16 pi G)`, and gives
  `1/G = N_0 LUV^2/(12 pi)` for `Q = 0`, matching appH "Sector sum".
- `c_W = W_C L/(32 pi^2)` and `c_R = W_R L/(32 pi^2)` in `eq:W4`.

The **relative** sign between the `R` and `C^2` coefficients is independent of the overall continuation sign, because both
come with the same `-1/(32 pi^2)` prefactor and both continue with the same factor. So the ghost and tachyon character of
the extra spin-2 pole is fixed by `sign(G_eff W_C)` alone.

### R2. Flat-space spin projections

The checks are in `check_spin_projections.py`, using sympy with Barnes-Rivers projectors in signature (-,+,+,+).

Method:
- `C^2` and `R^2` start at second order, so their quadratic parts are squares of linearized curvatures. The linearized
  Riemann tensor uses the MTW sign of `eq:riemann`.
- The Einstein-Hilbert quadratic part uses the manuscript's `(1/4) h^{mu nu} E_{mu nu}[h]`, with `E = -2 G^(1)`
  (appH Problem C).

Output:
- spin-2 coefficient `= -(k^2/(64 pi G)) (1 - 32 pi G c_W k^2)`;
- spin-0s coefficient `= (k^2/(32 pi G)) (1 + 96 pi G c_R k^2)`.

Consequences:
- The Weyl term does not enter spin 0. `R^2` does not enter spin 2. The Gauss-Bonnet quadratic form vanishes identically.
- Residues: the extra spin-2 pole has residue opposite to the massless graviton's (ghost). The extra spin-0 pole has
  residue opposite to the massless spin-0 (conformal-sign) pole, i.e. the same sign as the graviton (healthy).
- Stelle check: `c_W = -alpha/2` gives `m_2^2 = 1/(16 pi G alpha)`, a real-mass ghost for `alpha > 0`. This is consistent
  with Ch. 9, "order `1/sqrt(alpha G)`".

So `m_2^2 = -1/(32 pi G c_W)`, and with `Upsilon := pi/(G W_C LUV^2)` this is `m_2^2 = -Upsilon LUV^2/L`.

`m_0^2 = 1/(96 pi G c_R) = pi/(3 G W_R L)`. With `1/G = A_1 LUV^2/(2 pi)` this becomes `A_1 LUV^2/(6 W_R L)`.

Minimal scalars (`A_1 = N_0/6`, `W_C = N_0/120`, `W_R = N_0/72`) give `Upsilon = 10`, `m_2^2 = -10 LUV^2/L` and
`m_0^2 = 2 LUV^2/L`, all printed by `check_induced_pole.py`.

The Appendix H Problem F Hermitian block (16 components, `Q = 0`, weight 1) has the same per-component ratios. As a single
massless sector it would give `Upsilon = 10`, but it is massive (`m^2 = lambda v^2`), so it is only an illustration.

### R3. Why the local form fails at `|k| >> mu`

The small-`s` expansion integrated up to `s_max = mu^{-2}` is a derivative expansion. It applies to backgrounds varying
slowly on the scale `1/mu`. A perturbation of momentum `k >> mu` violates this for `s > 1/k^2`. At second order in
curvature, the one-loop action is a nonlocal form factor (Barvinsky–Vilkovisky, Covariant perturbation theory II, Nucl.
Phys. B 333 (1990) 471, DOI 10.1016/0550-3213(90)90047-H). If the form factor `f(s k^2)` decays for `s k^2 >> 1`, then

`∫_{LUV^-2}^{mu^-2} ds/s f(s k^2) = f(0) ln(LUV^2/k^2) + const + O(k^2/LUV^2, mu^2/k^2)`,

so the coefficient of the logarithm (the `a_2` value) is unchanged but `mu` is replaced by `k`.

`check_induced_pole.py` illustrates this for the potential-insertion form factor `∫_0^1 d alpha exp(-alpha(1-alpha) s k^2)`.
It finds `I - ln(LUV^2/k^2) = 1.4228 = 2 - gamma_E`, independent of `mu` from `10^-5` to `10^-9` (at `k = 10^-2`,
`10^-3`). The local value `ln(LUV^2/mu^2)` would instead be 23–41.

That the Weyl form factor decays at large argument is used, not re-derived. It is stated as an assumption in the proposed
text.

### R4. Disc criterion

With `L -> ln(1/x) + delta_W`, the zero condition `1 = (x/Upsilon)(ln(1/x) + delta_W)` becomes, with `x = e^{delta_W} y`,
`y ln(1/y) = Upsilon e^{-delta_W}`. So `ln y = W_j(-Upsilon e^{-delta_W})`.

Principal sheet (`Im ln x` in `(-pi, pi]`): only `j = 0, -1` qualify. `check_disc_criterion.py` tests branches -6..6 and
rejects all others.

Results:
- **Exact crossing at `delta_W = 0`:** `x = +-i` gives `F = 1 - pi/(2 Upsilon)`, so `Upsilon_*(0) = pi/2`.
- **Numerical results** (findroot, grid scan, argument-principle count on a keyhole contour; all are checks, not proofs):
  - `min|x|` is monotone increasing in `Upsilon` at fixed `delta_W` (scanned on `(0.05, 20)` for five `delta_W` values).
  - `Upsilon_*(delta_W)`: -10 → 10.41; -6 → 6.59; -4 → 4.755; -2 → 3.040; -1 → 2.27; 0 → 1.5708; 0.5 → 1.27;
    0.9 → 1.06; and `≈ delta_W` for `delta_W >= 1`, where the crossing is the real point `x = 1` with `F(1) = 1 - delta_W/Upsilon`.
  - `Upsilon = 10` window: `-9.5846 < delta_W < 10`. The argument-principle count is 2 zeros at -9.7, 0 zeros at
    -9.5, 0, 5 and 9.9, and 1 zero at 10.1 and 12.
  - At `Upsilon = 10`, `delta_W = 0`: the zeros are `x = -2.1216 ± 3.3144 i`, `|x| = 3.935`.

### R5. Literature

- Vassilevich 2003 (Phys. Rept. 388, 279; DOI 10.1016/j.physrep.2003.09.002; `Vassilevich2003` in bib): the standard
  `a_4` (manuscript's `a_2`) formula, matching `eq:appA-a2`. Bibliographic record verified; the formula was checked against
  `eq:appA-a2` from memory of the standard form, not re-fetched.
- Barvinsky & Vilkovisky 1990, NPB 333, 471: existence verified via the Crossref DOI record (title "Covariant perturbation
  theory (II). Second order in the curvature. General algorithms"). The abstract and full text could not be fetched (403).
  The specific claim that its Weyl form factor decays at large argument is **not independently verified**. The proposed
  text uses the citation only for "second-order curvature terms are nonlocal form factors" and states the decay as an
  assumption.
- Analogous literature, not cited in the proposed text: the resummed large-N graviton propagator has complex-conjugate poles
  whose location depends on the normalization scale. Calmet, Casadio, Kamenshchik & Teryaev, PLB 774 (2017) 332,
  arXiv:1708.01485; existence and abstract verified. That setting has `G` external and dimensional regularization. The
  present package differs in that `G_eff` is induced by the same sectors, which is what makes `Upsilon` cutoff-independent.
  Aydemir–Anber–Donoghue (arXiv:1203.5153) was checked and its abstract does **not** discuss graviton poles, so it is not
  cited.

### R6. Comparison with the original target

N requires a derivation from the matrix path integral for the Problem-F values, with the valid region stated. This package:
- supplies the form of that region (`Upsilon > Upsilon_*(delta_W)`), but only in the leading-log Presentation-B truncation;
- does not compute `Upsilon` or `delta_W`;
- does not control the form factor at `|k| ~ LUV`;
- does not derive anything from the matrix path integral.

It does show that the Ch. 9 justification of EFT-a2 ("available only because the metric is composite") does not by itself
place the extra pole above `LUV` within the induced truncation.

## Claim classification

| Claim | Class |
|---|---|
| `C^2`/`R^2`/`E_GB` decomposition of the scalar `a_2`; `C^2` coefficient `tr I/120`, `R^2` coefficient `(1/2)tr(1/6-Q)^2` | established identity (standard, re-checked symbolically) |
| Spin-2 and spin-0 coefficients of `R/(16piG)+c_W C^2+c_R R^2`; residue signs; `m_2^2=-1/(32piGc_W)`, `m_0^2=1/(96piGc_R)` | established derivation (standard; sympy check) |
| `c_W = W_C L/(32pi^2)`, `c_R = W_R L/(32pi^2)` and `1/(16piG) = A_1(LUV^2-mu^2)/(32pi^2)` | conditional on `thm:Geff` truncation, common limits, Appendix A continuation |
| `m_2^2 = -Upsilon LUV^2/L`; tachyonic ghost if `G W_C > 0`; below `LUV` iff `L > Upsilon` | conditional (as above, local truncation) |
| `Upsilon = A_1/(2 W_C)`; `= 10` for minimal scalars; `m_0^2 = 2LUV^2/L` | conditional (a_1-only `G_eff`, scalar sectors) |
| Positivity of `W_C`, `G_eff` for the actual locked-block sectors | unresolved (Problem F) |
| `L -> ln(LUV^2/k^2) + delta_W` for massless sectors at `mu << k << LUV` | conditional (standard nonlocal form factors; decay of Weyl form factor assumed; illustrated numerically for the potential form factor) |
| Lambert-W zero formula on the principal sheet | established (algebra, numerically verified) |
| `Upsilon_*(0) = pi/2` | established (exact) |
| `Upsilon_*(delta_W)` table, monotonicity, window `-9.58<delta_W<10` at `Upsilon=10` | numerical result (check, not proof) |
| Use of leading-log form factor up to `|k^2| ~ LUV^2` | unresolved (not controlled) |
| Whether complex zeros beyond `LUV` are propagating ghosts | unresolved / not claimed |
| Problem N discharged | **not claimed**; N remains OPEN |

## Proposed changes

### 1. `chapters/appH-microscopic-proofs.tex`: new paragraph in Problem N

Anchor: insert immediately after the "Missing step" paragraph of `\section{Problem N: control of the effective expansion}`,
whose last original sentence is (lines 1856-1857, unique, verified by search):

```
This is the requirement of item~6 of Chapter~\ref{ch:geometrogenesis}
and no stronger.
```

Insert the block below after this sentence and before `\paragraph{Status.}` (line 1859). Nothing is removed.

```latex
\paragraph{Induced Weyl term and the extra spin-two pole (conditional; not closure).}
Work in the truncated identity of Theorem~\ref{thm:Geff} on a flat
background, with every included sector assigned the common limits
\(\LUV,\mu\), \(\mu\ll\LUV\), and with the continuation of
Appendix~\ref{app:seeley-dewitt} (\(S_E=-iS_L\), curvature invariants
continued without change of sign). Rewrite the traced \(a_{2,s}\)
of~\eqref{eq:appA-a2} in the basis \(\{C^2,R^2,E_{\mathrm{GB}}\}\), and
let \(\mathcal W_C:=\sum_sw_sc_{C,s}\) and \(\mathcal W_R:=\sum_sw_sc_{R,s}\),
where \(c_{C,s}\) and \(c_{R,s}\) are the coefficients of
\(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\) and \(R^2\). For a real
scalar sector with \(E=E_0+QR\), \(c_{C,s}=\operatorname{tr}\mathbb I_s/120\)
and \(c_{R,s}=\tfrac12\operatorname{tr}(\tfrac16\mathbb I_s-Q)^2\); for
other sectors \(c_{C,s}\) also depends on \(E\) and on the bundle
curvature and is not computed here. The logarithmic term
of~\eqref{eq:W-expand} gives, in~\eqref{eq:W4},
\[
  c_W=\frac{\mathcal W_C L}{32\pi^2},\qquad
  c_R=\frac{\mathcal W_R L}{32\pi^2},\qquad
  L:=\ln\frac{\LUV^2}{\mu^2},
\]
that is, \(\alpha=-2c_W\) and \(\beta=2c_R\) in~\eqref{eq:stelle}; the
Gauss--Bonnet term does not contribute at quadratic order on a flat
background. With \(g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}\) and
\(k^2=\eta^{\mu\nu}k_\mu k_\nu\), the spin-two part of the quadratic form
of \(R/(16\pi G_{\mathrm{eff}})+c_WC^2+c_RR^2\) is proportional to
\(k^2(1-32\pi G_{\mathrm{eff}}c_Wk^2)\) and its spin-zero part to
\(k^2(1+96\pi G_{\mathrm{eff}}c_Rk^2)\) (a symbolic check, not a proof).
There is therefore a spin-two pole at \(k^2=-m_2^2\) with residue
opposite in sign to that of the massless graviton, and a spin-zero pole
at \(k^2=-m_0^2\) with residue of the graviton's sign, where
\[
  m_2^2=-\frac{1}{32\pi G_{\mathrm{eff}}c_W}
       =-\frac{\Upsilon\LUV^2}{L},
  \qquad
  m_0^2=\frac{1}{96\pi G_{\mathrm{eff}}c_R},
  \qquad
  \Upsilon:=\frac{\pi}{G_{\mathrm{eff}}\mathcal W_C\LUV^2}.
\]
If \(G_{\mathrm{eff}}\mathcal W_C>0\), the extra spin-two pole is a
tachyonic ghost, and it lies below the cutoff, \(|m_2|<\LUV\), exactly
when \(L>\Upsilon\). If \(1/G_{\mathrm{eff}}\) is taken from the
universal \(a_1\) term alone, \(1/G_{\mathrm{eff}}
=\mathcal A_1(\LUV^2-\mu^2)/(2\pi)\) with
\(\mathcal A_1:=\sum_sw_s\mathcal A_{1,R,s}\), and
\(\Upsilon=\mathcal A_1/(2\mathcal W_C)\) up to \(O(\mu^2/\LUV^2)\),
independent of \(\LUV\). For sectors of minimally coupled real scalars,
\(\mathcal A_1=\mathcal N_0/6\) and \(\mathcal W_C=\mathcal N_0/120\), so
\(\Upsilon=10\) for every \(\mathcal N_0>0\), the ghost lies below
\(\LUV\) once \(\LUV/\mu>e^{5}\), and \(m_0^2=2\LUV^2/L\). Within this
local truncation the Weyl correction relative to the Einstein term is
\(32\pi G_{\mathrm{eff}}c_Wk^2=(L/\Upsilon)\,k^2/\LUV^2\), not
\(k^2/\LUV^2\), and compositeness of the metric does not by itself place
the extra spin-two pole above \(\LUV\): its position relative to
\(\LUV\) is fixed by the ratio of weighted traces and by \(L\).

The fixed-\(L\) form is not the one-loop result at momenta
\(\mu\ll|k|\ll\LUV\). Second-order curvature terms of the one-loop
action are nonlocal form factors~\cite{Barvinsky1990}; assuming that
the Weyl form factor decays when \(sk^2\gg1\), its proper-time integral
is cut off at \(s\sim k^{-2}\) rather than at \(\mu^{-2}\), and for
massless sectors \(L\) is replaced by \(\ln(\LUV^2/k^2)+\delta_W\), with
a constant \(\delta_W\) fixed by the non-logarithmic part of the form
factor and by the finite Weyl counterterm. For the analogous
second-order form factor \(\int_0^1\mathrm d\tau\,
e^{-\tau(1-\tau)sk^2}\) of a potential insertion, a direct
numerical evaluation gives \(\ln(\LUV^2/k^2)+2-\gamma_{\mathrm E}\),
with \(\gamma_{\mathrm E}\) Euler's constant,
independent of \(\mu\) for \(k\gg\mu\); this illustrates the mechanism
and does not compute \(\delta_W\). With \(x:=k^2/\LUV^2\) and the
principal logarithm, the spin-two factor becomes
\[
  F(x)=1-\frac{x}{\Upsilon}\Bigl(\ln\frac1x+\delta_W\Bigr),
\]
whose zeros on the principal sheet are
\(x=-\Upsilon/W_j(-\Upsilon e^{-\delta_W})\), \(j\in\{0,-1\}\), with
\(W_j\) the branches of the Lambert function; \(\mu\) no longer enters.
At \(\delta_W=0\) the zeros cross \(|x|=1\) at \(x=\pm i\) when
\(\Upsilon=\pi/2\). A numerical scan with an argument-principle count
(a check, not a proof) finds that \(F\) has no zero in the disc
\(|k^2|<\LUV^2\) exactly when \(\Upsilon>\Upsilon_*(\delta_W)\), with
\(\Upsilon_*(0)=\pi/2\) and \(\Upsilon_*(\delta_W)=\delta_W\) for
\(\delta_W\ge1\), where the crossing is at \(x=1\). For \(\Upsilon=10\)
the condition is \(-9.58<\delta_W<10\); at \(\delta_W=0\) the zeros
are a complex-conjugate pair with \(|k^2|\approx3.9\LUV^2\).

These statements are conditional on the truncated identity, the
continuation and common limits stated, massless sectors (massive
sectors require the threshold functions of Problem~F), and the use of
the leading-logarithmic form factor up to \(|k^2|\sim\LUV^2\), where
the derivative expansion is not controlled. They do not compute
\(\mathcal W_C\), \(\mathcal A_1\), \(G_{\mathrm{eff}}\) or \(\delta_W\)
for the locked block, do not derive the induced coefficients from the
matrix path integral, and do not decide whether complex-conjugate zeros
beyond \(\LUV\) are propagating ghosts. Within this truncation, absence
of a ghost pole below \(\LUV\) is a numerical condition on \(\Upsilon\)
and \(\delta_W\), which are outputs of Problem~F, and is not implied by
the metric being composite. Problems~F and~N remain open.
```

Notes on the block:
- The labels used all exist exactly once: `thm:Geff` (ch08:187), `app:seeley-dewitt` (appA:2), `eq:appA-a2` (appA:77),
  `eq:W-expand` (ch08:131), `eq:W4` (ch09:62), `eq:stelle` (ch09:111). No new labels are introduced.
- `\LUV` is the existing macro.
- New symbols `\mathcal W_C`, `\mathcal W_R`, `\Upsilon`, `\delta_W` and `\mathcal A_1` (as a sum) do not occur elsewhere
  in `chapters/` (checked by grep).
- The form-factor integration variable is `\tau`, chosen to avoid any clash with the `\alpha` of `eq:stelle`.
  `\gamma_{\mathrm E}` is defined in the text as Euler's constant.

### 2. `chapters/appH-microscopic-proofs.tex`: Problem N status sentence (stale after item 1)

Replace exactly the second sentence of the Problem N "Status" paragraph (line 1860, unique):

```
Remains Assumption~\ref{ass:EFT-a2}. No computation is recorded.
```

with

```latex
Remains Assumption~\ref{ass:EFT-a2}. The conditional calculation above
does not discharge it.
```

The first sentence and the ledger label (lines 1839-1841) are unchanged. No status, priority or completion word changes.

### 3. Optional: `chapters/ch09-ultraviolet.tex`, Stelle paragraph (qualification of a sign assumption)

The current text says `eq:stelle` "propagates ... a massive spin-2 ghost and a massive scalar". That holds for `alpha > 0`,
`beta > 0`. Item 1 shows that the induced sign corresponds to `alpha < 0`.

Anchor: the last sentence of `\paragraph{Stelle quadratic gravity.}` (lines 124-126, unique ending "undetermined here."):

```
Whether such a pole lies
within the regime of the metric effective theory is therefore
undetermined here.
```

Append after it, in the same paragraph:

```latex
These statements take \(\alpha>0\) and \(\beta>0\). For \(\alpha<0\) the
extra spin-2 pole is tachyonic, with residue still opposite to that of
the graviton; Section~\ref{sec:status-N} records that a truncated
induced Weyl term has this sign when \(G_{\mathrm{eff}}\) and the
weighted Weyl trace are positive.
```

Label verified: `sec:status-N` (appH:1837). If the gatekeeper considers main-chapter edits out of scope for this package,
item 3 can be dropped without affecting items 1–2.

### 4. Bibliography (for the integrator; do not edit `bib/` from this proposal)

```bibtex
@article{Barvinsky1990,
  author  = {Barvinsky, A. O. and Vilkovisky, G. A.},
  title   = {Covariant Perturbation Theory ({II}). Second Order in the Curvature. General Algorithms},
  journal = {Nuclear Physics B},
  volume  = {333},
  number  = {2},
  pages   = {471--511},
  year    = {1990},
  doi     = {10.1016/0550-3213(90)90047-H}
}
```

The key `Barvinsky1990` is not present in `bib/namcg.bib` (checked).

### Stale passages elsewhere

None require change for consistency:
- Ch. 17 Problem N (lines 497-513) and the Ch. 17 criterion (724-728) remain accurate.
- Ch. 16 lines 139-143 (ghost below `LUV` as a killer) are consistent: item 1 shows the local truncation would realize this
  killer if `L > Upsilon`, which is a reason the local form cannot be used there.
- Ch. 9 exercise 3 ("same scale at which Stelle poles would have appeared") is consistent with item 1: both are set by
  `32 pi G c_W k^2 ~ 1`.
- `ass:EFT-a2` ("order `(p/LUV)^2`") is not edited. Item 1 records that in the induced truncation the factor is
  `(ln(LUV^2/p^2) + delta_W)/Upsilon` times `(p/LUV)^2`, or `L/Upsilon` in the local form. Changing the assumption's
  wording would be an assumption change and is left to the author.

## Verification scripts

All scripts are in `proposals/002-auto-target/` and run with `py -3 <script>` (sympy 1.14, mpmath). Outputs are saved as
`*.out.txt`.

- `check_spin_projections.py` / `.out.txt`. Linearized curvatures in mostly-plus signature and Barnes-Rivers projectors.
  It computes:
  - the spin-2 and spin-0s coefficients of `R/(16piG) + c_W C^2 + c_R R^2`;
  - the extra zeros and the residue ratios (-1 in both sectors, read with the conformal sign of the massless spin-0 pole);
  - the Stelle mapping `c_W = -alpha/2 -> k^2 = -1/(16 pi G alpha)`;
  - that the Gauss-Bonnet quadratic form vanishes identically.
- `check_induced_pole.py` / `.out.txt`. It computes:
  - `G_eff`, `m_2^2`, `m_0^2` and the TT expansion parameter from the induced coefficients;
  - the `C^2`/`E_GB`/`R^2` decomposition of `(Riem^2 - Ric^2)/180` and the `R^2` coefficient `(1/2)(1/6-Q)^2`;
  - the scalar values `Upsilon = 10`, `m_2^2/LUV^2 = -10/L`, `m_0^2/LUV^2 = 2/L`;
  - principal-sheet Lambert zeros for several `(Upsilon, delta_W)` (labelled `a, c` in the script) with residuals;
  - the illustrative form factor `I - ln(LUV^2/k^2) = 2 - gamma_E`, independent of `mu`.
- `check_disc_criterion.py` / `.out.txt`. It checks:
  - which Lambert branches give principal-sheet zeros (only 0, -1);
  - monotonicity of `min|x|` in `Upsilon`;
  - `Upsilon_*(delta_W)` on a grid, with no re-entry above threshold;
  - `Upsilon_*(0) = pi/2`;
  - argument-principle zero counts in the slit unit disc;
  - the `Upsilon = 10` window `(-9.58, 10)`.

Symbolic and numerical output is a check, not a proof. The proofs are the reasoning in R1–R4.

## Milestone assessment

Possibly **trigger 2 (new no-go result)**, in bounded form. Within the manuscript's own induced heat-kernel truncation,
the route "Assumption EFT-a2 holds because the metric is composite" (Ch. 9, lines 141-145) is ruled out as a parametric
argument:
- the extra spin-2 pole's position relative to `LUV` is a cutoff-independent number set by trace ratios;
- the local truncated form places a tachyonic ghost below `LUV` whenever `L > Upsilon` (`Upsilon = 10` for scalar content).

It also sharpens N's missing step into the stated `(Upsilon, delta_W)` condition. It does **not** meet trigger 1, because
nothing is derived from the matrix theory. It is not trigger 3: no merged claim is shown false. Ch. 9's statement is
qualified for `alpha < 0`, not refuted. If the gatekeeper judges the no-go too conditional to count, this is a routine
sharpening.

## Status-label recommendation

Current critical-path list, from `sec:ch17-done` and confirmed in Appendix H: A, B, C, D1, E, F, G-derived and N, all OPEN /
CRITICAL PATH / PROGRAMME-CONDITIONAL. Affected label: Problem N. **Recommendation: unchanged** (OPEN, CRITICAL PATH,
PROGRAMME-CONDITIONAL). No label edit is made in the LaTeX.

## Author decision needed

1. **Notation:** `alpha` has three meanings (Ch. 8/9 `a_2` prefactor; `eq:stelle` Weyl coefficient; ECG reduced
   coupling). The Ch. 17 and Appendix H wording of N ("the values of `alpha` and `G_eff` computed in Problem F") is
   ambiguous between the first two. The author may wish to restate N's target in terms of `c_W, c_R` of `eq:W4` (or
   `Upsilon`). This is a wording choice, not proposed here.
2. Whether `ass:EFT-a2`'s phrase "at order `(p/LUV)^2`" should be qualified to "up to a logarithm and a factor
   `1/Upsilon`". This would be an assumption-text change and is not proposed.

## Remaining open step

To close N one still needs:
- (a) the gauge-fixed locked-block operators and weights (Problem F, which needs D1), giving `W_C` and `G_eff`, hence
  `Upsilon`, including ghost and non-scalar sectors, whose Weyl coefficients depend on `E` and the bundle curvature;
- (b) the finite part `delta_W` in a stated scheme, including the finite Weyl counterterm;
- (c) massive-sector threshold functions in place of the massless logarithm;
- (d) control of the two-point function at `|k| ~ LUV`, beyond the leading-log form factor, where the decisive crossing
  occurs;
- (e) all of this derived from the matrix path integral (Problem A dictionary), not imposed in Presentation B.

Only then can `Upsilon > Upsilon_*(delta_W)`, or its controlled replacement, be checked for the computed values.

## Special instructions for the gatekeeper

- **Do not let the text assert** that N is solved, that the graviton propagator is ghost-free for `p < LUV`, or that
  `Upsilon = 10` holds for NAMCG. The value 10 is for minimally coupled scalar sectors with `G` from `a_1` only, and the
  Hermitian block mention in the proposal notes is illustrative. The proposed LaTeX deliberately does not apply it to the
  locked block.
- **Re-derive:**
  - `(Riem^2 - Ric^2)/180 = C^2/120 - E_GB/360`;
  - the TT quadratic form `C^2 -> (1/2) k^4 h·h` with `R^(1) = 0`, and spin-2 coefficient
    `-(k^2/64piG)(1 - 32piG c_W k^2)`;
  - `m_2^2 = -1/(32 pi G c_W)` and the Stelle check `alpha > 0 -> m^2 = 1/(16 pi G alpha)`;
  - `32 pi G c_W = 2 W_C L/(A_1 LUV^2)` from `1/G = A_1 LUV^2/(2pi)`;
  - `Upsilon_*(0) = pi/2` from `x = i`: `F = 1 - (i/Upsilon)(-i pi/2) = 1 - pi/(2 Upsilon)`.
- **Check the continuation argument:** the relative sign of the `R` and `C^2` coefficients does not depend on the overall
  Euclidean-to-Lorentzian sign, provided both curvature invariants continue with the same factor.
- **Numbers that appear nowhere else in the repository** are all produced by the saved scripts: 10, `e^5`, 2/L, `pi/2`,
  -9.58, 10, 3.9, `2 - gamma_E`. Re-run the scripts.
- **Citation:** the Barvinsky–Vilkovisky decay property is not verified beyond the bibliographic record. The text states it
  as an assumption, and the gatekeeper should keep it that way.
- **Separate observation, not part of this package.** `chapters/appK-endomorphism.tex` writes `a_1 = tr(E) - (1/6) R dim`.
  That is the opposite overall sign to `eq:appA-a1` / `eq:a0a1` (`a_1 = tr(R/6 - E)`). Appendix K's conclusion
  `delta a_1 = 0` is unaffected, so this is a non-load-bearing sign-convention inconsistency. It is recorded for a later
  bookkeeping item.
- Item 3 (Ch. 9) is optional and separable.
- No scratch LaTeX build was run: the copy-outside-repo command was not permitted in this session. The LaTeX blocks use only existing macros (`\LUV`, `\mathcal`, `\operatorname`) and verified labels, but `python scripts/build_check.py` must be run at integration.
