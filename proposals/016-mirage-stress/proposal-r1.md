# Proposal 016-mirage-stress, round 1

## Result

Hypothesis class `H16`: Poisson limit; leaf CP^{1,2}; `X^a = T^a + A^a`, `T^a = M^{a4}`, `R = 1`; the quartic term of `eq:Smatrix` (`C = 0`) plus the bilinear term `mu^2 = -3` of 014; level-one amplitudes `c_i^nu` (013/014); leading symbol in `1/(|q| ell)`, frozen coefficients, tree level, sheet `y^4 > 0`, base points with `y^i = 0` (samples `(y^0,y^4) = (5,3),(13,5)`, `R = 1`); an induced linearised Einstein-Hilbert form `(w/2) h.E[h]` and a conserved source `T` coupled through `h`, both supplied as inputs.

Established (exact; scripts saved):

1. **Matrix Noether identity and stress (item (i)).** For arbitrary functions `X^a` in the Poisson algebra, with `F^{ab} = {X^a,X^b}` and `E_c = -{X^b,{X_b,X_c}} + mu^2 X_c`: `{X^a,E_a} = 0` off-shell (Jacobi + Leibniz); the eta-variation stress `T^{ab} = F^{ac}F^b_c + mu^2 X^a X^b` obeys `{X_a,T^{ab}} = -F^b_c E^c + (1/4){X^b, F_{cd}F^{cd}}`, so its divergence vanishes on the field equation up to a gradient (exact, trace-subtracted form: no gradient). Linear level about `T^a`: `{T^a,L(A)_a} = -(3+mu^2){A^a,T_a}`, zero exactly for `mu^2 = -3`. This is Jacobi, not an argument.
2. **Derived conserved extra stress at the leading symbol.** With `c_i = D_ij s_j + gamma_i q` (`s_i^mu = S_i^{mu rho}q_rho`, `s_i.q = 0`), the Maxwell form is `q^2 tr(D G D^T)` and `h = sum (D+D^T)_ij s_i s_j` + divergence-free diffeo, with `G_ij = s_i.s_j = q_perp^2 delta_ij - (y^0/ell_5)^2 q_i q_j`, eigenvalues `q_perp^2` (twice) and `xi = -sigma q^2` (along the spatial `q`), `sigma = (y^4)^2/ell_5^2`. The amplitude equations give `X := w E[h] - T` with: `X` symmetric (this is the three inert-mode equations, `C_ij = c_i.s_j` symmetric), `q^mu X_{mu nu} = 0`, and
   `X_{mu nu} = -(Lambda/2) sum_i stilde^i_mu (M c)_{i nu}` (`stilde^i = G^{-1}_{ik}s_k`), i.e. the dual frame times the tree-level Maxwell equation of motion. `X` is fixed by `H^T X = -Lambda M c` modulo `q q` (the `C -> C + dC` ambiguity); conservation up to gradient follows from the divergence-free-diffeomorphism gauge identity, and here exactly (no gradient) once the `q q` term is fixed. So `E[h] = (1/w)(T + T_C)` with `T_C := X` conserved and determined by the amplitudes.
3. **Elimination (item (ii)).** `h_T = Q Y + Y Q` with `Y = -2X/(Lambda q^2)`, `Q = sum s_i s_i`, so exactly
   `(w + Lambda * Lc) E = T`, `Lc = (1/2) L^{-1} o (2 - P tr)`, `L[Z] = (eta Q)Z + Z(Q eta)`.
   `Lc` has eigenvalues `1/(2g)` (2 modes, TT-like), `1/(g+xi)` (2), `(g +- sqrt(g(g+8xi)))/(8 g xi)` (one each), `g = q_perp^2 = q^2 + (q.y)^2/ell_5^2`, zero on the 3 inert modes. TT-like channel: `(1 + varrho/(2 q_perp^2)) E = T/w`, `varrho = Lambda/w` (tree coefficient over induced coefficient): the form `(1 - m^2 Box^{-1})` with `Box -> -q_perp^2`, `m^2 = varrho/2`. It is controlled by `q_perp^2`, which is positive definite in `(omega,k)`, not by `q^2`; the other channels carry the anisotropic factors above.
