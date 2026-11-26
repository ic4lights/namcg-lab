# Proposal 116-d1-state-nondeg-realization, round 2

## Result

Edge 1 (STATE/CONFIGURATION REALIZATION) of the D1 frame clause, advanced inside the
hypothesis class that ordinal 43 (integrated item 115) fixed: Presentation B with the
displayed potential `eq:V` and the Repair-II frame reading `eq:vev-is-frame`. Three new
derived statements, each verified by `verify_r116.py` (29/29 PASS, recorded in
`out-r116.txt`):

1. **Sharp distance form of the threshold.** For the operator norm,
   `d(Phi) := min_{U unitary} ||Phi - v U|| = max_i |sigma_i - v|` exactly (the minimum
   is attained at the polar factor; Weyl's singular-value inequality is the lower bound;
   the Frobenius analogue is `sqrt(sum_i (sigma_i - v)^2)`). On `d <= v` the potential
   of `eq:V` obeys the two-sided estimate
   `(lambda/4) d^2 (2v - d)^2 <= V <= lambda d^2 (2v + d)^2`,
   and **both sides are sharp**: the upper is attained at the uniform radial deviation
   `Phi = (v + d) U`, the lower at the single-scalar deviation with singular values
   `(v - d, v, v, v)`. Consequences (all derived): the sublevel set localizes,
   `V <= eps <= lambda v^4/4` forces `d <= d_eps := v - sqrt(v^2 - 2 sqrt(eps/lambda))`
   (real exactly for `eps <= lambda v^4/4`; at `eps = lambda v^4/4` it reads `d <= v`,
   reproducing the ordinal-43 threshold `inf{V : det Phi = 0} = lambda v^4/4` as the
   statement that a defect point sits at distance exactly `v` from `v U(4)`), and
   `|det e| >= (1 - d/v)^4` with equality at `Phi = (v - d) U`; the induced bound
   `(1 - d_eps/v)^4 = (1 - sqrt(4 eps/lambda)/v^2)^2` coincides identically with the
   integrated ordinal-43 bound (sympy identity, N7), so the distance route neither
   duplicates nor contradicts it - it sharpens it into a geometric localization.

2. **Sharp fluctuation radius.** `sup{ V : d <= delta } = lambda delta^2 (2v + delta)^2`
   (exact, attained at `Phi = (v + delta) U`), hence the operator-norm ball of radius
   `delta` around the vacuum manifold `eq:vacuum-manifold` is mapped strictly below the
   defect threshold `lambda v^4/4` **if and only if** `delta < delta_* := (sqrt(6) - 2) v/2`
   (= `v (sqrt(3/2) - 1)`, ratio `delta_*/v = 0.2247448713915889...`, recorded); at
   `delta = delta_*` the supremum **equals** the threshold. Every configuration field
   with `sup_x d(Phi(x)) = delta < delta_*` therefore satisfies the pointwise hypothesis
   of the ordinal-43 paragraph everywhere with `|det e| >= (1 - delta/v)^4 > 0`. This is
   the explicit small-fluctuation domain requested by mission edge 1(a), with sharp
   constants, for the actual `eq:V` at its stated normalization.

3. **Realization by finite potential energy (measure form).** For any field
   `x -> Phi(x)` on any measure space `(R, mu)` with `E_V := int_R V dmu < oo`: the
   possible defect set has `mu{ x : det e(x) = 0 } <= mu{V >= lambda v^4/4} <=
   4 E_V / (lambda v^4)`, and for every `0 < eps < lambda v^4/4` the refined estimate
   `mu{ |det e| < (1 - sqrt(4 eps/lambda)/v^2)^2 } <= mu{V > eps} <= E_V / eps` holds;
   the volume bound is **saturated** by a region of singular values `(0, v, v, v)`
   (equality in the check output for `f = 0.01, 0.1, 0.37, 1.0`). Consequently the sets
   `{V >= lambda v^4/4}` and `{det e = 0}` have `mu`-measure at most
   `4 E_V/(lambda v^4)`: every configuration of finite potential energy - in
   particular every classical solution of `eq:Phi-eom` with finite potential
   energy on a finite-measure slice, and every finite Euclidean-form action
   history - realizes `V < lambda v^4/4` and pointwise frame non-degeneracy off
   a set of at most that measure; null when `E_V = 0`, and NOT improvable to
   null for `E_V > 0` (the constant `sigma = (0,v,v,v)` field is an exact
   `eq:Phi-eom` solution - `D Phi = 0` and
   `Phi(Phi^dag Phi - v^2 I) = W diag(sigma_i(sigma_i^2 - v^2)) Z^dag = 0` since
   every `sigma_i` lies in `{0, v}` - with `V = lambda v^4/4` and `det e = 0`
   everywhere and finite energy on every finite-measure slice, attaining
   `mu{det e = 0} = 4 E_V/(lambda v^4)` with equality).
   This is the first positive realization-grade statement for the state/configuration
   route: previously (ordinal 43 and its closing caveat) the pointwise bound was only
   recorded as an available hypothesis that no named class was shown to satisfy.

Bottom line: **derive**. Positive derivation-grade data for the named missing step
"that the physical state or the bilocal composite realizes the pointwise bound
`V < lambda v^4/4`" (ordinal-43 closing sentence; ranked avenue 1 of review-r1 of 115),
delivered as the sharp small-measure realization by finite-potential-energy
configurations (`mu{det e = 0} <= 4 E_V/(lambda v^4)`, null when `E_V = 0`, optimal in
`E_V` by the constant `(0,v,v,v)` `eq:Phi-eom` solution). No state of the matrix theory
is constructed and none is claimed: converting `ass:nondeg` into a state hypothesis or
a small-measure non-degeneracy statement is NOT discharging it; D1/D/E stay
OPEN; the frame reading stays conditional on `eq:vev-is-frame`; Presentation-A selection
of `eq:V` stays recorded-as-missing (ch03 `sec:ch3-relate`); the bilocal-composite
analogue of the Elitzur paragraph is checked and does NOT follow from the pointwise
machinery (stated, with reason, below).

## Target and status

- Problem: **D1 / Problem D frame clause**, `chapters/appH-microscopic-proofs.tex`,
  section `sec:status-D` (heading at live L765). Verbatim ledger status (live L769-772):
  "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.
  Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a
  scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion
  is unmet."
- The frame clause, verbatim (live L801-802, Problem D "Missing step"): "The locked
  frame and its non-degeneracy must also be derived rather than assumed
  (Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg})."
- Chapter 17, verbatim (live L330): "\emph{CRITICAL PATH; OPEN.}"; (live L339-342):
  "D1 closure also requires that the locked frame exist and be non-degenerate on the
  claimed domain, derived from the same microscopic data rather than taken from
  Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg}." Closure-list item (live
  L715-720): "Problem~D1: an \(SO(3,1)\) gauge symmetry is derived from the matrix
  algebra and condensate, with the \(\omega,A_\mu,B\) and ghost operators specified and
  the field content stated. The locked frame and its non-degeneracy on the claimed
  domain are derived, not assumed (Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg})."
