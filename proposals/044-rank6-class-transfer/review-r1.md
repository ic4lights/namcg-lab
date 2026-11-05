VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: SME-CONSULT is not needed; no label change; no PRIOR-CLAIM-ERROR | PROGRESS: first | OPEN: 0/2

## Verdict
The factorisation lemma, the K-dependent two-derivative coefficients, the on-mode torsion identities and the replica bookkeeping hold. Two claims overreach, the brane "no single G_T" no-go and the "finite part 2W_X" of the fixed-state gap. Several scope sentences and the paragraph heading need correction. M2 does not fire.

## Source reading
Digest + targeted reads. `make_digest --check` printed DIGEST STALE (head changed, after the proposal commit). The chapters are dirty with the 043 integration, so I applied CLAUDE.md 3(d) by direct reads. This is not a full scan.

Read in full:
- appH Problem B entry and blocks, L41-399 (L41-220 read in this session). The L221-399 blocks (log coefficient, contacts, Moser and Noether blocks, 043) were not reopened; I read L306-341 in full. The 043 block sits before Problem C, around L387-399.
- appH Problem F ledger, L1362-1384.
- The merged F paragraphs, L2074-2129 (more than four coordinates, leaf dimension above four, torsion invariant, CP^{1,2} first-order response, why y^μ), and L2292-2301 (supertrace at arbitrary matrix fluctuation).
- The Steinacker2023 sentences at L234, L2092, L2103, L2162, L2172 and L2178.
- Ch17 `sec:ch17-done` (L691-755) and `sec:ch17-coeff` F text.
- MILESTONE.md and the SME scout.

Chapter 4 was not re-read. The insert uses only the `ch:vierbein-emergence` ref and the explicit non-identification disclaimer.

External sources: I fetched the arXiv PDFs of 2303.08012 and 1901.03522 and extracted text with pdftotext. I read 2303.08012 Sec. 4.1 ((4.1)-(4.13)), Sec. 6 and Sec. 7. I read 1901.03522 eqs. (2.20)-(2.22).

## Claim under review
Class: product M×K at IKKT content, K a fuzzy space. Targets:
- **Problem F** (`sec:status-F`): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." Ch17 target: A, B, C and the sign/scheme dependence of G_eff computed from the specified operators, G_eff not an input.
- **Problem B** (`sec:status-B`): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."

Status: OPEN. Priority: CRITICAL PATH for both. The package changes no label.

## Checks performed
**(a) Factorisation and index parts**
- I re-ran s1. The factorisation residuals are ≤2e-13. c22 = -(1/8)v2^M v2^K to 4e-12 and 2e-13, and the vanishing pattern of the other c_mn is reproduced.
- s1 builds the full so(10) vector (10), spinor (16) and ghost traces with non-commuting random operators. It is a genuinely independent computation.
- I re-derived the identity by hand. Both splits give Σ s0·s0 = 10-2-8 = 0. The d=4 split gives -2σ s0^K - s0^M τ - ½(σ+τ+ + σ-τ-). The d=7 split gives -σ8 s0^K - 4 s0^M τ2 - ½σ8τ2.
- "The vector never enters the mixed term" is correct. The vector generators are block diagonal, so Σ^{ab}Σ^{ij} = 0 on R^10 = R^d ⊕ R^{10-d}.
- The Dynkin relations v2^M = 2(σ2+ + σ2-) and v2^K = τ2+ + τ2- agree with the merged vector weight ρ²X and Dirac weight ½ρ²X.
- Peierls–Bogoliubov: B = -sΣ𝔽 is Hermitian and traceless in the spinor index, so τ^K ≥ 0 and W_X < 0. Strictness for nonzero flux follows from the small-s limit τ ≈ s²v2 > 0.
- Normalisations W_R and W_X, Γ = -½∫ds/s str, and "Λ² → ∫ds s⁻²", agree with the merged c-units (S = (Λ²A/8π)c, 1/G = cΛ²/2π).

**(a) δρ=0 modes**
- I re-ran s2 (2 min). V = 0, 𝒯/X = 1/4, (3/2)S²/X = 1/2 and X = 2𝒯 + (3/2)S² + 2V², at four rational backgrounds.
- This matches the merged table independently: vector 5/6 = 4(-1/24) + 1, so ρ²X has eigenvalue +1, i.e. ρ²X ≅ -4ρR, and c_T = N_tot/6 - 4κ_X.
- c_T = W_R/6 - 4W_X is therefore consistent with the merged convention. The teleparallel value r = -2 gives W_R/6 - 2W_X.
- The Lorentzian null-mode check has X = S² = 𝒯 = 0 and a nonzero axial tensor. That is a statement about the tensor only, not about any quadratic invariant (see finding 9).

