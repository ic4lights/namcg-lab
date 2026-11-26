VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
All three items (A appK sign and A2 wording, B alpha gloss, C ch16 inventory row, premise sentence and chain item 6) check out. Anchors and labels are verified. B is notation only, and C touches no label and no Ch.17 text. I have three optional wording suggestions, none required.

## Source reading
Full scan: I read all 30 current `chapters/*.tex` files in full (ch01 to ch18 and appA to appL). That covers ch16 and ch17 in full and appH L1-2150 in full, in four ranges. The scan was required under CLAUDE.md 3(c), since the package changes the ch16 assumption inventory and edits Ch.17. It is not the "every 5th integrated item" case: the ledger shows 2 integrations so far, so this would be ordinal 3.

Digest status:
- `make_digest.py --check` printed DIGEST CURRENT at the start of the task.
- It now prints DIGEST STALE, because HEAD moved to 2b9b05b, which only changes `.claude/agents/*` and `.claude/settings.json`.
- `git diff 413ea50 HEAD -- chapters` is empty, so the chapters are unchanged.
- The scan read the files directly, so the stale flag does not affect it.

Also read:
- `proposals/006-followups-002-003-004/proposal-r1.md`, `verify_anchors_labels.py` and its output.
- `proposals/004-author-questions/recommendations-r2.md` (Q1, Q1b, Q2, and the gatekeeper's corrected gloss).
- Statements quoted from 003 review-r2 finding 5 (inventory, premise sentence, chain item 6).
- `reports/ledger.md` and `MILESTONE.md`.

## Claim under review
Three separable bookkeeping edits that derive nothing new:
- **A.** Correct the `a_1` sign in `appK-endomorphism.tex`, and narrow the A2 sentence.
- **B.** Add a parenthetical notation gloss identifying the `alpha` in Problem N's target with the Weyl-squared coupling of `eq:stelle`. It goes at ch17 L506 and appH L2032.
- **C.** Enter `ass:emergent-op` as load-bearing in the ch16 inventory, add a premise sentence, and rewrite chain item 6.

Current critical-path statuses, quoted verbatim from Appendix H:
- Problem N (appH `sec:status-N`): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- Problem F (appH `sec:status-F`): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- Ch17 `sec:ch17-done` lists A, B, C, D1, E, F, G-derived and N as critical path; H, I and J are optional.

The package changes none of these labels and does not advance N or F.

## Checks performed
**A (direct verification).**
- `eq:appA-O` is `O = -g^{mu nu}D_mu D_nu + E` and `eq:appA-a1` is `a_1 = tr_V(R/6 - E)`. The same sign appears in ch02 `eq:SDW-coeffs`, ch08 `eq:a0a1` and ch10.
- appK L17 gives `tr(E) - R dim/6` for the same operator form, the exact negative, so the sign error is real.
- The proposed `tr(R/6 - E) = R dim/6 - tr E` is correct. `delta a_1 = 0` rests only on `tr S = 0` and is sign independent.
- No other file references the appK labels `sec:a1-null` or `sec:a2`.

**A2: the narrowing is correct.**
- `eq:appA-a2` contains `(1/2) tr E^2 - (1/6) R tr E`. With `E = E_0 + xi F_ab S^ab`, the terms linear in F are `xi F_ab tr(S^ab E_0)` and `-(1/6) R xi F_ab tr S^ab`.
- The second vanishes by `tr S = 0`.
- The first is not killed by `tr S = 0`. It needs `tr(S^ab E_0) = 0`, and nothing in the manuscript establishes that for the unspecified `E_0`.
- So recommendations-r2 Q1b ("the linear term vanishes by `tr S = 0`") was too strong, and the researcher's correction is right.
- The replacement ("first non-vanishing correction proportional to F F ... quadratic in the laboratory field") is true as stated, because `F F` is quadratic.

**B.**
- `eq:stelle` (ch09 L116) has `-(alpha/2) C^2`, and `eq:W4` (ch09 L66) has `+c_W C^2`, so `c_W = -alpha/2`.
- appH L2038-2043 now holds the convention: "S_E=-iS_L as in Appendix app:seeley-dewitt, and with curvature invariants continued without change of sign (an added convention)". L2059 states "alpha=-2c_W and beta=2c_R in eq:stelle". So the 002 integration has landed and `sec:status-N` carries the convention.
- The ch17 text names the section by label as `Section~\ref{sec:status-N}`. This matches how ch17 already cites `sec:status-H`.
- In appH the convention follows in the next paragraph, so "stated below" is correct.
- The gloss is exactly the gatekeeper-corrected form from 004 r1. It does not replace alpha by Upsilon, does not restate N in `c_W, c_R`, and adds no hypothesis.
- The Problem N paragraph is at ch17 L497-513. `sec:ch17-done` item 8 (L724-728) and the ordering item at L655 are untouched.
- Other uses of alpha in the book (the `a_2` prefactor at ch08 L400 and ch09 L30, the ECG reduced coupling, the Fierz-Pauli parameter, the per-galaxy fit parameter) are what the disambiguating clause refers to.

**C.**
- `ass:emergent-op` is defined once (ch08 L288, with `rem:ch8-scaffold-vs-emergent`), and the ch16 inventory does not list it. The inventory table runs L81-106 (ch16 L77-108, rows L81-106).
- The row placement is correct: ch08 has `ass:laplace` (L91) before `ass:emergent-op` (L287).
- "Discharging Assumption emergent-op is part of Problem F" appears at ch08 L313-314.
- appH L1636-1644 says it "is assumed, not derived" and that F's missing step "includes discharging" it or "replacing it by another derived ingredient". The premise sentence is consistent with this.
- Ch17 is not edited. The only effect on the completion criterion is by cross-reference through the ch17 L91-96 table ("no load-bearing assumption of Chapter 16 remains assumed"). That is the author-approved effect.
- No contradiction arises with `sec:ch17-done`. The list there ("a chain that still uses dictionary, lorentzian, frame-lock, nondeg, gap-psi or EFT-a2 does not qualify") is already non-exhaustive: EE, local-lorentz, Sent-density and bdy-EE are load-bearing and also not named there.
- The existing ch16 sentence "targets of critical-path Problems A, E and N" is left intact.
- The proposal says the inserted premise sentence goes "after Problem~D1." and before "An assumption may remain". That placement is correct and reads correctly.

**Anchors and labels.**
- I re-ran `verify_anchors_labels.py`. All 8 text anchors occur exactly once and all 9 labels are defined once.
- My own greps found `ass:emergent-op`, `sec:status-N`, `eq:stelle` and `eq:W4` each defined once.
- The script normalises whitespace. Two of the ch17/appH anchors ("computed in / Problem~F") span a line break, and `.tex` files use CRLF. The integrator must match across the line break and preserve CRLF.
- No build was run. Verified only by reading: the new `\eqref` and `\ref` targets exist and `\ref{ass:emergent-op}` is valid in a table cell.

**Emergence.** Nothing in the package makes spacetime or the metric fundamental. The ch16 row says fluctuations propagate on the *emergent* metric, and the premise sentence keeps `ass:emergent-op` assumed and not derived.

## Findings
1. **Minor (optional), appK L38-39 replacement and the following sentences.**
   - Finding: the narrowed sentence is correct. The next two sentences ("The coupling is therefore confined to the conformal mode. No transverse-traceless response is generated at this order.") now rest only on the `F F` term. An `a_2` term linear in F, `tr(S^ab E_0)`, is neither claimed nor excluded.
   - Reason: this is accurate but silent. The text predates this package and is non-load-bearing.
   - Action: optional. If the integrator wants it explicit, append "A term linear in \(F_{\alpha\beta}\), proportional to \(\operatorname{tr}(S^{\alpha\beta}E_0)\), is not excluded by \(\operatorname{tr}S^{\alpha\beta}=0\) alone." This adds no new physics.
2. **Minor (optional), C premise sentence.** "that Problem~F must discharge" is slightly stronger than appH L1644, which allows "or replacing it by another derived ingredient". It matches ch08 L313, so it is acceptable. A fully matching form is "that Problem~F must discharge or replace by a derived ingredient."
3. **Minor (proposal text only, not manuscript), B placement.**
   - Finding: the proposal says the gloss sits "where the symbol is first introduced in each file's N entry". In appH, alpha first appears at L2025-2027 (the ghost-mass sentence), before the L2032 Missing-step gloss.
   - Reason: the stated rationale is wrong for appH, but the placement is still the defining statement of N's target.
   - Action: no manuscript change needed.

I also note, without requiring any action, that the B text in ch17 refers the completion-criterion paragraph to the continuation convention that appH labels "an added convention". It only fixes which symbol alpha is. If the author wants the criterion text kept free of any cross-reference to a conditional block, the clause "with the continuation convention ... in~\eqref{eq:W4}" can be dropped from the ch17 copy only, leaving "(here \(\alpha\) is the Weyl-squared coupling of~\eqref{eq:stelle}, whose \(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\) coefficient is \(-\alpha/2\); it is not any other coupling denoted \(\alpha\) in this book)". Both versions are notation only, and the as-submitted text is the previously reviewed corrected gloss.

## Scope of what is established
- **Established** (by direct comparison):
  - appK's `a_1` has the wrong sign relative to `eq:appA-a1`, and the corrected formula is right.
  - `F F` dependence is quadratic.
  - `c_W = -alpha/2`, conditional on the continuation convention, which now exists in `sec:status-N`.
- **Not established:**
  - The absence of other F-linear terms in `a_2`.
  - Anything about N or F beyond restating what they must show.
- **Classification of C:** `ass:emergent-op` stays an input assumption, not derived. Calling it load-bearing is a classification within the author's recorded approval ("proceed with worth integrating items").
- **Labels:** no problem label, priority or completion classification changes. N and F stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. Nothing here closes or advances N or F.
- **Prior-claim error:** the appK sign error is a pre-existing error in non-load-bearing merged text, already recorded as an author item from 002. MILESTONE.md lists sign corrections to non-load-bearing text as non-milestone, so I raise no `PRIOR-CLAIM-ERROR` flag.
- **Approval:** I did not raise `AUTHOR-DECISION` for B and C, per your instruction. I verified that B is notation only and that C changes no label and no Ch.17 text.

## Recommended disposition
Integrate as submitted, as ordinal 3. The three items are separable and the integrator may apply any subset. After integration, run `python scripts/build_check.py`. The integrator needs the CRLF and line-break matching noted above, and should regenerate the digest.

## Corrected snippet
None required. Optional additions, no extra assumptions:
- Finding 1: append "A term linear in \(F_{\alpha\beta}\), proportional to \(\operatorname{tr}(S^{\alpha\beta}E_0)\), is not excluded by \(\operatorname{tr}S^{\alpha\beta}=0\) alone." to the A2 sentence.
- Finding 2: "...premise of Theorem~\ref{thm:Geff} that Problem~F must discharge or replace by a derived ingredient."
