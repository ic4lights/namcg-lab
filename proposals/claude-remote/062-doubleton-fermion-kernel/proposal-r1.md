# Proposal 062-doubleton-fermion-kernel, round 1

## Result

The question that 061 ranked first and called decisive is decided here, in one stated class of operators. It asks whether the fermion form Γ^a[T̄_a,·] of the so(4,1) ⊂ so(4,2) doubleton member at γ>0 has a normalisable kernel.

**Theorem (conditional on the class; established within it).**
- *Setting.*
  - Definition (A) with h_0 of signature (9,1).
  - The supplied IKKT fermion and a supplied γ>0.
  - The 060 member T̄^a = √c M^{a4}, a = 0..3, on a doubleton (ladder) representation H_n of so(4,2), any n. Here W is timelike, c>0 and γ = 3c. Any frame L with H = L^T h_0 L = cη is reduced to this one by an isometry of h_0.
- *Class (premise).* Fermion fluctuations are Hilbert–Schmidt operators on H_n, with inner product Tr ψ†ψ, tensored with the 16. The form is taken on vectors that are smooth for the adjoint Spin(4,1) action.
- *Conclusion.* In that class the fermion form has **no kernel**: Pf-degeneracy by normalisable zero modes, which kills every compact member (061), does not occur for the Lorentzian doubleton member.

**Mechanism (established).**
- On each chirality, D_−D_+ = c(C5 − C4 − 2X) with X = σ·J_L. This is 061's identity in η-formed Casimirs.
- For the Lorentzian real form, J_L = ½(J ∓ iK) is not Hermitian, and 4J_L² = C4 ± 2iP with P = J·K.
- So a kernel vector must satisfy two separate conditions:
  - P = 0;
  - 1 + C4 = (C5 − C4 + 1)² ≥ 0, a real condition.
- On the unitary principal series of SL(2,C) (C4 = k² − p² − 1, P = ±kp) these force p = 0. That is a countable set of representations.

**Representation-theoretic input (established from verified sources plus a derivation given here).**
- HS(H_n) restricted to the four-index Spin(3,1) ≅ SL(2,C) lies in a multiple of the regular representation of SL(2,C).
  - The route: H_n|Poincaré is massless and irreducible (Mack–Todorov). Pairs of non-collinear null vectors have compact stabiliser U(1).
- The Plancherel measure of SL(2,C) is counting × density × Lebesgue on the principal series. It gives the p = 0 set measure zero, so ψ = 0.
- For n = 0 there is a second route, independent of Mack–Todorov: Manta–Steinacker Eqs. (11)–(12) plus Naimark's tensor-product decomposition (Martin-Dussaud Eq. (308)).

**Not established (precisely stated ambiguity and open steps).**
- **The class matters.** In B(H_n) the kernel contains 1 ⊗ χ for every constant spinor χ: at least 16 modes, the analogue of the trace mode. The full bounded kernel is not computed.
- **No bounded inverse.** A trivial kernel does not give a bounded inverse. Whether 0 lies in the continuous spectrum of D_±, how the N = ∞ Pfaffian is defined, and whether it vanishes are all **unresolved**.
- **The 061 conditional.** Its hypothesis ("fermion forms of the W-timelike members non-degenerate") now holds for the doubleton members *in the kernel sense*. Its conclusion, a one-loop separation, still needs a defined non-zero N = ∞ Pfaffian, so it is **not** established.
- **Not treated.** Non-smooth kernel vectors, members on other unitary representations of so(4,1), and products with K.
- **Nothing derived.** Nothing here derives the family, h_0, γ or the fermions. ass:lorentzian is not discharged, and E (and D1) stay OPEN.

## Target and status

- **Problem E (Appendix H, sec:status-E), verbatim.** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **Ch17 (L394–399).** "Problem E: Lorentzian signature. OPEN; CRITICAL PATH for the matrix-derived label." The completion item (L718) is "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})." This agrees with Appendix H; no discrepancy.
- **D1 (bearing only).** Ch17 L335–342 and L712–717: the locked frame and its non-degeneracy are to be derived (ass:frame-lock, ass:nondeg). Appendix H D is OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. This package makes no frame claim.
- **Original target.** Lorentzian signature derived from the matrix theory, not retained.
- **Route.** 061 review-r2, ranked avenue 1 ("DECISIVE"): the normalisable kernel of the fermion form for the so(4,1) ⊂ so(4,2) doubleton member at γ>0.
- **Dependencies.**
  - 061: the compact zero modes, the operator identities and the conditional statement;
  - 060: the family, H = cη, γ = 3cη^{c0c0}, and the Lorentzian member existing at N = ∞ only;
  - 059: h_0 (9,1) under P1 ∧ P2;
  - Definition (A);
  - supplied fermions.
- **Classification.** PROGRAMME-CONDITIONAL (not DERIVED).
- **Current critical-path set (Ch17 completion list L700–735, re-derived).** A, B, C, D1, E, F, G-derived, N. H, I, J are optional. This matches the ledger.

## Source reading

- **Mode.** Digest + targeted reads. `make_digest.py --check`: DIGEST CURRENT, `dirty-chapters: yes` (appH and bib from 061, as the orchestrator stated).
- **Full scan.** Not done and not required: no definition, assumption, scope or status passage is changed (rule 3(c) is not triggered). The integration ordinal would be 60, so the gatekeeper's 5th-item full scan is due before integration.
- **Baselines verified.**
  - appH: 599923 B, sha256 82ab2364…279c, CRLF 3313, bare LF 0.
  - bib: 28049 B, 582f09d5…1f22, CRLF 937.