**(a) Replica gaps**
- I re-derived the cone values from the merged text: Dirac index part -1/3 - 4/6 = -1 (antiperiodic), 0 (periodic), 0 (smooth in the torsion reading, since X is a torsion invariant).
- The mixed cone term is -(1/4)(-1)∫τ = -2W_X.
- Results: c_A = W_R/6 - 2W_X (fixed), W_R/6 (periodic), -W_R/12 (smooth). The three gaps in the proposal are arithmetically correct (s4).
- Gap in the fixed-state completeness: see finding 2.

**(b) Steinacker comparison**
- The reading of Sec. 6.1 is correct. (6.10)-(6.18) evaluate the K-only term V4,K with the derivative-free leading trace formula, giving the effective potential ∝ ∫ρ μ⁴ V4. No curvature term is given.
- (6.22) also drops the curvature-scale term in the mixed term. Sec. 6.3 only discusses the M-only term as a sub-leading higher-derivative contribution.
- The scaling argument that W_R is of the same order as G_N⁻¹ (~m_K²) holds: m_K⁸ × R/m⁶. This is an inference, but the quoted sentence "is not given there" is accurate.
- The mixed term is 2F^{μν}F_{μν}F^{ij}F_{ij} in (6.19). Eq. (4.13) gives R = -½T·T - ½T̃T̃ + dilaton terms, so T·T → -2R at T̃ = 0. This matches r = -2.
- In Steinacker the axial torsion T̃ is the axion, with T̃ = -2∂ϑ̃ on shell, and R + ½T̃T̃ appears in (6.32). Whether the axial half of ρ²X belongs to "G_T" or to the axion kinetic term is not decided by the proposal.
- The proposal's slogan "1/G_T = 2/G_N" is valid only under the merged definition of G_T (the whole quadratic form on the δρ=0 modes). The insert wording is acceptable once softened (finding 5).
- Numerical normalisation of Steinacker's G_N against W_X was not reproduced. Marked not independently verified.
- Steinacker's sign convention is "non-standard" (G_{μν} = -T_{μν}). The proposal's "positive" is a Euclidean statement in the merged convention. Agreement of signs with Steinacker is not verified.
- Role assignment: in 1901.03522 (2.21)-(2.22) the Yang–Mills matrices are X^a = rM^{a5} and T^a = R⁻¹M^{a4} are tangential generators. In 2303.08012 Sec. 4 and (7.6), the matrices are denoted T^a and F^{μν} = -{t^μ,t^ν}. The generators are verified. The insert's mapping of "matrices ↔ T^a, base functions ↔ y^μ" follows 2303.08012 (7.6) and is the opposite labelling to 1901.03522's matrix model. I could not resolve this. It is not independently verified; the wording must be softened (finding 6).

**(c) Brane class**
- I re-ran s3 (2m50s). The only difference from the saved output is line endings. The content is identical.
- (i) The algebra is exact. O_s = -λΔ_ĝ with ĝ = λG, λ = √|g|/ρ.
- (ii) The density equality (1/6)ρR[ĝ] is confirmed at a random jet. (This is a general operator identity, so it applies to the class.)
- (iii) rank = min(6, D-1), D = 4..11, and the Hamiltonian gauge direction is a ĝ-diffeo.
- (iv) The L⁴ coefficient is (p·p)(p·K·p)|φ|². Here K = θᵀθ is the kinetic tensor K^{μν} = θᵀgθ at the base point. It is not the fuzzy space.
- Consequence: p·K·p is exactly the tree-level kinetic symbol of φ, since □ = {x^I,{x^I,·}} = K^{μν}∂∂. See finding 1.