- DERIVED criterion, verbatim (live ch17 L57-59): "Completion words are \emph{DERIVED}
  and \emph{PROGRAMME-CONDITIONAL}. Derived means that the problem's target has no
  remaining assumed premise in the claimed chain." And (live L698-701): "DERIVED means
  no remaining assumed premise in the claimed chain, so a chain that still uses
  Assumption~\ref{ass:dictionary}, \ref{ass:lorentzian}, \ref{ass:frame-lock},
  \ref{ass:nondeg}, \ref{ass:gap-psi} or~\ref{ass:EFT-a2} does not qualify."
  This package claims nothing DERIVED; nothing here removes `ass:frame-lock` or
  `ass:nondeg` from the chain.
- Ordinal-43 paragraph's own scope sentence, verbatim (live appH L1711, last sentence):
  "These statements are properties of the displayed Presentation-B potential: that the
  matrix integral selects it, that the physical state or the bilocal composite of the
  preceding paragraph realizes the pointwise bound \(\mathcal V<\lambda v^4/4\), and the
  quantum stability of the minimum are not derived, so Assumptions~\ref{ass:frame-lock}
  and~\ref{ass:nondeg} are restated as conditional statements and are not discharged,
  the locking is not derived from Presentation~A, and Problem~D remains OPEN and
  PROGRAMME-CONDITIONAL."
- Gating (with src): review-r1 of 115, "Scope of what is established": "Avenues still
  open for the frame clause, ranked: (1) the state hypothesis 'pointwise bound
  V < lambda v^4/4' (sharpest current replacement of `ass:nondeg` on the configuration
  route); (2) its bilocal-composite analogue; (3) Presentation-A derivation of the
  potential form; (4) quantum stability of the strict orbit minimum." This package takes
  ranked avenue 1. Recommended disposition there: "the state-hypothesis route (1) above
  ... rank first."
- DERIVED vs PROGRAMME-CONDITIONAL: nothing is DERIVED for the full-GR criterion. The
  package converts the state-route gap from "no class shown to satisfy the bound" into
  "sharp geometric domain + small-measure realization by all
  finite-potential-energy configurations, with a saturated volume bound (the saturation
  configuration is itself an `eq:Phi-eom` solution, so no pointwise strengthening holds
  in this class)", inside Presentation B.

## Source reading

digest + targeted reads. Gate: `python -I scripts/make_digest.py --check` printed
`DIGEST CURRENT` (also re-run after the interrupted round-1 run; head 8b9ff393 as
expected). Baseline verified: `chapters/appH-microscopic-proofs.tex` sha1
`f7a415d4707241ea6829b607afbf207697b50409`, 830881 bytes (ordinal-43 integration,
uncommitted - expected). No full-scan trigger: this package adds a clearly labelled
conditional paragraph; it changes no definition, assumption, scope statement or status
passage. Files read in full or in relevant ranges this run: appH L765-812 (Problem D
ledger + missing step), L1160-1230 (indefinite locked-block quadratic diagnostic - see
scope note), L1600-1712 (end of Problem D: class paragraphs, L1708 Elitzur/bilocal,
L1711 ordinal-43), L1713 (Problem E heading, the insert anchor), L2148-2172 (recorded
\(V^{(2)}=2\lambda v^4\) and the \(\lambda v^2\) boost-mass split); ch17 L55-72,
L325-350, L645-660, L695-703; ch03 L225-300 (eq:Smicro tail, `eq:V` L240-244,
`eq:vacuum-manifold` L246-251, `eq:VEV`, `ass:frame-lock`), L305-315 (`eq:Phi-eom`),
L335-365 (Presentation-A gap, `ass:dictionary`); ch04 L55-99 (`eq:polar`,
`eq:vev-is-frame`), L150-184 (`def:composite-metric`, `eq:g-from-e`, `ass:nondeg` and
the defect paragraph); `proposals/115-d1-frame-nondeg-defect-threshold/proposal-r1.md`
(L1-L120; the three lemmas and scope) and `review-r1.md` (full); `cert-r115p.py`
(the certificate pattern reused); `proposals/114-.../manifest.md` (manifest
convention). `dirty-chapters: yes` corresponds to the uncommitted ordinal-43
integration; the working tree matches the pin. No unreadable files.

Verbatim definition quotes used by this package (live tree):

- `eq:V` (ch03 L240-244):
  "V(\Phi^\dagger\Phi) = \frac{\lambda}{4} \mathrm{Tr}\bigl(\Phi^\dagger\Phi-v^2\mathbb{I}\bigr)^2." (displayed equation; lambda/4 as shown)
- `eq:vacuum-manifold` (ch03 L246-251): "\Phi^\dagger\Phi=v^2\mathbb{I}" with prose "Its
  minima lie on the manifold ... in the internal space, up to unitary rotations."
- `eq:VEV` (ch03 L252-254): "\langle\Phi^I{}_A\rangle=v\,\delta^I{}_A".
- `ass:frame-lock` (ch03 L263-270): "There exists a stable vacuum~\eqref{eq:VEV} (or a
  locally equivalent vacuum) in which four internal directions are identified with the
  four tangent directions. Goldstone modes associated with the broken generators are
  available to be eaten by a connection, as in Chapter~10."
- `eq:vev-is-frame` (ch04 L89-95): "e^A_\mu(x) \equiv \frac1v\,\langle\Phi^{A}{}_\mu(x)\rangle",
  preceded by "The vierbein \emph{is} the normalized vacuum".
- `ass:nondeg` (ch04 L169-173): "On the region of spacetime under consideration,
  \(e^A_\mu\) has non-vanishing determinant. Equivalently, the four covectors
  \(e^A{}_\mu\mathrm{d}x^\mu\) are linearly independent." Preceded by (ch04 L168):
  "Non-degeneracy is not automatic."
- `eq:Phi-eom` (ch03 L308-314): "D_\mu\bigl(\sqrt{-g^{(0)}}\,g^{(0)\mu\nu}D_\nu\Phi\bigr)
  -\sqrt{-g^{(0)}}\,\frac{\lambda}{2}\Phi\bigl(\Phi^\dagger\Phi-v^2\mathbb{I}\bigr)=0."
- Elitzur/framing paragraph, live appH L1708 (bilocal passage), verbatim core: "On this
  reading Assumption~\ref{ass:nondeg} becomes a non-degeneracy statement about the
  two-point composite rather than a consequence of a broken symmetry, and the locking is
  recorded as a complementarity of regimes rather than a local spontaneous breaking."
- Recorded quadratic datum (live appH L2159-2161, cited not re-derived): "For \(d=vB\)
  that paragraph gives \(V^{(2)}=\lambda v^2\,\mathrm{Tr}H^2=2\lambda v^4\neq0\), so the
  potential of~\eqref{eq:V}, which is built from the positive-definite
  \(\mathrm{Tr}\,\Phi^\dagger\Phi\), is not invariant under these generators."

## Research and reasoning

### Setting and standing objects