- **Read in full.**
  - The Problem E entry, appH L1482–1624: Ledger label; Definition (A) paragraph; Fourier; linear contours; regulator; positive mass; other signatures (059); the 060 block L1588–1607; the 061 block L1609–1620; Status.
  - The 061 proposal-r2 and review-r2, and the 060/061 ledger entries.
  - Ch17 L330–345 (D1), L392–399 (E), L700–735 (completion list).
  - Ch04 L314–336 (ass:lorentzian).
- **CP^{1,2} / conjugate-class passages read.**
  - L1088–1096 (doubleton / MantaSteinacker2025);
  - L2364 (conjugate coordinates, T^a = M^{a4}/R, y = M^{μ5}/R, η_6 = diag(−,+,+,+,+,−));
  - L2476–2478 (Casimir notation C42, C41, C31);
  - L2505–2512 (fibre cutoffs; "principal series of SO(4,1)" admissible modes and the footnote on End(H_n), stated there as plausible, not investigated).
- **Labels used.** ass:lorentzian (ch04, 1 occurrence). No new labels.
- **Cites.** MantaSteinacker2025 already exists. Four new keys, none duplicated: MartinDussaud2019, FioresiYuncken2024, MackTodorov1969, Todorov2019.
- **SME scout.** The latest, reports/sme-scout-20261108-after55.md, was grepped for fermion, zero-mode, doubleton and so(4,1) leads; none bears on this route.

## Research and reasoning

### 0. Premises

- **(P-class) End(H) := HS(H_n).**
  - The fermion fluctuation ψ is a 16-component spinor of Hilbert–Schmidt operators. The inner product is Σ Tr ψ_α†ψ_α, and the fermion bilinear Tr ψ^T CΓ_I[T̄^I, χ] is defined, since a product of two HS operators is trace class.
  - "Normalisable" means "in this Hilbert space".
  - The alternative B(H_n) is discussed in §5.
- **(P-dom)** The kernel is taken on HS^∞ ⊗ 16. HS^∞ is the space of vectors smooth for the adjoint action ψ ↦ U(g)ψU(g)^{−1} of Spin(4,1) = Sp(1,1) ⊂ SU(2,2), the group generated by the five-index algebra.
- **Order of limits and γ.**
  - The member exists only at N = ∞ (060). The statement concerns the operator at the member: N → ∞ is taken first at fixed γ>0, and γ is supplied.
  - The ε of Definition (A) multiplies Σ Tr A_μ², so it acts on the bosons only and does not enter the fermion form.
- **Reduction of the frame.** A member T̄^I = L^I_a T^a with H = L^T h_0 L = cη has h_0-orthonormal frame vectors L e_a/√c spanning a timelike W.
  - Any isometry Λ ∈ O(9,1) carrying the standard frame to it lifts to Pin(9,1), which acts invertibly on the 32.
  - Since SΓ^I S^{−1} = ±Λ^I_J Γ^J, the lift maps the kernel on the 16 for one member to the kernel on the 16 or the 16' for the other.
  - Both chiralities are treated below, so a time-orientation-reversing Λ is harmless.
- **Reduction to Weyl operators.**
  - Under so(3,1)_W × so(6)_{W^⊥} (W^⊥ positive definite, by 060), 16 = (2,1;4) ⊕ (1,2;4̄). Γ^a (a ∈ W) acts as σ^a or σ̄^a ⊗ 1.
  - So ker(Γ^a ad T̄_a on 16 ⊗ HS^∞) = 4·ker D_+ ⊕ 4·ker D_−.
  - The form Tr ψ^T C(·) pairs HS non-degenerately, so the form is degenerate iff this kernel is non-zero.

### 1. Algebra (s1)

- **Signature-independent derivation.** Take generators M_AB with [M,M] relations for a diagonal g, T_a = M_{a4}, and {γ^a,γ^b} = 2g^{ab}.
  - Then D² = g^{ab} adT_a adT_b + ¼[γ^a,γ^b] ad[T_a,T_b], with [T_a,T_b] = −i g_{44} M_{ab} (g_{44} = +1 here).
  - So D² = (C5 − C4) − (C4^tot − C4 − C_sp), with spin generators obeying the M-relations. With C_sp = 3/2 on either Weyl spinor, D² = C5 − C4^tot + 3/2. This is 061's identity, now with η.
- **The X form.** On the (½,0) block:
  - C4^tot = 2(J_L + σ/2)² + 2J_R² = C4 + 2σ·J_L + 3/2, so D_−D_+/c = C5 − C4 − 2X with X = σ·J_L.
  - With su(2)-normalised J_L ([J_L^i, J_L^j] = iε J_L^k, true for J_L = ½(J ∓ iK) with the Lorentz relations), (σ·J_L)² = J_L² + iσ·(J_L × J_L) = J_L² − X.
  - Also 4J_L² = (J ∓ iK)² = C4 ∓ 2iP, P = J·K (using [J_i, K_i] = 0).
- **Check (s1).** On the Weyl-trick finite-dimensional representations of so(4,1) (Sym^n of the so(5) spinor, n = 1, 2, adjoint on End V):
  - all identities hold to 4e−15;
  - controls with the wrong sign fail by 2–6;
  - the chirality fixes the sign of P.
  - The generators satisfy the relations with the overall sign opposite to Manta–Steinacker Eq. (1); this is equivalent under M → −M and does not affect any Casimir.
  - These non-unitary finite-dimensional representations do have kernels: dim ker D_± = 12 (n = 1) and 40 (n = 2). That is 061's z(n) = 10, 38 plus the 2 trace modes. Real j_L, as here, permits zero modes.
