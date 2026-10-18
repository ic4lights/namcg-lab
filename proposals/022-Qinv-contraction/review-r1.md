VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/4

## Verdict
The core algebra and numerics reproduce, and the block is correctly scoped as conditional. Four statements are misstated, overstated or selectively reported (a factor in the Q⁻¹ identification, the no-go argument, the "only if" claim, and omitted negative-mode data), and one is missing (the signature/emergence disclaimer). These need small text fixes before ACCEPT.

## Source reading
**Full scan.** I read in full all 30 files of the current manifest:
- chapters ch01–ch18 and appA–appL;
- appH in five contiguous reads covering lines 1–2500.

I did not rely on the digest, which `make_digest.py --check` reports as `DIGEST STALE`. The working tree contains the integrated 017–020 text; the 020 block ends at line 1994.

**Ordinal.** The ledger shows 18 integrations, so 022 would be the 19th or 20th (if 021 integrates first). I did the full scan regardless.

**Anchor.** `\section{Problem G: HBEV}` occurs exactly once (appH line 1996). The 020 block ends at line 1994 with "Problem~F remains open." `block-r1.tex` equals the fenced block in `proposal-r1.md` (byte-compared after CRLF normalisation). The block has CRLF endings, no `\cite`, one `\ref{def:matrix-coords-ext}` (defined once, ch03 line 173), no process language, and no duplicate paragraph title.

**Build.** I could not run my own scratch compile because the sandbox denied the copy. The researcher's `compile_check_r1` (rc 0, 0 undefined, 270 pages) is therefore "not independently verified". I read the LaTeX and found no syntax problems.

## Claim under review
Problem F, original target: matrix-derived G_eff (sign and size).
- Appendix H, F, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- Problem E is touched through signature. Appendix H, E, verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- Chapter 17 and Appendix H agree on the critical-path set A, B, C, D1, E, F, G-derived, N. I found no discrepancy.

The proposal claims:
1. The contraction by Q⁻¹ is the induced Euclidean metric g of the hyperboloid, and K = m²η = m²(g⁻¹ − yy/ℓ²).
2. A bounded no-go in the four-matrix class: nothing supplies (y_aD^a)².
3. A classification of the six presentations X^A = M^{Ac0}.
4. For X^A = M^{A5}: f1 = f2, μ² = +4, and the exact identity H_V = C_so(4,2) − C_G + C_Σ + μ².
5. A bosonic density formula.
6. A compact finite-N check.

It claims no derivation of w and no label change.

## Checks performed

**Direct re-derivation (mine).**
- With D^a f = s·y⁴∂^a f on functions of y^μ, Q^{ab} = (y⁴)²η^{ab} + y^ay^b is the Gram matrix of the D^a in the ambient metric.
- Q⁻¹ = (η + yy/ℓ²)/(y⁴)². So Q⁻¹_{ab}D^aD^b has base symbol exactly g⁻¹ = η + yy/ℓ². Sherman–Morrison with y·y = −ℓ² gives the same g⁻¹ as the inverse of g = η + yy/(y⁴)².
- g is positive definite. Its determinant is ℓ²/(y⁴)² > 0, and g(y,y) = ℓ²(ℓ²+(y⁴)²)/(y⁴)² > 0.
- K = (y⁴)²η = (y⁴)²(g⁻¹ − yy/ℓ²) is immediate.
- μ² = +4: {M^{B5},M^{A5}} = −sM^{BA} and Σ_C η_{CB}{M^{C5},M^{BA}} = 4sM^{5A}. The four-matrix analogue gives −3.
- The density: 4cosh2x + 1 − 2 + n = 8sinh²x + 3 + n, so f²/(16π²)[8 + (3+n_ex)/sinh²(sf)]. The large-sf limit is f²/(2π²). The second term's integral converges (∫x³/sinh²x = 3ζ(3)/2).
- Signature classification: the horizontal metric is the induced metric of the quadric y·y = η_{c0c0}ℓ² in R^{p,q}.
  - c0 timelike gives R^{4,1} minus a timelike normal, so (4,0).
  - c0 spacelike gives R^{3,2} minus a spacelike normal, so (2,2).
  - Lorentzian (3,1) is excluded by this structure within this family, matching the numerics.

