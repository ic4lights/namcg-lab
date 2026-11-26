# Proposal 041-covariant-bundle-connection, round 2

## Result

Unchanged from r1 (see proposal-r1.md for the derivations, claim table, scripts and ranked open avenues; none of that is repeated here). The gatekeeper verdict on r1 was ACCEPT WITH REQUIRED REVISIONS (3 major, 5 minor, no PRIOR-CLAIM-ERROR). r2 applies snippets A to H of review-r1.md verbatim and nothing else. No new computation was needed; no number, claim or scope changed except where a snippet changed a label.

## Target and status

Unchanged: Problems B, D, F are OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (ledger text quoted in r1 and in review-r1). No label change is proposed or made.

## Source reading

Digest plus targeted reads as in r1; additionally review-r1.md in full and the current working-tree `chapters/appH-microscopic-proofs.tex` for the anchor and OLD-string checks. Not a full scan.

## Findings and how each was applied

All replacements were made by `make_r2_insert.py` (saved), which asserts that each OLD string occurs exactly once in `appH_insert_r1.tex` before replacing it. The r1 block is saved unchanged as `appH_insert_r1.tex`.

1. Finding 1 (major, factor 2 in E): snippet A applied. E is now the quadratic form 2 eps^{mu nu rho sigma} F F with eps^{0123} = 1, and the quadratic action is stated as rho G G F F + b eps F F. The original sentence "Apart from the term proportional to J, the connection sector is ..." was removed as instructed and re-stated inside the snippet (the "; the gauge function ..." clause that followed it is kept, joined with a semicolon in place of the snippet's final full stop).
2. Finding 2 (major, labels): snippet B (operator identity: sampled jets, numerical; linear growth along one family only), snippet C (Goldstone sentence: sampled generic omega-bar, necessary condition only, not tested for (anti-)self-dual), snippet D third replacement (stationary-set relation "to numerical accuracy ... numerical, not proved", "on those jets"), snippet A ("equals ... at six sampled rational points ... not proved for general omega"), and snippet F's added sentence (identities numerical at the sampled points). Applied verbatim.
3. Finding 3 (major, covariance sentence): snippet E applied verbatim.
4. Finding 4 (minor, a_1 normalisation): snippet D first and second replacements applied (a_1 stated in the normalisation sqrt|G| a_1(O_v) = (4/6) rho R[g_rho] + rho^2 X; "on fourteen random jets per signature ... on those jets").
5. Finding 5 (minor, Dirac notation): snippet F applied (gamma^mu D_mu, Poisson limit of Gamma^mu [X_mu, Psi]).
6. Finding 6 (minor, b notation): the (G, rho, vartheta) versus (G, rho, b) clause with the s4 negative check is inside snippet A.
7. Finding 7 (minor, Block 2): snippet G applied: the Casimir relation is now cited as the merged one (H_V = C_G - C_41 - C_Sigma + mu^2 with C_G = C_31^tot, C_Sigma = C_V = -3), with H_V^0 = H_V - mu^2 for the mass-free operator; the sentence ends "but the dependence of the induced form on the base point"; the so(6) sentence ends "in that case".
8. Finding 8 (minor, PRIOR-CLAIM qualifications): edit (a) kept with the snippet H wording as the NEW string; edit (b) dropped entirely.
9. Mechanics: the four leading `%%` comment lines were stripped; the four separator comment lines between the two blocks were also stripped (the block boundary is the paragraph title; the anchors are given below), so the file contains no comment lines.

## Proposed changes

File `chapters/appH-microscopic-proofs.tex`; insert only; existing text kept except edit (a). `appH_insert.tex` (r2): 11947 bytes; 0 TAB, 0 CR, 0 non-ASCII, 0 control characters other than LF; braces net 0; `\(` / `\)` net 0; `\[` and `\]` 3 and 3; no `\ref`, `\cite`, `\label`, no comment lines. The file contains two paragraphs: the first begins `\paragraph{Moser variables:` (Block 1), the second begins `\paragraph{Conjugate-coordinate class: the Casimir form` (Block 2).

Anchors (each confirmed to occur exactly once in the current working-tree file, CRLF normalised):

- Block 1 immediately before the line `\section{Problem C: conformal mode and Cassini}` (then a blank line).
- Block 2 immediately before the line `\section{Problem G: HBEV}` (then a blank line).

Edit (a), file `chapters/appH-microscopic-proofs.tex` (OLD occurs exactly once, verified with Python):

OLD: `It stays undetermined until the frame is dragged by a flow whose internal part is a local symmetry, that is until the question of local frame rotations (Problem~D) is settled.`

NEW:
```latex
In the coframe variables it stays undetermined until the frame is dragged by a flow whose internal part is a local symmetry, that is until the question of local frame rotations (Problem~D) is settled; in the variables \((G,\rho,\vartheta)\) of the paragraph on Moser variables the Noether coefficient takes two values related by one numerical identity, and covariance does not select one.
```

Edit (b): dropped. No merged sentence is false; no PRIOR-CLAIM-ERROR.

### Full text of the r2 blocks

```latex
\paragraph{Moser variables: the covariant form of the connection sector on the stationary set and an identity between curvature and gradient invariants (conditional; not closure).}
Keep the setting of the two preceding paragraphs: four matrix coordinates, the Poisson limit, \(\omega=\Theta^{-1}\) closed, \(e^A{}_\mu=\eta^{AB}\omega_{\mu B}\), \(\rho=\lvert\operatorname{Pf}\omega\rvert\), \(G^{\mu\nu}=\eta_{\alpha\beta}\Theta^{\alpha\mu}\Theta^{\beta\nu}\), \(V_\mu=\partial_\mu\ln\rho\), the vector operator \(\mathcal O_v\) in the background gauge with \(\alpha=1\), and the tree-level equation \(\mathfrak J^\nu=\Box_Gx^\nu-G^{\mu\nu}\partial_\mu\ln\rho=\rho^{-1}\partial_\mu(\rho G^{\mu\nu})=0\). Write \(s_\eta=+1\) for \(\eta=\delta\) and \(s_\eta=-1\) for \(\eta=\operatorname{diag}(-1,1,1,1)\).

\emph{The composite connection.} Let \(w_{c|ab}\) be the components along \(e_c\) of the Levi-Civita spin connection of \(e\), and \(B_{c|ab}=-T_{c|ab}\) the composite connection of \(\mathcal O_v\) in the frame components of the torsion. Then \(B_{c|ab}=w_{a|cb}-w_{b|ca}\) for every coframe: the form index and one frame index of the spin connection are exchanged (this is \(\mathrm de^A=-w^A{}_B\wedge e^B\); checked against \(w\) computed from the metric at random jets, residual \(10^{-15}\), both signatures). Under \(e\to(1+\epsilon\lambda)e\) with \(\lambda_{AB}=-\lambda_{BA}\) the inhomogeneous part of \(w_{c|ab}\) is \(\partial_c\lambda_{ab}\) (up to a convention-dependent sign) and that of \(B_{c|ab}\) is the exchanged expression \(\partial_a\lambda_{cb}-\partial_b\lambda_{ca}\) with the same sign: \(B\) is not a connection for local rotations of the matrix index. A local similarity \(\mathcal O\mapsto S\mathcal OS^{-1}\), \(S(x)\) invertible, leaves the diagonal of the heat kernel, hence \(a_1\) pointwise, unchanged (checked, \(10^{-14}\)), so no Stueckelberg field acting on the index by such a similarity changes a local heat-kernel invariant of \(\mathcal O_v\). The dressing of the preceding paragraph replaces \(B\) by \(B[\Lambda e]\) and is not a similarity. About the sampled generic constant \(\bar\omega\) (twelve draws, both signatures) the only first-order rotation that keeps \(\eta_{AB}e^B{}_\mu\) antisymmetric, a necessary condition for \(e\) to come from a two-form, is \(\lambda=0\); the Goldstone-extremised rotation of the preceding paragraph therefore does not satisfy this condition at those backgrounds. This was not tested for (anti-)self-dual \(\bar\omega\).

\emph{Moser variables.} For embedding functions \(X\) of a fixed symplectic leaf, \(S[X]=\int\mathrm d^4y\,L(\omega_X)\) with \(L(\omega)=\rho\,\eta_{ac}\eta_{bd}\Theta^{ab}\Theta^{cd}\) and \(\omega_X\) the push-forward of the leaf form. A variation \(a^\mu\) of \(X\) changes \(\omega_X\) by \(\mathrm dA\), \(A_\nu=a^\mu\omega_{\mu\nu}\) to first order, and \(L\) is an algebraic function of the six components of \(\omega\). The second-order term of \(S\) is therefore half the Hessian of \(L\) along \(\mathrm dA\) plus a term proportional to \(\mathfrak J\). That Hessian equals \(2\mathsf M_G+b\,\mathsf E\) at six sampled rational points, in exact arithmetic and for both signatures (not proved for general \(\omega\)): \(\mathsf M_G\) is the quadratic form \(\rho\,G^{\mu\rho}G^{\nu\sigma}F_{\mu\nu}F_{\rho\sigma}\), \(\mathsf E\) the quadratic form \(2\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\) with \(\epsilon^{0123}=1\), and \(b=-\operatorname{sgn}(\operatorname{Pf}\Theta)\,\eta_{ac}\eta_{bd}\Theta^{ab}\Theta^{cd}/8\), so that the quadratic action is \(\rho\,G^{\mu\rho}G^{\nu\sigma}F_{\mu\nu}F_{\rho\sigma}+b\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\) up to the term proportional to \(\mathfrak J\). Apart from that term, the connection sector is a Maxwell field of the metric \(G\) with weight \(\rho\), coupled to the pseudoscalar \(\vartheta=\rho b\) through \(b\,\epsilon FF\); the variables \((G,\rho,\vartheta)\) are not the variables \((G,\rho,b)\) of the paragraph on the order \(\Lambda^2\), and the axial torsion is not the dual of \(\partial\vartheta\) (tested, residual \(0.3\)-\(1.0\)); the gauge function \(D_\mu a^\mu\) equals \(-\rho^{-1}\partial_\nu(\rho G^{\nu\lambda}A_\lambda)\). At sampled jets with \(\mathfrak J=0\) and \(\partial\mathfrak J=0\) (numerical: six draws, both signatures, first-order coefficients to \(10^{-15}\), both vanishing at zeroth order) the operator \(S\mathcal O_vS^{-1}\), \((Sa)_\nu=a^\mu\omega_{\mu\nu}\), has the same principal, first-order and zeroth-order coefficients as the Maxwell--axion operator in the \(\rho\)-weighted Lorenz gauge; along a one-parameter family leaving \(\mathfrak J=0\) the first- and zeroth-order differences grow linearly with the parameter. In these variables the field has no frame index: the bundle is the cotangent bundle with the Levi-Civita connection of \(G\), and \(\ln\rho\) and \(\vartheta\) enter as tensor couplings. This is covariance of the operator under changes of the coordinates \(y\) when \(G\), \(\rho\) and \(\vartheta\) are treated as tensor fields. These fields are built from \(\omega\) with the constant \(\eta\) contracted with the matrix index, which is the coordinate index, so it is not a symmetry of the matrix action under independent chart diffeomorphisms, and it is not a local Lorentz symmetry of the matrix index.

\emph{Heat-kernel coefficient.} For the Maxwell--axion operator the coefficient \(a_1\), in the normalisation in which \(\sqrt{\lvert G\rvert}\,a_1(\mathcal O_v)=\tfrac46\rho R[g_\rho]+\rho^2X\), is
\[
  a_1=-\tfrac13R_G+\Box_G\ln\rho-\lvert V\rvert_G^2+6s_\eta\,\lvert\partial\vartheta-\vartheta V\rvert_G^2
\]
(the Hodge operator with the dilaton term \(V\) and the axion term; the dilaton part is derived analytically, and the axion term is checked at generic jets, ratio \(1\) to six digits, both signatures). On fourteen random jets per signature with \(\mathfrak J=\partial\mathfrak J=0\) it equals \(a_1(\mathcal O_v)\) to \(3\times10^{-11}\), and \(\sqrt{\lvert G\rvert}\,a_1(\mathcal O_v)=\tfrac46\rho R[g_\rho]+\rho^2X\). With \(\rho R[g_\rho]=\rho^2(R_G+3\Box_G\ln\rho-\tfrac32\lvert V\rvert_G^2)\) this gives, on those jets,
\[
  X=-R_G-\Box_G\ln\rho+6s_\eta\,\lvert\partial\vartheta-\vartheta V\rvert_G^2 .
\]
On the same jets the six invariants satisfy one linear relation to numerical accuracy (rank five of six),
\[
  s_\eta\,\lvert\partial\vartheta-\vartheta V\rvert_G^2=-\tfrac12R_G+\lvert V\rvert_G^2-\tfrac32\Box_G\ln\rho
\]
(residual \(6\times10^{-12}\); numerical, not proved), so that on those jets also \(X=-4R_G+6\lvert V\rvert_G^2-10\Box_G\ln\rho\).

\emph{Consequence for the Noether coefficient.} With \(c_W=N_{\mathrm{tot}}/6+\kappa_Xr\) as in the paragraph on the order \(\Lambda^2\), the coefficient of \(R_G\) in \(X\) is \(r=-1\) when the gradient of \(\vartheta\) is kept as an independent invariant and \(r=-4\) when it is eliminated by the identity above. The value \(r=-4\) is the on-mode value of the normalisation paragraph; the value \(r=-2\) of the preceding paragraph, which rests on the stipulated dressing, corresponds to neither. For \(n_D=0\) the residue of the fixed-state replica is \(c_A-c_W=-r\), that is \(1\) or \(4\), to be compared with the vector holonomy contact of modulus \(1\) of the paragraph on the order \(\Lambda^2\). Covariance of the density therefore does not fix \(r\): it leaves two representations related by one identity of the stationary set, and the choice between them is the choice of which of \(G\), \(\rho\), \(\vartheta\) are held fixed under the variation of the first law; in the class all three are functions of \(\Theta\). On the two modes with \(\delta\rho=0\) the term in \(\lvert\partial\vartheta-\vartheta V\rvert^2\) and the part of \(a_1(\mathcal O_v)-a_1\) proportional to \(\mathfrak J\) are each mode dependent and not proportional to the tree-level kernel; their sum is, and gives the value \(\rho^2X\to1\) in the units of that paragraph.

These statements are for the Poisson limit, four matrix coordinates, \(\alpha=1\), one loop, the density \(a_1\), points with \(\mathfrak J=\partial\mathfrak J=0\) for the operator identity (numerical, at sampled jets), and the covariant formula for \(a_1\). The Hessian, operator and stationary-set identities are numerical at the sampled points stated. They do not cover the Dirac sector for \(n_D>0\), whose X-term enters with its own coefficient and whose Dirac operator \(\gamma^\mu D_\mu\), the Poisson limit of \(\Gamma^\mu[\hat X_\mu,\Psi]\), is a frame derivative without a spin-connection term and is not shown to have a covariant form; the terms proportional to \(\mathfrak J\) off the stationary set; the replica, the tip domain or the choice of independent fields in the first law; the gauge parameters other than \(\alpha=1\); more than four matrix coordinates; or a value or sign of \(G_{\mathrm{eff}}\). They derive no local Lorentz symmetry. Problems~B and~D remain open and PROGRAMME-CONDITIONAL.

\paragraph{Conjugate-coordinate class: the Casimir form of the Zeeman-dressed vector operator and the base-point dependence (conditional; bounded no-go).}
Keep the Poisson limit, the leaf \(\mathbb{CP}^{1,2}\) of \(\mathfrak{so}(4,2)\), \(T^a=M^{a4}\), \(D^a=\{T^a,\cdot\}\), \(J^{AB}=\{M^{AB},\cdot\}\), \(F_{ab}=\{T_a,T_b\}\), \(\Box=\eta_{ab}D^aD^b\) and the vector operator \(H_V\varepsilon_a=-\Box\varepsilon_a-2\{F_{ab},\varepsilon^b\}\) of the paragraph on the \(\Theta\)-built heat kernel. Let \(C_{41}=\tfrac12J^{AB}J_{AB}\) and \(C_{31}=\tfrac12J^{ab}J_{ab}\) (indices \(\le4\) and \(\le3\)) act on functions, let \(R^{ab}\) be the generators of the vector representation of \(\mathfrak{so}(3,1)\) with the sign for which \(J^{ab}+R^{ab}\) commutes with \(H_V\), and \(C_{31}^{\mathrm{tot}}\) the Casimir of \(J^{ab}+R^{ab}\). Let \(C_{31}^{\mathrm{tot}}\) be as above and let \(H_V^{0}=H_V-\mu^2\) denote the operator without the mass term. The exact relation of the paragraph on the Casimir of \(\mathfrak{so}(4,2)\), \(H_V=C_G-C_{41}-C_\Sigma+\mu^2\), with \(C_G=C_{31}^{\mathrm{tot}}\) and \(C_\Sigma=C_V=-3\), reads \(H_V^{0}=-C_{41}+C_{31}^{\mathrm{tot}}+3\) (re-checked on random polynomial fields; the other sign of \(R^{ab}\) and the opposite sign of the Zeeman term give no such identity). In this class the vector operator is therefore a Casimir operator of the total Lorentz spin: a bundle connection covariant under \(J^{ab}+R^{ab}\) is present, and the dependence of \(A\), \(F_1\) and \(F_2\) of the paragraph on the Zeeman-dressed vector sector on \(y^\mu\) is not the absence of a connection, but the dependence of the induced form on the base point. From the displayed definitions, \(F_1=y^2\bigl((\kappa\cdot\alpha)^2-\kappa^2\alpha^2\bigr)\) depends on the base point only through the scalar \(y^\mu y_\mu=-\ell^2-(y^4)^2\), and \(F_2=\kappa^2(\alpha\cdot y)^2\) is the term that contains \(y^\mu\) as a vector. Since \(y\cdot y=-\ell^2\) in the five-dimensional contraction, \((y^0)^2=\ell^2+y^iy^i+(y^4)^2\ge\ell^2\): no point of the leaf is fixed by the matrix Lorentz group, so a local density cannot be evaluated at a Lorentz-symmetric base point. For the compact form \(\mathfrak{so}(6)\) with \(\delta\) the points \(y^\mu=0\), \(\lvert y^4\rvert=\ell\) exist, and they are the points where the preceding paragraphs find \(f_1=f_2\) in that case.

This is a statement for the Poisson limit, the Lie--Poisson algebra \(\mathfrak{so}(4,2)\), the operator without the mass term and with the background gauge function, and the algebraic identity on polynomials; the sign of \(R^{ab}\) is fixed by invariance, not by an independent convention. It does not compute a finite coefficient, does not treat fermions, the window or the Zeeman-dressed resolvent at order \(\epsilon^2\), and gives no value or sign of \(G_{\mathrm{eff}}\). This changes no ledger label; Problem~F remains open.
```

## Verification scripts

As in r1 (s1 to s15, `compile_check.py`), plus `make_r2_insert.py` (builds the r2 insert from the r1 insert and asserts uniqueness of every OLD string). `compile_check.py` now splits the insert at the second paragraph title, applies edit (a) and both blocks to a scratch copy outside the repository, runs two pdflatex passes and deletes the copy. Result in `compile_check.out.txt`: compile_check (scratch copy outside the repository; CRLF preserved: True); pdflatex exit codes [0, 0], 307 pages; undefined \ref targets: []; multiply defined labels: []; undefined citations: 33 (bibtex not run in the scratch copy; the inserted text contains no \cite and no \ref)

## Decisions Taken

As in r1. In r2: all gatekeeper snippets applied verbatim; the one join (semicolon after snippet A) is a punctuation adaptation only.

## Milestone assessment

Routine; not a breakthrough (unchanged).

## Status-label recommendation

None.

## Author decision needed

None.

## Remaining open step

Unchanged; ranked list as in review-r1 (Wald/Noether charge for the constrained class; the explicit J-proportional part; analytic proofs of the Hessian and stationary-set identities; the Dirac sector; replica and tip domain, gauge dependence; leaf dimension above four, Phi-block).

## Special instructions for the gatekeeper

- Re-check that each snippet appears in `appH_insert.tex` as given (A to G) and that edit (a) uses the snippet H wording.
- The Hessian, operator and stationary-set identities remain numerical at sampled points and are labelled so; nothing here is a derivation of a critical-path step.
- The integrator should run `scripts/build_check.py` after integration.
