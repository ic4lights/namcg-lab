# -*- coding: utf-8 -*-
"""Batch 2 reconciliation edits to proposal-r1.md (run with python -I)."""
p = "proposal-r1.md"
s = open(p, encoding="utf-8").read()
n = 0


def rep(old, new):
    global s, n
    assert s.count(old) == 1, ("COUNT", s.count(old), old[:60])
    s = s.replace(old, new)
    n += 1


# G) LaTeX expansion equation and following sentence
rep("""\\begin{equation}
  \\label{eq:bilocal-frame-expansion}
  \\mathcal G_{\\mu\\nu}(x,x+\\ell)
  =
  g^{+}_{\\mu\\nu}(x)
  +\\frac{\\ell^{\\rho}\\ell^{\\sigma}}{2}\\,D_{(\\rho}g^{+}_{\\sigma)\\mu\\nu}
  +\\frac{\\ell^{\\rho}}{6}\\bigl(R_{\\rho}{}^{\\lambda}(x)\\,g^{+}_{\\lambda\\mu\\nu}
   -g^{+}_{\\rho\\mu\\nu}R_{\\lambda}{}^{\\lambda}{}_{\\sigma}\\cdots\\bigr)_{\\text{higher}},
\\end{equation}
where $g^{+}_{\\mu\\nu}=v^{-2}\\eta_{AB}\\Phi^{A}{}_{\\mu}\\Phi^{B}{}_{\\nu}$ reduces at coincident
separation to the composite metric~\\eqref{eq:g-from-e} of the Repair~II
frame~\\eqref{eq:vev-is-frame}, $R$ is the curvature of the transported connection, and the
$\\mathcal O(\\ell)$ term of the unsymmetrized kernel is of pure-gauge type, proportional to the
$\\eta$-antisymmetric connector; an $\\eta$-symmetric (soldering-type) correction first appears at
$\\mathcal O(\\ell^{2})$.""",
"""\\begin{equation}
  \\label{eq:bilocal-frame-expansion}
  \\mathcal U(x,x+\\ell)
  =
  \\mathbb I+\\ell^{\\rho}w_{\\rho}
  +\\tfrac{1}{2}\\,\\ell^{\\rho}\\ell^{\\sigma}
   \\bigl(\\partial_{\\sigma}w_{\\rho}+w_{\\rho}w_{\\sigma}\\bigr)
  +\\mathcal O(|\\ell|^{3}),
\\end{equation}
the short-distance transport series of the kernel, in which $w_{\\rho}$ is the connection in the
frame representation (the dressed connection~\\eqref{eq:dressed-omega} in the vector
representation). Equation~\\eqref{eq:bilocal-frame-expansion} is an exact identity of the
truncated series through $\\mathcal O(\\ell^{2})$ (word-algebra check; coincidence with the exact
series solution of the transport equation through the same order checked numerically at cubic
scaling). In the induced expansion of $\\mathcal G_{\\mu\\nu}(x,x+\\ell)$ the coincidence term is
$g^{+}_{\\mu\\nu}=v^{-2}\\eta_{AB}\\Phi^{A}{}_{\\mu}\\Phi^{B}{}_{\\nu}$, the composite
metric~\\eqref{eq:g-from-e} of the Repair~II frame~\\eqref{eq:vev-is-frame}; the
$\\mathcal O(\\ell)$ connector contribution is of pure-gauge type, proportional to the
$\\eta$-antisymmetric $w_{\\rho}$; an $\\eta$-symmetric (soldering-type) connector contribution
first appears at $\\mathcal O(\\ell^{2})$; and the dependence of the kernel on the transport path
between $x$ and $y$ first appears at $\\mathcal O(\\ell^{2})$ with a curvature-type coefficient
(antisymmetric derivative of $w$ plus commutator, sign fixed by the transport convention).""")

