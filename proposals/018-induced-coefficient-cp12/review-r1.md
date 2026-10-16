VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 (narrow) | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
The central claims check out: the Casimir structure, the step-2 sub-Laplacian with Q = 8, the Landau diagonal with its 3ζ(3) closed form, the vector-sector spectrum −|f1−f2|, and the (22−n_ex)/6 coefficient. The paragraph is correctly scoped as a bounded no-go, and it bounds the merged 011 statement without contradicting it. Several wording corrections are required before integration (R1–R5 below). It is not a breakthrough.

## Source reading
**Full scan of all 30 chapter files, plus targeted verification.**
- `python scripts/make_digest.py --check` printed DIGEST STALE. `git status` shows `chapters/` and `bib/` clean.
- Files read in full: appA–appL (12) and ch01–ch18 (18), including all of `appH-microscopic-proofs.tex` (lines 1–2464).
- Other items read: `proposal-r1.md`, `block-r1.tex`, the scripts and their `.out.txt` files, the ledger tail and `MILESTONE.md`.
- No earlier `review-r*.md` exists for 018, so this is round 1.
- No file was unreadable.
- Ordinal: the ledger says the next integration is the 15th, or the 16th if 017 lands first. Either way the full scan was done.

## Claim under review
Bounded no-go in the CP^{1,2} Poisson-limit class for the Θ-built regulator. The regulator is the proper-time cutoff of a step-2 sub-Laplacian of homogeneous dimension 8. The heat-kernel diagonal is c0·s⁻⁴, not a 4D operator times a fibre mode count. The Euclidean-contracted vector sector has lowest eigenvalue −|f1−f2|, unbounded below. Exact structure: Box = C_so(4,1) − C_so(3,1), ghost operator −Box, fibre-constant density (5m²−3ℓ²)/(4m⁶), bosonic F² coefficient (22−n_ex)/6. The proposal adds the bib entry BenArous1989.

Original target, quoted from Appendix H, sec:status-F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- Ch. 17 says: "CRITICAL PATH; OPEN."
- The target is the matrix-derived G_eff (sign and size), with Problem F's A, B, C evaluated. The package does not derive it. It does not claim to.
- I found no discrepancy between the Ch. 17 and Appendix H labels.

## Checks performed
**Direct verification, mine:**
- **Anchor and labels.**
  - `\section{Problem G: HBEV}` occurs once (appH line 1961), immediately after the 016 block that ends at line 1959.
  - `thm:Geff`, `ch:vierbein-emergence` and `ass:EE` are each defined once.
  - No label is added or changed.
  - The block has no `\LUV_` subscript and no process language.
  - The block ends with a single status sentence.
