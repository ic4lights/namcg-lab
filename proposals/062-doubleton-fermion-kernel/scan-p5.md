Pass 5 of 5 for the ordinal-60 full scan (CLAUDE.md 3(a)). It covers ch10–ch18 and appendices A–G and I–L. Nothing blocks integrating the 062 insert.

**Pre-checks**
- `git status --short` shows:
  - ` M bib/namcg.bib`
  - ` M chapters/appH-microscopic-proofs.tex`
  - `?? proposals/062-doubleton-fermion-kernel/scan-p1.md` through `scan-p4.md`
- `git diff --stat f2d005f -- chapters`:

  | File | Lines changed |
  |---|---|
  | appE | +17/− |
  | appH | +93 |
  | appI | +18/− |
  | ch13 | +18/− |
  | ch16 | +11/− |

  None of the other 15 files in this pass changed since the ordinal-55 scan.
- `make_digest.py --check` prints `DIGEST STALE (head changed)`. The only HEAD change is the review-r2 commit, which touches no chapter file. Every file below was read directly, so the digest was used only for its manifest: 30 files, appA–appL (12) and ch01–ch18 (18).
- I read `proposals/062-doubleton-fermion-kernel/appH_insert.tex` in full (one paragraph block). Its 062 heading ("fermion form of the doubleton member") is not yet in appH, so it cannot be inserted twice. Its only `\ref` is `ass:lorentzian`, which is defined once, at ch04:322. Its five `\cite` keys:
  - `MantaSteinacker2025` is already in `bib/namcg.bib`.
  - `MartinDussaud2019`, `FioresiYuncken2024`, `MackTodorov1969` and `Todorov2019` are **not** in `bib/namcg.bib`. They are staged in `proposals/062-doubleton-fermion-kernel/bib_entries.bib`, and integration must add them.

**Files and lines read (in full, consecutive ranges)**
- ch10 1–451, ch11 1–432, ch12 1–400, ch13 1–410, ch14 1–398, ch15 1–331, ch16 1–363, ch18 1–93.
- ch17 1–790 with the Read tool. I saw the final line 791 ("belong in the book.") only through a byte-level tail.
- appA 1–266, appB 1–214, appC 1–220, appD 1–122, appE 1–316, appF 1–94, appG 1–68, appI 1–88, appJ 1–124, appK 1–92, appL 1–62.
- appH: only the grep of the 11 ledger status lines (16, 76, 435, 600, 1486, 1629, 2814, 2835, 2922, 3053, 3178). Passes 1–3 covered appH in full.
- Label and ref check over all 30 files, by script: 596 labels, no duplicates; 256 distinct refs, none undefined.

**Findings**

1. *Conflicts with 062 or the 053–061 Problem E blocks; any claim that the signature is derived.* None found.
   - ch10:372–373 and ch16:305–307 deny that the signature is derived.
   - ch17:394–399 retains Assumption~\ref{ass:lorentzian}. This matches 062's closing sentence ("Problem~E stays open with Assumption~\ref{ass:lorentzian} retained").
   - appA:34–36 ("made positive by a Wick rotation") and appA:162–171 are continuation conventions, not derivation claims. Note only.
   - Notation (note only): 062 uses local symbols A=C₅−C₄, B=1+C₄−(A+1)², P=J·K, X, K and c. These could be confused with Problems A and B, the diagonal Lorentz connection B (ch10:158, ch17:337), the ECG density 𝒫, and the Holst/PPN/EFE γ. All are defined locally, so there is no logical clash.

2. *Status, priority and completion consistency.*
   - ch17:700–732 lists A, B, C, D1, E, F, G-derived and N as critical path. ch17:685, ch17:744–747 and ch18:86–88 make H, I and J optional. ch16:131–133 agrees.
   - Problem E: ch17:395 reads "OPEN; CRITICAL PATH for the matrix-derived label", which matches appH:1486. The A, B, C, D, F, I, J and N lines also agree with appH.
   - ch17:475 (note, persists): Problem G reads "CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN", while appH:2814 reads "Status: OPEN. Priority: CRITICAL PATH." The qualifiers differ; both leave G open. Reported only; no label change proposed.
   - ch17:521 (note, persists): Problem H reads "OPTIONAL research within the theory", while appH:2835 reads "OPTIONAL within the phenomenological scope". The wording differs only.
   - ch18:32–53 (minor, persists): the "not obtained" list omits Problems E and N, although ch18:72–78 lists both.
   - appJ:62–111 (minor, new): the "not obtained" list omits Problems A and N.

3. *Labels, references, broken refs.*
   - No duplicate labels and no undefined refs.
   - appE:290 (minor, persists): the hard-coded "Assumption~E.1" can be misread as Problem E.

