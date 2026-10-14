# Proposal 002-auto-target (induced Weyl pole, Problem N), round 2

## Result

This package is a conditional sharpening of Problem N. It does not close N, and it is not a no-go.

Setting: the manuscript's conditional, truncated heat-kernel identity (Theorem `thm:Geff`, eq. `eq:W-expand`), expanded
about flat space with the vacuum term cancelled or neglected, with common proper-time limits `LUV, mu`, `S_E = -i S_L`,
and the added convention that curvature invariants continue without a sign change. In this setting:

1. **Local (fixed-`L`) truncation.**
   - The induced coefficients in `eq:W4` are `c_W = W_C L/(32 pi^2)` and `c_R = W_R L/(32 pi^2)`, with
     `L = ln(LUV^2/mu^2)`.
   - The spin-2 factor is `k^2 (1 - 32 pi G_eff c_W k^2)`. The extra spin-2 pole is at
     `m_2^2 = -Upsilon LUV^2/L`, with `Upsilon := pi/(G_eff W_C LUV^2)`. It is a tachyonic ghost if `G_eff W_C > 0`.
   - With `1/G_eff` from `a_1` alone, `Upsilon = A_1/(2 W_C)`. This does not depend on `LUV`. It equals 10 for minimally
     coupled real scalars.
   - **Scope of the pole statement (corrected in this round).** `|m_2|^2/mu^2 = Upsilon e^L/L`, which is `>> 1` for
     `mu << LUV` unless `Upsilon` is exponentially small. So the fixed-`L` pole always lies at momenta where the
     fixed-`L` form does not apply. It is a property of that form, not a one-loop prediction.
   - The fixed-`L` statement that is valid for `|k| <~ mu`: the Weyl correction relative to the Einstein term is
     `(L/Upsilon) k^2/LUV^2`.
2. **Leading-log form-factor model (conditional).** For massless sectors at `mu << |k| << LUV`, `L` is replaced by
   `ln(LUV^2/k^2) + delta_W`, assuming the Weyl form factor decays. This gives the model
   `F(x) = 1 - (x/Upsilon)(ln(1/x) + delta_W)`, with `x = k^2/LUV^2`.
   - Its principal-sheet zeros are `x = -Upsilon/W_j(-Upsilon e^{-delta_W})`, `j in {0,-1}`.
   - Exact unit-circle crossings: `Upsilon_*(0) = pi/2`, and `Upsilon_*(delta_W) = delta_W` for `delta_W >= 1`.
   - Numerically, `F` has no zero in `|x| < 1` iff `Upsilon > Upsilon_*(delta_W)`. For `Upsilon = 10` this means
     `-9.58 < delta_W < 10`.
3. **Consequence for N.** Within the leading-log model `F`, absence of a zero in `|k^2| < LUV^2` is a numerical condition
   on `(Upsilon, delta_W)`. Both are Problem-F outputs. The condition is not implied by compositeness alone. N's missing
   step is sharpened to: compute `W_C`, `G_eff` and `delta_W` for the locked block, and control the two-point function
   at `|k| ~ LUV`. N and F remain OPEN.

## Changelog against round 1

