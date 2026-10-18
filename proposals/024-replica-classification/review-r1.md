VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/1

## Verdict
The classification, the counterterm bookkeeping, the s-wave branches and the algebra all check out. One logical step in the Lewkowycz–Maldacena (LM) paragraph is overstated: the smooth family is called "the regularised cone", but its far field differs from LM's. That wording must be fixed before integration, with one minor wording change on Kabat.

## Source reading
Digest + targeted reads. The digest is STALE (dirty-chapters, expected). CLAUDE.md 3(c) is not triggered. The block changes no definition, assumption, scope or status passage, and it makes no merged sentence false.
- I read appH Problem B in full (lines 41–205: the ledger label, the 015/017/019/021 blocks, and the 021 "Outcome" paragraph). I also read the full proposal, `appH_insert.tex`, `bib_entries.bib` and the scout report.
- I read no other chapters. Ordinal 22 is not a multiple of 5, so 3(a) does not apply either.
- No PRIOR-CLAIM-ERROR. The 021 sentence "c_A^sm = 0 = c_T … not a derivation" is consistent with the block. 021's "values 2 and 0 … intermediate fluxes not computed" is consistent with it.

## Claim under review
The package classifies c_A = 2, 1, 0 at (n_D, N_s) = (2, 6) against published contact-term treatments. It also states what an LM argument implies for G_A versus G_T. All of it is conditional and bounded.

Problem B, quoted verbatim from Appendix H: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived." Problem A is touched only as a state/replica datum. I did not re-quote its ledger label in this round. No label change is proposed.

## Checks performed
Directly verified:
- **Herzog–Nishioka (H–N) 1610.02261 v3.**
  - I downloaded and opened the paper.
  - Eq. (2.19) is I_E = −2πξ(1−n)∫φ², "cancels the contribution from the tip to the Ricci scalar", and is equivalent to the Friedrichs extension.
  - Eq. (7.2) is I = −π(1−n)∫δ^{ij}A_iA_j. The text says it is not gauge invariant, and that Feynman gauge is already broken. It cites Kabat [30] and Donnelly–Wall [65].
  - The word "Wald" does not occur in the text (grep).
  - Eq. (5.20) and the sentence after it state that the boundary term "contributes oppositely to the contact term in the Adler–Zee formula … may be restated as removing the contact term". This independently supports the proposal's bookkeeping, so the block's "related only through this bookkeeping" is conservative.
- **Counterterm derivation.** I re-derived it by hand.
  - The cone delta gives a heat-trace term −(1−n)ξA/(4πs).
  - That gives S = −ξAΛ²/(8π) = −2πξA⟨φ²⟩ with ⟨φ²⟩ = Λ²/(16π²).
  - The H–N term enters ln Z_n as +2π(1−n)ξ∫⟨φ²⟩, so (1−n∂_n) gives +2πξA⟨φ²⟩.
  - The sum is zero, and the script agrees.
  - The contact is Donnelly–Wall (DW) Eq. (4), S_contact = −2πξ∫⟨φ²⟩. DW calls it a quantum expectation value of Wald's formula, assigns it to the generalised entropy for scalars, and gives the Maxwell contact an edge-mode reading, not a Wald one.
- **Solodukhin 1104.3712.**
  - Eqs. (143)–(144) give the factor (1/6 − ξ) from the delta-potential.
  - The text after (144) refuses to read this as an entanglement entropy.
  - Eq. (322) is S_BH = S_ent − Q, with Q = 2π Σξ⟨φ²⟩.
  - Replacing ξ by Q = 1/4 gives −1/12 per component, as the block states.
  - The numerical identity c_A − c_A^sm = (N_s+2)/4 = Q matches the structure of (322).
- **s-wave Bessel index.**
  - On f = ln ρ = a ln u with a = (n−1)/n, in the metric du² + n²u²dθ²: Box f = 0 away from the tip, |∇f|² = a²/u², and E_s = a²/(4u²).
  - This gives ν_k = √(k² + ((n−1)/2)²)/n, so ν_0 = |n−1|/(2n) ✓.
  - The tip flux is 2π(n−1), so −½Box f = π(1−n)δ, matching 021.
