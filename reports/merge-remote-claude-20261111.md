# Bring-in of `origin/remote/claude` into `local/gpu` — 2026-11-11

Uncommitted working-tree state, left for the author. Nothing was committed, pushed or merged;
`git merge` is denied to the orchestrator by `.claude/settings.json`, so the content was brought in
at file level. The history-level merge stays the author's.

## The two histories

Fork point `2cd49d0` (after proposal 053 r1/r2). Local line tip `651b1d7`, remote line tip `e59a120`.

| | local line | `origin/remote/claude` |
|---|---|---|
| proposals run after the fork | 054-068 (own slugs) | 053 r3, then 054-067 (different slugs) |
| integrated-item count | 68 | 65 |
| outcome | continues | 066 STALLED at the round cap; 067 un-ledgered |

`proposals/NNN` numbers are **not comparable** across the two lines: `054`-`066` name different
proposals. The remote line's evidence was therefore copied to `proposals/claude-remote/` unchanged
(249 files, blobs of `e59a120`); see its `README.md`. Their two SME scouts
(`sme-scout-20261108-after55.md`, `-after60.md`) came in under their own names.

## What entered the manuscript — 7 files, +371 / −32

Five files where only the remote line had advanced (local copies were still at the fork state, so
these are exactly their changes): `ch13-cores-galaxies.tex`, `ch16-falsifiers.tex`,
`appE-rar-bridge.tex`, `appI-gaia-wide.tex`, `ch14-dissipation.tex`.

Two files both lines had advanced, 3-way merged (`git merge-file`): `chapters/appH-microscopic-proofs.tex`
(3 conflicts) and `bib/namcg.bib` (1). `reports/ledger.md` merged as a union (1 conflict).
`namcg-book7.tex`: both lines made the identical edit (dropped `\include{chapters/appH-detailed}`),
so nothing to do. Both lines had already deleted `appH-detailed.tex` and
`appH-microscopic-proofs-compact.tex` — no modify/delete conflict.

### appH resolution (no wording of ours; text only kept or reordered)

1. **Problem E paragraph, "Bearing on Section ref{sec:status-E}"** — kept OURS: their version is a
   strict word-subset of ours (ours adds the finite-`N` positivity-failure sentence, which the same
   paragraph cross-references). No loss.
2. **"The regulated Lorentzian integral at finite `N`"** — both lines had written this paragraph
   from the same 053 preamble (15 identical lines + 626 identical characters, then a clean split at
   a sentence boundary, both closing on the *identical* status sentence). The preamble is kept once,
   then OUR continuation (exponential observables at `N=2`, slice bridge band, `\gamma\to0^-` link,
   reflection-positivity failure) followed by THEIR continuation (Fourier observables, index-mixing
   contours, regulator-fixed contour class, positive-mass plane class, other-signature target
   contractions, semi-classical signature criterion, one-loop conjugate-coordinate family, doubleton
   fermion kernel, relative Pfaffian density). Order forced by the text: our part continues the
   preamble mid-subparagraph, theirs opens with a fresh `\paragraph`.
3. **Later Problem G-derived anchor** — both blocks kept verbatim, ours (replica-density bounded
   obstruction) then theirs (relational edge entropy on a compact fuzzy factor). No shared lines.

Against our HEAD, the merge removed **0** lines of our text and added 176 in appH.

### bib resolution

Union by citation key: 101 (ours) + 94 (theirs) → 113 entries. 82 keys shared and byte-identical
after whitespace normalisation, **0 shared keys with differing text**, 12 only-theirs keys appended.
All 12 are cited in `chapters/` (none dead). No duplicate keys.

## Rule 2 check

No status, priority or completion label was added, removed or changed by this bring-in: the five
whole-file chapter edits touch no `Status:`/`Priority:`/`Completion:` line, and the appH diff against
our HEAD contains only additions of scoped-hypothesis sentences. Their stalled 066 (Problem A,
Bisognano-Wichmann diamond scope) produced **no** manuscript change.

## Corrections now in the working tree (their M3 PRIOR-CLAIM-ERROR items)

* **ch14 Problem I (their 063):** the `P_ent/P_GW` ratio was claimed to grow with separation as
  `(d/ĜM)^k`. Corrected: for a circular orbit both powers scale as `d^{-5}`, so the ratio is
  `(5/32)·η/(Ĝ³M²μ)`, independent of `d`; a growing ratio would need drag exponent `n<4`, which
  Assumption ref{ass:drag} does not adopt. The end-of-chapter exercise was rewritten to match.
* **ch13/ch16/appE (their 058, Problem H optional):** `nu_sqrt(g_gal) ~ 1.1` → `~1.35` at the
  manuscript's own inputs (`g_gal = 2.2e-10`, `g_s = ĝ = 1.20e-10`, `nu = 1.348`), sites
  ch13:255, ch16:208, appE:48, appE:221; the dependent "gamma ~ 1.4 not explained by that
  saturation" claim softened to "comparable to"; appI "20%" clarified as a velocity excess 0.16-0.22.
  **Their own ledger flags that `g_gal = 2.2e-10` and appI's `(1.5-2.2)e-10` have no source in the
  repository (rule 7), and that ch16 still hard-codes "Theorem~7.3", "Appendix~D", "Assumption~E.1".**
  These numbers arrived from the other run's gatekeeper and have not been re-derived on this line.

## Verification actually performed

* `python scripts/build_check.py` **could not run**: no `pdflatex`/`bibtex`/`latexmk` on this
  machine (`/usr/share/texlive` has `texmf-config` but no binaries). The PDF is untouched.
* Static equivalent, all clean over 31 files: 0 cited keys missing from the merged bib, 0
  `\ref`/`\eqref` targets with no `\label`, 0 multiply-defined labels, 0 conflict markers left.
* The merged appH has not been read as a whole by a gatekeeper: two adjacent Problem E blocks and
  two adjacent Problem G-derived blocks came from runs that never saw each other. A full scan
  (CLAUDE.md 3(a)/(c)) is advisable before the next integration.

## Author decisions left open

1. History: commit this state on `local/gpu`, or do a real `git merge origin/remote/claude` and
   re-resolve the same 6 paths yourself (this report is the resolution record).
2. Proposal 053 now has two r3 rounds (ours in `proposals/053-*`, theirs in
   `proposals/claude-remote/053-*`). The manuscript carries one fused paragraph. Pick which r3 is
   canonical for 053, or record both deliberately.
3. Ordinals: decide whether future work on this line continues numbering at 069, and whether the
   remote line's integrated count (65) is ever folded into the local count. It has not been folded
   in anywhere: the local ledger still says what it said.
4. Whether to adopt their corrected numbers (§ above) as this line's record, or re-derive them.
5. `scratch/digest.md` is stale for this tree — **not rebuilt**, held for your approval.

## Repository discrepancy worth correcting

`CLAUDE.md` states ".tex files use CRLF line endings. Preserve them." Every tracked `.tex` and `.bib`
file in this repository is pure LF (`chapters/appH-microscopic-proofs.tex`: 3560 LF, 0 CRLF).
LF was preserved. The instruction and the repository disagree; one of them should change.
