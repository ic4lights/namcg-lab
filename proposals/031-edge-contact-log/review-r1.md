VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The central identity is exact algebra and I reproduced it. The block overreaches in scope. It never says what the cancelled coefficient is compared with, it leaves out the hypotheses on which the cancellation depends, and its last sentence confuses log-order and Λ² statements. Not a breakthrough, no label change, no PRIOR-CLAIM-ERROR.

## Source reading
**Full scan** (CLAUDE.md 3(c): the package touches the merged 029 and the 021/024 classifications; the digest is also stale and the tree is dirty).

- Manifest, all read in the working tree: ch01–ch18 and appA–appL, 30 `.tex` files; `find chapters -name '*.tex'` returns 30.
- appH was read in full. During the review the orchestrator integrated 030, a new paragraph at the end of Problem F around line 2150, and I read it too. The insertion region (lines 238–247) did not change.
- `python scripts/make_digest.py --check` printed `DIGEST STALE`.
- I ran `scripts/build_check.py` once, which was not strictly read-only. It reported PASS, 291 pages, 0 undefined references, `git diff --check` clean. `git status` is unchanged (only appH modified).
- Anchor: the sentence "Problem~B remains open and PROGRAMME-CONDITIONAL." occurs exactly once, at appH line 245. `\section{Problem C…}` is at line 247 with a blank line 246 between. The anchor is unique and correct.
- The block has 0 TAB bytes, 0 CR bytes, balanced `\(`…`\)`, and no new `\label` or `\ref`.
- A stub compile in the scratchpad succeeded. The only warnings were the three citations undefined in the stub.

## Claim under review
The claim is a conditional cancellation σ_fs + C_b + C_Ω = 0 at (N_s, n_D) = (6,2) for the fixed-state replica, once uniform E_δ = −π(1−n)δ_Σ and Ω_δ = 2π(1−n)𝒥δ_Σ from the 021 smooth family are added. It also asserts that the 029 "Euler density" statement holds only where g = 2R_Σ.

Original target: the log-order area side against the T side in Problem B (Problem A is touched only as the dictionary). Exact ledger labels, quoted:

- Problem B: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived." Chapter 17: "CRITICAL PATH; OPEN. The fixed-algebra first-law identity is established, but not the required stationarity."
- Problem A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- Problem F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."

## Checks performed
Direct re-runs (exact rational arithmetic, run in the proposal folder):

- `identity_general_jets.py 4`: four random closed ω with 𝔍≠0, non-chiral. s24+CB+τ = 0, COm−τ = 0, total = 0. The Hodge-distribution total is nonzero.
- `contacts_summary.py 1`: the 029 example (3 points), the rotation-invariant SD family, and non-SD 𝔍=0 profiles with W≠0 (−25/18 and −200/9). All TOT_U = TOT_H = 0.
- `nonsd_total.py`: total = 0 on both 𝔍=0 profiles. With the Hodge distribution it is nonzero for the 𝔍≠0 control profiles (157/2592, −11/2, 505/5832).
- `rot_family_fit.py 6`: 18 points, 0 failures. X′ = (3/2)g and τ = R_Σ + (3/4)g, and R_Σ matches the intrinsic −ρ⁻¹Δ₀ ln ρ. g/R_Σ varies (about 3.7 at the first point), so the Euler statement fails for generic members.
- `general_sd_identity.py`: the identity fails at generic SD points, but Σ is not totally geodesic there. It is therefore not evidence for the claim. The md cites it in item 3; the LaTeX does not.
- Calibration scripts: Eq. (70) is reproduced at first order by the delta rule. Maxwell gives −31/(360π)·R_Σ + W/(20π), ratios 62 and 12 to the conformal scalar, and −62/90 on S⁴/S². Dirac weights (−½, 1, ½) are forced by a, c and Weyl covariance.
- `smooth_family_deltas.py`: E_G ⊃ ½f⁻²(l11+l22)·𝟙 for the scalar, vector and Dirac fields. Ω₁₂ has entry ∓(l11+l22) in the vector (1,2) block. This gives −π(1−n)δ·𝟙 and +2π(1−n)𝒥δ. `lc_convention_check.py` confirms the conventions against Levi-Civita (tr 𝒥Ω = −R_ijij, tr_N E = −R_ii).
- `edge_heat_check.py`: the unitary equivalence residual is 0, and the torus a₁ matches −πκ²/8 to about 0.3%.
- By hand: on the 029 example b₃ = 1+x₃²−x₄² is harmonic, so g = 2R_Σ analytically. The "Euler" statement is correct there.