Throughout, `Phi` is a complex `4 x 4` matrix (the mixed-index field of `eq:V`), with
singular values `sigma_1 >= ... >= sigma_4 >= 0`, `v > 0`, `lambda > 0`, and
`V(Phi) = (lambda/4) Tr(Phi^dag Phi - v^2 I)^2 = (lambda/4) sum_i (sigma_i^2 - v^2)^2`
(the SVD reduction is the identity verified in item 115; cited, not re-derived). The
vacuum manifold is `{v U : U unitary}` (`eq:vacuum-manifold`). The frame is the
Repair-II reading `e = Phi / v` (or its vev, `eq:vev-is-frame`); `det e = det Phi / v^4`,
so pointwise non-degeneracy of `e` is `det Phi != 0`, i.e. `sigma_4 > 0`. All statements
below are unconditional consequences of these displayed formulas; their hypothesis class
is Presentation B, and the closing scope paragraph records what remains underived.

### D1. Procrustes distance to the vacuum manifold

Define `d(Phi) := min_{U unitary} || Phi - v U ||` (operator norm).

**Claim D1a (exact value).** `d(Phi) = max_i |sigma_i - v|`, and the minimum is attained
at the polar factor `U_* = W Z^dag` of `Phi = W diag(sigma) Z^dag`.

*Proof.* (i) Attainability: `Phi - v U_* = W diag(sigma_i - v) Z^dag`, an SVD, so
`|| Phi - v U_* || = max_i |sigma_i - v|`. (ii) Lower bound: for any unitary `U`,
Weyl's singular-value perturbation inequality (`||A|| >= |sigma_j(A + B) - sigma_j(B)|`
for every `j`, applied with `A = Phi - vU`, `B = vU`, whose singular values are all `v`)
gives `sigma_j(Phi - vU) >= |sigma_j(Phi) - v|` for each `j`, hence
`|| Phi - vU || = sigma_1(Phi - vU) >= max_j |sigma_j(Phi) - v|`. The `d = 0` case
reads `Phi = vU`, i.e. `Phi^dag Phi = v^2 I` (`eq:vacuum-manifold`), so `d` vanishes
exactly on the vacuum manifold. The Frobenius-norm analogue `min_U || Phi - vU ||_F =
(sqrt(sum_i (sigma_i - v)^2)` follows from unitary invariance of the Frobenius norm by
expanding `|| Phi - vU ||_F^2 = sum sigma_i^2 + 4 v^2 - 2 v Re tr(Phi^dag U)` and
maximizing `Re tr(Phi^dag U) <= sum_i sigma_i` (equality at `U = U_*`).
Numerics: N1, three checks, rel-err ~1e-15. (Weyl's inequality and the polar
decomposition are standard; the named inequality is MIRACZYK-Weyl for singular values,
Bhatia, *Matrix Analysis*, III.2 - not independently re-verified beyond the numeric
lower-bound test of N1, which tested 3000 random unitaries against the polar value.)

### D2. Sharp two-sided estimate

**Claim D2.** For `d := d(Phi) <= v`:
`(lambda/4) d^2 (2v - d)^2 <= V(Phi) <= lambda d^2 (2v + d)^2`, and for `d > v` the
upper bound `V <= lambda d^2 (2v + d)^2` continues to hold with `2v + d > 0`; both
bounds are attained at fixed `d`: the upper at `sigma = (v + d, v, v, v)` repeated
uniformly (i.e. `Phi = (v + d) U`), the lower at `sigma = (v - d, v, v, v)`.

*Proof.* Write `sigma_i = v + t_i` with `|t_i| <= d` and, when `d <= v`, `t_i >= -v` so
`sigma_i >= 0` is automatic. Then `(sigma_i^2 - v^2)^2 = (2v + t_i)^2 t_i^2` and
`V = (lambda/4) sum_i (2v + t_i)^2 t_i^2`.
*Upper:* `|t_i| <= d` gives `(2v + t_i)^2 t_i^2 <= (2v + d)^2 d^2` termwise, and
`sum_i` of four such terms is `<= 4 lambda d^2 (2v+d)^2 / 4`. Wait - the sharp statement
is `V <= lambda d^2 (2v+d)^2` because each term `<= (lambda/4) d^2 (2v+d)^2` and there
are four terms: `V <= lambda d^2 (2v+d)^2`. Equality iff every `|t_i| = d` and every
`t_i = +d` (since `2v + t_i` is maximal at `t_i = +d`): `sigma_i = v + d` for all `i`.
*Lower (d <= v):* each term is `>= 0`; to minimize `sum_i (2v + t_i)^2 t_i^2` subject to
`max_i |t_i| = d`, put `|t_i| = d` on exactly one index with `t = -d` (minimizing
`(2v + t)^2` at fixed `|t|`) and `t_i = 0` elsewhere, giving
`V >= (lambda/4) d^2 (2v - d)^2`. This is attained at `sigma = (v-d, v, v, v)`.
(For fixed `|t|`, `(2v+t)^2 t^2` is increasing in `|t|` on `[0, v]` and minimized at
`t = -|t|`, so concentrating the deviation on one singular value is optimal; moving
mass between two nonzero `t_i` with `|t_i| < d` strictly decreases or increases nothing
at the constraint boundary - the two-point Lagrange check is in the numeric sweep N2/N3,
20000 + 20000 random draws, zero violations.)
*Sharpness:* attained points above; numerics N2 (0 violations / 20000 draws), N3
(both values hit exactly, 500 draws; no ball point exceeds the sup, 20000 draws).

### D3. Sublevel localization, threshold re-derivation, determinant bound

**Claim D3a.** For `0 < eps <= lambda v^4/4`, `V(Phi) <= eps` implies
`d(Phi) <= d_eps := v - sqrt(v^2 - 2 sqrt(eps/lambda))`.
*Proof.* The lower bound of D2 gives `(lambda/4) d^2 (2v - d)^2 <= eps`, i.e.
`d(2v - d) <= 2 sqrt(eps/lambda)`. The quadratic `f(d) = d(2v-d)` is strictly increasing
on `[0, v]` with `f(v) = v^2`, and `eps <= lambda v^4/4` is `2 sqrt(eps/lambda) <= v^2`,
so the smaller root `d_eps = v - sqrt(v^2 - 2 sqrt(eps/lambda))` of
`d(2v-d) = 2 sqrt(eps/lambda)` satisfies `d <= d_eps`. The branch `d > v` is excluded (Finding 2): `r > v`
forces some `sigma_i > 2v` (since `sigma_i >= 0`), hence
`V >= (lambda/4)(sigma_i^2 - v^2)^2 > (lambda/4)(3 v^2)^2 = 9 lambda v^4/4 >
lambda v^4/4 >= eps`, a contradiction. The root equation at `eps = lambda v^4/4`
gives `d_eps = v` exactly. The small-root selection is S1 (50 numeric points).
**Claim D3b (threshold as a distance statement).** `d(Phi) = v` is possible iff
`sigma_4 = 0` is reachable at that distance; the minimum of `V` over `{det Phi = 0}` is
attained at `sigma = (0, v, v, v)` with value `lambda v^4/4` (item 115, cited) and
equivalently `inf{ d : V < lambda v^4/4 fails somewhere below threshold } = v`: at
`eps = lambda v^4/4`, `d_eps = v`. So the ordinal-43 sharp threshold is exactly the
statement that the closed `v`-ball around `v U(4)` is the largest distance ball whose
complement contains all defect points - no numerical disagreement with 115, a
re-derivation from the distance geometry (recorded so the gatekeeper sees the
consistency, not a contradiction).
**Claim D3c (determinant bound).** For `d <= v`,
`|det e| = prod_i sigma_i / v^4 = prod_i (1 + t_i/v) >= (1 - d/v)^4`
(AM-GM-free: each factor `>= 1 - d/v`), with equality at `Phi = (v-d) U` (all
`t_i = -d`). Combined with D3a: `V <= eps` implies
`|det e| >= (1 - d_eps/v)^4 = (1 - sqrt(4 eps/lambda)/v^2)^2`, the last equality being
the symbolic identity N7 - identical to the integrated ordinal-43 bound. The distance
route reproduces, and geometrically explains, the manuscript's bound.

