VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/1

## Verdict
All three r1 major findings are closed. The researcher applied my snippet, E2 and E7 verbatim, and F0, F3 and F7 are sound. One major finding remains, and it blocks a plain ACCEPT. The opening sentence of the "General sector" paragraph (baseline L42–45) still says that the half-sided-inclusion construction "yields a well-defined modular operator … from matrix data alone". The corrected free-sector paragraph immediately before it now says that step is not derived even in the free case. The paragraph also omits the state that any modular operator requires. Fixing it takes one replacement, given below.

## Source reading
Digest + targeted reads. This is not a full scan.
- `python scripts/make_digest.py --check` printed `DIGEST CURRENT`. HEAD is 6fb263e. `dirty-chapters: yes` because appH and bib hold the uncommitted 064/065 changes, which is expected.
- The 6fb263e commit touches only the proposal folder (9 files). The manuscript working tree still matches the baselines.
- Read in full:
  - proposal-r2.md and review-r1.md;
  - the r2-patched appH L22–80 (Free/Poisson, General sector);
  - the r1→r2 diff and the baseline→r2 diff;
  - moyal_K0_symbol_066.py;
  - scratch_build_066_r2_output.txt.
- r1 reads (appH Problem A, ch17 L340–399, ch03 `sec:ch3-scales`, appB `sec:appB-BW`, ch02/ch06 BW passages, bib) are unchanged in the working tree, so I did not re-read them.

**Scan ruling (unchanged from r1).** E6/F1 narrow the scope statement of a claimed result in the ledger section of a critical-path problem, so CLAUDE.md 3(c) applies. The verdict carries M3, so 3(b) applies too. A full scan of all `chapters/**/*.tex` is required before a plain ACCEPT or integration. I have not done one. A future plain ACCEPT of this package is conditional on that scan finding no conflicts.

## Claim under review
- **Claim.** appH L30–31, "By the Bisognano–Wichmann theorem this charge is the modular Hamiltonian of the causal diamond of the free theory", is false. Bisognano–Wichmann is the wedge theorem. The diamond result is Hislop–Longo's, for the free massless scalar. The lemma's quadratic sector contains the massive radial mode.
- **What the edits do.** They correct that sentence. They mark the K_0 Weyl-symbol identification, the half-sided-inclusion step and the √δΘ estimates as not derived. They make the lemma conditional and restrict it to the free massless scalar part.
- **Original target (ch17 L377–392).** Assumption `ass:dictionary`, with Hilbert space, Weyl map, continuum limit and error at each order in Θ.
- **Labels, verbatim.** appH L16–20: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. The general matrix-to-modular map remains unproved. A scope-limited Presentation-B model may retain Assumption~\ref{ass:dictionary} and claims no derivation from the matrix model." ch17 L378: "OPEN; CRITICAL PATH for the matrix-derived label." The package changes no label.

## Checks performed
- **apply_check_066_r2.py**, re-run report-only into a fresh scratchpad directory (`…\scratchpad\gk066r2`). Result: ALL CHECKS PASS.
  - Baselines match: appH 624232 B / c2dac013…558b5c; bib 29781 B / 28fdd7f8…a64d.
  - The r1 chain reproduces 173ab97b….
  - Each of D0–D5 and F0–F8 has its OLD text exactly once before and its NEW text exactly once after.
  - The chain result equals the direct result.
  - appH r2: 625504 B, b8155af307c5d8840405d2bb8e4d3e1b5217316d1fcf555f398839c9ce82394e, CRLF = LF = 3398, no bare LF, no BOM.
  - bib: 30159 B, 4315a895…6060, CRLF = LF = 1006.
- **My diffs.**
  - r1 result → r2 result: hunks only at L28 (F0), the Hence/half-sided/lemma block (F1), the ℓ in E2 (F2), L37–39 (F7), the norm phrase (F3) and the display (F6/E7).
  - Baseline → r2: hunks only at L28, L30–34, L36–39, L51, L54 and L56–60.
  - Nothing else changed.
  - F1 matches my r1 snippet word for word, apart from its shared first line, which is kept as in the snippet. E2 matches with ℓ, and E7 matches. F4, F5 and F8 are identical to r1's E4, E5 and B1.