- **Branches.**
  - The regular-branch constant is −ν/2 (script, 7 digits). The k ≠ 0 first-order part reproduces 1/(12n).
  - With C = 1/(12n) − |n−1|/(4n), (1−n∂_n)[C − n/12] at n = 1 is 1/6 + 1/4 = 5/12 for n > 1 and 1/6 − 1/4 = −1/12 for n < 1.
  - The branches are non-analytic at n = 1, and −1/12 is the n < 1 regular-branch value ✓.
  - The less-singular branch (+ν/2) swaps them ✓.
  - The k ≠ 0 O(λ²) sum is logarithmic and drops at first order ✓.
  - The statement "the delta multiplies a function that vanishes at Σ" is an adequately scoped domain statement, in the manner of H–N after their (2.15). It is not a full self-adjoint-extension analysis, and the block does not claim one.
- **Contents algebra.**
  - c_T = (N_s − 22 + 8n_D)/6 and c_R = (N_s + 2 − 4n_D)/6.
  - c_A^sm − c_T = (14 − N_s − 4n_D)/4 ✓.
  - The lines N_s = 4n_D − 2 and N_s = 22 − 8n_D meet only at (6, 2) ✓.
  - c_A^sm = −c_R/2 ✓. The Dirac entry is consistent: it gives +1/3 per Dirac field.
  - I re-ran all three scripts and the outputs match.
