# Proposal 075-d1-cubic-term, round 1

## Result

Bounded result, part negative and part positive. No closure, no label change.

1. **Rigidity lemma (exact, operator level).** Only C_[μνλ] enters eq:Smatrix (trace cyclicity). For a real action
   it is C_[μνλ] = i g^-2 ε_μνλσ v^σ with a real vector v. No nonzero choice is SO(3,1)-invariant. With X_a = i D_a
   the field equation is E_b = [D^a,[D_a,D_b]] + ½ ε_bcdf v^f [D^c,D^d] = 0. Take any configuration on which unitary
   operators implement every label rotation Λ in SO+(3,1), as the fibre generators S_cd do in the first-order
   equivariant class. If it solves the equation with v ≠ 0, then [D_a,D_b] = 0, that is T = R = F = 0.
   Consequences:
   - none of the 068/071/072/073 backgrounds (other than the flat point) survives or deforms at C ≠ 0;
   - about the flat point, every equivariant linearised solution is pure gauge (or a constant frame deformation);
   - the two TT solutions and the twelve torsion solutions at null q are removed together.

   In the full class the cubic term is a constraint, not a mass. No gap arises.
2. **The fork: classes whose fibre is the stabiliser H_v (positive-aimed, within the core).** The cubic term is
   consistent there.
   - (a) **Exact curved backgrounds.** For every v, the backgrounds with vanishing connection and
     [E_a,E_b] = ½ ε_ab^d_f v^f E_d solve all three brackets identically. This is the fuzzy-sphere balancing in four
     dimensions. For timelike v the base is time × S^3 with radius 4/|v|. For spacelike v it is SL(2,R)~ × R.
   - (b) **Flat-point spectrum (exact closed form).** At the flat point, every characteristic root of the 28
     equations is a root of the Carroll–Field–Jackiw (CFJ)-type one-form operator, with multiplicity 7. The bracket
     is (q²)² − (q·v)² + q² v·v.
     - **Spacelike v:** a gauge-invariant gap of definite sign, q0² ≥ |v|² on one branch, with an SO(2,1) mass shell
       q² = −|v|² at q·v = 0.
     - **Timelike v:** no gap; imaginary roots for 0 < |q| < |v|.
     - **Null v:** shifted cones and no gap.
   - (c) **The gap is not selective.** It acts identically on the four frame labels and on the three connection
     one-forms. The other branch is non-Lorentzian at |q_v| ≲ |v|.
   - (d) **Time × S^3.** The spin-j sectors j ≤ 3/2 have only real roots, q0² = ¼|v|² l(l+1). These are compact
     levels, not masses.

Answer to the dispatched question: in the first-order equivariant class with local SO(3,1), the tree-level cubic term
does not produce a gauge-invariant gap. It removes all non-gauge modes. A gauge-invariant gap with definite positive
sign appears only in a variant class that realises local H_v = SO(2,1) (spacelike v). There it is a Chern–Simons-type
mass common to the frame and connection sectors.

## Target and status

- Problem D (local Lorentz), sub-target D1. Appendix H L719–722: "Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL." The reduced-scope D2 does not close D.
- Original target (ch17 L329–350 and L708–713). Derive local SO(3,1) from the matrix algebra and condensate.
  Specify ω, A_μ, B and the ghost operators with their field content. Derive the locked frame and its non-degeneracy
  (Assumptions ass:frame-lock, ass:nondeg). The connection dynamics must settle whether torsion vanishes, propagates
  or is massive (appH L745–757).
- Gating: ch17 L645–650 puts D1 first in the dependency order. F (step 3) uses the operators D1 specifies. This
  package attacks the D1 sub-question "torsion or propagating modes / mass".
- No discrepancy found between appH and ch17 for D. The critical-path set read from ch17 L645–668 and the appH
  ledger is A, B, C, D1, E, F, G-derived, N. It agrees with CLAUDE.md.
