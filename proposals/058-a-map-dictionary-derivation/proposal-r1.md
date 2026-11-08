# Proposal 058-a-map-dictionary-derivation, round 1

## Result

Within the flat Abelian constant-Θ Moyal class (the class the manuscript's own free/Poisson
lemma works in), the A.map data are pinned exactly and the per-order-in-Θ error is made
explicit:

1. **Weyl data and exact pairings.** On R⁴ with constant nondegenerate Θ, H = L²(R²),
   W_Θ(f) = ∫ d⁴k/(2π)⁴ f̃(k) e^{ik·X̂}, [X̂_μ,X̂_ν] = iΘ_{μν}, the pairing
   Tr W_Θ(f)W_Θ(g) = (2π)^{-2}|Pf Θ|^{-1}∫fg is exact and matches the density
   (2π)^{-2}|Pf Θ|^{-1} already displayed in ch03 (L467–474) and the ρ = 1/|Pf θ|
   normalization of Definition def:matrix-coords-ext. At finite N the same data are the
   't Hooft pair UV = e^{iθ}VU on C^N with Weyl-ordered symbols
   Ŵ(e_{m,n}) = e^{−i(θ/2)mn}U^mV^n: the product law
   [Ŵ_v,Ŵ_w] = 2i sin((θ/2)σ(v,w))Ŵ_{v+w} (σ(v,w) = mn′−nm′) and the pairing
   Tr Ŵ(f)Ŵ(g) = N Σ_v f̂_v ĝ_{−v} hold **exactly** (verified to machine precision; the
   pairing carries no Θ-order corrections).

2. **Explicit per-order bound.** For mode-limited symbols (|m|,|n| ≤ M, 2M < N, no
   wraparound), the operator-norm remainder of (1/i)[Ŵ(f),Ŵ(g)] − Ŵ({f,g}_Θ) satisfies the
   exact elementary bound ‖R‖ ≤ Σ_{v,w}|f̂_v||ĝ_w|(θ|σ(v,w)|)³/24, uniform in N. The
   continuum limit is N→∞ at fixed modes with θ→0. Only odd powers of Θ occur in the
   Moyal bracket; the order-Θ term is i{·,·}_Θ and the first correction is order Θ³ with
   coefficient −i/24, matching the displayed −i/24 term of Remark rem:ch3-moyal-check.
   Exactness of the bracket for symbols of degree ≤ 2 (the "exact at constant Θ" content of
   the appH free/Poisson lemma) is re-verified symbolically.

3. **Dictionary leading map inside the class.** For fluctuating coordinates
   X̂_μ = W(y_μ + θ_μ), the order-Θ part of the Weyl symbol of [X̂_μ,·] is
   iΘ_{μν}∂^νΦ + iΘ^{αβ}(∂_αθ_μ)(∂_βΦ): the first term is the dictionary leading map
   (eq:dictionary), the second is the connection-inducing piece (it reproduces a connection
   D^γ = Θ^{γμ}∂_μ + Θ^{γμ}Θ^{αβ}(∂_αθ_μ)∂_β at this order), and the first genuine
   higher-derivative correction of the dictionary in this class is order Θ³ with third
   derivatives of θ.

4. **Bounded associativity obstruction at variable Θ.** Inserting a nonconstant bivector
   Θ(x) into the constant-coefficient Moyal formula (no Kontsevich corrections) is
   inconsistent at order Θ²: the fully antisymmetrized Θ² associator equals the Schouten
   contraction [Θ,Θ]^{abc}∂_af∂_bg∂_ch **exactly with factor one** (coefficient comparison
   over the 27 first-derivative monomials), while for constant or Schouten-closed (Poisson)
   bivectors the Θ² associator vanishes. Consequence: any dictionary/continuum star
   calculus at a nonconstant expectation-value Θ must either have Schouten-closed leading
   Θ (a derived consistency condition) or supply explicit order-Θ² correction bidifferential
   operators.

None of this derives Assumption ass:dictionary or closes Problem A; see "Remaining open
step". The honest hard part left open is the one the SME scout flagged (Route 2): the
norm bounds are established for bounded symbol classes (finite N matrices, mode-limited /
Schwartz symbols), not for the unbounded boost/diamond-charge symbol of K_0 nor for the
sharp diamond-boundary cutoff.

