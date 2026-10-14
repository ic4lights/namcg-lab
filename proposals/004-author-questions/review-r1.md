VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: AUTHOR-DECISION | PROGRESS: first | OPEN: 0/4

(Advisory review. The verdict applies to the recommendations, not to any chapter text. No milestone fires on this file. M5 would fire if the author adopts S1. No label change is proposed and none is warranted. No PRIOR-CLAIM-ERROR beyond the already-recorded 003 items. AUTHOR-DECISION covers S1/S2, the ch17 gloss, and the ch16 inventory entry.)

## Verdict
Q1, Q3 and Q6 are sound, Q4 is sound with corrections, and Q2 and Q5 are sound with corrections. The Q5 identity is correct and holds more generally than the script tests. The claims that R1 is "dead" and that R4 is "the only route with a path to a matrix-derived G_eff" need softer wording, and one placeholder label is wrong.

## Source reading
Digest plus targeted reads, not a full scan. The orchestrator reports `DIGEST CURRENT`. The researcher saw STALE, but I confirmed `chapters/` is unchanged. I read in full:
- `recommendations-r1.md`, `MILESTONE.md`, and `review-r1.md` of 003.
- The relevant parts of 003 `proposal-r1.md`.
- appK L10-20 and L36-43.
- appA `eq:appA-O` and `eq:appA-a1`.
- ch09 `eq:W4` and `eq:stelle`.
- ch03 `rem:ch3-moyal-check` and `rem:ch3-varying-theta`.
- ch08 L52-60, appB L104-115, appG L15-30, ch04 L414-424, ch16 L120-132.
- Label greps.

I did not re-read ch17 or appH end to end. For the critical-path set I rely on the 003 reviewer's full scan and on the 003 review quotes below. I found no discrepancy in the passages I read.

## Claim under review
The advisory answers Q1-Q6, with no label changes. The current statuses, quoted from the 003 review's verbatim Appendix H quotations, are unchanged:
- **F:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **C:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion."
- **D:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- **B:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **N** is in the Chapter 17 set; I have not re-quoted its Appendix H entry here.

## Checks performed

**Q1 (verified directly).**
- appA `eq:appA-O` is O = −D² + E.
- `eq:appA-a1` is a_1 = tr(R/6 − E).
- appK L17 reads a_1 = tr(E) − (1/6)R dim, which is the exact negative. The sign error is real.
- δa_1 = 0 does not depend on the overall sign.
- Correction (a) with `\eqref{eq:appA-a1}` is right.
- The side note is right: F F is quadratic in the laboratory field (appK L38-39 says "linear").

**Q2 (verified directly).**
- `eq:stelle` has −(α/2)C². `eq:W4` has +c_W C².
- So c_W = −α/2. This is conditional on the continuation convention in proposal 002 (002 item 4).
- Rejecting Υ and rejecting the c_R widening are sound.
- Declining to edit `ass:EFT-a2` is sound.
- Option 2 is the right choice, but the draft gloss has errors (finding 2).

**Q3 (partly verified).**
- Crossref via WebFetch confirms the entry: Barvinsky and Vilkovisky, NPB 333 (1990) 471-511, "Covariant perturbation theory (II). Second order in the curvature. General algorithms".
- Grep finds no Barvinsky or Vilkovisky entry in `bib/` or `chapters/`.
- Narrow citation for nonlocal form factors only; decay unverified. Correct scoping. I did not read the paper.

**Q4 (verified directly).**
- ch08 L285 and `prop:scaffold` exist.
- References to `prop:scaffold` exist at appB L112 and ch08 L364, as stated.
- ch16 L128 reads "targets of critical-path Problems A, E and N", so adding F is a real edit.
- Labels `sec:ch8-which-g`, `app:status`, `sec:status-F`, `ch:heat-kernel`, `ch:agenda`, `eq:O-eta`, `eq:Smicro` and `eq:W-expand` each exist.
- `ass:emergent-op` does not exist yet.
- **`ch:vierbein` does not exist.** The ch04 label is `ch:vierbein-emergence` (ch04 L2).
- The draft correctly includes the fixed-A_μ qualifier required by 003 finding 2.