4. *Merged claims that are false or overbroad.*

   *058 corrections: verified, internally consistent, no stale text.*
   - I recomputed the values with g_gal=2.2e-10 and g†=1.2e-10:

     | Quantity | Value | Where it appears |
     |---|---|---|
     | ν(g_gal) | 1.348 | ch13:255, ch16:208, appE:48, appE:225 |
     | L_e | −0.236 | |
     | ν(1+L_e) | 1.030 | |
     | ν(1+L_e/2) | 1.189 | |
     | inverted g_ext | ≈1.5e-10, with ν≈1.49 | appE:51–53 |
     | ν(1e-11) | 3.99 | |
     | √1.35−1, √1.5−1 | 0.16, 0.22 | appI:28 |

     All match the text.
   - eq:nu-efe (ch13:229–233) now has [ν(g_tot)−ν(g_ext)]g_ext. Linearised, it gives ν_e transverse and ν_e(1+L_e) along g_ext, as ch13:258–261 states.
   - I re-derived the 3D QUMOND point-mass solution: Φ=−GMν_e[1+L_e sin²θ/2]/r. This gives ν_e along g_ext and ν_e(1+L_e/2) transverse, matching ch13:262–264.
   - A grep finds no remaining "≈1.1" and no "not explained" in these files. ch16:212–214 and appE:226–229 now say "comparable … coefficient-level agreement, not a derivation".
   - The prior major finding and the eq:nu-efe sign finding are resolved.

   *058 residue (minor).*
   - eq:efe-sat (ch13:241–245) and the quotes at ch16:207–208, appE:222–225 and appI:27–30 give γ→ν(g_ext)≈1.35 without a direction qualifier. ch13:256–264 then says the algebraic form gives about 1.03 along g_ext.
   - appE:260 ("the QUMOND external-field limit") and appI:26 ("or the equivalent AQUAL/QUMOND … prescription") overstate the match. ch13:262–264 says 3D QUMOND has the opposite anisotropy.

   *New finding, major (PRIOR-CLAIM-ERROR candidate; optional Problem I, not critical path).*
   - ch14:243–253: for a circular orbit with v²=GM/d and Ω²=GM/d³, P_ent=ημGM/d⁵ and P_GW∝G⁴μ²M³/d⁵. The ratio is therefore independent of d (k=0). The claim of "a positive power of d that makes the ratio grow toward wide separations" is false. Exercise ch14:366–368, which asks for the separation at which the two powers are comparable, inherits the error.

   *New findings, minor.*
   - appF:94, appJ:118 and ch18:6 say "divergenceless entanglement stress". ch11:137 (Theorem~\ref{thm:conservation}) says separate conservation of any one summand is not implied; only the total is conserved.
   - appB:186–189: "Those are Problem~B … and the physical input of Chapter~6, respectively" pairs three items with two referents.
   - appD:14: "McGaugh, Lelli & Schombert (2016)" is plain text, not `\cite`.

   *Persisting from ordinal 55.*
   - ch12:342 (minor): "f→1−Λ_eff r²/3 as r→0" omits −2Mr²/r₀³. ch13:106–113 has it correctly.
   - ch12:224 and ch12:398–400 (minor): "does not scale as Λ_UV²" and "the derivation just completed" overstate. The remark at ch12:243–265 marks the result as dimensionally incomplete. The "consistent regulation" wording at appJ:50–53 and ch18:22–23 has the same tension.
   - appJ:55 (minor): "Λ_eff=3/L_IR²" uses L_IR, which is undefined and appears nowhere else in chapters/.
   - appJ:80–81 (minor): "ψ is not identical to the radial Higgs" is in tension with ch17:208–209, where they are the same field in Repair II unitary gauge.
   - appC:103 (minor): "U_N=−Geff-less toy potential" is garbled.

5. *Chat and process language.*
   - Persists (minor):
     - ch11:216 "source notes";
     - ch13:123 "working profile of the notes";
     - ch15:43 "source-note values";
     - ch15:157 "corrected notebook dmcg5.py";
     - ch15:188 "PNG from the notes".
   - No reviewer or proposal process language. The ch17:765–769 exercises use "proposal" legitimately.
   - appI:46–48 (minor, persists): citations are plain text, and "quality-framework study 2026" cannot be identified. Not independently verified.
   - Hard-coded numbers (minor, persist): ch16:215 "Theorems~7.3--12.4", ch16:268 "Appendix~D", ch16:276 "Theorem~7.3", appE:225 "Theorem~7.3", appJ:103–104 "Chapter~3" (wrong; the assumption is at ch04:322), ch17:782–788 "Appendix~A…D", and many "Chapter~N" in ch10–ch18.
   - ch17:789 (note, persists): "None of the appendices introduces a new physical hypothesis" is in tension with appE's `ass:sqrt-mod`.
   - ch11:396 and ch14:317 (note): γ is reused as a drag constant.

6. *Ordinal-55 pass-5 items, re-confirmed.*
   - Resolved by 058:
     - ch13:255 "1.1";
     - ch16:208 "1.1";
     - appE:48 and appE:221 "1.1";
     - the "not explained" sentences at ch16:212–213 and appE:220–222;
     - the appI:27 inconsistency;
     - the eq:nu-efe sign.
   - Still present:
     - ch12:342;
     - ch12:224 and ch12:398–400;
     - appJ:55, appJ:80–81, appJ:102–104;
     - appC:103;
     - appE:290 (formerly 283);
     - ch18 omitting E and N;
     - the process wording in ch11, ch13 and ch15;
     - the appI plain-text citations;
     - the hard-coded numbers;
     - the ch17:789 note;
     - the G and H qualifier notes.

**Blocking status.** Nothing in this pass blocks integrating 062. No passage conflicts with it or with the 053–061 Problem E blocks, and none claims a derived Lorentzian signature. One integration prerequisite, not a scan finding: the four missing bib keys (`MartinDussaud2019`, `FioresiYuncken2024`, `MackTodorov1969`, `Todorov2019`) must be added from `proposals/062-doubleton-fermion-kernel/bib_entries.bib`, or the build will report undefined citations. The new major item (ch14:243–253) concerns optional Problem I phenomenology. I report it for the loop as a PRIOR-CLAIM-ERROR candidate; it is not a condition on 062.

**Coverage.** By the manifest in scratch/digest.md (30 files: appA–appL and ch01–ch18), passes 1–3 (appH), pass 4 (ch01–ch09) and this pass (the remaining 20 files) together have read every file in the current chapters manifest.

Relevant paths:
- C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\bib_entries.bib
- C:\Users\redgi\Projects\namcg-lab\chapters\ch14-dissipation.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\ch13-cores-galaxies.tex
