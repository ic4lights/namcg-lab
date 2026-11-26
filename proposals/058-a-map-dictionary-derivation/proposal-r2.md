# Proposal 058-a-map-dictionary-derivation, round 2

Round 1 verdict: ACCEPT WITH REQUIRED REVISIONS (review-r1.md). This round applies all
six findings; the mathematics of r1 is otherwise unchanged. The three r1 scripts are
byte-identical and reproduce exactly (gatekeeper: MOYAL/TORUS/ASSOC MATCH); a fourth
script is added to lock F1. No manuscript edits, no bib changes, no label changes, no
new labels.

## Result

Within the flat Abelian constant-Θ Moyal class the A.map data are pinned exactly and the
per-order-in-Θ error is made explicit (unchanged from r1):

1. Exact plane Weyl data and pairing Tr W_Θ(f)W_Θ(g) = (2π)^{-2}|Pf Θ|^{-1}∫fg, matching
   the trace density of Remark rem:ch3-trace-quadratic and the |Pf θ|^{-1} density of
   Definition def:matrix-coords-ext.
2. Exact finite-N 't Hooft-torus Weyl data (Weyl ordering β = −(θ/2)mn): product law
   [Ŵ_v,Ŵ_w] = 2i sin((θ/2)σ(v,w))Ŵ_{v+w}, pairing Tr Ŵ(f)Ŵ(g) = N Σ f̂_v ĝ_{−v}, and the
   operator-norm remainder bound ‖R‖ ≤ Σ|f̂_v||ĝ_w|(θ|σ(v,w)|)³/24 for mode-limited
   symbols with 2M < N, uniform in N; continuum limit N→∞ at fixed modes, θ→0.
3. Odd-powers-only Moyal bracket; order-Θ term i{·,·}_Θ; order-Θ³ coefficient −i/24
   (matching rem:ch3-moyal-check); exactness for symbols of degree ≤ 2.
4. Fluctuating coordinates: order-Θ symbol of [X̂_μ,·] is
   iΘ_{μν}∂^νΦ + iΘ^{αβ}(∂_αθ_μ)(∂_βΦ) (connection-inducing term); first
   higher-derivative correction of eq:dictionary in this class at order Θ³.
5. **Revised** variable-Θ statement (F1/F2): for the naive insertion of Θ(x) into the
   constant-coefficient Moyal formula (truncated at Θ², coefficients of the higher terms
   not differentiated), associativity **generically** fails at order Θ²; the antisymmetrized
   order-Θ² associator equals [Θ,Θ]^{abc}∂_af∂_bg∂_ch exactly with factor one **in the
   cyclic-sum convention now pinned inline**; Schouten-closure alone does NOT remove the
   full Θ² associator of the naive truncation — new counterexample (script 4): a generic
   variable 2D bivector is automatically Schouten-closed yet the Θ² coefficient is nonzero
   (4 terms), with vanishing fully antisymmetric part. The necessity condition stands:
   [Θ,Θ] ≠ 0 forces explicit order-Θ² correction operators (or abandonment of the naive
   star ansatz).

Assumption ass:dictionary is not derived and Problem A stays OPEN; nothing here closes
any critical-path item.

## Response to gatekeeper findings

- **F1 (major) — addressed.** Classification corrected (see "Claim classification"): the
  Θ²-associator-vanishing claim is scoped to "constant bivector and the Casimir-transverse
  Poisson control tested in script 3"; generic Poisson bivectors are NOT guaranteed, and
  the new script `verify_poisson_2d_counterexample.py` reproduces the counterexample
  (generic 2D bivector: Schouten-closed by dimension, c2 ≠ 0 with 4 terms; Alt(c2) = 0;
  c2 = 0 for constant w). In the insertion the failure clause now reads "generically fails
  associativity at order Θ²", and the added clause "Schouten-closure alone does not remove
  the full order-Θ² associator of the naive truncation" blocks the sufficiency misreading;
  the "requires … or …" clause is retained as a necessity statement only.