**Q5 (my re-derivation).**
- I re-ran `check_weighted_laplacian_a1.py`. It reproduces its saved output: parts 1 and 1b are zero, and the pointwise difference is identically zero.
- Hand check, any 4D g with det g = 1 and G = ρg:
  - L = Δ_G − ∇lnρ·∇ ✓.
  - R_G = ρ⁻¹[R − 3□lnρ − (3/2)|∇lnρ|²].
  - E = ρ⁻¹(−½□lnρ − ¼|∇lnρ|²).
  - So R_G/6 − E = ρ⁻¹R/6, and √G = ρ² gives √G(R_G/6 − E) = ρR[g]/6 pointwise.
- The identity therefore holds for every unimodular 4D metric, not just the diagonal family. The researcher's "not checked" caveat is over-cautious in the safe direction.
- The sign conventions (−L = −D² + E, a_1 = R/6 − E) match appA.

**Q6 (verified against source text).** The anchors exist exactly as quoted: ch04 L418-423, ch08 L56-58, ch08 L363-367, appG L19-29, appB L110-112.

## Findings

1. **Severity: major.**
   - **Location:** Q5, R4 "escapes Lemma 2".
   - **Finding:** R4 escapes the hypotheses of Lemma 2 (an SO(4)-invariant vacuum and regulator), but this is not evidence for an Einstein-Hilbert term.
   - **Reason:**
     - For constant Θ, K_Θ is a fixed constant metric. The example in `rem:ch3-varying-theta` has only an SO(1,1)×SO(2) isometry. A K_Θ-built regulator gives the same situation as a flat scaffold, with g^(0) replaced by K_Θ and anisotropic rather than p²-only forms.
     - Nothing there gives linearized diffeomorphism invariance of a composite h.
     - The preview calculation is exactly Lemma 1's mechanism applied to a curved Θ-built scaffold metric. It produces curvature of g_ρ, a Θ-built metric, not of a Φ-composite metric.
     - Whether the metric seen by Φ fluctuations is the Θ-built one or e[Φ] (the locked-block target of F) is unresolved. This is what S1 is about.
   - **Required action:**
     - Reword to "R4 is not excluded by Lemma 2's hypotheses, and it is the only route identified in the documents read that ties the derivative index to the tangent index (via Θ)".
     - State that the Θ-built metric, not the Φ-composite metric, is the one that acquires curvature.
     - State that Lorentz recovery (D1/E) is an open cost, not just a falsifier.
     - Drop "the only within-core route that keeps a genuine path to a matrix-derived G_eff" in favour of "the only one identified here". R3 and S2 are not shown dead.

2. **Severity: major.**
   - **Location:** Q2 draft gloss.
   - **Finding:** The draft says α "is the coefficient of CC in eq:stelle". That is wrong, because the coefficient is −α/2. It also states c_W = −α/2 with no mention that this depends on the continuation convention recorded in 002.
   - **Reason:** The gloss would enter a completion criterion (ch17 L506 and L727). It must not carry an unflagged convention-dependent identity or an incorrect definition.
   - **Required action:** Use the corrected snippet below. The author must approve the ch17 edit as a pure notation gloss.

3. **Severity: major.**
   - **Location:** Q4 DRAFT.
   - **Finding:** `\ref{ch:vierbein}` is a nonexistent label. The real label is `ch:vierbein-emergence`.
   - **Reason:** Using the placeholder would add an undefined reference.
   - **Required action:** Use `ch:vierbein-emergence`. `ch:heat-kernel` and `ch:agenda` exist. The researcher's "placeholder" status for them is unnecessary caution.

4. **Severity: major.**
   - **Location:** Q5 preview and wording of "R1 dead".
   - **Finding (a):** The identity is computed for a heat-kernel Λ that is constant. The text also cites a Θ-dependent regulator (Λ_UV ~ Θ^(−1/2)). A position-dependent Λ² would multiply the Λ² term by a further function of ρ.
   - **Finding (b):** The "(∂ρ)² term cancels" statement is not a physical cancellation. With det g_ρ = 1 there is no conformal mode, and ρ is a separate dilaton. Brans-Dicke ω = 0 means no ρ kinetic term in this sector.
   - **Finding (c):** The Λ⁴ ∫ρ² term and the vector-sector contributions are not addressed.
   - **Finding (d):** "Dead end (Lemma 2 covers it)" is consistent with 003 review finding 2, which says Lemma 2 covers eliminated connections. It holds only within Lemma 2's class: flat scaffold, rotation-preserving regulator and gauge fixing, invariant vacuum, and a fixed linear image of the Φ components.
   - **Required action:**
     - Say "constant Λ; scalar sector; unimodular g_ρ; ρ treated as a field; identity holds for every 4D unimodular g_ρ".
     - Replace the "cancels" wording.
     - Say "excluded within Lemma 2's class" instead of "dead".