4. **Poles (item (iii), leading symbol only).** `det(Lambda A + w B) ∝ Lambda^3 (q^2)^9 (Lambda + 2gw)^2 (Lambda + (g+xi)w)^2 (-Lambda^2 + 2Lambda g w + 8 g w^2 xi)`; cross-checked against 014's generalised eigenvalues (0 x3, 2 x2, 7/16 x2, -1 +- i sqrt(14)/2 in units of q^2). Besides `q^2 = 0` there are extra roots, direction dependent through the frame. TT-like: `omega^2 = -(k^2 + varrho/2)/sigma`, complex for all `k` if `varrho > 0`, complex for `k^2 > -varrho/2` if `varrho < 0`; helicity-zero roots complex when `g + 8 xi < 0` (spacelike `q`). The inert modes are not decoupled from the visible ones once `xi != g` (they appear in the tree form through `G`). Sign of `varrho`: with `eq:Smatrix` as displayed `Lambda > 0` and a healthy-sign induced term (`w < 0` in the convention `S_ind = (16 pi G)^{-1} int sqrt(-g) R`, `delta g = zeta h`: `w = -zeta^2/(16 pi G_eff)`) one gets `varrho < 0`; the sign of the induced coefficient is the open sign of Problem F, so both signs are reported.

NOT established: subleading order (masses, frame connection, harmonic mixing); the sign and size of the induced coefficient (input); matrix-derived matter coupling (input: conserved `T`); that the extra roots are poles of the retarded response (constraints, gauge fixing untreated); relation of the frame-component divergence `{X_a,.}` to the coordinate divergence (differs by frame-derivative terms of relative order `1/(|q|ell)`); identification with the emergent metric; `y^i != 0` base points.

## Target and status

Problem F (`sec:status-F`), also B, A by the dependency on a conserved total stress. Appendix H and Chapter 17: A, B, C, D1, E, F, G-derived, N are OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (ledger of 2026-10-15 agrees; no discrepancy). Original target of F: `A,B,C` and sign/scheme of `G_eff` computed from specified operators with `G_eff` not an input. NOT met; this package is PROGRAMME-CONDITIONAL (induced term and `G_eff` are inputs).

## Source reading

Digest + targeted reads (`make_digest.py --check` printed `DIGEST STALE` at start; I did not rely on it). Read in full: `reports/sme-scout-20261015-1110.md`, `reports/ledger.md`, `MILESTONE.md`, appH lines 1842-1905 (008/009/011/013/014 paragraphs and anchor), `proposals/014-level1-dynamics/proposal-r2.md` and scripts `check_maxwell_factorisation.py`, `check_tree_plus_induced.py`, `check_poisson_algebra_s2.py`, `proposals/013-*/cp12_realisation.py` (head), `ch03` `eq:Smatrix` passage. Not a full scan. Not read: reviews of 013/014, 015 files (ignored by instruction).

## Research and reasoning

*Noether identity.* `{X^a,{X^b,Z_ba}}` with `Z` antisymmetric vanishes by Jacobi, giving `{X^a,E_a}=0`; the stress identity follows from `{X_a,F^{ac}F^b_c} = {X_a,F^{ac}}F^b_c + F^{ac}{X_a,F^b_c}` and `Z := F^{ac}{X_a,F^b_c} = (1/4){X^b,F^2}` (Jacobi twice). Verified by `check_noether_poisson.py` for random polynomial `X^a` and symbolic `mu^2`, both signs of the bracket.

*Leading-symbol algebra.* Since `s_i . q = 0` in the 4D contraction, `{s_1,s_2,s_3,q}` is a basis; `X(s_i,v) = -(Lambda/2) u_i.v` with `u_i = M c_i` and `X(q,.) = 0` determine `X` completely and force the symmetry condition on the antisymmetric part of `C`. The Gram matrix follows from the 5D identity `s_i.s_j = q_perp^2 delta_ij` (013/014) minus the fifth component `s_i^4 = -(y^0/ell_5) q_i`. All steps verified exactly (`check_mirage_stress.py`, 93 checks, base points (5,3) and (13,5), five rational `q` each, random conserved `T`, `Lambda = 3/7`, `w = 2`). `check_sector_poles.py` gives the 9x9 determinant and the `Lc` spectrum symbolically and reproduces 014's side computation.

*Sign.* The overall sign of `eq:Smatrix` relative to the healthy Maxwell sign was already left open in 014; here the relative sign of tree and induced terms is the only thing that matters, so both are given.