| Review finding | Change in r2 |
|---|---|
| 1 (major): fixed-`L` pole stated as a result | I adopted the gatekeeper's snippet, with one verified refinement: "`>> 1` for `mu << LUV` unless `Upsilon` is exponentially small". The reason is that `Upsilon e^L/L >= e Upsilon`, so `>> 1` needs `Upsilon` not exponentially small. The sentence "and it lies below the cutoff ... exactly when `L > Upsilon`" is now explicitly scoped to "this fixed-`L` form". I deleted the sentence "compositeness ... does not by itself place the extra spin-two pole above `LUV`: its position ... fixed by ... `L`". "Not implied by compositeness" is now supported only through the model `F`. The milestone-2 "no-go" claim is withdrawn, and neither the Result nor the Milestone section asserts it. |
| 2: closing sentence scope | Now reads "Within the leading-logarithmic model `F`, absence of a zero in `|k^2|<LUV^2` ...", as in the gatekeeper's snippet. |
| 3: flat background needs the vacuum term removed | Opening sentence now says "expanded about a flat background with the vacuum term cancelled or neglected so that flat space is a solution". |
| 4: continuation attribution | Now reads "with `S_E=-iS_L` as in Appendix~\ref{app:seeley-dewitt}, and with curvature invariants continued without change of sign (an added convention)". |
| 5: consecutive status lines | Item 2 now **deletes** only "No computation is recorded."; it no longer replaces it. The Status paragraph reads "Remains Assumption~\ref{ass:EFT-a2}." |
| 6: "not `k^2/LUV^2`" overstates | Now reads "`k^2/LUV^2` multiplied by `L/Upsilon`" (as `(L/\Upsilon)\,k^2/\LUV^2`), restricted to `|k| <~ mu`. |
| 7: `Upsilon_*` table | Recomputed from the exact crossing equations by the new `check_upsilon_star_r2.py` (see R4). Corrected values: -10 → 10.40, -1 → 2.26, 0.9 → 1.05 (1.0507), 0.5 → 1.268. The others are unchanged. |
| 8: `\cite{Barvinsky1990}` needs a bib edit | I removed the citation from the integration text, which now cites nothing new. The sentence is self-contained: "At second order in curvature the one-loop action is nonlocal, with momentum-dependent form factors". The decay property is still stated as an assumption. The bib entry is moved to "For the author", outside the integration text. |
| 9: appK `a_1` sign | Not fixed in this package. Recorded under "For the author". |
| 10: `alpha` overloading and N target wording | Not fixed in this package. Recorded under "For the author", with the gatekeeper's fuller list of occurrences. |

No new physics is introduced in r2. The only added explicit assumption is the one the gatekeeper required: the vacuum term
is cancelled or neglected.

## Target and status

- **Problem N** (`sec:status-N`, appH lines 1836-1860; Ch. 17 lines 497-513, criterion item lines 724-728).
  - Ledger label, re-read this round: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion:
    PROGRAMME-CONDITIONAL." Chapter 17 agrees.
  - Original target: derive from the matrix path integral that the graviton two-point function has no propagating
    Ostrogradsky ghost for `p < LUV`, for the Problem-F values of the four-derivative coefficient and `G_eff`, and state
    the region where this holds.
  - Current Status sentence (appH:1860): "Remains Assumption~\ref{ass:EFT-a2}. No computation is recorded."
- **Dependencies:** Problem F (OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL), and through F, D1, C and A.
- **Classification of this package:** PROGRAMME-CONDITIONAL. It is not DERIVED.
- **Critical-path set:** A, B, C, D1, E, F, G-derived and N, re-derived from `sec:ch17-done` and Appendix H. This
  agrees with the gatekeeper's full scan. I found no discrepancy.

## Source reading

**Digest + targeted reads.**
- Digest: `python scripts/make_digest.py --check` printed `DIGEST CURRENT` (chapters-hash d3558e44b583da45,
  dirty-chapters: no). `git status` shows that no chapter files changed since round 1.
- I re-read in full:
  - appH lines 1836-1862 (Problem N entry and Status);
  - ch09 lines 108-128 (Stelle paragraph);
  - the gatekeeper review and my round-1 proposal.
- Labels re-verified by grep, each occurring once: `sec:status-N` (appH:1837), `thm:Geff` (ch08:187),
  `app:seeley-dewitt` (appA:2), `eq:appA-a2` (appA:77), `eq:W-expand` (ch08:131), `eq:W4` (ch09:62),
  `eq:stelle` (ch09:111), `ass:EFT-a2` (ch09:135).
- `Barvinsky` occurs nowhere in `bib/` or `chapters/`.
- Round 1 included a full scan of all 30 chapter files. The gatekeeper also ran a full scan in review r1. This round
  changes only wording of the same status passage, and the chapters are unchanged, so I did not repeat the full scan.
