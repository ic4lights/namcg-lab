# Proposal 023-casimir-regulator, round 1

## Result
Bounded outcome, partly positive, in the hypothesis class: Poisson limit, one loop, leading symbol, four matrices T^a = M^{a4}, quartic plus one bilinear term (mu^2 = -3), background gauge, ghost -Box, regulators that are functions of the Casimirs C_42 = C_so(4,2) and C_41 = C_so(4,1) (both commute with every operator of the class).

1. (Established, exact, both signs of the bracket.) Four-matrix relation: H_V = C_G - C_41 - C_Sigma + mu^2 (C_G the Casimir of the total so(3,1) action on vector-valued functions), with the coefficient of C_42 equal to zero in the unique fit; Box = C_41 - C_31; C_42 - C_41 = -sum_{A<=4} eta_AA (J^{A5})^2. C_42 is central and C_41 commutes with so(4,1), so both commute with H_V, Box and the ghost operator.
2. (Numerical, exact structure.) The symbol form of C_42 (and of C_41) on the six-dimensional leaf has signature (2,4): negative definite on the 4-dim base, positive definite on the 2-dim fibre. The 022 "Euclidean symbol -2 l^2 g^{-1}" is the base block only; the fibre has the opposite sign. Pencil (C_41, C_42): eigenvalues 1/2 (x4), 1 (x2), deviation 3e-13 at 30 points.
3. (Bounded no-go.) A cutoff on C_42 alone cannot regulate the leading-symbol trace: the symbol is indefinite, level sets are non-compact, the window density diverges (null cone).
4. (Conditional route.) The matrix-built combination Delta_kappa = kappa C_42 - C_41, 1/2 < kappa < 1, has a positive definite symbol on the whole leaf, commutes with H_V, and gives a finite local window density for every continuous F(sigma(H_V)). It confines the central variable zeta to |zeta| <~ Lambda, which regulates the zeta-integral left divergent in 018/020/022 (at the leading symbol). It is an added element of the regularisation (uses J^{A5} outside U(so(4,1)')), not derived from the action; the leading coefficient is proportional to [(kappa-1/2)^2 (1-kappa)]^{-1}, divergent at both ends, so no kappa is singled out.
5. (Negative direction: bounded, not removed.) Euclid-contracted model: Zeeman depth <= d_* Lambda, 1.7 <= d_* <= 5.6 at six points. Lorentzian K: the window symbol of H_V has a point-independent lower bound -2 Lambda^2 (kappa = 3/4) but is negative on part of the window, so the Euclidean proper-time integral still diverges at large s. Exact compact analogue (so(6), delta, finite matrices; there the C_6 cutoff IS the matrix truncation): H + G^dag G has the spectrum lambda = c5(a,b) - c4(c',d') + 3 + m^2 (verified N = 1,2,3 to 1e-12); lowest eigenvalue in the window k <= A is -(A+3), negative modes 38, 124, 344, 750 (A = 1..4), fraction 2.5e-3 at A = 48.
6. Sign and size of w: nothing follows. The weight-two coefficient and its variation under A are not computed; the leading coefficient, and presumably the quadratic one, depend on kappa and on the cutoff function; the signature is Lorentzian for K and Euclidean for the window.
7. (Fork, new numerics.) Eight-matrix set {T^a, y^a}: stationarity needs bilinear coefficients lambda-3 (T) and 3 lambda-1 (y), equal only at lambda = -1 (common -4), where the contraction form has signature (3,3), not Lorentzian. For lambda > 0, lambda != 1, signature (5,1) (Lorentzian, nondegenerate, no centre, so no Landau/zeta problem) at lambda = 0.01, 0.1, 10; this needs two independent bilinear coefficients. Hessian not examined.

## Target and status
Problem F, coefficients A,B,C (appH sec:status-F): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." Original target: matrix-derived G_eff (sign and size) from the one-loop trace with a specified regulator. Dependencies: E (signature; OPEN / CRITICAL PATH for the matrix-derived label / PROGRAMME-CONDITIONAL) and the 018/020/022 blocks. Critical-path set unchanged: A, B, C, D1, E, F, G-derived, N. This package: PROGRAMME-CONDITIONAL; no discrepancy found between Chapter 17 and Appendix H.

## Source reading
Digest + targeted reads (scratch/digest.md read first; dirty-chapters: yes, as expected for the accepted uncommitted 022 block, treated as current). Read in full: appH Problem F ledger entry, the 018/020/022 blocks, proposals/022 review-r2 and scripts, and sections 3 and 4 of reports/sme-scout-flux-regulator-20261017.md. No full scan claimed.

## Research and reasoning
Setting. Operators of the class are polynomials in D^a = J^{a4}, J^{ab} and the vector index, i.e. in U(so(4,1)') (022). The Lorentz-invariant matrix-built operators commuting with them are C_42 (central in U(so(4,2))) and C_41 (central in U(so(4,1)), which contains all generators in H_V). exact_algebra_P4.py verifies the relations in the polynomial Poisson algebra (sympy, s = +-1), including commutators on random vector polynomials (a test; the proof is centrality).

Signature. sym_signatures.py, sym_definite.py, sym_pencil.py build the 6x6 forms sum w v v^T on the tangent space at random orbit points (40/25/30 points): C_42 and C_41 are (2,4); pencil eigenvalues 1/2 (x4), 1 (x2). Hence sigma(C_42) = -alpha q_b + beta q_f, sigma(C_41) = -(alpha/2) q_b + beta q_f, and A_kappa = sigma(kappa C_42 - C_41) = alpha(kappa-1/2) q_b + beta(1-kappa) q_f, positive definite for 1/2<kappa<1. kappa = 1 is the five-matrix Box (hypoelliptic, centre unregulated); kappa = 1/2 is purely vertical. kappa = 3/4 gives the absolute value of the Killing symbol in the splitting (the compact-dual symbol with the fibre sign reversed): natural, not unique. distrib.py: the four-matrix horizontal plane differs from the five-matrix one.

Regulated trace. [Delta_kappa, H_V] = 0, so Tr[F(H_V) chi(Delta_kappa/Lambda^2)] has a joint spectral meaning. At the leading symbol the local density is (2 pi)^{-6} int d^6 xi chi(A_kappa/Lambda^2) F(sigma_H), finite because the window is compact. The symbol sigma_H depends on (y^4)^2; the generalised eigenvalues of (sigma(Box), A_{3/4}) are -2 (all 8 points), 0, 0 and three positive values growing with (y^4)^2 (window_local.py (a)): the lower bound is uniform, the upper is not. The D^a are not SO(4,1)-invariant, so only local densities are claimed, not a trace over the infinite leaf.

Negative direction. In the nilpotent model (020) f ~ |zeta|; the window gives |zeta| <~ Lambda and the lowest level -|f1-f2| is bounded by d_* Lambda (window_local.py (b), Euclid contraction; the 020 model does not commute with Delta_kappa, so this is an estimate). The shell near the null cone of sigma(C_42) lies outside the nilpotent regime, which is another reason C_42 alone cannot be used.

Compact exact analogue. compact_exact.py: for X^a = M^{a5} (a = 1..4) on Sym^N(C^4), H + G^dag G has the spectrum lambda = c5(a,b) - c4(c',d') + 3 + m^2 over L^2(CP^3_N) = sum_{a<=N, b<=a} (a,b) (each so(5) irrep once, a the so(6) label), (c,d) in (a,b)|so(4), (c',d') in (c,d) x (1,0). Verified against dense diagonalisation for N = 1,2,3 (max difference 1.2e-13). Min in the window is -(A+3); count exponents approach 4 and 6 (compact_scaling.py, A <= 48; not proved). This extends the 022 compact check (min -(N+3)) to the whole spectrum; the C_6 cutoff is the matrix truncation there. It is a Euclidean section, not the Lorentzian problem.

Literature (from the coordinator note and the SME scout; I did not open the papers, so not independently verified): no paper uses an so(4,2) Casimir proper-time regulator, so this has no template. The published Lorentzian i-epsilon Schwinger integral organised in the flux (Steinacker-Tran 2405.09804 eqs 4.1-4.3; Manta-Steinacker-Tran 2411.02598 eqs 3.4-3.5) is the favourable fork. Chou-Nishimura-Tripathi 2501.17798 report inequivalent Euclidean and Lorentzian models, so no Euclidean w is claimed to carry over. The compact fuzzy fibre with a spin cutoff (Manta-Steinacker 2502.02498 eq 70) is the matrix-intrinsic fibre truncation, and could fix kappa. No BibTeX proposed and no citation in the block.

Comparison with the original target. The package removes one obstruction (the unregulated zeta-integral) by adding a regulator and shows that the negative direction and the signature mismatch remain; it computes no weight-two coefficient.

Fork list. Regulator: a function of C_42 alone fails; Delta_kappa works but kappa and chi are choices; avenue: fix kappa by a matrix-intrinsic fibre admissibility condition (SME R-F2). Signature: Lorentzian i-epsilon Schwinger integral in the window (SME R-F1/R-E1): finite window, compute the weight-two coefficient of Tr[e^{-isH_V} chi(Delta_kappa/Lambda^2)]; the e^{s|f1-f2|} growth belongs to the resummed Euclidean trace. Matrix set: eight matrices with lambda > 0 (Lorentzian (5,1), no centre), needing two bilinear coefficients; examine its Hessian. Sector: exact so(4,1) harmonic analysis of H_V = C_G - C_41 - C_Sigma + mu^2 on normalisable states. Content: fermions (the f^2/(2 pi^2) zero-mode term of the Euclid model).

## Claim classification
- Relations H_V = C_G - C_41 - C_Sigma + mu^2, Box = C_41 - C_31, C_42 - C_41 formula, commutation: established (exact algebra; commutation by centrality).
- Signature (2,4), pencil (1/2, 1), definite interval 1/2<kappa<1, window volume dependence on kappa: established on sampled points (numerical, 1e-13); the volume formula follows from the pencil.
- No function of C_42 alone regulates the leading-symbol trace: conditional (symbol level).
- Delta_kappa regulates the zeta-integral: conditional (symbol level, added regulator).
- d_* bound: estimate (numerical; Euclid, non-commuting model).
- Compact spectrum formula: numerically verified for N = 1,2,3, branching derivation not written out; counts exact from the formula; exponents numerical.
- Eight-matrix coefficients: established (exact); signatures: numerical (30 points per lambda).
- Sign and size of w; Wick or i-epsilon relation: unresolved (Problem E).

## Proposed changes
File chapters/appH-microscopic-proofs.tex. Anchor: the line `\section{Problem G: HBEV}` (occurs once, verified by compile_check_r1.py). The block is inserted immediately before it, after the 022 paragraph that ends "This changes no ledger label; Problem~F remains open." Nothing is replaced. Labels used and verified to exist once: ch:vierbein-emergence, ass:lorentzian. No new labels, citations or macros beyond those in use (\LUV, \mathfrak); no doubly-subscripted macros. Stale passages elsewhere: none (earlier blocks say the regulator is a function of Box_X and that the Casimir lies outside U(so(4,1)'); the new block is consistent with both and relaxes the first).

```latex
@@BLOCK@@```

## Verification scripts
All in proposals/023-casimir-regulator/ with .out.txt outputs:
- exact_algebra_P4.py: mu^2, Box, fit of H_V, commutators, C_42 - C_41 (both signs).
- sym_signatures.py, sym_definite.py, sym_pencil.py, distrib.py: signatures, base/fibre split, pencil and kappa scan, horizontal planes.
- window_local.py: Lorentzian window eigenvalues, Zeeman depth, volume factor.
- compact_exact.py (uses quantum_compact_hessian.py), compact_scaling.py: exact compact spectrum, counts, exponents.
- sym_eight.py, sym_eight_scan.py, eight_stationarity.py: eight-matrix set.
- compile_check_r1.py: scratch-copy compile outside the repository.
Support modules copied from 022: cp12_realisation.py, symbol_tools.py.

## Decisions Taken
- Relaxed "C_42 as regulator" to "matrix-built combination of C_42 and C_41", because the symbol of C_42 alone is indefinite; chose Delta_kappa over a delta-contracted sum of squares because only Delta_kappa commutes with H_V.
- Used kappa = 3/4 only as a reference value (absolute value of the Killing symbol), not as a derived preference.
- Recorded the eight-matrix lambda scan in the block (short exact and numerical record) since it answers the fork named in 022.
- No citations of the SME-listed papers in the manuscript block.

## Milestone assessment
Routine. A reproducible bounded structural result (regulator class, symbol signature, exact compact spectrum); no critical-path step is derived. Not a breakthrough.

## Status-label recommendation
None. F and E remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; the critical-path set is unchanged.

## Author decision needed
None.

## Remaining open step
A regulator-independent (or matrix-intrinsically fixed) weight-two coefficient of the induced term and its second variation under A, in the Lorentzian i-epsilon form, with the negative direction controlled; plus the Hessian of the eight-matrix lambda > 0 set and exact normalisable-state analysis. Then sign and size of w and the Problem E tie.

## Special instructions for the gatekeeper
- Do not assert that the regulator is derived from the matrix action, that the zeta-integral is regulated beyond the leading symbol, or anything about the sign or size of w.
- Re-run exact_algebra_P4.py (fit uniqueness, both signs), sym_pencil.py, compact_exact.py (N = 1,2,3 match), eight_stationarity.py.
- Re-check the convention "symbol form = minus principal symbol; H_V = -Box + ... has symbol form sigma(Box)".
- The Zeeman estimate d_* uses the Euclid-contracted 020 model, which does not commute with Delta_kappa; the block says only "bounded by ... in the normalisation of the forms".
- The compact formula is verified numerically, not derived; the block says "checked".