# H) right stabilizer phrase in paragraph
rep("""determinant, and the composite determines the frame only modulo the right stabilizer, so on this
reading Assumption~\\ref{ass:nondeg} becomes a non-degeneracy statement about the two-point
composite.""",
"""determinant, and the composite determines the frame only modulo the right action of the
orthogonal group of $g^{+}$, so on this reading Assumption~\\ref{ass:nondeg} becomes a
non-degeneracy statement about the two-point composite.""")

# I) editorial note
rep("""Editorial note for the integrator (not manuscript text): equation
\\eqref{eq:bilocal-frame-expansion} as drafted carries an ellipsis term that the CAS result (K4c)
does not fully fix (the mixed-curvature higher-order remainder beyond the recorded O(ell^2)
piece); if the gatekeeper objects to the dotted term, the approved fallback is to replace the
curvature bracket in that line by a remainder `{}+O(|\\ell|^{3})` with the sentence "through
$\\mathcal O(\\ell^{2})$ the transport is path-independent up to curvature terms of the displayed
type", keeping everything else verbatim. All claims in the paragraph are supported by this
proposal; the O(ell^2) coefficient in \\eqref{eq:bilocal-frame-expansion} is the K4e conditional
form.""",
"""Editorial note for the integrator (not manuscript text): equation
\\eqref{eq:bilocal-frame-expansion} is the verified transport-series identity (exact word-algebra
identity K1b plus numerical cubic scaling of the gap against the exact series solution of the
transport equation, K4c1); the remainder $\\mathcal O(|\\ell|^{3})$ is the standard statement and
no unsupported higher-order term appears in the text (earlier drafts carried an unfounded
mixed-curvature bracket; it has been removed here). All claims in the paragraph are supported
by this proposal; the soldering statement is an order-and-split statement (K1d/K1e), not a
closed form.""")

# J) verification script item 4
rep("""4. `check_bilocal.py` (new this round; imports `bilocal_reps_core`) - the bilocal of
   Equation~\\eqref{eq:bilocal-frame-op} and its expansion: K4a exact endpoint invariance via the
   closed loop `G(x,y) G(y,x)`; K4b coincidence expansion through O(ell^3); K4c path-independence
   obstruction `= (1/6)(R(x+ell).G0 - G0.R(x))` with `R` antisymmetric (curvature of the
   connector); K4d coincidence of the two transport orderings at coincidence; K4e/K4f the
   symmetric O(ell^2) block equals `nabla_{(mu} g_{nu)rho}` under the connection-compatibility
   hypothesis (zero without it); K4g manifest (blframe)-form invariance under simultaneous
   Lorentz transformation and `eta`-conjugation of the kernel; K4h right-stabilizer action on the
   factorized coincidence kernel (frame orbit, not section).""",
"""4. `check_bilocal.py` (new this round; needs `sympy` and `numpy`) - the bilocal of
   Equation~\\eqref{eq:bilocal-frame-op}: K4z eta-antisymmetry of the six `so(3,1)` generators;
   K4b the finite truncated-exponential group element preserves `eta` through `O(th^4)` exactly;
   K4a the endpoint substitution residual of `Psi^T eta U Phi` factors through
   `L^T eta L - eta` (y endpoint cancels exactly) and the factor vanishes through `O(th^3)`;
   K4i coincidence reduction `U(x,x) = 1`, `G(x,x) = Psi^T eta Phi`; K4c1 connector series vs
   the exact series solution of the transport ODE (numerical gap scales as `e^3` under
   `e -> e/2`, ratio window [5.5, 10.5]); K4c2 plaquette - two L-path transporters between the
   same endpoints: loop defect scales as `e^2` (window [3, 5]) while the residual against
   `1 -/+ e^2 (d1 w2 - d2 w1 + sigma [w1, w2])` scales as `e^3` (window [5.5, 10.5]) over the
   sign/sigma choice (observed sigma = -1, convention `U' = +w U` on columns, d-part sign
   verified Abelian-first); K4h an exact nontrivial right `O(G0)` element exhibits the
   right-stabilizer ambiguity (frame orbit, not section). All assertions are made by
   scaling-ratio windows - no hand-tuned tolerances.""")