- No file was unreadable.

## Research and reasoning

R1-R3 are unchanged from round 1, and the gatekeeper re-derived them: the basis change, the continuation, the spin
projections, the pole masses, `Upsilon`, and the `2 - gamma_E` constant. Only the points changed in round 2 are restated
below.

### R1'. Flat background and vacuum term (finding 3)

`eq:W-expand` contains the `a_0` vacuum term `rho_Lambda`. For massless sectors this term is nonzero. Expanding about
`eta` requires `eta` to solve the field equations, so the vacuum term must be cancelled (by a counterterm or tuning) or
neglected. The spin projections are quadratic in `h` and are not affected otherwise. This is the same proviso as Ch. 9,
ECG item 2.

### R1''. Continuation (finding 4)

Appendix A fixes `S_E = -i S_L` and the vacuum map. Continuing `R`, `C^2` and `R^2` with no sign change (the
mostly-plus Wick rotation) is an additional convention. The Appendix H "Sector sum" paragraph calls the analogous choice "a
convention to be checked". The ghost/tachyon character depends only on `sign(G_eff W_C)`. That holds because the `R` and
`C^2` terms carry the same prefactor and continue with the same factor, and the gatekeeper confirmed it. The sign of
`c_W` itself (and so `alpha = -2 c_W`), however, does rely on the convention. The Ch. 9 qualifier (item 3) is therefore
worded conditionally.

### R2'. Where the fixed-`L` form applies (finding 1)

The derivative expansion with `s_max = mu^{-2}` is valid only for `|k| <~ mu`.
- From `m_2^2 = -Upsilon LUV^2/L` and `LUV^2/mu^2 = e^L`, we get `|m_2|^2/mu^2 = Upsilon e^L/L`.
- `e^L/L >= e` for `L > 0`, and `e^L/L` grows without bound as `mu/LUV -> 0`. So `|m_2| >> mu` unless `Upsilon` is
  exponentially small in `L`. For `Upsilon = 10`, `|m_2|^2/mu^2 >= 10e ≈ 27`.
- So the fixed-`L` form never reliably places its own pole. The pole location is an artefact of applying that form
  outside its domain.
- The valid fixed-`L` content is the size of the correction at `|k| <~ mu`:
  `32 pi G_eff c_W k^2 = (L/Upsilon) k^2/LUV^2`. This is suppressed by `mu^2/LUV^2` times `L/Upsilon`.

The round-1 "no-go" (milestone trigger 2) rested on the pole location and is withdrawn. A statement that compositeness
alone does not ensure a ghost-free region below `LUV` can only be made inside the model `F`. There it holds in the
following form: `F` has zeros in the disc for `Upsilon < Upsilon_*(delta_W)`, and nothing in the composite construction
excludes that range.

### R4'. Corrected `Upsilon_*` table (finding 7)

On `|x| = 1`, write `x = e^{i theta}` with `theta in [0, pi]`. A zero of `F` there requires
`Upsilon = (delta - i theta) e^{i theta}`.
- **Real-part and imaginary-part conditions:** `delta sin(theta) = theta cos(theta)` and
  `Upsilon = delta cos(theta) + theta sin(theta)`.
- **`0 < delta < 1`:** there is a unique root `theta in (0, pi/2)`, because `tan(theta)/theta` increases from 1 to
  infinity and must equal `1/delta > 1`.
- **`delta < 0`:** there is a unique root in `(pi/2, pi)`.
- **`delta >= 1`:** only `theta = 0`, giving `Upsilon = delta`. This agrees with the gatekeeper.
- **`delta = 0`:** `theta = pi/2` and `Upsilon = pi/2`.

`check_upsilon_star_r2.py` solves these equations to 30 digits. It also counts principal-sheet Lambert zeros inside
`|x| < 1` at `Upsilon_* ± 10^{-3}`, and finds that the count drops to 0 above the threshold in every case.