- **moyal_K0_symbol_066.py**, re-run. Output is byte-identical to the stored file.
  - Exact Moyal product, d = 2, generic quadratic h with six coefficients.
  - The integrand ½Θ^{-1}_{μν} x_μ⋆[x_ν,h]_⋆ equals (i/2)x·∂h identically, with difference 0. It differs from the boost weighting.
  - I checked the index contraction in the code: Θ^{-1}_{μν}Θ_{νρ} = δ. This matches my r1 computation.
  - The script's "proportional to boost?" test only checks a single symbolic k, so it is weak. The displayed forms are plainly different, so this does not matter.
  - This reproduces a computation under the Moyal-element reading of H_quad. It does not disprove L28, and the text does not claim that it does.
- **Scratch build** (researcher's log; I did not re-run it): pdflatex/bibtex/pdflatex/pdflatex all exit 0, 0 bibtex warnings, 0 undefined or multiply-defined lines, `HislopLongo1982` in the .bbl, 380 pages.
- **Labels, citations and wording.** `sec:appB-BW` and `sec:ch3-scales` each exist once. No new labels. The citations `BisognanoWichmann1976` and `HislopLongo1982` are verified (literature checks in review-r1: AIP DOI redirect, Crossref, UKY abstract, Longo–Morsella full text). No process language. No status-label text is touched.

### Re-verification of r1 findings
1. **F1 conflated the wedge and diamond generators. Closed.** The new sentence makes the identification conditional on which generator the charge coincides with. It is logically correct.
2. **The half-sided sentence was unsourced ("exactly H_D"). Closed.** It is now restricted to the diamond case and marked not derived. The lemma is stated as conditional on it ("Given these two steps").
3. **The K_0 symbol claim was unsupported. Closed.** The F1 sentence "Which of these charges … is not derived here" closes it, and F0 supports that.
   - F0 judgement: "is taken here to have Weyl symbol equal to" is consistent with F1. It marks the identification as a working premise rather than an established fact, and it does not assert that L28 is false.
   - The parenthetical "(Moyal bracket reduces exactly … degree ≤ 2)" is still a true statement. It now reads as background to the premise, which is acceptable.
   - Because the Moyal-element reading gives a dilatation weighting, the "taken here" premise is visibly fragile. The text is honest about this ("for which H_quad"), so the wording is acceptable.
4. **R → ℓ. Closed.** E2 and the display both use ℓ, consistent with ch06/appB.
5. **Wording/norm. Closed.**
   - F3 reads "which is not derived here (in a norm not specified here)". The doubled "here" is clumsy but correct; see the optional wording under the snippet.
   - Keeping the estimate as "unproved", rather than deleting it, is right. E5/F5 already limit what it would control.
6. **L38 dangling "already noted above". Closed.** F7's "This records the conditional free/Poisson content of Problem~A; it remains dependent on the free-field theorems cited above and on the two steps not derived here" is accurate. It refers to the BW and HL citations and to the two F1 steps, and it does not restate a status label.

## Findings
1. **Major. appH "General sector", baseline L42–45, unchanged by the package.**
   - Finding: the paragraph says "the same algebraic construction yields a well-defined modular operator of a half-sided inclusion from matrix data alone". The corrected free paragraph (F1) now says the half-sided-inclusion step is not derived even in the quadratic sector. The general-sector sentence still asserts it as established for the harder non-quadratic or fluctuating-Θ case.
   - Reason, inconsistency: the correction itself has made this sentence stale, inside the section being corrected. Reviewers must look for exactly this kind of stale statement an insertion creates. I missed it in r1, where it appeared in the half-sided grep (L44) but was not raised. The researcher is not at fault.
   - Reason, missing state: "from matrix data alone" is wrong as written. A modular operator is defined only relative to a cyclic and separating state, so a commutator identity or other algebraic data cannot fix it on their own.
   - Required action: replace as in the corrected snippet below. This is new edit F9. Re-run apply_check and the scratch build afterwards.
2. **Minor, optional.** The doubled "here" in F3; see the alternative wording under the snippet. This is not required.

## Scope of what is established
- **Established (correction; PRIOR-CLAIM-ERROR confirmed, M3, provisional pending the full scan).**
  - The original L30–31 sentence misattributes the diamond modular result to Bisognano–Wichmann. It also extends that result to a sector that contains the massive radial mode m_σ ∼ √λ v.
  - Bisognano–Wichmann gives the wedge modular group as rescaled boosts, independent of mass.
  - Hislop–Longo gives the geometric diamond modular group for the free massless scalar.
- **Established computation, conditional on reading H_quad as a Moyal algebra element.** K_0's integrand is (i/2)x·∂h, a dilatation-type weighting, not a boost charge.
- **Unresolved, and now correctly marked:** the K_0 symbol identification; the half-sided-inclusion step (free sector, and in the general sector once F9 is applied); the δΘ estimates in an unspecified norm.
- **Not claimed, correctly:** that the massive diamond modular flow is non-geometric.
- **Problem A** stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. This is neither DERIVED nor PROGRAMME-CONDITIONAL progress on A.
- **Open avenues that could still help the IR / full-GR derivation**, ranked:
  1. A wedge reformulation of the modular map. BW is mass-independent, so this needs only a boost charge.
  2. An operator-level definition of H_quad, followed by redoing the K_0 symbol computation. Under the Moyal-element reading a different operator is needed to get a boost or CKV charge. The researcher's forks (i) and (iii), a stress-tensor density or a partial internal trace, fall within the core. Fork (ii), with a supplied ω^{μν}, would import geometric data and is not matrix-derived.
  3. The IR theory below m_σ, then a check of which conformal free sectors remain.
  4. Small-diamond (ℓ ≪ 1/m_σ) error control. This is hard: the published massive-ball result was withdrawn because of a gap.
  5. Free massless Maxwell/fermion diamond results (literature not checked).
- **Report-only item, unchanged:** the ch17/appH definitional mismatch for Problem A (dictionary vs. matrix-to-modular map) is an author scope decision. No edit is proposed.

## Recommended disposition
Revise (r3) with the single F9 replacement below, keeping F0–F8 unchanged. Re-run apply_check and the scratch build. If F9 is applied verbatim and nothing else changes, I expect a plain ACCEPT, conditional on the required full scan (3(b)/(c)). The orchestrator runs that scan in split passes before integration.

## Corrected snippet
F9, in `chapters/appH-microscopic-proofs.tex`, "General sector". The OLD text occurs once in both the baseline and the r2 result. Use CRLF line endings.

OLD:
```latex
\(\Theta=\Theta_0+\delta\Theta\), the same algebraic construction yields
a well-defined modular operator of a half-sided inclusion from matrix
data alone. That operator is a candidate modular Hamiltonian. It is the
```
NEW:
```latex
\(\Theta=\Theta_0+\delta\Theta\), the same algebraic construction would
yield, if it generates a half-sided inclusion (a step not derived here,
as in the free case) and given a cyclic and separating state, a
modular operator built from matrix data. That operator would be a
candidate modular Hamiltonian. It is the
```
F9 introduces no new physics. It makes explicit the standard Tomita–Takesaki requirement of a cyclic and separating state. This is a prerequisite already implicit in any use of "modular operator", not a new NAMCG assumption.

Optional, for F3 only, if the researcher wants to remove the doubled "here":
```latex
terms and is not a routine specialisation of the free-field result. The
estimate, which is not derived here and whose norm is not specified,
\[
```

Relevant paths:
- C:\Users\redgi\Projects\namcg-lab\proposals\066-bw-diamond-scope-correction\proposal-r2.md
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (General sector, baseline L41–61)
- Re-run outputs:
  - C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk066r2\ (r2-patched copies)
  - C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\moyal066.txt

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/1