## Target and status

- Problem: A, "matrix-to-modular map", A.map sub-target.
- Current status (appH-microscopic-proofs.tex L15–20, read in full): **OPEN. Priority:
  CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL.** Original
  target (ch17-agenda.tex L377–392, read in full): a derivation must specify the Hilbert
  space, Weyl map, continuum limit, and error at each order in Θ, i.e. derive
  Assumption ass:dictionary (eq:dict-again) so it can be retired; "Renaming the same map
  does not meet this item." Completion criterion: "Problem A: Assumption ass:dictionary is
  derived, or the chains of the other items are re-derived without invoking it."
- Dependencies: ch03 def:def:matrix-coords (eq:NC), def:matrix-coords-ext, ass:dictionary
  (eq:dictionary), rem:ch3-moyal-check; appH free/Poisson lemma (L22–39) and general-sector
  candidate bound (L41–61). DERIVED / PROGRAMME-CONDITIONAL: this package is
  PROGRAMME-CONDITIONAL — a class-restricted derivation of the map data and error bookkeeping;
  it changes no status.

## Source reading

digest + targeted reads. Digest COMPACT and CURRENT (head a33e52c, 30 files, dirty-chapters:
no; label index empty, so all labels were verified by direct grep in the .tex sources).
Read in full: appH-microscopic-proofs.tex L12–73 (Problem A entry incl. free/Poisson lemma
and general-sector passage), ch17-agenda.tex L370–400 and the completion-criterion region,
ch03-matrix-action.tex L55–205 (eq:NC, eq:Smatrix, def:matrix-coords-ext with the
|Pf θ| density) and L215–440 (ass:dictionary L345–363, eq:dictionary L353,
rem:ch3-moyal-check L371–441) and the pairing region L460–510; reports/ledger.md (recent
items and environment notes); reports/sme-scout-20261107-1758.md in full. No unreadable
files.

## Research and reasoning

**Step 1 (plane data).** For constant Θ the Stone–von Neumann/Weyl form gives H = L²(R²)
and W_Θ(f) as above. Exact pairing: ∫dk dg f̃ g̃ Tr e^{ik·X̂}e^{ig·X̂} = (2π)^{-4}∫dk dg
f̃ g̃ e^{−(i/2)k∧Θg}(2π)²δ(k+g) = (2π)^{-2}|Pf Θ|^{-1}∫fg (the phase is odd in (k,g) and
drops). This matches ch03's existing (2π)^{-2}|Pf Θ|^{-1} measure — a consistency check of
the map against ch03 normalization, not a new input.

**Step 2 (finite-N class).** 't Hooft data: H_N = C^N, U = diag(w^j), V cyclic shift,
UV = e^{iθ}VU, θ = 2πp/N. The symmetric (Weyl-ordered) map Ŵ(e_{m,n}) = e^{−i(θ/2)mn}U^mV^n
conjugates the clock/shift algebra into the exact product law
[Ŵ_v,Ŵ_w] = 2i sin((θ/2)σ(v,w))Ŵ_{v+w}. (Sign convention: with β = +θmn/2 the law carries
sin(−θσ/2); the Weyl-ordered symmetric choice is β = −(θ/2)mn. An earlier script version
had the sign wrong and the verification below fixed it.) Comparing the structure constant
2 sin((θ/2)σ) with the classical iθσ and using |2 sin x − 2x| ≤ |x|³/3 gives the exact
remainder bound ‖R‖ ≤ Σ|f̂||ĝ|(θ|σ|)³/24 — a per-order-in-Θ operator-norm bound that is
honest because every object is a bounded N×N matrix; it is uniform in N for fixed mode
sets (2M < N). The pairing Tr Ŵ(f)Ŵ(g) = N Σ f̂_v ĝ_{−v} = N·(torus mean of fg) is exact.

**Step 3 (odd powers and exactness).** The Moyal bracket 2i sin((Θ∂∂)/2) contains only odd
powers; coefficients i (order Θ) and −i/24 (order Θ³), matching rem:ch3-moyal-check's
displayed expansion; exactness for linear symbols and degree ≤ 2 symbols is verified
symbolically (script 1) — this is the algebraic content of the appH "exact at constant Θ"
clause.