*Literature (abstract-level only).* Verified by arXiv API fetch: Kumar-Steinacker arXiv:2312.01317 (modified Einstein equations from the one-loop effective action, anharmonicity contribution); Steinacker arXiv:2601.08031 (one-loop plus induced EH, extra non-Ricci-flat modes); Steinacker arXiv:2609.08955 (review). Not independently verified: their equation numbers, the linearised crossover form `(1 - m^2 Box^{-1})`, the `c/3` extra modes and their "apparent tachyon" (taken from the SME report as extracted). Comparison, not import: both have a tree/Yang-Mills part of degree zero in `q` plus an Einstein part and a crossover scale from the coefficient ratio; here the crossover is governed by `q_perp^2`, anisotropic, and the extra roots are complex/spacelike-type for generic signs, which is qualitatively tachyon-like; no match of speed or mass is claimed. In the literature as extracted conservation of the extra stress is argued; here it is derived in one class.

## Claim classification

- Established (exact Poisson-algebra identities): `{X^a,E_a}=0`; stress divergence identity; `{T^a,L(A)_a} = -(3+mu^2){A^a,T_a}`.
- Established (exact rational, leading symbol, `H16`): decomposition, `X` conserved/symmetric, closed form of `T_C`, Sylvester relation, modified Einstein equation, `Lc` spectrum, determinant/roots.
- Input: induced form `(w/2) h.E[h]` and its sign; conserved `T` coupled through `h`; `mu^2 = -3`; model `S_i` of 013/014.
- Conditional: all physical readings (healthy sign, instability), complex roots as poles of the response.
- Unresolved: subleading order; `G_eff`; matter coupling from the matrix action; emergent-metric identification; `y^i != 0`.

## Proposed changes

Only `chapters/appH-microscopic-proofs.tex`. Insert before `\section{Problem G: HBEV}` (occurs once; re-check, 015 may also insert there), after the 014 paragraph ending "...This changes no ledger label; Problem~F remains open." (not unique, so the `\section` line is the anchor). Existing text kept. Labels used (each occurs once): `eq:Smatrix`, `ch:vierbein-emergence`, `ass:EE`. Bib keys existing: `KumarSteinacker2023`, `Steinacker2026`. No new labels or bib entries. Status line once, at the end of the second paragraph.