**Scripts re-run.**
- `check_all_five_matrix_presentations`: ranks (4,2); h of type (0,4) for c0 ∈ {0,5} with f2/f1 = 1.000000; h of type (2,2) for c0 ∈ {1,…,4}.
- `check_P5_selfduality_large` (300 points × 91 directions, s = ±1): worst opposite-chirality fraction 2.2e-12, worst 1 − f2/f1 = 4.5e-12.
- `check_P5_exact_algebra` (both signs): μ² = 4 and Box5 = C_so(4,1) − C_so(4,2). H_V = C42 − C_G + C_Σ + μ² holds only for the combination (1,−1,1), and H_V = −□ − 2σs J·A + μ² holds with σ = −1 only.
- `check_P5_family_polynomial`: the Weyl combination is 0 for k = 0…12. It is the polynomial (2k²+6k) − (2k²+6k+4) + 4 ≡ 0, so it holds for all k. The (2,1) component has dimension 35 at eigenvalue +4.
- `quantum_compact_hessian` (I re-ran N = 1,2,3): negative modes are exactly 35/140/371 at −4 plus 14 at −2.
- `check_extended_sets` and `check_orbit_relations`: reproduced. Residuals are 1e-12 for the orbit relation and 1.9e-6 for the g⁻¹ identity, which is looser than the 10⁻¹² quoted for the orbit relation.

**Not independently verified.**
- Self-duality is numerical only.
- The k = 1 verification and the identification of leading-symbol zero modes with the polynomial family are not independently derived.
- The twistor remark is not used in the block.

## Findings

**1. Major — the "equivalently" clause in the identification paragraph (first paragraph, last sentence).**
- Finding: Q⁻¹_{ab}D^aD^b = (y⁴)⁻²[η_{ab}D^aD^b + (y_aD^a)²/ℓ²]. The block says "equivalently the term (y_aD^a)²/ℓ² added to η_{ab}D^aD^b".
- Reason: that sum has base symbol (y⁴)²g⁻¹, not g⁻¹. It differs by a non-constant conformal factor. The symbol of Q⁻¹ itself is correct.
- Action: state "up to the factor (y⁴)⁻²". Also state that y·y = η_{AB}y^Ay^B (A = 0,…,4).

**2. Major — the no-go argument (second paragraph).**
- Finding: the sentence on G†G ≥ 0 and negative-mode counts does not bear on whether (y_aD^a)² is supplied. A positive operator can remove negative modes, and the proposal's own text wrongly says it "cannot remove" them. The real reason is that every listed operator (Hessian, gauge function D_aA^a, ghost, □_X regulator) is built from D^a and J^{ab} with constant η_{ab}. Also, "not in the Lie algebra so(4,1)'" is too weak, since the symbol could in principle arise from the enveloping algebra. The Casimir C_so(4,2) lies in U(so(4,2)) and has symbol −2ℓ²g⁻¹ (script 8). The correct claim is that (y_aD^a)² is not in U(so(4,1)'), where so(4,1)' is generated by D^a and J^{ab}, because the missing generators M^{a5}, M^{45} are needed. I checked the base-symbol argument: y⁴y_a∂^a, with a non-polynomial y⁴, is not a constant-coefficient combination.
- Action: replace the G†G sentence with the structural one, and state the hypothesis class explicitly:
  - Poisson limit;
  - four matrices T^a = M^{a4};
  - quartic term plus a single bilinear term;
  - background gauge function D_aA^a, ghost −□, regulator a function of □_X;
  - constant index form η_{ab}.
- Define so(4,1)'. The prime is not defined anywhere else in the manuscript.

**3. Major — Consequence (i) "supplied by the matrix data only if the matrices are X^A = M^{A5}" (Consequences paragraph).**
- Finding: this is a universal claim, but only these sets were tested: T^a; M^{Ac0}; and the extended sets S8, S7, S9.
- Eight matrices {T^a, y^a} with the y-block contracted by −η are stationary with a single coefficient. In `check_extended_sets`, λ_I·w_I = −4 for all eight, so μ² = −4, with horizontal rank 6. The block says only that "positive-norm" extensions need different coefficients, which is true for the δ-contracted y-block, but the consequence overreaches. The (4,4)-signature set is not analysed for its induced contraction or flux.
- Action: reword to "in the matrix sets examined". Add that the eight-matrix set with the y-block contracted by −η is stationary with one coefficient and is not examined.