- **Casimir structure.** By hand: {T_a,T_b} = s M_ab, [D_a,D_b] = s J_ab, Box = C_so(4,1) − C_so(3,1), [Box,J^ab] = 0. On functions of y, D^a = s(y⁴∂^a − y^a∂_4), so Box f = m²□f − y·∂f. The script `check_casimir_forms.py` agrees for both s.
- **Fibre-constant density.** I wrote my own sympy check. The Laplace-type form is P = −Box. I used G^{μν} = m²η, the Christoffel-corrected first-order term, and the convention a₁ = tr(R/6 − E) with E = ∇ω + ω² (the manuscript's operator −D² + E). At a rational point the density is 103469361778125/339271699168586, equal to (5m²−3ℓ²)/(4m⁶). It is a formal Lorentzian evaluation (see R3).
- **Landau diagonal.** Each plane gives f/(4π sinh sf). After the substitution u = s|ζ| the scaling is exactly s⁻⁴, and the prefactor is 1/((2π)²·16π²) = 1/(64π⁴). For f1 = f2 the integral is ∫u³/sinh²u du = (3/2)ζ(3), so c0·ν = 2π·(3/2)ζ(3)/(64π⁴) = 3ζ(3)/(64π³). **I checked the 3ζ(3) closed form by hand and the script's number matches (0.0018172584…).**
- **Vector sector.** The Hessian is −D² − 2F_ab, where F_ab = s J_ab = [D_a,D_b] up to sign, so the term is the standard Nielsen–Olesen −2F. The Zeeman eigenvalues are ±2f1 and ±2f2. The lowest level is f1+f2−2max(f1,f2) = −|f1−f2|, with order-|ζ| growth, so it is unbounded below. The script's Fock diagonalisations at (1,1), (1,3) and (0.3,2) agree.
- **Series coefficient.** The scalar series is 1 − s²Σf²/6. The vector is (4 + 4s²Σf²)(1 − s²Σf²/6). With ghost weight −2 and n scalars the total is 2 + n + s²Σf²(10/3 + 1/3 − n/6), i.e. (22−n)/6. This is the usual 11/3 − n/6 of one-loop YM.
- **Literature.**
  - Crossref DOI 10.5802/aif.1158 confirms title, Ben Arous, Ann. Inst. Fourier 39 (1989) no. 1, pp. 73–99.
  - Numdam gives the abstract only: expansion on the diagonal under Hörmander's strong hypoellipticity.
  - The abstract does not mention the nilpotent leading term. I corroborated that independently from Colin de Verdière–Hillairet–Trélat, arXiv:2004.06461, Thm A and Cor 1.2.1. They state t^{Q(q)/2} e(t,q,q) = ê^q(1,0,0) + c₁t + … at regular points, with the coefficient identified through the nilpotentization. They say they recover the result of Ben Arous and Métivier.
  - That corollary also shows the on-diagonal corrections come in integer powers of t. The block's O(s^{1/2}) is correct but weaker than necessary (optional).
  - The hypotheses, strong Hörmander and no drift, hold for Σ(D^a)². The result is local.
  - The citation is therefore adequate for the form of the leading term. The theorem statement in the 1989 paper itself is "not independently verified"; the secondary source is. No SME consultation is needed.
- **Re-run scripts.** I re-ran all four check scripts. I did not re-derive the ranks (4 and 6) in a new script. They rest on the 013-vetted realisation and are labelled numerical.
- **Compile record.** I read the researcher's `compile_check_r1.out.txt`: 264 pages, 0 errors, 0 undefined references. I did not run the build.

**Not verified:** the rank claims on all of the leaf; the f1/f2 range outside the sampled (point, direction) pairs (see R5); the full text of Ben Arous 1989.

**Merged 011 text (appH ~1877–1886, "Heat kernel over a fuzzy factor").** I read the whole paragraph, the surrounding conjugate-coordinate material, and ch08, ch17 and appA.
- 011 states the replication ("each four-dimensional sector is replicated over the dim Mat(H_C) modes, … threshold factor F") only "for the product leaf with a finite fuzzy factor", where the operator is O_s⊗1 + 1⊗Box_C.
- The same text says the CP^{1,2} leaf is not a product and that "the matrix-induced tensor on the six-dimensional leaf has rank four". Nothing in appH or elsewhere asserts the replication for CP^{1,2}.
- 018 shows that replication is the sf ≪ 1 limit of the hypoelliptic diagonal, and that the Poisson limit with unbounded |ζ| leaves that regime.
- **Decision: 018 bounds a conditional statement and does not contradict it. There is no PRIOR-CLAIM-ERROR, and M3 does not apply.**
- No other statement in the 30 files conflicts: ch08, ch17, appA, appG, ch16 and ch18 do not assert a product or fibre mode count for the CP class.
- Emergence: nothing here makes spacetime or the metric fundamental. The scope sentence disclaims identification of G with the emergent metric and says the paragraph does not bear on ass:EE.

## Findings
All minor. Every one is a wording fix needing no new physics.

- **R1. Minor. Location: first sentence of "Hypoelliptic structure".** The text says "Hence Box is a sub-Laplacian of step two…" for the η-contracted Box = C_so(4,1) − C_so(3,1). With η = diag(−1,1,1,1), Box is not a sum of squares, so the sub-Laplacian and Hörmander results do not apply to it. They apply to the Euclidean contraction Box_E = Σ_a(D^a)², where D^a = J^{a4} are the same vector fields. Box_E is not the so(4,1)−so(3,1) Casimir difference. The ranks, step and Q = 8 depend only on the D^a and are contraction-independent. The Euclidean contraction appears only later in the paragraph.
  - Required action: state in that sentence that the statement is for the Euclidean contraction η→δ of the contracted index, and that ghost and vector operators are then built from Box_E.
- **R2. Minor. Location: consequence (ii).** "it has no sign-definite heat trace" is inaccurate. Every e^{−sE} is positive, and the lowest level is −c|ζ|, so e^{−sH_V} is unbounded and the ζ-integral diverges for every s > 0 at the leading symbol.
  - Required action: replace with "e^{−sH_V} is unbounded for every s > 0 at the leading symbol, so the proper-time trace of this sector diverges and is not regulated by the cutoff".
- **R3. Minor. Location: fibre-constant density sentence.** The value (5m²−3ℓ²)/(4m⁶) is a formal evaluation of the Seeley–DeWitt algebra for η = diag(−1,1,1,1). The block does not say so, yet the same paragraph then moves to a Euclidean-contracted analysis.
  - Required action: add "(formal evaluation for η = diag(−1,1,1,1); no Euclidean heat-kernel statement is made for this sector)".
- **R4. Minor. Location: closing scope sentence.** The regulator choice (H5, the proper-time cutoff of Box_X) and "one loop" are hypotheses of the no-go but are not listed.
  - Required action: add both to the list.
- **R5. Minor. Location: Euclidean-contraction sentence.**
  - (a) "f1/f2 lies between 0.006 and 0.84" is from 12 points × 9 ζ-directions (linspace(0,π,9)). Say so, e.g. "at 12 sampled points and 9 directions of ζ each". This is not a claim over all of the leaf.
  - (b) "for which no heat kernel exists" for the Lorentzian contraction is too strong. Say instead that the Euclidean heat-kernel construction does not apply to that case.
- **R6. Minor. Location: closing sentence of the block, and ahead of consequence (iv).** `w` and `\varrho` are used without definition. Add a pointer, e.g. "with w and ϱ = Λ/w the induced and tree-level coefficients of the preceding paragraph".
  - Item (iii) is correctly conditional on s f_j ≪ 1. The proposal's reading of the s² term as "logarithmic" is the finite-fibre statement. Keep the block's wording and do not strengthen it.
- **Optional.** Replace O(s^{1/2}) with O(s) on the strength of the cited corollary. In the proposal text (not the block), "the sign of w is scheme-dependent" is stronger than anything established. Do not move it into the manuscript.

## Scope of what is established
**Established (exact).**
- The Casimir/Poisson-algebra identities, [Box,J^{ab}] = 0, the ghost operator −Box, and the fibre-constant invariant subspace.
- The l = 0 density formula as a formal Lorentzian algebraic evaluation. Its relevance to w is not claimed.
- The Landau and Weyl closed forms for the nilpotent model, including 3ζ(3), the Zeeman spectrum −|f1−f2|, and the (22−n_ex)/6 coefficient, conditional on s f_j ≪ 1 and the nilpotent model.

**Conditional or numerical.**
- Rank 4 and 6, and the f1/f2 range, are numerical at sampled points.
- The s⁻⁴ asymptotics rest on the cited nilpotent-approximation result at equiregular points.
- The Euclidean contraction η→δ with the Lie–Poisson algebra kept is a continuation choice, as the block states.

**Class of the no-go.** It holds within these hypotheses:
- H1 Poisson limit and leading (nilpotent) symbol;
- H2 Euclidean contraction η→δ, Lie–Poisson algebra kept;
- H3 equiregular points (y⁴ ≠ 0);
- H4 bosonic content, background gauge, one loop;
- H5 regulator = proper-time cutoff of Box_X.

It excludes the product/replication reading as the Poisson-limit diagonal, and it exhibits the Nielsen–Olesen-type unboundedness of the vector sector. It does not close any direction outside H1–H5. The regime-of-validity remark (Λ_UV vs the NC scale) is a conjecture, correctly labelled.

**Not derived:** w, its sign, or ϱ. Problem F remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change, no LABEL-CHANGE-PROPOSED, no AUTHOR-DECISION.

**Open avenues** (each a relaxation of an H-item, ranked by my judgement of how much it favours the infrared or full-GR derivation):
1. **Relax H4, bosonic content: fermionic or supersymmetric partners, or a fibre truncation.** The Zeeman instability is the obstruction to any definite sign of w in the bosonic class, and a fermionic content change is how the published IKKT one-loop mechanism avoids it. Such a content change would need the usual structural review.
2. **Relax H1, Poisson limit and leading symbol together: exact so(4,2) harmonic analysis and character technique at the quantum-space level, Moyal terms included.** This treats Λ_UV ~ Λ_NC directly. It is the only route that does not presuppose the sf ≪ 1 or Landau regime.
3. **Relax H1, leading symbol: the second-order sub-Riemannian symbol, meaning the weight-two s⁻³ term of the diagonal and its A-variation in the nilpotent model.** This is the direct computation of w, but only meaningful once avenue 1 or 4 fixes the vector-sector problem. The cited expansion has integer powers, so the weight-two coefficient is a well-defined target.
4. **Relax H5 and H3: a different regulator, for example a cutoff on fibre harmonic number l, which restores the product regime.** The connection-sector torsion term X for the CP class is still not derived.
5. **Relax H2: a compact Euclidean section (twistor CP³ → S⁴).** Self-dual horizontal curvature replaces the instability by a zero-mode family. A consistency check only, since signature remains Problem E.

## Recommended disposition
Revise (R1–R6, wording only) and then integrate. A re-review of the revised block should be quick; the substance is verified. Add the bib entry BenArous1989 as proposed; I checked it against Crossref (title, author, volume, pages, year, DOI). The `{\'e}` spellings should follow the bib file's existing style (the integrator should confirm). The package is coherent: one problem, shared hypotheses, no unrelated bundling.

**Significance and BREAKTHROUGH.** M2 narrow: a reproducible bounded obstruction to the product reading, plus a clear locus for where the missing computation sits. Not a BREAKTHROUGH. It derives no critical-path step, changes no label, and w is undetermined.

## Corrected snippet
Wording only; no new physics.
- R1: replace "Hence \(\Box\) is a sub-Laplacian of step two…" by "Hence, for the Euclidean contraction \(\eta\to\delta\) (the operator \(\Box_E=\sum_a(D^a)^2\), which is not the Casimir difference above), the operator is a sub-Laplacian of step two with homogeneous dimension \(4+2\cdot2=8\), not an elliptic operator on a product."
- R2: replace "it has no sign-definite heat trace" by "\(e^{-sH_V}\) is unbounded for every \(s>0\) at the leading symbol, so the proper-time trace of this sector diverges".
- R3: after "which is not of definite sign" insert "(a formal evaluation for \(\eta=\mathrm{diag}(-1,1,1,1)\))".
- R4: add "the proper-time cutoff of \(\Box_X\) as the regulator, one loop," to the closing list.

Extra assumptions: none.

Files: /c/Users/redgi/Projects/namcg-lab/proposals/018-induced-coefficient-cp12/proposal-r1.md and block-r1.tex (reviewed); chapters/appH-microscopic-proofs.tex lines 1877–1886 and 1961 (anchor and 011 text).
