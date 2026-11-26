# Proposal 061-one-loop-real-form, round 2

## Changes r1 → r2

- **F1 (major; RESEARCHER-DECISION → option (a)).** In the insert's "Non-compact members and normalisation" block, the two sentences listing the base-coordinate member are replaced verbatim by the review's corrected snippet. The base member has γ = −3c < 0 (merged 060 L1603), so at γ>0 only so(4,1) with W timelike remains. Result 5, ranked avenues 1, 2, 4 and 6, and the fork table are updated to match.
- **F2.** "For a kinetic form K=k^T𝖪k of signature (3,1)" → "For K=−k0²+|k|²", and "for a positive definite K" → "for K=k0²+|k|²" (verbatim).
- **F3.** "… does not distinguish the moduli of the members' contributions" (verbatim).
- **F4.** "on the traceless fluctuations along the four directions of W (the compact check of Section~\ref{sec:status-F} counts four more from the trace)" (verbatim). The new ref sec:status-F resolves to 1 label.
- **F5 (optional, adopted).** so(5) → Spin(5) in the N = ∞ unitary-representation sentence.
- **Process.**
  - The r1 insert is kept as appH_insert.r1.tex.
  - The edits were made by apply_r2_edits.py. It checks the r1 hash a5039fc3…f493 and that each old and each new string occurs exactly once; output in apply_r2_edits.out.txt.
  - apply_check was re-run (apply_check.txt; the r1 output is kept as apply_check.r1.txt).
  - The scratch build ran (build_r2.txt).
- **Baselines (now committed, 276c04b).** appH 590875 B, 94befe3b…85c6; bib 27601 B, 645c93c9…0f67. Both checked and matching.
- **Unchanged.** No other insert bytes, no bib change, no script changes other than the new edit script, and no label changes.

## Result

This package compares, at one loop, the compact and non-compact real forms of the 060 conjugate-coordinate family, in Definition (A) with h_0 of signature (9,1), the IKKT fermion content (supplied) and fixed γ>0 (supplied). The decisive datum is the fermion Pfaffian. The bosonic determinant is not.

1. **Exact operator forms (established).** Take a compact member (five-index algebra so(5), W spacelike, c>0, γ=3c). In background Feynman gauge its one-loop operators are Casimir combinations:
   - bosons on W: c(C5 − C4^tot);
   - each of the six transverse directions: ±c(C5 − C4 − 3);
   - ghost: c(C5 − C4);
   - (Γ^a[T̄_a,·])² on each so(4) Weyl spinor: c(C5 − C4^tot + 3/2).

   These were checked on explicit Hessians for Sym^n C^4, n = 1, 2. The species weights 5 − 4 − 1 = 0, so apart from zero modes the one-loop modulus does not depend on γ.
2. **Bounded no-go (established, exact at every finite N, regulator-free).**
   - *Statement.* At every finite N, every non-zero member of the family has a degenerate fermion form, so Pf M(T̄) = 0.
   - *Where the zero modes sit.* In every so(5) component (m1,m2) ≠ 0 of the matrices, take the so(4) component (k1,k2) = (m1,m2) and couple it to total spin j_L + ½ (or the mirror for the other chirality). There C4^tot = C5 + 3/2 holds identically. The adjoint always occurs, so the kernel has dimension at least 32.
   - *Counts for V_n = Sym^n C^4.* The kernel has dimension (4/3)n(n+4)(n²+4n+7), i.e. 80 and 304 for n = 1, 2 on explicit 10D matrices. These are the only zero modes for n ≤ 20. Random four-matrix configurations have no kernel.
   - *Extensions.* The kernel persists for every unitary representation of so(5) at N = ∞, and on products with a transverse finite factor K.
   - *Consequence.* The fermionic factor of the one-loop term vanishes at every finite-N member. Its expansion starts at order ≥ (kernel dimension)/2 in the fluctuations.
3. **Stability does not discriminate (established).** The compact Hessian is indefinite: 34, 120, 340 negative eigenvalues on W and 10, 19, 19 per spacelike transverse direction for n = 1, 2, 3. In Definition (A) negative eigenvalues only change the phase.
4. **Normalisation dependence of the bosonic comparison (established in a flat local model).** The leading SUSY-breaking (mass-insertion) term per unit volume on a member with a (3,1) kinetic form behaves differently under different regulators:
   - after Wick rotation its real part is 0;
   - over an ellipsoidal cut-off with time stretch a, the real part is 2π²Λ² a/(1+a²);
   - for a positive-definite form over the same region it is 2π²Λ² a/(1+a).

   Definition (A) supplies no such cut-off at N = ∞, so no regulator-independent comparison of bosonic factors exists.
5. **Conditional route (direction of the selection; corrected in r2).** At fixed γ>0 and h_0 of signature (9,1), 060's identity γ = 3cη^{c0c0} with H = cη admits only two five-index algebras: so(5) with W spacelike (the compact members) and so(4,1) with W timelike (N = ∞ only). The latter include the conjugate-coordinate member, whose 𝖪 is Lorentzian on m ≠ 0. The base-coordinate member (so(3,2)) has γ = −3c < 0 by merged 060 (L1603), so it is **not** in the γ>0 setting.
   - If the so(4,1) members' fermion forms are non-degenerate, then within this family at one loop only members with W timelike have a non-vanishing one-loop term. For the conjugate member this means a Lorentzian 𝖪 on m ≠ 0.
   - That Lorentzian kinetic tensor is then fixed by the supplied sign of γ, the supplied h_0 and the supplied fermion content. It is not derived, and it is not identified with the emergent metric.
   - Whether the so(4,1) fermion forms have a normalisable kernel is **unresolved**. This is the open step.

Nothing here derives the family, the mass or the fermion content. Assumption ass:lorentzian is not discharged, and E (and D1) stay OPEN.

