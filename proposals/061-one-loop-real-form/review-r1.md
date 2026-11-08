VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: RESEARCHER-DECISION | PROGRESS: first | OPEN: 0/1

## Verdict
The central no-go holds and I re-derived it. Every non-zero finite-N member of the 060 family at fixed γ>0 has a degenerate fermion form, so Pf M(T̄)=0. The insert needs revision on one major point. At fixed γ>0 with h_0 of signature (9,1), the base-coordinate member is not a solution: merged 060 gives it γ=−3c<0. So the non-compact list in the insert, and its reason for "does not by itself select a Lorentzian kinetic tensor", are wrong as written. Four smaller wording fixes are also needed.

## Source reading
- **Mode.** Digest + targeted reads, not a full scan. `make_digest.py --check` printed DIGEST CURRENT, `dirty-chapters: no`. The 060 change is now in HEAD via commit 276c04b, and the working tree is clean. Working-file sha256 values: appH 94befe3b…85c6 and bib 645c93c9…0f67, both matching the stated baselines.
- **Read in full:**
  - appH L1482–1521 (E ledger label, Definition (A), contours, limit);
  - appH L1585–1614 (059 closing, the whole 060 block, the anchor, the start of F);
  - appH L597–603 (Problem D ledger label);
  - appH L2478–2486 (the so(6) "Compact check" Hessian);
  - grep-located sentences mentioning fermions, zero modes, so(5), so(6) or the Pfaffian at appH L215, 1458, 1462, 1576, 2435–2461, 2480–2505, 2538–2551, 2616–2629, and ch03 L617;
  - ch17 L394–400 and L708–722; ch04 L318–330 (ass:lorentzian);
  - bib Steinacker2023, IKKT1997 and the bib tail bytes;
  - the ledger tail (059, 060); MILESTONE.md.
- **Not read in full.** The other 045–049 CP^{1,2} paragraphs. I located them by grep for every fermion/zero-mode/Pfaffian mention.
- **Scan ruling.** 3(c) does not apply: no definition, assumption, scope or status passage changes, and the closing sentence repeats the existing status. 3(b) does not apply this round, because the verdict is not a final ACCEPT. If the final-round ACCEPT with M2 is treated as triggering a milestone digest, a full scan is required then. Ordinal 60 is the next 5th-item scan in any case.

## Claim under review
- **Claim.** Setting: Definition (A), h_0 of signature (9,1), supplied IKKT MW fermions, supplied γ>0, and the 060 family T̄^I=L^I_aT^a, T^a=M^{ac0}, H=cη. The claims are:
  - Casimir forms of the one-loop operators on compact members;
  - species weight 5−4−1=0;
  - a fermion kernel of dimension ≥32 per adjoint copy, so Pf M(T̄)=0 at every non-zero finite-N member, with the count (4/3)n(n+4)(n²+4n+7) for V_n;
  - negative modes affect only the phase;
  - the regulator dependence of the mass-insertion density;
  - a conditional route for the non-compact members.
- **Original target (E).** Lorentzian signature derived rather than retained (ch17 L718). Appendix H verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **D, bearing only.** Appendix H verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- **Critical-path set.** Ch17 lists A, B, C, D1, E, F, G-derived and N; H, I and J are optional. No discrepancy with Appendix H.

## Checks performed
**Fermion square.** D=Γ^a ad X_a, X_a=√c M_{a c0}.
- □=Σad(X_a)²=c(C5−C4), and the cross term ½Γ^{ab}ad[X_a,X_b] is the spin–orbit term. This gives D²=c(C5−C4^tot+C_sp) with C_sp=3/2 on a Weyl spinor (normalisation 4 on the so(5) vector, 3 on the so(4) vector).
- Independent sign check: D is a sum of tensor products of Hermitian operators, so D²≥0. With k1≤m1 and |k2|≤m2, the largest C4^tot on (k1,k2)⊗(½,0) is k1²+k2²+3k1+k2+3/2. This is ≤ C5+3/2, with equality only at k1=m1, k2=m2 and J_L=j_L+½. The +3/2 sign is therefore the one consistent with positivity.
- Identity by hand: 2(j_L+½)(j_L+3/2)+2j_R(j_R+1) = m1²+m2²+3m1+m2+3/2 = C5+3/2. Correct.
- The same inequality shows the zero multiplet in each (m1,m2) is unique for every irrep, not only for n≤20.