- **Bib.**
  - Crossref confirms HerzogNishioka2016: JHEP 2016(12) 138, title and authors correct.
  - Crossref confirms LewkowyczMaldacena2013: JHEP 2013(8) 90 (the entry's "090" is fine).
  - Neither key, arXiv ID nor DOI is present in `bib/namcg.bib` or the chapters (grep), so there are no duplicates.
  - The cited keys Solodukhin2011, Kabat1995 and DonnellyWall2016 exist.
  - BibTeX record: VERIFIED (HerzogNishioka2016). BibTeX record: VERIFIED (LewkowyczMaldacena2013).
- **Anchor.** The sentence "or the next order of either side, and give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open." occurs exactly once (line 204). It ends the 021 block and is followed by `\section{Problem C…}` (line 206). The 023 block sits before Problem G and is far from the anchor. `\LUV` exists (namcg-book7.tex:54). The block has no `\ref`. Spacetime stays emergent: only Θ-built G and ρ are used, and no metric is made fundamental.

Not independently verified: the body of Kabat, Frenkel, and Jing–Niu–Xian (not cited in the block). The teleparallel reading is the researcher's own and is presented as algebra only.

## Adjudication of G_A = G_T "by construction" (the scout's inference)
The researcher is right within the class, and the scout's inference is not supported.
- In the smooth family, c_A^sm = −c_R/2 is the coefficient of √G R_G at fixed torsion. S = A/4G_ind in those variables is then a definition of G_ind, not a test of G_A = G_T.
- G_T is read from the integrated quadratic form on the δρ = 0 modes. That form also receives the torsion and X terms, because the induced action is not a functional of G alone. The difference (14 − N_s − 4n_D)/4 is arithmetic, and it vanishes only on N_s + 4n_D = 14.
- "G_A = G_T by construction" would need a covariant functional of the metric alone, plus the LM stationarity condition. The latter is the open step of Problem B. At (6, 2) the 0 = 0 is the vanishing of the Λ² term.
- Both the fixed-state replica (c_A − c_T = 2) and the smooth replica (0 = 0) give no information on G at IKKT.

## Findings
1. **MAJOR. "Dynamical metric" paragraph, sentence "…so the regularised cone is the first-order smooth family and the area coefficient is c_A^sm = −c_R/2".**
   - **Finding.** LM's off-shell regularised cone agrees with the cone at infinity, and LM stress that both configurations obey the same boundary conditions, so there are no boundary terms. They cancel the first bracket by the equations of motion on that basis.
   - **Reason.** In the Θ-only class, R_G^(1) = −2Box δlnρ shows no such configuration exists at first order. The smooth family has a different far field (ρ ∝ r^{n−1}, with flux), so it is not LM's regularisation. The first-bracket cancellation is not shown for it.
   - **Required action.** Say that LM's construction is not available as stated. Say that the smooth family is the only first-order regularisation in the class, with a different asymptotic ρ. Say that the area coefficient −c_R/2 is therefore that of this replica, and that the vanishing of the LM first bracket is not established for it. The conclusion c_A^sm − c_T ≠ 0 is unaffected.
2. **MINOR. Connection-sector paragraph, "absent from the entanglement entropy~\cite{Kabat1995}".** DW treat the contact as the entanglement of edge modes, which sits in the extended-Hilbert-space entropy. Say "absent from the bulk-mode entanglement entropy". Optionally cite H–N Eq. (5.20) for the "oppositely to the contact term" statement.
3. **MINOR. Last sentence of the "Dynamical metric" paragraph.** It uses Q of Solodukhin's (322), which is defined for ξ-coupled scalars. Add "in form" and state that Q here is the bosonic contact (N_s+2)/4 of the smooth reading.
4. **No finding on the affine law or the holonomy template.**
   - The affine law is explicitly an assumption (superposition of local densities).
   - The imaginary twist, ν_k = |k + iλ|/n, correctly blocks the real-holonomy (Bernoulli) template.
   - No first-order family joins the endpoints: smooth first-order flux fixes the deficit, and the fixed-state cone is not a first-order smooth structure.
   - The "c_A = 1" vector contact is correctly labelled an input.

## Scope of what is established
- **Established (algebra and bookkeeping, inside the 021 class: Poisson limit, Euclidean section, α = 1, Λ² term, one loop, two replicas).**
  - The contact and the H–N counterterm are equal and opposite.
  - The s-wave branch values are 1/6 ∓ 1/4 on the regular branch.
  - c_A^sm = −c_R/2.
  - c_A^sm − c_T = (14 − N_s − 4n_D)/4.
  - The two vanishing lines meet only at (6, 2).
- **Classification only (by the form of the coefficient, an analogy).** The values 2, 0 and 1 correspond to the contact-free, delta-potential and imported vector-contact cases. The H–N and Solodukhin analyses are scalar, flat-background and explicit-ξ. Neither value is asserted to be the matrix state's entanglement entropy.
- **Not established.** The replica or state selected by the matrix model, stationarity, covariance of the induced action in Θ, the vector contact, edge modes, tip domains, and the next order.
- **Classification.** PROGRAMME-CONDITIONAL. B and A stay OPEN. No label change.
- **Open avenues, ranked.**
  1. Next order (Λ⁰, log) on a curved J = 0 leaf at the SUSY content, where the Λ² term vanishes.
  2. A covariant completion of the induced action, identifying the torsion invariants behind c_A^sm ≠ c_T.
  3. Stationarity at the SUSY point.
  4. Tip domains and symplectic/fermion edge modes (the Frenkel–Hartnoll 1/e² structure).
  5. A state-dependent frame κ (Frenkel).
  6. Non-quasi-free or non-rotational states.
  7. Contents on N_s + 4n_D = 14 (a non-vacuity check).

## Recommended disposition
Revise per findings 1–3, then integrate. No full scan is required. The integrator should still run `build_check.py` and preserve CRLF.

## Corrected snippet (finding 1; no new physics)
Replace the sentence beginning "With \(\Theta\) the only field…" through "\(c_A^{\mathrm{sm}}=-c_R/2\)." with:

With \(\Theta\) the only field, \(R_G^{(1)}=-2\Box_{\bar G}\,\delta\ln\rho\) excludes such a configuration at first order, as stated above. The only first-order regularisation in this class is the smooth family, whose far field has \(\rho\propto r^{n-1}\) and so differs from that of the cone; the construction of~\cite{LewkowyczMaldacena2013}, and the vanishing of its first bracket, are therefore not reproduced for it. For the smooth replica the area coefficient is \(c_A^{\mathrm{sm}}=-c_R/2\).

The sentence after it, "This is the coefficient of \(\sqrt G\,R_G\)…", stays unchanged.
