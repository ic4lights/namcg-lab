# Proposal 067-n-positivity-remainder-sublemma, round 1

## Result

Two bounded conditional results for Problem N, plus one named-class obstruction; nothing is closed.

1. **Spectral-positivity sublemma (conditional).** If the matrix dynamics admits a
   self-adjoint Hamiltonian bounded below with a normalizable ground state and a
   self-adjoint composite spin-two operator `T_{mu nu}` in the fluctuation class, then
   the spectral decomposition makes the vacuum two-point function of `T_{mu nu}` a
   positive-moment integral and the residue at any isolated simple **real** pole of its
   spin-two projection a sum of squared matrix elements, hence non-negative: the exact
   correlator has no negative-residue real pole at any energy. I record the exact
   hypothesis class and why it is **not** available here: the Hamiltonian hypothesis is
   the content of `ass:lorentzian`; the Euclidean route is blocked by the recorded
   Osterwalder-Schrader failures (Section `sec:status-E`: failure on the invariant
   polynomial algebra at finite N; Section `sec:status-D`: tree-level reflected form
   negative on gauge-invariant translation probes at the Euclidean flat point); neither
   `T_{mu nu}` nor the fluctuation class is derived (Problem D). I also show the sublemma
   would not by itself discharge `ass:EFT-a2`: the recorded pole statements of the
   Problem N block concern **truncated** kernels. A two-oscillator quantum-mechanical
   model with an exactly positive spectrum exhibits precisely this artifact: the exact
   two-point function has positive residues at both normal modes (sum rule = 1), while
   the O(s^2) truncation of the same kernel develops one real negative-residue pole,
   provably located **above** the truncation's own expansion scale.
2. **Named completion class + bounded obstruction (R2).** The generic caveat
   "conditional on the truncated identity" can be sharpened to a named class: the
   leading-logarithmic `F` is the second-order curvature kernel of a
   Barvinsky-Vilkovisky-class heat-kernel expansion (`BarvinskyVilkovisky1990`, DOI
   verified this run); about a flat background the second-order kernel is the only part
   contributing to the two-point function, and a completion fixing the computed
   logarithm enters **additively**, `F -> F + R`, `R(x) = (x/Upsilon) r(x)`, `r(0) = 0`
   (massless threshold). Every analytic O(x) completion reparametrizes `delta_W`
   (exact identity `F(x;delta_W) + eps*x = F(x;delta_W - Upsilon*eps)`, sympy residual
   0). **The unconditional R2 target is FALSE**: a completion `-c x^2` carries no
   logarithm, leaves the O(p^4) log coefficient and `delta_W` unchanged, and for `c > 1`
   puts a zero at `0 < x < 1` (at `Upsilon = 10, delta_W = 0`; zero at `x = 0.9088995776`
   for `c = 1.2`). This is a bounded no-go for any stability theorem that constrains
   completions only through the logarithmic coefficient. The honest replacement is a
   quantitative conditional sublemma (Rouche/argument-principle on the **slit disc**
   `{|x|<1} \ (-inf,0]`, needed because `F` is not analytic at 0): with
   `m(Upsilon,delta_W)` = min |F| on the slit-disc boundary — computed `m(10,0) =
   0.82202509` (circle part, attained at `|x| = 1`, `theta = 1.954`; cut-side min
   1.0002074) — if `sup|R|` on the same boundary is below `m`, then `F + R` and `F`
   have the same number of zeros in the slit disc, so in the recorded parameter region
   `F + R` has no zero with `|x| < 1`. Establishing the bound on `R` requires the
   spectral data of the computed form factors — an input of Problem F. The manuscript
   caveat is updated so the zero-location claims are explicitly conditional on such a
   bound.

Problem N remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. All numbers re-derived
from the repository's own `F`; none copied.

## Target and status

- **Problem N** (`chapters/appH-microscopic-proofs.tex` L3350-3355, verbatim):
  "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label.
  Completion: PROGRAMME-CONDITIONAL." Unchanged by this proposal.
- **Original target** (appH "Missing step.", L3365-3367): "Derive from the matrix path
  integral that the graviton two-point function has no propagating Ostrogradsky ghost
  for `p < Lambda_UV`, for the values of `alpha` and `G_eff` computed in Problem F."