```latex
\paragraph{Conjugate-coordinate class: matrix Noether identity and the divergence of the stress (conditional; not closure).}
Work in the Poisson limit with \(F^{ab}=\{X^a,X^b\}\) and \(E_c=-\{X^b,\{X_b,X_c\}\}+\mu^2X_c\), the field equation of \((4g_{\mathrm{YM}}^2)^{-1}\int\mathrm{vol}\,(F_{ab}F^{ab}+2\mu^2X_aX^a)\), for arbitrary functions \(X^a\) on the leaf. The Jacobi identity and the Leibniz rule give \(\{X^a,E_a\}=0\) identically. The tensor \(\mathbb T^{ab}=F^{ac}F^{b}{}_{c}+\mu^2X^aX^b\), which is the variation of the action with respect to the contraction form, satisfies \(\{X_a,\mathbb T^{ab}\}=-F^{b}{}_{c}E^c+\tfrac14\{X^b,F_{cd}F^{cd}\}\); its divergence therefore vanishes on the field equation up to a gradient, and \(\mathbb T^{ab}-\tfrac14\eta^{ab}F_{cd}F^{cd}\) is divergence-free on the field equation exactly. About \(X^a=T^a\) the linear form obeys \(\{T^a,L(A)_a\}=-(3+\mu^2)\{A^a,T_a\}\), which vanishes exactly for \(\mu^2=-3\). These identities were verified in the polynomial Poisson algebra for both signs of the bracket. The derivative \(\{X_a,\cdot\}\) is a frame-component derivative; it differs from the coordinate divergence of the fibre-averaged tensor by terms containing derivatives of the frame coefficients, of relative order \(1/(|q|\ell)\), which are not computed. The paragraph does not identify \(\mathbb T^{ab}\) with the source of an Einstein-type equation.

\paragraph{Conjugate-coordinate class: derived extra stress and crossover response at the leading symbol (conditional; not closure).}
Keep the setting and notation of the preceding paragraphs at the base points \(y^i=0\), with \(s_i^\mu=S_i^{\mu\rho}q_\rho\), \(Q^{\mu\nu}=\sum_is_i^\mu s_i^\nu\) and \(G_{ij}=s_i\!\cdot\! s_j\) (four-dimensional contraction). Add as inputs a term \(\tfrac12w\int h^{\mu\nu}\mathcal E_{\mu\nu}[h]\), the quadratic form of an induced Einstein--Hilbert term with \(w=-\zeta^2/(16\pi G_{\mathrm{eff}})\) when \(\delta g=\zeta h\), and a conserved source \(T_{\mu\nu}\) coupled as \(\int h^{\mu\nu}T_{\mu\nu}\). Write \(\Lambda\) for the tree-level coefficient of \(\tfrac12c_i\cdot Mc_i\), \(M c^\nu=q^2c^\nu-q^\nu q\!\cdot\! c\). Since \(s_i\!\cdot\! q=0\), \(\{s_1,s_2,s_3,q\}\) is a basis for \(q^2\neq0\); \(c_i=D_{ij}s_j+\gamma_iq\) with \(\gamma_i\) the gauge part, \(h\) depends only on \(D^{S}\), the three antisymmetric \(D\) are the inert amplitudes, \(c^TMc=q^2\mathrm{tr}(DGD^T)\), and \(G=q_\perp^2\mathbf 1-(y^0/\ell_5)^2\mathbf k\mathbf k^T\) with \(q_\perp^2=q^2+(q_\mu y^\mu)^2/\ell_5^2\), \(\ell_5^2=\ell^2-(y^4)^2\); its eigenvalues are \(g=q_\perp^2\) (twice) and \(\xi=-\sigma q^2\), \(\sigma=(y^4)^2/\ell_5^2\), along the spatial \(\mathbf q\).

\emph{Derived stress.} The amplitude equations are equivalent to \(H^{T}X=-\Lambda Mc\) with \(X=w\mathcal E[h]-T\). In exact rational arithmetic at \((y^0,y^4)=(5,3),(13,5)\) and several rational \(q\) one finds: \(X\) is symmetric (equivalent to the three inert-amplitude equations), \(q^\mu X_{\mu\nu}=0\), and \(X_{\mu\nu}=-\tfrac12\Lambda\sum_i\tilde s^i_\mu(Mc_i)_\nu\) with \(\tilde s^i=\sum_kG^{-1}_{ik}s_k\). \(X\) is fixed by the amplitude equations up to the addition of \(q_\mu q_\nu\), which \(H^T\) annihilates; conservation up to a gradient is the statement that the gauge transformations act on \(h\) as divergence-free diffeomorphisms, and the \(q_\mu q_\nu\) term can be chosen so that the divergence vanishes. The equation reads \(\mathcal E[h]=w^{-1}(T+T_C)\) with \(T_C=X\) conserved and determined by the amplitudes.

\emph{Crossover.} With \(\mathbb L[Z]=(\eta Q)Z+Z(Q\eta)\) one has \(h_T=\mathbb L[Y]\), \(Y=-2X/(\Lambda q^2)\), and eliminating the amplitudes gives exactly \((w+\Lambda\,\mathcal L)\mathcal E=T\), \(\mathcal L=\tfrac12\mathbb L^{-1}\circ(2-P\,\mathrm{tr})\), where \(P\) projects on \(q^\perp\). The operator \(\mathcal L\) has eigenvalues \(1/(2g)\) (two modes), \(1/(g+\xi)\) (two), \((g\pm\sqrt{g(g+8\xi)})/(8g\xi)\) (one each) and zero on the three inert modes. In the first channel \((1+\varrho/(2q_\perp^2))\mathcal E=T/w\) with \(\varrho=\Lambda/w\) the ratio of the tree-level to the induced coefficient, the form \((1-m^2\Box^{-1})\) with \(\Box\to-q_\perp^2\) and \(m^2=\varrho/2\); \(q_\perp^2=k^2+\sigma\omega^2\) is positive definite in \((\omega,\mathbf k)\), not the form \(q^2\).

\emph{Roots.} \(\det(\Lambda A+wB)\propto\Lambda^3(q^2)^9(\Lambda+2gw)^2(\Lambda+(g+\xi)w)^2(-\Lambda^2+2\Lambda gw+8gw^2\xi)\), which reproduces the generalised eigenvalues of the tree-plus-induced form at the sampled points. Besides \(q^2=0\) there are roots that depend on the direction of \(q\) through the frame: in the first channel \(\omega^2=-(k^2+\varrho/2)/\sigma\), complex for every \(k\) if \(\varrho>0\) and for \(k^2>-\varrho/2\) if \(\varrho<0\); the helicity-zero roots are complex when \(g+8\xi<0\). The sign of \(\varrho\) is that of \(\Lambda/w\); the sign of the induced coefficient is not determined here. These are roots of the leading-symbol dispersion relation, not shown to be poles of a retarded response (constraints and gauge fixing are not treated).

This is a statement for the Poisson limit, the stated class with the bilinear term, the leading symbol, tree level plus the supplied induced form and conserved source, and the base points with \(y^i=0\). It derives no value or sign of \(G_{\mathrm{eff}}\) or of \(\varrho\), no masses or subleading terms, no matrix-derived matter coupling and no identification of \(G\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; the comparison with the modified Einstein equation of~\cite{KumarSteinacker2023,Steinacker2026} is structural and not a derivation of theirs. This changes no ledger label; Problem~F remains open.
```