- Classification of this package's result: PROGRAMME-CONDITIONAL evidence (bounded no-go plus a conditional
  positive result in a variant class). Nothing is DERIVED for the original target.

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT` (digest marks appH CHANGED
and dirty-chapters: yes, consistent with the uncommitted 073 integration). The appH sha256 is 84f9c61e…24f, which
equals the dispatch hash. Read in full:
- appH L715–800: Problem D ledger, missing step, symmetries of Presentation A, the C = 0 branch;
- appH L1513–1533: class definition, matrix equation, flat spectrum, sources and scope;
- appH L1606–1686: 068, 071, 072 and 073 paragraphs;
- appH L3066–3072 and L3104: the fuzzy-sphere cubic term and its normalisation C_ijk = i c3 ε_ijk/g²;
- ch03 L138–186: eq:Smatrix, the remark on the cubic term, def:matrix-coords-ext ("the cubic term is not extended
  here");
- ch17 L329–350, L645–668, L708–713;
- 073 review-r1 avenues and 073 proposal-r2 "Remaining open step";
- reports/ledger.md entries on the cubic term (L692, L834–837, L899, L920).

Not a full scan.

## Research and reasoning

### R1. Which part of C enters, reality, normalisation (exact; s1 (a)–(c))
- `Tr([X^μ,X^ν]X^λ)` is antisymmetric in μν and invariant under cyclic permutations, so it is totally
  antisymmetric. Only C_[μνλ] contributes; s1(a) checks this on random complex C to 3e-17.
- In 4D, C_[μνλ] = ε_μνλσ u^σ. Hermitian X make the trace imaginary, so a real action needs u = i v/g² with v
  real. This is the fuzzy-factor convention of appH L3066, and s1(b) gives Im S = 2e-15.
- An SO(3,1)-invariant C would need an invariant vector, so v = 0.
- Variation: δS_4 = g^-2 Tr(δX^μ [X^ν,[X_ν,X_μ]]) and δS_3 = ½ C_λμν Tr(δX^λ [X^μ,X^ν]). This gives
  G_λ = [X^ν,[X_ν,X_λ]] + (i/2) ε_λμνσ v^σ [X^μ,X^ν]. s1(b) checks it against finite differences
  (rel. 1.7e-10).
- The 3-direction form reproduces χ = c3/2 (s1(c), residual 0 at j = ½, 1, 3/2), which matches appH L3068.
- With X_a = i D_a: E_b = [D^a,[D_a,D_b]] + ½ ε_bcdf v^f [D^c,D^d].

### R2. Rigidity lemma (exact; by hand, s1 (d)–(g))
- In the class, [S_cd, D_a] = η_ad D_c − η_ac D_d with S anti-Hermitian. Hence U_Λ = exp(½θ^{cd}S_cd) is unitary
  and U_Λ D_a U_Λ† = Λ_a^b D_b for all Λ ∈ SO+(3,1).
- E_b is a polynomial with c-number coefficients, so U E_b[D] U† = E_b[ΛD]. The quartic part is covariant, and ε is
  invariant under det Λ = 1. Hence E_b[ΛD; v] = Λ_b^{b'} E_{b'}[D; Λ^-1 v] (s1(d), residual 4.5e-12 with entries
  of Λ up to about 10).
- If E[D; v] = 0, then E[D; Λ^-1 v] = 0 for all Λ. Subtracting gives ε_bcdf (v − Λ^-1 v)^f [D^c,D^d] = 0 (s1(g)).
- Span. Suppose a covector α annihilates every v − Λv. Then α is constant on the orbit, which is one sheet of a
  hyperboloid or the open half null cone. The orbit lies in no affine hyperplane; for null v it contains v and 2v.
  So α = 0 and the span is R^4 (s1(e): rank 4 for timelike, spacelike, null and generic v).
- Injectivity. F ↦ ε_bcdf F^{cd} is the Hodge dual, which is injective (s1(f): rank 6).
- Hence [D_a,D_b] = 0. The D_e, S_de and order-zero parts are independent (appH L1527), so T = R = F = 0.
- Linear version. An equivariant fluctuation keeps D + δD in the class, so the same conjugation argument applies to
  the linearised operator equation and gives δ[D_a,D_b] = 0. About the flat point (plane waves, q ≠ 0):
  - δR_ab = i(q_aω_b − q_bω_a) = 0 gives ω = qλ, a local rotation;
  - after subtracting that rotation, δT = 0 gives h_b^c = q_b ξ^c, a diffeomorphism;
  - δF = 0 gives a U(1) gauge direction.

  At q = 0, δT = −ω_ab^c + ω_ba^c = 0 forces ω = 0, and any constant h solves.
- Numerics (s2(2)). With the 40 equations stacked over 6 random fibre points, the kernel is 10 (= gauge) at generic,
  timelike, spacelike and null q. At C = 0 and null q it is 24 = 10 + 14, as in the integrated L1529. The kernel of
  δ(T,R) is also 10. At q = 0 the kernel is 16. The order-zero field has kernel 1 (s2(3)).
- s2(1): the Heisenberg, null-rotation, family (i) and Heisenberg-with-connection backgrounds have residual O(1) at
  C ≠ 0 at random fibre points, as the lemma requires.
- Hypotheses of the lemma: (H1) c-number constant C; (H2) unitary implementation of all of SO+(3,1) on the labels;
  (H3) the equation is the operator identity (stationarity against finite-rank variations); (H4) no non-covariant
  extra term. The lemma persists if a Lorentz-covariant matter term is evaluated on an equivariant configuration.
  This is not put into the insert, which keeps "no matter term". (H5) For the linear statement, equivariant
  fluctuations. Tree level, four dimensions.

### R3. Fork: hypotheses and relaxations explored

| Hyp. | Relaxation | Explored here? | Outcome |
|---|---|---|---|
| H2 full SO(3,1) fibre | fibre = Stab(v) = H_v | yes (s3, s4, s6) | consistent; exact curved backgrounds; CFJ spectrum; gap iff v spacelike |
| H5 equivariant fluct. | non-equivariant fibre harmonics of the full class | no | open (avenue 1) |
| H1 c-number C | C ∈ 𝒜 co-rotating with the fibre (condensate field) | no | open (avenue 3); meaning of C must be fixed |
| tree level | one loop with C ≠ 0 (bilocal M(Q) operator) | no | open (avenue 2) |
| background | non-flat backgrounds of the H_v classes | partly (time × S^3, j ≤ 3/2) | real Casimir levels |

**R3a. Stabiliser classes.** Replace SO(3,1) by H_v in the class definition. H_v is SO(3), SO(2,1) or the 3-dim
null-stabiliser. This is a choice of the data of the class (appH L1519 calls Z, its fibre and 𝒜 "data of the class"),
so it is within the core. It realises local H_v only. The fields are h (16), ω ∈ Lie(H_v) (12) and A (4), with gauge
3+4+1.
- s3(1): the S-components outside Lie(H_v) vanish identically.
- s3(2): the gauge residual is 1e-16 and the kernel at random q is 7.

**R3b. Exact backgrounds (s6 exact sympy for symbolic v; s4 numerics).** Take c̄_ab^d = ½ ε_ab^d_f v^f with zero
connection. Then:
- Jacobi holds, v^a c̄_ab^d = 0 and c̄_ac^c = 0, so t = F = 0;
- B1 − ½ ε v T vanishes identically, and B2 = 0 because R = 0;
- T_abcT^abc = −(3/2) v·v.

For timelike v this is su(2) with structure constant |v|/2, so the S^3 radius is 4/|v|. For spacelike v it is
sl(2,R). In the full class these backgrounds fail: s4 residuals 4.3 and 0.48 at random u. s4 also shows that for
time × SU(2) only κ = +|v|/2 works (κ = −|v|/2 gives residual 0.81), and that at C = 0 there is no solution.

**R3c. Flat-point spectrum (s3 numerics, s5 exact).** About flat in the H_v class, the brackets are triangular:
- the second bracket involves only ω (δR = dω), and each Lie(H_v) component obeys ∂^aF_ab + ½ ε_b^{cd}_f v^f F_cd = 0;
- the first bracket has the same operator on each frame label h^e, sourced by ω;
- the third bracket is the same operator on 𝒜 = t − iA.

The one-form operator is M_b^d = −(q²δ − q_b q^d) + i ε_b^{cd}_f v^f q_c. Its properties:
- s5(1), exact: det(M − q_bq^d) = (q²)²[(q²)² − (q·v)² + q² v·v], and Mq = 0;
- s3(4): the product of the nonzero eigenvalues equals −q²[…] (ratio 1.000000);
- s3(3): at 6–7 sampled k for each type of v, all 28 roots of the 28-field system are one-form roots, each with
  multiplicity 7. Where two roots lie within tolerance the count is shared, which shows up as 14.

Branches (s5(2), exact):
- **Timelike v** (rest frame): q0² = |q|² ± |v||q|, imaginary for 0 < |q| < |v|, max |Im q0| = |v|/2 at |q| = |v|/2.
  No gap.
- **Null v:** q² ± q·v = (q ± ½v♭)² = 0. Shifted cones, no gap.
- **Spacelike v:** q² = −|v|²/2 ∓ sqrt(|v|⁴/4 + |v|² q_v²), so q0² = |q|² + |v|²/2 ± sqrt(…).
  - Upper branch: q0² − |q|² − |v|² = −|v|²/2 + |v| sqrt(|v|²+4q_v²)/2 ≥ 0. At q·v = 0, q² = −|v|²: an SO(2,1)
    mass shell (the Maxwell–Chern–Simons topological-mass mechanism on the three directions orthogonal to v).
  - Lower branch: q0² = k_⊥² + q_v⁴/|v|² − 2q_v⁶/|v|⁴ + …, and q0² − k_⊥² ≥ 0 because the rationalised
    numerator is q_v⁴.

  All roots are real for real k.

This is a derivative (first-order) term producing the gap, not a non-derivative term, so hazard F3 does not apply. The
gap statement is a statement about characteristic roots. No norm is used.

**R3d. Time × S^3 linearised (s4(C), numerical).** Spin-j sectors use E_i = −iκJ_i^{(j)} with κ = |v|/2. The
[E,E] = c̄E residual is ≤ 6e-17. The generic kernel is 7(2j+1). For j = 0, ½, 1, 3/2:
- all roots are real (max |Im| = 0);
- the nonzero roots satisfy (q0/κ)² ∈ {l(l+1)}, l ∈ {j−1, j, j+1}, l ≥ 0, to ≤ 2.7e-12;
- there are zero roots at j = 0 (24 counted; includes chains) and at j = 1 (l = 0), not analysed.

This parallels the fuzzy-sphere statement H_V^K = χ²(L² − κ3 S·L) with κ3 = 0 at χ = c3/2 (appH L3068–3072). The
levels sit at the curvature scale of a compact section, so they are not a mass.

### R4. Bearing on the target
- **The C = 0 restriction of 068–073 is forced.** Within the class that realises local SO(3,1) as matrix gauge
  transformations, any C_[μνλ] ≠ 0 leaves no non-commuting background and no propagating equivariant mode. So the
  tree-level gap for torsion or Lorentz modes cannot come from the cubic term on the D1 route.
- **Where a cubic-term gap lives.** It needs local Lorentz reduced to H_v with v spacelike. There the gap is
  Lorentz-violating, the same for the frame and the connection, and the frame sector's gapless branch is
  non-Lorentzian at momenta ≲ |v|. An emergent Lorentzian infrared therefore needs |v| below the infrared momenta,
  where the gap is irrelevant.
- **The missing ingredient** for a selective, Lorentz-invariant torsion gap is not in the tree-level displayed action
  on equivariant configurations, with or without C. It must sit in loops, in non-equivariant or bilocal sectors, or in
  a condensate reading of C.

### Literature
- Carroll, Field, Jackiw, Phys. Rev. D 41, 1231 (1990), DOI 10.1103/PhysRevD.41.1231. Verified through
  bibliographic listings (Bohrium, citing papers arXiv:1604.01102 and arXiv:2602.14217): authors, journal, DOI, and
  that it is a Lorentz- and parity-violating, gauge-invariant Chern–Simons-type modification of electrodynamics. The
  full text was not read. The dispersion relation used here is derived independently (s5), not imported.
- Adam, Klinkhamer, arXiv:hep-ph/0101087, Nucl. Phys. B607 (2001) 247–267 (journal ref from the arXiv abstract
  page). Abstract verified: for a purely spacelike preferred direction a well-behaved Feynman propagator exists and
  microcausality holds; for timelike directions unitarity or causality is violated. The insert cites only this.
  DOI not verified, so none is given.
- Deser–Jackiw–Templeton (Ann. Phys. 140, 372 (1982), DOI 10.1016/0003-4916(82)90164-6, verified via listing) is
  mentioned here only and not cited in the insert.

## Claim classification

| # | Claim | Class |
|---|---|---|
| C1 | only C_[μνλ] enters; real action ⇔ C_[μνλ] = i g⁻² ε v, v real; no SO(3,1)-invariant nonzero choice | established identity |
| C2 | field equation E_b with coefficient ½ | established derivation (checked numerically) |
| C3 | rigidity: unitary implementation of SO+(3,1) label rotations + C ≠ 0 ⇒ [D_a,D_b] = 0 | established (by hand), conditional on H1–H4 |
| C4 | prior backgrounds do not survive or deform at C ≠ 0 | established corollary of C3 |
| C5 | equivariant linearised solutions about flat are gauge or constant deformations; 14 null-q solutions removed | established (by hand) + numerical |
| C6 | cubic term is a constraint, not a mass, in the full class | established consequence of C3/C5 |
| C7 | H_v classes: consistency, fields and gauge count | established |
| C8 | exact backgrounds c̄ = ½ ε v, all v | established (exact sympy) |
| C9 | flat spectrum of H_v class = 7 copies of M(q); M also the order-zero operator | numerical (roots at sampled k) + exact triangular structure |
| C10 | det identity and branch formulas, gap iff spacelike, q0² ≥ |v|², lower branch non-Lorentzian | established (exact) given C9 |
| C11 | CFJ identification; AK causality statements | literature (abstract-level verified) |
| C12 | time × S^3 levels q0² = ¼|v|² l(l+1), all real, j ≤ 3/2 | numerical |
| C13 | the missing gap ingredient lies outside tree-level equivariant configurations | conjecture/mechanism (direction-setting) |
| C14 | the matrix integral selects any of these classes, backgrounds or C | unresolved, not claimed |

## Proposed changes

### File: chapters/appH-microscopic-proofs.tex (one insertion; nothing replaced)

- **Anchor:** the unique line `\section{Problem E: signature}` (one occurrence; checked by
  `apply_and_build_r1.py`).
- **Placement:** directly after the closing paragraph of the 073 paragraph "First-order equivariant class on the
  Heisenberg background: connections with legs off the null direction". That paragraph ends "…Problems~D, F and~N
  remain open and PROGRAMME-CONDITIONAL.".
- **What is kept:** all existing text. The block plus one blank CRLF line goes before the section line.
- **Hashes:** pre sha256 84f9c61e066fa19fda86907a5651e551f35e3112bfba6697a76c1b0efee0224f; post sha256
  8aed4519472ef5ec9b1c8a4668e39b02b0882b5e7edb2cf9a9e0b5ba513ae229.
- **Block:** 8606 bytes, CRLF, no BOM, one status sentence in the last paragraph.

The exact text is the file `appH_insert_r1.tex`, generated by `make_insert_r1.py`:

```latex
\paragraph{First-order equivariant class with the cubic term: rigidity under the fibre group and classes with fibre the stabiliser (conditional; bounded no-go).}
Keep the class of the paragraph on local \(\mathrm{SO}(3,1)\) inside the unitary group without the matter term, but take \(C_{\mu\nu\lambda}\neq0\) in Equation~\eqref{eq:Smatrix}, a constant \(c\)-number tensor. By cyclicity of the trace \(\mathrm{Tr}([\hat X^\mu,\hat X^\nu]\hat X^\lambda)\) is totally antisymmetric, so only \(C_{[\mu\nu\lambda]}\) enters; for a real action on Hermitian matrices it is \(C_{[\mu\nu\lambda]}=\mathrm i g_{\mathrm{YM}}^{-2}\epsilon_{\mu\nu\lambda\sigma}\mathsf v^\sigma\) with a real vector \(\mathsf v\), in the normalisation of \(C_{ijk}\) on the fuzzy factor in Section~\ref{sec:status-F}, and no nonzero choice is invariant under \(\mathrm{SO}(3,1)\). With \(\hat X_a=\mathrm i\mathbb D_a\), the field equation, read as stationarity against variations of finite rank, is
\[
\mathcal E_b:=[\mathbb D^a,[\mathbb D_a,\mathbb D_b]]+\tfrac12\epsilon_{bcdf}\mathsf v^f[\mathbb D^c,\mathbb D^d]=0
\]
(against finite differences of the action on random Hermitian matrices; its form on three directions gives the fuzzy-sphere solution \(\chi=c_3/2\) of that section). The generators \(\mathcal S_{cd}\) exponentiate to unitary operators \(U_\Lambda\) with \(U_\Lambda\mathbb D_aU_\Lambda^\dagger=\Lambda_a{}^b\mathbb D_b\) for every \(\Lambda\in\mathrm{SO}^+(3,1)\). The quartic part is covariant and \(\epsilon\) is invariant, so \(U_\Lambda\mathcal E_bU_\Lambda^\dagger=\Lambda_b{}^{b'}\mathcal E_{b'}|_{\mathsf v\to\Lambda^{-1}\mathsf v}\) (by hand; checked on random matrices), and a solution satisfies \(\epsilon_{bcdf}(\mathsf v-\Lambda^{-1}\mathsf v)^f[\mathbb D^c,\mathbb D^d]=0\) for all \(\Lambda\). For \(\mathsf v\neq0\), timelike, null or spacelike, these differences span \(\mathbb R^4\), since the orbit of \(\mathsf v\) lies in no affine hyperplane, and \(F^{cd}\mapsto\epsilon_{bcdf}F^{cd}\) is injective on bivectors. Hence \([\mathbb D_a,\mathbb D_b]=0\), that is \(\mathsf T=\mathsf R=\mathsf F=0\). The argument uses only the unitary implementation of the rotations of the label \(a\), not the first-order form. So for \(C_{[\mu\nu\lambda]}\neq0\) every solution in the class has commuting \(\mathbb D_a\): none of the backgrounds of the preceding paragraphs other than the flat point solves the equation or deforms to a solution. The same argument applies to the linearised equation on an equivariant fluctuation, so about the flat point every solution has \(\delta[\mathbb D_a,\mathbb D_b]=0\); for plane waves with \(q\neq0\) the conditions \(\delta\mathsf R=0\), \(\delta\mathsf T=0\) and \(\delta\mathsf F=0\) leave only gauge directions, and at \(q=0\) only constant frame deformations (by hand; numerically the kernel of the forty equations required at all fibre points is the ten gauge directions at sampled \(q\), null \(q\) included, against twenty-four at null \(q\) for \(C_{\mu\nu\lambda}=0\)). The two transverse-traceless solutions and the twelve torsion solutions at null \(q\) of the paragraph on local \(\mathrm{SO}(3,1)\) inside the unitary group are removed together. Here the cubic term acts as a constraint and not as a mass, and no gap arises.