### D4. Sharp fluctuation radius

**Claim D4.** `sup{ V(Phi) : d(Phi) <= delta } = lambda delta^2 (2v + delta)^2`
(attained at `Phi = (v+delta) U`), and this is `< lambda v^4/4` iff
`delta (2v + delta) < v^2/2`, iff `delta < delta_* := (sqrt(6) - 2) v / 2`.
*Proof.* The sup over the ball is the sup over `|t_i| <= delta` of
`(lambda/4) sum_i (2v+t_i)^2 t_i^2`; each term is monotone in `|t_i|` on `[0, delta]`
(derivative `2 (2v+t_i) t_i (2v + 3 t_i) ... ` in `t_i >= 0` positive; negative-`t`
terms are smaller than their `+|t_i|` counterparts since `|2v - t| < 2v + t`), so the
sup is at all `t_i = +delta`. Setting `lambda delta^2 (2v+delta)^2 = lambda v^4/4` is
`delta(2v+delta) = v^2/2`, whose positive root is `(sqrt(6)-2) v/2` (S2, S3).
Recorded ratio `delta_*/v = 0.2247448713915889`; then `(1 - delta_*/v)^4 =
0.3612256587700821` is the uniform determinant floor on the ball (a number appearing
only in this package's recorded output, derived here - rule 7 satisfied).
*Sharpening note (why "if and only if" is exact, not a one-way estimate):* the ball of
radius `delta > delta_*` contains `Phi = (v + delta) U` with
`V = lambda delta^2 (2v+delta)^2 >= lambda v^4/4`, so no larger radius works for a
pointwise-below-threshold certificate by distance alone.
*Connection to recorded quadratic data (cited, not re-derived; edge 1(a) asked for it):*
along a single-direction fluctuation `sigma = (v + tau, v, v, v)`,
`V = (lambda/4)((v+tau)^2 - v^2)^2 = lambda v^2 tau^2 + O(tau^3)` (S4), matching the
manuscript's recorded Hessian scale `lambda v^2` (appH ~L2160-2168 mass-split paragraph:
`V^{(2)} = lambda v^2 Tr H^2`); the uniform radial direction carries `4 lambda v^2`,
and the recorded boost-direction datum `2 lambda v^4 t^2` (N8 coefficient check, from
the live `\(...\)\neq0` paragraph) sits between the two bracket values, as the two-sided
estimate of D2 requires. These are consistency checks between the new geometric bounds
and the recorded quadratic expansions; they do not re-derive the expansions.
*Scope (rule-3 boundary):* `delta_*` is a fluctuation-radius certificate in the
operator norm for the pointwise bound `V < lambda v^4/4`. It is **not** a spectral gap,
not a stability statement, and says nothing about the `eta`-contracted quadratic
diagnostic of appH L1166-1179, which is about a different (indefinite) function - the
locked kinetic block - as that passage records in the live wording (Finding 3):
"Because K is indefinite, this quadratic form is negative along the three 0i
self-adjoint directions for lambda > 0", and, verbatim there, "a quadratic diagnostic
about a stationary background and not a spectrum about a stable vacuum". The insert
says so in one clause.

### D5. Volume/small-measure realization (edge 1(b), positive)

**Claim D5.** Let `x -> Phi(x)` be any (measurable) field on a measure space `(R, mu)`
with `E_V := int_R V(Phi(x)) dmu(x) < oo`, and `e(x) := Phi(x)/v`. Then
(i) `{x : det e(x) = 0} subset {x : V(x) >= lambda v^4/4}` (D3b contrapositive: a
defect point has `d >= v` along the segment to `(0,v,v,v)`-type... precisely:
`sigma_4 = 0` forces `V >= lambda v^4/4` by the item-115 threshold);
(ii) Markov: `mu{ V >= lambda v^4/4 } <= 4 E_V / (lambda v^4)`;
(iii) for every `0 < eps < lambda v^4/4`, with
`c(eps) := (1 - sqrt(4 eps/lambda)/v^2)^2`,
`mu{ |det e| < c(eps) } <= mu{ V > eps } <= E_V / eps` (D3c contrapositive + Markov).
The exceptional set (where the bound or the non-vanishing may fail) has
`mu`-measure at most `4 E_V/(lambda v^4)` (at most `E_V/eps` for the refined set);
it is null when `E_V = 0` and is NOT null in general when `E_V > 0` (see the
optimality paragraph below).
*Proof.* (i) item-115 threshold; (ii) `(lambda v^4/4) mu{A} <= int_A V <= E_V` on
`A := {V >= lambda v^4/4}`; (iii) `{ |det e| < c(eps) } subset { V > eps }` is the
contrapositive of D3c, then Markov. Numerics N6: lattice check (0.05-fraction defect
patch: measured bad volume 0.050875 vs bound 0.057175 - bound satisfied, non-saturated
in the generic case) and **saturation** on the extremal configuration: a region of
measure `f` with `sigma = (0,v,v,v)` has `E_V = f lambda v^4/4` and `mu{det e = 0} = f
= 4 E_V/(lambda v^4)` exactly (four recorded equalities, `f = 0.01, 0.1, 0.37, 1.0`).
So the constant is best possible in this hypothesis class.
*Named classes (rule: name the class, do not pretend more).* A classical solution of
`eq:Phi-eom` on a spatial slice with finite potential energy `int V d^3x < oo` (e.g.
finite-energy textures/skyrmion-type configurations with `Phi -> v U(infty)` outside a
compact set; the vacua themselves: `E_V = 0`); a Euclidean path-integral history with
finite action obeys `int V dmu_E d^4x < oo` on `mu_E`-a.e. history whenever the weighted
measure exists, giving the weighted version `E_mu[ mu{det e = 0} ] <= 4 E_mu[S_E-vev
potential part]/(lambda v^4)` **conditionally on the measure being defined**, which it
is not (recorded below, not claimed). What is *unconditional* is the small-measure statement for
every configuration with finite `int V dmu` (a.e. only when `E_V = 0`): it is the
measure-theoretic shadow of the 115 threshold and it is realization-grade for the state
route inside Presentation B. *Optimality / honest limit (gatekeeper counterexample,
adopted, Finding 1):* the constant field `sigma = (0,v,v,v)` satisfies `eq:Phi-eom`
exactly (`D Phi = 0`, and `Phi(Phi^dag Phi - v^2 I) = W diag(sigma_i(sigma_i^2 - v^2))
Z^dag = 0` since every `sigma_i` lies in `{0, v}`), has `V = lambda v^4/4` and
`det e = 0` everywhere, and on a slice of measure `M` attains
`mu{det e = 0} = M = 4 E_V/(lambda v^4)`: the upper bound is optimal in `E_V` and no
a.e. statement can replace it when `E_V > 0`. This converts state construction into a
single consumable estimate: any candidate state/measure with `E_mu[V] <= f lambda
v^4/4` gives `mu{det e = 0} <= f`.

