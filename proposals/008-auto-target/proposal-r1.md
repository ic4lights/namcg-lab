# Proposal 008-auto-target, round 1

## Result
Target chosen: option (i), the identification of the Presentation-A (Poisson-limit) frame with `<Phi>/v`, i.e. the discharge of `ass:emergent-op`. It is **not** derived. What is established is a bounded no-go with an explicit hypothesis class H_A and an explicit relaxation map.

H_A: four Hermitian matrix coordinates; Poisson (semiclassical) limit; matrix indices contracted with a constant `eta = diag(-1,1,1,1)`; real nondegenerate `Theta`; the metrics are `K = Theta^T eta Theta`, `G = K^{-1}`, `rho = 1/|Pf Theta|`, `g_rho = (rho K)^{-1}` (the setting of the merged 005 paragraph).

Established inside H_A (exact algebra, sympy-checked):
1. **Image of `Theta -> G`.** `N = Theta eta` has characteristic polynomial `z^4 + (B^2-E^2) z^2 - (E.B)^2`, so `K eta = -N^2` has two doubly degenerate eigenvalues and `(K eta)^2 - (1/2) tr(K eta) K eta - Pf(Theta)^2 1 = 0`. This is 4 conditions on the 10 components of `G`.
2. **Immersion.** The map is an immersion (rank six) at every `Theta` with `Pf != 0`. Proof: in `sl2+sl2`, `N = (n+,n-)` and `N^2 = (nu+ + nu-) 1 + 2 n+ (x) n-`. A kernel element forces `d n+ = -lambda n+`, `d n- = lambda n-`, and then `lambda (nu+ - nu-) = 0`; `Im nu = 0` iff `E.B = 0`. The rank drops to 5 at `Pf = 0`. This upgrades the "sample points tested" rank statement of the merged paragraph.
3. **Linear response.** For `Theta = Thetabar + eps T`, `T = Thetabar d a - (mu<->nu)`, `a = u cos(p.x)`, `q = Thetabar p`, the amplitude of `sin(p.x)` is
   `dG = (Gu) o p + n o m`, with `n = G Thetabar p`, `m = G Thetabar eta u`, `a o b = a b^T + b a^T`, and `d ln rho = p.u`.
   - `u = q` gives `dTheta = 0` (the matrix gauge).
   - The first term is a linearised diffeomorphism. The second is not for generic `p`: `<n,p>_K = 0` and `<n,n>_K = p^T eta^{-1} p`.
   - The image of `u -> (dG, drho)` and of `u -> (dg_rho, drho)` is 3-dimensional.
4. **Field-content no-go.** The linearised Einstein operator about the constant background has rank 3 on this image. Its image lies in the 6-dimensional space of conserved symmetric sources (checked for both `G` and `g_rho`). So `E[h] = T` is solvable with `h = dG[u]` only on a codimension-3 subspace of conserved `T`. This is independent of every coefficient (`A,B,C`, `N_tot`, `G_eff`). The same count holds nonlinearly: 4 coordinate functions minus 1 matrix gauge give 3 gauge-invariant functions, against `10-4+1 = 7` for a diffeomorphism-invariant metric plus one scalar. This does not apply if an additional conserved stress (such as `T_ent`) is allowed to absorb the codimension; that would have to be derived.
5. **Operator metric.** For `D >= 4` matrices with `Phi^I_mu := d_mu x^I` and `g := Phi^T eta_D Phi`: `K = theta^T g theta` (exact; D = 4 gives `g = eta`). `K = c g^{-1}`, `c != 0`, is impossible for real Lorentzian `g`, because it would give `N^2 = -c` with `N = theta g` in `so(g)`, while the constant term of the characteristic polynomial is `-(E.B)^2 <= 0 < c^2`. The case `c = 0` is excluded by invertibility. (Euclidean `eta` allows `Theta = theta J`.) Hence in this class the operators sit on `G = K^{-1}`, never on the composite metric `g` of `def:composite-metric`; `ass:emergent-op` read with that `g` cannot be discharged here. This extends the K != c eta obstruction of `rem:ch3-moyal-check` to every real Lorentzian `g` and to nonconstant `theta`.
6. **Vacuum manifold.** With `e = eta^{-1} omega_hat` (`omega_hat` the dimensionless inverse of `Theta/l^2`), `e^T e = 1` iff `omega_hat^2 = -1`. Then `G = 1 - 2 n n^T` with `n = -J e_0` a spatial unit vector. Of the 6 directions of `dTheta`, only 2 are tangent to `{Phi^T Phi = v^2}`; 4 pay `V^(2) = lambda v^2 Tr H^2`.
7. **Tree level.** By `rem:ch3-trace-quadratic`, the tree-level quadratic action is `proportional to ∫ rho_bar eta eta T T`, algebraic in `T = dTheta`, hence algebraic in `(dG, drho)`. All derivative terms of the metric perturbation are one-loop.

