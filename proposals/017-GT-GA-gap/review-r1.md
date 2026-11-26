VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The gauge-parameter lemma, the α-cancellation (on the stated domain) and the Dirac a_1 are correct, and the package is a useful bounded no-go. Three scope statements in the LaTeX are unsupported or incomplete and must be corrected first. These are the tip-domain claim, "for every α>0", and the omission of the periodic fermion gluing.

## Source reading
FULL SCAN. `python scripts/make_digest.py --check` printed DIGEST CURRENT, and `chapters/` is clean (no `dirty-chapters` flag). The scan was mandatory because this would be integration ordinal 15, a 5th-item case under CLAUDE.md 3(a).

I read all 30 files in the current manifest:
- ch01–ch18: ch01, ch02, ch03, ch04, ch05, ch06, ch07, ch08, ch09, ch10, ch11, ch12, ch13, ch14, ch15, ch16, ch17 (in full), ch18.
- appA–appL: appA, appB, appC, appD, appE, appF, appG, appH, appI, appJ, appK, appL.
- appH was read in full, in segments covering lines 1–2464.

I also read the proposal, appH_insert.tex (byte-identical to the proposal's LaTeX block; checked), the SME scout `reports/sme-scout-gap-GT-GA-20261015.md`, MILESTONE.md and the ledger tail.

## Claim under review
Target: the G_T ≠ G_A gap of integrated proposal 015, in `sec:status-B`, which is the normalisation half of B1/B2. The package claims the gap is not closed by:
- the 't Hooft parameter α, or an EOM term in the gauge function;
- Dirac fermion content;
- frame, Kabat or centre choices.

Current Appendix H labels, quoted verbatim:
- **Problem B:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **Problem F** (touched, since the induced coefficients are involved): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
- **Problem A** (touched through the replica gluing): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

Chapter 17 `sec:ch17-done` lists A, B, C, D1, E, F, G-derived and N as critical path (unchanged). No label change is proposed or implied.

## Checks performed
**Direct verification (mine):**
- **Gauge lemma by hand.**
  - Jacobi gives [D_μ,D_ν]={Θ_{μν},·}, and D_μ is a derivation.
  - So [D_μD_μ,D_ν]φ = {E_ν,φ} + 2{Θ_{μν},D_μφ}.
  - With O_v a_ν = O_s a_ν − 2{Θ_{νl},a_l} (the sign in the merged appH, line 1755) the cross terms cancel, leaving O_vG = GO_s − {E,·}.
- **Independent exact-rational check.** Script `gi.py` in the session scratchpad, with a different nonlinear Poisson bivector (a different polynomial ψ, different Θ̄ and a different point).
  - The residual is exactly [0,0,0,0] with the manuscript sign of the 2{Θ,a} term.
  - With the opposite sign the residual is nonzero, so the sign matters and is correct.
  - E at the point is non-zero, so the check is off shell.
- **Proposal scripts re-run.**
  - `check_intertwining.py` reproduces residual 0 and the Jacobi and ρ-divergence residuals.
  - `hk_eval.py vector 0.5 n=16` gives TT = 0.79165/0.79179 against the closed form 0.79167, and the third mode 1.12509 against 1.12500. n=12 is coarser: 0.791/0.796 and 1.127.
- **Decomposition algebra by hand.**
  - κ = 1−1/α, so O_κ|Ran G = O_s/α.
  - Tr e^{−sO_κ} = Tr e^{−sO_v} − Tr e^{−sO_s} + Tr e^{−sO_s/α}.
  - The connection sector is therefore (3+α)/6 ρR + ρ²X on E=0 backgrounds.
  - Hence c_T(α) = (N_s+α−1)/6 − 11/3, c_A(α) = (N_s+α+1)/6, and the difference is 4.
- **Ratio-3 test.** Net third/TT = 3 requires α² = 9, so α = 3 (checked by hand, with the fitted third-mode form). The SME ratio test is therefore not a gauge-invariant diagnostic. The correction is right.
- **Fermion operator.** O_f = O_s − ½γ^{μν}{Θ_{μν},·} = O_s − Σ^{μν}{Θ_{μν},·}, the same form as O_v with the spinor representation.
  - This confirms the Dirac Dynkin ratio ½.
  - It also confirms a_1 = (4/6)ρR + ½ρ²X, with eigenvalues (1/3,1/3,0).
  - The weights are right: −1 for Dirac over 4 components, −½ for Majorana-Weyl over 16 real components. So b_total = 1 − n_D/2 and n_D=2 gives b=0.
- **Gap arithmetic.** Antiperiodic gluing gives c_A(Dirac) = +1/3 and gap 4−n_D. Periodic gluing gives c_A(Dirac) = −2/3 and gap 4−2n_D (see finding 3).
- **Literature.** Solodukhin arXiv:1104.3712, text extracted with pdftotext.
  - Eq. (126)–(127): S ∝ D_s/6, D_{1/2}(4)=2 for Dirac with fermion weight ½. So Dirac = 2 scalars in the cone area term. ✓
  - Eq. (136): a_1^{(1/2)} = −(D_{1/2}/6)R. ✓
  - Eq. (147): a_1 = (D_1/6 − 1)R, which is −2/3 at d=4. ✓
  - So the proposal's Kabat contact of −1 in c-units (6 scalar units) is consistent with the source, and the SME's 1/6 was a magnitude error. ✓
  - The equation numbers refer to the arXiv PDF.
- **Anchor.**
  - The sentence "…they give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open." occurs once, at appH line 179, as the end of the 015 block.
  - `\section{Problem C: conformal mode and Cassini}` occurs once, at line 181.
  - The generic closing sentence recurs elsewhere but not in this combination.
- **Labels and macros.**
  - `rem:ch3-trace-quadratic`, `eq:O-eta` and `ass:EE` are each defined once.
  - `\LUV` is defined at namcg-book7.tex line 54. The bib keys IKKT1997 and Solodukhin2011 exist once each. No label is added or changed.
  - The insert contains no process language, and the two paragraphs do not carry consecutive repeated status lines.
- **Emergence.** Preserved. G is built from Θ, and η contracts only the matrix indices, exactly as in the merged a^μ treatment.

**Not independently verified:**
- The off-shell TT eigenvalue 5/6 − (α−1)/24 and the third-mode form are numerical fits only. I re-ran one point, α=2.
- The EOM-gauge-function shift c²q²/(2p²) was not re-run.
- `cone_twist_zeta.py` was not re-derived. Only its Dirac = 2 scalars ratio and its Maxwell −2/3 were cross-checked against Solodukhin.
- Steinacker arXiv:2303.08012 was not opened, and the proposal uses no number from it.
- The "D=4,6 give b=3/4, 1/2" claim is proposal-only and not in the LaTeX.

## Findings

**1. MAJOR. Location:** LaTeX paragraph 1, last sentence ("a different choice of domain changes it by an α-independent amount, because a finite set of angular modes has a scale-free transverse trace"). The same claim is in proposal §2 "Remark" and row 3b.
- *Finding:* The justification fails.
  - The cone term is (parallel heat kernel A/(4πs′)) × (transverse constant), with s′ = s/α in the longitudinal sector.
  - A domain change in that sector shifts the transverse constant by some δ⊥. That is multiplied by the parallel factor α/s, so it appears as α·δ⊥ and is not α-independent.
  - A vector-versus-scalar tip domain also changes the non-minimal operator's transverse trace by a κ-dependent amount.
  - So the stated reason for the robustness of the α-cancellation under domain choice is unsupported, and probably false.
- *Required action:* Delete the sentence. State only that the α-independence of the gap holds for the stated domain and that other tip domains are not examined. In the proposal, withdraw "an α-independent tip-local ambiguity of O(1)" (row 3b). The claim that a Kabat or centre shift "cannot remove a gap of 4" is an order-of-magnitude observation (Kabat = 1 against 4), not a theorem.

**2. MAJOR. Location:** LaTeX paragraph 1, "so \(1/G_A-1/G_T=2\LUV^2/\pi\) for every \(\alpha>0\)", and the matching headline claim in the proposal.
- *Finding:* The off-shell δρ=0 eigenvalue 5/6 − (α−1)/24 is numerical, with agreement ≤2×10⁻³ at α = 1/3…3 only. The α=4 run did not converge, as the proposal itself says.
  - The lemma is exact only on E=0 backgrounds, and conditional on domain, zero modes and the continuation in n.
  - "For every α>0" is therefore an extrapolation. The verb "gives" in "a second-order evaluation … gives" also reads as derived.
- *Required action:*
  - Say "numerical evaluation" and call the closed forms "rational fits, not derived".
  - Restrict the explicit claim to 1/3 ≤ α ≤ 3. For E=0 backgrounds, state "every α>0" only under the conditions already listed.
  - Keep the sentence that the TT form agrees with the exact on-shell lemma.

**3. MAJOR. Location:** LaTeX paragraph 2 ("Then c_A = … and c_A−c_T = 4−n_D … equality needs n_D=4 …", and "the area coefficient does not [vanish]"), and proposal claim 2 ("zero only at n_D=4", numerology).
- *Finding:* The result depends on a gluing choice that is not presented as one.
  - The 015 baseline for a^μ is unrotated, pull-back gluing: every field is periodic in chart components.
  - The phase (−1)^{n+1} is what the polar-frame antiperiodic condition gives when the spinor index is transported with the replica rotation. That is the same kind of prescription as the "rotated" vector, not the unrotated one. So 4−n_D mixes two prescriptions.
  - Consistent alternatives, from the proposal's own arithmetic (`gap_table.py`):
    - unrotated, periodic fermions: c_A(Dirac) = −2/3, which equals its ρR coefficient, so the gap is 4b = 4−2n_D. This vanishes at n_D=2, and there c_T = c_A = 0;
    - rotated vector with antiperiodic spinor: 3−n_D (branch n<1) or 5−n_D (n>1).
  - The proposal mentions periodic gluing in one clause as "not the replica of a state". It does not report the zero-gap outcome.
  - So "SUSY content does not give equality" and "equality only at n_D=4" are conditional on a spin-structure assumption that the matrix state has not been shown to select.
- *Required action:* Report the periodic result in the LaTeX, explicitly as an equality of vanishing Λ² coefficients (0 = 0), not a derivation. Note that the choice of gluing belongs to Problem A. Make the closing statement conditional ("2 for antiperiodic, 0 for periodic gluing"). Drop "numerology" as a characterisation, or restrict it to the antiperiodic prescription. See the corrected snippet.

**4. Minor. Location:** LaTeX notation.
- `\mathcal G` is the backreaction tensor 𝒢_{μν} of ch04/ch08, and the new gradient map reuses it.
- E_ν (EOM vector) clashes with the endomorphism E and E_f in the same paragraph.
- *Required action:* Rename both.

**5. Minor. Location:** LaTeX paragraph 2.
- The fermion Yukawa couplings Γ^i[X_i,Ψ] to the N_s transverse matrices vanish on the background and are dropped. Say so in one clause.

**6. Minor. Location:** Appendix H, 015 block, line 179 ("they do not treat … fermions or additional scalars"), and the Presentation-A Poisson-limit paragraph ("does not treat … fermionic or additional scalar fields").
- These remain accurate for those paragraphs. The new paragraphs carry their own scope statement, so no edit is required.

## Scope of what is established
- **Established identity:** O_vG = GO_s − {E,·} and G†G = O_s, for any Poisson bivector. I verified it independently, including that the sign of the 2{Θ,a} term is essential.
- **Conditional (E=0 backgrounds, domain, zero modes, common cutoff on O_κ):** the decomposition and a_1 = ((3+α)/6)ρR + ρ²X. This also covers the cone coefficient (3+α)/6, and so the α-independence of c_A − c_T = 4 for the stated domain and gluing.
- **Numerical, fitted (1/3 ≤ α ≤ 3):**
  - the off-shell TT and third-mode eigenvalues;
  - the EOM-gauge-function shift, which enlarges the gap for real c and acts on all three modes;
  - the "ratio 3 at α=3" statement, a consequence of the fit.
- **Established algebra plus numerics:** the Dirac a_1 and the Dynkin ratio, and the fermion weights.
- **Conditional on gluing:** c_A(Dirac). The gap is 4−n_D (antiperiodic Cartesian phase), 4−2n_D (periodic, zero at n_D=2), or 3−n_D / 5−n_D (rotated vector).
- **Input, not derived:** the identification n_D=2, N_s=6 with the 10D content.
- **No-go class:**
  - Poisson limit, Euclidean section, one loop, Λ² term.
  - The two δρ=0 modes of a^μ.
  - Replica (I), pull-back gluing, with the tip domain stated.
  - Linear 't Hooft gauge families D·a, and D·a + cE·a for the EOM term.
  - Dirac fields built from the same D_μ.
  - The no-go does not close the direction beyond this class. It relaxes the hypothesis "Feynman gauge" and the hypothesis "no fermions". It does not relax "Λ² order", "tensor block = δρ=0 modes of a^μ", the gluing prescription, or Moyal corrections.
- **Problem B remains OPEN** (Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL), as do F and A.

**BREAKTHROUGH:** No. This is a bounded no-go with sharpening. It does not derive a critical-path step and does not change a label.

**M2** is justified, narrowly: two relaxations that the manuscript kept open (gauge parameter, fermion content at the Λ² order) are shown not to close the gap within the stated class.

**Ranked open avenues** (all stay within emergence):
1. **Next order in the D=10 content** (hypothesis relaxed: "Λ² term only"). At n_D=2, N_s=6, c_T = 0 for all gluings, and c_A = 0 (periodic) or 2 (antiperiodic). The first non-vanishing coefficient on both sides (log or a_2, Moyal) must be compared, and it must be done for each gluing. This is the most promising avenue.
2. **Replica gluing and internal-index rotation from the matrix state** (a Problem A sub-lemma; hypothesis relaxed: "pull-back, unrotated gluing"). The choice between 4−n_D, 4−2n_D and 3−n_D now decides whether SUSY content gives 0 = 0. This is a derivation from the modular flow, not a choice. It also requires resolving the non-analyticity at n=1.
3. **Tensor-block identification** (hypothesis relaxed: "δρ=0 modes of a^μ"): Φ–a mixing, and the torsion irreducible parts of ρ²X. The merged identity ρ²X = −2ρR − ρ|∇lnρ|² + (3/2)ρ²S² + total derivative already isolates the axial-torsion piece.
4. **Explicit non-constant E=0 Poisson backgrounds** (hypothesis relaxed: "constant Θ̄"), to test the lemma's domain and tip conditions directly. This needs signature input from Problem E.
5. **Other gauge functions** (hypothesis relaxed: "D·a or D·a + cE·a"): vectors proportional to K∇lnρ, anisotropic Θ̄, Vilkovisky–DeWitt terms, α≥4 with a better grid.
6. **Tip domain and edge modes for the non-minimal operator.** The effect on c_A may be α-dependent (finding 1), and the Kabat and centre shifts were not shown to be small.
7. **Tree-level (014) class, Moyal and curved backgrounds.**

Torsion-coupled scalars have no matrix origin and are rightly left unranked.

## Recommended disposition
Revise, then re-review. The core mathematics is sound, and the revisions are wording and scope only. No new physics is needed. After the three major corrections and the minor notation fixes, I expect to ACCEPT. Integration targets only `chapters/appH-microscopic-proofs.tex`, after line 179 and before `\section{Problem C…}`, with CRLF preserved. Nothing in the ledger or in Chapter 17 changes.

## Corrected snippet
Extra assumptions: none. This is arithmetic already in `gap_table.py`.

(a) Paragraph 1, replace the sentence beginning "On the replica cover with constant \(\bar\Theta\) …" up to "scale-free transverse trace." with:
```latex
On the replica cover with constant \(\bar\Theta\) the same intertwining, with the domain at \(\Sigma\) for which the longitudinal sector is the image of the regular scalar domain, gives the area coefficient \(\tfrac{3+\alpha}6\) for the connection sector in the units \(c\) of the table above, equal to the coefficient of \(\rho R[g_\rho]\). This depends on that choice of domain; other choices are not examined.
```

(b) Paragraph 1, the numerical sentence and its conclusion:
- Replace "a second-order evaluation … gives for the connection sector the eigenvalue" with "a numerical second-order evaluation … gives for the connection sector the values, matched by the rational forms".
- Add "(rational fits to \(2\times10^{-3}\), not derived; \(\alpha=\tfrac13,\dots,3\) only)".
- Replace "so \(1/G_A-1/G_T=2\LUV^2/\pi\) for every \(\alpha>0\)" with:
```latex
so \(1/G_A-1/G_T=2\LUV^2/\pi\) for the tested range \(\tfrac13\le\alpha\le3\); on backgrounds with \(E=0\) and under the conditions above the \(\alpha\)-dependence cancels in the difference for every \(\alpha>0\).
```

(c) Paragraph 2, replace from "Then \(c_A=\dots\)" through "has coefficient \(-1\)." with:
```latex
Then \(c_A=\tfrac{N_s+\alpha+1}6+\tfrac{n_D}3\) and \(c_A-c_T=4-n_D\). This gluing transports the spinor index with the replica rotation; it is not the unrotated pull-back gluing used above for \(a^\mu\). With unrotated periodic gluing of the Cartesian components the area coefficient of a Dirac field is \(-\tfrac23\), equal to its coefficient of \(\rho R[g_\rho]\), and \(c_A-c_T=4-2n_D\), which vanishes at \(n_D=2\) with \(c_T=c_A=0\): an equality of vanishing \(\LUV^2\) coefficients, not a derivation. The \(\rho^2X\) coefficient vanishes at \(n_D=2\); for antiperiodic gluing \(c_A-c_T=2\) there and equality needs \(n_D=4\), where \(\rho^2X\) has coefficient \(-1\). The gluing selected by the matrix state is not determined here.
```
and in the last sentence of paragraph 2's first block, replace "and the area coefficient does not" with "and the area coefficient is \(2\) for antiperiodic and \(0\) for periodic gluing".

(d) Notation: rename the gradient map (not `\mathcal G`) and the EOM vector (not `E_\nu`), consistently in both paragraphs.

Relevant paths:
- C:\Users\redgi\Projects\namcg-lab\proposals\017-GT-GA-gap\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\017-GT-GA-gap\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (lines 179–181 anchor; O_v at 1755)
