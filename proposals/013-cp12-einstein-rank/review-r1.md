VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1

## Verdict
The kinematic result is correct and reproduced independently: image dimension 9, linearised Einstein rank 6, kernel on the image equal to the 3 transverse diffeomorphisms, and the exact constraint q_μq_νh^{μν}=0. One unverified attribution sentence must go and a few scope and wording points need fixing before integration. It is a bounded positive sub-lemma, not a BREAKTHROUGH.

## Source reading
Digest + targeted reads. The digest was reported CURRENT by the orchestrator, and this is not a 5th-item scan.

Read in full:
- `proposals/013-cp12-einstein-rank/proposal-r1.md`.
- appH ledger F (lines 1103-1118).
- appH 008 paragraph (line 1820), the 011 paragraphs (1837-1855), the anchor region, and appH 795-812.
- ch17 lines 60-120 (criterion table).
- `reports/ledger.md`.
- `MILESTONE.md`.
- ch03 Remark `rem:ch3-trace-quadratic` (head).
- `cp12_realisation.py`, `check_cp12_rank_exact.py` and its output, `check_cp12_base_selection.py` and its output, and the geometry output.

Not read in full:
- The Monte Carlo second-moment script (output only).
- Other chapters beyond a grep for stale "rank not computed" and conjugate-coordinate statements.

Running `check_cp12_geometry.py` regenerated two tracked by-product files (`Wy_numeric.npy`, `geometry_summary.json`). I restored them with `git restore`; `git status` is clean.

## Claim under review
The claim is a kinematic result in `H_CP`: Poisson limit, CP^{1,2} conjugate-coordinate class (011), linear order, frozen coefficients, leading order in 1/(|q|ℓ), fibre-integrated operator tensor.

Original target: Problem F (`ass:emergent-op`), with A, D1 and E by dependency. Appendix H `sec:status-F` reads verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." The Chapter 17 set (A, B, C, D1, E, F, G-derived, N) matches. The proposal changes no label. The target is not met.

## Checks performed
**1. Linear response (direct, by hand).**
- δK^{μν}=s m({A^ν,y^μ}+{A^μ,y^ν}) follows from {T^a,y^μ}=s η^{aμ}m.
- The fibre-integration identity is correct. It uses ∫{f,g}=0, the Leibniz rule, {y^μ,χ(y)}=∂_ρχ{y^μ,y^ρ} with {y^μ,y^ρ}∝M^{μρ}, and m a function of y alone.
- This gives ∫dμ δK=m∂_ρ(B^{ν;μρ}+B^{μ;νρ}) exactly, with B=∫dμ A M^{μρ}.
- Only the projection of A onto span{M^{μρ}} (a 3-dimensional function space) survives. So fibre-constant fluctuations and harmonics l≠1 give no linear response, exactly.
- ∂_μ∂_ν(δ𝒦^{μν}/m)=0 holds by antisymmetry.
- The `y^4>0` sheet and the fold are correctly excluded from the hypothesis.

**2. Fibre geometry.**
- I re-ran `check_cp12_geometry.py` (base point (5,3)).
- Reproduced: M^{ab}y_b=0 to 5e-14; M^{μρ} has rank 3 on the fibre; T^μ lies in the span (residual 1e-13); W_y equals the projection of the self-dual forms of y^⊥ (2.4e-14).
- Reproduced: the opposite chirality is off by 1.66, and T^μ=−M^{μσ}y_σ/y^4.
- The 12 amplitudes (R^4⊗W_y) coincide with the frame-type fluctuations κ^ν_σT^σ modulo k^νy_σ: 16−4=12.

**3. Rank, independent re-derivation.**
- I wrote my own float script (scratchpad `gk_check.py`). It builds W_y by Hodge duality in an orthonormalised y^⊥ of R^{1,4}, at generic y with y⃗≠0, and uses my own linearised-Einstein symbol.
- Over 6 random (y,q): image dimension 9 and rank 6 every time. Null q: rank 3. Fold (y^4=0): image 7 and rank 5. All match the proposal.
- I also re-read the researcher's exact-rational output (4 base points, 12 generic q plus special q):
  - dim I=9, dim(I∩Diff)=3, rank E|I=6.
  - E[gauge]=0 and E[q∘ξ]=0.
  - The image of E is conserved.
  - Chirality-independent.