Not established: `<Phi>/v` = coframe; any value or sign of `G_eff`; anything for Presentation B with an independent `Phi`; Moyal corrections.

## Target and status
- Problems A, D1, F (and B, C by dependency). Appendix H: Status OPEN, Priority CRITICAL PATH (A: "for the matrix-derived label"), Completion PROGRAMME-CONDITIONAL. Chapter 17 lists A, B, C, D1, E, F, G-derived, N; no discrepancy found.
- Original target (F): discharge `ass:emergent-op` or replace it by a derived ingredient (`rem:ch8-scaffold-vs-emergent`; appH Problem F "What the two preceding results imply"). Not met. This proposal is PROGRAMME-CONDITIONAL and a bounded no-go.

## Source reading
Digest + targeted reads. The digest was current (head 8693e27). Read in full: appH Problems A, B, D (symmetries, Steinacker, integrable-frame paragraphs), F (L1103-1815); ch17 L370-520; ch03 L25-755; ch04 L28-440; ch08 L27-126 and 278-335; ch10 L26-208; the 005 proposal, its review and scripts. Not a full scan. No unreadable files.

## Research and reasoning
Choice (i) over (ii)/(iii): both 003 and 005 ended at "the frame identification is not derived". Tracing the Presentation-A frame `E_A = [X_A,.]` to its consequences gave definite answers. The three consequential outputs are the field-content count (3 vs 7), the Lorentzian operator-metric obstruction, and the vacuum-manifold mismatch.

Derivations (all standard linear algebra; scripts re-run them).
- Frame: `E_A^mu = eta_{AB} Theta^{B mu}`, `e^A_mu = eta^{AB} omega_{mu B}`, `G = eta e e`, and `e_{A mu}` antisymmetric. This is already in 005. The new input is the image and response analysis.
- Linear response: `dK = -[q o m_u + u o s]` with `m_u = Thetabar eta u` and `s = Kbar p`. Then `dG = -G dK G`, using `G s = p`. The script confirms the final form for both signatures with exact rationals.
- Field-content count: see item 4. The matrix gauge `du = Theta d lambda` removes one of the four functions.
- Relaxation count (necessary, not sufficient): with `N` matrices the gauge-invariant data are `N-4` embedding functions plus `3` for the closed 2-form `omega`, i.e. `N-1`. Adding 4 diffeomorphism functions must reach the 11 functions of `(G, rho)`, so `N >= 8`. IKKT's `N = 10` passes. No embedding theorem is invoked and none is cited.
- Literature: none cited in the manuscript text proposed. Steinacker's open-string metric `G = theta^T g theta` is already recorded in appH Problem D. Not independently verified here.

## Claim classification
- Items 1, 2, 3, 5, 6: established (algebra, sympy-checked; exact rationals where stated).
- Item 4 (linear): established. The nonlinear functional count is a counting argument (conditional).
- Item 7: established from the manuscript's own formula.
- N >= 8 and the embedding reading `Phi^I_mu = d_mu x^I`: conjecture / relaxation sketch.
- `<Phi>/v` = coframe: unresolved.

## Proposed changes
File: `chapters/appH-microscopic-proofs.tex`. Insert one paragraph after the 005 paragraph. Anchor (occurs once, verified): "...do not apply; no linearized-diffeomorphism invariance is claimed. Problems~B, C, D and~F remain open." Insert before `\section{Problem G: HBEV}`. Nothing is replaced. Labels verified once each: `thm:Geff`, `eq:O-eta`, `ass:emergent-op`, `rem:ch3-moyal-check`, `rem:ch3-trace-quadratic`, `def:composite-metric`, `eq:g-from-e`, `eq:vev-is-frame`, `eq:V`, `ass:EE`. No new labels. No label changes.