My own algebra:

- With the 026 relation weighted a₁ ≡ 0 (equivalently trE_f = 2e + ½trE_v), s24 + CB = −τ identically. This is an algebraic consequence, not a numerical coincidence.
- The identity tr_V(𝒥Ω^v) = τ_Ω is simply the common (12) component of the same so(4) connection in two representations, with S(𝒥) = ½γ¹².
- 029's s24 equals exactly the Fursaev–Solodukhin (FS) first-order cross term of the uniform (E_δ, Ω_δ) applied to the Dirac fields, weight −1 each: 3a₁^{D4} − τ.
- The total is then the sum of universal contacts over all sectors, proportional to the weighted a₁ and the weighted Dynkin index. Both vanish at (6,2). So the log-order cancellation is the same N_tot = 0 mechanism as c_A^sm = 0 = c_T at Λ².

Literature, read in the PDFs:

- Solodukhin 1104.3712: Eqs. (55)–(59), (70), (275), (276) and (322) match their use. Note the caveat there that the O((1−α)²) terms are ill-defined.
- Donnelly–Wall 1506.05792: Eqs. (82), (85)–(86), (97)–(98). The edge entropy is the 2D wrong-sign-scalar anomaly −R/24π, derived for the S¹×H³ sphere. 62 vs 32 gives −31/45 = −16/45 − 1/3.
- Herzog–Nishioka 1610.02261: Eqs. (7.1)–(7.2) exist as cited. Their remark is that the term is not gauge invariant and that BRST invariance is "subtle". They give no log coefficient. Their (5.20) and (2.19) I did not re-read this round (not independently verified here).
- Bib entries Solodukhin2011, DonnellyWall2016 and HerzogNishioka2016 match Crossref (journal, volume, article number, year). No new bib entries.

Not verified: a first-principles derivation of the delta content for generic backgrounds, the Dirac gluing at log order beyond the identity above, and the T-side Wald reading (not in the LaTeX).

## Findings

**1. (major) Location: the "These statements…" paragraph and the sentence "which cancels σ_log".**
- Finding: the block never states what the cancelled coefficient is compared with. It also does not say that the result is an equality of zeros.
- Reason: the T-side log coefficient is 0 on these backgrounds (weighted a₂ = ½𝒮₄ = 0 for chiral b). The completed A side is 0 by the pointwise vanishing of the weighted a₁ and the weighted Dynkin index at (6,2). This is the log-order image of "c_A^sm = 0 = c_T", which 024 and 029 already call an equality of vanishing coefficients. It carries no information on G, and it holds for any universal contact shared by all sectors. The T-side zero for non-chiral b (𝒮₄ > 0) is a Wald-type reading in the variables (G, torsion), conditional on that choice of variables (the 024 variable-dependence issue). The md says this; the LaTeX does not.
- Required action: add one sentence in the style of the corrected snippet below.

**2. (major) Location: the hypotheses paragraph and the "Contacts" paragraph.**
Five hypotheses that decide the result are missing or too weak.
- The contacts were derived only on the product family Θ¹²=1/f, Θ³⁴=1. Their universality for generic backgrounds (uniform E_δ on all bosonic components, Ω_δ ∝ 𝒥, no traceless E_δ) is assumed. With the normal-block (Hodge) distribution, the one used in the Maxwell calibration, the sum is nonzero for 𝔍≠0. It coincides with the uniform distribution only on 𝔍=0.
- The Dirac fields keep the fixed-state antiperiodic Z_n value. The identity above shows this equals Dirac periodic plus the Dirac contacts, so the combination is a hybrid: bosons in the smooth-family reading, Dirac in the fixed-state reading.
- 029 showed that the fixed-state replica is not a limit of smooth Poisson structures at first order (R_G^{(1)} = −2□δ ln ρ). 029 also says the rotated-index branches are "not continuations of Tr ρⁿ". The block's replica ("connection index transported with the replica angle") is that rotated prescription. The block does not say that it is therefore an imported (S_BH = S_ent − Q type) prescription, not the trace of the n-th power of one state.
- The omitted non-delta singular parts (b ~ ε/r, the Aharonov–Bohm-type |1−n| terms) are of the same first order as the retained deltas. At Λ² they appear as the ∓1 shift of the rotated connection sector. "Not treated" is not enough.
- The block says the 029 inputs are "Equation (70) and a=11/360"; see finding 4.
- Required action: state these in the closing paragraph. Do not say the 029 mismatch is cancelled without "for this imported prescription".

