# Proposal 110-cd1-bilocal-coincidence-evaluation, round 2

## Result

Inside the posited locked sector (Assumption `ass:frame-lock`, polar data
`eq:polar` with SO(3,1)-valued coset factor and frame `eq:vev-is-frame`,
dressed connection `eq:dressed-omega` in the frame representation), the
bilocal composite `eq:bilocal-frame-op` of item 109 is evaluated
explicitly, and three previously uncomputed or only-asserted statements
become derived identities:

1. **Coincidence (dispatch (a)).** The coincidence value is exactly
   G_{mu nu}(x,x) = (1+sigma(x)/v)^2 * eta_{IJ} e^I_mu e^J_nu, i.e. the
   composite metric `eq:g-from-e` of the frame times the positive radial
   factor; the constant of proportionality is 1 at the vacuum sigma=0 and
   the coincidence at <e>=I is exactly eta. The internal coset phase drops
   out identically via Lambda^T eta Lambda = eta. Symbolic + numeric
   verification (`run_locked.out`).
2. **Path-curvature coefficient (dispatch (b)).** The O(ell^2)
   path-dependent (loop-minus-chord) transport coefficient is derived, in
   the ordering convention of `eq:bilocal-frame-expansion`, as
   (area) x F_{12} with F_{rho sigma} = d_rho w_sigma - d_sigma w_rho -
   [w_rho, w_sigma]: coefficient ab/2 for the L-shaped triangular loop and
   ab/6 for a parabolic arc (area between arc and chord ab/6), so the path
   dependence depends only on the enclosed oriented area. The commutator
   carries the MINUS sign in the printed (left-multiplication) ordering of
   `eq:bilocal-frame-expansion`; reversing the ordering side flips it, and
   the O(ell^2) coincidence series is insensitive to the ordering side at
   that order (symmetrization of ell^rho ell^sigma). This fixes the meaning
   of the drafted clause "sign fixed by the transport convention". The
   abelian subcase reduces to (area) x (d_1 w_2 - d_2 w_1) (`run_path.out`).
3. **Connector/soldering structure of the full composite.** For the full
   composite G in the locked subclass: the eta-symmetric part of the
   O(ell) coefficient contains no connector term (eta w_rho is antisymmetric);
   the connector contribution to the eta-symmetric part of the mixed
   second-ell coefficient at rho != sigma is exactly
   (1/2)(1+sigma/v)^2 * sym_{mu nu}(eta {w_rho, w_sigma}), generically
   nonzero, and nonzero even in the abelian single-generator subcase
   (boost instance); every derivative piece d_s w_r and the curvature-type
   piece eta F_{rs} are eta-antisymmetric, so O(ell^2) path dependence
   never enters the symmetric sector; the full symmetric O(ell^2) sector
   decomposes as (profile) + (radial e_rs) + (radial-gradient x e) +
   (mixed e-w) + the anticommutator connector
   (`run_induced.out`, corrected r2 identity in R6). The item-109 draft claims
   are confirmed and made explicit; no claim in them needed correction.
4. **Non-degeneracy (dispatch (c)).** det(E^T eta E) = det(eta) det(E)^2
   is verified; concrete data: det G = -1 for E=I, -44100 for
   E=diag(2,3,5,7), 0 for a rank-3 frame. The item-109 sentence "the
   composite determines the frame only modulo the right action of the
   orthogonal group of g+" is verified concretely: O = D^{-1} B D with a
   rational boost B preserves G = diag(-4,9,25,49) and (DO)^T eta (DO) = G
   with DO != D (`run_rightiso.out`); the right action of SO(eta) on
   spacetime indices is instead a pushforward and NOT an invariance
   (checked non-invariant). The equivalence of non-degeneracy with frame
   invertibility is a square-frame statement: with N=6 internal directions
   a rank-deficient locked block can give an invertible composite
   (scope note, not manuscript text).

All four items are algebraic evaluations within the posited locked-sector
hypotheses: **conditional results / derivation-grade inputs to
Missing-step (i)**, not closures. Problem C (and D, D1) stay exactly as
recorded: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Target and status

- Problem: Appendix H Problem C (conformal mode), section
  `sec:status-C` (appH L529). Ledger label verbatim (L532-533): "Status:
  OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
  Chapter 17 (ch17-agenda.tex L139-157): "Problem C: the conformal mode.
  CRITICAL PATH; OPEN."
- Original target (Missing step, appH L754): the gauge-fixed quadratic
  scalar operator on the locked vacuum in a constructed frame (kinetic
  coefficient, mixing with T_{mu nu}, non-minimal coupling, matter
  coupling, pole mass), with ass:gap-psi discharged; input (i) is "a
  frame".