Stale text: the 014 sentence "no local \(\mathcal E[h]=P(\partial)J\)" stays true (the new relation is nonlocal in `q_perp`); the 014 sentence on the induced term (tree dominates at small `q`, Newton response above the crossover) is now made exact for the TT-like channel; no edit.

## Verification scripts

All in `proposals/016-mirage-stress/`, run with `python -B`, outputs beside them.
- `check_noether_poisson.py` / `.out.txt`: (N1) `{X^a,E_a}=0`, (N2) stress divergence identity and trace-subtracted form, (N3) linear identity, `s=+-1`.
- `lib_ls.py`: shared exact machinery.
- `check_mirage_stress.py` / `.out.txt`: Gram/eigenvalue identities (symbolic), decomposition, `E[h_T]` form, `X` properties, closed form of `T_C`, inert equation, Sylvester relation, modified Einstein equation; 93 checks, all True (an earlier run had three coding errors in index placement, fixed).
- `check_sector_poles.py` / `.out.txt`: symbolic determinant, generalised eigenvalues, `Lc` spectrum, cross-check with 014.
- `verify_anchors_labels.sh` / `.out.txt`: anchor count 1, labels, bib keys.

## Decisions Taken

- Took "stress" in two senses and derived both: the matrix eta-variation stress (exact identity, no leading-symbol restriction) and the extra stress `T_C` defined by the amplitude equations (leading symbol). Rejected: claiming they coincide; their relation needs the frame-derivative terms.
- Kept `G_eff`, the induced form, and the conserved source as inputs; reported both signs of `varrho` rather than assuming the healthy one.
- Stopped item (iii) at the leading symbol; the subleading operator is a separate package.
- Did not compare quantitatively with the `c/3` / `-m^2` statement (not independently verified).

## Milestone assessment

Candidate trigger 1 in a weak form: the "derived extra conserved stress" flagged twice in the ledger is derived in one class (conditional on the induced term, conserved source and `y^i=0` samples), with an exact modified Einstein equation. It derives no critical-path step. Also a bounded finding: the crossover is controlled by a Euclidean-definite `q_perp^2` and extra roots are complex for generic sign, so a Lorentz-covariant `(1 - m^2 Box^{-1})` does not result here. The gatekeeper decides; I do not claim a breakthrough.

## Status-label recommendation

None. A, B, C, D1, E, F, G-derived, N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

Forks from the no-go-like findings (anisotropic `q_perp^2`; complex extra roots), ranked for the infrared / full-GR derivation:
1. Subleading order (masses `O(1/ell^2)`, frame connection, harmonic mixing): decides whether `varrho >~ 1/ell^2` lies in the regime and whether the complex roots survive.
2. Compute the sign and size of the induced coefficient in this class (heat kernel of 005/011 with the Theta-built regulator): fixes the sign of `varrho`.
3. Relax `y^i = 0` and the frozen frame: average over base cells / fibre-averaging classes (011/013) to test whether the `q_perp^2` Lorentz-violating structure averages to an `eta`-covariant one.
4. Replace the supplied conserved source by a matrix-derived matter coupling, using the matrix stress of item 1 (conserved up to gradient).
5. Doubleton phase-space constraints (Manta-Steinacker) restricting the inert modes.
6. Nonlinear order and transverse matrices.

## Special instructions for the gatekeeper

- Must not be asserted: closure of F or any critical-path problem; that the induced term, its sign, or `G_eff` is derived; that the extra roots are physical instabilities; that the result holds beyond `H16`; any quantitative agreement with Steinacker et al.; any label change.
- Re-run all four scripts; re-derive by hand `{X_a,F^{ac}F^b_c}` step, `s_i.q=0`, `G` Gram formula, `X(q,.)=0`, and the `Lc` spectrum.
- Check: hypotheses (`y^i=0`, model `S_i`), that both signs of `varrho` are reported, that the first paragraph makes no status claim, anchor and labels.