### D6. Why the bilocal-composite analogue (edge 1(c)) does not transfer

The Elitzur paragraph (live appH L1708) recasts `ass:nondeg` as non-degeneracy of a
two-point composite `C^{AB}(x,y) ~ <Phi^A(x) Phi^{B dagger}(y)>`-type object. The
pointwise machinery above bounds `det` of a one-point `Phi`. A composite's
non-degeneracy is a statement about a matrix of two-point functions whose singular
values are not controlled by pointwise `sigma_i(Phi(x))` alone (Schwinger-function
positivity constrains diagonals, not determinant non-vanishing of a smeared kernel;
no pointwise bound on `Phi` implies any bound on the composite's smallest singular
value without state input). Honest conclusion: **edge 1(c) is not derivable from this
package's hypotheses**; it remains open and depends on a state or on large-`N`/cluster
input. Recorded as the first avenue still open after this package (ranking below), not
as a no-go beyond its hypothesis class (pointwise-only tools).

### Edge (b) second variant and the Presentation-A note

The finite-energy classical-solution variant of edge 1(b) is subsumed by D5. The
Presentation-A selection of `eq:V` (ch03 `sec:ch3-relate` records it missing) and the
quantum stability of the strict orbit minimum (115 ranked avenue 4) are outside this
package; nothing here advances or contradicts them. Mission edge 2 (Presentation-A
selection presentation) was rejected because a restatement of the recorded gap is not
progress (brief); mission edge 3 (quantum/finite-`N` stability) was rejected as not
reachable at full rigor within the package boundary (it needs the measure, which is an
open item).

### Comparison with the original target

Original target (D1 frame clause): derive the locked frame's existence and
non-degeneracy from microscopic data, discharging `ass:frame-lock` and `ass:nondeg`.
This package derives, inside Presentation B: (i) the exact distance geometry of the
ordinal-43 bound; (ii) a sharp fluctuation domain realizing it; (iii) small-measure realization
by every finite-potential-energy configuration (`mu{det e = 0} <= 4 E_V/(lambda v^4)`,
null when `E_V = 0`, optimal by the constant `(0,v,v,v)` solution) with a saturated
volume bound. It does
not construct the matrix-theory state or measure, does not select `eq:V` from
Presentation A, does not derive the frame reading `eq:vev-is-frame`, and does not
discharge `ass:nondeg` (small-measure or otherwise): the target remains OPEN.

## Claim classification

| # | claim | tier |
|---|-------|------|
| C1 | `d(Phi) = min_U ||Phi - vU||_op = max_i abs(sigma_i - v)`, attained at polar factor; Frobenius analogue | established derivation (Weyl inequality + polar decomposition; numerics N1) |
| C2 | sharp two-sided estimate `(lambda/4) d^2 (2v-d)^2 <= V <= lambda d^2 (2v+d)^2` on `d<=v`, both sides attained | established derivation (elementary; N2/N3) |
| C3 | sublevel localization `V<=eps => d <= d_eps`; threshold as `d_eps = v` at `eps = lambda v^4/4` | established derivation (D3a; S1; consistent with integrated 115) |
| C4 | `abs(det e) >= (1-d/v)^4`; induced bound identical to integrated `(1 - sqrt(4eps/lambda)/v^2)^2` | established derivation + symbolic identity (N7) |
| C5 | `sup_{d<=delta} V = lambda delta^2 (2v+delta)^2`; below threshold iff `delta < delta_* = (sqrt6-2)v/2`; sharp | established derivation (D4; N5, S2, S3) |
| C6 | volume bounds (i)-(iii) incl. saturation on `(0,v,v,v)` patch | established derivation (Markov + 115 threshold; N6) |
| C7 | small-measure realization of `V < lambda v^4/4` and `det e != 0` by every finite-`int V dmu` configuration: exceptional set at most `4 E_V/(lambda v^4)`, null when `E_V = 0`, optimal by the constant `(0,v,v,v)` `eq:Phi-eom` solution | established measure bound + conditional application (hypotheses: Presentation B, `eq:V`, `eq:vev-is-frame` reading, finite potential energy; small-measure, not pointwise) |
| C8 | quadratic consistency with recorded `lambda v^2` / `2 lambda v^4` data | conditional/consistency (recorded data cited not re-derived; identities N8, S4) |
| C9 | Euclidean-weighted version `E[bad] <= 4 <V>_E/(lambda v^4)` | conditional on existence of the weighted measure (measure NOT constructed; unresolved item) |
| C10 | bilocal composite non-degeneracy | unresolved; explicitly NOT derived here (D6) |
| C11 | presentation: `eq:V` is the Presentation-B potential; its selection is missing | input from manuscript (ch03 `sec:ch3-relate`, cited) |
| C12 | `delta_*` is not a gap and the `eta`-contracted diagnostic is a different function | established reading of appH L1166-1179 + D4 scope |

## Proposed changes

### File: `chapters/appH-microscopic-proofs.tex` (one insertion; nothing else in the repository changes)

Passage anchor: the unique line (live L1713)

    \section{Problem E: signature}

Boundary quote (verified unique by search in the live tree, baseline sha1
`f7a415d4...`): the inserted paragraph lands between the existing blank line (L1712)
and this `\section` line; the paragraph immediately before the blank line is the
ordinal-43 paragraph ending with the verbatim boundary sentence "...and Problem~D
remains OPEN and PROGRAMME-CONDITIONAL." (live L1711). All existing text is kept;
this is a pure insertion of one labelled conditional paragraph at the end of the
Problem D section, next to the ordinal-43 paragraph it extends. The anchor `\section
{Problem E: signature}` occurs exactly once (grep: L1713). Splice rule: bytes
`insert-d1-state-nondeg.tex` (one CRLF-terminated line) followed by the anchor line,
i.e. `data.replace(ANCHOR, ins + ANCHOR, 1)` - the pre-existing blank L1712 supplies
the paragraph break before the insert; this is the same splice the ACCEPTED item 115
used (cert-r115p.py line 37).