**Step 4 (fluctuating coordinates).** With X̂_μ = W(y_μ + θ_μ) the bracket symbol at order Θ
is iΘ_{μν}∂^νΦ + iΘ^{αβ}(∂_αθ_μ)∂_βΦ. The second term is linear in ∂θ and of order Θ,
matching the "connection + higher-derivative corrections" structure of eq:dictionary: it
induces D_γ = ∂_γ − (Θ^{αβ}∂_αθ_μ)∂_β-type connection terms. The first correction beyond
the dictionary form is order Θ³ (third derivatives of θ). This derives the **shape** of
eq:dictionary's leading map and its first higher-derivative order inside the flat Abelian
class; it does not derive the metric, the sign, the specific connection A_μ of the
ch03 kinetic term, or the non-Abelian content, and ch03's own constant-Θ kinetic matching
obstruction in rem:ch3-moyal-check (no nonzero constant real Θ with K_Θ^{νρ} ∝ η^{νρ})
remains untouched.

**Step 5 (variable-Θ associativity).** The naive insertion of Θ(x) into the constant-form
Moyal series fails associativity at order Θ² unless [Θ,Θ]_Schouten = 0. Verified exactly
(script 3, 3D model with Θ^{12} = εa(x³), Θ^{23} = εb(x²)): all second-derivative pieces
of the Θ² associator cancel, the 8 remaining terms are pure (Θ∂Θ)(∂f)(∂g)(∂h)
trilinears, and the antisymmetrized Θ² associator equals
([Θ,Θ]^{123}/ε²)·det(df,dg,dh) with coefficient exactly 1 (after fixing a sympy
sequential-subs pitfall by building the antisymmetrization by slot construction). For
constant Θ and for the Poisson variable choice Θ^{12} = εa(x³) (x³ a Casimir) the Θ²
coefficient vanishes identically. This is the first Gerstenhaber obstruction; it yields a
**derived consistency condition** on any variable expectation-value Θ entering a Moyal-type
continuum description of the dictionary: at leading order the bivector must be
Schouten-closed or explicit order-Θ² correction operators (Kontsevich-type) must be part
of the map. All hypotheses stated: formal star product truncated at Θ², constant-form
higher terms, smooth components.

**Emergence guard (explicit).** The plane and torus descriptions are used as LIMITING
descriptions of matrix data only. Θ is the state expectation of the matrix coordinate
commutator (as in ch03), not input geometry; no fundamental metric is assumed anywhere in
this package. This is the caveat the SME scout attached to Routes 1–2 and is honoured here.

