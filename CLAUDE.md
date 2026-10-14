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

## Source reading (token-efficient protocol)

1. The orchestrator runs `python scripts/make_digest.py` once per run and again after every integration.
   `python scripts/make_digest.py --check` must print `DIGEST CURRENT` before a subagent relies on it.
2. Each subagent reads `scratch/digest.md` first, then reads IN FULL: the Problem entry in
   `chapters/appH-microscopic-proofs.tex`, the matching passage in `chapters/ch17-agenda.tex`, every passage it
   cites, edits or relies on, and every definition, assumption and label it uses (grep the digest, then view ranges).
3. A FULL 30-file scan is mandatory (a) for the gatekeeper on every 5th integrated item, (b) for the gatekeeper
   before issuing a milestone verdict that triggers a milestone digest, (c) for any proposal that changes a
   definition, an assumption, a scope statement or a status passage, and (d) when the digest is stale or
   `dirty-chapters: yes`.
4. Never claim a full scan unless it was done. State "digest + targeted reads" otherwise.
5. In revision rounds, the gatekeeper receives the proposal diff and the previous review. It re-derives the central
   equations and every changed claim, and re-verifies each earlier finding.

## Autonomy protocol

See `.claude/commands/run-cycle.md` and `MILESTONE.md`. Short version: loop researcher -> gatekeeper -> (integrator)
until a milestone trigger fires, a stop condition occurs, or the budget is reached; then write a digest in
`reports/` and **stop for the author**.

## Directories

- `proposals/NNN-slug/` — `proposal-rK.md`, `review-rK.md`, verification scripts.  Not part of the manuscript.
- `reports/` — run digests and the running ledger (`reports/ledger.md`).
- `.claude/state/` — transient flags used by the guard hook. Do not edit by hand.