- **Chapter 17 criterion** (`chapters/ch17-agenda.tex` L658-660, item 4 of the
  matrix-derived completion enumeration): "Problem N: using the `alpha` and
  `G_eff` of Problem F, control the effective expansion and exclude propagating
  Ostrogradsky ghosts for `p < Lambda_UV`."
- **Dependencies:** the N.1 ghost test at physical parameters is blocked on Problem F
  (`alpha`, `G_eff`); I verified proposal 064 delivered only the q=0 fibre-level trace
  response, **not** `G_eff` or `alpha`, so the F-dependency assertion is safe. The
  positivity route additionally depends on `ass:lorentzian` and on Problems E/D.
- **Classification of this contribution:** conditional sublemma + bounded named-class
  obstruction. It does not make the step DERIVED (the hypothesis class of both results
  is not established, and the region inputs are F-conditional). It is
  PROGRAMME-CONDITIONAL evidence inside the still-open problem.

## Source reading

digest + targeted reads. Flag: `scripts/make_digest.py --check` reported DIGEST STALE
(HEAD moved; integrations 062-066 are uncommitted in the working tree; `scratch/` is
off-limits to me so I could not regenerate). I proceeded against the
orchestrator-certified working tree and re-verified the certification myself:
`appH` = 592,220 B, sha256 `de48d55754b7e91b034dd4fc76bc4d8ad01a7d527280fa7d34a62c2774eb819b`,
CRLF 3489, bare LF 0 — matches. Files read in full: `chapters/appH-microscopic-proofs.tex`
(Problem N block L3350-3481, Problem D/E passages L1530-1551 and ledger headers),
`chapters/ch09-ultraviolet.tex` (ass:EFT-a2 L140-145, Stelle passage L120-132,
forbidden-questions list L169-177), `chapters/ch17-agenda.tex` (criterion enumeration
L649-670, Problem N paragraph L497 ff), `bib/namcg.bib` (Barvinsky, OS entries),
`proposals/064-*` (deliverable audit), `reports/sme-scout-20261109-1854.md`.
Unreadable files: none.

## Research and reasoning

### A. Re-derivation of the existing Problem N block (independent check)

`F(x) = 1 - (x/Upsilon)(Log(1/x) + delta_W)`, `x = k^2/Lambda_UV^2`, principal Log.
Put `t = Log(1/x)`: `F = 0 <=> (t + delta) e^{-(t+delta)} = Upsilon e^{-delta}
<=> -(t+delta) = W_j(-Upsilon e^{-delta})`, and using `e^W = W/a` with
`a = -Upsilon e^{-delta}` gives `x_j = -Upsilon / W_j(-Upsilon e^{-delta})`. The
**principal-sheet** condition is that `x_j` satisfy `F(x_j) = 0` with the *principal*
Log; enumerating branches `j in [-6,6]` and testing this at `(Upsilon,delta) = (10,0)`
leaves only `j in {0,-1}`, `x = -2.12160672801 +/- 3.31438991652 i`,
`|x| = 3.9352758` — the text's "complex-conjugate pair with
`|k^2| approx 3.9 Lambda_UV^2`" (appH L3463) is confirmed.

Crossing system on `|x| = 1`, `x = e^{i theta}`, `theta in (0,pi)`:
`delta sin(theta) = theta cos(theta)` and `Upsilon = delta cos(theta) + theta sin(theta)`.
For `delta < 1`: `theta*` solves `delta = theta cot(theta)`, `Upsilon_* = theta*/sin(theta*)`;
`Upsilon_*(0) = pi/2 = 1.57079632679` (text: 1.57); `Upsilon_*(0.5) = 1.268279495`;
`Upsilon_*(0.99) = 1.005007497`. For `delta >= 1` the only crossing is `x = 1`, giving
`Upsilon_* = delta` (verified at `delta in {1,2,5,20}`); the pinch is real: at
`delta = 2`, `Upsilon = 1.97` gives min |zero| 0.9704 (inside), `Upsilon = 2.03` gives
1.0305 (outside). At `Upsilon = 10` the circle crossing `theta* = 2.85234189445` gives
`delta_min(10) = -9.584578536`, confirming the window `-9.58 < delta_W < 10`
(text L3461-3463). Eleven `(Upsilon, delta)` region comparisons (zeros in `|x| < 1`
vs `Upsilon > Upsilon_*(delta)`) are all consistent (`check_f_zeros.py`).