**3. (major) Location: the last sentence of the "Contacts" paragraph ("the Q contacts of the scalars and ghosts vanish at logarithmic order when R[g_ρ]=0, and with them the Λ_UV² coefficient is c_A=0=c_T").**
- Finding: it mixes two orders.
- Reason: the scalar and ghost contacts vanish at log order because e = R_G/6. At Λ² they are −(N_s−2)/4 = −1 and do not vanish. c_A = 0 needs all eight bosonic Q contacts (6+4−2 components, −2 in total). The statement rests on 021 and 024, not on a new derivation.
- Required action: rewrite it as a separate clearly attributed Λ² remark, or delete it.

**4. (minor) Location: the Dirac-weights sentence in paragraph 1.**
- Finding: "a=11/360 is an output of those weights and not a separate input" contradicts the preceding 029 paragraph ("use … a=11/360 as inputs").
- Reason: in 029, a fixes the Levi-Civita part and the Z_n weights x = −½ and z = ½ are derived. y = 1 was not independently derived there. What the check shows is that (x, y, z) = (−½, 1, ½) is forced by a, c and Weyl covariance, so c is an output given a, and x, z are confirmed.
- Required action: say "consistent with a and c" and reconcile with 029.

**5. (minor) Location: the second paragraph of the block.**
- Finding: "(the n<1 branch of the rotated connection index of the paragraph on replica prescriptions)" cites the wrong paragraph.
- Reason: the rotated-index branches (−1/3 and 5/3) are in the fermionic-content paragraph at line 191.
- Required action: fix the cross-reference.

**6. (minor) Location: paragraph 1, on Donnelly–Wall and Herzog–Nishioka.**
- Finding: three attributions go beyond the cited papers.
  - "of which −R_Σ/24π is the edge-mode density of Donnelly–Wall" extends DW's sphere result to a local density by form.
  - The w-coupled density is the author's replacement of the 2D operator by −w⁻¹div(w∇), not a result of DW Sec. VI A.
  - "A Herzog–Nishioka term removing E_δ" applies HN's (7.2) and (2.19) by form to the Poisson-structure delta, as 024 states.
- Required action: add "by the form of the term" or "obtained here by", and state that the symplectic U(1) edge interpretation and w = ρ⁻¹ are unproved.

**7. (minor) Location: the sentence "tr_V(𝒥Ω^v_12) = τ_Ω" in paragraph 3.**
- Finding: it does not say that it is the same so(4) connection b in both representations, with 𝒥 acting as ½γ¹² on spinors.
- Required action: add this.

**8. (minor) Location: the closing lines of the 029 and the new paragraph.**
- Finding: they are identical ("Problem~B remains open and PROGRAMME-CONDITIONAL.") on consecutive paragraphs.
- Required action: vary the wording or drop it.

**9. (minor) Location: the wording "holds only where g = 2R_Σ".**
- Required action: say that σ_log is a multiple of R_Σ pointwise only where g = 2R_Σ.

**10. (minor) Location: the proposal md, not the LaTeX.**
- Finding: item 8 ("Ghost: no delta") contradicts `C_b`, which includes ghosts with E_δ. Item 3 cites `general_sd_identity.py` as showing the failure, which is not valid evidence (Σ is not totally geodesic there; `rot_family_fit` is).
- Required action: fix the md.

## Scope of what is established
**Established identity (algebra):**
- At (6,2), for any closed ω, σ_fs + C_b + C_Ω = 0, exactly, given the uniform E_δ and Ω_δ = 2π(1−n)𝒥δ; it is the sum of universal contacts over all sectors. This also verifies 029's Z_n Dirac weights at log order as "periodic Dirac + FS contacts". It is a consistency result, not a derivation of G.