## Target and status

- **Problem E (Appendix H, sec:status-E), verbatim.** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **Ch17.** "Problem E: Lorentzian signature. OPEN; CRITICAL PATH for the matrix-derived label …". The completion item is "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})". These agree with Appendix H; no discrepancy.
- **D1 (bearing only).** Ch17 item D1: "The locked frame and its non-degeneracy on the claimed domain are derived, not assumed (ass:frame-lock, ass:nondeg)". Appendix H D is OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. This package bears on D1 only through which members survive; it makes no frame claim.
- **Original target.** Lorentzian signature derived from the matrix theory rather than retained.
- **Route.** 060 review-r2 ranked avenue 1: a one-loop comparison of the so(4,2) and so(6) members at N → ∞ and fixed γ > 0. This is the only route in that family by which the integral itself could select the real form.
- **Dependencies.**
  - 060 (family, EOM ⇔ H = cη, finite-N ⇒ definite five-index η);
  - 059 (h_0 of signature (9,1) under P1 ∧ P2);
  - Definition (A) (E ledger);
  - supplied IKKT fermion content.
- **Classification of the outcome.** PROGRAMME-CONDITIONAL (not DERIVED).
- **Current critical-path set (Ch17 completion criterion, re-derived).** A, B, C, D1, E, F, G-derived, N. H, I, J are optional. This matches the ledger.

## Source reading

- **Mode.** Digest + targeted reads. `make_digest.py --check` printed DIGEST CURRENT. The dirty files are appH and bib (060), both read.
- **Baselines verified.** appH is 590875 B, sha256 94befe3b…85c6, CRLF 3300, bare LF 0. bib is 27601 B, 645c93c9…0f67, CRLF.
- **Read in full:**
  - the Problem E entry L1482–1611, including the dirty 060 block L1588–1607 (and its proposal file appH_insert.tex);
  - ch17 E (L394–399) and the completion list (L700–740);
  - ch04 ass:lorentzian (L318–333).
- **CP^{1,2} / conjugate-class passages read:**
  - L1377–1392 (frame index; the y·y = −ℓ² − m² notation);
  - L2346–2355 (conjugate coordinates: K = (M^{45})²η);
  - L2375–2378 (base functions, □T = −3T);
  - L2383 (μ² = −3 stationarity, the mass as input);
  - L2439–2445 (Euclidean flux eigenvalues, including (ii) on so(6) with δ, where vector instabilities are not replaced by zero modes, and fermions are not treated);
  - L2446–2448 (ambient-metric contraction).
- **Headings only.** The other 045–049 / Section F CP^{1,2} paragraphs (L2366–2700) were read by headings and first lines, not in full. My insert relies only on the 060 paragraph's notation and on the cross-checks noted.
- **Labels used and verified.** ass:lorentzian (ch04, 1 occurrence). No new labels.
- **Ledger.** The 059/060 entries at the tail of reports/ledger.md were read. The SME scout reports/sme-scout-20261108-after55.md was read for one-loop leads; R2/R3 there are not this route.
- **Full scan.** Not required: no definition, assumption, scope or status passage is changed. Integration ordinal would be 59, and the 5th-item scan is due at 60.

## Research and reasoning

### 1. Setting and the one-loop term
- **Setting.** Definition (A) with S_b built from h_0 of signature (9,1), mass S_γ = −(γ/2g²) Tr A_μA^μ with γ > 0, and the Pf M(A) of the supplied MW fermion. The family is that of 060: T̄^I = L^I_a T^a, T^a = M^{a c0}, H = L^T h_0 L = cη, γ = 3cη^{c0c0}.
- **Reduction to a standard form.** Let W be spacelike. By Witt's theorem there is an isometry of h_0 mapping W to a coordinate spacelike 4-plane. It can be composed with elements of O(W^⊥) ≅ O(5,1), which meets every component of O(9,1), to lie in SO⁺(9,1). Its spin lift acts invertibly on the 16, so kernel dimensions are invariant. Hence T̄^a = √c M^{a c0} along four spacelike directions.
- **The one-loop term.** It is (bosonic Gaussian) × (ghost determinant) × Pf of the fermion form at the member. I use the conventions of Steinacker 2303.08012 (JHEP 05 (2023) 129, bib key Steinacker2023), whose regulator S → S + iε Tr ΣT² is exactly Definition (A).

### 2. Operators (s1 and s2)
- **Normalisation.** X_a = αM_{a5} with α² = c, on V_n = Sym^n C^4 with so(5) generators from the 4-dim spinor. The background satisfies Σ_b [X_b,[X_b,X_a]] = 3α² X_a (s1, residual 0).
- **Assembly.** The exact quartic Hessian was assembled from the t² coefficient of S(X̄ + tA), plus the gauge term −½Tr([X̄_μ,A^μ])² (≥ 0).
- **Comparison.** The resulting spectra were compared eigenvalue by eigenvalue with the Casimir formulas:
  - 4-block: K_A = α²(C5 − C4^tot). Residual 7e−15 (n = 1) and 2.5e−14 (n = 2). The other sign choices fail by 4–5.
  - Transverse: α²(C5 − C4 − 3). Ghost: □ = α²(C5 − C4) (residual 2e−15).
  - (Γ^a ad X_a)² on 4d Euclidean Dirac spinors: α²(C5 − C4^tot + 3/2) per chirality, with S_ab = −(i/4)[γ_a,γ_b]. Residual 1e−14. Chirality commutes with it.
- **Derivation.**
  - □ = Σ_a ad(X_a)² = α²(C5 − C4).
  - D² = □ + ½Γ^{ab} ad[X_a,X_b] = □ − α²(C4^tot − C4 − C_sp) in conventions where the S_ab obey the relations of the M_ab. The sign is fixed by the explicit check.
  - The vector term has the same structure, and the mass −3α² combines to give C5 − C4^tot.