```latex
\paragraph{Presentation~A in the Poisson limit: what four matrix coordinates can supply (conditional; not closure).}
Keep the setting of the preceding paragraph: four matrix coordinates, the Poisson limit, matrix indices contracted with \(\eta=\mathrm{diag}(-1,1,1,1)\), a real nondegenerate \(\Theta\), \(K^{\mu\nu}=\eta_{\alpha\beta}\Theta^{\alpha\mu}\Theta^{\beta\nu}\), \(G=K^{-1}\), \(\rho=1/|\operatorname{Pf}\Theta|\), \(g_\rho^{\mu\nu}=\rho K^{\mu\nu}\). Let \(N=\Theta\eta\in\mathfrak{so}(3,1)\) with electric and magnetic parts \(\mathbf E,\mathbf B\), so \(\operatorname{Pf}\Theta=\pm\mathbf E\cdot\mathbf B\).

\emph{Image of \(\Theta\mapsto G\).} The characteristic polynomial of \(N\) is \(z^4+(\mathbf B^2-\mathbf E^2)z^2-(\mathbf E\cdot\mathbf B)^2\), so \(K\eta=-N^2\) has two doubly degenerate eigenvalues and \((K\eta)^2-\tfrac12\operatorname{tr}(K\eta)\,K\eta-(\operatorname{Pf}\Theta)^2\,\mathbb I=0\): four conditions on the ten components of \(G\). Decomposing \(N=(n_+,n_-)\) in \(\mathfrak{sl}_2\oplus\mathfrak{sl}_2\), \(N^2=(\nu_++\nu_-)\mathbb I+2\,n_+\otimes n_-\), and a kernel element of the differential of \(\Theta\mapsto K\) must satisfy \(\delta n_\pm=\mp\lambda n_\pm\) and \(\lambda(\nu_+-\nu_-)=0\); since \(\operatorname{Im}\nu_+=0\) only if \(\mathbf E\cdot\mathbf B=0\), the map has rank six at every \(\Theta\) with \(\operatorname{Pf}\Theta\neq0\) and rank five at \(\operatorname{Pf}\Theta=0\) (symbolic and exact-rational checks).

\emph{Linear response.} Let \(\Theta=\bar\Theta+\epsilon T\), \(T^{\mu\nu}=\bar\Theta^{\mu\rho}\partial_\rho a^\nu-\bar\Theta^{\nu\rho}\partial_\rho a^\mu\), \(a^\mu=u^\mu\cos(p\cdot x)\), \(q=\bar\Theta p\). The amplitude of \(\sin(p\cdot x)\) in \(\delta G_{\mu\nu}\) is \((\bar Gu)_{(\mu}p_{\nu)}+n_{(\mu}m_{\nu)}\) (symmetrisation without a factor \(\tfrac12\)), with \(n=\bar G\bar\Theta p\), \(m=\bar G\bar\Theta\eta u\), and \(\delta\ln\rho=p\cdot u\). For \(u\propto q\) one has \(T=0\) (the matrix gauge). The first term is a linearised diffeomorphism; \(n\) is orthogonal to \(p\) and \(n\) is not parallel to \(p\) for generic \(p\), so the second is not. The images of \(u\mapsto(\delta G,\delta\rho)\) and \(u\mapsto(\delta g_\rho,\delta\rho)\) are three-dimensional. For generic \(p\) the linearised Einstein operator about the constant background has rank three on this image, whose image lies in the six-dimensional space of symmetric tensors with \(p^\mu T_{\mu\nu}=0\) (exact-rational check for \(G\) and for \(g_\rho\)). Hence \(\mathcal E[h]=T\) with \(h=\delta G[u]\) is solvable only for \(T\) in a three-dimensional subspace of the conserved sources, whatever the coefficients of an induced action. More generally four coordinate functions minus one matrix gauge give three gauge-invariant functions, against \(10-4+1=7\) for a diffeomorphism-invariant theory of a metric and one scalar. This does not exclude an additional conserved stress that absorbs the codimension; such a stress would have to be derived. The tree-level quadratic action of Remark~\ref{rem:ch3-trace-quadratic} is proportional to \(\int\rho\,\eta_{\mu\alpha}\eta_{\nu\beta}T^{\mu\nu}T^{\alpha\beta}\), algebraic in \((\delta G,\delta\rho)\); every term with derivatives of the metric perturbation is a loop term. Whether the algebraic term is cancelled is the content of Assumption~\ref{ass:EE} and is not decided here.

\emph{Metric seen by the operators.} For \(D\ge4\) coordinate matrices \(X^I\) with a Lorentzian \(\eta_{IJ}\) and \(\Phi^I{}_\mu:=\partial_\mu x^I\), \(g:=\Phi^T\eta\Phi\), the operator metric satisfies \(K=\theta^{T}g\,\theta\) exactly; for \(D=4\), \(x^I=y^I\), \(g=\eta\). The relation \(K=c\,g^{-1}\), \(c\neq0\), would give \(N^2=-c\) with \(N=\theta g\in\mathfrak{so}(g)\), whose characteristic polynomial has constant term \(-(\mathbf E\cdot\mathbf B)^2\le0<c^2\); \(c=0\) contradicts invertibility. So for real Lorentzian \(g\) and any nonconstant \(\theta\) the operators sit on \(G=K^{-1}\), not on a metric of the form~\eqref{eq:g-from-e} built from \(\Phi\), and Assumption~\ref{ass:emergent-op} read with that metric is not discharged by this class (this extends the obstruction of Remark~\ref{rem:ch3-moyal-check}). If \(e=\eta^{-1}(\Theta/\ell^2)^{-1}\) is identified with \(\langle\Phi\rangle/v\) as in~\eqref{eq:vev-is-frame}, then \(e^Te=\mathbb I\) on the vacuum manifold of~\eqref{eq:V} requires \((\Theta/\ell^2)^{-1}\) to be a complex structure \(J\); then \(G=\mathbb I-2nn^T\) with \(n=-Je_0\) a spatial unit vector, and only two of the six directions of \(\delta\Theta\) are tangent to that manifold.

This is a statement for four matrix coordinates, the Poisson limit and a constant \(\eta\); it does not apply to an independent field \(\Phi\) of Presentation~B, to additional matrix coordinates (a necessary functional count \(N-1+4\ge11\) for \(N\) coordinates is not a sufficient condition), or to Moyal corrections. It does not derive \(\langle\Phi\rangle/v\) as a coframe and gives no value or sign of \(G_{\mathrm{eff}}\). Problem~F, and Problems~A, B, C and~D, remain open.
```

