# NAMCG-Lab: standing rules for Claude Code

This repository is a LaTeX manuscript (`namcg-book7.tex`, sources in `chapters/`). Claude Code is used here in two
separated roles, a **researcher** and an independent **gatekeeper**, coordinated by the `/run-cycle` command.
Subagent definitions live in `.claude/agents/`. The human author is the only party who can approve a merge.

## Hard rules (apply to every agent and the orchestrator)

1. **Status labels are frozen.** Problems B, C, D, F, G stay `OPEN — CRITICAL PATH — PROGRAMME-CONDITIONAL`
   unless the original matrix-derived target is actually derived. Changing, removing or adding a status label,
   or writing "closed/solved/derived" about one of these problems, is never done autonomously. Propose it in the
   report for the author instead.
2. **No closure by scope.** A conditional result, toy model, supplied input, consistency check, fit, or
   reduced-scope outcome does not close a problem. D2 / G-model / G-external results do not close D or G.
3. **Roles are separated.**
   - Only the researcher originates mathematics. It writes proposals only under `proposals/`.
   - The gatekeeper never originates research or replacement derivations. It reviews, re-derives what it needs
     to verify, and issues a verdict. It is read-only.
   - Only the integrator edits `chapters/`, and only with text that has a gatekeeper `ACCEPT` for exactly that text.
4. **Nothing reaches `main` autonomously.** All work happens on a branch `auto/<YYYYMMDD-HHMM>`. No push, no merge,
   no force operations, no rewriting of history. The author merges.
5. **Evidence over elegance.** Do not accept a result because it is neat or because another agent accepted it.
   Classify claims as: established identity/derivation; conditional result; phenomenological input;
   conjecture/mechanism; unresolved step. Mark unverifiable citations "not independently verified".
6. **Do not invent citations or numbers.** A number appearing nowhere else in the repository is unsourced.

## Manuscript conventions

- Metric signature `(−,+,+,+)`. Use `SO(3,1)` to match the manuscript.
- Use `\ref{...}` with verified labels; never hard-code chapter numbers. Check for duplicate labels.
- Do not use chat/process language in the manuscript ("as proposed above", "the researcher"). No undefined labels.
- New conditional paragraphs go in `chapters/appH-microscopic-proofs.tex` next to the relevant problem's ledger
  section, close with one scoped status sentence, and avoid repeating "Problems~B, C, D, F and~G remain open." on
  consecutive paragraphs: keep one such line per contiguous block.
- `.tex` files use CRLF line endings. Preserve them. Write UTF-8 without BOM.
- A change must be the smallest text that accurately records the result.

## Build and verification

- Use `python scripts/build_check.py`. It runs two `pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex`
  passes, scans the log for undefined or multiply-defined references, restores the tracked PDF with
  `git restore -- namcg-book7.pdf`, and runs `git diff --check`. `latexmk` is known to fail here.
- Keep sympy/Python verification scripts under `scratch/` (git-ignored) or inside the proposal folder so the
  gatekeeper can re-run them. Symbolic output is a check, not a proof.

## Mandatory source scan

Every subagent starts with an empty context, so each must do its own scan: enumerate `chapters/**/*.tex`, read
every file completely (successive `view_range`/offset reads for large files), and record the manifest, `HEAD`
hash, and whether `git status --porcelain -- chapters` is clean. Never claim coverage that was not completed.
Read `appH-microscopic-proofs.tex` and `ch17-agenda.tex` with particular care.

## Autonomy protocol

See `.claude/commands/run-cycle.md` and `MILESTONE.md`. Short version: loop researcher -> gatekeeper -> (integrator)
until a milestone trigger fires, a stop condition occurs, or the budget is reached; then write a digest in
`reports/` and **stop for the author**.

## Directories

- `proposals/NNN-slug/` — `proposal-rK.md`, `review-rK.md`, verification scripts.  Not part of the manuscript.
- `reports/` — run digests and the running ledger (`reports/ledger.md`).
- `.claude/state/` — transient flags used by the guard hook. Do not edit by hand.