# K) reproduction pack
rep("""Reproduction pack (exact commands, from the proposal folder; PowerShell-safe form first):

```
powershell: python -I -c "import sys; sys.path.insert(0,'.');exec(open('check_reps.py').read())"
  -> last line: ALL CHECKS PASS (full output must equal check_reps.out)
powershell: python -I -c "import sys; sys.path.insert(0,'.');exec(open('check_connectors.py').read())"
  -> last line: ALL CHECKS PASS (full output must equal check_connectors.out)
powershell: python -I -c "import sys; sys.path.insert(0,'.');exec(open('check_bilocal.py').read())"
  -> last line: ALL CHECKS PASS
bash:       python -I -c "import sys; sys.path.insert(0,'.');exec(open('check_reps.py').read())"
            (same for the other two scripts)
```
Key invariants if diffing is inconvenient: `Hom(dOmega,V(x)V) = 0`; `Hom(W(x)W,Sym^2V) = 22`;
`Hom(W(x)W,V(x)V) = 42`; `dim(Sym^2V)^G = 1`; `K1b ... exactly through O(ell^2) = PASS`;
`K3a/K3b PASS`; `K4c path-independence obstruction = curvature term PASS`;
`K4h frame determined only up to right stabilizer PASS`. Dependencies: CPython 3 with only the
standard library (`fractions`, `itertools`, `random`, `sympy` for scripts 3-4). Verified with the
repository interpreter on 2026-11-21.""",
"""Reproduction pack (exact commands, from the proposal folder; PowerShell-safe form first):

```
powershell: python -I -c "import sys; sys.path.insert(0,'.');exec(open('check_reps.py').read())"
  -> last line: ALL CHECKS PASS (full output must equal check_reps.out)
powershell: python -I -c "import sys; sys.path.insert(0,'.');exec(open('check_connectors.py').read())"
  -> last line: ALL CHECKS PASS (full output must equal check_connectors.out)
powershell: python -I check_bilocal.py
  -> last line: ALL CHECKS PASS (output equals check_bilocal.out; deterministic across runs)
bash:       the same three commands (check_bilocal.py needs no sys.path insert - it has no
            intra-folder import; the other two do, because `python -I` removes the script
            directory from `sys.path` and they import `bilocal_reps_core`).
```
Key invariants if diffing is inconvenient: `Hom(dOmega,V(x)V) = 0`; `Hom(W(x)W,Sym^2V) = 22`;
`Hom(W(x)W,V(x)V) = 42`; `dim(Sym^2V)^G = 1`; `K1b ... exactly through O(ell^2) = PASS`;
`K3a/K3b PASS`; `K4b ... = O(th^4) exactly PASS`; `K4c1 ... ratio 8.0 PASS`;
`K4c2 ... ratio 8.1 ... ratio 4.0 PASS`; `K4h ... right O(g)-orbit PASS`. Dependencies:
CPython 3; `sympy` and `numpy` for scripts 3-4 (plus stdlib `fractions`, `itertools`,
`random`, `functools`). Verified with the repository interpreter on 2026-11-21.""")

# L) gatekeeper conditionality note
rep("""- Known conditionalities to keep visible: the O(ell^2) symmetric block (K4e) requires the
  connection-compatibility hypothesis; the curvature-path statement is O(ell^2)-exact, beyond
  that "higher" is not computed (see editorial fallback note); the internal-index contraction
  normalization is a choice; point-splitting below `L_UV^{-1}` is outside the operator's domain.""",
"""- Known conditionalities to keep visible: the curvature-path statement is connector-level at
  O(ell^2) with transport convention sigma = -1 (`U' = +w U` on columns) and numerical
  scaling-ratio evidence; nothing beyond that order is computed; the O(ell^2) soldering block
  is claimed as order-and-split only, not in closed form; the internal-index contraction
  normalization is a choice; point-splitting below `L_UV^{-1}` is outside the operator's domain.""")

open(p, "w", encoding="utf-8", newline="\n").write(s)
print("batch2 applied:", n)