**4. Major — selective reporting of stability data (Five-matrix paragraph and Compact check paragraph).**
- Finding, polynomial space: the 75-dimensional degree-1 space has H_V eigenvalues −8 (×1), −4 (×5), −2 (×20), +2 (×14), +4 (×35). The block reports only the +μ² eigenspace.
- Finding, compact form: the Hessian has 49/154/385/814 negative modes for N = 1,2,3,4. The block gives only the lowest eigenvalue −4 and the 14 modes at −2. Set beside the four-matrix "−(N+3), growing with N", this reads as favourable. In fact both compact backgrounds are unstable.
- Action:
  - Add that the formal polynomial spectrum has negative values with no spectral meaning for non-normalisable polynomials.
  - Add that the compact five-matrix background has negative modes, and give the counts.
  - Correct the multiplicity sum to 1 ≤ k ≤ N.
  - Extend Consequence (ii) to say that negative formal modes of the same operator may persist on normalisable states.

**5. Major — emergence and signature wording (Consequences and the final paragraph).**
- Finding: the block says "emergent horizontal metric is then the Euclidean metric g". Every sibling block says it "does not identify G with the emergent metric of Chapter~\ref{ch:vierbein-emergence}". Definition 3.x says neither g nor K⁻¹ is asserted to be the emergent metric. The block omits this disclaimer and never states that Assumption~\ref{ass:lorentzian} (Problem E) is untouched.
- Action:
  - Replace "emergent horizontal metric" with "horizontal metric induced by the contraction".
  - Add: "It does not identify g with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, does not derive Lorentzian signature, and leaves Assumption~\ref{ass:lorentzian} in place (Problem~E)."

**6. Minor.**
- (a) "(Definition~\ref{def:matrix-coords-ext}, D=5)": the Definition has diag(−1,1,…,1), which covers c0 ∈ {0,5} up to relabelling. The (3,2) forms for c0 ∈ {1,…,4} lie outside it. Say so.
- (b) "so the preceding level-one and stress results do not carry over" should read "the level-one and stress results of the four-matrix class are not obtained in this presentation". It is a scope statement, not a retraction.
- (c) "ζ is bounded by the fibre harmonic number of the quantum space" is asserted without derivation. Hedge it with "expected".
- (d) Add a cross-reference to the 020 sentence "self-duality holds identically only for the contraction by Q⁻¹, which is not a constant contraction". That sentence is correct within the four-matrix T^a class, but a reader could see tension with the constant-contraction five-matrix result. One clause in the new block suffices.
- (e) y_AD^A = 0 holds on the orbit. Say so. In `check_P5_exact_algebra` item (2), the printed True contradicts its own "expected False" label. The sampled polynomial f contained no M^{·5} factor, so the item is inconclusive. The orbit-level check in `check_P5_vs_P4` (1.4e-13) supports the block.
- (f) Optional: SO(4,1)-covariance reduces "identically f1 = f2" to a finite sampling check, and mentioning this would strengthen the claim.

No blocking findings.

## Scope of what is established

**Established (algebra plus numerics, within scope).**
- The Q⁻¹ symbol is g⁻¹, Euclidean.
- K = m²η = m²(g⁻¹ − yy/ℓ²).
- The orbit relation holds.
- μ² = +4 (both signs of s).
- Box5 = C_so(4,1) − C_so(4,2).
- The exact polynomial identity H_V = C_so(4,2) − C_G + C_Σ + μ².
- The (k+1,k) component has eigenvalue μ² on polynomial vector fields (k = 1 checked directly, dimension 35).
- The exact compact identity H + G†G = C6 − C5tot + C5vec + m² (N = 2).
- The compact lowest eigenvalue is −4 for N ≤ 4, versus −(N+3) for the four-matrix background.

**Established numerically only.**
- Self-duality of the flux, hence f1 = f2.
- The signature classification of the six presentations.

**No-go, within its exact hypotheses.** In the four-matrix class (see Finding 2), no listed ingredient produces (y_aD^a)².

