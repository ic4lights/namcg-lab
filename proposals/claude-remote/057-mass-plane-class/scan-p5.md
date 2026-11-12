Pass 5 of 5 for the ordinal-55 full scan (CLAUDE.md 3(a)): ch10–ch18 and appendices A–G and I–L. Nothing blocks integrating the 057 insert.

**Pre-checks**
- `git status --short` shows ` M chapters/appH-microscopic-proofs.tex` and `?? proposals/057-mass-plane-class/scan-p1.md` through `scan-p4.md`.
- `git diff --stat -- chapters` shows only appH changed (35 insertions). These lines are the uncommitted 055/056 blocks ("Linear contours that mix the indices…" and "The regulator fixes the class…"). The 057 text is not yet in appH (a grep for its heading finds nothing), so there is no risk of inserting it twice.
- I read `proposals/057-mass-plane-class/appH_insert.tex` (lines 1–11) in full. Its only cross-reference is `ass:lorentzian`, which is defined once, at ch04:322.

**Files and lines read (in full, consecutive)**
- ch10 1–450, ch11 1–431, ch12 1–399, ch13 1–399, ch14 1–397, ch15 1–330, ch16 1–361.
- ch17 1–790 with the Read tool. Line 791 ("belong in the book.") I saw only through a byte-level tail of the file.
- ch18 1–92.
- appA 1–265, appB 1–213, appC 1–219, appD 1–121, appE 1–308, appF 1–93, appG 1–67, appI 1–83, appJ 1–123, appK 1–91, appL 1–61.
- appH: only the 11 ledger status lines and their context, for the ch17 comparison. Passes 1–3 covered appH in full.

**Findings**

1. *Signature, Wick rotation and Euclidean/Lorentzian conventions versus the 057 insert and the 053–056 blocks.* No conflict found. No passage claims Lorentzian signature is derived.
   - ch10:372–373 and ch16:305–306 explicitly deny it.
   - ch17:394–399 says Euclidean positivity and a formal Wick rotation do not select the signature, which matches 057's closing sentence.
   - appA:162–171 uses S_E=−iS_L under t=−iτ. This is consistent with 057's weight condition Re iS_b≤0.
   - appA:34–36 ("made positive by a Wick rotation") is a formal convention, not a derivation claim. Note only.
   - The real-time Kubo reading at ch14:113–151 is conditional and does not touch 057.

2. *Status, priority and completion consistency.*
   - Chapter 17 lists A, B, C, D1, E, F, G-derived and N as critical path (ch17:700–732). H, I and J are optional (ch17:685, ch17:744–747, ch18:86–88). ch16:131–133 matches.
   - ch17's status lines for A, B, C, D, E, F, I and N agree with Appendix H. For Problem E, ch17:395 reads "OPEN; CRITICAL PATH for the matrix-derived label", matching appH:1486.
   - ch17:475 (note): Problem G reads "CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN", while appH:2756 reads "Status: OPEN. Priority: CRITICAL PATH." The qualifier differs; both leave G open. Reported only; no label change proposed.
   - ch17:521 (note): Problem H reads "OPTIONAL research within the theory", while appH:2777 reads "OPTIONAL within the phenomenological scope". Wording differs only.
   - ch18:32–53 (minor): the "not obtained" list leaves out Problems E and N, although ch18:72–78 lists both as next steps.

3. *Labels, references and notation.*
   - Across all 30 chapter files there are no duplicate labels and no undefined `ref{...}` targets (253 distinct references checked by grep).
   - Notation (note only): 057 symbols are defined locally and do not clash with labels. Symbols a reader could confuse with existing uses:
     - E (a real 2-plane in 057) versus the heat-kernel endomorphism E (appA, ch17:450, appG, appK) and Problem E;
     - γ (mass) versus PPN γ (ch17:309, appJ:79, appK:58), the Holst γ (ch10:244), the EFE γ (ch13:241, ch16:206, appE:42) and appL's γ;
     - σ₁, σ₂ versus the radial mode σ;
     - P versus the ECG density 𝒫;
     - κ versus κ_IR;
     - v versus the condensate vev v.
   - appE:283 (minor): the hard-coded "Assumption~E.1" can be misread as Problem E.