5. **Severity: minor.**
   - **Location:** Q5, the "Recommendation and next target" paragraph.
   - **Finding:** It recommends the author "authorize S1 for investigation", inside the STRUCTURAL section. The separation itself is correct: S1 to S3 are not defaults. The next target is within F and does not change the F locked-block target.
   - **Required action:** Say the computation is a preview, and that its output is only meaningful for F if S1 is adopted.
   - The Q5 ranking as "highest impact" is not supported while R4 is unproven.

6. **Severity: minor.**
   - **Location:** Q5 literature.
   - **Finding:** The arXiv 2411.02598 abstract claim and `Steinacker2023` are unverified. I also did not verify them.
   - **Required action:** Keep them marked "not independently verified".

7. **Severity: minor.**
   - **Location:** Q6.
   - **Finding:** The item 6 corrected ch05 snippet depends on the 003 revision. Q6 should state that it uses the corrected snippet from `review-r1.md`.
   - **Required action:** The ch16 additions and all labels need a normal proposal round.

## Scope of what is established
- **Established identity:**
  - The Q1 sign error.
  - α = −2c_W (conditional on the continuation convention).
  - The Barvinsky-Vilkovisky bibliographic record.
  - The Q5 pointwise identity √G(R_G/6 − E) = ρR[g_ρ]/6 for every 4D unimodular g_ρ. The script covers a diagonal family; the general case I verified by hand.
- **Conditional:** The Q5 operator L and the trace map are assumed (`rem:ch3-varying-theta`). Constant Λ, scalar sector only.
- **Not shown:**
  - Any EH term or sign of G_eff.
  - Recovery of Lorentz invariance in Presentation A.
  - Equivalence of K_Θ with e[Φ].
- **Labels:** F, C, B, D and N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- **Bias check:** The favour-NAMCG bias shows only in the "only route" and "highest impact" phrasing (findings 1 and 5). The STRUCTURAL options are separated correctly, no label change is proposed, and nothing is closed by scope.

## Q-by-Q summary
- **Q1:** sound. **Q2:** sound with corrections (finding 2). **Q3:** sound. **Q4:** sound with corrections (finding 3). **Q5:** sound with corrections (findings 1, 4 and 5). **Q6:** sound, pending the label fix and a normal proposal round.

## Recommended disposition
Do not integrate any text from this file. Fix findings 1-5, then return to the author. The next step is a normal proposal round per item. The Q1 appK fix is the smallest and most self-contained, and is routine, not a milestone. The Q4/Q6 package should go together, and the ch16 inventory entry is an author-approval item.

## Corrected snippet
No new physics. Extra assumption: the continuation convention is recorded in 002 and the identity is conditional on it.

Q2 gloss, replacing the draft:
```latex
(here \(\alpha\) is the Weyl-squared coupling of~\eqref{eq:stelle},
whose \(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\) coefficient is
\(-\alpha/2\); with the continuation convention stated for
Chapter~\ref{ch:ultraviolet-placeholder}, \(c_W=-\alpha/2\)
in~\eqref{eq:W4}; it is not any other coupling denoted \(\alpha\) in
this book)
```
The label `ch:ultraviolet-placeholder` is a placeholder. The integrator must use the actual ch09 chapter label, or the appendix label where the 002 continuation convention is stated. I have not verified that label here.

Q4 label fix: replace `Chapter~\ref{ch:vierbein}` with `Chapter~\ref{ch:vierbein-emergence}`.

Files: `C:\Users\redgi\Projects\namcg-lab\proposals\004-author-questions\recommendations-r1.md` and `check_weighted_laplacian_a1.py` / `.out.txt` in the same folder.