- The `lin_einstein` routine is the 009 routine. I confirmed E has rank 6 on all 10 tensors for generic q.
- I did not re-run the exact-rational script itself. I checked its logic and its saved output.

**4. Structure of the rank result.**
- I = {h : q_μq_νh^{μν}=0} is a hyperplane that does not contain Diff.
- Any 9-dimensional hyperplane complementary to the longitudinal diffeomorphism has I∩Diff of dimension 3 and E|I of rank 9−3=6.
- Rank 6 is therefore equivalent to surjectivity of b↦h onto the hyperplane, which is a count (12≥9).
- To test the dependence on the geometry, I replaced W_y by random 3-planes of Λ²(R^4). Image 9 and rank 6 again. So the result is generic and insensitive to the detailed W_y.
- This is not an error; it is a significance limit (see Findings, point 3).

**5. Lower-semicontinuity step.** The image of E lies in the 6-dimensional conserved space and the rank is lower-semicontinuous, so 6 is the generic rank. The argument is valid.

**6. Gauge identification.**
- A^ν={Λ,T^ν} gives, at leading order, b^{ν;μρ}∝q^νΛ^{μρ} and h=q∘(Λq) with ξ=Λq. Here ξ·q=0 because Λ is antisymmetric.
- The map Λ↦Λq is injective on W_y, so the gauge image is the full 3-dimensional space {ξ·q=0} = I∩Diff = ker E|_I. The identification is exact at the leading symbol.
- The longitudinal diffeomorphism lies outside I because qqh=2q²(q·ξ)≠0.
- The gauge group of the matrix class is therefore the divergence-free diffeomorphisms (unimodular-type), with the density fixed by the Liouville measure. This is a consistent, not a mismatched, structure.
- Count: 10−3 (gauge) −1 (relation) = 6 = 10−4 = number of conserved sources. So no gauge mismatch obstructs the count.
- The absence of the longitudinal mode is a real structural feature. It should be stated as such, not as a defect.

**7. Methodology consistency with 008/009.** 008 and 009 counted the rank of E on the image of the linear response map against the 6 conserved sources, with the identical `lin_einstein`. The 013 count is consistent with that.

**8. Base-function paragraph.**
- The analytic K_u^{μν}=α²η_abM^{aμ}M^{bν}+β²m²η^{μν} is verified directly from Poisson brackets in the explicit realisation (deviation ≤7e-15).
- The Box eigenvalues are verified directly (script output).
- The gradient-rank script uses the analytic K_u and Box u as inputs. It confirms only the rank consequences, not the brackets (the brackets I checked separately).

**9. Literature and BibTeX.**
- Crossref for DOI 10.1007/JHEP07(2019)010: title "Covariant cosmological quantum space-time, higher-spin and gravity in the IKKT matrix model", authors Marcus Sperling and Harold C. Steinacker, JHEP 2019, issue 7, article number 10.
- The arXiv 1901.03522 abstract matches: covariant FLRW space-time from projecting the fuzzy hyperboloid H^4_n, higher-spin tower, linearised Einstein-Hilbert-type action by gauge invariance.
- **BibTeX record: VERIFIED** (metadata level; the content of the paper beyond the abstract is not independently verified).
- Attribution: the abstracts support only the H^4_n/S² fibre, the FLRW base and the higher-spin tower. They do not support equating the first-harmonic amplitudes with a "lowest member" of that tower (see Finding 1).
- The CP^{1,2} setting itself is attributed to `MantaSteinacker2025`, which is already in the bib and is not re-read here.

**10. Anchor and labels.**
- `\section{Problem G: HBEV}` occurs exactly once (line 1857).
- The labels `def:matrix-coords-ext`, `rem:ch3-trace-quadratic`, `ch:vierbein-emergence` and `ass:EE` each occur once.
- `ass:emergent-op` occurs once. Verified by `verify_anchors_labels.out.txt`, and I grep-checked the anchor myself.
- No new labels. No process language in the LaTeX.
- The status sentence closes only the second paragraph, which is fine.

**11. Emergence.** Spacetime stays emergent: G is built from K, a fibre average, and the base functions are functions on the leaf. Nothing makes the metric fundamental.

## Findings