**(d) Merged sentences**
I checked L234, L2092, L2103, L2162, L2172 and L2178, and also L2099. All remain true.
- L2103 says the SUSY mechanism "rests on field content that is not part of the present sector list". The insert supplies that content as an input, which is compatible.
- L2297-2299 say the species sums cancel for n ≤ 3 and the quartic is nonzero. This agrees with c40 ≠ 0.
- L2300 says the case of transverse matrices with flux is not computed. The insert's claim to cover it for product backgrounds is correct.
- L337-339: the merged dressed density (Stueckelberg Λ, an input of the local-Lorentz assumption) sets S = 0 and ρ²X → 2𝒯 + 2V² ≅ -2R. This gives c_T^ext at r = -2. See finding 3.
- No PRIOR-CLAIM-ERROR.

**(f) Insert mechanics**
- 10397 bytes, 0 CR, 0 TAB, 0 non-ASCII, 0 control other than LF. Braces balanced. `\(`/`\)` 166/166. `\[`/`\]` 2/2.
- Anchor `\section{Problem G: HBEV}` occurs once, directly after the 041 Casimir paragraph.
- `sec:status-B` and `ch:vierbein-emergence` each defined once. IKKT1997, Steinacker2023 and SperlingSteinacker2019 each occur once in the bib.
- `\LUV` is defined in namcg-book7.tex. No `\label`. One `\paragraph`. The paragraph title does not collide with an existing one.
- No process language. Named internal paragraph references match existing titles.
- Build: I did not re-run compile_check. The saved output reports 0 undefined/multiply-defined references. Not independently re-verified.

## Findings
1. **Major. Insert, "Classes with six polarisations", bending no-go (claim 12).** The fourth-order term is not an obstruction.
   - (p·g⁻¹p)(p·K^{μν}p)|φ|² is the induced d'Alembertian symbol times the tree-level kinetic symbol of φ. It is removable at one-loop order by a local redefinition φ → φ + c□_gφ, and it vanishes on the tree mass shell.
   - A term of higher homogeneity does not prevent an order-p² part from carrying an Einstein form. The check's own output shows a nonzero L² coefficient (-769438919/1296), which is the order-p² II² part and was never compared with EH(ĝ).
   - "Frozen-coefficient leading symbol" mislabels the situation. The p⁴ term is the leading symbol, and EH is subleading.
   - Required: delete "no single G_T" and the bending "no-go" status. State only that the mixed term adds a fourth-order term proportional to the product of two symbols, and that the order-p² part is not compared with EH(ĝ). Rename the notation clash (K the kinetic tensor versus K the fuzzy space).
   - Consequently the package has no brane no-go. The positive sub-result stands: the scalar part is exactly ρ × EH(ĝ), with rank min(6, D-1).
2. **Major. Insert, "Area coefficient", fixed-state replica.** "plus the finite part 2W_X" is incomplete. The first term's cone contribution is 2∫ds s⁻² s0^K(s), not 2N_KΛ².
   - Since s0^K(s) = N_K - s·Tr H0^K + …, there is a logarithmic term proportional to Tr H0^K. Its finite remainder is of the same order as W_X.
   - Required: replace "finite part" by "the part from the mixed term", and say that cutoff-dependent terms from the first term (order Λ² and logarithmic) are not computed. The periodic and smooth replicas are unaffected.
3. **Moderate. Insert, same paragraph.** The "criterion" sentence omits the already-merged dressed route.
   - With the merged Stueckelberg dressing (an input of the local-Lorentz assumption, not derived), c_T^ext = W_R/6 - 2W_X on the δρ=0 modes.
   - Then the mixed-term part of the fixed-state gap is c_A - c_T^ext = (-2W_X) - (-2W_X) = 0, leaving the Λ² (and log) first-term excess.
   - Required: record this as a conditional remark that does not close D, rather than posing the vanishing gap only as a hypothetical for CP^{1,2}×K.
4. **Minor. Heading.** The title says "bounded no-go". The results are conditional bookkeeping.
   - The periodic gap 4W_X is nonzero for W_X ≠ 0. The smooth gap vanishes at W_R = 16W_X, a condition on K that is not excluded.
   - The fixed-state gap is cutoff dominated and depends on unfixed replicas (Problem A) and on the off-shell gauge-dependent quadratic form.
   - Required: use "(conditional; not closure)".
5. **Minor. Steinacker identification.** "corresponds to its part -2W_X" must be qualified.
   - Both come from the same mixed term, but normalisations were not compared.
   - In the cited construction the axial torsion is the axion, so whether its half belongs to G_T is a convention of the tensor block.
   - Required: say "corresponds structurally"; add that the cited sign convention differs and that the normalisation is not compared.