**Class (exact hypotheses):** Poisson limit, Euclidean section, one loop, α = 1, content (6,2), totally geodesic Σ, FS cross terms at first order in (1−n), one common proper-time limit, delta content computed only on the Θ¹²=1/f, Θ³⁴=1 family, uniform distribution assumed for all backgrounds, Dirac fixed-state gluing.

**Not established:**
- G_A = G_T (both sides are zero; no information on G).
- That the matrix state selects this replica.
- The non-delta and AB-type parts, and the n>1 branch.
- The Wald reading of the T side.
- Problems A, B and F stay OPEN and PROGRAMME-CONDITIONAL. No label change is proposed.

**BREAKTHROUGH criteria:** no. Nothing is derived from the matrix theory without new inputs, the cancellation is structurally the N_tot = 0 counting, and the imported contacts and state selection remain open.

**No-go hypotheses a within-core route could relax**, ranked most promising first (all within the scope above):
1. A content scan off (6,2). The first non-vacuous test of A-side against T-side at log order: there the weighted a₁ ≠ 0, the contact-completed coefficient is nonzero, and the T-side a₂ has curvature terms.
2. A direct log-order computation of the smooth cone replica. The exact Aharonov–Bohm/Landau heat trace for b ~ ε/r at first order, including |1−n| terms, traceless E_δ, and generic (not product-family) backgrounds. This removes the delta-only and uniformity assumptions.
3. A variable-independent Wald/Iyer–Wald entropy of the log induced action, which decides whether the T-side zero for non-chiral 𝒮₄ > 0 is real (a within-core route to relax the (G, torsion) variable choice).
4. State and replica selection via the modular flow of a quasi-free state (Problem A link), and the n>1 branch.
5. Non-totally-geodesic Σ.
6. Statistical edge content of the symplectic gauge sector, and fermion edge modes.

## Recommended disposition
Revise, then re-review (one round should suffice): findings 1–3 in the LaTeX, the minor items alongside. Integrate only the revised text.

## Corrected snippet
Replace the closing paragraph of `appH_insert.tex` (the one starting "These statements are for…"). The wording below states only what I verified above. The researcher should confirm each clause.

```latex
These statements are for the Poisson-limit operators, one loop, \(\alpha=1\), \(N_s=6\), \(n_D=2\), a totally geodesic \(\Sigma\) and cross terms at first order in \(1-n\) (the \(n<1\) branch of the rotated connection index of the paragraph on fermionic content). They assume that the delta content computed on the family \(\Theta^{12}=1/f\), \(\Theta^{34}=1\) (\(E_\delta\) uniform on every bosonic component and \(\Omega_\delta=2\pi(1-n)\mathcal J\delta_\Sigma\)) is the complete delta content for the backgrounds used; with the normal-block distribution of the Ricci-type delta, used in the Maxwell check, the sum does not vanish for \(\mathfrak J\neq0\). The Dirac fields keep the fixed-state antiperiodic gluing, which equals the periodic value plus the contacts above, so the replica is an imported prescription of the type \(S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q\) and not the trace of the \(n\)-th power of one state; the fixed-state replica is not a limit of smooth Poisson structures at first order. The non-delta singular first-order parts of the smooth family, which are of the same order and include the non-analytic dependence on \(|1-n|\) of the rotated connection index, the \(n>1\) branch and the state selected by the matrix model are not treated. The completed coefficient vanishes, as does the coefficient of the induced action of the preceding paragraph on these backgrounds (a Wald-type reading in the variables \((G,\text{torsion})\)); this is an equality of vanishing coefficients, which follows from \(N_{\mathrm{tot}}=0\) and the vanishing weighted Dynkin index and gives no value or sign of \(G_{\mathrm{eff}}\). Problem~B remains open and PROGRAMME-CONDITIONAL.
```

Extra assumptions are all stated above. Also: fix the cross-reference in paragraph 2, replace the final sentence of paragraph 3 as in finding 3, and soften the Donnelly–Wall and Herzog–Nishioka attributions as in finding 6.

Absolute paths: `C:\Users\redgi\Projects\namcg-lab\proposals\031-edge-contact-log\` (`proposal-r1.md`, `appH_insert.tex`, scripts); `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex`.