- **F2 (major) — addressed.** The definition
  [Θ,Θ]^{abc} := Θ^{ad}∂_dΘ^{bc} + Θ^{bd}∂_dΘ^{ca} + Θ^{cd}∂_dΘ^{ab} is pinned inline,
  matching the cyclic-sum convention used in script 3 (`sch123`), in which the factor-one
  identity was verified (by me and independently by the gatekeeper's `assoc_generic.py`).
- **F3 (minor) — addressed.** The pairing sentence now cites Remark~\ref{rem:ch3-trace-quadratic}
  for the (2π)^{-2}|Pf Θ|^{-1} trace density and Definition~\ref{def:matrix-coords-ext}
  for the |Pf θ|^{-1} density. Label verified: `\label{rem:ch3-trace-quadratic}` occurs
  exactly once in the .tex sources (ch03-matrix-action.tex:450).
- **F4 (minor) — addressed.** "At finite \(N\) the finite-\(N\) analogue of these data is
  the 't Hooft pair …".
- **F5 (minor) — addressed.** "where \(\{\cdot,\cdot\}_\Theta\) is the symbol-level
  Poisson bracket" is inserted at first use.
- **F6 (minor) — addressed.** The LaTeX block writes ``t Hooft\ (LaTeX left-quote form)
  throughout. In the proposal text Lechner–Scotford (2111.03172) is now labelled scout
  Route 6; verified against reports/sme-scout-20261107-1758.md ("6. Modular-theory tools
  for fluctuating Theta (half-sided inclusions)").

## Target and status

- Problem: A, "matrix-to-modular map", A.map sub-target. appH L15–20 (re-read):
  **OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion:
  PROGRAMME-CONDITIONAL.** Original target (ch17, re-read): specify the Hilbert space,
  Weyl map, continuum limit, and error at each order in Θ; completion: derive
  Assumption ass:dictionary (eq:dict-again) or re-derive the chains without it.
- Dependencies: ch03 eq:NC, def:matrix-coords-ext, ass:dictionary (eq:dictionary),
  rem:ch3-moyal-check, rem:ch3-trace-quadratic; appH free/Poisson lemma and general-sector
  candidate bound. This package is PROGRAMME-CONDITIONAL: class-restricted derivation of
  map data and error bookkeeping; it changes no status.

## Source reading

digest + targeted reads (as in r1; digest COMPACT and CURRENT, head a33e52c, dirty-chapters:
no; label index empty, labels verified by direct grep). This round additionally read in
full: proposals/058-a-map-dictionary-derivation/review-r1.md; reports/sme-scout-20261107-1758.md
route headers (Route numbering); ch03-matrix-action.tex around L450–474
(rem:ch3-trace-quadratic label and the (2π)^{-2}|Pf Θ|^{-1} display). No unreadable files.

## Research and reasoning

Only F1-relevant mathematics changed. The F1 counterexample was reproduced independently:
on R² with Θ^{12} = ε w(x1,x2) the naive truncated product (same truncation hypothesis as
script 3) has order-ε² associator coefficient with four terms, all carrying a derivative
of w (the constant-w control vanishes identically). In dimension 2 there is no independent
Schouten component and the fully antisymmetrized c2 vanishes (dimension: three covariant
indices in 2D), so this is exactly the case where the antisymmetric (Gerstenhaber)
obstruction is silent while the naive truncation is still non-associative at Θ². Hence:
(a) the factor-one antisymmetric identity is compatible with the counterexample; (b)
Schouten-closedness is necessary (at the antisymmetric level) but not sufficient for the
naive truncation; (c) the r1 control (Θ^{12} = ε a(x³) on R³, x³ Casimir) vanishes because
the product is slice-wise constant — a genuinely special family, not the generic Poisson
class. This is recorded in the insertion (the "generically" + "Schouten-closure alone …"
clause) and in the classification below. All other r1 derivations, scripts and outputs are
unchanged.

Literature: still no manuscript citation added, so no bib entries. Lechner–Scotford
(2111.03172, scout Route 6) remains a lead marked not independently verified; the
Latremoliere package (scout Route 1) was not imported.

## Claim classification (corrected per F1)

- Torus product law; torus pairing identity; Hermiticity; plane pairing with
  (2π)^{-2}|Pf Θ|^{-1}: **established identities** (derived; scripts 2, verified
  independently by the gatekeeper).
- Bound ‖R‖ ≤ Σ(θ|σ|)³/24 for mode-limited symbols, 2M<N, uniform in N: **conditional
  result** (established under the stated finite-N hypotheses).
- Odd powers, coefficients i and −i/24, degree-≤2 exactness: **established identity**
  (script 1; matches rem:ch3-moyal-check display).
- Order-Θ fluctuating-coordinate symbol and induced connection; Θ³ first correction:
  **conditional result** within the flat Abelian Weyl calculus.
- Antisymmetrized Θ² associator = [Θ,Θ]^{abc}(cyclic-sum definition)∂_af∂_bg∂_ch with
  factor one: **established identity** under the naive-truncation hypotheses (script 3,
  generic 3D check).
- Θ² associator vanishing: **established only for the constant bivector and the
  Casimir-transverse Poisson control of script 3.** For a generic Poisson bivector it is
  **false for the naive truncation**: nonzero Θ² coefficient demonstrated (script 4;
  established counterexample). The r1 blanket "constant/Poisson" phrasing is withdrawn.
- Consistency condition ([Θ,Θ] ≠ 0 forces Θ² correction operators, or the naive star
  ansatz must be abandoned): **conditional result, necessity only**; Schouten-closedness
  is not asserted as sufficient.
- Selection of the data class by the matrix condensate; unbounded boost/diamond-charge
  symbol and sharp diamond cutoff: **unresolved step**.
- Lechner–Scotford (scout Route 6) and propinquity (scout Route 1) content: **not
  independently verified**, leads only, not used in any derivation here.

## Proposed changes

One insertion, one file, same anchor and position as r1 (gatekeeper-confirmed unique,
byte offset 3007).

**File:** `chapters/appH-microscopic-proofs.tex`, section `sec:status-A`.
**Anchor (verbatim, occurs exactly once):**
"The error bound therefore controls the difference from an unproven candidate, not from the diamond modular Hamiltonian."
Insert the block below after that sentence and before `\paragraph{Missing step.}`, as one
`\paragraph{}` separated by blank CRLF lines; CRLF endings, UTF-8 no BOM. Everything else
in the file is kept unchanged.

COMPLETE final insertion block (ready for integration; gatekeeper markers stripped; the
gatekeeper's corrected wording applied verbatim except that ``t Hooft uses the LaTeX
left-quote form per F6):

```latex
\paragraph{Explicit Weyl data and per-order error in the flat Abelian class.}
Within the constant-\(\Theta\) Abelian Moyal class the map data of Problem~A can be
pinned and the per-order error made explicit. These descriptions are limiting
descriptions of matrix data: \(\Theta\) remains the expectation of the matrix coordinate
commutator, not input geometry. On \(\mathbb R^4\) with constant nondegenerate
\(\Theta\), take \(\mathcal H=L^2(\mathbb R^2)\) and
\(W_\Theta(f)=\int\frac{d^4k}{(2\pi)^4}\tilde f(k)\,e^{\mathrm i k\cdot\hat X}\) with
\([\hat X_\mu,\hat X_\nu]=\mathrm i\Theta_{\mu\nu}\); the pairing
\(\operatorname{Tr}W_\Theta(f)W_\Theta(g)=(2\pi)^{-2}|\operatorname{Pf}\Theta|^{-1}\!\int fg\)
is exact, with the \((2\pi)^{-2}|\operatorname{Pf}\Theta|^{-1}\) trace density of
Remark~\ref{rem:ch3-trace-quadratic} and the \(|\operatorname{Pf}\theta|^{-1}\) density of
Definition~\ref{def:matrix-coords-ext}. At finite \(N\) the finite-\(N\) analogue of these
data is the ``t Hooft pair \(UV=e^{\mathrm i\theta}VU\) on \(\mathbb C^N\),
\(\theta=2\pi p/N\), with Weyl-ordered symbols
\(\widehat W(e_{m,n})=e^{-\mathrm i(\theta/2)mn}U^mV^n\):
\([\widehat W_v,\widehat W_w]=2\mathrm i\sin(\tfrac{\theta}{2}\sigma(v,w))\,\widehat W_{v+w}\)
and \(\operatorname{Tr}\widehat W(f)\widehat W(g)=N\sum_v\hat f_v\hat g_{-v}\) hold
exactly, and for mode-limited symbols with \(2M<N\) the operator-norm remainder of
\(\tfrac1{\mathrm i}[\widehat W(f),\widehat W(g)]-\widehat W(\{f,g\}_\Theta)\), where
\(\{\cdot,\cdot\}_\Theta\) is the symbol-level Poisson bracket, obeys
\(\|R\|\le\sum_{v,w}|\hat f_v|\,|\hat g_w|\,(\theta|\sigma(v,w)|)^3/24\), uniform in
\(N\); the continuum limit is \(N\to\infty\) at fixed modes with \(\theta\to0\). Only
odd powers of \(\Theta\) occur in the Moyal bracket; the order-\(\Theta\) term is
\(\mathrm i\{\cdot,\cdot\}_\Theta\) and the first correction is order \(\Theta^3\) with
coefficient \(-\mathrm i/24\), the third-derivative contraction of
Remark~\ref{rem:ch3-moyal-check}. For fluctuating coordinates
\(\hat X_\mu=W(y_\mu+\theta_\mu)\), the order-\(\Theta\) symbol of
\([\hat X_\mu,\Phi]_\star\) is
\(\mathrm i\Theta_{\mu\nu}\partial^\nu\Phi+\mathrm i\Theta^{\alpha\beta}(\partial_\alpha\theta_\mu)(\partial_\beta\Phi)\):
the second term is the connection-inducing piece and the first higher-derivative
correction of Equation~\eqref{eq:dictionary} in this class is order \(\Theta^3\) with
third derivatives of \(\theta\). For nonconstant \(\Theta\) the naive insertion of
\(\Theta(x)\) into the constant-coefficient Moyal formula generically fails associativity
at order \(\Theta^2\); the antisymmetrized order-\(\Theta^2\) associator equals
\([\Theta,\Theta]^{abc}\partial_af\,\partial_bg\,\partial_ch\) with
\([\Theta,\Theta]^{abc}:=\Theta^{ad}\partial_d\Theta^{bc}
+\Theta^{bd}\partial_d\Theta^{ca}+\Theta^{cd}\partial_d\Theta^{ab}\), and
Schouten-closure alone does not remove the full order-\(\Theta^2\) associator of the
naive truncation; hence a Moyal-type continuum description at a variable
expectation-value \(\Theta\) requires a Schouten-closed leading bivector or explicit
order-\(\Theta^2\) correction bidifferential operators. These statements are for the
flat Abelian constant-\(\Theta\) class with mode-limited or Schwartz symbols; they do
not select this class from the matrix condensate, do not identify the induced connection
with the connection of the ch03 kinetic term or resolve the constant-\(\Theta\) kinetic
obstruction of Remark~\ref{rem:ch3-moyal-check}, do not cover the non-Abelian sector, and
do not bound the unbounded boost/diamond-charge symbol or the sharp diamond cutoff, so
they do not derive Assumption~\ref{ass:dictionary}.
```

Labels referenced and verified to exist, each exactly once in the .tex sources:
`def:matrix-coords-ext` (ch03:173), `rem:ch3-moyal-check` (ch03:372),
`rem:ch3-trace-quadratic` (ch03:450), `eq:dictionary` (ch03:352), `ass:dictionary`
(ch03:346). No new labels; no duplicates (digest: "Duplicate labels: none").
Stale passages elsewhere: none (gatekeeper greps confirmed no conflicting
't Hooft/torus/associator/Schouten usage).

## Verification scripts

All in `proposals/058-a-map-dictionary-derivation/`, run with `python -I`:

1. `verify_moyal_odd_powers.py` (`moyal_out.txt`) — unchanged from r1; all checks True
   (gatekeeper byte-matched).
2. `verify_nc_torus_bound.py` (`torus_out.txt`) — unchanged; all checks True
   (gatekeeper byte-matched).
3. `verify_variable_theta_associator.py` (`assoc_out.txt`) — unchanged; all checks True
   (gatekeeper byte-matched). Its control statement is scoped to the constant bivector
   and the Casimir-transverse family, as its own header comments already say.
4. `verify_poisson_2d_counterexample.py` (`poisson2d_out.txt`) — NEW (F1 lock): generic
   variable 2D bivector (automatically Schouten-closed): order-Θ² associator coefficient
   nonzero (4 terms); its fully antisymmetrized part vanishes; constant-w control
   vanishes. ALL CHECKS: True (run this round).

## Decisions Taken

- Adopted the gatekeeper's corrected snippet verbatim (stripping only the % markers),
  since it preserves the factor-one content while pinning the convention (F2) and the
  necessity-only reading (F1); rejected re-wording it further, to keep the diff minimal.
- Added script 4 rather than only citing the gatekeeper's scratch counterexample, so the
  F1 fact is reproducible inside the proposal folder (the gatekeeper's `assoc_2d.py` lives
  outside the repository and is not part of the record).
- Kept Lechner–Scotford as a lead (scout Route 6) and did not import it; no bib entries.

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step closed; r2 is a scoping/wording
correction round.

## Status-label recommendation

Derived current critical-path set from ch17/appH: A, B, C, D1, E, F, G-derived, N
(H, I, J optional within their scopes). Problem A stays OPEN / CRITICAL PATH for the
matrix-derived label / PROGRAMME-CONDITIONAL. No label changes proposed.

## Author decision needed

none

## Remaining open step

Unchanged from r1: (1) derive that the matrix condensate selects this data class (which
algebra, which expectation-value Θ); (2) identify the connection-inducing term with the
ch03 kinetic-term connection and the metric/sign matching, evading the constant-Θ
obstruction K_Θ^{νρ} ∝ η^{νρ} of rem:ch3-moyal-check; (3) non-Abelian extension of the
map and the per-order bound; (4) symbol classes for the unbounded boost/diamond-charge
symbol and the sharp diamond-boundary cutoff; (5) error control for the δΘ fluctuation
bound (appH general sector).

Ranked avenues (incorporating the F1 sharpening):
1. relax the naive-truncation hypothesis: Kontsevich-formal / corrected star products can
   restore associativity at variable Θ without Schouten-closure (script 4 shows the naive
   Θ² error is nonzero even for Poisson bivectors), so the Θ² obstruction constrains but
   does not forbid a variable-Θ dictionary;
2. extend the per-order calculus to unbounded (boost/diamond-charge) symbol classes;
3. use the Schouten-closedness necessity as a diagnostic on candidate condensate Θ
   expectation values (ties A.map to the condensate problems);
4. upgrade the δΘ candidate bound via half-sided modular inclusion deformation
   (Lechner–Scotford 2111.03172, scout Route 6; not independently verified);
5. theorem-level continuum-limit language via spectral/covariant propinquity (scout
   Route 1; not independently verified).

## Special instructions for the gatekeeper

- Re-run script 4; confirm c2 ≠ 0 (4 terms), Alt(c2) = 0, constant-w control = 0, and that
  the insertion's "generically" + "Schouten-closure alone …" wording matches these facts.
- Confirm the inline definition of [Θ,Θ]^{abc} in the block matches the `sch123` cyclic
  convention of script 3 (factor one only there).
- Confirm the block contains ``t Hooft\ (left-quote form), no straight apostrophe, and no
  % markers from the corrected snippet.
- Confirm rem:ch3-trace-quadratic is the Remark whose display carries (2π)^{-2}|Pf Θ|^{-1}
  (ch03 L466–474 per your read) and that the insertion cites it without asserting the two
  ch03 conventions are reconciled (pre-existing coexistence, per F3).
- Verify nothing in r2 changes the r1 scope limits: no closure language, emergence guard
  intact, anchor unique, one insertion only, no bib/label changes.