- **The key step.** Let ψ ∈ HS^∞ ⊗ C² with D_+ψ = 0 (the D_− case is the mirror).
  - Then (C5 − C4 − 2X)ψ = 0. Put A := C5 − C4, symmetric on HS^∞ and commuting with X, C4 and P.
  - 2Xψ = Aψ ⇒ 4X²ψ = 2XAψ = A·2Xψ = A²ψ. With X² = J_L² − X: (4J_L² − 2A − A²)ψ = 0.
  - That is Bψ = ±2iPψ (the sign is fixed by the chirality), with B := 1 + C4 − (A+1)².
  - B and P are symmetric and commute on HS^∞, so ⟨Bψ,Pψ⟩ = ⟨ψ,BPψ⟩ = ⟨ψ,PBψ⟩ = ⟨Pψ,Bψ⟩ is real.
  - Then ‖Bψ‖² = ⟨Bψ, ±2iPψ⟩ = ±2i·(real), so ‖Bψ‖² = 0, hence Bψ = 0 and Pψ = 0.
- **Compact contrast.** For so(4) compact, J_L is Hermitian and 4J_L² = C4 + 2P' with P' real. There is no imaginary part to separate, and the condition A = 2x has real solutions: the 061 top components.

### 2. Spectral form (functional analysis; established, standard)

- **Self-adjoint extensions.** Decompose HS as a direct integral over Spin(4,1), and separately over Spin(3,1); both are type I groups.
  - On smooth vectors, central elements act fibrewise by the scalars χ_π(Ω). This follows from Stone's theorem for decomposable one-parameter groups, applied iteratively, and the scalar action of Z(U(g)) on smooth vectors of irreducible unitary representations.
  - So C5, C4 and P (each symmetric, hence with real scalars) extend to decomposable self-adjoint operators.
- **Strong commutation.**
  - The spectral projections of C4 and P lie in the centre of U(Spin(3,1))''.
  - Those of C5 commute with all U(g), g ∈ Spin(4,1) ⊃ Spin(3,1), so they lie in U(Spin(3,1))'.
  - Hence the three operators strongly commute and have a joint spectral measure. Polynomials in them agree on HS^∞ with the algebraic operators.