### B. R1: the Kallen-Lehmann-type sublemma and its bounded obstruction

*Statement (conditional).* Let `H` be self-adjoint, bounded below, with normalizable
ground state `Omega`; let `T_{mu nu}` be self-adjoint. Then
`<Omega| T_{mu nu}(t) T_{rho sigma}(0) |Omega> = sum_n e^{-i(E_n - E_0)t}
<Omega|T_{mu nu}|n><n|T_{rho sigma}|Omega>` (spectral resolution of `H`; at finite N
the matrix model's spectrum is discrete, so the measure is a positive sum of point
masses). The residue at any isolated simple real pole of the spin-two-projected
two-point function is a sum of squared matrix elements and is non-negative. Hence the
**exact** correlator has no negative-residue real pole at any energy.

*Obstruction (bounded by its hypothesis class).* The hypotheses are exactly what the
ledger records as missing: a self-adjoint `H` bounded below with a normalizable ground
state is `ass:lorentzian` (ch04 L322); the Euclidean substitute fails — Section
`sec:status-E` records OS reflection positivity failing on the invariant polynomial
algebra at finite N, and Section `sec:status-D` records the tree-level reflected form
at the Euclidean flat point negative on gauge-invariant translation probes; and neither
the fluctuation class nor `T_{mu nu}` is derived (Problem D). So the positivity
representation is **unavailable in the current hypothesis class** — that is the honest
R1 outcome, named and pinned to existing ledger entries rather than asserted as a
theorem.

*Why positivity would not close N even if granted (derived).* N's recorded pole
statements are properties of truncated kernels, so positivity of the exact correlator
does not reach them. The two-oscillator model makes this explicit and is itself fully
derived (`toy_ghost_truncation.py`): with `M^2 = [[mx2,g],[g,my2]]`,
`D_xx(s) = (s - my2)/det(s - M^2)` has residues `(mx2 - my2 +/- Delta)/(2 Delta)` at
`lambda_±`, both positive since `Delta^2 - (mx2-my2)^2 = 4g^2 > 0`, with sum rule
`r_+ + r_- = 1`. The exact kernel `Gamma(s) = s - mx2 - g^2/(s - my2)` expanded in
`s/my2` (valid `|s| < my2`) and truncated at O(s^2) has exactly one negative root
(`c/a < 0` when `mx2 > g^2/my2`) and `Gamma_2'(s*) = a (s* - s_p) < 0` (symbolic
residual 0) gives a **negative residue**, while
`|s*| = (b + sqrt(D))/(2a) > b/a` and `b/a - my2 = my2^3/g^2 > 0` put it **above the
expansion scale**. Numeric instance (`my2 = 100, mx2 = 1, g = 1`):
`s* = -1000100.98990` residue `-0.999898030599`; `s_p = 0.989900030095` residue
`+0.999898030599`; exact poles `100.010099980` (r `0.000102`) and `0.989900020299`
(r `0.999898`); the exact kernel has no pole anywhere near `s*`.
This mirrors the structure of the fixed-L tachyonic-pole statement: a
negative-residue real pole of a truncation, sitting above the truncation's scale.

### C. R2: the named class, the counterexample, and the remainder bound

*Structure (conditional on the BV expansion being the completion framework).* The
leading-log `F` is the second-order curvature kernel of the covariant perturbation
expansion of `BarvinskyVilkovisky1990`; about a flat background, curvature-cubic and
higher terms of the action contribute at O(h^3) and higher, so the second-order kernel
is the only part contributing to the two-point function. A completion that fixes the
computed O(p^4) logarithm therefore changes the two-point kernel additively by a
remainder `R(x) = (x/Upsilon) r(x)` with `r(0) = 0` (massless threshold: no local
mass-term shift). This is the *induced-vertex-correction* reading of "form factors" —
it never dresses a fundamental propagator, in compliance with `ass:EFT-a2` and ch09's
forbidden questions.

*Identity (established).* `F(x;delta_W) + eps*x = F(x; delta_W - Upsilon*eps)` —
sympy residual 0 (the opposite sign gives residual `2 eps x`, caught in development).
So every analytic O(x) completion is a reparametrization of `delta_W`: the sense in
which finite local terms are absorbed is exact and small.