The term is compatible with the stabiliser \(H_{\mathsf v}\subset\mathrm{SO}(3,1)\) of \(\mathsf v\). In the variant of the class with fibre \(H_{\mathsf v}\), with the generators of its Lie algebra in the same relation to \(\mathbb D_a\), the connection takes values in that algebra, the fields are the frame (16), the connection (12) and \(A\) (4) with gauge parameters \(3+4+1\), and in section values \(\mathsf v\) appears unchanged at every fibre point. With vanishing connection and a base group with
\[
[E_a,E_b]=\tfrac12\epsilon_{ab}{}^d{}_f\mathsf v^fE_d ,
\]
the field along \(\mathsf v\) is central, the algebra is unimodular, \(\mathsf T_{abc}\mathsf T^{abc}=-\tfrac32\eta_{ab}\mathsf v^a\mathsf v^b\), and all three brackets hold identically in \(\mathsf v\) (exact); the cubic term balances the quartic term, as on the fuzzy sphere. For timelike \(\mathsf v\) the frame metric is that of time times a three-sphere of radius \(4/|\mathsf v|\), with \(|\mathsf v|:=|\eta_{ab}\mathsf v^a\mathsf v^b|^{1/2}\); for spacelike \(\mathsf v\) the base is the universal cover of \(\mathrm{SL}(2,\mathbb R)\) times a line. About the flat point of this variant, every characteristic root of the twenty-eight linearised equations at plane waves \(\mathrm e^{\mathrm iq\cdot y}\) is a root of the one-form operator
\[
M_b{}^d(q)=-(q^2\delta_b{}^d-q_bq^d)+\mathrm i\,\epsilon_b{}^{cd}{}_f\mathsf v^fq_c,\qquad \det\bigl(M-q_bq^d\bigr)=(q^2)^2\bigl[(q^2)^2-(q\cdot\mathsf v)^2+q^2\,\eta_{ab}\mathsf v^a\mathsf v^b\bigr],
\]
with multiplicity seven, that of three connection one-forms and four frame labels, and \(M\) is also the operator of the order-zero field; the generic kernel is the seven gauge directions (the determinant exact, the rest numerical at sampled \(q\)). This is the dispersion of the Chern--Simons-like modification of electrodynamics by a fixed vector~\cite{CarrollFieldJackiw1990}. In a frame adapted to \(\mathsf v\), the bracket gives:
\begin{itemize}
\item for timelike \(\mathsf v\), \(q_0^2=|\vec q|^2\pm|\mathsf v||\vec q|\): every root tends to zero with \(\vec q\), there is no gap, and the roots are imaginary for \(0<|\vec q|<|\mathsf v|\), with \(|\operatorname{Im}q_0|\le|\mathsf v|/2\);
\item for null \(\mathsf v\), \((q\pm\tfrac12\mathsf v^\flat)^2=0\): shifted cones, as on family~(i) of the paragraph on left-invariant backgrounds with curvature and torsion, and no gap;
\item for spacelike \(\mathsf v\), with \(q_{\mathsf v}=q\cdot\mathsf v/|\mathsf v|\) and \(\vec q_\perp\) the part of \(\vec q\) orthogonal to \(\mathsf v\), \(q_0^2=|\vec q|^2+\tfrac12|\mathsf v|^2\pm\bigl(\tfrac14|\mathsf v|^4+|\mathsf v|^2q_{\mathsf v}^2\bigr)^{1/2}\), all real. The upper branch has \(q_0^2\ge|\vec q|^2+|\mathsf v|^2\), and at \(q\cdot\mathsf v=0\) it lies on \(q^2=-|\mathsf v|^2\), a mass shell of \(H_{\mathsf v}=\mathrm{SO}(2,1)\) acting on the three directions orthogonal to \(\mathsf v\). The lower branch has \(q_0^2=|\vec q_\perp|^2+q_{\mathsf v}^4/|\mathsf v|^2+O(q_{\mathsf v}^6/|\mathsf v|^4)\) and \(q_0^2\ge|\vec q_\perp|^2\)
\end{itemize}
(exact, from the bracket). For this term a well-behaved propagator and microcausality are reported for a purely spacelike vector, and a violation of unitarity or causality for a timelike one, in~\cite{AdamKlinkhamer2001}. So with spacelike \(\mathsf v\) the cubic term gives a gauge-invariant gap of definite sign, \(q_0^2\ge|\mathsf v|^2\) on the upper branch, at a scale fixed by \(C_{\mu\nu\lambda}\). It acts in the same way on the four frame labels as on the three connection one-forms, so it does not separate the Lorentz or torsion modes from the frame, and the lower branch is not Lorentzian for \(|q_{\mathsf v}|\lesssim|\mathsf v|\). On time times the three-sphere above, the twenty-eight equations in the spin-\(j\) sectors with \(j\le\tfrac32\) have only real roots, \(q_0^2=\tfrac14|\mathsf v|^2\,l(l+1)\) with \(l\in\{j-1,j,j+1\}\), \(l\ge0\), together with zero roots for \(j=0\) and \(j=1\) that are not analysed (numerical, to \(10^{-12}\)); these are levels on spatial sections of radius \(4/|\mathsf v|\), not masses.