What the insert does NOT touch: the ordinal-43 paragraph (L1711), the Elitzur/bilocal
paragraph (L1708), the Problem D ledger (L769-772), the D1 frame clause (L801-802),
ch17, ch03, ch04. No status, priority or completion label is altered anywhere. No
stale passages: no text elsewhere asserts that no configuration class realizes the
pointwise bound (the ordinal-43 scope sentence says the realization "is not derived",
which remains true beyond the small-measure finite-energy statement established
here; the new
paragraph is explicitly scoped so the two are consistent).

Payload file: `insert-d1-state-nondeg.tex` (sha1 `d99b67be680f3b727ab16367ea283680cd2d6269`,
3782 bytes, one line, CRLF-terminated, ASCII, control-byte scan recorded below).
Generated byte-exact by `gen_payload_116.py` (no heredoc). Content:

```latex
\emph{State-route realization of the pointwise bound.} Write \(r(\Phi):=\min_{U}\|\Phi-vU\|\) for the operator-norm distance from \(\Phi\) to the vacuum manifold \(v\,\mathrm U(4)\) of Equation~\eqref{eq:vacuum-manifold}, the minimum running over unitary \(U\). By the polar decomposition and Weyl's singular-value inequality, \(r=\max_i|\sigma_i-v|\) exactly, the minimum attained at the polar factor, and on \(r\le v\) the function~\eqref{eq:V} obeys the sharp two-sided estimate \((\lambda/4)\,r^2(2v-r)^2\le\mathcal V\le\lambda\,r^2(2v+r)^2\), the upper bound attained at the uniform radial deviation \(\Phi=(v+r)\,\Omega\) with \(\Omega\) unitary and the lower bound at singular values \((v-r,v,v,v)\). Hence \(\mathcal V\le\varepsilon\le\lambda v^4/4\) forces \(r\le r_\varepsilon:=v-\sqrt{v^2-2\sqrt{\varepsilon/\lambda}}\), which equals \(v\) at \(\varepsilon=\lambda v^4/4\) and re-derives the threshold \(\inf\{\mathcal V:\det\Phi=0\}=\lambda v^4/4\) as the statement that defect points lie at distance at least \(v\) from the vacuum manifold, equality being attained at \((0,v,v,v)\), and it gives \(|\det e|\ge(1-r/v)^4\ge(1-r_\varepsilon/v)^4\), the last factor equal to the recorded \((1-\sqrt{4\varepsilon/\lambda}/v^2)^2\). Moreover \(\sup\{\mathcal V:r\le\delta\}=\lambda\,\delta^2(2v+\delta)^2\), attained at uniform radial deviation, and this is below the defect threshold if and only if \(\delta<\delta_*:=(\sqrt{6}-2)\,v/2\), with equality of the supremum and the threshold at \(\delta=\delta_*\); consequently every configuration field with \(\sup_x r(\Phi(x))<\delta_*\) realizes the pointwise bound \(\mathcal V<\lambda v^4/4\) everywhere, with \(|\det e|\ge(1-\delta/v)^4\). In measure form, for any field on any measure space with \(E_{\mathcal V}:=\int\mathcal V\,d\mu<\infty\), Markov's inequality and the threshold give \(\mu\{x:\det e(x)=0\}\le\mu\{\mathcal V\ge\lambda v^4/4\}\le 4E_{\mathcal V}/(\lambda v^4)\), attained as an identity on any region where the singular values are \((0,v,v,v)\), and \(\mu\{|\det e|<(1-\sqrt{4\varepsilon/\lambda}/v^2)^2\}\le E_{\mathcal V}/\varepsilon\) for every \(0<\varepsilon<\lambda v^4/4\); consequently the sets \(\{\mathcal V\ge\lambda v^4/4\}\) and \(\{x:\det e(x)=0\}\) have \(\mu\)-measure at most \(4E_{\mathcal V}/(\lambda v^4)\), and every configuration of finite potential energy, in particular every finite-potential-energy classical solution of Equation~\eqref{eq:Phi-eom} on a slice, realizes \(\mathcal V<\lambda v^4/4\) and the non-vanishing determinant of Assumption~\ref{ass:nondeg} off a set of at most that measure, which is null when \(E_{\mathcal V}=0\) and cannot in general be improved, saturation being attained on a region where the singular values are \((0,v,v,v)\). Scope: these are geometric statements about configurations of the displayed Presentation-B potential read through Equation~\eqref{eq:vev-is-frame}; the radius \(\delta_*\) is a fluctuation certificate and not a spectral gap, and it bounds neither the indefinite \(\eta\)-contracted quadratic diagnostic recorded above for the locked block nor the quantum stability of the minimum; no state of the matrix theory and no integration measure is constructed; the bilocal composite reading above is not covered, because pointwise singular-value bounds do not control the smallest singular value of a two-point kernel; the small-measure exception obtained when \(E_{\mathcal V}>0\) is a fortiori not the pointwise statement of Assumption~\ref{ass:nondeg} and does not discharge it; the selection of Equation~\eqref{eq:V} by Presentation~A remains the missing input of Section~\ref{sec:ch3-relate}; and Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg} remain assumed, so Problem~D remains OPEN and PROGRAMME-CONDITIONAL.
```

Reference/label verification (all checked unique in the live tree this round,
`grep -rn "label{...}" chapters/`): `eq:V` (ch03 L241), `eq:vacuum-manifold`
(ch03 L248), `eq:Phi-eom` (ch03 L310), `sec:ch3-relate` (ch03 L335, a `\section` so
`Section~\ref` is correct), `eq:vev-is-frame` (ch04 L91), `ass:frame-lock` (ch03
L265), `ass:nondeg` (ch04 L171). No new labels are introduced by the insert (no
`\label` in the payload). The two-pass compile certificate resolved all of them:
`undefrefs_pass2=0` and `undefrefs-touching-package-labels=0`.

Byte discipline (recorded by `gen_payload_116.py` output):
`bytes 3782 CR 1 LF 1 CRLF 1 loneCR 0 loneLF 0 badC0 0 tab 0 backslash+ws 0
nonascii 0 endsCRLF True` plus `PAYLOAD SCAN OK`.

### File: no other manuscript file changes

ch17, ch03, ch04, bib: unchanged. No BibTeX entries are needed (the insert cites no
new work; Weyl's inequality and the polar decomposition are cited by name in the
proposal text, and the insert itself names them without a citation, as appH L1711
does for its sum-of-squares step).

## Verification scripts (reproduction pack)

All files in `proposals/116-d1-state-nondeg-realization/`. Re-run commands are
executed from that folder; interpreter: the repo's `python` (CPython 3.x with numpy,
sympy), flag `-I -B`.