- **Real forms.** These are identities in U(so(5)) ⊗ End(vector/spinor). By complexification they hold for every real form, with Casimirs formed with η.
- **Scale independence.** K_B ∝ c on 10(N²−1) modes contributes |det|^{−1/2} ∝ c^{−5(N²−1)}. Pf ∝ c^{4(N²−1)}. The FP determinant ∝ c^{N²−1}. Net c^0, apart from zero modes. Hence the one-loop modulus is γ-independent. This agrees with the species identity Σ w_i d_i = 0 of the appH Section F supertrace paragraph (weights 1·4, 1·n_ex, −2·1, −½·16 with n_ex = 6).

### 3. Fermion zero modes (s1, s1b, s2, s2b)
- **Branching data.**
  - End(V_n) = ⊕_{0≤m2≤m1≤n} (m1,m2), each once. This was found by Racah–Speiser for n ≤ 20, with dimension sums checked against N².
  - so(5) → so(4) Gelfand–Tsetlin: m1 ≥ k1 ≥ m2 ≥ |k2|.
  - Casimirs: C5(m1,m2) = m1(m1+3) + m2(m2+1); C4 = 2j_L(j_L+1) + 2j_R(j_R+1).
- **Identity.** Take (k1,k2) = (m1,m2) ⊗ (½,0) → j_L + ½. Then 2(j_L+½)(j_L+3/2) + 2j_R(j_R+1) = C5 + 3/2. This is symbolic (sympy, s2b), with the mirror identity for (m1,−m2) ⊗ (0,½).
- **Kernel.** K_ψ = D²/c = 0 there, and D is Hermitian, so these are kernel vectors of D.
- **Uniqueness.** For every so(5) irrep with m1 ≤ 12, integer or half-integer, exactly one left zero multiplet exists (s2b). For V_n these are the only zero modes for n ≤ 20: the counts equal the closed form, z(n) = n(n+4)(n²+4n+7)/6 per Weyl doublet and chirality.
- **10D count.** 16 = 4 × (2,1) + 4 × (1,2) under so(4) × so(5,1), so z16 = 8z(n).
  - The explicit 10D chiral-16 kernel gives 80 (n = 1) and 304 (n = 2) (s1(e)).
  - The rotated and rescaled frame gives 80. The reducible cases are V1 ⊕ V1: 368 and V1 ⊕ V0: 144.
  - Random Hermitian 4-tuples (N = 4, 6, 10) give 0 (s1b).
- **Generality.** For any non-trivial finite-dimensional representation, the image of so(5) in End(V) is a copy of the adjoint (1,1). It is injective because so(5) is simple, and traceless.
  - The left top component (1,1) → j_L = 1, j_R = 0 → (3/2,0) has dimension 4, and the right one likewise. So the kernel of the 16-component operator has dimension ≥ 4·(4+4) = 32 per copy.
  - By 060, every non-zero finite-N member has a definite five-index η, hence is of this kind. So Pf M(T̄) = 0 at every non-zero finite-N member.
  - Compact-group unitary representations at N = ∞ are direct sums of these, so the kernel persists.
  - For products with a transverse factor K, D(ψ_M ⊗ 1_K) = (D_M ψ_M) ⊗ 1 + Γ^i ψ_M ⊗ [K_i, 1] = 0.
- **Normalisation of the count (stated, not decisive).**
  - z16/(16(N²−1)) ~ 3/n² → 0 per fermionic mode.
  - z16/N ~ 8n → ∞ per unit symplectic volume (N ∝ symplectic volume).
  - The exact statement (Pf = 0) needs neither normalisation nor regulator.
- **Literature.** Zero modes of the same Casimir type for fuzzy S^4_N with five matrices: Steinacker 1510.05779 v4, Eq. (3.28). The text says "There are again zero modes (n − m, 2m + 1) for n = m … Hence supersymmetry is clearly broken". In Section 4: "these contain the zero modes, which should not be integrated out, and we will drop them". Read from the arXiv PDF (pdftotext) and verified; JHEP 12 (2015) 115, DOI 10.1007/JHEP12(2015)115.

### 4. Consequences and power counting (conditional, proposal only)
- **What is exact.** Each insertion of the Yukawa vertex ψ M(A) ψ absorbs at most two zero modes. So the fermionic integral about a compact member starts at degree ≥ z16/2 in A. This is exact degree counting.
- **Heuristic power counting.** Gaussian modes have amplitude ~ g/α, i.e. a relative factor g/(α²) ~ 3g/γ. Quartic-lifted flat modes have relative amplitude (g/γ)^{1/2}. The quadratic-flat bosonic directions other than the 24 rotation moduli are z_B' = z_A + 6(z_⊥ − 4); each costs at most (γ/g)^{1/2}.
- **Net exponent.** In the worst case the net exponent of g/γ is z16/4 − z_B'/2. It is positive for every n ≤ 20: 17.0, 5.0, 57.5 for n = 1, 2, 3, then 74801.5 at n = 20 (s2 table). It grows like n^4 against n^3.
- This is a heuristic power counting, not a proof. It also needs combinatorial control (~ (z/2)!), i.e. z·g²/γ² small. So the manuscript text states only the exact degree bound and the zero-eigenvalue counts.

### 5. Stability (s2)
- **4-block negative eigenvalues.** 34, 120, 340, …, 147146 for n = 1, 2, 3, …, 20.
- **Per spacelike transverse direction.** 10, then 19 for n ≥ 2. The timelike transverse direction has the opposite overall sign.
- **Reading.** In the oscillatory integral, a mode with λ < 0 contributes |λ|^{−1/2} e^{−iπ/4}. So the Morse index enters only the phase.
- **Agreement with 2440(ii).** The paragraph at appH L2439–2445(ii) shows, at the leading symbol, that the so(6)/δ vector sector has negative modes −|f1 − f2|. This is consistent.