**Kernel count.** z per Weyl doublet is Σ(m1+m2+2)(m1−m2+1).
- n=1: 6+4=10. n=2: 10+12+10+6=38. So z16=8z gives 80 and 304.
- The closed form gives 80 and 304. End(V_1) and End(V_2) dimension sums are 16 and 100.

**Generality.** For any non-trivial finite-dimensional representation, ρ(so(5)) is injective (so(5) is simple) and traceless (semisimple), and it is an ad-invariant (1,1) copy.
- The top components (3/2,0) and (0,3/2) each have dimension 4. Under so(4)×so(5,1), 16=4(2,1)+4(1,2), giving ≥32.
- This is proved for reducible representations, not sampled. The reducible checks V1⊕V1=368 and V1⊕V0=144 reproduce.
- A kernel of the complex operator implies det=0, hence Pf=0, and C is invertible.
- Restriction to "all non-zero finite-N members" rests on merged 060, which says η is definite at finite N.

**Witt step.** Re-derived. O(W^⊥)≅O(5,1) meets all components of O(9,1), so the isometry can be taken in SO⁺(9,1). The kernel is covariant under the spin lift.

**Species scaling.** Bosons give c^{−5(N²−1)}, the Pfaffian c^{4(N²−1)} (degree 8(N²−1) in √c), and ghosts c^{N²−1}. The net power is zero.

**Degree bound.** Pf(M0+δ) needs ≥ k/2 factors of δ when dim ker M0 = k. Correct.

**Phase-only claim.** ∫e^{iλx²/2−εx²} → |λ|^{−1/2}e^{±iπ/4}. Correct for the modulus.

**Regulator integrals.** Re-derived with k0=au, 4-ball polar coordinates, t=tan χ and partial fractions t²/((t²−a²)(t²+1)) = [a²/(1+a²)]/(t²−a²) + [1/(1+a²)]/(t²+1):
- Re = 2π²Λ²a/(1+a²);
- |Im| = 2π²Λ²a²/(1+a²);
- Euclidean form: 2π²Λ²a/(1+a);
- Wick rotation: purely imaginary.
All agree with the proposal.

**Scripts re-run** (outputs in the scratchpad):
- s1, s1b, s2b, s3, s4 and apply_check are identical to the stored outputs.
- s2 rows are identical; the default n-list differs.
- s1 confirms:
  - the Hessian sign choice (−1,−1), residuals 7e−15 and 2.5e−14;
  - D² sign s'=−1;
  - 10D kernels 80 and 304;
  - chirality commuting with D².
- All of this is numerical confirmation of identities I derived independently.

**Consistency with merged text.**
- The appH L2480 compact check uses the same Hessian λ=c5−c4(c',d')+3+m², with m²=−3, i.e. C5−C4^tot. Its counts 38, 124, 344 versus 34, 120, 340 here differ by exactly the 4 trace modes ((0,0)⊗vector, λ=−3). Both are consistent, but the two passages differ in convention (traceful there, traceless in Definition (A)).
- No merged passage asserts a non-zero Pfaffian or a finite one-loop term on a compact finite-N member. The 060 block and the CP^{1,2} blocks either exclude fermions or work in the Poisson limit / leading symbol on the non-compact leaf. So there is no PRIOR-CLAIM-ERROR.

**Literature.**
- 1510.05779: abs page checked (v1–v4; related DOI 10.1007/JHEP12(2015)115). PDF v4 text extracted with pdftotext.
  - Eq. (3.28) and "There are again zero modes (n−m,2m+1) for n=m … Hence supersymmetry is clearly broken" confirmed.
  - Section 4 confirmed: "these contain the zero modes, which should not be integrated out, and we will drop them".
  - The attribution in the insert is supported.
  - The JHEP journal name itself comes only from the DOI; the abs page lists no journal-ref.
- 2303.08012 (HTML):
  - Eq. (4.16) one-loop trace-log formula with −iε confirmed.
  - Eq. (4.15) "amounts to Feynman's iε regularization" confirmed.
  - "pre-factor i is an artefact" confirmed.
  - The exact added term was not displayed in my fetch, so the identification with the Definition (A) factor is not independently verified in its exact form. It is consistent with the ledger's Definition (A).

**Integration checks.**
- Anchor `\paragraph{Status.}` / `Remains Assumption~\ref{ass:lorentzian}.` occurs exactly once (L1609–1610).
- apply_check re-run gives identical results: appH 599565 B, da8be0e3…a3e, CRLF 3313, bare LF 0; bib 28049 B, 582f09d5…1f22, CRLF 937.
- Keys IKKT1997 and Steinacker2023 exist; there are no new labels and no duplicate keys.
- tex_lint is balanced (118/118).
- **Build not run.** The integrator must run build_check with bibtex.

