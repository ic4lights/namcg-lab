# Proposal 008-auto-target, round 2

## Changelog against r1
- F1 (major): the embedding reading is labelled an assumed dictionary outside the four-matrix class; K != c g^{-1} is stated as pointwise for every real Lorentzian g; the sentence implying that no eq:g-from-e metric exists is removed (G has that form for the Theta-coframe); the conclusion is scoped to the embedding reading. The review's corrected snippet is used.
- F2 (major): the linear-response conclusion uses the review's wording (tensor equation or any linear local relation; "conserved" means p^mu T_{mu nu} = 0; varying a^mu gives only the projected equations; an extra conserved stress is not excluded and would have to be derived). "Whatever the coefficients of an induced action" is deleted.
- F3: "codimension four ... lies in the set cut out by the relation" replaces "four conditions".
- F4: the N-1+4 >= 11 parenthetical is deleted from the manuscript text. N >= 8 appears only under "Decisions Taken" (the author has pre-approved emergence-preserving structural changes; it is not an author question).
- F5: ell defined; orthogonality made metric-explicit (nbar^T K p = 0); a o b := a b^T + b a^T; e_0 and J defined; vacuum statement gives the delta contraction and the real locked block; the 3-versus-7 count is marked a counting argument.
- F6: "rank five" now refers to the differential of Theta -> K for Theta != 0, Pf Theta = 0.
- All four scripts re-run: outputs identical to the saved r1 outputs (`r2_*.out.txt`). No computation changed.

## Result
Unchanged in substance. Target: discharge of `ass:emergent-op` (identification of the Presentation-A frame with <Phi>/v). It is **not** derived. Established: a bounded conditional obstruction with hypothesis class H_A: four Hermitian matrix coordinates; Poisson limit; matrix indices contracted with constant `eta = diag(-1,1,1,1)`; real nondegenerate `Theta`; `K = Theta^T eta Theta`, `G = K^{-1}`, `rho = 1/|Pf Theta|`, `g_rho = (rho K)^{-1}`; linear order about constant `Thetabar`, generic `p`.

Established inside H_A (exact algebra, sympy-checked):
1. Image of `Theta -> G`: `K eta = -N^2`, `N = Theta eta`; the image satisfies `(K eta)^2 - (1/2) tr(K eta) K eta - Pf^2 1 = 0`. The six-dimensional image has codimension four in the ten-dimensional space of metrics and lies in the set cut out by this relation (sufficiency of the relation is not claimed).
2. Rank six of `Theta -> G` at every `Theta` with `Pf != 0`. The differential of `Theta -> K` has rank five when `Theta != 0`, `Pf Theta = 0` (G is undefined there).
3. Linear response: three-dimensional image of `u -> (dG, d rho)`; amplitude `(Gu) o p + n o m`.
4. Dimension count: the linearised Einstein operator (indeed any linear local operator) maps the 3-dimensional mode space into at most a 3-dimensional subspace of the 6-dimensional space of sources with `p^mu T_{mu nu} = 0`. The tensor equation `E[h] = T` cannot hold for generic conserved `T` without an additional conserved stress. Varying `a^mu` gives only the projected equations.
5. `K != c g^{-1}` pointwise for every real Lorentzian `g`.
6. Tree-level quadratic action algebraic in `(dG, d rho)`.

Conditional: the vacuum-manifold mismatch (only if `e` is identified with `<Phi>/v`); the nonlinear 3-versus-7 count (counting argument).
Not established: `<Phi>/v` as coframe; any value or sign of `G_eff`; Presentation B with independent `Phi`; Moyal corrections; `T_ent`.

## Target and status
Problems A, D1, F (B, C by dependency). Appendix H: Status OPEN, Priority CRITICAL PATH (A: "for the matrix-derived label"), Completion PROGRAMME-CONDITIONAL. Chapter 17 lists A, B, C, D1, E, F, G-derived, N; no discrepancy. Original target (F): discharge `ass:emergent-op` or replace it by a derived ingredient. Not met. PROGRAMME-CONDITIONAL; a bounded conditional obstruction.

## Source reading
Digest + targeted reads (digest CURRENT). Not a full scan. No unreadable files. The proposal changes no definition, assumption, label or scope text.