6. **Minor. CP^{1,2} sentence.** "that is T^a and y^μ here up to normalisation" asserts a role assignment.
   - It is supported by 2303.08012 (7.6) and by the NAMCG paragraph at L2101/L2125.
   - It is opposite to the matrix/base labelling of 1901.03522, where X^a = rM^{a5} are the Yang–Mills matrices.
   - Required: state that the bundle structure and the generator definitions match, and that the assignment of the two families follows Section 7 of the cited work; the correspondence of roles is not independently verified.
7. **Minor. Scope sentence.** K is not required to solve the equations of motion; pure IKKT has no fuzzy-sphere solution. Add "K is not required to be a solution; no stationarity of K is assumed" (cf. Steinacker's effective potential for K).
8. **Minor. Area section.** "G_A ≠ G_T" is generic, not forced. Phrase the periodic and smooth gaps as conditions ("vanishes only if").
9. **Minor. Null-mode statement.** Add "although its quadratic invariants vanish on a single null wave".

Other items:
- Unverified items. The finite statements on W_X < 0 are strict only for nonzero flux. The D>4 index density X_D = g^{ρλ}∂Θ^{IJ}∂Θ_{IJ} is taken as the analogue of the merged four-coordinate X and was not independently derived.
- "Set by the K scale" relies on finite Mat(H_K). The insert states this.

## Scope of what is established
**Established** (identities and exact algebra, with the hypotheses stated):
- The exact factorisation lemma.
- The order counting: (4,0), (0,4), and (2,2) with -(1/8)v2^M v2^K.
- τ^K ≥ 0, hence W_X < 0.
- The K-dependent two-derivative density for four-coordinate M.
- The on-mode identities V = 0, 𝒯 = X/4, (3/2)S² = X/2.
- O_s = -λΔ_ĝ and the density (1/6)ρR[ĝ].
- The rank min(6, D-1).

**Conditional** (not derived):
- IKKT content supplied.
- The three replica values.
- The Euclidean convention and the off-shell, gauge-dependent form.
- The Poisson limit on M with exact K.
- The orientation-even part only.
- The Steinacker identification.

**Open:**
- The sign of W_R.
- No G_eff value or sign.
- K not constructed.
- The CP^{1,2}×K computation (the Dirac index density on the six level-one amplitudes, plus whether they source axial torsion).
- The bending sector at order p².

Classification: PROGRAMME-CONDITIONAL. Nothing is DERIVED. B and F stay OPEN; no label change.

**Hypotheses of the exclusions, stated as forks**
- G_A ≠ G_T holds in this class only for the replica values taken from the ledger and the on-class (undressed) quadratic form. It is relaxed by the dressed density (finding 3) and by the Problem A replica.
- "No single G_T" for the brane is not established.

**Open avenues, ranked**
1. CP^{1,2} (finite fibre) × K: the Dirac index density on the six level-one modes, and whether they source axial torsion.
2. The Stueckelberg-dressed route (D2 input) as a conditional comparison: the mixed finite gap vanishes; compute the Λ² and log first-term excess and its dependence on the replica.
3. The first-term cone with full s0^K(s): the log structure and whether a K-dependent finite scheme fixes c_A.
4. The sign of W_R and the ratio W_R/W_X for explicit K (smooth condition W_R = 16W_X).
5. Non-product backgrounds (H1), where the vector enters the mixed term.
6. The order-p² part of the transverse sector in the brane class, and the regime p ≪ |II|.
7. The orientation-odd mixed term.

## Milestone (strict, per MILESTONE.md)
- **M1** (derives a remaining step of a critical-path problem): no. The F target is not met. The content is supplied, K is not constructed, W_R has no sign, M is the rank-3 class, and G_eff is not computed.
- **M2** (new no-go ruling out a class of routes the manuscript keeps open): no. Once finding 1 is applied the brane no-go is gone. The fixed-state, periodic and smooth gaps are conditional on unfixed replicas, and the smooth gap can vanish by a condition on K. The fuzzy-KK route, CP^{1,2}×K, the dressed route and non-product backgrounds all remain open. The result sharpens scope; it is not a closure of a route.
- **M3** (merged claim wrong): no.
- **M4**/**M5**: no.
- **BREAKTHROUGH**: no.

## Recommended disposition
Revise, then re-submit for an ACCEPT of exactly the revised text. Findings 1 and 2 are required; findings 3-9 are required wording corrections. After revision, the integrator inserts the block before `\section{Problem G: HBEV}` (CRLF). The accepted text is the insert as corrected below; the uncorrected insert is not accepted. A shorter alternative is to drop the brane bending clause entirely and keep the scalar-part rank result.

## Corrected snippets
Each "old" string occurs once in `appH_insert.tex`. No new physics is added. Extra assumptions: none beyond the merged dressed-density input (finding 3), which is marked.

1. Title: replace `(conditional; bounded no-go)` with `(conditional; not closure)`.

2. Old: `and for the fixed-state replica a cutoff-dependent term of order \(\LUV^2\) plus the finite part \(2W_X\): for \(W_X\neq0\) the periodic gap does not vanish and the smooth one vanishes only for \(W_R=16W_X\), a condition on \(K\).`
New: `and for the fixed-state replica cutoff-dependent terms from the first term (the order \(\LUV^2\) term and a logarithmic term proportional to the trace of \(H_0^K\), whose finite remainders are not computed) plus the part \(2W_X\) from the mixed term. For \(W_X\neq0\) the periodic gap does not vanish, and the smooth gap vanishes only if \(W_R=16W_X\), a condition on \(K\).`

3. Old: `The finite part \(2W_X\) of the fixed-state gap is the axial-torsion part of the Dirac index density on the tensor modes;`
New: `The part \(2W_X\) of the fixed-state gap that comes from the mixed term is the axial-torsion part of the Dirac index density on the tensor modes;`
Old: `the finite gap would vanish for tensor modes that source neither the axial nor the vector torsion at first order.`
New: `the mixed-term part of the gap would vanish for tensor modes that source neither the axial nor the vector torsion at first order. This is the case for the dressed density of the paragraph on local frame rotations (an input of Assumption~\ref{ass:local-lorentz}, not derived), which sets \(S=0\) and gives \(c_T^{\mathrm{ext}}=\tfrac16W_R-2W_X\), equal to the mixed-term part of the fixed-state \(c_A\).`
(Check that `ass:local-lorentz` is defined once before use; it is cited in the merged L337.)

4. Old: `The two forms are not proportional, so for a nonzero flux of \(K\) no single \(G_T\) covers the transverse polarisations at the frozen-coefficient leading symbol.`
New: `The fourth-order term is the product of the symbol \(p\cdot g^{-1}p\) of the induced d'Alembertian and the tree-level kinetic symbol \(p\cdot\mathsf K p\) of \(\phi\), with \(\mathsf K=\theta^{T}g\theta\) the kinetic tensor; at this order it can be moved by a local redefinition of \(\phi\) and vanishes on the tree-level mass shell. The part of second order in \(p\), which is nonzero in the same check, is not compared with the Einstein--Hilbert form of \(\hat g\), so a common \(G_T\) on the transverse polarisations is neither established nor excluded.`
Also write `\mathsf K` in place of `K` in the two earlier occurrences `(p\cdot g^{-1}p)(p\cdot Kp)` and `(p\cdot K\,p)` within that sentence, and in the closing scope sentence replace "for the transverse modes, frozen coefficients" accordingly.

5. Old: `The coefficient that~\cite{Steinacker2023} identifies with the inverse Newton constant corresponds to its part \(-2W_X\);`
New: `The coefficient that~\cite{Steinacker2023} identifies with the inverse Newton constant corresponds structurally to its part \(-2W_X\) (the same mixed term; the normalisations and the sign convention are not compared, and there the axial torsion is the axion);`

6. Old: `that is \(T^a\) and \(y^\mu\) here up to normalisation;`
New: `the bundle structure and the generator definitions agree with those of the conjugate-coordinate class here up to normalisation, the assignment of the two families to the matrices and the base functions following Section~7 of~\cite{Steinacker2023};`

7. Old: `the axial part of the torsion is also nonzero on the on-shell null mode with \(\delta\rho=0\) of the Lorentzian section.`
New: `the axial part of the torsion is also nonzero as a tensor on the on-shell null mode with \(\delta\rho=0\) of the Lorentzian section, although its quadratic invariants vanish on a single null wave.`

8. In the final scope sentence, after `the content stated,` insert `a fuzzy space \(K\) that is not required to solve the equations of motion,`.

Closing sentence stays: `Problems~B and~F remain open and PROGRAMME-CONDITIONAL.`