**Literature.** No manuscript citation is added, so no bib entries are proposed. Scout
Route 2 (Calderón–Vaillancourt/Shubin/Rieffel symbol calculus; books "not independently
verified" by the scout) was NOT imported: the finite-N bound above is self-contained and
elementary, and the only place the literature would enter is the unbounded-symbol extension,
which stays open. Scout Route 3 (Lechner–Scotford 2111.03172) is listed as an avenue; the
record was not independently verified this session (marked not independently verified).

## Claim classification

- Pairing Tr W_Θ(f)W_Θ(g) = (2π)^{-2}|Pf Θ|^{-1}∫fg; finite-N product law; finite-N pairing
  identity; Hermiticity for real symbols: **established identity** (derived; scripts 2).
- Exact per-order operator-norm bound ‖R‖ ≤ Σ(θ|σ|)³/24 for mode-limited symbols, 2M<N:
  **conditional result** (hypotheses: finite N, 't Hooft data, mode limit; established under them).
- Odd powers, coefficients i and −i/24, degree-≤2 exactness: **established identity**
  (script 1; consistent with rem:ch3-moyal-check).
- Order-Θ fluctuating-coordinate map and induced connection; Θ³ first correction:
  **conditional result** within the flat Abelian Weyl calculus.
- Θ² associator = Schouten contraction (factor one); vanishing for constant/Poisson bivectors:
  **established identity** under the stated truncation hypotheses (script 3).
- Derived consistency condition (Poisson leading Θ or explicit Θ² corrections needed):
  **conditional result** (conditional on using a Moyal-type star calculus for the continuum
  description; if the dictionary map is not a star product this condition need not bind —
  but then the map must still be constructed).
- Selection of this data class by the matrix condensate; bounded-symbol ⇒ unbounded
  boost/diamond-symbol extension: **unresolved step**.
- Lechner–Scotford theorem content: **not independently verified** (scout-sourced lead only).

## Proposed changes

One insertion, one file.

**File:** `chapters/appH-microscopic-proofs.tex`, section `sec:status-A`, after the
"General sector" paragraph and before `\paragraph{Missing step.}`.

**Anchor (verbatim, occurs exactly once, verified by grep at L59–61):**
"The error bound therefore controls the difference from an unproven candidate, not from the diamond modular Hamiltonian."
(kept, together with everything before and after it; nothing else in the file changes;
the paragraph `\paragraph{Missing step.}` is kept unchanged).

Insert:

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
is exact, matching the density of Definition~\ref{def:matrix-coords-ext}. At finite
\(N\) the same data are the 't Hooft pair \(UV=e^{\mathrm i\theta}VU\) on
\(\mathbb C^N\), \(\theta=2\pi p/N\), with Weyl-ordered symbols
\(\widehat W(e_{m,n})=e^{-\mathrm i(\theta/2)mn}U^mV^n\):
\([\widehat W_v,\widehat W_w]=2\mathrm i\sin(\tfrac{\theta}{2}\sigma(v,w))\,\widehat W_{v+w}\)
and \(\operatorname{Tr}\widehat W(f)\widehat W(g)=N\sum_v\hat f_v\hat g_{-v}\) hold
exactly, and for mode-limited symbols with \(2M<N\) the operator-norm remainder of
\(\tfrac1{\mathrm i}[\widehat W(f),\widehat W(g)]-\widehat W(\{f,g\}_\Theta)\) obeys
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
\(\Theta(x)\) into the constant-coefficient Moyal formula fails associativity at order
\(\Theta^2\), with antisymmetrized associator equal to the Schouten contraction
\([\Theta,\Theta]^{abc}\partial_af\,\partial_bg\,\partial_ch\); hence a Moyal-type
continuum description at a variable expectation-value \(\Theta\) requires a
Schouten-closed leading bivector or explicit order-\(\Theta^2\) correction
bidifferential operators. These statements are for the flat Abelian constant-\(\Theta\)
class with mode-limited or Schwartz symbols; they do not select this class from the
matrix condensate, do not identify the induced connection with the connection of the
ch03 kinetic term or resolve the constant-\(\Theta\) kinetic obstruction of
Remark~\ref{rem:ch3-moyal-check}, do not cover the non-Abelian sector, and do not bound
the unbounded boost/diamond-charge symbol or the sharp diamond cutoff, so they do not
derive Assumption~\ref{ass:dictionary}.
```

Labels referenced and verified to exist (single occurrence in .tex sources):
`def:matrix-coords-ext` (ch03:173), `rem:ch3-moyal-check` (ch03:372), `eq:dictionary`
(ch03:352), `ass:dictionary` (ch03:346). No new labels are introduced; no duplicates.

Stale passages elsewhere: none. The ch17 Problem A text and the appH "Missing step."
paragraph remain accurate; this insertion does not weaken them. ch03 rem:ch3-moyal-check's
expansion coefficients are confirmed by script 1 (no edit needed).

## Verification scripts

All under `proposals/058-a-map-dictionary-derivation/`, run with `python -I`:

1. `verify_moyal_odd_powers.py` (output `moyal_out.txt`): Moyal bracket per-order
   structure; checks (a) even powers vanish, (b) order-Θ coefficient = i·Poisson,
   (c) order-Θ³ coefficient = −i/24 third-derivative contraction, (d) exactness for
   linear and degree-≤2 symbols. Final run: all True.
2. `verify_nc_torus_bound.py` (output `torus_out.txt`): 't Hooft data, Weyl-ordered map;
   product law to 1e-14; exact pairing identity to 6e-13; per-order bound
   ‖R‖ ≤ (θ³/24)Σ|σ|³ satisfied at θ = 2πp/N, p = 1..4 (N = 60, M = 5); real symbol ⇒
   Hermitian. All checks True.
3. `verify_variable_theta_associator.py` (output `assoc_out.txt`): variable-bivector
   associator; (1) [Θ,Θ]¹²³ = ε²a b′ ≠ 0; (2) Θ² associator nonzero, 8 terms all pure
   first-derivative; (3) antisymmetrized Θ² associator = ([Θ,Θ]¹²³/ε²)·det(df,dg,dh)
   exactly; (4) Θ² coefficient vanishes for constant bivector and for the Poisson
   single-component variable bivector. All checks True.

## Decisions Taken

- Route: implemented the scout Route 2 core elementarily (finite-N exact bound + symbol
  bookkeeping) instead of importing propinquity theorem machinery: the import would add
  unverifiable citations for content the package proves self-containedly, and the hard
  part (unbounded symbols) is untouched by either route. Rejected alternative: Route 1
  (Latremoliere propinquity) as the package spine.
- Variable-Θ obstruction: kept as a *bounded* result with its hypothesis class (naive
  constant-form star calculus truncated at Θ²) rather than dismissing variable Θ; the
  Poisson-closedness condition is offered as a derived consistency requirement to test
  against the condensate's Θ. Rejected: presenting the associator failure as a general
  no-go.
- Insertion wording: single labelled paragraph in appH next to Problem A's ledger section
  with one scoped closing sentence (CLAUDE.md convention), no ch03 edits, no closure
  language.
- Fixed the antisymmetrization method after discovering that sympy's chained `subs`
  corrupts multi-relabel antisymmetrization; the corrected construction gave the exact
  factor-one Schouten identity.

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step is closed; the package fixes the
A.map data and error structure inside a stated class and records a bounded obstruction.

## Status-label recommendation

Derived current critical-path set from ch17/appH: A, B, C, D1, E, F, G-derived, N (H, I, J
optional within scope). Problem A stays OPEN / CRITICAL PATH for the matrix-derived label /
PROGRAMME-CONDITIONAL. No label changes proposed.

## Author decision needed

none

## Remaining open step

To close the original A.map target one still needs:
1. a derivation that the matrix condensate selects the pinned data class (which algebra,
   which expectation-value Θ) — currently an input class;
2. the identification of the connection-inducing term with the ch03 kinetic-term
   connection A_μ and the metric/sign matching, including a mechanism that evades the
   constant-Θ obstruction K_Θ^{νρ} ∝ η^{νρ} of rem:ch3-moyal-check (nonconstant Θ or
   other sector structure);
3. the non-Abelian extension of the map and of the per-order bound;
4. extension of the norm bounds to the unbounded boost/diamond-charge symbol of K_0 and
   to the sharp diamond-boundary cutoff (the honest hard part; also open in the field per
   the scout);
5. error control for the δΘ fluctuation bound of appH L51–61 (candidate, unproved).

Ranked avenues (favouring the infrared / full-GR derivation):
1. extend the per-order calculus to the unbounded boost/diamond-charge class (weighted
   symbol classes; the exact finite-N bound suggests the right Θ³ bookkeeping);
2. use the derived Schouten-closedness condition as a diagnostic on candidate condensate
   Θ expectation values (ties A.map to the condensate problem in ch03/ch04);
3. upgrade the δΘ candidate bound via half-sided modular inclusion deformation
   (Lechner–Scotford 2111.03172 template; record not independently verified);
4. theorem-level continuum-limit language via covariant/spectral propinquity
   (Latremoliere; scout-sourced, not independently verified);
5. Kontsevich-form correction operators if the condensate Θ turns out non-Poisson.

## Special instructions for the gatekeeper

- Re-run the three scripts (outputs saved). Re-derive by hand: the sign of the
  Weyl-ordering phase (β = −(θ/2)mn vs +) and the product law [Ŵ_v,Ŵ_w] =
  2i sin((θ/2)σ(v,w))Ŵ_{v+w} — an earlier draft had the opposite sign; the current one is
  what the numerical product law (1e-14) supports.
- The Θ² associator identity holds only for the naive constant-form truncated calculus;
  it must not be asserted for Kontsevich-deformed or non-star products. Check the
  hypothesis wording in the inserted paragraph matches this.
- The inserted paragraph must not be read as closing anything: it names its class in the
  first and last sentences. Verify no closure language crept in.
- Confirm no bib changes are needed (none proposed), no labels are added, and the anchor
  sentence occurs once.
- Pairing normalizations must be checked against ch03 L467–474 (they agree; do not
  "correct" them).