## Research and reasoning
As r1: kernel argument in sl2+sl2; `dK = -[q o m_u + u o s]`, `dG = -G dK G`; Einstein-operator rank 3 versus 6 conserved sources (independently reproduced by the gatekeeper). Round-2 changes are in wording and scope. On F1: G itself has the form eq:g-from-e for the Theta-coframe `e`; what fails is the identification of G with a Phi-induced metric `Phi^T eta Phi`, meaningful only under an assumed embedding dictionary. On F2: the dimension count concerns any linear relation from the 3-dimensional mode space to the 6-dimensional conserved-source space, not the field equations of a particular induced action. No literature cited; none to verify.

## Claim classification
- Established (algebra, sympy / exact rational): items 1, 2, 3, 5, 6; item 4 at linear order about constant `Thetabar`, generic `p`.
- Conditional: vacuum-manifold mismatch; nonlinear 3-versus-7 counting argument.
- Conjecture / relaxation sketch (not in manuscript text): N >= 8 matrices with `Phi^I_mu = d_mu x^I`.
- Unresolved: `<Phi>/v` as coframe; `G_eff`.

## Proposed changes
File: `chapters/appH-microscopic-proofs.tex`. Insert one paragraph after the 005 paragraph. Anchor (occurs once, re-verified by `verify_anchors_labels.py`; immediately followed by `\section{Problem G: HBEV}`): "...do not apply; no linearized-diffeomorphism invariance is claimed. Problems~B, C, D and~F remain open." Nothing is replaced. Labels verified once each: `eq:O-eta`, `thm:Geff`, `ass:emergent-op`, `rem:ch3-moyal-check`, `rem:ch3-trace-quadratic`, `def:composite-metric`, `eq:g-from-e`, `eq:vev-is-frame`, `eq:V`, `ass:EE`. No new labels, no label changes.