4. *Merged claims that are false or overbroad (PRIOR-CLAIM-ERROR candidates; none touches Problem E or 057).*
   - ch13:255, ch16:208, appE:48 and appE:221 (major): "ν_√(g_gal)≈1.1" is numerically false under eq:nu-sqrt. At g_gal=2.2e-10 and g†=1.2e-10, ν = 1/(1−exp(−√1.833)) ≈ 1.35; I computed this. As a result, ch16:212–213 and appE:220–222 ("γ≈1.4 is not explained by that saturation") lose their support. appI:27 ("of order 20%") is inconsistent with 1.1 as well.
   - ch13:229–233 (minor; please verify): the bracket in eq:nu-efe, [ν(g_ext)−ν(g_tot)]g_ext, has the opposite sign to the QUMOND uniform-field form, ν(g_tot)g_N+[ν(g_tot)−ν(g_ext)]g_ext. appE:253–254 calls it the QUMOND limit. As written, the parallel component tends to about 1.67 rather than ν(g_ext); I checked this numerically. eq:efe-sat (γ→ν(g_ext)) holds only for the transverse component.
   - ch12:341–342 (minor): "f(r)→1−Λ_eff r²/3 as r→0" omits the −2Mr²/r₀³ term. ch13:106–113 (eq:f-core) has it correctly.
   - appJ:55 (minor): "Λ_eff=3/L_IR²" uses L_IR, which appears nowhere else in chapters/. It is unsourced and undefined.
   - appJ:80–81 (minor): "ψ is not identical to the radial Higgs" is in tension with ch17:208–209, where ψ and σ are the same field in Repair II unitary gauge. Scope wording is needed.
   - ch12:224 and ch12:398–400 (minor): "Λ_eff does not scale as Λ_UV²" and "the derivation just completed" overstate. ch12:243–265 already marks the result as conditional and dimensionally incomplete.

5. *Chat/process language, hard-coded numbers, the appJ item.*
   - appJ:102–104 (minor, confirmed): "the assumption stated in Chapter 3" is wrong; `ass:lorentzian` is at ch04:322. Use `\ref{ass:lorentzian}`.
   - Provenance and process wording (minor): ch11:216 ("source notes"), ch13:123 ("working profile of the notes"), ch15:43 and ch15:157 ("source-note values", "corrected notebook dmcg5.py"). appI:45–46 cites "Banik et al. 2024; Pittordis… 2025; quality-framework study 2026" as plain text, not `\cite`; the last item is unidentifiable. Not independently verified.
   - Hard-coded chapter, theorem and appendix numbers (minor, existing text): throughout ch10–ch18; specifically ch16:214 "Theorems~7.3--12.4", ch16:267 "Appendix~D", ch16:275 "Theorem~7.3", appE:219 "Theorem~7.3", ch17:782–788 "Appendix~A…D".
   - ch17:789 (note): "None of the appendices introduces a new physical hypothesis" is in tension with appE's `ass:sqrt-mod`.
   - appC:103 (minor): "U_N=−G_eff-less toy potential" is garbled.

**Blocking status.** Nothing blocks integrating the 057 insert. No finding conflicts with it or with the 053–056 Problem E blocks. The PRIOR-CLAIM-ERROR candidates in item 4 concern optional Problem H phenomenology and Problem J model text; I am reporting them for the loop, not as conditions on 057.

**Coverage.** The manifest in scratch/digest.md lists 30 files: appA–appL (12) and ch01–ch18 (18). Passes 1–3 (appH), pass 4 (ch01–ch09) and this pass (the remaining 20 files) together have read every file in it in full.