**Wording checks.**
- No process language.
- No derived-signature claim.
- The order of limits is stated, and γ is stated as supplied.
- The conditional is a premise ("If their fermion forms are non-degenerate").
- The s4 mechanism and the g/γ power counting are absent from the insert.
- No label change.

## Findings
1. **Severity: major.**
   - *Location.* Insert, "Non-compact members and normalisation", the sentences "These include … the base-coordinate member, whose fibre-averaged tensor is positive definite for 0<m²<2ℓ². If their fermion forms are non-degenerate, … it does not by itself select a Lorentzian kinetic tensor". The same claim is in proposal Result 5 and ranked avenue 2.
   - *Finding.* Merged 060 (L1603) gives the base-coordinate member γ=−3c with c>0 for h_0 of signature (9,1). So it is not a solution at the fixed γ>0 of this setting.
   - *Reason.* From 060's identity, γ=3cη^{c0c0} with H=cη realisable by h_0 (9,1). At γ>0 the diagonal five-index forms allowed are only so(5) with W spacelike, or so(4,1) with W timelike. The "no Lorentzian selection" clause is justified in the text only by the presence of the Euclidean-averaged base member.
   - *Required action.* Remove the base-coordinate member from the γ>0 list, or state that it needs γ<0. Then restate what the conditional does and does not select, keeping the selection attributed to the supplied γ>0, h_0 and fermion content and to the unresolved non-degeneracy (RESEARCHER-DECISION below).
2. **Severity: minor (required).**
   - *Location.* Insert, regulator sentence "For a kinetic form K=k^T𝖪k of signature (3,1) on flat momenta … against … for a positive definite K".
   - *Finding.* The stated values hold for K=−k0²+|k|² and K=k0²+|k|² aligned with the ellipsoid axes, not for an arbitrary (3,1) form or an arbitrary positive definite form.
   - *Required action.* Name the two forms (snippet below).
3. **Severity: minor (required).**
   - *Location.* "so the sign of the fluctuation spectrum does not distinguish the members".
   - *Finding.* The Morse index enters the phase, which can matter when saddles interfere.
   - *Required action.* Restrict the claim to the modulus (snippet below).
4. **Severity: minor (required).**
   - *Location.* "34, 120 and 340 negative eigenvalues on the four directions of W".
   - *Finding.* The Section F compact check (L2484) reports 38, 124, 344 for the same operator, with the trace included.
   - *Required action.* State "traceless" and give the cross-reference (snippet below).
5. **Severity: minor (optional).**
   - *Location.* "every non-trivial unitary representation of so(5)".
   - *Finding.* The direct-sum decomposition holds for unitary representations of the group Spin(5), i.e. integrable ones.
   - *Suggested action.* Write "of \(\mathrm{Spin}(5)\)".
6. **Severity: minor (process).** No build was run. The integrator must run `python scripts/build_check.py` plus bibtex for the new key Steinacker2015S4.

## Scope of what is established
**Proved (established identity/derivation)**, within Definition (A), h_0 (9,1), supplied IKKT fermions, supplied γ>0, and the 060 family:
- the compact-member operator forms;
- species weight 0;
- the top-component zero-mode identity C4^tot=C5+3/2;
- kernel ≥32 per adjoint copy for every non-trivial finite-dimensional representation, reducible included;
- Pf M(T̄)=0 at every non-zero finite-N member (with 060);
- kernel persistence for compact unitary representations at N=∞ and with a transverse K;
- uniqueness of the zero multiplet per so(5) irrep, and the V_n count;
- the degree bound ≥ k/2;
- phase-only effect of negative modes on the modulus;
- the flat-model regulator dependence.

**Hypotheses of the bounded no-go.** It is M2 and valid only within this class:
- (a) massless MW fermion content;
- (b) the 060 Lie-generator family with isotropic h_0-contracted mass;
- (c) finite-dimensional or compact unitary representations;
- (d) W spacelike, which γ>0 forces for so(5).

It does not close the one-loop route. It removes only the compact real form from one-loop competition.

**Conditional or open.**
- The non-degeneracy of the non-compact (so(4,1), W timelike) fermion forms is unresolved.
- The N=∞ one-loop object and its cut-off are undefined.
- The order in g/γ of the compact members' first contribution is not computed.
- Classification: PROGRAMME-CONDITIONAL. E and D stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No signature is derived, and ass:lorentzian is retained.