| `delta_W` | -10 | -6 | -4 | -2 | -1 | 0 | 0.5 | 0.9 | `>= 1` |
|---|---|---|---|---|---|---|---|---|---|
| `Upsilon_*` | 10.402 | 6.586 | 4.755 | 3.040 | 2.262 | pi/2 | 1.268 | 1.051 | `delta_W` |

The `Upsilon = 10` lower edge is `delta_W = -9.58458`. These values agree with the gatekeeper's numbers. The round-1
grid-overshoot values (10.41, 2.27, 1.06) are superseded. The LaTeX uses only `pi/2`, `delta_W` (for `>= 1`), the window
`-9.58 < delta_W < 10`, and `|k^2| ≈ 3.9 LUV^2`. None of these changed.

### Literature (finding 8)

The integration text no longer cites Barvinsky–Vilkovisky. The sentence "At second order in curvature the one-loop action
is nonlocal, with momentum-dependent form factors" is standard. The decay of the Weyl form factor is stated as an
assumption, and the mechanism is illustrated by the potential-insertion form factor, which the scripts verify. Crossref
verified the bibliographic record of Barvinsky & Vilkovisky, NPB 333 (1990) 471, DOI 10.1016/0550-3213(90)90047-H, in
round 1. The decay claim attributed to it remains **not independently verified**.

## Claim classification

| Claim | Class |
|---|---|
| `C^2/R^2/E_GB` decomposition; `c_C = tr I/120`, `c_R = (1/2)tr(1/6-Q)^2` | established identity |
| Spin-2/spin-0 coefficients; residue signs; `m_2^2 = -1/(32 pi G c_W)`, `m_0^2 = 1/(96 pi G c_R)` | established derivation |
| `c_W, c_R, G_eff` from the induced action; `Upsilon = A_1/(2W_C)`; `Upsilon = 10` for minimal scalars | conditional (truncated identity, common limits, `S_E=-iS_L` plus added continuation convention, vacuum term removed, `a_1`-only `G_eff`) |
| Fixed-`L` pole location `|m_2| < LUV` iff `L > Upsilon` | property of the fixed-`L` form only; **not** a one-loop prediction (`|m_2| >> mu`) |
| `(L/Upsilon) k^2/LUV^2` correction at `|k| <~ mu` | conditional (as above) |
| `L -> ln(LUV^2/k^2) + delta_W` for massless sectors | conditional model (decay of Weyl form factor assumed) |
| Lambert zero formula; `Upsilon_*(0) = pi/2`; `Upsilon_*(delta) = delta` for `delta >= 1` | established (within model `F`) |
| `Upsilon_*` table, iff-direction, window `-9.58 < delta_W < 10` | numerical (check, not proof) |
| Absence of zeros in `|k^2| < LUV^2` not implied by compositeness | conditional on model `F` |
| Values of `W_C, A_1, G_eff, delta_W` for the locked block; control at `|k| ~ LUV`; matrix derivation | unresolved |
| Problem N discharged | **not claimed** |

## Proposed changes

### 1. `chapters/appH-microscopic-proofs.tex`: new paragraph in Problem N

Anchor: after the last sentence of the "Missing step" paragraph of `\section{Problem N: control of the effective
expansion}` (appH lines 1856-1857). "and no stronger." occurs once (verified):

```
This is the requirement of item~6 of Chapter~\ref{ch:geometrogenesis}
and no stronger.
```

Insert the following block after this sentence and before `\paragraph{Status.}`. Nothing is removed by this item.