### 6. Non-compact members
- **What carries over.** The Casimir identities carry over algebraically.
- **What does not.** H_n (doubleton) is infinite-dimensional, and its so(4,1) components are not finite-dimensional. Gelfand–Tsetlin top components do not exist in the same sense. Moreover the spinor of so(3,1) is non-unitary, so the "total" decomposition is not a unitary direct integral.
- **Open.** Whether the fermion form has a normalisable kernel is open.
- **Mechanism, proposal only (s4).**
  - For a real flux F, the eigenvalues of ½F_{ab}S^{ab} on a Weyl spinor are real in so(4): ±½(f1 ± f2)-type. In so(3,1) they are ±½√((B ± iE)·(B ± iE)), complex unless E·B = 0 (checked at random F).
  - Consequence: for Euclidean fluxes the lowest fermion Landau level of one chirality is an exact zero for any (f1, f2), since its Zeeman term cancels f1 + f2. This needs no self-duality, in contrast to the vector sector of L2439. For a Lorentzian flux with an electric part the would-be zero locus has real codimension 2.
  - This suggests, but does not prove, that the Lorentzian member's fermion form has no normalisable kernel from this mechanism. Classified as conjecture/mechanism; not in the insert.

### 7. Bosonic factor regulator dependence (s3)
- **Mass-insertion term.** Γ ⊃ (i/2)·10·(−γ) Tr(K0 + iε)^{-1}, so iΓ ⊃ 5γ Tr(K0 + iε)^{-1}. The real part sets the modulus.
- **Flat model.** K = −k0² + |k|², over the ellipsoid k0²/a² + |k|² ≤ Λ². Substitute k0 = a u and t = tan χ, so the angular integrand is t²/((t² − a²)(t² + 1)).
  - PV∫ dt/(t² − a²) = 0, which gives π/(1+a²). Hence Re = 2π²Λ² a/(1+a²).
  - Im (for −iε) = 2π²Λ² a²/(1+a²).
  - Euclidean: π/(1+a), hence 2π²Λ² a/(1+a).
  - The ratio is (1+a)/(1+a²). It is 1 at a = 1 and maximal, (1+√2)/2, at a = √2 − 1.
  - Wick rotation (Lorentz-invariant analytic): Re = 0.
- **Checks.** Quadrature agrees to about 1e−6.
- **Lorentz-congruent cut-offs.** For P = L^T L (L ∈ SO(3,1)) the region is the Lorentz image of the ball and k_M² is invariant, so the result equals a = 1. This is consistent with the regulator class of the Problem E paragraphs.

### Literature checked
- **Steinacker 2303.08012 (= bib Steinacker2023, JHEP 05 (2023) 129).** Abstract fetched. The HTML text was fetched for Eqs. (4.14)–(4.21), (5.5)–(5.10) and the "pre-factor i is an artefact … extra i upon evaluating the iε regularization" remark. The equation numbers are from the arXiv HTML (latest version), so the insert cites the formula without equation numbers.
- **Battista–Steinacker 2310.11126 (JHEP 01 (2024) 125).** Fetched in three parts. It uses the CP^{1,2} background T̄ = M^{a4}/R, k = −1 FLRW, with no mass term, and one-loop terms dominated by the fuzzy extra dimension K. It contains no comparison of real forms and no iε/Wick discussion (in the fetched text). It is not cited in the insert.
- **Steinacker 1510.05779 v4 (JHEP 12 (2015) 115).** Read from the PDF, Eqs. (3.20)–(3.28) and Section 4. Cited.
- **Not independently verified.** Snippet-level search leads about the Pfaffian vanishing for 2d configurations (a Nishimura talk) and fermion mass regulating zero modes (KEK talk). Not used.

## Claim classification

