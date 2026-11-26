## Scan pass 1 of 5 (ordinal-60 full scan, CLAUDE.md 3(a)): appH-microscopic-proofs.tex lines 1–1100

**Nothing in lines 1–1100 blocks integrating the 062 insert.** I found no blocking, major or PRIOR-CLAIM-ERROR findings in this range.

**File and hash.** `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` is 599923 bytes with sha256 `82ab236415a5fbbea02be7ceb6eebc791e560eef4a7e589cb25be2cf9ffa279c`, which matches the expected values. It has 3313 lines.
- The only uncommitted change in this file is one hunk, +13 lines at 1609–1621 (the 061 insert), which is outside this range.
- `bib/namcg.bib` also has an uncommitted +14 lines.
- `make_digest.py --check` printed `DIGEST STALE (head changed)`. I did not rely on the digest for any content; every passage was read directly from the working tree.

**Read first.** `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\appH_insert.tex`, all 10 lines.

**Range read.** I read every line from 1 to 1100, in chunks: 1–180, 181–240, 241–285, 286–325, 326–365, 366–397, 398–437, 438–607, 608–807, 808–957 and 958–1100. The chunks over 181–437 were shorter because those lines are very long. The range covers the Problem A, B, C and D sections and the start of the "Related covariant quantum-space constructions" paragraph, which continues past line 1100. It does not reach Problem E.

**Changes since the ordinal-55 scan.** `git diff -U0 6aa4490` against the working tree shows hunks only at lines 1478 and later. So lines 1–1100 have not changed since the ordinal-55 pass 1, and the line numbers of the status lines match that scan's record.

## Findings

1. **Note (no conflict with 062 or the 053–061 Problem E blocks).** None of the following appears in 1–1100: `ass:lorentzian`, Definition (A), the regulated Lorentzian integral, contours, the mass γ, so(4,2) doubletons as a member of a family, D_±, H_n or fermion zero modes. The Lorentzian statements in the range are each scoped, and none claims the signature is derived:
   - line 355: the normal-plane "Lorentzian boost";
   - lines 368 and 400: the Lorentzian Hessian case and the boost case;
   - line 776: g_cand is "Lorentzian by construction" from η^{AB}V_AV_B, and is explicitly not identified with the emergent metric.

   This agrees with 062's closing sentence ("without deriving the signature … Assumption~\ref{ass:lorentzian} retained").

2. **Note (fermion content is consistent).** Lines 220 and 229 describe n_D=2 Dirac fields as "the sixteen real components" of the IKKT spinor. That matches 062's decomposition under so(3,1)×so(6): four copies of (½,0) and four of (0,½), that is 8 complex = 16 real components. The paragraphs at 220–235 are Euclidean-section and Poisson-limit statements, so they do not overlap 062's Lorentzian Spin(4,1) setting.

3. **Note (doubleton citation is consistent).** Lines 1090–1093 say a Lorentzian space built on "the minimal doubleton representation of so(4,2)" is described in MantaSteinacker2025, "not reproduced". That is consistent with 062's use of 𝓗_n, 𝓗_0 and Eqs. (11)–(12) of the same reference.

4. **Note (status lines are consistent; none claims closure).**
   - Line 16 (A): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
   - Lines 76–77 (B): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
   - Lines 435–438 (C): the same label, plus "it does not by itself meet the matrix-derived criterion".
   - Lines 600–603 (D): the same label, plus "Reduced-scope result: D2 … D remains OPEN and the matrix-derived criterion is unmet."

   These agree with the critical-path set A, B, C, D1, E, F, G-derived, N. The closing lines at 276, 285, 304, 311, 324, 335, 361, 372, 397, 416 and 429 ("Problem~B stays/remains open and PROGRAMME-CONDITIONAL", "Problems~B and~D remain open …") also agree.

5. **Minor (pre-existing, unchanged since ordinal 55): fixed problem lists in closing lines.** Lines 171, 210, 222, 229, 235, 250, 267, 594, 707, 749, 814, 874, 902 and 918 end with "Problems~B, C, D, F and~G remain open". This is a fixed list, which the manuscript conventions discourage. It is not false and does not imply that A, E or N are closed.

6. **Minor (pre-existing): hard-coded chapter numbers.** Lines 69, 70, 103, 526, 541 and 606 contain "Chapter~8/3/5/3/17/10".

7. **Minor (pre-existing): typography at lines 611–612.** "Proposition~" followed by a line break and then `\ref{prop:B-torsion-free}` produces a tie plus a space. It is harmless.

8. **Minor (pre-existing): first-person voice.** Lines 1090 and 1098 use "we have not checked" and "We have not reproduced". This is authorial voice, not forbidden process language.

9. **Note (symbol overlap with 060–062).** These symbols are reused in this range with different meanings. Each is defined locally inside the Problem A–D sections, so none is ambiguous. I list them for the cross-section check.
   - **X:**
     - torsion invariant X = T·T at 187, 220 and 357;
     - embedding functions X / X^a at 379 and 402;
     - dummy matrix X in K(X) at 999.

     062 uses X = σ·J_L.
   - **γ:** γ_{μν} is the pull-back of η at 402–416, while 060–062 use γ as the mass, with γ=3c in 062. The γ^μ Dirac matrices appear at 220.
   - **𝒥 and 𝔍:** 𝒥 = 𝒥_12 (normal-plane rotation) at 279–335, and 𝔍_ν (Poisson equation of motion) at 213–263. 062 uses \vec J and J_L.
   - **P:** P^{μ|λν} at 366. 062 uses P = J·K.
   - **K:** K_0 at 26, Kabat-type "K" in the prose, and K = an antisymmetric block at 925. 062 has "products with a factor K", referring to its own 060/061 meaning.

   The sans-serif 𝖪, the D_± operators and H_n do not appear in 1–1100.

10. **Note (labels and references).**
    - A grep over `chapters/*.tex` finds no duplicate `\label`s.
    - `ass:lorentzian` is defined exactly once, at `ch04-vierbein-emergence.tex:322`.
    - The range itself is unchanged, so its `\ref`s are as verified at ordinal 55.
    - 062 defines no labels; its one `\ref` is `ass:lorentzian`, which is valid.
    - Of 062's citation keys, only MantaSteinacker2025 is currently in `bib/namcg.bib`. MartinDussaud2019, MackTodorov1969, Todorov2019 and FioresiYuncken2024 are absent from the working bib, but they are supplied in `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\bib_entries.bib`, and none clashes with an existing key. They must be added when 062 is integrated, or the build will report undefined citations. This is an integration step, not a scan finding against the range.

11. **Note (no materially false or overbroad merged claims).** I spot-checked two items:
    - the complexified decomposition at 462–474, (½,½)⊗[(1,0)⊕(0,1)];
    - the g_cand components at 844, diag(a²,−a²,b²,b²) from V_0=a∂_1, V_1=−a∂_0.

    Both are correct. Numerical and sampled checks in the range are labelled as such ("not proved", "numerical").

12. **Note (no chat or process language)** ("as proposed", "the researcher" or similar) appears in the range.

**Blocking for 062: none.** Nothing in lines 1–1100 conflicts with the 062 insert or calls for a change to it. The only action item is the four bib entries from `bib_entries.bib`, which must be added with the insert.

This pass covers lines 1–1100 only. Lines 1101–3313 and the other chapter files are left for passes 2–5.