- **Support.** Bψ = 0 means ψ ∈ E({b = 0}) with b(c5,c4) = 1 + c4 − (c5 − c4 + 1)². Pψ = 0 means ψ ∈ E_P({0}).
  - So ψ ∈ E_{(C4,P)}(S'), with S' := {p = 0, 1 + c4 ≥ 0}, since b = 0 ⇒ 1 + c4 = (real)² ≥ 0.
- **Unitary dual and Casimirs (s2(i)).** The unitary dual of SL(2,C) consists of the principal series, the complementary series and the trivial representation (Martin-Dussaud §7.1–7.2, citing Gel'fand–Naimark).
  - On the principal series D(p,k), Eq. (297) there gives K² − J² = p² − k² + 1 and K·J = pk.
  - s2(i) rederives this independently from the Freidel–Livine realisation (hep-th/0205268 Eq. (6.3)), with first-order differential operators in z and z̄: J² − K² = j² − ρ² − 1 and J·K = −jρ, symbolic and exact. It also gives 4J_L² = (j + iρ)² − 1.
  - **Preimage of S'.** pk = 0 and k² − p² ≥ 0 force p = 0 (if k = 0 then −p² ≥ 0). So within the principal series, S' consists of {D(0,k) : k ∈ ½Z≥0}, a countable set.
  - Complementary series satisfy the algebraic condition (1 + C4 = r² > 0, P = 0). They are excluded below by the Plancherel support, not by algebra.

### 3. HS(H_n) restricted to Spin(3,1)

**Route 1 (all n).**
- **(a) The Poincaré subalgebras.** In our basis, with η_6 = diag(−,+,+,+,+,−) as in appH L2364 and Manta–Steinacker Eq. (1), {M^{μν}, M^{μ4} ± M^{μ5}} are Poincaré subalgebras containing exactly the four-index so(3,1) of the member (s2(iii), exact).
- **(b) Irreducibility.** The ladder representations of U(2,2), at fixed helicity, "[are] irreducible and remain irreducible when restricted to the Poincaré subgroup". This is Todorov 1905.13009, Bulg. J. Phys. 46 (2019) 117, read from source (Sect. 1, after Eq. (1.15), with p⁰ = |p| in (1.14)), citing Mack–Todorov J. Math. Phys. 10 (1969) 2078.
  - The Mack–Todorov record was verified via Crossref (DOI 10.1063/1.1664804). Its text was **not** read.
- **(c) Identification of H_n.** H_n are the "doubletons or minireps" of SO(4,2) (Manta–Steinacker, read), i.e. the minimal, ladder, representations (Todorov). For n = 0 this is the massless scalar (MS: "H_0 can be interpreted as space of massless scalar fields on Minkowski space").
  - The matching of our Lorentz subalgebra to Mack–Todorov's is by conjugacy. SO_0(4,2) acts transitively on (1,1)-planes in R^{4,2}: Witt, plus the fact that O(1,1) × O(3,1) meets every component of O(4,2). It is implemented unitarily on H_n.
  - The identification of Manta–Steinacker's H_n with the ladder representation of helicity ±n/2 is taken from the literature (MS; Fernando–Günaydin 0908.3624, abstract read). It is not re-derived. For n = 0 Route 2 removes this dependence.
- **(d) Wigner.** A massless irreducible Poincaré representation, restricted to SL(2,C), is L² of sections of a line bundle over a null cone C, with Lorentz-invariant measure d³p/|p| and Wigner phases. The same holds for H̄_n, with the conjugate character. Hence HS(H_n) ≅ H_n ⊗ H̄_n = L² sections over C × C.
- **(e) Orbits (s2(iv)).** The collinear pairs have measure zero.
  - For a non-collinear pair (p,q), the stabiliser in so(3,1) is one-dimensional with imaginary eigenvalues, i.e. a rotation in span(p,q)^⊥. In SL(2,C) it is U(1), which is compact.
  - The stabiliser of p acts transitively on {q: q² = 0, p·q = −s} (orbit-map rank 2 = dimension of the level set). So the orbits are exactly the level sets of p·q.
  - A smooth global section s ↦ (p_0, q_s) gives a G-equivariant diffeomorphism R_{>0} × G/U(1) ≅ (non-collinear pairs).
  - By uniqueness of the invariant measure on G/U(1) (G unimodular, U(1) compact), the measure is ρ(s)ds ⊗ dμ_{G/U(1)}.
  - Hence HS(H_n)|Spin(3,1) ≅ L²(R_{>0}) ⊗ Ind_{U(1)}^{G} χ.
- **(f) Inclusion in the regular representation.** For compact M, Ind_M^G χ ≅ {f ∈ L²(G): f(gm) = χ(m)^{−1} f(g)} is a closed left-invariant subspace of L²(G). So HS(H_n)|Spin(3,1) ⊂ ∞·λ_G.
- **(g) Plancherel.** Fioresi–Yuncken 2403.17180 Theorem 7.1, read from source: L²(SL(2,C)) = ∫ L²(H_{μ,λ}) dm over the unitary principal series, with dm = ½|μ + iλ|² dμ dλ (counting × Lebesgue).
  - Any countable set of irreducibles therefore has m-measure 0, independently of how their labels are matched to Martin-Dussaud's (p,k).
  - Complementary series and the trivial representation are outside the support. Herb–Sally 1101.3753 also states that the complementary series are omitted from the Plancherel support for complex groups.
- **(h) Conclusion.** On ∞λ, E_{(C4,P)}(S') = ∫ 1_{S'}(χ(π)) dm(π) = 0. An invariant subspace reduces this central projection. So E(S') = 0 on HS(H_n) ⊗ C², and ψ = E(S')ψ = 0.

**Route 2 (n = 0, independent of Mack–Todorov).**
- **Casimirs on H_0.** Manta–Steinacker Eqs. (11)–(12), read: ½M_{μν}M^{μν} = −1 − r^{−2}X_4² = −1 − (M^{45})², and ε M M = 0.
  - So every Spin(3,1) constituent of H_0 has C4 ≤ −1 and P = 0. By the dual above, it is D(p,0): complementary series have C4 ∈ (−1,0), and the trivial representation has C4 = 0.
- **Conjugates.** The conjugate of a principal series has the same real Casimirs, so it is again D(±p,0).
- **Tensor products.** Martin-Dussaud Eq. (308) gives D(p1,k1) ⊗ D(p2,k2) = ∫_R dp ⊕_k D(p,k), a decomposition over Lebesgue measure in p (stated there, attributed to Naimark; not independently re-derived).
- **Result.** HS(H_0)|Spin(3,1) = ∫∫ D(p1,0) ⊗ D(p2,0) is a direct integral of principal series, absolutely continuous in p, whatever the measure of H_0's own decomposition. So the countable set {p = 0} is null, and ψ = 0.

### 4. What is not needed, and how far the result reaches

- **No so(4,1) decomposition needed.** The so(4,1) decomposition of End(H_n) is not needed. Manta–Steinacker state that H_0 is irreducible under SO(4,1), in the minimal discrete class Π_{1,0} of Dixmier. Appendix H L2508 records "principal series of SO(4,1)" as the admissible modes, with the identification "plausible, not investigated".
  - The argument works through the Spin(3,1) spectral measure of the whole HS space, so it holds whatever Spin(4,1) series occur.
  - It does **not** claim that every individual Spin(4,1) irreducible π has a kernel-free fibre operator on H_π ⊗ C².
  - As a corollary, no π occurring in HS(H_n) restricts to Spin(3,1) with a discrete summand, since ∞λ has none.
- **Other members (proposal only; not in the insert).** The argument uses only "HS(H)|Spin(3,1) ⊂ ∞λ". This also holds for H a unitary principal series of Spin(4,1):
  - Realise it on L²(S³), the conformal boundary of H⁴.
  - The Spin(3,1) fixing e_4 has two open orbits, each ≅ H³ = Spin(3,1)/Spin(3), with compact stabiliser, plus a null equator.
  - So H|Spin(3,1) ⊂ ∞λ, and HS(H) = H ⊗ H̄ ⊂ ∞λ by Fell absorption.
  - Classified **conditional (sketch; the unitary norm of the principal series as the L² norm on S³ is assumed standard, not verified from a source here)**.
  - Complementary and discrete series of Spin(4,1), used as H, remain open; Speh–Venkataramana-type discrete components are possible there (not verified).

### 5. The class: bounded operators, and the spectrum at zero

- **B(H_n).** D_±(1 ⊗ χ) = σ^a χ ⊗ [T̄_a, 1] = 0.
  - Since H_n is irreducible under so(4,1) (Manta–Steinacker, for H_0 explicitly, and "like all doubleton irreps"), the commutant is C1, and these are the only kernel elements of the form "commutant ⊗ constant spinor".
  - That gives 2 per Weyl block, i.e. 16 on the 16, the analogue of the u(1) trace mode removed at finite N by tracelessness.
  - Other bounded kernel vectors, such as massless "on-shell" operators, are **not computed**.
- **Spectrum at 0 (conjecture/mechanism, proposal only).** D_± = adT̄_0 ± σ·adT̄ is symmetric on HS^∞ ⊗ C², since σ^a is Hermitian and ad T̄_a is symmetric.
  - In the Poisson limit its symbol is ξ_0 ± σ·ξ, which vanishes on the null cone.
  - So 0 is expected in the continuous spectrum, and the N = ∞ Pfaffian then needs a definition (a regulator or a finite-N truncation).
  - This is the precise remaining ambiguity of the one-loop route.

### Literature checked vs not verified

- **Read from source (PDF text):**
  - Martin-Dussaud 1902.08439 v3: §7.1–7.2, Eqs. (258)–(261), (297), (308).
  - Fioresi–Yuncken 2403.17180 v1: §7.1, Theorem 7.1.
  - Manta–Steinacker 2502.02498 v1: Eqs. (1)–(12), §2.1–2.2.
  - Todorov 1905.13009: §1, Eqs. (1.14)–(1.15), reference [MT].
  - Freidel–Livine hep-th/0205268: Eq. (6.3), used in s2.
  - Herb–Sally 1101.3753: §1.
- **Abstract only:** Fernando–Günaydin 0908.3624 (DOI 10.1063/1.3447773).
- **Record only (Crossref), text not read:** Mack–Todorov 1969 (DOI 10.1063/1.1664804); Harish-Chandra, Trans. AMS 76 (1954) 485.
- **Not independently verified:**
  - Naimark's proof of (308);
  - the Gel'fand–Naimark classification (taken from Martin-Dussaud);
  - the n > 0 identification H_n ↔ ladder representation of helicity n/2.

## Claim classification

| Claim | Class |
|---|---|
| D² = C5 − C4^tot + 3/2 with η-Casimirs; D_−D_+/c = C5 − C4 − 2X; X² + X = J_L²; 4J_L² = C4 ± 2iP | established (derivation; s1 check n = 1, 2) |
| Wψ = 0, ψ smooth ⇒ Bψ = Pψ = 0 | established (algebra plus symmetry) |
| Casimirs extend to strongly commuting self-adjoint operators; ψ ∈ E_{(C4,P)}(S') | established (standard direct-integral theory) |
| Principal-series Casimirs k² − p² − 1, ±kp; S' ∩ principal = {p = 0} | established (Martin-Dussaud (297); s2(i) rederivation) |
| {M^{μν}, M^{μ4} ± M^{μ5}} Poincaré subalgebras | established (s2(iii)) |
| H_n|Poincaré massless irreducible | established in the literature (Mack–Todorov via Todorov 2019); identification of H_n with the ladder representations taken from the literature |
| Pair stabiliser U(1), orbits = level sets, HS(H_n)|Spin(3,1) ⊂ ∞λ | established (derivation; s2(iv) numerical check) |
| Plancherel support on principal series, atomless | established (Fioresi–Yuncken Thm 7.1) |
| **No normalisable (HS, smooth) kernel of the fermion form for the doubleton member, every n** | **conditional on (P-class), (P-dom); established within them** |
| n = 0 via Manta–Steinacker (11)–(12) and Eq. (308) | established, modulo Naimark's (308) as stated in a verified source |
| B(H_n) kernel contains 1 ⊗ χ (16 modes) | established |
| Full bounded kernel | unresolved |
| 0 in the continuous spectrum of D_± | conjecture (symbol-level) |
| N = ∞ Pfaffian defined and non-zero; one-loop separation of the W-timelike members | unresolved |
| Same conclusion for H a unitary principal series of Spin(4,1) | conditional (sketch, proposal only) |
| Complementary/discrete-series members, non-smooth kernel vectors, products with K | unresolved |
| h_0 (9,1), γ > 0, fermion content, family | inputs (supplied) |

## Proposed changes

### File 1: chapters/appH-microscopic-proofs.tex
- **Anchor.** Insert one paragraph block immediately before the unique two-line anchor of Problem E (L1622–1623), followed by one blank line, i.e. directly after the 061 paragraph (whose closing sentence ends "Problem~E remains open and PROGRAMME-CONDITIONAL."):
  ```
  \paragraph{Status.}
  Remains Assumption~\ref{ass:lorentzian}.
  ```
  apply_check reports count 1, line 1622, and the preceding bytes end with a blank line.
- **What is kept.** Everything; no existing sentence is replaced.
- **Insert text.** `appH_insert.tex`: 6350 B LF, sha256 8f7c27f5ce2c385e63ee4504d93f9d92bf37dff9aa415edff3851e89915d8902; ASCII; CRLF 6360 B, 7a724912…e275. Verbatim:

```latex
\paragraph{The fermion form of the doubleton member at fixed \(\gamma>0\) (conditional on the class of operators; bounded result).}
Keep the setting of the preceding paragraph and take the member with \(T^a=M^{a4}\), \(a=0,\dots,3\), on a doubleton representation \(\mathcal H_n\) of \(\mathfrak{so}(4,2)\)~\cite{MantaSteinacker2025}, with \(W\) timelike, \(c>0\) and \(\gamma=3c\). The fermion fluctuations are taken to be Hilbert--Schmidt operators on \(\mathcal H_n\), with the inner product \(\operatorname{Tr}\psi^\dagger\psi\), times the spinor index, and the form is taken on the vectors that are smooth for the adjoint action of \(\mathrm{Spin}(4,1)\). Both are premises, since whether a kernel is normalisable depends on them. Under \(\mathfrak{so}(3,1)\times\mathfrak{so}(6)\) the chiral spinor of \(\mathrm{SO}(9,1)\) consists of four copies of \((\tfrac12,0)\) and four of \((0,\tfrac12)\), so the form is non-degenerate exactly when the Weyl operators \(\mathcal D_+\psi=\sigma^a[\bar T_a,\psi]\) and \(\mathcal D_-\psi=\bar\sigma^a[\bar T_a,\psi]\), with \(\sigma^a=(1,\vec\sigma)\) and \(\bar\sigma^a=(1,-\vec\sigma)\), have trivial kernels. A member with another frame \(L\) is carried to this one by an isometry of \(h_0\), whose lift acts invertibly on the spinor and maps each chirality to one of the two.

\emph{Algebra.} On one chirality the identity of the preceding paragraph reads \(c^{-1}\mathcal D_-\mathcal D_+=C_5-C_4-2X\), where \(C_5\) and \(C_4\) are now the Casimirs of \(\mathfrak{so}(4,1)\) and \(\mathfrak{so}(3,1)\) formed with \(\eta\), \(X=\tfrac12(C_4^{\mathrm{tot}}-C_4-\tfrac32)=\vec\sigma\cdot\vec J_{\mathrm L}\), and \(\vec J_{\mathrm L}=\tfrac12(\vec J\mp\mathrm i\vec K)\) is formed from the rotations \(\vec J\) and boosts \(\vec K\) of \(\mathfrak{so}(3,1)\) in the adjoint action; the other chirality has \(\vec J_{\mathrm R}\) in its place. Then \(X^2+X=\vec J_{\mathrm L}^2\) and \(4\vec J_{\mathrm L}^2=C_4\pm2\mathrm iP\), with \(P=\vec J\cdot\vec K\) and the sign fixed by the chirality (checked on explicit finite-dimensional representations of the real form \(\mathfrak{so}(4,1)\)). Let \(\psi\) be in the kernel and put \(A=C_5-C_4\). Then \(2X\psi=A\psi\), so \(4X^2\psi=A^2\psi\), and therefore \(B\psi=\mp2\mathrm iP\psi\) with \(B=1+C_4-(A+1)^2\). On smooth vectors \(B\) and \(P\) are symmetric and commute, so \(\|B\psi\|^2=\mp2\mathrm i\langle B\psi,P\psi\rangle\) with \(\langle B\psi,P\psi\rangle\) real, and hence \(B\psi=P\psi=0\). For the compact members \(\vec J_{\mathrm L}\) is Hermitian and no such condition arises; the factor \(\mathrm i\) comes from the real form.

\emph{Spectral condition.} The Casimirs act as real scalars on the irreducible components, \(C_5\) for \(\mathrm{Spin}(4,1)\) and \(C_4\), \(P\) for \(\mathrm{Spin}(3,1)\), and so extend to strongly commuting self-adjoint operators. Hence \(\psi\) lies in the spectral subspace of \((C_4,P)\) for the set \(P=0\), \(1+C_4\ge0\). On the unitary principal series of \(\mathrm{Spin}(3,1)\cong\mathrm{SL}(2,\mathbb C)\), labelled by \(k\in\tfrac12\mathbb Z\) and \(p\in\mathbb R\), one has \(C_4=\vec J^2-\vec K^2=k^2-p^2-1\) and \(P=\pm kp\) (Eq.~(297) of~\cite{MartinDussaud2019}; rederived in the realisation by functions on \(\mathbb C\)). Within the principal series this set therefore consists of the countably many representations with \(p=0\).

\emph{Restriction to \(\mathrm{Spin}(3,1)\).} The \(M^{\mu\nu}\) and \(M^{\mu4}\pm M^{\mu5}\) span Poincar\'e subalgebras, and the ladder representations restrict to the Poincar\'e group as irreducible massless representations of fixed helicity~\cite{MackTodorov1969}, as stated in~\cite{Todorov2019}. As a representation of \(\mathrm{SL}(2,\mathbb C)\), \(\mathcal H_n\) is then a space of sections over the light cone, and the Hilbert--Schmidt operators, \(\mathcal H_n\otimes\bar{\mathcal H}_n\), are sections over pairs of null vectors. The pairs that are not collinear have full measure; they form orbits labelled by their scalar product, with stabiliser \(\mathrm U(1)\), which is compact. Each orbit therefore carries a representation induced from \(\mathrm U(1)\), which is contained in the regular representation, so the adjoint action restricted to \(\mathrm{Spin}(3,1)\) is contained in a multiple of the regular representation. The Plancherel measure is supported on the principal series and is the counting measure in the discrete label times a polynomial density times Lebesgue measure in the continuous one (Theorem~7.1 of~\cite{FioresiYuncken2024}). The set above therefore has measure zero, and \(\psi=0\). For \(n=0\) this also follows without the Poincar\'e group. On \(\mathcal H_0\) one has \(C_4=-1-(M^{45})^2\) and \(P=0\) (Eqs.~(11) and~(12) of~\cite{MantaSteinacker2025}), so \(\mathcal H_0\) restricts to principal series with \(k=0\), and a tensor product of principal series is a direct integral of principal series over Lebesgue measure in \(p\) (Eq.~(308) of~\cite{MartinDussaud2019}).

So, for every \(n\), the fermion form of the doubleton member has no normalisable kernel in this class. The hypothesis of the conditional statement of the preceding paragraph thus holds for these members in that sense. The decomposition of the operators under \(\mathfrak{so}(4,1)\) is not needed. The class matters: among bounded operators the identity, times any constant spinor, lies in the kernel, as the trace mode does at finite \(N\) before it is removed, and the kernel in that class is not computed. A trivial kernel does not make the operator invertible with a bounded inverse. Whether zero lies in its continuous spectrum, how the Pfaffian at \(N=\infty\) is then defined, and whether it vanishes are not decided, so the separation at one loop stated conditionally in the preceding paragraph is not established. Kernel vectors that are not smooth, members on other unitary representations of \(\mathfrak{so}(4,1)\), and products with a factor \(K\) are not treated. These statements concern the operator at the member, for \(N\to\infty\) taken first at fixed \(\gamma>0\), and involve no \(\epsilon\), which Definition~(A) puts on the bosons only. Nothing here derives the family, \(h_0\), the mass or the fermion content, so Assumption~\ref{ass:lorentzian} is not discharged, and Problem~E remains open and PROGRAMME-CONDITIONAL.
```

- **Result after insertion.** appH 606285 B, sha256 6a8c811d73b28f80077625dd724ae6193d5719ca68a17ac804ed30ddcb8686d6, CRLF 3324, bare LF 0.
- **Stale passages elsewhere.** None.
  - The 061 sentence "whether their fermion form has a normalisable kernel is not decided here" refers to that paragraph and stays literally true. The new paragraph supplements it for the doubleton members.
  - 061's conditional ("If the fermion forms of these members are non-degenerate, …") stays correct. The new paragraph states explicitly that its consequent is not established.

### File 2: bib/namcg.bib
Append `bib_entries.bib` (CRLF) after a CRLF blank line. It contains four entries:

```bibtex
@article{MartinDussaud2019,
  author  = {Martin-Dussaud, Pierre},
  title   = {A primer of group theory for {Loop Quantum Gravity} and spin-foams},
  journal = {General Relativity and Gravitation},
  volume  = {51},
  pages   = {110},
  year    = {2019},
  doi     = {10.1007/s10714-019-2583-5},
  eprint  = {1902.08439},
  archivePrefix = {arXiv},
  note    = {Version 3; the equation numbers cited refer to it}
}

@misc{FioresiYuncken2024,
  author  = {Fioresi, Rita and Yuncken, Robert},
  title   = {Quantized semisimple {Lie} groups},
  year    = {2024},
  eprint  = {2403.17180},
  archivePrefix = {arXiv},
  note    = {Version 1; the theorem number cited refers to it}
}

@article{MackTodorov1969,
  author  = {Mack, G. and Todorov, I.},
  title   = {Irreducibility of the ladder representations of {$U(2,2)$} when restricted to the {Poincar\'e} subgroup},
  journal = {Journal of Mathematical Physics},
  volume  = {10},
  pages   = {2078--2085},
  year    = {1969},
  doi     = {10.1063/1.1664804}
}

@article{Todorov2019,
  author  = {Todorov, Ivan},
  title   = {The lure of conformal symmetry},
  journal = {Bulgarian Journal of Physics},
  volume  = {46},
  pages   = {117--133},
  year    = {2019},
  eprint  = {1905.13009},
  archivePrefix = {arXiv}
}
```

- **Verification of each entry.**
  - **MartinDussaud2019.** Title page of v3 ("Gen Relativ Gravit 51, 110 (2019). DOI:10.1007/s10714-019-2583-5"); Crossref confirms journal, volume 51 and article 110.
  - **FioresiYuncken2024.** arXiv API (title, authors), with no journal-ref listed, so @misc.
  - **MackTodorov1969.** Crossref record (title, JMP 10, 2078–2085, 1969, DOI). The text was not read; the content is cited "as stated in" Todorov2019.
  - **Todorov2019.** arXiv API journal_ref "Bulg. J. Phys. 46 (2019) 117-133".
- **Result.** bib 29360 B, sha256 1d280848d1bb597193dc648963f81b9b635afce238aa2467fd13ce792002856d, CRLF 980, bare LF 0. No duplicate keys.

## Verification scripts

All are in the proposal folder, with outputs saved as .txt.

- **`s1_lorentzian_identities.py` → `s1_lorentzian_identities.out.txt`.** Weyl-trick finite-dimensional so(4,1) representations (n = 1, 2), adjoint on End V. Checks:
  - the commutation relations;
  - the spin-generator algebra;
  - D² = C5 − C4^tot + 3/2 (control −3/2);
  - per chirality, X² + X = J_L² with 4J_L² = C4 ± 2iP (sign by chirality; control sign fails), C4 = 2(J_L² + J_R²), and D² = C5 − C4 − 2X;
  - kernel dimensions 12 and 40 (non-unitary, real j_L).
- **`s2_principal_series_and_orbits.py` → `s2_principal_series_and_orbits.out.txt`.**
  - (i) symbolic Casimirs of the Freidel–Livine principal series: J² − K² = j² − ρ² − 1 and J·K = −jρ;
  - (ii) case analysis of the kernel condition;
  - (iii) Poincaré subalgebras {M^{μν}, M^{μ4} ± M^{μ5}} in the so(4,2) vector representation;
  - (iv) for 200 random null pairs: stabiliser dimension 1 and compact, orbit-map rank 2.
- **`apply_check.py` → `apply_check.txt`.** Report mode: baselines, unique anchor, hashes, refs/cites, duplicate keys. `--out DIR` writes the patched copies outside the repository and refuses to write inside it. Backslashes are built with chr(92).
- **`build_r1.txt`.** Scratch build record.

## Decisions Taken

- **Class of operators: HS (with smooth vectors), with B(H) treated as the contrasting class.**
  - Reason: HS is the Hilbert space of the Gaussian/Grassmann integral (Tr ψ†ψ) and the N → ∞ limit of the finite-N traceless matrices. In it the question "normalisable kernel" has its literal meaning.
  - Rejected: B(H) as the primary class. It contains the trace-type modes 1 ⊗ χ trivially, the analogue of what tracelessness removes at finite N, so it cannot be the class in which the 061 question is posed. It is recorded as the ambiguity.
- **Smooth-vector premise kept explicit, not removed by an unverified regularity claim.**
  - Reason: D_± is hyperbolic-type (symbol ξ_0 ± σ·ξ), so elliptic regularity is unavailable, and closure-kernel vectors need not be smooth.
- **Method: the Spin(3,1) spectral measure of the whole HS(H_n), not the Spin(4,1) decomposition.**
  - Reason: it avoids an unverified Spin(4,1) content of End(H_n), which appH L2508 records as "plausible, not investigated", and Spin(4,1) → Spin(3,1) branching laws.
  - It needs only Plancherel for SL(2,C) and the massless restriction.
- **Two routes kept.**
  - Route 2 (n = 0) makes the n = 0 case independent of the Mack–Todorov text, which was not read. It rests on the cited Manta–Steinacker paper and on Martin-Dussaud.
- **Insert placement: Problem E, directly after the 061 block.** It answers 061's open sentence in the same setting and order of limits.
- **Principal-series members of Spin(4,1): kept out of the insert.** The sketch relies on a standard but unverified-here realisation.

## No-go fork: what the result does and does not close, and ranked open avenues

**Hypotheses of the positive result:**
- (P-class) HS;
- (P-dom) smooth vectors;
- the doubleton representation;
- no transverse factor;
- Definition (A) content and a supplied γ>0.

**What each relaxation gives:**
- **B(H) class.** The kernel is non-trivial (≥ 16 trace-type modes). This is the stated ambiguity.
- **Non-smooth kernel of the closure.** Open.
- **Other Spin(4,1) representations.**
  - Principal series: same conclusion (sketch).
  - Complementary and discrete series: open.
- **Products with K.** Open: Lorentzian D_W² is not positive, so ker D ≠ ker D_W ∩ ker D_K a priori.

**Ranked open avenues (toward the one-loop selection, i.e. favouring the infrared/full-GR route):**
1. **Zero in the spectrum and the N = ∞ Pfaffian.** Decide whether 0 ∈ σ_cont(D_±). Define a regulated Pfaffian, for example by finite-N truncations of so(4,1) (061 avenue 2) or a heat-kernel/ζ definition with the iε of Definition (A) extended to fermions, and show that it is non-zero, compared with the compact members' exact zero. This is decisive for the one-loop separation.
2. **Approximate finite-N truncations of so(4,1).** Find the smallest singular values of the truncated fermion operator against N. This connects (1) to a finite-N statement.
3. **Products with K and the transverse sector**, for the doubleton member.
4. **Complementary and discrete-series members of Spin(4,1).**
5. **The non-smooth kernel of the closure.** This needs a core statement for the Casimir polynomials on HS^∞.
6. **The bounded-operator kernel beyond 1 ⊗ χ** (massless on-shell operators).

## Milestone assessment

- **Routine, not a breakthrough.**
  - It decides, in a stated class, the sub-case 061 ranked as decisive. The obstruction that kills every compact member (normalisable fermion zero modes) is absent for the Lorentzian doubleton member.
  - This removes a candidate no-go for the conditional route, but it derives nothing about E.
  - The one-loop separation still needs the N = ∞ Pfaffian (avenue 1), and the family, h_0, γ and fermions are supplied.
- **Not M1:** no E step is derived.
- **Not M2:** it is not a no-go; it removes one.
- **Not M3:** no merged claim is wrong; 061's text stays correct.
- **Not M4 or M5.**

## Status-label recommendation

- **Critical-path set (Ch17 L700–735, Appendix H).** A, B, C, D1, E, F, G-derived, N.
- **Affected.** E, and D1 indirectly. Both remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.
- **No change recommended.**

## Author decision needed

None.

## Remaining open step

To turn the 061 conditional into a one-loop selection of the W-timelike member:
1. Define the N = ∞ fermion Pfaffian at the doubleton member, given that its kernel is trivial and 0 is probably in its continuous spectrum, by a regulator or a limit of finite-N truncations that Definition (A) supplies or that is derived.
2. Show that it is non-zero, while the compact members' Pfaffians vanish exactly.
3. Supply the regulator-independent bosonic comparison (061).

Even then, the family, h_0, γ and the fermion content remain supplied. E's original target, Lorentzian signature derived, would need these derived too.

## Special instructions for the gatekeeper

- **Re-run** s1 (under 1 s), s2 (about 2 s) and apply_check.py.
- **Re-derive** the key step, B ψ = ∓2iPψ ⇒ Bψ = Pψ = 0, including:
  - the sign/i bookkeeping in 4J_L² = C4 ± 2iP;
  - the fact that ⟨Bψ,Pψ⟩ is real.
- **Check the preimage of S'.** pk = 0 and k² − p² ≥ 0 ⇒ p = 0.
- **Check** the orbit/stabiliser argument (U(1) compact) and the inclusion Ind_{U(1)}^G χ ⊂ L²(G).
- **Check that the conclusion is used only in HS.** The insert must not be read as "the fermion operator is invertible" or "the one-loop term is non-zero".
- **Literature status.**
  - Read: Martin-Dussaud Eqs. (297) and (308); Fioresi–Yuncken Theorem 7.1; Manta–Steinacker Eqs. (1), (11) and (12); Todorov 2019 §1.
  - Not read: the Mack–Todorov text, which is cited "as stated in" Todorov2019.
- **Must not be asserted:**
  - that the Lorentzian member is selected;
  - that any signature is derived;
  - that the N = ∞ Pfaffian is non-zero;
  - that the kernel is trivial in B(H);
  - anything about complementary/discrete-series members or products with K.
- **Full scan.** Integration ordinal 60: the 5th-item full scan is due before integration. This proposal changes no definition, assumption, scope or status passage.
- **Build (researcher scratch).**
  - The tracked files plus the patched appH/bib were built outside the repository with pdflatex, bibtex, pdflatex, pdflatex, all exiting 0.
  - Results: 376 pages; 0 undefined; 0 multiply-defined; no bibtex warnings; all four new keys in the .bbl (build_r1.txt).
  - The first copy command, which included an `rm -rf` of a scratchpad directory, was denied. It was not retried in that form; a non-destructive copy then ran.
- The integrator's `build_check.py` remains required.