Stale passages: none must change. The 005 sentence "At the sample points tested the map Theta -> G has rank six" remains true and is strengthened by the new paragraph.

## Verification scripts
In `proposals/008-auto-target/`, each with a saved `.out.txt`:
- `check_theta_image.py`: char poly, minimal polynomial, `Pf^2 | Gram det`, rank 6 at 79 random points, rank 5 at `Pf = 0`, `N^2 = -c` minimisation (Lorentzian min `2c^2 > 0`; Euclidean solvable for `c > 0`).
- `check_linear_response.py`: `dG` formula, `d ln rho`, `u = q` null, `<n,p>_K`, `<n,n>_K`, rank 3, Einstein-operator rank 3 vs 6 conserved sources, both signatures.
- `check_embedding_and_vacuum.py`: `K = theta^T g theta` for D = 4, 6, 10; `e^T e = 1`; `G = 1 - 2 n n^T`; tangent count 2.
- `verify_anchors_labels.py`: anchor count 1, all labels once.
All checks are algebraic or exact-rational except the minimisation and rank samples, which are checks and not proofs; the proofs are in the text above.

## Decisions Taken
- Chose option (i) and kept the result a bounded no-go with its hypothesis class H_A, because no honest derivation of `<Phi>/v` exists in this class.
- Did not edit `ass:emergent-op` wording; recorded the result in appH only (smallest insertion).
- Presented the N-matrix relaxation as a sketch only (see below). Rejected: asserting the IKKT embedding as the route, claiming N >= 8 as a theorem, and citing embedding theorems.

## Milestone assessment
Candidate M2 (bounded): rules out four-matrix Poisson-limit Presentation A as a carrier of Einstein-type dynamics with generic sources, and rules out `ass:emergent-op` with the composite `g` in that class. Not M1, not M3 (no merged claim is contradicted; 005's statements remain true). The gatekeeper decides.

## Status-label recommendation
None. A, B, C, D1, E, F, G-derived and N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
Whether Presentation A should carry N > 4 matrix coordinates (`def:matrix-coords` currently has 4), with `Phi^I_mu = d_mu x^I` as the dictionary for the rectangular `Phi` of Chapter 3. Emergence is preserved (spacetime still emerges from the matrices), but this changes Presentation A's field content. Not adopted by default; the counting suggests N >= 8.

## Remaining open step
To discharge `ass:emergent-op`: either (a) a Presentation-A content with enough fluctuating data (relaxation of H_A) together with the dictionary of `Phi` from the matrices, with the operator metric `G` then identified as the emergent metric; or (b) a Presentation-B derivation tying derivative indices to tangent indices. Neither is done. G_eff remains undetermined.

## Special instructions for the gatekeeper
- Do not read this as closing or advancing a label. It is a no-go within H_A only.
- Re-run the three scripts. Re-derive the kernel argument (item 2) and the dimension count (item 4).
- Check that the text claims nothing for Presentation B, N > 4, Moyal corrections or `T_ent`.
- Check the sign/convention of `dG` against `K = Theta^T eta Theta`.
