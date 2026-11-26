# -*- coding: utf-8 -*-
"""Batch 1 reconciliation edits to proposal-r1.md (run with python -I)."""
p = "proposal-r1.md"
s = open(p, encoding="utf-8").read()
n = 0


def rep(old, new):
    global s, n
    assert s.count(old) == 1, ("COUNT", s.count(old), old[:60])
    s = s.replace(old, new)
    n += 1


# A) header note
rep("""- New script added by this round: `check_bilocal.py` (written to a new filename; it imports the
  surviving core). It passes on first run (see Reproduction pack).""",
"""- New script added by this round: `check_bilocal.py` (new filename; depends only on `sympy`
  and `numpy` - no intra-folder import - so it runs with plain `python -I check_bilocal.py`).
  Final version passes with deterministic output (saved `check_bilocal.out`). Getting there
  corrected three initial claims of this draft, now fixed in place throughout: the endpoint
  invariance check is a FACTORED residual (the kernel does not form a closed loop
  `U(x,y) U(y,x)`), the right-stabilizer statement is the right `O(G0)` action (not right
  unitary, which holds instead for the `X X^H` model composite, K3b), and the plaquette
  commutator enters with the transport-convention sign `sigma = -1` for `U' = +w U` on
  columns (d-part sign checked Abelian-first).""")

# B) Result item 3
rep("""3. **(New this round, CAS-checked.)** The bilocal itself: `G_{mu nu}(x, x+ell)` is invariant under
   the local Lorentz rotation at both endpoints and independent of the transport path through
   second order in `ell` to the extent that the failure is the curvature of the transported
   connection (checks K4a-e: exact endpoint invariance at finite group elements via the closed
   loop; O(ell^3) coincidence-expansion coefficients; symmetric O(ell^2) coefficient equal to the
   covariant derivative of the composite metric; curvature obstruction of path-independence
   exactly `1/6 (R(x+ell).G0 - G0.R(x))` with `R` antisymmetric). Consequence recorded (K4c/K4h):
   in the background-field split where the fluctuation has no singlet and no antisymmetric part,
   the O(ell) coefficient vanishes and the bilocal reads as `G0 + 1/2 ell^mu ell^nu` times the
   covariant second moment, with the frame appearing as the "square root" only modulo the right
   stabilizer (K4h) - the bilocal frame is a frame field (the `e`-orbit), not a fixed section.""",
"""3. **(New this round, CAS-checked; `check_bilocal.py`.)** The bilocal itself: the residual of
   the endpoint gauge substitution in the kernel `Psi^T eta U Phi` factors EXACTLY as
   `Psi^T (L^T eta L - eta) U Phi` (the `y`-endpoint pair `Lambda_y^{-1} Lambda_y` cancels
   between `U` and `Phi`), and the factor vanishes through `O(th^3)` at the finite
   truncated-exponential group element (K4a/K4b, exact symbols; the six `so(3,1)` generators
   are eta-antisymmetric, K4z); `U(x,x) = 1` and `G(x,x) = v^{-2} Psi^T eta Phi` (K4i); the
   connector series of `eq:bilocal-frame-op` coincides with the exact series solution of the
   transport ODE through `O(ell^2)` - the numerical gap under `e -> e/2` scales as `e^3`
   (ratio 8.0; K4c1, scaling-certified, no hand-tuned tolerance); path dependence of the
   two-point transport begins at `O(ell^2)` and its coefficient is the curvature-type
   expression `d_1 w_2 - d_2 w_1 + sigma [w_1, w_2]` of the connector - best `(sign, sigma)`
   error scaling as `e^3` (ratio 8.1) against a loop defect scaling as `e^2` (ratio 4.0;
   K4c2; observed `sigma = -1` fixes the holonomy convention for `U' = +w U` acting on
   columns); and the coincidence composite fixes the frame only up to a right `O(G0)`
   stabilizer (exact nontrivial element, K4h) - the bilocal gives the metric and a frame
   orbit, not a fixed section.""")

