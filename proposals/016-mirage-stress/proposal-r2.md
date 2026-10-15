# Proposal 016-mirage-stress, round 2

## Changelog against r1

- F1 (major): second paragraph retitled "extra stress and crossover response at the leading symbol"; "Derived stress" deleted and "derived" removed from the heading; conservation sentence replaced by the review's (Bianchi identity plus conservation of T, paralleling the ambiguity-fixing of KumarSteinacker2023/Steinacker2026); the closed form X = -Lambda L E is stated as the content and wE as the supplied input; the closing scope sentence now says "no new derivation of the conservation of the extra stress"; no claim to supply the 008/009 stress; milestone assessment changed (below).
- F2 (major): ell_5 deleted; ell used throughout (ell^2 = -y_a y^a, a = 0..4, already the 5D quantity). The scripts' variable `ell5` equals ell; no calculation changed.
- F3: H (linear map c -> h) and D^S (symmetric part of D) defined; the normalisation constant of 014 absorbed in w and Lambda (stated); L defined in the Crossover paragraph, on the 6-dim span of symmetrised s_i s_j, invertible for q^2 != 0, xi != 0; "(spacelike q)" after g+8xi<0 dropped.
- F4: added: wE is input and the result is input plus a non-local frame-dependent tree correction; elliptic in omega with conditions on real roots; G indefinite for spacelike q; anisotropy that of yhat, SO(3,1)-covariant if y^mu is a vector; literature extra modes in the same family, no match claimed.
- F5: prior-art sentence ("standard") used; no new bib entries (option "cite nothing new"), so Steinacker 0812.3761 and Abou-Zeid-Dorn are not cited and nothing is added to bib/; {X_a,.} stated to be a frame derivative, not nabla_mu; "trace term" replaced by "the term (1/4) eta^{ab} F_cd F^cd".
- F6: comparison stays structural; the text says (as extracted) that the extra modes of Steinacker2026 are rotation-isotropic with reduced velocity; no quantitative match.
- Review note: y^i = 0 is not essential; the text now says it "only provides the closed forms". The reviewer's floating-point check at y^i != 0 is cited here; I did not re-run my exact scripts at y^i != 0 (class kept at y^i = 0 in the text).
- Unchanged: all mathematics, scripts and outputs of r1; the anchor and insertion position. The Remaining open step now adopts the review's ranked avenues.
- Compile check added: `compile_check_r2.py` copies the repo to a scratch directory outside the repository, inserts `block-r2.tex` before the anchor, and runs two pdflatex passes: both exit 0, no `!` errors, no undefined/multiply-defined reference (`compile_check_r2.out.txt`, 262 pages). The block uses no doubly-subscripted macros (no \LUV, \Geff, \LIR); only \ell, \varrho, \mathcal, \mathbb, \mathbf.

## Result

Hypothesis class `H16`: Poisson limit; leaf CP^{1,2}; `X^a = T^a + A^a`, `T^a = M^{a4}`, `R = 1`; the quartic term of `eq:Smatrix` (`C = 0`) plus the bilinear term `mu^2 = -3` of 014; level-one amplitudes `c_i^nu` (013/014); leading symbol in `1/(|q| ell)`, frozen coefficients, tree level, sheet `y^4 > 0`, base points with `y^i = 0` (closed forms only; the review checked numerically that `y^i != 0` is not essential); an induced linearised Einstein-Hilbert form `(w/2) h.E[h]` and a conserved source `T` coupled through `h`, both supplied as inputs.

Established (exact computation within the class):
1. The Poisson-limit Noether identity `{X^a,E_a} = 0`, the stress divergence identity with the `mu^2` term, and the linear identity about `T^a`. The massless matrix-level identity is standard; the Poisson-limit form and the `mu^2` variant were not found in the literature (SME: "not found", not "absent").
2. At the leading symbol: the closed form `X = -Lambda L E` of the extra stress `X = wE - T` (symmetric, `q.X = 0`), the exact relation `(w + Lambda L)E = T`, the spectrum of `L`, and the dispersion determinant. Conservation of `X` follows from the Bianchi identity and the conservation of the input `T`; it is not an independent derivation. `wE` is the supplied input.