These statements are for Equation~\eqref{eq:Smatrix} with a constant \(c\)-number \(C_{\mu\nu\lambda}\) and no matter term, tree level, the Lorentzian contraction, the first-order class and its variants with fibre \(H_{\mathsf v}\), and, for the linearised equations, linear order in equivariant fluctuations on the flat point and on time times the three-sphere in the sectors named. The variants realise local \(H_{\mathsf v}\) and not local \(\mathrm{SO}(3,1)\). The fluctuations of the full class that are not equivariant, which the cubic term couples to the equivariant ones, an operator-valued \(C_{\mu\nu\lambda}\), the bilocal modes, loops, a norm, the nonlinear evolution, the regulated trace and the domains of the unbounded operators are not treated. Nothing here shows that the matrix integral selects these classes, these backgrounds or a value of \(C_{\mu\nu\lambda}\), so the assumptions listed in the paragraph on left-invariant backgrounds with curvature and torsion are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

(The block above is the verbatim content of `appH_insert_r1.tex` with LF shown for CRLF.)

- Labels used, all verified to exist once: eq:Smatrix (ch03), sec:status-F (appH), ch:vierbein-emergence (ch04). No
  new labels.
- Citations: CarrollFieldJackiw1990, AdamKlinkhamer2001. Both are new; see bib below.