*Bounded no-go (established, numerically, at the locked point).* No stability statement
can rest on the logarithmic coefficient alone: `G = F - c x^2` has no logarithm, so
the O(p^4) log coefficient and `delta_W` are unchanged, yet at `(Upsilon, delta_W) =
(10, 0)` the threshold for a zero in `(0,1)` is `c* = inf_{(0,1)} F(x)/x^2 = 1`
(attained at the endpoint `x = 1`; `d/dx (F/x^2) < 0` verified on a grid; existence for
`c > 1` by the intermediate value theorem since `G(0+) = 1 > 0`, `G(1) = 1 - c < 0`).
At `c = 1.2` the zero is at `x = 0.9088995776` and a dense-seed Newton count finds
**three** zeros in the slit disc (that real zero plus a conjugate pair
`-0.9078874341 +/- 0.1256711648 i`, `|x| = 0.91654396`) — the completion destabilizes
the disc beyond the single crossing. So the R2 target as literally posed ("completions
fixing the O(p^4) log coefficient cannot move the first zero below the stated scale")
is **false** for the named class, unconditionally.

*Positive replacement (conditional sublemma, standard theorem + computed margin).*
Because `F` has a logarithmic branch point at `0` (inside the unit disc), an ordinary
disc Rouche hypothesis is not well posed; the correct domain is the slit disc
`D = {|x| < 1} \ (-inf, 0]`, on which `F` and `R` are analytic, continuous to both
sides of the cut, and (for `R` as above) `|F| -> 1`, `|R| -> 0` near `0`, so the
keyhole boundary is controlled at the small circle. If
`sup_{partial D} |R| < m(Upsilon, delta_W) := min_{partial D} |F|`, then by the
argument principle `F + R` has the same number of zeros in `D` as `F`, namely zero in
the recorded region. Computed margins: `m(10,0) = 0.82202509` (circle part, attained
at `|x| = 1`, `theta = 1.9540706`; cut-side min `1.0002074`); `m(2,0) = 0.1882287`;
`m(3,2) = 0.33333333`; `m(pi/2, 0) ~ 1.7e-8` (vanishing at the region crossing, as it
must). Cross-check: `c = 0.5 < m` gives 0 zeros (condition holds); `c = 1.2` violates
the bound and produces zeros. The open sub-lemma is then precisely: bound
`sup |R|` on the slit-disc boundary from the spectral data of the computed form
factors — a Problem F input.

### D. R4/R6: context and the N.1 dependency audit

Proposal 064 audit: 064 computed the q = 0 fibre-level trace response only; it did not
produce `G_eff` or `alpha`. The N-block sentence tying the ghost-mass regime to
Problem F inputs is therefore current: the N.1 physical-parameter ghost test is
F-blocked. Closest published matrix-model analogues (the Steinacker noncommutative
matrix-model programme, keys present in `bib/`) state one-loop effective actions and
no-ghost results for other backgrounds/sectors; none states a pole or positivity
theorem for a composite-graviton two-point function of this type. These literature
items were consulted at metadata level only and are **not independently verified** in
this run; they are deliberately not cited in the manuscript text.

## Claim classification

| claim | class |
|---|---|
| Lambert-W zero formula; principal-sheet branch filter; `Upsilon_*(0)=pi/2`; `Upsilon_*=delta` for `delta>=1`; window `-9.58 < delta_W < 10` at `Upsilon=10`; `|x_zero|=3.9352758` | established derivation + verified numerics (re-derivation of existing block, `check_f_zeros.py`) |
| KL-type sublemma (positive measure, non-negative real-pole residues) | conditional result (standard spectral theorem; conditional structure is the contribution) |
| hypothesis class unavailable (`ass:lorentzian`; E/D OS failures; `T_{mu nu}` not derived) | ledger-recorded bounded no-gos (established within the repository), quoted |
| two-oscillator: exact residues > 0, sum rule 1; truncation pole negative residue; `|s*| > my2` | established (symbolic identities + proofs displayed alongside; `toy_ghost_truncation.py`) |
| `F` is the second-order BV kernel; completions enter additively, `R=(x/Upsilon)r(x)`, `r(0)=0` | conditional result (standard heat-kernel structure; conditional on the BV class being the completion framework) |
| `F(x;delta)+eps x = F(x;delta-Upsilon eps)` | established identity (sympy residual 0) |
| `-c x^2` counterexample, `c*=1`, zero at `x=0.9089` (c=1.2), 3 zeros in slit disc | established numerically at the locked point (`remainder_rouche.py`) |
| slit-disc Rouche sublemma with margin `m(10,0)=0.82202509` | conditional result (argument principle on the keyhole domain; margin verified numerically) |
| bound on `R` from form-factor spectral data | unresolved (input of Problem F) |
| N.1 physical ghost test F-blocked; 064 gave only q=0 fibre response | established by audit of 064 |
| Steinacker-analogue context | not independently verified (metadata level); not used in manuscript |

## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`, Problem N block. No other file, no
bib addition (all cited keys already exist in `bib/namcg.bib`, one occurrence each —
verified by `verify_manifest.py`).

**Hunk 1 — insertion.** Anchor: between the end of the zero-location paragraph and the
start of the caveat paragraph. Boundary quote (occurs exactly once, marker verified):
`are a complex-conjugate pair with \(|k^2|\approx3.9\LUV^2\).` (L3463, last line of the
zeros paragraph) and the next paragraph's first line `These statements are conditional
on the truncated identity, the` (L3465). Insert the two paragraphs below (the exact
content of `insert-r1.tex`, LF-only in the folder; the integrator writes CRLF). The
anchor is not on any `\paragraph{Missing step.}` line (9 occurrences untouched).

```latex
\paragraph{Spectral positivity of the exact correlator.}
Suppose the matrix dynamics admits a self-adjoint Hamiltonian \(H\)
bounded below with a normalizable ground state \(\Omega\), and let
\(T_{\mu\nu}\) be a self-adjoint composite rank-two operator, the
fluctuation of the composite metric to which the external metric
couples through the dictionary. Then
\(\langle\Omega|T_{\mu\nu}(t)\,T_{\rho\sigma}(0)|\Omega\rangle
=\sum_n e^{-\mathrm i(E_n-E_0)t}
\langle\Omega|T_{\mu\nu}|n\rangle\langle n|T_{\rho\sigma}|\Omega
\rangle\) over the spectral resolution of \(H\): the measure is
positive and carried by squared matrix elements, and the residue at
any isolated simple real pole of the spin-two-projected two-point
function is a sum of squared matrix elements and so non-negative.
Under these hypotheses the exact composite spin-two two-point
function has no negative-residue real pole at any energy; the extra
pole of the fixed-\(L\) form and of the leading-logarithmic \(F\)
above is a property of those truncated kernels. These hypotheses
are not established in the present hypothesis class: a self-adjoint
Hamiltonian bounded below with a normalizable ground state is the
content of Assumption~\ref{ass:lorentzian}; the Euclidean measures
of Section~\ref{sec:status-E} fail the positivity of
\cite{OsterwalderSchrader1973,OsterwalderSchrader1975} on the
invariant polynomial algebra at finite \(N\), and the tree-level
reflected form at the Euclidean flat point of
Section~\ref{sec:status-D} is negative on the gauge-invariant
translation probes; neither the fluctuation class nor \(T_{\mu\nu}\)
is derived (Problem~D). Even under the hypotheses the sublemma
would not by itself discharge Assumption~\ref{ass:EFT-a2}: it
constrains the exact kernel, whereas the pole statements of this
section concern computed truncations whose remainder is not bounded
near the would-be pole. A two-oscillator quantum-mechanical model
with two positive-norm modes exhibits the artifact: the exact
two-point function of the observed mode has positive residues at
both normal modes, while the quadratic truncation of the same
kernel acquires one real negative-residue pole, located above the
scale of the truncation.

\paragraph{The named completion class and the remainder bound.}
The leading-logarithmic \(F\) is the second-order curvature kernel
of a Barvinsky--Vilkovisky-class heat-kernel expansion
\cite{BarvinskyVilkovisky1990}: about a flat background the
second-order kernel is the only part of that expansion that
contributes to the two-point function, and a completion that fixes
the computed logarithm enters additively,
\(F(x)\mapsto F(x)+R(x)\), with \(R(x)=(x/\Upsilon)r(x)\) and
\(r(0)=0\) in the massless case. Every analytic \(O(x)\) completion
reparametrizes \(\delta_W\), since
\(F(x;\delta_W)+\varepsilon x=F(x;\delta_W-\Upsilon\varepsilon)\);
this is the sense in which finite local terms are absorbed. No
stability statement for the zero-free disc can rest on the
logarithmic coefficient alone: at \(\Upsilon=10\) and
\(\delta_W=0\), the completion \(-c\,x^{2}\) carries no logarithm,
so the \(O(p^4)\) logarithmic coefficient and \(\delta_W\) are
unchanged, and for \(c>1\) it places a zero at \(0<x<1\)
(\(x\approx0.909\) at \(c=1.2\)). What is available is
conditional: with \(m(\Upsilon,\delta_W)\) the minimum of \(|F|\)
over the boundary of the slit disc
\(\{|x|<1\}\setminus(-\infty,0]\) (at \(\Upsilon=10\) and
\(\delta_W=0\), \(m=0.82\), attained at \(|x|=1\)), if
\(\sup|R|\) over the same boundary is below
\(m(\Upsilon,\delta_W)\), then \(F+R\) and \(F\) have the same
number of zeros in the slit disc, so within the parameter region
recorded above \(F+R\) has no zero with \(|x|<1\). The bound on
\(R\) requires the spectral data of the computed form factors on
the unit circle and is not established; it is an input of
Problem~F.
```

What is kept: everything else in the Problem N block, in particular the ledger
paragraph, the "Missing step." paragraph, the zeros paragraph, the sentence
`...and is not implied by the metric being composite.` and the block closer
`Problems~F and~N remain open.` (both occurrence count 1 after the insert — they are
not adjacent to the insertion site and are untouched), and the `\paragraph{Status.}`
line `Remains Assumption~\ref{ass:EFT-a2}.` (count 1).

**Hunk 2 — caveat first-sentence replacement (5 source lines -> 7).** Inside the
caveat paragraph, replace exactly:

    These statements are conditional on the truncated identity, the
    continuation and common limits stated, massless sectors (massive
    sectors require the threshold functions of Problem~F), and the use of
    the leading-logarithmic form factor up to \(|k^2|\sim\LUV^2\), where
    the derivative expansion is not controlled.

with

    These statements are conditional on the truncated identity or, for
    the zero-location statements, on the remainder bound of the preceding
    paragraph, on the continuation and common limits stated, on massless
    sectors (massive sectors require the threshold functions of Problem~F),
    and on the use of the leading-logarithmic form factor up to
    \(|k^2|\sim\LUV^2\), where the derivative expansion is not
    controlled.

All sentences after this one ("They do not compute \(\mathcal W_C\) ..." etc.) are
kept verbatim. Reason: once the inserted paragraph makes the zero-free-disc claim rest
on a remainder bound, the caveat must name that condition; this is the smallest
accurate edit. Old string occurrence count 1 (verified).

Labels/keys verified (occurrences in the working tree): `\ref` targets
`ass:lorentzian` (ch04), `sec:status-D`, `sec:status-E` (appH), `ass:EFT-a2` (ch09) —
each defined exactly once in `chapters/*.tex`; cite keys
`BarvinskyVilkovisky1990`, `OsterwalderSchrader1973`, `OsterwalderSchrader1975` — one
bib entry each. The insert adds no new `\label`. No stale passages elsewhere: the
ch09 ass:EFT-a2 passage and the ch17 item-4 text remain accurate; nothing contradicts
the insert.

**Predicted post-states** (`simulate_apply.py`, marker-anchored, read-only):
`appH` current 592,220 B / `de48d557...` / CRLF 3489 / bare LF 0; predicted
596,247 B / sha256
`85b93bf86f527ee195d40a4cd828b6138a9dda385729b8c5dc9a80b04f2c4ea3` /
CRLF 3559 / bare LF 0; head-before-insertion byte-identical: True; tail-after-replaced-
caveat byte-identical: True. `bib/namcg.bib` unchanged (no new keys).

## Verification scripts

All under `proposals/067-n-positivity-remainder-sublemma/`, run with `python -I`;
each `.out` reproduces byte-identically (re-verified after the final insert edit).

- `check_f_zeros.py` / `.out` — zero formula derivation, principal-sheet branch
  filter, region comparisons vs the crossing system, pinch at x=1 (dps 40).
- `toy_ghost_truncation.py` / `.out` — exact positive residues + sum rule; truncated
  kernel's negative-residue pole above the expansion scale; numeric instance.
- `remainder_rouche.py` / `.out` — delta-shift identity; counterexample threshold
  `c* = 1`; slit-disc margins `m(...)`; direct zero counts at `c = 0.5, 1.2`.
- `simulate_apply.py` / `.out` — predicted post-integration appH bytes (see above).
- `verify_manifest.py` / `.out` — cite keys, label uniqueness, marker counts, closer
  sentences intact, no new labels. (Note: an earlier inline heredoc check gave false
  zeros `marker_a 0`, `closer2 0`; this file-based script gives counts 1 for
  `marker_a`, `old_c`, the closers, and `Remains Assumption~\ref{ass:EFT-a2}` —
  the heredoc result was a quoting artifact; trust the written script.)
- `insert-r1.tex` — the manuscript text (LF-only; integrator converts to CRLF).
- `captures/barvinsky_vilkovisky_1990_crossref.json` — Crossref bibliographic query
  capture (see citation table).

## Citation table

| key | source | verification |
|---|---|---|
| `BarvinskyVilkovisky1990` | Nucl. Phys. B 333, 471-511 (1990), "Covariant perturbation theory (II). Second order in the curvature. General algorithms", DOI 10.1016/0550-3213(90)90047-H | verified this run via Crossref bibliographic-string query (never by guessed DOI); capture saved in `captures/`; matches the existing bib entry field-for-field. Discrepancy noted: the scout report said the bib entry lacked a DOI; the working tree has it (bib L158-166) — working tree wins. |
| `OsterwalderSchrader1973`, `OsterwalderSchrader1975` | existing bib entries, already cited in the existing Problem D block | bib keys exist (1 occurrence each); DOIs not re-verified this run (existing manuscript citations, not new entries). |
| Steinacker-programme items, Figueras-Held-Kovacs 2407.08775, Li-Vaman 2512.06132 | consulted via scout report | **not independently verified**; used as context only, not cited in any proposed text. |

No `bib_additions.bib`: no new entries are needed.

## Decisions Taken

1. **Two paragraphs, one file.** R1 (positivity) and R2 (remainder) have disjoint
   hypothesis classes and must be scoped separately; merging them would blur the
   conditional structure. Kept in one contiguous block because they jointly re-scope
   the same caveat.
2. **Finite-volume spectral form, not Wightman axioms.** The matrix model at finite N
   has a discrete spectrum; the Hamiltonian spectral decomposition states the sublemma
   without assuming Poincare covariance or a Wightman framework (which would smuggle
   in emergent-spacetime input the sublemma is supposed to condition on).
3. **BV class as additive remainder to the second-order kernel**, never a dressed
   fundamental propagator — required by `ass:EFT-a2` and the ch09 forbidden list.
4. **R2 recorded as a bounded no-go + conditional replacement**, not as the requested
   unconditional theorem: the `-c x^2` completion falsifies the literal R2 target. The
   bounded no-go is stated with its exact hypothesis class (completions constrained
   only through the O(p^4) logarithmic coefficient).
5. **Slit disc (keyhole) instead of unit disc for the Rouche statement**: `F` has a
   branch point at `x = 0` inside the disc, so the disc version is not well posed; the
   keyhole domain also controls the small circle (`|F| -> 1`, `|R| -> 0`).
6. **delta-shift sign `delta_W - Upsilon*eps`** (identity residual 0; the opposite
   sign leaves residual `2 eps x`).
7. **Threshold `c* = inf_{(0,1)} F/x^2 = 1`** (the `sup` scan diverges at `x -> 0`;
   the monotonicity of `F/x^2` was checked).
8. **No new bib keys**: `BarvinskyVilkovisky1990` already exists with the verified
   DOI; capture saved only for provenance.
9. **Literature context (R4/R6) kept out of the manuscript text** — minimal insertion;
   the metadata-level-only items must not be cited before independent verification.
10. **Toy model in one manuscript sentence**, full structure in the script: it is a
    demonstrated artifact mechanism, not a model of NAMCG.
11. **Anchor choice**: insertion site marker is the unique zeros-paragraph/caveat
    boundary, never a `Missing step.` line (9 occurrences, all untouched).

## Milestone assessment

Routine. No MILESTONE.md trigger fires: no critical-path step is closed; the package
is a conditional sublemma plus a bounded named-class obstruction plus a precisely
recorded open sub-lemma (the bound on `R`). Problem N remains OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL.

## Status-label recommendation

Re-derived critical-path set from the current manuscript: the Chapter 17 completion
enumeration (`ch17-agenda.tex` L649-666) orders D1, C, F, N, B, G; A and E "are not
placed in this sequence" but remain CRITICAL PATH premises (L668-669); the ledger
snapshot remains A, B, C, D1, E, F, G-derived, N. Affected labels: **none**. I propose
no status, priority or completion-class change; the proposal text asserts no closure.

## Author decision needed

none.

## Remaining open step

To reach the original N target (ch17 item 4) all of the following remain:
1. **The remainder bound**: `sup |R|` on the slit-disc boundary bounded below
   `m(Upsilon, delta_W)` for the locked region — requires the computed form factors
   (Problem F spectral data); without it the `-c x^2`-type completions remain live.
2. **The positivity hypothesis class**: a self-adjoint `H` bounded below with a
   normalizable ground state and a derived self-adjoint `T_{mu nu}` in the fluctuation
   class — i.e. progress on `ass:lorentzian`, Problem E and Problem D.
3. **Physical parameters**: `alpha` and `G_eff` from Problem F for the N.1 ghost test.

Open avenues (forks from the two bounded obstructions, ranked):
(a) Problem F spectral data -> bound `R` (most direct; F is already on the critical
path; would give conditional zero-free-disc stability under all named-class
completions, still not DERIVED N because the region inputs stay F-conditional).
(b) Relax the Euclidean hypothesis: the E no-go is OS/reflection-positivity-specific
on the invariant polynomial algebra at finite N; it does not touch Hamiltonian
positivity for the finite-N quantum-mechanical model, which is exactly `ass:lorentzian`
— a within-core route for the R1 hypotheses.
(c) Other field content (fermions, gauge sectors) changes `Upsilon` and `delta_W` and
the size of `m`; a region with larger margin makes (a) easier — F input.
(d) Loop terms beyond one-loop inside `R`; the bound must include them.
(e) Ghost analysis through the Hamiltonian/Ostrogradsky counting at physical
parameters instead of `F`-zero locations — the N.1 route, F-blocked.
(f) Edge-mode / contact-term contributions to `T_{mu nu}` (affects the positivity
hypotheses; speculative).
Spacetime-emergence constraint respected throughout: no route postulates a fundamental
metric; the spectral sublemma is stated in the microscopic theory's Hilbert space.

## Special instructions for the gatekeeper

- Run all scripts with `python -I` from the repository root; all three math `.out`s
  and `simulate_apply.out` reproduce byte-identically (verified after the final insert
  edit). Predicted post-integration appH: 596,247 B, sha256
  `85b93bf86f527ee195d40a4cd828b6138a9dda385729b8c5dc9a80b04f2c4ea3`, CRLF 3559,
  bare LF 0; re-run `simulate_apply.py` and `verify_manifest.py` to confirm.
- Re-derive two things by hand: (i) the principal-sheet condition at (10,0) keeps only
  `j in {0,-1}` and `|x| = 3.9352758`; (ii) `m(10,0) = 0.82202509` is circle-dominated
  (cut-side min 1.0002074) and the keyhole-domain analyticity claim (F analytic on the
  slit disc, continuous to both cut sides, `|F| -> 1` at the small circle,
  `|R| -> 0` there because `R = (x/Upsilon) r(x)` with `r(0) = 0`).
- Check the counterexample reading: the claim is about the number of zeros of `F + R`
  in the slit disc, not about the principal-sheet zero locations elsewhere; at
  `c = 1.2` the direct count finds 3 (not 1).
- Must not be asserted: that the positivity paragraph discharges N or `ass:EFT-a2`
  (it states hypotheses and an obstruction); that the remainder bound holds (it is a
  conditional with an open input); that the toy models NAMCG; that the exact correlator
  exists as a constructed object here.
- Anchors: `marker_a` and `old_c` occur exactly once; the two closers
  ("is not implied by the metric being composite." / "Problems~F and~N remain open.")
  and `Remains Assumption~\ref{ass:EFT-a2}.` occur exactly once each and are outside
  the edited spans; the 9 `Missing step.` paragraphs are untouched.
- Digest is STALE (uncommitted integrations 062-066): verify against the working tree,
  whose appH hash you should match to `de48d557...` before applying.
- Earlier inline-heredoc counts of 0 for `marker_a` and the EFT-a2 closer were quoting
  artifacts; the written `verify_manifest.py` is authoritative.