| Claim | Class |
|---|---|
| Casimir forms of K_A, K_⊥, ghost, D² for compact members (any rep) | established (algebraic; explicit check n = 1, 2) |
| Same identities for all real forms in the enveloping algebra | established (complexification) |
| One-loop modulus independent of c (γ) apart from zero modes | established (scaling count) |
| C4^tot = C5 + 3/2 on top components; kernel ≥ 32 per adjoint copy; Pf M(T̄) = 0 at every non-zero finite-N member | established (exact) |
| Persistence at N = ∞ (compact unitary), and on products with transverse K | established |
| V_n: decomposition, uniqueness, z16 = (4/3)n(n+4)(n²+4n+7) | established for n ≤ 20 (computation); closed form symbolic |
| Generic 4-matrix configurations have trivial kernel | numerical sample |
| Fermionic factor of the one-loop term vanishes; fermionic integral starts at degree ≥ z/2 | established |
| Suppression power (g/γ)^{z/4 − z_B'/2} or better | conjecture / heuristic (proposal only) |
| Negative modes affect only the phase in (A) | established |
| Mass-insertion real part: 0 (Wick), 2π²Λ²a/(1+a²) (ellipsoid), vs 2π²Λ²a/(1+a) Euclidean | established (flat local model) |
| Lorentzian member's local density equals the flat model | conditional (local approximation) |
| so(4,1) (W timelike) members' fermion form non-degenerate (the only non-compact real form at γ>0; base member needs γ<0) | unresolved |
| If so, within the family at γ>0 only W-timelike members have a non-vanishing one-loop term (Lorentzian 𝖪 fixed by the supplied γ>0, h_0, fermions) | conditional |
| Landau / complex-Zeeman mechanism against Lorentzian zero modes | conjecture / mechanism (proposal only) |
| h_0 (9,1), mass γ > 0, fermion content, family | inputs (supplied) |

## Proposed changes

### File 1: chapters/appH-microscopic-proofs.tex
- **Anchor.** Insert one new paragraph block immediately before the unique two-line anchor in Problem E, at L1609–1610, followed by one blank line:

  ```
  \paragraph{Status.}
  Remains Assumption~\ref{ass:lorentzian}.
  ```

  The anchor occurs exactly once (apply_check: count 1). The bytes before it end with a blank line.
- **What is kept.** Everything. No existing sentence is replaced, and the 060 block is untouched.
- **Insert text.** The text is `appH_insert.tex`, r2: 9034 B LF, sha256 08f9bb84845ecc5ef1881c5c2a246af289cd8d274cc1635491289b6ecc923a7a; pure ASCII, LF in the proposal; the integrator converts it to CRLF. The r1 bytes are kept as `appH_insert.r1.tex` (a5039fc3…f493). Verbatim:

```latex
\paragraph{One loop about the conjugate-coordinate family at fixed \(\gamma>0\): the fermion form of the finite-\(N\) members (conditional; bounded no-go).}
Keep Definition~(A) with \(h_0\) of signature \((9,1)\) in place of \(\eta\), the mass term \(S_\gamma\) with \(\gamma>0\), the fermion content of~\cite{IKKT1997}, supplied as there, and the family \(\bar T^I=L^I{}_aT^a\), \(T^a=M^{ac_0}\), \(H=L^{\mathrm T}h_0L=c\,\eta\), of the preceding paragraph. The one-loop term about a member is the Gaussian integral over the bosonic and ghost fluctuations in the background Feynman gauge times the Pfaffian of the fermion form \(\operatorname{Tr}\psi^{\mathrm T}C\Gamma_I[\bar T^I,\psi]\) at the member, as in the one-loop formula of~\cite{Steinacker2023}, whose \(\mathrm i\epsilon\) is the regulator of Definition~(A). A member whose four-plane \(W\) is spacelike is carried, by an isometry of \(h_0\) in its identity component, which acts invertibly on the spinor index, to \(\bar T^a=\sqrt c\,M^{ac_0}\) along four spacelike basis directions of a basis in which \(h_0=\eta\).

\emph{Operators of the compact members.} Let the five-index algebra be \(\mathfrak{so}(5)\), with \(W\) spacelike and \(c>0\), so that \(\gamma=3c\), and use that form. Write \(C_5\) and \(C_4\) for the Casimirs of \(\mathfrak{so}(5)\) and of its four-index subalgebra \(\mathfrak{so}(4)\) in the adjoint action on the matrices, normalised to \(4\) and \(3\) on the vector, and \(C_4^{\mathrm{tot}}\) for the Casimir of \(\mathfrak{so}(4)\) acting on the matrices and on a vector or spinor index together. The bosonic Hessian in this gauge is then \(c\,(C_5-C_4^{\mathrm{tot}})\) on the four directions of \(W\) and \(\pm c\,(C_5-C_4-3)\) on each of the six others, with the sign of \(h_0\) there; the ghost operator is \(c\,(C_5-C_4)\); and the square of \(\Gamma^a[\bar T_a,\cdot\,]\) is \(c\,(C_5-C_4^{\mathrm{tot}}+\tfrac32)\) on each Weyl spinor of \(\mathfrak{so}(4)\), of which the chiral spinor of \(\mathrm{SO}(9,1)\) contains four of each chirality (exact, with spinor generators obeying the relations of the \(M^{ab}\); checked on explicit matrices for the representations \(n=1,2\) below). The ten bosons, sixteen fermion components and two ghosts weight the scale \(c\) by \(5-4-1=0\), so that, apart from zero modes, the modulus of the one-loop term does not depend on \(\gamma\).

\emph{Fermion zero modes.} Label the irreducible components of the matrices under \(\mathfrak{so}(5)\) by \((m_1,m_2)\), \(m_1\ge m_2\ge0\), both integers or both half-integers, in the orthogonal basis, with \(C_5=m_1(m_1+3)+m_2(m_2+1)\), and those of \(\mathfrak{so}(4)\) by \((k_1,k_2)\), with \(j_{\mathrm L}=\tfrac12(k_1+k_2)\), \(j_{\mathrm R}=\tfrac12(k_1-k_2)\) and \(C_4=2j_{\mathrm L}(j_{\mathrm L}+1)+2j_{\mathrm R}(j_{\mathrm R}+1)\). The Gelfand--Tsetlin branching \(m_1\ge k_1\ge m_2\ge|k_2|\) contains \((k_1,k_2)=(m_1,m_2)\), and this component coupled to a spinor of type \((\tfrac12,0)\) contains total spin \(j_{\mathrm L}+\tfrac12\), on which \(C_4^{\mathrm{tot}}=2(j_{\mathrm L}+\tfrac12)(j_{\mathrm L}+\tfrac32)+2j_{\mathrm R}(j_{\mathrm R}+1)=C_5+\tfrac32\); likewise \((m_1,-m_2)\) with \(j_{\mathrm R}+\tfrac12\) for \((0,\tfrac12)\). On these subspaces the Hermitian operator \(\Gamma^a[\bar T_a,\cdot\,]\) vanishes. In a non-trivial finite-dimensional representation the generators are linearly independent and span a copy of the adjoint \((1,1)\) among the traceless matrices. So at every finite \(N\) the fermion form of every non-zero member has a kernel, of dimension at least \(32\) per copy of the adjoint, and \(\operatorname{Pf}\mathcal M(\bar T)=0\). By the preceding paragraph these are all the non-zero members at finite \(N\). The fermion form also has a kernel at \(N=\infty\) for every non-trivial unitary representation of \(\mathrm{Spin}(5)\), each being a direct sum of finite-dimensional ones, and on a product with a finite factor \(K\) in the transverse directions, where these modes tensored with the identity of \(K\) stay in the kernel. For \(V_n=\mathrm{Sym}^n\mathbb C^4\), which is irreducible under \(\mathfrak{so}(5)\cong\mathfrak{sp}(4)\) and has \(N=\binom{n+3}3\), the matrices are \(\bigoplus_{0\le m_2\le m_1\le n}(m_1,m_2)\), each with multiplicity one, these are the only zero modes, and the kernel has dimension \(\tfrac43n(n+4)(n^2+4n+7)\), that is \(80\) and \(304\) for \(n=1,2\), as on explicit matrices (Racah--Speiser and the branching for \(n\le20\)); random Hermitian configurations of four matrices give no kernel (sampled). The ratio of this dimension to the \(16(N^2-1)\) fermion components tends to zero like \(3/n^2\), and its ratio to \(N\), which is proportional to the symplectic volume, grows like \(8n\). Zero modes of the same Casimir type occur for fuzzy \(S^4_N\) with five matrices in the Euclidean model, where the sector containing them is left out of the one-loop potential~\cite{Steinacker2015S4} (its Eq.~(3.28) and Section~4).

\emph{Consequences for the compact members.} Since \(\operatorname{Pf}\mathcal M(\bar T)=0\) is a property of the integrand, the fermionic factor of the one-loop term vanishes at every finite-\(N\) member, whatever the regulator. Each Yukawa vertex absorbs at most two zero modes, so the fermionic integral about such a member starts at an order in the fluctuations of at least half the dimension of the kernel, and the contribution of the member is not of one-loop form. Its order in \(g_{\mathrm{YM}}/\gamma\) is not stated, since the bosonic Hessian has, besides the twenty-four zero modes of the rotations that move \(W\), further zero eigenvalues (\(6\), \(142\) and \(277\) for \(n=1,2,3\)) whose lifting is not computed. It is also indefinite, with \(34\), \(120\) and \(340\) negative eigenvalues on the traceless fluctuations along the four directions of \(W\) (the compact check of Section~\ref{sec:status-F} counts four more from the trace) and \(10\), \(19\) and \(19\) on each spacelike transverse direction for \(n=1,2,3\); in Definition~(A) negative eigenvalues change the phase of the one-loop term and not its modulus, so the sign of the fluctuation spectrum does not distinguish the moduli of the members' contributions.

\emph{Non-compact members and normalisation.} The operator identities above are identities in the enveloping algebra and hold for \(\mathfrak{so}(4,1)\supset\mathfrak{so}(3,1)\), with the Casimirs formed with \(\eta\). The non-compact members act, however, on infinite-dimensional unitary representations, whose components under the five-index algebra are not finite-dimensional, so the branching argument does not apply; whether their fermion form has a normalisable kernel is not decided here. By the zero modes, the members of this family with a non-vanishing one-loop term are at most those with a non-compact five-index algebra, which exist only for \(N\to\infty\). At fixed \(\gamma>0\) and \(h_0\) of signature \((9,1)\) the identity of the preceding paragraph admits, besides \(\mathfrak{so}(5)\), only the five-index algebra \(\mathfrak{so}(4,1)\) with \(W\) timelike, among them the conjugate-coordinate member, whose kinetic tensor is Lorentzian on \(m\neq0\); the base-coordinate member requires \(\gamma<0\) there. If the fermion forms of these members are non-degenerate, the supplied fermion content, and not the bosonic action, separates them from the compact members at one loop; the Lorentzian kinetic tensor is then fixed by the supplied sign of \(\gamma\), \(h_0\) and fermion content, not derived, and is not identified with the emergent metric. A comparison of the bosonic factors per unit volume, by contrast, depends on the regulator. The leading term in which the mass spoils the cancellation between the species is proportional to \(\gamma\operatorname{Tr}(K+\mathrm i\epsilon)^{-1}\), and its real part enters the modulus. For \(K=-k_0^2+|\vec k|^2\) on flat momenta, the real part of \(\int\mathrm d^4k\,(K+\mathrm i\epsilon)^{-1}\) is \(0\) after Wick rotation. Over the ellipsoid \(k_0^2/a^2+|\vec k|^2\le\Lambda^2\) it is \(2\pi^2\Lambda^2a/(1+a^2)\), against \(2\pi^2\Lambda^2a/(1+a)\) for \(K=k_0^2+|\vec k|^2\) over the same region (exact; numerical check), and Definition~(A) supplies no such cut-off at \(N=\infty\).

These statements are for Definition~(A) with the supplied mass, fermion content and family, one loop about the members and the background Feynman gauge. For the compact members they hold for finite-dimensional representations, exactly at every finite \(N\), and need no limit. For the non-compact members the order is \(N\to\infty\) first at fixed \(\gamma>0\), then \(\epsilon\to0\), as in the preceding paragraph. Their fermion form, the existence of that limit, the cut-off of their bosonic factor and the contributions of saddles outside the family are not treated. Nothing here derives the family, the mass or the fermion content, so Assumption~\ref{ass:lorentzian} is not discharged, and Problem~E remains open and PROGRAMME-CONDITIONAL.
```

- **Content of the six blocks.**
  1. Setting.
  2. Operators of the compact members.
  3. Fermion zero modes.
  4. Consequences for the compact members.
  5. Non-compact members and normalisation.
  6. Closing scope sentence ending "Problem~E remains open and PROGRAMME-CONDITIONAL."
- **Result after insertion.** appH 599923 B, sha256 82ab236415a5fbbea02be7ceb6eebc791e560eef4a7e589cb25be2cf9ffa279c, CRLF 3313, bare LF 0. (r1 gave 599565 B, da8be0e3…a3e.)
- **Stale passages elsewhere.** None. The 060 paragraph's sentence "The criterion is not evaluated for … one loop" stays true: this block treats the one-loop term, not the criterion. It also says "Nothing here selects the real form …", which stays true for 060's own statements.

### File 2: bib/namcg.bib
Append `bib_entries.bib` (CRLF) after a CRLF blank line:

```bibtex
@article{Steinacker2015S4,
  author  = {Steinacker, Harold C.},
  title   = {One-loop stabilization of the fuzzy four-sphere via softly broken {SUSY}},
  journal = {Journal of High Energy Physics},
  volume  = {2015},
  number  = {12},
  pages   = {115},
  year    = {2015},
  doi     = {10.1007/JHEP12(2015)115},
  eprint  = {1510.05779},
  archivePrefix = {arXiv},
  note    = {Version 4; the equation number cited refers to it}
}
```

- **Verification.** arXiv abs page (title, author, related DOI 10.1007/JHEP12(2015)115) and the PDF v4 text.
- **Result.** bib 28049 B, sha256 582f09d5a0bca24e930a8e7c130907f495e738f6d14d89809aac6f7f7e7e1f22, CRLF 937, bare LF 0. No duplicate keys.
- **Existing keys cited.** Steinacker2023 (= 2303.08012, verified) and IKKT1997.

## Verification scripts

All are in the proposal folder, with outputs saved as .txt.

- **`s1_explicit_hessian.py` → `s1_explicit_hessian.out.txt`.**
  - Explicit so(5) Sym^n reps (n = 1, 2): EOM; □ = Casimir.
  - Exact quartic Hessian plus gauge term vs the Casimir formula (all sign choices tested).
  - Transverse spectrum; D² vs the Casimir formula; chirality.
  - (e) Full 10D chiral-16 kernel: 80 and 304.
- **`s1b_generic_kernel.py` → `s1b_generic_kernel.out.txt`.** Control cases:
  - random Hermitian 4-tuples (kernel 0);
  - reducible V1 ⊕ V1 and V1 ⊕ V0;
  - a rotated and rescaled frame.
- **`s2_casimir_spectra.py` → `s2_casimir_spectra.out.txt`.**
  - Racah–Speiser plus Gelfand–Tsetlin spectra for n ≤ 20.
  - Zero and negative counts of every operator.
  - Γ_E' with zero modes omitted. This is not a weight, since Pf = 0.
  - z16, z_B' and the heuristic net exponent.
- **`s2b_zero_mode_formula.py` → `s2b_zero_mode_formula.out.txt`.**
  - Symbolic identity; closed form z(n); asymptotics.
  - Count match n ≤ 20.
  - One zero multiplet per irrep, m1 ≤ 12 (integer and half-integer).
- **`s3_mass_insertion_regulators.py` → `s3_mass_insertion_regulators.out.txt`.** Ellipsoid PV/Im/Euclidean closed forms vs quadrature, and the maximum of the ratio.
- **`s4_weyl_flux_symbol.py` → `s4_weyl_flux_symbol.out.txt`.** Weyl spin–flux eigenvalues, so(4) real vs so(3,1) complex. Mechanism only.
- **`apply_check.py` → `apply_check.txt`.** Report mode: baselines, unique anchor, hashes, refs/cites. Backslashes are built with chr(92), and it refuses to write inside the repository.
- **`tex_lint.py` → `tex_lint.txt`.** Static brace and math balance and the macro list (all macros already used in appH or amsmath).

## Decisions Taken

- **RESEARCHER-DECISION (review-r1, F1): option (a) adopted.** At fixed γ>0 the conditional is stated only for the so(4,1), W-timelike members, among them the conjugate-coordinate member.
  - The base-coordinate member is recorded as requiring γ<0.
  - The Lorentzian kinetic tensor is stated as fixed by the supplied sign of γ, h_0 and fermion content. It is not derived and not identified with the emergent metric.
  - The gatekeeper's corrected snippet is applied verbatim.
  - **Reasons.** Merged 060 L1603 gives γ = −3c, c>0, for the base presentation under h_0 (9,1), so the r1 text that included it was wrong. Option (a) keeps the fixed-γ>0 setting and order of limits of 060. It also reduces the decisive step for the infrared/full-GR route to a single member: the fermion form of the so(4,1) doubleton.
  - **Rejected: (b), widening to both signs of γ.** A comparison across the sign of a supplied parameter is not a selection, and it would reintroduce a member outside the setting of the integral studied. It is kept as ranked avenue 6.
- **F2, F3, F4: applied verbatim.**
  - F2 names the two kinetic forms, −k0²+|k|² and k0²+|k|², for which the s3 values hold.
  - F3 restricts the stability statement to the moduli.
  - F4 says traceless fluctuations and cross-references the Section F compact check (38/124/344 = 34/120/340 + 4 trace modes).
- **F5 (optional): adopted.** "unitary representation of Spin(5)". Reason: the decomposition into finite-dimensional pieces holds for integrable (group) unitary representations, so this is the precise statement.
- **F6 (build).** A scratch build was run this round (below).


- **Target: avenue 1 (one loop), not avenue 2 (saddle at N → ∞ first).**
  - Reason: it is the only route by which the integral could select the real form.
  - The compact side is exactly computable at finite N.
  - Rejected: avenue 2 first. It needs the undefined N = ∞ integral before any comparison.
- **Decisive datum: the Pfaffian (exact, regulator-free), not a per-volume bosonic free energy.**
  - Reason: s3 shows that the bosonic per-volume comparison is decided by the regulator; Wick gives 0.
  - The instruction asked that such a normalisation dependence be stated as a premise. It is stated, and the exact statement avoids it.
  - Rejected: declaring a winner from bosonic one-loop free energies under a chosen cut-off.
- **Power counting in g/γ: kept out of the manuscript.**
  - Reason: it depends on how the extra bosonic zero eigenvalues are lifted, which is not computed.
  - The insert states only the exact degree bound and the counts.
- **Lorentzian zero-mode mechanism (s4): kept out of the manuscript.** Reason: it is symbol-level and unproved. It is recorded here as the top open avenue.
- **Placement.** Problem E, immediately after the 060 block. Reason: it continues that block's family and order of limits. Rejected: Section F (one-loop coefficients). This is a selection statement, not a coefficient.
- **Citation of 2303.08012 without equation numbers.** Reason: the equation numbers were read from arXiv HTML, and the bib entry is the JHEP version.

## No-go fork: hypotheses and relaxations

**Hypotheses of the compact-member no-go:**
- (a) Definition (A) with IKKT MW fermion and no fermion mass;
- (b) the 060 family (four generators with exact Lie relations, isotropic h_0-contracted mass);
- (c) a finite-dimensional (or compact unitary) representation;
- (d) spacelike W.

| Relaxation | Effect / status |
|---|---|
| Fermion mass or SUSY-preserving mass deformation (polarised-IKKT-type) | would lift the zero modes; outside Definition (A) content; not explored (supplied input) |
| Transverse factor K (products) | explored: zero modes persist (exact) |
| Reducible reps, rotated/scaled frames | explored: persist (s1b) |
| Non-compact five-index algebra (N = ∞; at γ>0 only so(4,1), W timelike) | the open step; mechanism suggests no kernel for Lorentzian flux (s4) |
| Approximate finite-N truncations of so(4,1) (060 avenue 4) | not explored; would test whether near-Lorentzian finite-N configurations escape the zero modes |
| Higher-order lifting (g/γ power) | heuristic counting only (s2) |

**Ranked open avenues:**
1. Normalisable kernel of the fermion form on End(H_n) for the so(4,1) ⊂ so(4,2) doubleton (conjugate) member at γ>0, the only non-compact real form in the γ>0 family. Use the so(4,1) Plancherel decomposition of End(H_n), or the leading-symbol Landau analysis with electric flux. This decides whether the one-loop selection is real.
2. Approximate finite-N truncations of so(4,1): whether near-Lorentzian finite-N configurations evade the adjoint-copy zero modes, i.e. relaxing the exact Lie relations of hypothesis (b). r1's avenue 2, separating the base member, is withdrawn at γ>0. A comparison across the sign of γ, which brings the base member back, is avenue 6, and it would not be a selection, since the sign of γ is supplied.
3. The order in g/γ of the compact members' first contribution: lifting of the 6, 142, 277, … extra bosonic zero eigenvalues.
4. A fermion mass or SUSY-preserving deformation lifting the zero modes (relaxing hypothesis (a); this would be supplied content).
5. A cut-off for the N = ∞ bosonic factor derived from Definition (A) at large finite N.
6. Comparison across the sign of γ (base-coordinate member at γ<0), and saddles outside the family (commuting, Liao-type).

## Milestone assessment

- **M2 (bounded no-go), non-stopping.**
  - New exact no-go: every non-zero finite-N member of the 060 family is a Pfaffian zero, so none contributes at one loop.
  - It removes the compact real form from the one-loop competition within the family and hypotheses.
  - It is accompanied by a conditional route: a selection by the supplied fermion content, toward non-compact real forms, if the non-compact fermion forms are non-degenerate.
- **Not M1.** Nothing about E is derived; the family, mass and fermions are supplied, and the non-compact kernel is open.
- **Not M3.** No merged claim is found false. 2440(ii) concerns bosonic vectors and is consistent.
- **Not M4 or M5.**
- **Not a breakthrough.**

## Status-label recommendation

- **Current critical-path set from Ch17 and Appendix H.** A, B, C, D1, E, F, G-derived, N.
- **Affected.** E (and D1 indirectly). Both remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.
- **No change recommended.**

## Author decision needed

None.

## Remaining open step

To turn the conditional route into a one-loop selection:
1. Show that the fermion form on the Lorentzian (so(4,2) doubleton) member has no normalisable kernel, or compute its zero-mode density per unit symplectic volume.
2. Define the N = ∞ one-loop comparison (order N → ∞, then ε → 0, at fixed γ > 0) without a supplied cut-off.

Even then, the family, h_0, mass and fermion content remain supplied, so E's original target (Lorentzian signature derived) would still need these to be derived.

## Special instructions for the gatekeeper

- **Re-run** s1 (about 1 min), s1b, s2 (n list as in the output), s2b, s3, s4 and apply_check.
- **Check the sign choice in s1.** Gauge-term sign −1 means G2 = −½Tr g² ≥ 0. Casimir sign s = −1 gives K_A = c(C5 − C4^tot) after the mass.
- **Check the identity** C5 + 3/2 = C4(j_L + ½, j_R) for (k1,k2) = (m1,m2) by hand.
- **Check the decomposition** 16 → 4(2,1) + 4(1,2). It is supported by 80 = 8·10 in the explicit 10D kernel.
- **What must not be asserted:**
  - that the Lorentzian member is selected;
  - that any signature is derived;
  - that the non-compact fermion form is non-degenerate;
  - any power of g/γ for the compact members;
  - that the per-volume bosonic comparison has a regulator-independent sign.
- **The isometry/Witt step** (reduction of a general spacelike-W member to standard form in the identity component) should be re-derived.
- **The flat-model regulator formulas** are for a local model of the mass-insertion density, not for the actual CP^{1,2} operator. The insert says "for a kinetic form … on flat momenta".
- **Build (r2): PASS.**
  - The git-tracked files plus the r2-patched appH and bib were copied into the scratchpad, outside the repository, and built with pdflatex, bibtex, pdflatex, pdflatex. All passes exited 0.
  - Results: 374 pages; 0 undefined references or citations; 0 multiply-defined labels; no bibtex warnings. Steinacker2015S4 is present in the .bbl (build_r2.txt).
  - In r1 the build command was denied, and it was not worked around.