| script | sha1 | bytes | command | expected invariant output |
|---|---|---|---|---|
| `verify_r116.py` | `a232e6a185574d4c27de154621ae5eec202df7dc` | 12086 | `python -I -B verify_r116.py` | last lines `PASS 29 FAIL 0` and `ALL CHECKS DONE 116`; exit 0; seed 116 (deterministic) |
| `gen_payload_116.py` | `54b64f4c7d7b25438c35a0d31440e229a605fa5a` | 6101 | `python -I -B gen_payload_116.py` | `bytes 3782 CR 1 LF 1 CRLF 1 loneCR 0 loneLF 0 badC0 0 tab 0 backslash+ws 0 nonascii 0 endsCRLF True` then `PAYLOAD SCAN OK`; regenerates `insert-d1-state-nondeg.tex` byte-identically |
| `cert-r116p.py` | `ea4eef9764ae62c5eee22a11eae9423cbae97cf7` | 3484 | `python -I -B cert-r116p.py` | `rc1=0 rc2=0 errlines=0 outw=True undefrefs_pass2=0`, `undefrefs-touching-package-labels=0`, `CERT PASS`; exit 0 (two pdflatex passes on a temp copy OUTSIDE the repo incl. untracked `namcg-book7.bbl`; asserts anchor uniqueness; Finding 5 makes both reference counters hard assertions before `CERT PASS`) |

Recorded outputs: `out-r116.txt` (sha1 `5dcec29ea733a69f8bcf72d960062de50fc38d96`,
2420 B; PASS 29 FAIL 0) and `out-cert-r116p.txt` (sha1 `bb6d6c7fbeaf80e4db145716e00ab15ecbeb7850`,
158 B). What each `verify_r116.py` block checks maps to the derivation labels of the
"Research and reasoning" section: N1 -> D1a (polar attains; Weyl lower bound; Frobenius
analogue), N2/N3 -> D2 (estimate + attainment + no ball point exceeds sup), N4 -> D3a
(localization at 5 epsilon values, 5000 accepted draws each), N5 -> D4 (equality at
`delta_*`, sharpness, all ball points below threshold), N6 -> D5 (Markov volume bound,
containment of the defect set, four exact equalities for the `(0,v,v,v)` patch,
refinement over 20 epsilons), N7/S1/S2/S3/S4 -> the symbolic identities of D3c/D3a/D4
and the quadratic consistency S4, N8 -> the bracket consistency with the recorded
`2 lambda v^4` boost coefficient and the exact `lambda v^2` / `4 lambda v^2` quadratic
identities. Recorded numerical constants (traceable per rule 7 - all derived here,
none imported): `delta_*/v = 0.2247448713915889`, `(1-delta_*/v)^4 = 0.3612256587700821`,
lattice bad volume `0.050875` vs bound `0.057175`, `d_eps(eps=5.1, v=2, lambda=1.3) =
1.803408`-type lines in `out-r116.txt`; manuscript-traced constants `lambda v^4/4`,
`2 lambda v^4`, `lambda v^2` are quoted with appH line references. Tool output is a
check, not a proof; the proofs are in D1-D5.

## Decisions Taken

1. **Edge choice: 1(a)+1(b) combined (sharp fluctuation domain + finite-potential-energy
   small-measure/volume realization).** Chosen because both rest on one derivation (the sharp
   two-sided distance estimate), and their union is the strongest positive output for
   the named missing step reachable at full rigor in Presentation B; bundling is
   justified by the shared derivation. Rejected: 1(c) bilocal composite - checked, it
   does not follow from pointwise tools (D6), recording the reason instead of forcing a
   claim; 2 Presentation-A selection - a restatement of the recorded ch03 gap would
   violate "no routine restatements" and could not be derived here; 3 quantum/finite-N
   stability - needs the not-constructed measure, outside the package's evidence
   boundary. (No RESEARCHER-DECISION flags outstanding.)
2. **Presentation-A selection was NOT re-stated as "progress"**; it is referenced in
   the insert's scope clause only (`Section~\ref{sec:ch3-relate}`), per the brief's
   warning that a vaguer restatement of the recorded gap is not progress.
3. **Distance symbol `r`** (not `d`, which the manuscript uses for the vierbein
   one-form and the differential; not `D`, the covariant derivative).
4. **Splice join: `ins + ANCHOR`** after the pre-existing blank L1712 (identical to the
   ACCEPTED 115 splice), so the insert is a new paragraph; rejected splicing with an
   extra blank line (would change the paragraph-break count the 115 review blessed).
5. **Two-pass certificate** (115's single pass left all references unresolved,
   `undefrefs=1526` noise): pass 2 resolves references, giving a real check that the
   insert's seven `\ref/\eqref` targets exist. Cost: one extra ~minute of compile.
   Rejected: adding `.aux` files to the copy (stale aux from a non-spliced tree can
   mis-resolve page numbers without proving the pass-2 property used here).
6. **Consistency (not duplication) with ordinal 43 made explicit**: the package shows
   the distance-route bound equals the integrated `(1 - sqrt(4 eps/lambda)/v^2)^2` and
   re-derives the `lambda v^4/4` threshold geometrically; the existing text is kept
   untouched.

## Milestone assessment

Routine for milestone triggers as such, but a substantive advance: no MILESTONE.md
trigger is claimed (no critical-path problem is closed; no new status word). If the
gatekeeper maintains a "first positive realization-grade input for a named missing
step" note, this package qualifies for it: the ordinal-43 caveat "that the physical
state ... realizes the pointwise bound ... [is] not derived" now has a bounded
positive complement (small-measure realization - `mu{det e = 0} <=
4 E_V/(lambda v^4)`, null when `E_V = 0` - by every finite-potential-energy
configuration, and pointwise realization inside the sharp radius `delta_*`), with the
remainder of the caveat explicitly intact.

## Status-label recommendation

Current critical-path list re-derived from ch17 (live): A, B, C, D1, E, F, G-derived,
N (all CRITICAL PATH; OPEN) with D ledger PROGRAMME-CONDITIONAL as quoted. This
package changes no labels anywhere: D/D1/D2/E statuses, priorities and completion
classifications are exactly as quoted from the live tree. No label change is
recommended.

## Author decision needed

none.

## Remaining open step