- What this item is: an evaluation of the item-109 candidate composite
  inside the posited locked sector - a conditional input to input (i) of
  the Missing step. It derives no dynamics, does not discharge
  ass:frame-lock or ass:nondeg, does not define an action for G, and does
  not close C, D or D1. Classification: PROGRAMME-CONDITIONAL (unchanged);
  nothing is marked DERIVED beyond the explicitly scoped identities.
- Dependencies relied on: eq:Smicro, eq:VEV, ass:frame-lock (ch03 L254,
  L265), eq:Phi-transform (ch03 L280), eq:polar (ch04 L62-63),
  eq:vev-is-frame (ch04 L91), eq:g-from-e (ch04 L161), ass:nondeg
  (ch04 L171), eq:dressed-omega (ch10 L133), eq:bilocal-frame-op
  (appH L701), eq:bilocal-frame-expansion (appH L712), item-109 paragraph
  (appH L693-752). No dependency on Problem D/D1 outputs: the connection w
  is taken as the posited dressed connection, exactly as item 109 states
  ("it presupposes the connection content that the closure of Problem D1
  requires to be specified").

## Source reading

Digest status at r1 run start: `python scripts/make_digest.py --check`
printed "DIGEST STALE (head changed)"; at r2 run time it prints DIGEST
CURRENT (head 23266972cd07dd01497abe5e0962810fa059db63, dirty-chapters:
no). r2 required reading: review-r1.md (sha1
5fc150de1587cc15fbe4cba31d893169405ccd14), read in full; r2 adds no
manuscript reading beyond the count-only appH anchor re-verification.
Per protocol 3 the r1 digest was NOT relied on and I used live targeted reads (digest + targeted reads of live
files; no full scan claimed - none of the four conditions (a)-(d) applies
to this package: no definition, assumption, scope-statement or status
passage is changed). Files read live: appH-microscopic-proofs.tex L529-560
and L688-756 (Problem C ledger label, item-109 paragraph, Missing step);
ch03-matrix-action.tex L248-289 (eq:vacuum-manifold, eq:VEV,
ass:frame-lock, eq:Phi-transform); ch04-vierbein-emergence.tex L55-96
(eq:polar, eq:polar-deriv, eq:higgs-frame, eq:vev-is-frame) and labels at
L161, L171; ch10 label at L133; ch17-agenda.tex L139-157;
proposals/109-cd1-bilocal-frame-operator/ (review verdict context).

## Research and reasoning

Conventions. Metric signature (-,+,+,+); eta = diag(-1,1,1,1); matrices
below carry the internal index A as row and the spacetime index mu as
column, so the coincidence composite is G = v^-2 Phi^T eta Phi. The
transporter is realized by the left-multiplication ODE dV/ds = M(s) V,
M(s) = gamma'(s).w(gamma(s)), V(0) = I along gamma(s) = x + s ell; this is
the realization whose O(ell^2) series equals the printed
`eq:bilocal-frame-expansion` (check P1 below fixes this: it is the
ordering side that reproduces the printed product order w_rho w_sigma in
the coincidence series).

R1. Transport series (P1). With M(s) = ell^rho w_rho + s ell^rho ell^sigma
d_sigma w_rho, the ODE gives V_1(1) = ell^rho w_rho and V_2(1) =
(1/2)(ell^rho ell^sigma d_sigma w_rho + ell^rho ell^sigma w_rho w_sigma),
which reproduces `eq:bilocal-frame-expansion` exactly through O(ell^2) for
generic noncommuting 3x3 coefficient matrices. This re-derives the item-109
"exact identity of the truncated series" by the ODE (order-by-order)
method instead of the word-algebra method.

R2. Loop coefficient (P2, P2b, P3). Compare the L-shaped path
x -> x + eps a e_1 -> x + eps a e_1 + eps b e_2 with the chord x -> x +
eps(a e_1 + b e_2). The difference U_L - U_chord vanishes at O(eps) and at
O(eps^2) equals (ab/2) ((B_21 - B_12) - (C_1 C_2 - C_2 C_1)) = (ab/2)
F_12(0), where B_{rho mu} = d_mu w_rho(0), C_mu = w_mu(0), and
F_{rho sigma} = d_rho w_sigma - d_sigma w_rho - [w_rho, w_sigma]. For the
parabolic arc x = eps a s, y = eps b s^2 the O(eps^2) difference equals
(ab/6) F_12(0); ab/6 is the area between the parabola and its chord, while
the triangle has area ab/2 - the same F with different enclosed oriented
area, which is the area-law form of path dependence at this order. In
Einstein notation with A^{rho sigma} the oriented-area bivector of the
loop (A^{12} = area), the loop coefficient is A^{12} F_12 summed over
rho < sigma; e.g. A^{12} F_12 with A^{12} = ab/2 reproduces P2. The
commutator enters with a MINUS sign in this ordering; with the opposite
(path-anti-ordered, right-multiplication) realization the coincidence
series reads (1/2)(d_sigma w_rho + w_sigma w_rho) - indistinguishable at
O(ell^2) because ell^rho ell^sigma symmetrizes the product - and the loop
coefficient carries +[w_rho, w_sigma]. The ODE derivation thus makes the
109 clause "sign fixed by the transport convention" explicit: with the
series exactly as printed in `eq:bilocal-frame-expansion`, it is
F = dw - [w, w]. The abelian specialization C_2 = c_2 C_1, B_{rho mu} = b_{rho mu} C_1
(single generator with proportional derivative data; check P3) gives
(ab/2)(b_21 - b_12) C_1 = (ab/2)(d_1 w_2 - d_2 w_1), commutator gone.

R3. so(eta) structure (P4a, P4b). The explicit boost/rotation basis of
so(eta) = {X : X^T eta + eta X = 0} is eta-antisymmetric and closed under
commutators (checked entrywise for generic 12-parameter pairs). Hence
F_{rho sigma} is so(eta)-valued, eta F is antisymmetric in (mu,nu), and
the O(ell^2) path dependence is of pure connector type: it can never
contribute to the symmetric part of G. This is the structural reason the
item-109 separation "soldering first at O(ell^2) vs path dependence first
at O(ell^2)" is consistent rather than accidental.

R4. Coincidence (L1, L2, L2b, L2c, L3, L3b). With locked polar data
Phi^A_mu = (v+sigma)/v * (Lambda E)^A_mu (normalization as in eq:VEV,
Lambda SO(3,1)-valued per appH L549 and eq:polar after the base
identification of eq:vev-is-frame), L2 verifies
G(x,x) = ((v+sigma)/v)^2 E^T eta E exactly for generic symbolic E and a
symbolic boost*rotation Lambda; L2b: at sigma=0, G(x,x) = E^T eta E,
proportionality constant 1; L2c: exact numeric instance agrees; L3b: the
left internal action E -> Lambda E is invisible (local-Lorentz redundancy
of eq:g-from-e). At <e> = I (eq:VEV) this gives G(x,x) = eta at the vacuum
(L4a).

R5. Non-degeneracy and the right action (L3, L4, L6). L3:
det(E^T eta E) = det(eta) det(E)^2 symbolically. L4: det G = -1 (E=I),
det G = -44100 = -(2*3*5*7)^2 (E = diag(2,3,5,7)), det G = 0 for a rank-3
frame; so on square frames non-degeneracy of G(x,x) is equivalent to
invertibility of e, with no extra condition - Assumption ass:nondeg reads,
in this subclass, exactly as the 109 text says. L6 (check_right_isometry):
with E = D = diag(2,3,5,7), G = diag(-4,9,25,49) and the conjugated
rational boost O = D^{-1} B D satisfies O^T G O = G and (DO)^T eta (DO) =
G with DO != D: two distinct frames induce one composite, ambiguity = right
action of O(g+), matching the 109 sentence "modulo the right action of the
orthogonal group of g+". L6c: the same construction with a mis-centered
conjugation does not preserve G, so the ambiguity is O(g+)-specific.
L3c: by contrast the right action of SO(eta) on spacetime indices is NOT
an invariance of the composite (checked non-invariant) - the 109 sentence
is about O(g+), and this is the correct reading. Scope note (not
manuscript text): the det-equivalence is a square-frame statement; with
N = 6 internal rows and a 4x4 locked block of rank 3 the composite can be
invertible (L5: explicit 6x4 example, det G6 = 2 while det locked = 0).
The locked sector of eq:VEV identifies four internal directions, so this
does not affect any current claim; it records the hypothesis a future
N>4 statement would have to handle.

R6. Induced expansion of the full composite (I0-I7). At the locked frame
point e = I (so g+ = eta), G(ell) = f eta U E with f = (1+a)^2 + (1+a)
delta, a = sigma/v, U the truncated transport (eq:bilocal-frame-expansion)
and E the frame-profile expansion. I0 checks the product-rule
coefficients against direct substitution. Results: I1 G(0,0) = (1+a)^2
eta, vacuum eta (I1b); I2 sym(eta w_r) = 0 identically for general
so(eta)-valued w (no O(ell) soldering); I3 sym(eta d_s w_r) = 0; I4
sym(eta {w_r,w_s}) generically nonzero (entries printed), nonzero for the
explicit boost-rotator instance (I4b) and in the abelian single-generator
subcase (I4c, boost generator: sym(eta w^2) != 0); I5 the symmetric part
of the total O(ell) coefficient is (1+a) a_r eta + (1+a)^2 sym(eta e_r),
the second term being (1+a)^2/2 * d_r g+ (I5b) - profile and radial data
only; I7 the symmetric part of the mixed coefficient d_r d_s G|0 (r != s)
is exactly F_rs eta + F_0 sym(eta E_rs) + F_0 sym(eta(w_r e_s + w_s e_r))
+ sym(F_r eta w_s + F_s eta w_r) + sym(F_r eta e_s + F_s eta e_r)
+ F_0 (1/2) sym(eta {w_r,w_s}), with F_0 = (1+a)^2 = (1+sigma/v)^2
and F_r = (1+a) a_r, where a_r = partial_r(sigma/v)|0 is the linear
coefficient of delta; i.e. the connector-soldering term is exactly
(1/2)(1+sigma/v)^2 sym(eta {w_r,w_s})
(the printed claim "soldering-type connector first at O(ell^2)" with its
coefficient made explicit). Ground truth for I7 is direct
differentiation of G = f eta U E: the r1 exactly-list omitted the
term sym(F_r eta e_s + F_s eta e_r) and the battery targets G2 and
tgt7 omitted it too, so the r1 I7 check was tautological off-vacuum
(review-r1 finding 1 and its S1 ground-truth check); the corrected
identity above equals the direct-differentiation ground truth
exactly. The narrower claims pinned in the payload are unaffected:
the connector-quadratic part and the connector-free O(ell) sector
stand as printed. I6, I6b: sym(eta F_12) = 0, sym(eta d_1 w_1) =
0. All coefficient checks run at the coefficient level (product rule on
the three factors; I0 certifies equivalence with the direct expansion).

R7. Comparison with the original target. None of this is the Problem C
operator: no action, no quadratic fluctuation operator, no mixing, no
mass. What it does for Missing-step input (i) (a frame): within the
posited locked sector it shows the candidate composite (i) coincides with
the composite metric of the frame up to an exactly known positive factor
(vacuum factor 1), (ii) has a derived transport-induced expansion whose
soldering content is the connector anticommutator at O(ell^2), and (iii)
has a curvature-type path dependence that is structurally incapable of
contaminating the symmetric (metric) sector. Inputs (ii) G_eff and
(iii) constraint structure are untouched. Literature was not needed: no
external result is imported (all statements derive from repository data);
accordingly no citations are proposed and none are used.

## Claim classification

- Established derivation (identities, checked symbolically): R1 series
  reproduction; R2 loop coefficient and area law and ordering-sign
  statement; R3 so(eta) closure and eta-antisymmetry of F; R5 determinant
  identity, concrete determinants, O(g+) ambiguity example, SO(eta)
  non-invariance example, N=6 counter-scope example; R6 all coefficient
  identities I0-I7 with the general so(eta)-valued w and generic profile
  data.
- Conditional results (derived under explicitly posited locked-sector
  hypotheses): R4 coincidence identity (input: locked polar data
  Phi = (v+sigma) Lambda e with SO(3,1)-valued Lambda - the subclass used
  by the 109 text and appH L549; and the locked identification of
  eq:VEV); R6 (input: evaluation point e = I, w_r and d_s w_r
  so(eta)-valued per eq:dressed-omega, f/U/E forms).
- Phenomenological input / mechanism (unchanged from item 109): existence
  of the locked sector (ass:frame-lock), the dressed connection content
  (eq:dressed-omega; D1 input), invertibility (ass:nondeg), identification
  of G with the emergent metric (not claimed anywhere).
- Conjecture/mechanism (not established here): that the locked polar form
  and w arise from the bare matrix dynamics; that G satisfies an action.
- Unresolved steps (unchanged, Problem C): the quadratic scalar operator,
  kinetic coefficient, mixing, non-minimal and matter couplings, pole
  mass; ass:gap-psi discharge; Problem D1 connection specification;
  Problem D local Lorentz derivation.

## Proposed changes

### File chapters/appH-microscopic-proofs.tex (single insertion; one paragraph)

Anchor contract (byte-verified against the live file at splice time):
- HEAD anchor (41 chars; ASCII, so 41 bytes): `sign fixed by the transport convention). `
- TAIL anchor (66 chars; ASCII, so 66 bytes): `The representation content is admissible where the linear Repair~I`
  (r1 stated 43/81; corrected at r2 by python len on the anchor
  strings, review-r1 finding 2: bookkeeping only).
- Joined anchor HEAD+TAIL: occurrence count = 1 (re-verified at r2 by
  count-only python on the live appH: HEAD 1, TAIL 1, joined 1; the
  integrator asserts the counts, not the lengths). The block is
  inserted BETWEEN the two anchors; both
  anchors stay byte-identical, as does every other character of the file.
- The sentence carrying `(antisymmetric derivative of $w$ plus
  commutator, sign fixed by the transport convention)` is KEPT unchanged;
  the insertion only makes that clause explicit. All 109-paragraph
  sentences (coincidence term, connector claims, Hom dimensions,
  non-degeneracy sentence at L740-743) are KEPT; the new text refines them
  and corrects nothing.
- New label: `eq:bilocal-coinc-locked`. Pre-insertion occurrence count of
  this string in the repository: 0 (checked). Labels referenced by the
  insertion, all verified to exist exactly once: `eq:polar` (ch04:62),
  `eq:vev-is-frame` (ch04:91), `eq:g-from-e` (ch04:161),
  `eq:bilocal-frame-expansion` (appH:712), `eq:dressed-omega`
  (ch10:133). `ass:frame-lock`/`ass:nondeg` are referenced by
  surrounding text, not by the inserted block.
- Scope labels: the insertion changes no status, priority, completion
  classification, Chapter 17 scope line, or critical-path list.

Insert exactly this (file `insert-bilocal-coinc.tex`, sha1
2cca5842ace0c3a1e67e6712d2c521990023f508), as one in-paragraph insertion
(white space around the display as shown; integrate as flowing text):

```latex
Within the locked polar data $\Phi^{A}{}_{\mu}=(v+\sigma)\,\Lambda^{A}{}_{I}\,e^{I}{}_{\mu}$ of Equation~\eqref{eq:polar}, with $\mathrm{SO}(3,1)$-valued coset factor and frame $e^{I}{}_{\mu}$ of Equations~\eqref{eq:vev-is-frame} and~\eqref{eq:g-from-e}, this evaluation is explicit: the identity $\Lambda^{T}\eta\,\Lambda=\eta$ removes the coset phase from the coincidence composite, leaving
\begin{equation}
  \label{eq:bilocal-coinc-locked}
  \mathcal{G}_{\mu\nu}(x,x)
  =
  \Bigl(1+\frac{\sigma(x)}{v}\Bigr)^{2}\eta_{IJ}\,e^{I}{}_{\mu}(x)\,e^{J}{}_{\nu}(x),
\end{equation}
the composite metric~\eqref{eq:g-from-e} of the frame multiplied by the positive radial factor, with unit proportionality constant at the vacuum $\sigma=0$ and coincidence exactly $\eta$ at $\langle e\rangle=\mathbb I$. In the induced expansion of $\mathcal{G}_{\mu\nu}(x,x+\ell)$ the $\eta$-symmetric part of the $\mathcal{O}(\ell)$ coefficient contains no connector term, and the connector-quadratic part of the $\eta$-symmetric $\mathcal{O}(\ell^{2})$ coefficient $\partial_{\rho}\partial_{\sigma}\mathcal{G}|_{\ell=0}$ ($\rho\neq\sigma$) is $\tfrac{1}{2}(1+\sigma/v)^{2}\,\eta\{w_{\rho},w_{\sigma}\}$ symmetrized in $(\mu,\nu)$, which does not vanish even for an abelian $w$; the curvature-type path-dependent coefficient, in the transport ordering of Equation~\eqref{eq:bilocal-frame-expansion}, is the oriented area bivector of the loop contracted with $\mathcal{F}_{\rho\sigma}=\partial_{\rho}w_{\sigma}-\partial_{\sigma}w_{\rho}-[w_{\rho},w_{\sigma}]$ ($\tfrac{1}{2}ab$ for the triangle with legs $a$ and $b$, $\tfrac{1}{6}ab$ for the parabolic arc), an $\eta$-antisymmetric tensor whose commutator sign flips when the ordering side is reversed. These evaluations are algebraic identities within the posited locked sector with the dressed connection~\eqref{eq:dressed-omega} in the frame representation; they add no dynamical input, define no action or fluctuation operator for $\mathcal{G}$, and do not identify it with the emergent metric.
```

Stale passages elsewhere: none found. The Problem D / D1 entries and
sec:status-D describe the same composite qualitatively and remain
accurate; the ch17 Problem C passage (L139-157) is untouched. No bib
entries, no other files.

## Verification scripts (reproduction pack)

Environment: Python 3 + sympy 1.14.0; run with `python -I` from this
folder. All outputs are deterministic (no randomness in time; fixed
rational instances); re-runs verified byte-identical to the stored .out
files (cmp) on 2026-11-22; in r2 the induced battery was corrected per
review-r1 finding 1 and re-run (output byte-identical), the other
three batteries untouched.

1. `check_path_curvature.py` + `_part2.py` + `_part3.py` (R1-R3)
   Re-run: `python -I -c "exec(open('check_path_curvature.py').read()); exec(open('check_path_curvature_part2.py').read()); exec(open('check_path_curvature_part3.py').read())"`
   Expect: P1, P2, P2b, P3, P4a, P4b all PASS; lines
   `P2 eps^2 loop coeff = (ab/2)*((d1 w2 - d2 w1) - [w1,w2])`,
   `P2b parabolic eps^2 coeff = (ab/6)*loop form (area between parabola and chord)`,
   `LOOPCOEFF_over_halfab verified for L-path; parabolic = ab/6 area.`,
   final `ALL CHECKS PASS` (stored: `run_path.out`). Central invariants:
   order-eps path difference = 0; loop O(eps^2) coefficient = (ab/2) F_12
   with F_12 = B21 - B12 - [C1,C2]; abelian (ab/2)(b21-b12) C_1.
2. `check_locked_coincidence.py` (R4, R5 first half)
   Re-run: `python -I check_locked_coincidence.py`
   Expect L1-L5 all PASS, `det G6 = 2`, `det locked = 0`, final
   `ALL CHECKS PASS` (stored: `run_locked.out`). Central invariants:
   G(x,x) - (1+sigma/v)^2 E^T eta E = 0 (trigsimp entrywise + numeric);
   det(E^T eta E) + det(E)^2 = 0; det G(diag(2,3,5,7)) = -44100; rank-3
   det = 0; N=6 invertible composite over degenerate locked block.
3. `check_right_isometry.py` (R5 second half)
   Re-run: `python -I check_right_isometry.py`
   Expect L6a-L6c PASS, `O = [[5/4, 9/8, 0, 0], [1/2, 5/4, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]`,
   final `ALL CHECKS PASS` (stored: `run_rightiso.out`). Invariants:
   B^T eta B = eta; O^T G O = G with G = diag(-4,9,25,49);
   (DO)^T eta (DO) = G; DO != D; mis-centered conjugate fails.
4. `check_induced_expansion.py` + `_part2.py` + `_part3.py` (R6)
   Re-run: `python -I -c "exec(open('check_induced_expansion.py').read()); exec(open('check_induced_expansion_part2.py').read()); exec(open('check_induced_expansion_part3.py').read())"`
   Expect I0-I7 all PASS (stored: `run_induced.out`). Central invariants:
   G(0,0) = (1+a)^2 eta; sym(eta w_r) = 0; sym(eta d_s w_r) = 0;
   sym(eta{w1,w2}) nonzero (entries printed); sym(G1_r) target;
   sym(G2_rs) = profile + radial + (Fd1[r] eta Ed1[s] + Fd1[s] eta
   Ed1[r]) + mixed + (1/2) F0 sym(eta{w_r,w_s});
   sym(eta F_12) = 0. r2 correction: the r1 G2/tgt7 targets omitted
   the Fd1*eta*Ed1 terms (review-r1 finding 1); the corrected targets
   match the direct-differentiation ground truth (review-r1 S1) and
   the r2 re-run is byte-identical to the stored output, whose r1
   copy is kept as run_induced_r1_outdated.out.

Tool output is a check, not a proof; the derivations are R1-R6 above.
sha1 (2026-11-22):
- check_path_curvature.py 2145e16ee54b65532d86a97b9e9d7ca5d8d0d739
- check_path_curvature_part2.py 8aef4877dabeca9ebd836f928824e7e894ba4d8e
- check_path_curvature_part3.py 679a0dedbb477709bde4fb02c849a22cbf3cd4ac
- check_locked_coincidence.py c0f0bbda2de31a341db1cb62cf9262f565853c37
- check_right_isometry.py 5496fbc60d25074c1c31486d9dcbaefd5f1b6cb1
- check_induced_expansion.py 94184fd43019143ea3e3948d175acd06480d0d10
  (r2: G2 target corrected per review-r1 finding 1)
- check_induced_expansion_part2.py 8950ff462761c52febaafd3f261d2a743cb69e35
- check_induced_expansion_part3.py fb440b2bab67cce0b412fc33642d5eacb58a71d9
  (r2: tgt7 target corrected per review-r1 finding 1)
- run_path.out 7da3445d83f9d1f7d4a44333ba75b8191e72bd39
- run_locked.out 9177127be94e865d0e3ee6df40a5012178d4fcf8
- run_rightiso.out 23281c81dc8ed16678ca30508423b07c379f2069
- run_induced.out 32b3701886be98430b5430d00fc4f2c49163992a
- run_induced_r1_outdated.out 32b3701886be98430b5430d00fc4f2c49163992a
  (superseded r1 battery output, inert provenance; the r2 re-run of the
  corrected scripts is byte-identical because the added terms enter the
  check targets, not the printed PASS lines)
- insert-bilocal-coinc.tex 2cca5842ace0c3a1e67e6712d2c521990023f508

Compile cert: sandbox copy of the tracked tree (git ls-files | tar), the
insertion spliced into scratch/sb110b/chapters/appH-microscopic-proofs.tex
(anchor assert count = 1, byte delta +2036, CRLF preserved), repo
namcg-book7.bbl copied in, then two passes
`pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex`:
exit codes 0/0, `Output written on namcg-book7.pdf (434 pages, ...)`,
zero `Citation ... undefined`, no "Reference ... undefined" or
"multiply defined" lines, no `!` error lines. Sandbox deleted afterwards;
the working tree was not built and not modified.

## Decisions Taken

1. Sign convention fixed to the printed equation: the loop coefficient is
   reported as F = dw - [w,w] because P1 shows the printed
   `eq:bilocal-frame-expansion` product order is reproduced by the
   left-multiplication ODE; the alternative "standard" +[w,w] would
   silently contradict the printed coincidence series. The ordering
   sensitivity is stated in the inserted text instead of being hidden.
2. The soldering coefficient claim is phrased as the connector-quadratic
   part of the O(ell^2) symmetric coefficient (the full symmetric part
   also contains sigma-gradient x w, sigma-gradient x e and e x w
   cross terms; claiming more would be false off-vacuum). r1 listed
   only the first and third families; r2 restores the
   sigma-gradient x e family consistently in Result 3, R6 and the
   battery targets (review-r1 finding 1).
3. Non-degeneracy and N>4 scope facts were kept out of the manuscript:
   the 109 text already states the square-frame equivalence and the N=4
   locked identification of eq:VEV is the programme setting; only the
   proposal records the N=6 counter-scope example (avoids widening
   Chapter 17 scope or adding a caveat with no mission effect).
4. Right-action wording in the 109 text ("modulo the right action of the
   orthogonal group of g+") was found CORRECT after L6; the initial
   reading "right SO(eta) action" is wrong and is recorded as such so the
   integrator/gatekeeper does not "fix" a correct sentence.
5. The heavy full-polynomial expansion check was replaced by
   product-rule coefficient checks plus an independent substitution
   cross-check (I0): same content, reproducible in seconds.
6. No status/priority/completion edits; no new labels beyond
   eq:bilocal-coinc-locked; insertion is additive, so the package cannot
   create stale cross-references.

## r1 -> r2 changelog

Round 2 is a record-and-battery correction round on the gatekeeper
verdict ACCEPT WITH REQUIRED REVISIONS (review-r1.md). The physics of
the pinned payload was verified there and is unchanged; no manuscript
text differs from round 1. Changes, keyed to the review findings:

1. Finding 1 (major). R6/Result 3: the "exactly" I7 decomposition
   gains the term sym(F_r eta e_s + F_s eta e_r), with F_0 = (1+a)^2 =
   (1+sigma/v)^2 and F_r = (1+a) a_r, a_r = partial_r(sigma/v)|0; with
   this term the identity equals the direct-differentiation ground
   truth of G = f eta U E (review-r1 S1). Battery: G2 in
   check_induced_expansion.py and tgt7 in check_induced_expansion_part3.py
   gained the matching Fd1*eta*Ed1 terms (r1 omitted them on both sides,
   making the r1 I7 check tautological off-vacuum). run_induced.out
   re-run from the corrected scripts; its byte content is unchanged
   (the terms enter the check targets, not the printed lines), and the
   r1 output is archived as run_induced_r1_outdated.out (sha1
   32b3701886be98430b5430d00fc4f2c49163992a). The Decision 2
   cross-terms parenthetical is updated to match. The payload is
   byte-identical (sha1 2cca5842ace0c3a1e67e6712d2c521990023f508): it
   claims only the connector-quadratic part and the connector-free
   O(ell) sector, both unaffected by the correction.
2. Finding 2 (minor). Anchor contract: HEAD/TAIL lengths corrected to
   the measured 41/66 chars (r1 said 43/81); occurrence counts
   re-verified 1/1/1 on the live appH; the integrator contract (assert
   counts, not lengths) unchanged.
3. Finding 3 (minor). R2 body: the B-convention sentence now reads
   B_{rho mu} = d_mu w_rho(0), matching the script convention under
   which F_12 = B21 - B12 - [C1, C2].
4. Finding 4 (minor). Source reading records the r2 digest state
   DIGEST CURRENT (head 23266972cd07dd01497abe5e0962810fa059db63,
   dirty-chapters: no) and review-r1.md as required reading.

Result and claim classification are UNCHANGED: conditional
in-hypothesis evaluations / derivation-grade inputs to Problem C
Missing-step (i); nothing is closed (rule 3); no status, priority or
completion label is touched (rule 2); the payload, labels and
references are unchanged.

## Milestone assessment

Routine. No MILESTONE.md trigger: the package supplies conditional,
in-hypothesis evaluations to input (i) of Problem C's Missing step; it
closes no critical-path problem, discharges no assumption, and derives no
new dynamical object. It is not a no-go either: every dispatched subtask
returned positive derivation-grade data.

## Status-label recommendation

Derived from live sources (ch17 L139-157; appH L532-533): full-GR
critical-path set A, B, C, D1, E, F, G-derived, N; Problem C = OPEN /
CRITICAL PATH / PROGRAMME-CONDITIONAL. Proposed label changes: none. C,
D, D1 all remain OPEN; no completion-class change.

## Author decision needed

None. (All choices here change no label, scope line, or core assumption.)

## Remaining open step

To reach the 109 paragraph's own bar of "constructed frame composite with
dynamics", and Problem C input (i) as a DERIVED input, still needed:
(i) derivation of the locked polar data (or acceptance of it as stated
hypothesis), i.e. the content of ass:frame-lock from eq:Smicro; (ii) the
D1 specification of the connection w (here taken as given, as in item
109); (iii) an action / selection rule / fluctuation operator for G (not
defined by anything in this package); (iv) the full Problem C operator
chain (kinetic coefficient, mixing, non-minimal coupling, matter
coupling, pole mass, ass:gap-psi), plus inputs (ii) G_eff (Problem F) and
(iii) constraint structure. Natural next computations feeding (iii):
bilinear fluctuations of G about the locked sector (second variation of
the composite), and the O(ell^3) term of the transport series (path
dependence beyond area law).

## Special instructions for the gatekeeper

- Scope: this package must NOT be read as closing C, D or D1 or as
  making any part of the locked sector derived; classify R4/R6 as
  conditional, R1-R3/R5 as established identities.
- Re-check the sign claim of R2 directly with 2x2 matrices (cheapest
  re-derivation): V' = (eps C1 + eps^2 s(b B11))V on [0,1], then (C2-branch)
  segment, minus chord transport - the eps^2 coefficient must be
  (ab/2)(B21 - B12 - (C1C2 - C2C1)). If you use right ordering you must
  get +[w_1,w_2] while keeping the printed series: the ordering
  sensitivity is the point, not an error.
- Verify the insertion anchors (HEAD/TAIL, count 1) against the live
  appH before splicing (another chain may have moved the text); insert as
  flowing in-paragraph text (the display equation may be kept as-is);
  convert to CRLF.
- Confirm eq:bilocal-coinc-locked is still unused elsewhere at splice
  time; the compile cert was run on the tracked tree of 2026-11-22 (HEAD
  2326697, branch local/gpu) with exactly the fenced text.
- Do not import the N>4 example into manuscript text; it is scope
  bookkeeping only.
- The 109 sentence about the right action of the orthogonal group of g+
  is correct as printed (L6 verifies it); do not edit it.
- r2 addendum: the payload is unchanged (insert-bilocal-coinc.tex
  sha1 2cca5842ace0c3a1e67e6712d2c521990023f508, compile cert
  unchanged at that sha). Only check_induced_expansion.py (G2 gained
  + Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r]) and
  check_induced_expansion_part3.py (tgt7 gained the symmetrized same
  term) changed among the scripts; fix_batt.py in this folder
  reapplies exactly those two edits with count asserts. Verify the
  corrected I7 identity in R6 by direct differentiation of
  G = f eta U E, re-run the induced battery (expect ALL CHECKS
  PASS), and check the anchor counts (not lengths) on the live appH
  before splicing.