**1. Major (attribution). Location:** last sentence of the first LaTeX paragraph ("The amplitudes are the lowest member of the tower of fibre harmonics studied in~\cite{SperlingSteinacker2019,MantaSteinacker2025}; no comparison with those results is made.")
- **Finding:** The sentence asserts an identification with the tower of those papers while disclaiming any comparison. The proposal's own Literature section admits the papers' matrix definitions (X^μ=M^{μ4} or M^{μ5}) were not read.
- **Reason:** The class here takes T^a=M^{a4} as the matrices and y^μ=M^{μ5} as the base functions. Whether the first fibre harmonic of A^ν is the "lowest member" of their tower, or sits in a different spin sector, is not verified.
- **Required action:** Replace by a hedged sentence (see Corrected snippet 1).

**2. Minor (stale text). Location:** the 011 paragraph's closing line ("... does not compute the rank of the linearised Einstein operator in the conjugate-coordinate class", appH line ~1846) and the new paragraph's opening.
- **Finding:** After insertion the earlier line reads as stale.
- **Required action:** Open the new paragraph with one cross-reference clause saying it supplements the preceding paragraph, whose rank was left uncomputed. Leave the 011 text unchanged (see Corrected snippet 2).

**3. Minor (significance and scope wording). Location:** the "Response" paragraph.
- **Finding:** The text does not say that the rank-6 conclusion is equivalent to surjectivity of the 12 amplitudes onto the hyperplane qqh=0. It also does not say that it holds for any generic 3-plane W_y (my random-plane test).
- **Reason:** Without this, the result can be read as a fine-structure consequence of the CP^{1,2} geometry. It is essentially a count: 12 amplitudes against 9 components.
- **Required action:** Add one clause (Corrected snippet 3). Also state that the image hyperplane is not diffeomorphism-covariant: the longitudinal mode is absent, so the gauge group of the class is the divergence-free diffeomorphisms.

**4. Minor (reference mismatch). Location:** "The tree-level quadratic action of Remark~\ref{rem:ch3-trace-quadratic} ...".
- **Finding:** That remark is stated for the constant-Θ Heisenberg (Weyl) setting, not for CP^{1,2} with a mass term.
- **Reason:** Citing it as supplying the action in this class is loose. The "if it is of the form" hedge helps but does not fix the referent.
- **Required action:** Reword as "a Yang-Mills-type quadratic action, analogous to that of Remark~\ref{rem:ch3-trace-quadratic}, built from first derivatives of A. No such action is computed in this class". Keep the counting remark labelled as undecided.

**5. Minor (base-function paragraph).** Two sentences overstate.
- "For α≠0 ... Box u^μ=−(3αT^μ+βy^μ)/R² is not a function of u". For β=0, Box T^μ=−3T^μ is a function of u, and the script shows Box u closed for (1,0). Only K_u fails there. Say "for α≠0 K_u is fibre dependent; for α,β both nonzero Box u^μ is also not a function of u".
- The (α,β)=(1,1) case: the numerics show du of rank 4, so u is not an independent chart and the test is vacuous. State "for α=β the u^μ are not independent and the test does not apply", or restrict to α≠±β.
- Also qualify "a numerical gradient-rank test ... confirms both failures" to "a gradient-rank test, using the analytic K_u and Box u, confirms".

**6. Minor (sheet).** The fibre over y^μ in the 2:1 chart has two sheets (y^4=±). The text already defines the measure "on a sheet y^4>0". Add that the other sheet, which has the opposite chirality of W_y and the opposite sign of m, is not included. (My expectation is that the rank is unchanged, but this is not computed.)

**7. Minor (honesty already present, keep).**
- The gauge invariance holds only at the leading symbol.
- The algebraic remainder is relative O(1/(|q|ℓ)).
- Gauge parameters in harmonics l≥2 break the E-invariance at subleading order.
- This limits the use of the result: it gives no exact gauge-covariant equation.
- The text discloses this; keep it.

## Scope of what is established
**Proved or exact** (within `H_CP`):
- The first-order formula for δK.
- The fibre-integrated response and the constraint.
- Only the first harmonic contributes.
- The fibre geometry (numerical, plus group theory).
- Image dimension 9, rank 6, kernel = transverse diffeomorphisms.
- 12=3+3+6 at the leading symbol, with the density fixed by Liouville.