To close the D1 frame clause as originally targeted (frame exists and is
non-degenerate on the claimed domain, derived from the same microscopic data):
(1) selection of `eq:V` by the matrix integral from Presentation A (ch03
`sec:ch3-relate`, missing); (2) construction of the physical state or measure of the
matrix theory and proof that it concentrates on configurations satisfying the
pointwise bound (this package gives the small-measure bound conditional on
finite potential energy of a configuration - `mu{det e = 0} <= 4 E_V/(lambda v^4)`, so
that construction of the state reduces to the single estimate `E_mu[V] <= f lambda
v^4/4 => mu{det e = 0} <= f` (gatekeeper ranking, review-r1 Scope) - and the weighted
path-integral form conditional on the measure's existence; neither is the construction); (3) non-degeneracy of the
bilocally framed composite under the Elitzur reading (appH L1708; not reachable from
pointwise bounds - needs state or clustering input, first-ranked avenue after this
package); (4) quantum stability of the strict orbit minimum (115 avenue 4, untouched).
Within the hypothesis class of this package, the open step it does resolve is: exhibit
a named class realizing the bound - resolved (sharp-radius domain `r < delta_*`
pointwise; all finite-`int V dmu` configurations off a set of measure at most
`4 E_V/(lambda v^4)`, null when `E_V = 0`).

## Special instructions for the gatekeeper

- Scope limits to enforce on the integrated paragraph: it is Presentation-B geometry
  for `eq:V` under `eq:vev-is-frame`; it must not be read as constructing the matrix
  state/measure, as selecting `eq:V` from Presentation A, as covering the bilocal
  composite, as a quantum stability or gap statement, or as discharging
  `ass:frame-lock`/`ass:nondeg` (a small-measure exception is not pointwise; the scope sentence says all of
  this - verify it survived integration verbatim).
- Re-check first (cheap): the anchor uniqueness of `\section{Problem E: signature}`
  against the CURRENT tree at integration time (another chain may have moved it); the
  D2 estimate by hand (three lines: `(sigma_i^2-v^2)^2 = (2v+t_i)^2 t_i^2`,
  `|t_i| <= r`); the D4 equality `delta_*(2v+delta_*) = v^2/2` (S2); the N7 identity
  `(1-d_eps/v)^4 = (1-sqrt(4 eps/lambda)/v^2)^2`.
- Re-run the reproduction pack (three commands above) BEFORE the compile certificate;
  the certificate is the spliced-file compile (payload + CRLF + anchor, 115 pattern),
  run on a copy outside the repository - it must print `CERT PASS` with
  `undefrefs_pass2=0`.
- Verify byte discipline of `insert-d1-state-nondeg.tex` independently (the scan is in
  the gen output): 3782 bytes, single CRLF line, ASCII, no tab, no backslash-whitespace.
- What must NOT be asserted in review or integration: any change to D/D1/E status;
  that `ass:nondeg` is discharged or "nearly" so; that the finite-energy small-measure result
  holds pointwise or for the physical state (the state is not constructed; the constant
  `(0,v,v,v)` `eq:Phi-eom` solution shows the exceptional set need not be null for
  `E_V > 0`); that `delta_*` is a gap
  or bounds the eta-contracted indefinite diagnostic; that this closes 115's avenue
  (1) beyond the small-measure named class - pointwise realization by the physical state and
  the bilocal composite (avenue 2 there) remain open.
- The `2 lambda v^4` / `lambda v^2` numbers in N8/S4 are quoted from appH L2159-2168
  (live); if those lines moved at integration, re-anchor but do not re-derive - they
  are cited consistency data, and the insert itself quotes no numbers from them.


## Response to review-r1 (round 2)

Verdict addressed: ACCEPT WITH REQUIRED REVISIONS. The geometric core (Procrustes
identity, sharp two-sided estimate, `delta_*`, Markov bound + saturation) is unchanged.

- **Finding 1 (blocking) - addressed.** The false quantifier clause is gone from every
  artefact. The payload was regenerated through `gen_payload_116.py` with the
  gatekeeper's Corrected snippet applied VERBATIM (substring-identity check against
  `review-r1.md`: corrected clause and scope clause each present byte-for-byte; the
  strings "almost every point" and `\mu`-almost-every quantifier absent from the new
  payload bytes; `\checkmark` recorded in `r2-report.md`). The scope clause is the
  gatekeeper's ("the small-measure exception obtained when \(E_{\mathcal V}>0\) is a
  fortiori not the pointwise statement..."). All proposal-side echoes (Result item 3,
  bottom line, conversion statement, D5 claim/proof/unconditional paragraph, C7,
  comparison paragraph, stale-passages note, milestone note, remaining-open step,
  gatekeeper instructions) now state the measure-upper-bound with `null when
  \(E_{\mathcal V}=0\)` and non-improvability. The gatekeeper's counterexample - the
  constant `sigma = (0,v,v,v)` field as an exact `eq:Phi-eom` solution with
  `det e = 0` everywhere, finite energy on finite-measure slices, attaining
  `mu{det e = 0} = 4 E_V/(lambda v^4)` with equality - is adopted into the
  honest-limitations record (D5 optimality paragraph, Result item 3) and into the
  ranked-avenue statement (construction reduced to `E_mu[V] <= f lambda v^4/4`).
- **Minor 2 - addressed.** D3a now carries the two-line `d > v` exclusion (`r > v`
  forces some `sigma_i > 2v`, hence `V >= 9 lambda v^4/4 > lambda v^4/4 >= eps`).
- **Minor 3 - addressed.** The non-verbatim quote is replaced by the live appH wording
  ("Because K is indefinite, this quadratic form is negative along the three 0i
  self-adjoint directions for lambda > 0"); the one clause that IS verbatim there is
  kept quoted.
- **Minor 4 - addressed.** Line pointers corrected: ch17 DERIVED criterion at live
  L57-59; appH note at live L698-701.
- **Minor 5 - addressed.** `cert-r116p.py` now hard-asserts `undefrefs_pass2 == 0` and
  zero package-label undefined refs BEFORE writing `CERT PASS`; the certificate was
  re-run fresh (two passes) and `out-cert-r116p.txt` re-recorded.
- **Finding 6 - addressed.** The payload now reads "attained as an identity on any
  region where the singular values are \((0,v,v,v)\)" (part of the verbatim corrected
  block).
- **verify pack:** `verify_r116.py` unchanged (grep: no check text echoed the false
  quantifier); fresh rerun prints `PASS 29 FAIL 0` / `ALL CHECKS DONE 116`.

## Decisions Taken (round 2)

- Adopted the gatekeeper's corrected quantifier and counterexample verbatim rather
  than re-deriving an independent wording (maximizes verifiability; the mathematics
  was re-checked by hand: `W diag(sigma_i(sigma_i^2 - v^2)) Z^dag = 0` for
  `sigma_i in {0, v}` and `D Phi = 0` for a constant field, so the counterexample is
  an exact solution, and equality in the Markov chain holds on the `(0,v,v,v)` region).
  This strengthens rather than weakens the package: the bound is now recorded as
  optimal, and state construction is reduced to one consumable estimate
  (`E_mu[V] <= f lambda v^4/4 => mu{det e = 0} <= f`), which is the derivation-first
  ranking for the next package.
- Kept `verify_r116.py` at round 1 (procedure condition: rerun unchanged unless a
  check echoed the false quantifier; it did not - grep evidence in `r2-report.md`),
  preserving the accepted `PASS 29 FAIL 0` record.
- Recorded the round-1 payload `daa9d33f29414c0aa856af37314fe8981f2d8bc7` (3473 B) as
  SUPERSEDED by `d99b67be680f3b727ab16367ea283680cd2d6269` (3782 B); the canonical POST
  size must be recomputed by the integrator from the NEW payload (arithmetic pointer
  only: 830881 + 3782 = 834663 if the tree is unchanged; not pinned).
- Rejected alternatives: (a) keeping "a.e." with a caveat - rejected, the quantifier
  itself is the error; (b) weakening to `E_V = 0`-only statements - rejected, the
  Markov bound for `E_V > 0` is exactly the positive realization-grade input the state
  route consumes; (c) hand-editing the payload - forbidden by byte discipline, the
  generator is the single source.
