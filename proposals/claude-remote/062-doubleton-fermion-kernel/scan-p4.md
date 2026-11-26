## scan-p4.md: full-scan pass 4 of 5 (ordinal-60 CLAUDE.md 3(a) scan), chapters ch01–ch09

**Read-only.** I made no edits and no git writes.

**Pre-checks**
- `git status --short`: ` M bib/namcg.bib`, ` M chapters/appH-microscopic-proofs.tex`, plus untracked `proposals/062-doubleton-fermion-kernel/scan-p1.md`, `scan-p2.md` and `scan-p3.md`.
- `git diff --stat -- chapters`: only `chapters/appH-microscopic-proofs.tex` is modified (13 insertions, which is 061). The bib diff has 14 insertions (061). This is what was expected.
- `git diff --stat f2d005f --` on the nine files gave empty output. None of ch01–ch09 has changed since the ordinal-55 scan.
- I read all of `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\appH_insert.tex` (lines 1–10).

**Files and lines read, in full and consecutively** (all under `C:\Users\redgi\Projects\namcg-lab\chapters\`)
- ch01-geometrogenesis.tex, lines 1–386 (all of it)
- ch02-preliminaries.tex, lines 1–583 (all of it; the last line has no trailing newline)
- ch03-matrix-action.tex, lines 1–916, read as 1–460 and 460–915, plus the final unterminated line 916 checked with `tail`
- ch04-vierbein-emergence.tex, lines 1–442 (all of it)
- ch05-lorentz-decomposition.tex, lines 1–419 (all of it)
- ch06-entanglement-equilibrium.tex, lines 1–458 (all of it)
- ch07-massless-tensor.tex, lines 1–476 (all of it)
- ch08-heat-kernel.tex, lines 1–411 (all of it)
- ch09-ultraviolet.tex, lines 1–392 (all of it)

Supporting greps:
- No label is defined twice anywhere in `chapters/`.
- Every `\ref`/`\eqref` in ch01–ch09 points to an existing label.
- ch01–ch09 cite only Bueno2016ECG, Cardy2013MI and DorauMuch2026.

**1. Conflicts with 062 or with the 053–061 Problem E blocks: none found**
- **ch04:313–333 (`ass:lorentzian`, L321–328).** The signature is borrowed from η_AB, and its dynamical emergence "is not proved in the source notes and is not pretended here". ch04:375 lists "The signature is dynamical" among the results not obtained. This agrees with the 062 closing sentence ("without deriving the signature … Assumption ass:lorentzian retained").
- **ch03:172–205 (`def:matrix-coords-ext`).** η_IJ contracts matrix indices only, and its Lorentzian signature "is retained as Assumption ass:lorentzian". This is the same reading as 062's use of η in the Casimirs C_5 and C_4 and in the Clifford relation for σ_±.
- **ch03:142–157 (`eq:Smatrix`).** The equation carries a generic S_matter(Ψ, X̂) and no fixed fermion content. 062 states that the fermion content "remain[s] supplied", so the two agree.
- **ch02:499–503, note.** This passage says NAMCG "as formulated in the source notes is bosonic at the microscopic level". Appendix H (L220) already adds the IKKT Dirac fields explicitly as an extra input, and 062 keeps them supplied. The wording is consistent with this, but a reader might see a tension. It does not block.
- **Wick rotation and regulated integrals.** These appear at ch02:276–278 and 289–305, ch06:192–198, ch08:80 and 151–153, and ch09:184–197. All of them concern the Presentation-B field theory or say the Lorentzian bound is "not solved here". None asserts anything about the N→∞, fixed-γ>0 fermion operator, its Pfaffian or the ε regulator, which is what 062 treats.
- Nothing in ch01–ch09 claims that Lorentzian signature is derived or emergent.

**2. Status, priority and completion statements: no contradiction with ch17 or Appendix H**
- ch01–ch09 contain no status, priority or completion labels.
- ch03:445, 596 and 786 still each end with "Problems B, C, D, F and G remain open". This is a fixed partial list, but it is not false. Note, pre-existing.

**3. Labels, references and notation**
- **The pre-existing minor items are still present:**
  - ch01:321–323 hard-codes "Chapter 16 … Chapter 17 lists what would falsify", which is inverted against the include order.
  - ch01:325–326 has two consecutive `\paragraph` headings.
  - ch05:174 and 181 each have a stray "." after `\end{equation}`.
- **ch06:68, minor (new observation, pre-existing text).** "Appendix~\ref{sec:status-A}--\ref{sec:status-B}" puts the word "Appendix" before section references.
- **ch07:462, note.** The label `sec:ch8-bridge-from-7` sits in ch07. The name is odd but not broken.
- **The 062 insert cites four keys that are not yet in `bib/namcg.bib`:** MartinDussaud2019, MackTodorov1969, Todorov2019 and FioresiYuncken2024. All four are supplied in `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\bib_entries.bib`. MantaSteinacker2025 is already present. **The integrator must add these four entries** or the build will show undefined citations. This is an integration step, not a defect in the text.
- **Notation overlaps between 062 and ch01–ch09 (note; 062 defines all of these locally, so none blocks):**
  - T^a = M^{a4}, against the gauge generators T^a (ch02:246) and the tensor mode T_{μν}.
  - ψ for the fermion, against the trace scalar ψ (ch05:95 onward).
  - σ_±, against the radial σ (ch04, ch05).
  - K for boosts and "a factor K", against the operator tensor K^{μν} (ch03:192).
  - B, against the connection B (ch05:328, ch09:312).
  - P, against P(k) (ch03:551).
  - C_4 and C_5, against C_{μνλ} (ch03:141).
  - \mathcal D_±, against D^μ.
  - The symbol clashes recorded in the ordinal-55 scan (Θ, γ, η, h, ε) are unchanged.

**4. Overbroad or materially false claims (all pre-existing and committed; no PRIOR-CLAIM-ERROR, and none bears on 062)**
- **The ordinal-55 minor items are re-confirmed as still present:**
  - ch04:330–333 ("What the book does derive…").
  - ch04:311 (Minkowski condensate said to be "part of ass:nondeg").
  - ch01:64 and 257–259, and ch06:47–48 (unqualified "theorems" and "forbids m_T²≠0").
  - ch05:347–349 ("separately established" thm:mT).
  - ch05:321–322 and 418–419, ch07:19–21, ch08:22, and ch09:325 and 381 (m_T=0 or Einstein gravity read off without "conditional on thm:mT").
  - ch02:582–583, ch03:22–23 and 915–916 ("geometry … is an output"; note).
  - ch03:838–850 (the assumption list omits ass:lorentzian; note).
  - ch02:289–290 (the Wick-rotation direction is reversed).
  - ch09:163–164 (index placement).
  - ch09:231 ("Two distinct properties", but three are listed).
  - ch02:438–440 (garbled additive-constant sentence).
- **New observations, both minor and in the same family as the items above:**
  - ch06:405–406 and 454–457 say "reads off m_T=0" and "forces m_T=0" without the conditional qualifier.
  - ch09:179 says NAMCG "claims the first list", which includes boundedness of S_matrix and existence of the saddle. ch09:184–197 itself says the Lorentzian bound is not solved. The wording overstates; "regards as the meaningful questions" would be accurate. It does not conflict with 062, which leaves the fixed-γ>0 limit and the Pfaffian undecided.

**5. Chat or process language**
- **ch02:490, minor, still present.** "Theorem 2 in the ultraviolet note".
- **Note.** "The source notes" appears throughout ch02–ch05 as an attribution, not as process language. Nothing says "the researcher" or "as proposed".

**Does anything block integrating the 062 insert?**
No. Nothing in ch01–ch09 blocks integrating the 062 insert. All findings are minor items or notes in committed text that has not changed since f2d005f, and none needs fixing as part of 062. One integration step is required: add the four bib entries from `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\bib_entries.bib` to `bib/namcg.bib` together with the insert.