```latex
\paragraph{Presentation~A in the Poisson limit: what four matrix coordinates can supply (conditional; not closure).}
Keep the setting of the preceding paragraph: four matrix coordinates, the Poisson limit, matrix indices contracted with \(\eta=\mathrm{diag}(-1,1,1,1)\), a real nondegenerate \(\Theta\), \(K^{\mu\nu}=\eta_{\alpha\beta}\Theta^{\alpha\mu}\Theta^{\beta\nu}\), \(G=K^{-1}\), \(\rho=1/|\operatorname{Pf}\Theta|\), \(g_\rho^{\mu\nu}=\rho K^{\mu\nu}\). Let \(N=\Theta\eta\in\mathfrak{so}(3,1)\) with electric and magnetic parts \(\mathbf E,\mathbf B\), so \(\operatorname{Pf}\Theta=\pm\mathbf E\cdot\mathbf B\). For vectors \(a,b\) write \(a\circ b:=ab^T+ba^T\).

\emph{Image of \(\Theta\mapsto G\).} The characteristic polynomial of \(N\) is \(z^4+(\mathbf B^2-\mathbf E^2)z^2-(\mathbf E\cdot\mathbf B)^2\), so \(K\eta=-N^2\) has two doubly degenerate eigenvalues and \((K\eta)^2-\tfrac12\operatorname{tr}(K\eta)\,K\eta-(\operatorname{Pf}\Theta)^2\,\mathbb I=0\). Hence the six-dimensional image has codimension four in the ten-dimensional space of metrics and lies in the set cut out by this relation. Decomposing \(N=(n_+,n_-)\) in \(\mathfrak{sl}_2\oplus\mathfrak{sl}_2\), \(N^2=(\nu_++\nu_-)\mathbb I+2\,n_+\otimes n_-\), and a kernel element of the differential of \(\Theta\mapsto K\) must satisfy \(\delta n_\pm=\mp\lambda n_\pm\) and \(\lambda(\nu_+-\nu_-)=0\); since \(\operatorname{Im}\nu_+=0\) only if \(\mathbf E\cdot\mathbf B=0\), the map \(\Theta\mapsto G\) has rank six at every \(\Theta\) with \(\operatorname{Pf}\Theta\neq0\). The differential of \(\Theta\mapsto K\) has rank five when \(\Theta\neq0\) and \(\operatorname{Pf}\Theta=0\) (symbolic and exact-rational checks).

\emph{Linear response.} Let \(\Theta=\bar\Theta+\epsilon T\), \(T^{\mu\nu}=\bar\Theta^{\mu\rho}\partial_\rho a^\nu-\bar\Theta^{\nu\rho}\partial_\rho a^\mu\), \(a^\mu=u^\mu\cos(p\cdot x)\), \(q=\bar\Theta p\). The amplitude of \(\sin(p\cdot x)\) in \(\delta G\) is \((\bar Gu)\circ p+n\circ m\), with \(n=\bar G\bar\Theta p\), \(m=\bar G\bar\Theta\eta u\), and \(\delta\ln\rho=p\cdot u\). For \(u\propto q\) one has \(T=0\) (the matrix gauge). The first term is a linearised diffeomorphism. Since \(n\) and \(p\) are covectors, orthogonality is taken with the metric \(\bar K\): \(n^T\bar Kp=0\), while \(n\) is not parallel to \(p\) for generic \(p\), so the second term is not a diffeomorphism. The images of \(u\mapsto(\delta G,\delta\rho)\) and \(u\mapsto(\delta g_\rho,\delta\rho)\) are three-dimensional. For generic \(p\) the linearised Einstein operator about the constant background has rank three on this image, and its image lies in the six-dimensional space of symmetric tensors with \(p^\mu T_{\mu\nu}=0\) (``conserved''; exact-rational check for \(G\) and for \(g_\rho\)). Hence the tensor equation \(\mathcal E[h]=T\), and any linear local relation between \((\delta G,\delta\rho)\) and \(T\), can hold only for \(T\) in a subspace of dimension at most three of the six-dimensional space of conserved sources; varying the four functions \(a^\mu\) gives only the projection of the equation onto that image. This does not exclude an additional conserved stress that absorbs the codimension; such a stress would have to be derived. As a counting argument (not a derived result), four coordinate functions minus one matrix gauge function leave three gauge-invariant functions, against \(10-4+1=7\) for a diffeomorphism-invariant theory of a metric and one scalar. The tree-level quadratic action of Remark~\ref{rem:ch3-trace-quadratic} is proportional to \(\int\rho\,\eta_{\mu\alpha}\eta_{\nu\beta}T^{\mu\nu}T^{\alpha\beta}\), algebraic in \((\delta G,\delta\rho)\); every term with derivatives of the metric perturbation is a loop term. Whether the algebraic term is cancelled is the content of Assumption~\ref{ass:EE} and is not decided here.

\emph{Metric seen by the operators.} Suppose, as an assumed dictionary not contained in the four-matrix class, that there are \(D\ge4\) coordinate matrices \(X^I\) with a Lorentzian \(\eta_{IJ}\), and put \(\Phi^I{}_\mu:=\partial_\mu x^I\), \(g:=\Phi^T\eta\Phi\). Then \(K=\theta^{T}g\,\theta\) exactly; for \(D=4\), \(x^I=y^I\) and \(g=\eta\). The relation \(K=c\,g^{-1}\), \(c\neq0\), would give \(N^2=-c\) with \(N=\theta g\in\mathfrak{so}(g)\), whose characteristic polynomial has constant term \(-(\mathbf E\cdot\mathbf B)^2\le0<c^2\); \(c=0\) contradicts invertibility. So, pointwise for any real Lorentzian \(g\), the operator metric \(G=K^{-1}\) is not \(g\); this extends Remark~\ref{rem:ch3-moyal-check}, and Assumption~\ref{ass:emergent-op} read with the metric of that embedding reading is not discharged. The metric \(G\) itself has the form~\eqref{eq:g-from-e} for the coframe of the preceding paragraph. Let \(\ell\) be the fixed length scale in \(\Theta/\ell^2\), and \(e=\eta^{-1}\hat\omega\) with \(\hat\omega=(\Theta/\ell^2)^{-1}\). If \(e\) is identified with \(\langle\Phi\rangle/v\) as in~\eqref{eq:vev-is-frame}, then, with the internal index contracted with \(\delta\) and the locked block real, \(e^Te=\mathbb I\) on the vacuum manifold of~\eqref{eq:V} holds iff \(\hat\omega^2=-\mathbb I\), i.e. \(J:=\hat\omega\) is an orthogonal complex structure. Then \(G=\mathbb I-2nn^T\) with \(n=-Je_0\), where \(e_0\) is the first basis vector, so \(n\) is a spatial unit vector, and only two of the six directions of \(\delta\Theta\) are tangent to that manifold.

This is a statement for four matrix coordinates, the Poisson limit, a constant \(\eta\), linear order about constant \(\bar\Theta\) and generic \(p\); it does not apply to an independent field \(\Phi\) of Presentation~B, to the embedding statement above beyond four coordinates, or to Moyal corrections. It does not derive \(\langle\Phi\rangle/v\) as a coframe and gives no value or sign of \(G_{\mathrm{eff}}\). Problem~F, and Problems~A, B, C and~D, remain open.
```