**Conditional or conjectural.**
- Lifting the zero modes by +μ² on normalisable states.
- Whether negative formal modes persist.

**Not determined.** The sign and size of w, the weight-two coefficient, fermions, Moyal terms. F stays OPEN and PROGRAMME-CONDITIONAL. E stays OPEN: the five-matrix route gives a Euclidean horizontal metric, and a Lorentzian coefficient would need a Wick-rotation hypothesis, which is not a derivation. No label changes.

**Emergence.** The block keeps spacetime emergent. Everything is induced from the leaf and a constant matrix-index form, and no fundamental or non-emergent metric is introduced. The block does not weaken any merged Lorentzian claim of 013–016 or any Problem E statement, so no PRIOR-CLAIM-ERROR. It is consistent with the existing remark in appH around line 1888 that an orthogonal complex structure gives G ∝ g but then G is Euclidean.

**Open avenues (ranked, most promising first).**
1. Relax the regulator hypothesis: use the matrix-built Casimir C_so(4,2) (symbol −2ℓ²g⁻¹, Euclidean) as the proper-time operator in the four-matrix class.
2. Examine the eight-matrix set {T^a, y^a} with the y-block contracted by −η, which is stationary at μ² = −4 with rank 6. Compute its induced contraction, signature and flux.
3. Exact so(4,2) analysis of H_V on normalisable states of the five-matrix presentation, including the negative formal modes.
4. The weight-two (s⁻³) coefficient of the five-matrix class with a finite fibre. This gives a Euclidean w, then the Wick tie to E.
5. Fermionic partners or a finite fibre to remove the f²/(2π²) divergence.
6. A gauge function involving y: this needs a non-matrix input and is therefore low value.
7. A quintic stabiliser: exploratory and outside eq:Smatrix.

## Recommended disposition
Revise the block per Findings 1–5 and minor items 6(a)–(e), then re-review. The package is coherent: the identification, the no-go, the five-matrix route and the exact algebra share one context. It is a consequential but bounded contribution (milestone M2, narrow, as for 018): it closes the Q⁻¹ "supply" avenue of 020 within its class and gives a Euclidean-signature route. It is not a breakthrough. No AUTHOR-DECISION or label change.

## Corrected snippet
No new physics is needed. Suggested replacements:
- First paragraph, last sentence: "…the contraction by \(Q^{-1}\) equals \((y^4)^{-2}\bigl[\eta_{ab}D^aD^b+(y_aD^a)^2/\ell^2\bigr]\), and replaces the Lorentzian tensor \(K\) by the Euclidean metric \(g\); it is not a Wick rotation of \(\eta\)."
- No-go paragraph: replace the G†G sentence with: "In the class (Poisson limit, matrices \(T^a=M^{a4}\), quartic plus one bilinear term, background gauge function \(D_aA^a\), ghost \(-\Box\), regulator a function of \(\Box_X\), constant \(\eta_{ab}\)) every operator is a polynomial with constant coefficients in \(D^a\) and \(J^{ab}\); \((y_aD^a)^2\) is not an element of the enveloping algebra of \(\mathfrak{so}(4,1)'\), generated by \(D^a\) and \(J^{ab}\)."
- Consequence (i): "…in the matrix sets examined (\(T^a\); \(M^{Ac_0}\); the extended sets listed). The eight-matrix set \(T^a,y^a\) with the \(y\)-block contracted by \(-\eta\) is stationary for one coefficient \(\mu^2=-4\) and is not examined further."
- Add to (ii): "On degree-one vector polynomials \(H_V\) also has the formal eigenvalues \(-8,-4,-2,+2\) with multiplicities \(1,5,20,14\); the compact background has \(49,154,385,814\) negative modes for \(N=1,\dots,4\)."
- Final paragraph: add "It does not identify \(g\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, does not derive Lorentzian signature, and leaves Assumption~\ref{ass:lorentzian} in place (Problem~E)."

All paths:
- Proposal and review input: C:\Users\redgi\Projects\namcg-lab\proposals\022-Qinv-contraction\proposal-r1.md
- Block: C:\Users\redgi\Projects\namcg-lab\proposals\022-Qinv-contraction\block-r1.tex
- Scripts: C:\Users\redgi\Projects\namcg-lab\proposals\022-Qinv-contraction\
