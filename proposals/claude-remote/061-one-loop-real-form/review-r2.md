VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
Round 2 is accepted. All five round-1 findings (F1–F5) are applied verbatim, nothing else in the insert changed, the researcher's choice of option (a) is recorded and justified, and the result I verified in round 1 still stands within its stated hypotheses.

## Source reading
- **Mode.** Digest plus targeted reads; no full scan. HEAD is 579fcfc and the working tree is clean.
- **Baselines.** The committed `chapters/appH-microscopic-proofs.tex` (sha256 94befe3b…85c6) and `bib/namcg.bib` (sha256 645c93c9…0f67) match the stated baselines.
- **What I read this round.**
  - `appH_insert.r1.tex` diffed against `appH_insert.tex`.
  - `proposal-r2.md`: the change summary, Result 5, the claim table, Decisions Taken and the avenues.
  - The header and target of `apply_r2_edits.py`.
  - `build_r2.txt`.
  - My round-1 reads of appH L1482–1614 (including 060's L1603: base-coordinate member γ=−3c, c>0) and L2478–2486 (Section F compact check) still apply; neither file has changed.
- **Scan ruling.**
  - 3(c): not triggered. No definition, assumption, scope or status passage changes; the closing status sentence is unchanged.
  - 3(b): treated as in 059/060 (M2 non-stopping, no milestone digest).
  - The integration ordinal would be 59. The 5th-item full scan is due at 60.

## Claim under review
- **Claims.**
  - Pf M(T̄)=0 at every non-zero finite-N member of the 060 family. The setting is Definition (A), h_0 of signature (9,1), the supplied IKKT fermions and a supplied γ>0.
  - Supporting statements: the operator forms, the species weight, zero-mode counts, phase-only negative modes, and regulator dependence of the bosonic comparison.
  - A conditional statement, now restricted to the so(4,1), W-timelike members.
- **Problem E (Appendix H, verbatim).** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **Problem D (Appendix H, verbatim).** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."

## Checks performed
- **Diff r1 → r2.** Only three paragraphs change (insert lines 6, 8, 10):
  - **F5.** In the zero-mode block, "\(\mathfrak{so}(5)\)" became "\(\mathrm{Spin}(5)\)" in the N=∞ sentence.
  - **F3, F4.** In the consequences block, the traceless qualifier and the cross-reference to Section~\ref{sec:status-F} were added, and the "moduli of the members' contributions" wording was applied. Both match my snippets character for character.
  - **F1, F2.** In the non-compact block, the F1 option (a) snippet and both F2 substitutions (K=−k_0²+|k|² and K=k_0²+|k|²) were applied verbatim.
  - The setting, operators, scope and closing paragraphs are byte-identical to r1.
- **F1 re-verified.** From 060's identity γ=3cη^{c0c0} with H=cη, which h_0 (9,1) must realise on W, the only options at γ>0 are:
  - η definite, giving so(5) with W spacelike;
  - η of type (4,1), giving so(4,1) with W timelike.

  The base-coordinate member (c0=5) needs γ<0, which the inserted text now states correctly. The new conditional attributes the Lorentzian kinetic tensor to the supplied γ sign, h_0 and fermion content, says it is "not derived", and does not identify it with the emergent metric.
- **Decision record.** "Decisions Taken" records option (a) with its reason (060 L1603). Option (b), the comparison across the sign of γ, is kept as avenue 6. The table and Result 5 are consistent with the insert.
- **apply_check, re-run in report mode.** Output is identical to `apply_check.txt`.
  - Anchor count 1, at L1609.
  - Insert: LF 9034 B, 08f9bb84…3a7a (matches the file on disk); CRLF 9046 B, 9c9b47e4…42fe.
  - Result appH: 599923 B, sha256 82ab2364…279c, CRLF 3313, bare LF 0.
  - Bib result: 28049 B, 582f09d5…1f22, CRLF 937.
  - Labels: ass:lorentzian and sec:status-F each resolve once. No new labels.
  - Cites: IKKT1997, Steinacker2023 and Steinacker2015S4 all resolve. No duplicate keys.
- **Edit script.** `apply_r2_edits.py` checks the r1 hash (a5039fc3…) and writes only to the insert file in the proposal folder.
- **Build.** `build_r2.txt` reports pdflatex/bibtex/pdflatex/pdflatex exiting 0, 374 pages, 0 undefined, 0 multiply-defined, and a clean bibtex run. The patched hashes it records match the ones I recomputed. I did not run the build myself, so this is the researcher's record. The integrator's `build_check.py` remains required.
- **Unchanged since round 1.** The core derivations I checked in round 1 are unchanged:
  - the D² shift of +3/2, with its sign confirmed by positivity;
  - the identity C4^tot=C5+3/2 on top components;
  - the ≥32 kernel per adjoint copy for any non-trivial finite-dimensional representation;
  - counts of 80 and 304;
  - the species weight 5−4−1=0;
  - the degree bound k/2;
  - the regulator integrals;
  - the literature checks: 1510.05779 Eq. (3.28) and Section 4 read from source; 2303.08012 Eqs. (4.14)–(4.16) checked. The exact form of the 2303.08012 regulator term remains not independently verified, which is not load-bearing.

## Findings
- **Round-1 findings.**
  - F1 (major): resolved.
  - F2, F3, F4 (minor): resolved, verbatim.
  - F5 (optional): adopted.
  - F6 (no build): a scratch build is recorded; the integrator build is still needed.
- **New findings.** None.

## Scope of what is established
- **Established** (bounded no-go, M2). Within:
  - (a) Definition (A) with massless MW IKKT fermions;
  - (b) the 060 Lie-generator family with isotropic h_0-contracted mass;
  - (c) finite-dimensional or compact unitary (Spin(5)) representations;
  - (d) fixed γ>0, h_0 of signature (9,1), hence W spacelike for so(5);

  the fermion form of every non-zero compact member is degenerate, so Pf M(T̄)=0 at every non-zero finite-N member. This also holds with a transverse factor K, and the kernel persists at N=∞.
- **Also established.** Negative modes affect only the phase. The bosonic per-volume comparison depends on the regulator.
- **Conditional.** If the fermion forms of the so(4,1), W-timelike members (N=∞ only) are non-degenerate, the supplied fermions separate those members from the compact ones at one loop. Among them is the conjugate-coordinate member, whose kinetic tensor is Lorentzian on m≠0. That tensor is fixed by supplied inputs, not derived.
- **Status.** The outcome is PROGRAMME-CONDITIONAL. E and D (D1) remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL, and ass:lorentzian is retained. No label change.
- **Open avenues, ranked.**
  1. Normalisable kernel of the fermion form for the so(4,1)⊂so(4,2) doubleton member at γ>0. This is decisive.
  2. Approximate finite-N truncations of so(4,1), which would relax hypothesis (b).
  3. A fermion mass or SUSY-preserving deformation, which would relax (a); this content would be supplied.
  4. A derived N=∞ cut-off for the bosonic factor.
  5. The g/γ order of the compact contribution.
  6. The γ<0 / base-coordinate comparison and saddles outside the family.
- **Not a breakthrough.**

## Recommended disposition
Integrate as-is:
- the r2 `appH_insert.tex`, converted to CRLF, inserted before the unique Problem E `\paragraph{Status.}` anchor;
- `bib_entries.bib` appended with CRLF.

Then run `python scripts/build_check.py` with bibtex.

## Corrected snippet
None needed.

Files:
- C:\Users\redgi\Projects\namcg-lab\proposals\061-one-loop-real-form\proposal-r2.md
- C:\Users\redgi\Projects\namcg-lab\proposals\061-one-loop-real-form\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\061-one-loop-real-form\apply_check.txt
- C:\Users\redgi\Projects\namcg-lab\proposals\061-one-loop-real-form\build_r2.txt

VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0