Not established: subleading order; sign and size of `w`; a matrix-derived matter coupling; that the extra roots are retarded poles; the nonlinear order; any supply of the 008/009 stress (that obstruction was a rank deficiency in the `H_A` class; 013 found rank 6 in `CP^{1,2}`, and 016's `X` is the 014 tree-level term recast, with the induced term supplied).

This is not a no-go beyond its hypotheses (Poisson limit, level-one sector, leading symbol, frozen coefficients, tree level plus the input EH form).

## Target and status

Problem F (`sec:status-F`), also bearing on B and A. Verbatim from Appendix H: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." Original target: A, B, C and the sign/scheme of `G_eff` computed from specified operators with `G_eff` not an input. NOT met. Chapter 17 (A, B, C, D1, E, F, G-derived, N) and the ledger agree; no discrepancy. The package is PROGRAMME-CONDITIONAL; nothing is derived toward F's target.

## Source reading

Digest + targeted reads, not a full scan (no definition, assumption or status passage changes). Read in full: proposal-r1.md, review-r1.md, review-r1-provisional.md, sme-consult-r1.md, and the appH insertion region and anchor (the anchor is now at appH line 1947 after the 015 integration, which sits in `sec:status-B`, far from the anchor). The scripts of r1 are unchanged.

## Research and reasoning

Mathematics unchanged from r1: `{X^a,{X^b,Z_ba}} = 0` for antisymmetric `Z` by Jacobi; `{X_a,F^{ac}F^b_c}` by Leibniz and `F^{ac}{X_a,F^b_c} = (1/4){X^b,F^2}`; the leading-symbol algebra from `s_i.q = 0`, `X(s_i,v) = -(Lambda/2) u_i.v`, `X(q,.) = 0`; the Gram matrix `G = q_perp^2 1 - (y^0/ell)^2 k k^T`. The reviewer reproduced these independently (including at `y^i != 0`).

Conservation (F1): `X := wE[h] - T` is symmetric by definition and satisfies `q^mu X_{mu nu} = 0` because `E` obeys the Bianchi identity and `T` is conserved. What the amplitude equations add is the explicit linear map `X = -Lambda L[E]`, the tree-level force conjugate to `h` expressed through `E`. This is the same logic as the literature: the `C -> C + dC` ambiguity of the anharmonicity tensor is fixed by Einstein-tensor and matter conservation in KumarSteinacker2023 App. C (read by the reviewer); in Steinacker2026 conservation of T[C] is imposed via the ambiguity, with the `(1 - m^2 Box^{-1})` form at linear order (SME extraction, not independently verified by me).

Literature: arXiv:2312.01317 and 2601.08031 were verified at abstract level in r1; 0812.3761 and hep-th/0104244 are not cited, so no new verification is needed. Not independently verified: equation numbers and velocities from the SME extraction.

## Claim classification

- Established (exact Poisson-algebra identities): `{X^a,E_a}=0`; stress divergence identity; `{T^a,L(A)_a} = -(3+mu^2){A^a,T_a}`. The massless form is standard.
- Established (exact within `H16`): decomposition; `X` symmetric and conserved given the inputs; closed form `X = -Lambda L E`; `(w + Lambda L)E = T`; spectrum of `L`; determinant.
- Input: `w` (hence `G_eff`, `varrho`), the conserved `T` and its coupling, `mu^2 = -3`, model `S_i`, identification of `h` with the emergent metric.
- Conditional: physical readings (ellipticity, instability); extra roots as poles of a response.
- Unresolved: subleading order; sign and size of `w`; matter coupling from the matrix action; nonlinear order.

## Proposed changes

Only `chapters/appH-microscopic-proofs.tex`. Insert, as one block, immediately before `\section{Problem G: HBEV}`. That anchor occurs exactly once (appH line 1947 in the current tree; `verify_anchors_labels.out.txt`); the preceding paragraph is the 014 paragraph ending "...This changes no ledger label; Problem~F remains open." (not unique, so the `\section` line is the anchor). Existing text kept. Labels: only `\ref{ch:vierbein-emergence}` is used, and it exists once (`eq:Smatrix`, `ass:EE`, `sec:status-F` also exist once but are not referenced in the new text). Bib keys `KumarSteinacker2023`, `Steinacker2026` exist. No new labels or bib entries. Status line once, at the end of the second paragraph. Compiles (see changelog). The same text is in `block-r2.tex`.

```latex
\paragraph{Conjugate-coordinate class: matrix Noether identity and the divergence of the stress (conditional; not closure).}
Work in the Poisson limit with \(F^{ab}=\{X^a,X^b\}\) and \(E_c=-\{X^b,\{X_b,X_c\}\}+\mu^2X_c\), the field equation of \((4g_{\mathrm{YM}}^2)^{-1}\int\mathrm{vol}\,(F_{ab}F^{ab}+2\mu^2X_aX^a)\), for arbitrary functions \(X^a\) on the leaf. The Jacobi identity and the Leibniz rule give \(\{X^a,E_a\}=0\) identically. The tensor \(\mathbb T^{ab}=F^{ac}F^{b}{}_{c}+\mu^2X^aX^b\), which is the variation of the action with respect to the contraction form, satisfies \(\{X_a,\mathbb T^{ab}\}=-F^{b}{}_{c}E^c+\tfrac14\{X^b,F_{cd}F^{cd}\}\); its divergence therefore vanishes on the field equation up to a gradient, and \(\mathbb T^{ab}-\tfrac14\eta^{ab}F_{cd}F^{cd}\) is divergence-free on the field equation exactly, the subtracted term being \(\tfrac14\eta^{ab}F_{cd}F^{cd}\) and not a trace of \(\mathbb T^{ab}\). About \(X^a=T^a\) the linear form obeys \(\{T^a,L(A)_a\}=-(3+\mu^2)\{A^a,T_a\}\), which vanishes exactly for \(\mu^2=-3\). For the massless model the matrix-level identity \([X_a,\mathbb T^{ab}]\propto\) equation of motion is standard; the Poisson-limit form \(\{X^a,E_a\}=0\) and the divergence identity with the \(\mu^2\) term are recorded here as exact identities in the polynomial Poisson algebra, and were verified there for both signs of the bracket. The tensor \(\mathbb T^{ab}\) carries matrix indices and \(\{X_a,\cdot\}\) is a frame derivative, not \(\nabla_\mu\mathbb T^{\mu\nu}\); it differs from the coordinate divergence of the fibre-averaged tensor by terms containing derivatives of the frame coefficients, of relative order \(1/(|q|\ell)\), which are not computed. The paragraph does not identify \(\mathbb T^{ab}\) with the source of an Einstein-type equation.

\paragraph{Conjugate-coordinate class: extra stress and crossover response at the leading symbol (conditional; not closure).}
Keep the setting and notation of the preceding paragraphs at the base points \(y^i=0\), with \(s_i^\mu=S_i^{\mu\rho}q_\rho\), \(Q^{\mu\nu}=\sum_is_i^\mu s_i^\nu\) and \(G_{ij}=s_i\!\cdot\! s_j\) (four-dimensional contraction). Add as inputs a term \(\tfrac12w\int h^{\mu\nu}\mathcal E_{\mu\nu}[h]\), the quadratic form of an induced Einstein--Hilbert term with \(w=-\zeta^2/(16\pi G_{\mathrm{eff}})\) when \(\delta g=\zeta h\), and a conserved source \(T_{\mu\nu}\) coupled as \(\int h^{\mu\nu}T_{\mu\nu}\); the normalisation of the tree-level term and of the coupling is absorbed in \(w\) and in \(\Lambda\), the coefficient of \(\tfrac12c_i\cdot Mc_i\), \(Mc^\nu=q^2c^\nu-q^\nu q\!\cdot\! c\). Since \(s_i\!\cdot\! q=0\), \(\{s_1,s_2,s_3,q\}\) is a basis for \(q^2\neq0\); \(c_i=D_{ij}s_j+\gamma_iq\) with \(\gamma_i\) the gauge part, \(h=H(c)\) with \(H\) the linear map \(c\mapsto h\), which depends only on the symmetric part \(D^{S}\) of \(D\), the three antisymmetric components of \(D\) are the inert amplitudes, \(c^TMc=q^2\mathrm{tr}(DGD^T)\), and \(G=q_\perp^2\mathbf 1-(y^0/\ell)^2\mathbf k\mathbf k^T\) with \(q_\perp^2=q^2+(q_\mu y^\mu)^2/\ell^2\) and \(\mathbf k=\mathbf q/|\mathbf q|\); its eigenvalues are \(g=q_\perp^2\) (twice) and \(\xi=-\sigma q^2\), \(\sigma=(y^4)^2/\ell^2\), along the spatial \(\mathbf q\). The restriction to \(y^i=0\) only provides these closed forms.

\emph{Extra stress.} The amplitude equations are equivalent to \(H^{T}X=-\Lambda Mc\) with \(X=w\mathcal E[h]-T\). In exact rational arithmetic at \((y^0,y^4)=(5,3),(13,5)\) and several rational \(q\) one finds that \(X\) is symmetric (equivalent to the three inert-amplitude equations), that \(q^\mu X_{\mu\nu}=0\), and that \(X_{\mu\nu}=-\tfrac12\Lambda\sum_i\tilde s^i_\mu(Mc_i)_\nu\) with \(\tilde s^i=\sum_kG^{-1}_{ik}s_k\). The amplitude equations determine \(X\) up to \(q_\mu q_\nu\), which \(H^T\) annihilates; \(q^\mu X_{\mu\nu}=0\) follows from the Bianchi identity of \(\mathcal E\) and the conservation of \(T\), which fixes that term, as the ambiguity of the anharmonicity tensor is fixed in~\cite{KumarSteinacker2023,Steinacker2026}. The closed form \(X=-\tfrac12\Lambda\sum_i\tilde s^i\otimes Mc_i=-\Lambda\mathcal L\mathcal E\) expresses the extra stress through the tree-level equations; it is not an independent derivation of its conservation, and the Einstein part \(w\mathcal E\) is the supplied input.

\emph{Crossover.} The operator \(\mathcal L\) is defined on the six-dimensional span of the symmetrised products \(s_is_j\) and is invertible for \(q^2\neq0\) and \(\xi\neq0\). With \(\mathbb L[Z]=(\eta Q)Z+Z(Q\eta)\) one has \(h_T=\mathbb L[Y]\), \(Y=-2X/(\Lambda q^2)\), and eliminating the amplitudes gives exactly \((w+\Lambda\,\mathcal L)\mathcal E=T\), \(\mathcal L=\tfrac12\mathbb L^{-1}\circ(2-P\,\mathrm{tr})\), where \(P\) projects on \(q^\perp\). The operator \(\mathcal L\) has eigenvalues \(1/(2g)\) (two modes), \(1/(g+\xi)\) (two), \((g\pm\sqrt{g(g+8\xi)})/(8g\xi)\) (one each) and zero on the three inert modes. In the first channel \((1+\varrho/(2q_\perp^2))\mathcal E=T/w\) with \(\varrho=\Lambda/w\) the ratio of the tree-level to the induced coefficient, the form \((1-m^2\Box^{-1})\) with \(\Box\to-q_\perp^2\) and \(m^2=\varrho/2\); \(q_\perp^2=k^2+\sigma\omega^2\) is positive definite in \((\omega,\mathbf k)\), not the form \(q^2\). The result is the supplied Einstein part \(w\mathcal E\) plus a non-local, frame-dependent tree-level correction.

\emph{Roots.} \(\det(\Lambda A+wB)\propto\Lambda^3(q^2)^9(\Lambda+2gw)^2(\Lambda+(g+\xi)w)^2(-\Lambda^2+2\Lambda gw+8gw^2\xi)\), which reproduces the generalised eigenvalues of the tree-plus-induced form at the sampled points. Besides \(q^2=0\) there are roots that depend on the direction of \(q\) through the frame: in the first channel \(\omega^2=-(k^2+\varrho/2)/\sigma\), complex for every \(k\) if \(\varrho>0\) and for \(k^2>-\varrho/2\) if \(\varrho<0\); the helicity-zero roots are complex when \(g+8\xi<0\). The relation is elliptic in \(\omega\) rather than wave-like: for \(\varrho>0\) the first channel has no real-frequency root, and for \(\varrho<0\) real roots exist only for \(k^2<|\varrho|/2\), with \(\omega^2<0\) and growth rate proportional to \(k\) above that. The anisotropy is that of the background direction \(\hat y=y/\ell\), through \(q_\perp^2=q^2+(q\!\cdot\!\hat y)^2\), and \(G\) is indefinite for spacelike \(q\); the anisotropy is \(SO(3,1)\)-covariant if \(y^\mu\) is treated as a vector, and is not an explicit breaking of covariance. The sign of \(\varrho\) is that of \(\Lambda/w\); the sign of the induced coefficient is not determined here. These are roots of the leading-symbol dispersion relation, not shown to be poles of a retarded response (constraints and gauge fixing are not treated). The extra modes reported in~\cite{Steinacker2026} are, as extracted, rotation-isotropic with a reduced velocity from the cosmic frame; they belong to the same family of non-boost-invariant effects, and no match is claimed, since the map between the present \(q_\perp,\xi,\sigma\) and the notation there is not established.

This is a statement for the Poisson limit, the stated class with the bilinear term, the leading symbol, tree level plus the supplied induced form and conserved source, and the base points with \(y^i=0\). It derives no value or sign of \(G_{\mathrm{eff}}\) or of \(\varrho\), no masses or subleading terms, no matrix-derived matter coupling, no new derivation of the conservation of the extra stress, and no identification of \(G\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; the comparison with the modified Einstein equation of~\cite{KumarSteinacker2023,Steinacker2026} is structural. This changes no ledger label; Problem~F remains open.

```

Stale text elsewhere: the 014 sentence "no local E[h] = P(partial)J" stays true; no edit.

## Verification scripts

In `proposals/016-mirage-stress/` (r1 scripts and outputs unchanged and not re-run, since no calculation changed; the reviewer re-ran `check_noether_poisson.py` and `check_sector_poles.py` and an independent numpy check):
- `check_noether_poisson.py` / `.out.txt`: Noether identity, stress divergence, linear identity, both bracket signs.
- `lib_ls.py`, `check_mirage_stress.py` / `.out.txt`: exact leading-symbol checks (93).
- `check_sector_poles.py` / `.out.txt`: determinant, `L` spectrum, 014 cross-check.
- `verify_anchors_labels.sh` / `.out.txt`: anchor count 1 and labels (re-run in r2).
- `compile_check_r2.py` / `compile_check_r2.out.txt`, `block-r2.tex`: scratch-copy compile of the inserted block.

## Decisions Taken

- F5: chose "cite nothing new and say standard" rather than adding Steinacker 0812.3761 and Abou-Zeid-Dorn to the bibliography; hep-th/0104244 was not opened by anyone and the claim needs no citation. Rejected: citing unverified sources.
- Kept the first paragraph's identities as exact Poisson-algebra statements with an explicit prior-art disclaimer, since they are a correct bounded result relevant to a matrix-derived matter coupling (open avenue 4).
- Kept the class at `y^i = 0` in the text (my exact scripts) and said the restriction only provides closed forms, rather than extending the claim to `y^i != 0` without my own exact check.
- Did not explore the open avenues here, per instruction.

## Milestone assessment

Routine. No milestone trigger is claimed. The closed form `X = -Lambda L E` is a rewrite of the tree-level term whose conservation follows from the Bianchi identity and the conservation of the input `T`; the 008/009 obstruction is not resolved and `G_eff` stays an input. This replaces the r1 "weak trigger 1" assessment. The package is a bounded structural finding within `H16`.

## Status-label recommendation

None. A, B, C, D1, E, F, G-derived, N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

To close F's target one needs `G_eff` and its scheme computed from specified operators with no input. Ranked open avenues (each a relaxation of a hypothesis of `H16`; the review's ranking is adopted; none is explored here):
1. Subleading order `1/(|q| ell)`: masses, frame connection, harmonic mixing could change the indefinite-`G` structure and the extra roots, and decide whether `varrho >~ 1/ell^2` is within validity. (Next to be queued.)
2. The induced coefficient in this class (heat kernel with the Theta-built regulator): fixes the sign and size of `w` and `varrho`, F's own target, and selects the branch.
3. Relax the frozen frame: average over base cells and fibre classes to test whether the `yhat`-dependent `q_perp^2` averages to an `eta`-covariant form or maps onto the literature's reduced-speed modes (`y^i != 0` is not essential).
4. Replace the supplied `T` by a matrix-derived matter coupling using the matrix stress, after relating the frame divergence to the coordinate divergence.
5. Doubleton phase-space constraints on the inert modes, possibly removing the indefinite-`G` ghosts.
6. Nonlinear order, transverse matrices, `N >= 8` matrix coordinates.

## Special instructions for the gatekeeper

- Must not be asserted: closure of F or any critical-path problem; that `w`, its sign or `G_eff` is derived; that conservation of `X` is an independent derivation; that 008/009's stress is supplied; that the extra roots are physical instabilities or poles; any match with Steinacker et al.; any label change; any result beyond `H16`.
- Re-check: F1-F6 wording in the block; `ell_5` absent; H, D^S, L defined; "(spacelike q)" absent after the `g+8xi<0` clause; anchor once; `\ref{ch:vierbein-emergence}` exists; no new bib entries; compile output.