```latex
\paragraph{Induced Weyl term and the extra spin-two pole (conditional; not closure).}
Work in the truncated identity of Theorem~\ref{thm:Geff}, expanded about
a flat background with the vacuum term cancelled or neglected so that
flat space is a solution, with every included sector assigned the common
limits \(\LUV,\mu\), \(\mu\ll\LUV\), with \(S_E=-iS_L\) as in
Appendix~\ref{app:seeley-dewitt}, and with curvature invariants
continued without change of sign (an added convention). Rewrite the
traced \(a_{2,s}\) of~\eqref{eq:appA-a2} in the basis
\(\{C^2,R^2,E_{\mathrm{GB}}\}\), and let
\(\mathcal W_C:=\sum_sw_sc_{C,s}\) and \(\mathcal W_R:=\sum_sw_sc_{R,s}\),
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
If \(G_{\mathrm{eff}}\mathcal W_C>0\), the extra spin-two pole of this
fixed-\(L\) form is a tachyonic ghost, with \(|m_2|<\LUV\) exactly when
\(L>\Upsilon\). If \(1/G_{\mathrm{eff}}\) is taken from the
universal \(a_1\) term alone, \(1/G_{\mathrm{eff}}
=\mathcal A_1(\LUV^2-\mu^2)/(2\pi)\) with
\(\mathcal A_1:=\sum_sw_s\mathcal A_{1,R,s}\), and
\(\Upsilon=\mathcal A_1/(2\mathcal W_C)\) up to \(O(\mu^2/\LUV^2)\),
independent of \(\LUV\). For sectors of minimally coupled real scalars,
\(\mathcal A_1=\mathcal N_0/6\) and \(\mathcal W_C=\mathcal N_0/120\), so
\(\Upsilon=10\) for every \(\mathcal N_0>0\),
\(|m_2|<\LUV\) in this fixed-\(L\) form once \(\LUV/\mu>e^{5}\), and
\(m_0^2=2\LUV^2/L\). Since \(|m_2|^2/\mu^2=\Upsilon e^{L}/L\), which is
much larger than one for \(\mu\ll\LUV\) unless \(\Upsilon\) is
exponentially small, this pole lies at momenta where the fixed-\(L\)
form does not apply (see below); it is a property of that form, not a
one-loop prediction. For \(|k|\lesssim\mu\), where the fixed-\(L\) form
applies, the Weyl correction relative to the Einstein term is
\(32\pi G_{\mathrm{eff}}c_Wk^2=(L/\Upsilon)\,k^2/\LUV^2\).

The fixed-\(L\) form is not the one-loop result at momenta
\(\mu\ll|k|\ll\LUV\). At second order in curvature the one-loop action
is nonlocal, with momentum-dependent form factors; assuming that
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
beyond \(\LUV\) are propagating ghosts. Within the leading-logarithmic
model \(F\), absence of a zero in \(|k^2|<\LUV^2\) is a numerical
condition on \(\Upsilon\) and \(\delta_W\), which are outputs of
Problem~F, and is not implied by the metric being composite.
Problems~F and~N remain open.
```

Notes:
- Labels used (each verified to exist once): `thm:Geff`, `app:seeley-dewitt`, `eq:appA-a2`, `eq:W-expand`, `eq:W4`,
  `eq:stelle`. No new labels are introduced, and there is no `\cite`.
- Macros: only `\LUV` (existing), `\mathcal`, `\operatorname`, `\mathbb`, `\tfrac`. These are the same as in r1, which the
  gatekeeper checked against the preamble usage.
- The new symbols `\mathcal W_C`, `\mathcal W_R`, `\Upsilon`, `\delta_W` are unused elsewhere in `chapters/` (round-1 grep,
  confirmed by the gatekeeper).
- The block is ASCII-only.

### 2. `chapters/appH-microscopic-proofs.tex`: Problem N Status paragraph

Delete only the sentence "No computation is recorded." from appH line 1860. That line occurs once:

```
Remains Assumption~\ref{ass:EFT-a2}. No computation is recorded.
```

becomes

```latex
Remains Assumption~\ref{ass:EFT-a2}.
```

The ledger label (lines 1839-1841) and everything else are unchanged.

### 3. `chapters/ch09-ultraviolet.tex`: Stelle paragraph qualifier (optional, separable; gatekeeper: may integrate)

Anchor: the last sentence of `\paragraph{Stelle quadratic gravity.}` (lines 124-126). Its ending "undetermined here."
occurs once:

```
Whether such a pole lies
within the regime of the metric effective theory is therefore
undetermined here.
```

Append the following after it, in the same paragraph. Nothing is removed.

```latex
These statements take \(\alpha>0\) and \(\beta>0\). For \(\alpha<0\) the
extra spin-2 pole is tachyonic, with residue still opposite to that of
the graviton; Section~\ref{sec:status-N} records that a truncated
induced Weyl term has this sign when \(G_{\mathrm{eff}}\) and the
weighted Weyl trace are positive.
```

This is unchanged from r1. The phrase "a truncated induced Weyl term" points to the conditional setting of item 1, which
now states the added continuation convention explicitly. Label `sec:status-N` was verified (appH:1837).

### Stale passages elsewhere

None.
- Ch. 17 lines 497-513 and 724-728 remain accurate.
- Ch. 16 lines 139-143 (a ghost below `LUV` is a killer) are consistent with this package. The package no longer claims
  that the truncation realizes that killer.
- `ass:EFT-a2` is not edited (see For the author, item 3).

## Verification scripts

All scripts are in `C:\Users\redgi\Projects\namcg-lab\proposals\002-auto-target\`. Run them with `py -3`.

- **`check_spin_projections.py` / `.out.txt`** (r1, unchanged): spin-2/spin-0 coefficients, residue ratios, the Stelle
  mapping, and that the Gauss–Bonnet quadratic form vanishes.
- **`check_induced_pole.py` / `.out.txt`** (r1, unchanged): induced coefficients, `Upsilon = 10`, `m_0^2 = 2LUV^2/L`,
  Lambert zeros, and `2 - gamma_E`.
- **`check_disc_criterion.py` / `.out.txt`** (r1, unchanged): branch selection, monotonicity, argument-principle counts,
  and the `Upsilon = 10` window. Its grid-scan `Upsilon_*` values overshoot by up to 0.01. They are superseded by the
  next script.
- **`check_upsilon_star_r2.py` / `.out.txt`** (new): exact unit-circle crossing `Upsilon_*(delta)` from
  `delta sin(theta) = theta cos(theta)` and `Upsilon = delta cos(theta) + theta sin(theta)`. It counts Lambert zeros in
  `|x| < 1` at `Upsilon_* ± 1e-3`, and gets 2 → 0 for `delta < 1` and 1 → 0 for `delta >= 1`. It also computes the
  `Upsilon = 10` lower edge, `-9.5845785`.

The arithmetic in `|m_2|^2/mu^2 = Upsilon e^L/L >= e Upsilon` is elementary: the minimum of `e^L/L` is at `L = 1`.
No script is needed for it.

## Milestone assessment

**Routine.** I accept the gatekeeper's assessment.
- Trigger 1 does not apply: nothing is derived from the matrix theory.
- Trigger 2 does not apply: the round-1 "no-go" rested on the fixed-`L` pole artefact and is withdrawn.
- Trigger 3 does not apply to this package. The appK sign issue is a non-load-bearing sign inconsistency, which
  `MILESTONE.md` lists as routine, and it is not handled here.
- No label change is proposed.

## Status-label recommendation

The current critical path, from `sec:ch17-done` cross-checked with Appendix H, is A, B, C, D1, E, F, G-derived and N.
All are OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- Affected label: Problem N. **Unchanged.**
- Problem F: **unchanged.**

## Author decision needed

None for integrating items 1-3. The optional and author-only items are listed below.

## For the author (outside the integration text; not part of this package's edits)

1. **Optional bibliography entry (finding 8).** The integration text cites nothing new. If the author wants a source for
   "at second order in curvature the one-loop action is nonlocal", the author may add the entry below to `bib/namcg.bib`.
   The key `Barvinsky1990` is not present (verified).
   - It would be cited by appending `~\cite{Barvinsky1990}` after "momentum-dependent form factors" in item 1.
   - Only the bibliographic record was verified (Crossref). That the paper establishes decay of the Weyl form factor at
     large argument is not independently verified, and the text keeps decay as an assumption.

   ```bibtex
   @article{Barvinsky1990,
     author  = {Barvinsky, A. O. and Vilkovisky, G. A.},
     title   = {Covariant Perturbation Theory ({II}). Second Order in the Curvature. General Algorithms},
     journal = {Nuclear Physics B},
     volume  = {333},
     pages   = {471},
     year    = {1990}
   }
   ```

   This is DOI-free, to match the style of the existing entries. The DOI, if wanted, is
   10.1016/0550-3213(90)90047-H.

2. **appK `a_1` sign (finding 9).** `chapters/appK-endomorphism.tex` line 17 writes `a_1 = tr(E) - (1/6) R dim` for
   `Delta = -D^2 + E`. This has the opposite overall sign to `eq:appA-a1` and `eq:a0a1` (`a_1 = tr(R/6 - E)`), which is
   the standard value for this convention. The conclusion `delta a_1 = 0` is unaffected. This needs a separate one-line
   correction item, and this package does not touch it.

3. **Notation and N target wording (finding 10).** `alpha` is used for several unrelated quantities:
   - the `a_2` prefactor in `eq:W-again-9` / `eq:W-through-2`;
   - the Weyl coefficient of `eq:stelle`;
   - the ECG coupling (ch09:236; appH Problem J);
   - the Fierz–Pauli mass parameter (ch07:79, 423);
   - `nu_exp` (appE:98);
   - the per-galaxy fit parameter (ch17:572, 626).

   As a result, the N target phrase "values of `alpha` and `G_eff` computed in Problem F" (Ch. 17 and appH) is
   ambiguous. Possible author wording choices:
   - (a) restate N's target in terms of `c_W, c_R` of `eq:W4`, or of `Upsilon`;
   - (b) qualify the "`(p/LUV)^2`" wording of `ass:EFT-a2`. The induced truncation gives `(L/Upsilon)(p/LUV)^2` for
     `p <~ mu`, and `(ln(LUV^2/p^2) + delta_W)/Upsilon` times `(p/LUV)^2` in model `F`.

   Neither is proposed here. (b) would change the text of an assumption.

## Remaining open step

To close N one still needs:
- (a) the gauge-fixed locked-block operators and weights (Problem F, which needs D1), giving `W_C` and `G_eff`, hence
  `Upsilon`, including ghost and non-scalar sectors;
- (b) `delta_W` in a stated scheme, including the finite Weyl counterterm;
- (c) massive-sector threshold functions;
- (d) control of the two-point function at `|k| ~ LUV`, beyond the leading-log model `F`;
- (e) all of this from the matrix path integral (Problem A dictionary);
- (f) whether the vacuum-term cancellation and the curvature-invariant continuation convention are realized.

## Special instructions for the gatekeeper

- **Diff to check against your snippet.**
  - The opening sentence matches your text verbatim.
  - The replacement for the end of paragraph 1 matches your text, except that "\(\gg1\)" became "much larger than one for
    \(\mu\ll\LUV\) unless \(\Upsilon\) is exponentially small". Reason: `Upsilon e^L/L >= e Upsilon` holds for all
    `L > 0`, and `>> 1` needs `Upsilon` not exponentially small.
  - I also scoped the preceding sentence ("tachyonic ghost, with `|m_2| < LUV` exactly when `L > Upsilon`") to "this
    fixed-\(L\) form".
  - The closing sentences match your text.
  - The Status edit is a deletion only.
  - `\cite{Barvinsky1990}` is replaced by an uncited sentence.
- **Must not be asserted:** a no-go; that the truncation places a ghost below `LUV`; that N or F is closed; that
  `Upsilon = 10` holds for the locked block.
- **Re-run** `check_upsilon_star_r2.py` for finding 7.
- **Build:** no LaTeX build was run by the researcher. Run `python scripts/build_check.py` at integration.