**Conditional:**
- Poisson limit, linear order, frozen coefficients, leading order in 1/(|q|ℓ).
- The object is the fibre-integrated tensor on one sheet.
- Input: η=diag(−1,1,1,1), the choice T^a=M^{a4}, the orbit CP^{1,2}.
- Base functions y^μ are held fixed (step 6 handles relabelling).

**Not established:**
- Any field equation. The proposal itself notes that a tree-level F² action gives second-order equations while E[h(b)] is third order.
- Masses and positivity of the 12 amplitudes.
- O(1/(|q|ℓ)) terms.
- Fibre-non-constant parts of δK.
- Identification of G with the emergent metric.
- G_eff.
- The background as a solution.
- That y^μ is the physical base. The closure criterion works only within the Lorentz-vector family.

**Status:** PROGRAMME-CONDITIONAL. Problem F and the other critical-path problems stay OPEN; no label change.

**No-go side result** (within the hypotheses): fibre-constant matrix fluctuations (the ordinary 4D gauge fields) and all harmonics l≠1 give no linear response in the fibre-averaged operator metric. This is exact in this class. A route that relaxes the fibre-average, the fixed base functions, or the linear order is not excluded.

**BREAKTHROUGH judgment: not flagged.**
- It does not derive a critical-path step. It removes the kinematic count obstructions of 008, 009 and 011 only at the leading-symbol, linear, frozen level.
- The rank-6 conclusion follows from a count (12 amplitudes onto a 9-dimensional hyperplane) and holds for generic 3-planes.
- There is no dynamics: no action, masses or positivity.
- There is a third-order versus second-order mismatch.
- The gauge invariance is only at the leading symbol.
- It is neither a decisive resolution nor an "important missing link" in the sense of the author directive. It is a valuable bounded positive sub-lemma: it identifies the first class where the counting obstructions are absent and sharpens where the real work lies (the dynamics of the level-1 amplitudes).
- MILESTONE: none. No M1-M5 trigger fires: nothing is derived, no no-go rules out a currently kept route, no prior claim is wrong, and no label or core change is proposed.

## Recommended disposition
Revise (Findings 1-6), then integrate the two appH paragraphs before `\section{Problem G: HBEV}` and add the BibTeX entry `SperlingSteinacker2019` (record verified). Findings 2-6 are short wording edits. A short r2 confirming the edits is sufficient.

## Corrected snippet
No new physics is needed; no extra assumptions.

1. Replace the last sentence of the first paragraph with:
`Fibre harmonics of the fluctuation matrices form the higher-spin tower described in~\cite{SperlingSteinacker2019,MantaSteinacker2025}; the relation of the amplitudes \(b^{\nu;\mu\rho}\) to that tower is not examined here.`

2. Start the first paragraph with:
`This paragraph supplements the preceding one, which left the rank of the linearised Einstein operator in this class uncomputed.`
Then continue with "Keep the conjugate-coordinate class ...".

3. After "...so the image has dimension at most nine", add:
`The rank is a consequence of the image being the whole hyperplane \(q_\mu q_\nu h^{\mu\nu}=0\) and does not depend on the particular three-dimensional space \(W_y\); this hyperplane is not invariant under longitudinal diffeomorphisms, so the gauge group of the class is that of divergence-free diffeomorphisms.`

4. Replace "The tree-level quadratic action of Remark~\ref{rem:ch3-trace-quadratic}, if it is of the form ..." with:
`A Yang--Mills-type tree-level quadratic action, analogous to that of Remark~\ref{rem:ch3-trace-quadratic} and built from first derivatives of \(A\), gives equations of second order in these amplitudes (no such action is computed in this class), whereas ...`
Keep the rest.

5. Base-function paragraph: replace "and \(\Box u^\mu=-(3\alpha T^\mu+\beta y^\mu)/R^2\) is not a function of \(u\) (a numerical gradient-rank test at random points of the leaf confirms both failures)" with:
`and for \(\beta\neq0\) also \(\Box u^\mu=-(3\alpha T^\mu+\beta y^\mu)/R^2\) is not a function of \(u\) (a gradient-rank test at random points of the leaf, using these expressions, confirms both failures; for \(\alpha=\beta\) the \(u^\mu\) are not independent and the test does not apply)`.

6. In the "Response" paragraph, after "on a sheet \(y^4>0\)", add:
`(the other sheet is not included)`.