Stale passages elsewhere: none. The 005 sentence "At the sample points tested the map Theta -> G has rank six" remains true and is strengthened.

## Verification scripts
In `proposals/008-auto-target/`: `check_theta_image.py`, `check_linear_response.py`, `check_embedding_and_vacuum.py`, `verify_anchors_labels.py` (outputs `*.out.txt`; r2 re-runs saved as `r2_*.out.txt`, identical to the r1 outputs). They check: characteristic polynomial and image relation; rank 6; rank 5 at Pf = 0 (of the differential of Theta -> K); N^2 = -c minimisation; dG formula and d ln rho; u = q null; rank 3; Einstein rank 3 versus 6 for G and g_rho; K = theta^T g theta for D = 4, 6, 10; e^T e = 1 and G = 1 - 2nn^T; tangent count 2; anchor count 1 and labels. Rank samples and the minimisation are checks, not proofs.

## Decisions Taken
- The manuscript text stays scoped to the four-matrix obstruction (H_A), with the embedding dictionary labelled as assumed.
- N >= 8 (pre-approved by the author on 2026-10-14 for emergence-preserving structural changes; only status/priority/completion labels remain author-only): recorded here as the pre-approved next route, not in the 008 manuscript text and not as an author question. Counting: with N matrices the gauge-invariant data are N-4 embedding functions plus 3 for the closed 2-form, i.e. N-1; adding 4 diffeomorphism functions must reach the 11 functions of (G, rho), so N >= 8. This is a necessary heuristic count, not sufficient, not a theorem. Changing `def:matrix-coords` is a separate proposal and needs its own gatekeeper ACCEPT; spacetime stays emergent.
- Which next package: (1) N >= 8 with the dictionary `Phi^I_mu = d_mu x^I`, repeating the linear-response and Einstein-operator rank computation for N = 8 and 10. Reason: it is the only relaxation that directly removes both the 3-versus-7 field-content deficit and the K != c g^{-1} identification obstruction, it is testable with the machinery already in hand, and it needs no new stress to be derived. (2) A derived extra conserved stress such as `T_ent` (could absorb the codimension in the four-matrix class, but needs a new microscopic derivation not in hand). (3) Presentation B with independent `Phi`. (4) Moyal corrections, non-constant backgrounds, fermion and scalar content (lower leverage: they add subleading or loop terms and leave the tree-level counting intact). Rejected: treating the count as sufficient; citing embedding theorems.

## Milestone assessment
Candidate M2 (bounded), as the gatekeeper's r1 verdict: conditional obstruction for four-matrix Poisson-limit Presentation A with generic conserved sources and no extra conserved stress, and for the embedding reading of `ass:emergent-op` in that class. Not M1, not M3, not a breakthrough.

## Status-label recommendation
None. A, B, C, D1, E, F, G-derived and N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
None. (N >= 8 is covered by the author's standing pre-approval for emergence-preserving structural changes and is not part of this text; no status, priority or completion label is touched.)

## Remaining open step
To discharge `ass:emergent-op`, hypotheses of H_A that can be relaxed within the core: (a) a derived additional conserved stress such as `T_ent`; (b) Moyal corrections beyond the Poisson limit; (c) non-constant backgrounds; (d) fermion and scalar content; (e) Presentation B with an independent `Phi` tying derivative indices to tangent indices; (f) more matrix coordinates (N >= 8, counting only). Most promising for discharging `ass:emergent-op` while keeping spacetime emergent: (f), as a separate proposal that extends `def:matrix-coords`, fixes the dictionary `Phi^I_mu = d_mu x^I`, and repeats the rank computations for N = 8, 10. Still undone after that: identification of the emergent metric with a derived operator metric, and a value and sign of `G_eff`.

## Special instructions for the gatekeeper
- This is a conditional obstruction within H_A; it closes or advances no label.
- The manuscript text must claim nothing for Presentation B, for N > 4 beyond the labelled assumed dictionary, for Moyal corrections or for `T_ent`; N >= 8 must not appear in it.
- Re-check: the displayed dG amplitude `(Gu) o p + n o m` (no factor 1/2) against `check_linear_response.py`; metric-explicit orthogonality `n^T K p = 0`; the vacuum statement with delta contraction and real locked block; the F6 rank-five wording.