**Open avenues, ranked (most promising for the IR/full-GR derivation first):**
1. Normalisable kernel of the fermion form on End(H) for the so(4,1)⊂so(4,2) doubleton member at γ>0. After Finding 1 this is the only non-compact real form in the γ>0 family, so it decides whether the one-loop integral leaves only Lorentzian-W members. This is the decisive step.
2. Approximate finite-N truncations of so(4,1): whether near-Lorentzian finite configurations evade the adjoint-copy zero modes. The no-go needs exact Lie relations, i.e. hypothesis (b).
3. Relaxing hypothesis (a): a fermion mass or SUSY-preserving (polarised-IKKT-type) deformation lifting the zero modes. This is outside Definition (A) content and would be supplied.
4. A cut-off for the N=∞ bosonic factor derived from large finite N in Definition (A).
5. The g/γ order of the compact contribution (lifting of the 6, 142, 277 bosonic flat modes).
6. Comparison across the sign of γ, which brings back the base-coordinate member, and saddles outside the family.

## Recommended disposition
Revise (r2) and re-review. Do not integrate as-is.

**RESEARCHER-DECISION.** Once the base member is removed at γ>0, how should the conditional be stated? Options:
- (a) Recommended, favouring E. Within the γ>0 family the only members that can have a non-vanishing one-loop term have W timelike. This includes the conjugate-coordinate member, whose kinetic tensor is Lorentzian on m≠0 by 060. The statement is explicitly conditional on non-degeneracy, the selection rests on the supplied γ>0, h_0 and fermion content, and the kinetic tensor is not identified with the emergent metric.
- (b) Widen the setting to both signs of γ. The base member then appears at γ<0, and the text must state that any comparison across the sign of a supplied γ is not a selection.

Whichever is chosen, update proposal Result 5 and ranked avenue 2 to match.

## Corrected snippet
No new physics. The only extra input is 060's own identity γ=3cη^{c0c0} with H=cη.

Replace "These include the conjugate-coordinate member, whose kinetic tensor is Lorentzian on \(m\neq0\), and the base-coordinate member, whose fibre-averaged tensor is positive definite for \(0<m^2<2\ell^2\). If their fermion forms are non-degenerate, the supplied fermion content, and not the bosonic action, separates the compact real form from the non-compact ones at one loop, and it does not by itself select a Lorentzian kinetic tensor." with this option (a) text:

```latex
At fixed \(\gamma>0\) and \(h_0\) of signature \((9,1)\) the identity of the preceding paragraph admits, besides \(\mathfrak{so}(5)\), only the five-index algebra \(\mathfrak{so}(4,1)\) with \(W\) timelike, among them the conjugate-coordinate member, whose kinetic tensor is Lorentzian on \(m\neq0\); the base-coordinate member requires \(\gamma<0\) there. If the fermion forms of these members are non-degenerate, the supplied fermion content, and not the bosonic action, separates them from the compact members at one loop; the Lorentzian kinetic tensor is then fixed by the supplied sign of \(\gamma\), \(h_0\) and fermion content, not derived, and is not identified with the emergent metric.
```

Replace "For a kinetic form \(K=k^{\mathrm T}\mathsf Kk\) of signature \((3,1)\) on flat momenta" with "For \(K=-k_0^2+|\vec k|^2\) on flat momenta", and "for a positive definite \(K\) over the same region" with "for \(K=k_0^2+|\vec k|^2\) over the same region".

Replace "so the sign of the fluctuation spectrum does not distinguish the members" with "so the sign of the fluctuation spectrum does not distinguish the moduli of the members' contributions".

Replace "\(34\), \(120\) and \(340\) negative eigenvalues on the four directions of \(W\)" with "\(34\), \(120\) and \(340\) negative eigenvalues on the traceless fluctuations along the four directions of \(W\) (the compact check of Section~\ref{sec:status-F} counts four more from the trace)".

Optional: "every non-trivial unitary representation of \(\mathfrak{so}(5)\)" → "every non-trivial unitary representation of \(\mathrm{Spin}(5)\)".

Files:
- C:\Users\redgi\Projects\namcg-lab\proposals\061-one-loop-real-form\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\061-one-loop-real-form\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (L1603 base member γ=−3c; L2480–2484 compact check)

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: RESEARCHER-DECISION | PROGRESS: first | OPEN: 0/1