### File: bib/namcg.bib (integrator adds; keys verified absent)

```bibtex
@article{CarrollFieldJackiw1990,
  author  = {Carroll, Sean M. and Field, George B. and Jackiw, Roman},
  title   = {Limits on a {Lorentz}- and Parity-Violating Modification of Electrodynamics},
  journal = {Phys. Rev. D},
  volume  = {41},
  pages   = {1231},
  year    = {1990},
  doi     = {10.1103/PhysRevD.41.1231}
}

@article{AdamKlinkhamer2001,
  author  = {Adam, C. and Klinkhamer, F. R.},
  title   = {Causality and {CPT} Violation from an {Abelian} {Chern--Simons}-like Term},
  journal = {Nucl. Phys. B},
  volume  = {607},
  pages   = {247--267},
  year    = {2001},
  eprint  = {hep-ph/0101087},
  archivePrefix = {arXiv}
}
```

### Stale passages elsewhere
- appH L1514, L1533, L1629, L1646, L1661, L1686 scope their statements to C_μνλ = 0. They stay correct, and the new
  paragraph explains why that branch is the only non-trivial one in the full class. No edit is needed.
- ch03 L161–164 ("its detailed index symmetries are constrained by the requirement that the vacuum preserve a
  Lorentzian interpretation") is consistent with C1. It is left unchanged; the smallest change is none.

## Verification scripts

All run with `python -I` from `proposals/075-d1-cubic-term/`. They import `../068-d1-torsion-nonzero/core.py` (and,
in s2, `../071-*/lin.py`) read-only with bytecode writing disabled. Each script's output is saved next to it as
`*_output.txt`.

| Script | Checks | Expected invariant output |
|---|---|---|
| `python -I s1_lemma.py` | C1–C3 on finite matrices | (a) ~1e-17; (b) Im S ~1e-15, rel.diff ~1e-10; (c) residual 0 for j = ½, 1, 3/2; (d) covariance residual ≲ 1e-11; (e) rank 4 ×4; (f) rank 6; (g) ~1e-14 |
| `python -I s2_full_class.py` | C4, C5 | (1) every residual O(1) at c ≠ 0 and ≤ 2e-16 at c = 0; (2) kernel 10 for all q and v types, c = 0 null q: 24; δ(T,R) kernel 10; q = 0: 16; (3) all 1 |
| `python -I s3_reduced_flat.py` | C7, C9 | (1) ≤ 1e-15; (2) gauge rank 7, kernel 7, fields 28; (4) ratio 1.000000; (3) "roots off them: 0", multiplicities 7 (14 where two one-form roots coincide within tolerance) |
| `python -I s4_group_backgrounds.py` | C8, C12 | residual 0 at κ = +c/2 only, full class O(1); (C) max \|Im q0\| = 0, distance to l(l+1) ≤ 3e-12, kernel 7(2j+1); (D) Jacobi 0, residual 0 for all four v |
| `python -I s5_closed_forms.py` | C10 | (1) 0 and Mq = 0; gapped branch q0²(k=0) = c²; lower-branch series k_perp² + k_w⁴/C² − 2k_w⁶/C⁴; timelike factorisation 0; null identity 0 |
| `python -I s6_symbolic_background.py` | C8 exact | (1) 0, (2) {0}, (3) {0}, (4) {0}, (5) −3/2 |
| `python -I -B make_insert_r1.py` | writes the insert | 8606 bytes, 24 CRLF, bare LF 0, 1 status sentence |
| `python -I -B apply_and_build_r1.py --build` | hashes, anchor, labels, build on a temp copy | pre/post hashes match, labels defined 1, BUILD CLEAN, 0 warnings, temp copy removed |

## Decisions Taken
- **Reading of C.** C is read as a constant c-number tensor, which is the literal reading of "background condensate
  tensor" in eq:Smatrix. The operator-valued reading (C ∈ 𝒜) is listed as an avenue and not computed, because it
  changes what the displayed action means.
- **The fork variant.** The H_v-fibre variant was computed rather than a deformation ansatz in the full class,
  because the lemma excludes every full-class deformation exactly. A numerical search there would only confirm the
  lemma.
- **What is recorded.** The insert records the spacelike gap as a gauge-invariant characteristic-root statement of
  definite sign. It also says, in the same paragraph, that the gap is non-selective and that the infrared branch is
  non-Lorentzian. This keeps the positive datum without inflating it.
- **Notation.** \mathsf v is used for the vector (unused elsewhere). Structure constants are written explicitly so
  that κ (the Heisenberg scale) is not reused.
- **Time × S^3 spectrum.** It is included numerically for j ≤ 3/2 only, with the compact-level caveat.

## Milestone assessment
Routine. This is a bounded no-go plus a conditional positive result in a variant class. No critical-path step is
derived. (It does redirect D1: the tree-level cubic term is excluded as the source of a Lorentz-invariant torsion gap
on the SO(3,1)-equivariant route.)

## Status-label recommendation
Critical-path list (ch17 L645–668, appH ledger): A, B, C, D1, E, F, G-derived, N. All are OPEN. Optional: H, I, J,
also OPEN. Affected labels: none. D stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Remaining open step
**To close D1 (unchanged).** Derive local SO(3,1) and the locked frame from the matrix data, select the class, and
specify ω, A, B and the ghost operators with their field content and propagating modes, including norms.

**Ranked avenues for the torsion/Lorentz-mode gap (derivation-first).**
1. **Non-equivariant fibre harmonics of the full class at C ≠ 0 (within core, positive-aimed).** On the flat point
   of the full SO(3,1) class, the cubic term couples the equivariant fluctuations to the fibre harmonic carrying
   u^-1 v. Full SO(3,1) is kept, and the restriction of R2 (H5) is lifted. Task: the linearised equations on the
   lowest fibre harmonics (Peter–Weyl on the fibre, truncated). Success criterion: propagating gauge-invariant modes
   with a q-independent term.
2. **One loop at C ≠ 0.** About commuting matrices, the Hilbert–Schmidt fluctuations see the same algebra with q
   replaced by the relative momentum Q, giving M(Q). Its regulated log-determinant gives the induced
   Lorentz-violating and parity-odd terms of the connection sector. That is the input a one-loop gap needs, and it
   transfers to Problem F (operator content).
3. **C as an element of 𝒜 co-rotating with the fibre (condensate reading).** This yields a section-constant v with
   the full 40-field content, and then possibly a gap for all six connection components. It first needs the
   ordering terms of Tr(C[X,X]X) with non-central C, and a decision on whether C is dynamical. If adopted as the
   meaning of eq:Smatrix, it is STRUCTURAL; as a scoped hypothesis class it is not.
4. **H_v classes beyond the flat point.** SL(2,R)~ × R linearised (spacelike v, where the flat gap exists); the
   time × S^3 zero roots at j = 0, 1; norms.
5. (Bottom of record) further C = 0 constant-connection families on Heisenberg, or wider H_v deformations at tree
   level. The likely outcome is the same bounded results.

**Transfer to the gated problem F.** The fuzzy-factor cubic term of Section F is on transverse directions and is not
affected. If avenue 2 is pursued, M(Q) is the operator of the four-dimensional block at C ≠ 0.

## Special instructions for the gatekeeper
- Re-derive the coefficient ½ in E_b and the conjugation identity E[ΛD; v] = Λ E[D; Λ⁻¹v]. The lemma rests on these
  and on the span and Hodge arguments.
- Check that the lemma's hypothesis (unitary implementation of all of SO+(3,1) on the label) holds in the class as
  defined at appH L1514–1521. Do not let it be read as a statement about non-equivariant fluctuations (excluded in
  the scope sentence).
- Must not be asserted:
  - that C must vanish in NAMCG. Only the full equivariant class is rigid; the H_v variants and the other
    readings are open;
  - that the H_v gap is a mass of the torsion modes in the D1 sense. It is common to frame and connection, and the
    class realises only local H_v;
  - that the time × S^3 levels are masses;
  - any norm or stability statement.
- The H_v variant is a change of the data of the class, not of eq:Smatrix. Check that this is acceptable as
  "within core". The insert scopes it as a variant that does not realise local SO(3,1).
- s3 multiplicity counts of 14 arise where two one-form roots coincide within tolerance at small k. The invariant to
  check is "roots off them: 0".