# C) expansion sketch + K4 paragraph
rep("""    the eta-symmetric soldering correction first appears at O(ell^2) (K1e), and its projection
    onto G_{(mu nu)} is `nabla_{(mu} g_{nu)lambda}` at that order when the background is
    connection-compatible (K4e).

Checks K4a-d, K4g in `check_bilocal.py` (new this round) establish, exactly (finite group
elements, exact rationals/symbols): `G_{mu nu}(x, x+ell)` is invariant under independent local
Lorentz rotations at `x` and `x+ell` at every order through O(ell^2) (closed-loop argument made
explicit: `Phi^T eta Phi` at one point is `Lambda^T (Phi^T eta Phi) Lambda`-covariant and the
loop `U(x,y)U(y,x) = 1` closes it); the coefficients match the coincidence expansion of
`G0(x) + (1/2)(d^2 G0) ell ell + ell (dG0).w` with `w` eta-antisymmetric; path-independence fails
at O(ell^2) exactly by `1/6 (R(x+ell) G0 - G0 R(x))` with `R` the curvature 4-form in `so(3,1)`
(K4c) - the transport is well defined through the order used, and the ambiguity that remains is
precisely curvature, i.e. Riemann normal coordinates are the natural gauge of the operator.""",
"""    the eta-symmetric soldering-type contribution from the connector first appears at O(ell^2)
    (K1e); its closed form is not fixed by the checks of this round (only the order and the
    gauge/soldering split are used).

Checks K4z/K4b/K4a/K4i/K4c1/K4c2/K4h in `check_bilocal.py` (new this round) establish: endpoint
local-Lorentz invariance at finite group elements through O(th^3) - the substitution residual
factors exactly as `Psi^T (L^T eta L - eta) U Phi` and the `y`-endpoint factors cancel exactly
(K4a/K4b, exact symbols); the coincidence reduction `U(x,x) = 1`, `G(x,x) = Psi^T eta Phi`
(K4i, exact); the connector series equals the exact series solution of the transport ODE through
O(ell^2), certified by the cubic scaling of the gap under `e -> e/2` (K4c1, ratio 8.0); path
dependence of the two-point transport beginning at O(ell^2) with curvature-type coefficient
`d_1 w_2 - d_2 w_1 + sigma [w_1, w_2]` of the connector (K4c2: best `(sign, sigma)` error scales
as `e^3`, ratio 8.1, while the loop defect scales as `e^2`, ratio 4.0; observed `sigma = -1`
matches the holonomy convention of `U' = +w U` on columns, the d-part sign verified
Abelian-first) - the transport is well defined through the order used and the ambiguity that
remains is curvature-type, so a locally flat (Riemann-normal-type) frame is the natural gauge of
the operator; and an exact nontrivial right `O(G0)` element shows the composite fixes the frame
only up to the right stabilizer (K4h).""")

# D) stabilizer paragraph
rep("""rational trials). K3b/K4h: the composite is blind to right unitary recombination (`Y = X V`,
`Y Y^H = X X^H`, recovered factor unitary), so **the bilocal determines the frame modulo the
right stabilizer** - a frame-orbit (metric-plus-connection) datum, not a canonical section.""",
"""rational trials). Stabilizer structure - two distinct statements: K3b, the Hermitian model
composite `X X^H` is blind to right UNITARY recombination (`(XV)(XV)^H = X X^H`); K4h, the
bilocal coincidence composite `G0 = Phi^T eta Phi` is invariant under LEFT local Lorentz (the
gauge invariance of K4a/K4b), while a right recombination `Phi -> Phi C` sends
`G0 -> C^T G0 C`, so given `G0` the frame is fixed only up to the right action of `O(G0)`
(exact nontrivial element checked). So **the bilocal determines the metric and a frame orbit,
not a canonical section** - a frame-orbit (metric-plus-connection) datum.""")

# E) named hypothesis line
rep("""  connection content feeding `U_omega` (eq:dressed-omega is gauge-covariant by construction, but
  `omega` and `Lambda` are the D1 objects whose existence and dynamics D1 must derive); a
  background-compatible transport for reading the O(ell^2) block (K4e hypothesis).""",
"""  connection content feeding `U_omega` (eq:dressed-omega is gauge-covariant by construction, but
  `omega` and `Lambda` are the D1 objects whose existence and dynamics D1 must derive); that the
  connector `w` entering the transport series is the smooth-background value of eq:dressed-omega
  in the operator's domain `|ell| >> L_UV^{-1}`.""")

# F) classification
rep("""  `check_bilocal.py` (exact finite computations: characters, CG, word-algebra series identity,
  determinant identities, closed-loop invariance, curvature obstruction); the invariance of
  (blframe) under eq:Phi-transform and eq:llts (by construction, verified symbolically K4a-d,g);
  the linear-only scope of the recorded Repair-I obstruction.""",
"""  `check_bilocal.py` (exact finite computations: characters, CG, word-algebra series identity,
  determinant identities, factored endpoint-invariance residual, right-O(G0) stabilizer element);
  the order-scaling of the transport-series gap and of the plaquette curvature coefficient
  (K4c1/K4c2: numerical e-scaling ratios 8.0/8.1/4.0 - scaling evidence for the O(ell^2)
  curvature-type path dependence, with the exact word-algebra identity K1b carrying the
  symbolic content); the invariance of (blframe) under eq:Phi-transform and eq:llts (by
  construction, verified symbolically K4a/K4b); the linear-only scope of the recorded
  Repair-I obstruction.""")

rep("""  a definition within the locked sector); K4e soldering-block form (connection-compatibility
  hypothesis); "evasion" of the obstruction in the sense of nonvanishing intertwiner space for
  the source sector the composite occupies.""",
"""  a definition within the locked sector); that the curvature-type plaquette coefficient of
  K4c2 extends to the full curvature of eq:dressed-omega once its dynamics is derived (the
  check fixes the connector-level expression and its transport convention, nothing more);
  "evasion" of the obstruction in the sense of nonvanishing intertwiner space for
  the source sector the composite occupies.""")

open(p, "w", encoding="utf-8", newline="\n").write(s)
print("batch1 applied:", n)
