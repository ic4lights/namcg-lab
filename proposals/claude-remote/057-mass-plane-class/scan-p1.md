## Scan pass 1 of 5 (ordinal-55 full scan, CLAUDE.md 3(a)): appH-microscopic-proofs.tex lines 1–1100

**Nothing in lines 1–1100 blocks integrating the 057 insert.** I found no blocking, major or prior-claim-error findings in this range.

**File and hash.** `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` is 561466 bytes with sha256 `ea5c753b0f01a3a92e426435f747fa464521980f609ab330f4a432868daba1f5`, which matches the expected values. It has 3255 lines. `git diff --stat` shows +35 uncommitted lines in this file only.

**Digest.** `make_digest.py --check` printed `DIGEST STALE (head changed)`. The digest head is 154023c and the current HEAD is a86bfca. The only commit since then is a proposals-only review commit, and no `chapters/` commit is newer. I used the digest only to locate status lines and read the passages directly from the working tree, so this does not affect the scan.

**Range read.** I read every line from 1 to 1100, in chunks: 1–180, 181–240, 241–285, 286–325, 326–365, 366–397, 398–437, 438–607, 608–807, 808–957 and 958–1100. Chunks over lines 181–437 were shorter because those lines are very long; that stretch is about 125 KB. The range covers Sections A, B, C and D and the start of the "Related covariant quantum-space constructions" paragraph. It does not reach Problem E.

**Also read first.** The digest, and `C:\Users\redgi\Projects\namcg-lab\proposals\057-mass-plane-class\appH_insert.tex` in full.

## Findings

1. **Note: no conflict with 057 or the 054–056 Problem E blocks.** None of `ass:lorentzian`, Wick rotation, Definition (A), the mass term γ, `\mathfrak C`, `M_\gamma`, `F_{\mathrm E}` or `\mathcal R_u` appears in lines 1–1100. The Lorentzian statements in the range are each tied to a stated scope, and none says the signature is derived or that `ass:lorentzian` is discharged:
   - line 776: the candidate metric is "Lorentzian by construction" from `η^{AB}V_AV_B`, and is explicitly not identified with the emergent metric;
   - line 355: Lorentzian boost;
   - lines 368 and 400: the Lorentzian Hessian and boost cases.

   This agrees with 057's closing statement that the classes "select no signature" and that the mass "does not discharge Assumption~\ref{ass:lorentzian}". Separately, I confirmed that `ass:lorentzian` is defined exactly once, at `ch04-vierbein-emergence.tex:322`.

2. **Note: status lines are consistent.**
   - Line 16 (A): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
   - Lines 76–77 (B): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
   - Lines 435–438 (C): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." It adds that a scalar-tensor result is a reduced-scope outcome that "does not by itself meet the matrix-derived criterion".
   - Lines 600–603 (D): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2 … D remains OPEN and the matrix-derived criterion is unmet."

   All four agree with the critical-path set A, B, C, D1, E, F, G-derived, N and with ch17 as the digest summarises it (L123, L140, L330, L344, L378, L395). None claims closure.

3. **Minor (pre-existing): fixed problem lists in closing lines.** Lines 171, 210, 222, 229, 235, 250, 267, 594, 707, 749, 814, 874, 902 and 918 close with "Problems B, C, D, F and G remain open". This is a fixed list, which the manuscript conventions discourage. It is not false, since it does not imply that A, E or N are closed, and it does not conflict with 057.

4. **Minor (pre-existing): hard-coded chapter numbers.** Lines 69, 70, 103, 526, 541 and 606 contain "Chapter~8", "Chapter~3", "Chapter~5", "Chapter~3", "(Chapter~17)" and "Chapter~10". Outside this range, lines 2761 and 2851 do the same. This breaks the `\ref` convention but is not material to 057.

5. **Minor (pre-existing): typography at lines 611–612.** `Proposition~` followed by a line break and then `\ref{prop:B-torsion-free}` produces a tie plus a space. It is harmless.

6. **Minor (pre-existing): first-person voice.** Line 1090 has "we have not checked these conditions" and line 1098 has "We have not reproduced any of these results". This is authorial voice rather than the process language that is forbidden, so I flag it as minor only.

7. **Note: symbol overlap with 055–057 local symbols.**
   - Lines 253–335 use `\mathfrak J` and `\mathcal J` (= `\mathcal J_{12}`, the generator of the normal-plane rotation). 057 itself does not use `\mathcal J`, and the 055/056 meaning is local to Section E.
   - Θ is used throughout as the Poisson bivector, while 057 uses Θ(E) as an angle.

   Neither overlap is ambiguous, because each is defined locally in a different Problem section. I flag them only for the final cross-section check.

8. **Note: labels and references are clean in this range.** I checked all `chapters/*.tex` and found no duplicate `\label`s. The range defines `app:status` and `sec:status-A`, `-B`, `-C` and `-D`. Every `\ref` and `\eqref` in lines 1–1100 resolves to a `\label` in `chapters/`. The 057 insert defines no labels; its only `\ref` is `ass:lorentzian`, which is valid.

9. **Note: no materially false or overbroad merged claims.** I found no merged claim in lines 1–1100 that would warrant PRIOR-CLAIM-ERROR. Numerical and sampled checks are labelled as such ("not proved", "numerical"), and each Problem B paragraph ends with a scoped "not closure" sentence.

10. **Note: no chat or process language** ("as proposed", "the researcher" or similar) appears in the range.

This pass covers lines 1–1100 only. Lines 1101–3255 are left for passes 2–5, together with the other chapter files the full scan requires.
