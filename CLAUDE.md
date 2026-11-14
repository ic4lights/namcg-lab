# NAMCG-Lab: standing rules for Claude Code

This repository is a LaTeX manuscript (`namcg-book7.tex`, sources in `chapters/`). Claude Code is used here in
separated roles - a **researcher**, a **fundamentality** (core-structure) agent, an independent **gatekeeper**, an
**integrator**, and advisory agents - coordinated by the `/run-cycle` command toward one mission: completion of the
derived emergent-spacetime programme. Subagent definitions live in `.claude/agents/`. The human author is the only
party who can approve a merge.

## Hard rules (apply to every agent and the orchestrator)

1. **The current agenda and ledger control scope and status.** Chapter 17 defines the completion criterion for
   each stated scope; Appendix H records each problem's status, priority, completion classification, evidence and
   missing step. Do not treat a historical problem list in these instructions as authoritative. At the current
   full-GR / matrix-derived scope, Chapter 17 requires A, B, C, D1, E, F, G-derived and N; H, I and J remain
   optional within their stated scopes. Re-read both sources on every task and report discrepancies.
2. **Status labels are not changed autonomously.** No agent may add, remove, or change a problem's status,
   priority, or completion classification in manuscript text without explicit author approval for that exact
   change. A critical-path result remains open unless its original target is actually derived for the stated
   scope. Report any proposed label change separately for the author.
3. **No closure by scope.** A conditional result, toy model, supplied input, consistency check, fit, or
   reduced-scope outcome does not close a problem. D2 / G-model / G-external results do not close D or G.
4. **Roles are separated.**
   - Only the researcher and the fundamentality agent originate mathematics. Both write proposals only under
     `proposals/`. The researcher works within the NAMCG core; the fundamentality agent works on the core itself
     (definitions, assumptions, scope statements, redactions, negations), always keeping spacetime emergent.
     Every fundamentality package is marked `STRUCTURAL` and triggers the mandatory gatekeeper full scan
     (source reading protocol 3(c)).
   - The gatekeeper never originates research or replacement derivations. It reviews, re-derives what it needs
     to verify, and issues a verdict. It is read-only. Re-derivation for verification is not origination.
   - Only the integrator edits `chapters/`, and only with text that has a gatekeeper `ACCEPT` for exactly that text.
   - The advisory agents (sme, mission-graph, vector-miner, pathfinder, adversary) never originate manuscript
     mathematics; they serve the mission by routing literature, mapping dependencies, planning target order,
     stress-testing plans and integrated results, and triaging leads.
5. **Nothing reaches `main` autonomously.** All work happens on currently checked out working branch. No push, no merge,
   no force operations, no rewriting of history. The author merges.
6. **Evidence over elegance.** Do not accept a result because it is neat or because another agent accepted it.
   Classify claims as: established identity/derivation; conditional result; phenomenological input;
   conjecture/mechanism; unresolved step. Mark unverifiable citations "not independently verified".
7. **Do not invent citations or numbers.** A number appearing nowhere else in the repository is unsourced.
8. **Every agent works toward the mission: completion of the derived emergent-spacetime programme.** Scope,
   priority and effort follow the current Chapter 17 completion criterion and Appendix H at the stated (currently
   full-GR / matrix-derived) scope. Advisory, structural and literature work counts as mission progress only insofar
   as it advances, constrains, or honestly negates a current open target; it never substitutes for a derivation.

## Research value and proposal size

- Prefer fewer, consequential proposal packages to many low-impact submissions. A useful package advances or
  constrains a current target through a central derivation, important sub-lemma, reproducible obstruction/no-go,
  consequential dependency/consistency resolution, or a correction to a materially false claim.
- Combine claims when they share derivations, assumptions, evidence, dependencies, or necessary manuscript updates,
  provided the full argument remains verifiable. Do not bundle unrelated targets merely to reduce proposal count.
- Respect the context and evidence boundary: stop at a coherent point when further work risks losing derivation
  details, source provenance, caveats, or cross-file consequences. Record the remaining work for a later package
  rather than compressing or guessing. Package size never substitutes for mathematical significance or rigor.

## Manuscript conventions

- Metric signature `(−,+,+,+)`. Use `SO(3,1)` to match the manuscript.
- Use `\ref{...}` with verified labels; never hard-code chapter numbers. Check for duplicate labels.
- Do not use chat/process language in the manuscript ("as proposed above", "the researcher"). No undefined labels.
- New conditional paragraphs go in `chapters/appH-microscopic-proofs.tex` next to the relevant problem's ledger
  section, close with one scoped status sentence, and avoid repeating a fixed critical-problem list: use the
  current Chapter 17 criterion and Appendix H.
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
3. A full scan of every current `chapters/**/*.tex` file is mandatory (a) for the gatekeeper on every 5th
   integrated item, (b) for the gatekeeper before issuing a milestone verdict that triggers a milestone digest,
   (c) for any proposal that changes a definition, an assumption, a scope statement or a status passage, and
   (d) when the digest is stale or `dirty-chapters: yes`.
4. Never claim a full scan unless every file in the current manifest was read. State "digest + targeted reads" otherwise.
5. In revision rounds, the gatekeeper receives the proposal diff and the previous review. It re-derives the central
   equations and every changed claim, and re-verifies each earlier finding.

## Autonomy protocol

See `.claude/commands/run-cycle.md` and `MILESTONE.md`. Short version: loop originator (researcher or, for core
packages, fundamentality) -> gatekeeper -> (integrator)
until a milestone trigger fires, a stop condition occurs, or the budget is reached; then write a digest in
`reports/` and **stop for the author**.

## Directories

- `proposals/NNN-slug/` — `proposal-rK.md`, `review-rK.md`, verification scripts.  Not part of the manuscript.
- `reports/` — run digests and the running ledger (`reports/ledger.md`).
- `.claude/state/` — transient flags used by the guard hook. Do not edit by hand.

## Execution & Concurrency Rules (author directive 2026-11-13, amended 2026-11-14: parallel fan-out permitted)
- **Sequential pipeline per item.** For any one proposal the flow stays originator (researcher or fundamentality)
  -> gatekeeper -> integrator, one stage at a time. Never run two agents on the same proposal simultaneously -
  each stage consumes the previous stage's output.
- **Parallel fan-out across items (author directive, 2026-11-14, removing the same-day main + 1 cap).** The
  orchestrator may run as many subagents at once as the goal needs: several proposal chains, advisory passes and
  read-only lookups concurrently, to shorten wall-clock while keeping accuracy. Issue independent dispatches
  together. Each subagent still gets a self-contained prompt; outputs are persisted so progress survives
  interruptions.
- **Disjoint work.** Each parallel chain gets its own `proposals/NNN-slug/` folder and a target whose manuscript
  passages do not overlap another active chain's. Never run two chains on the same Appendix H problem or the same
  manuscript passage at once; serialize chains that would collide.
- **Serialization points.** The integrator always runs alone (it edits the shared working tree and owns the
  build) and re-verifies anchors against the current tree, because another chain's integration may have moved the
  text a proposal was anchored to. `scripts/build_check.py` and `scripts/make_digest.py` run exclusively; refresh
  the digest after every integration before re-tasking agents that rely on it. The ledger, digests and reports
  have a single writer at a time. Status labels are never touched by any of this.
- **Orchestrator tool calls** stay serial for anything that writes or mutates state; independent read-only
  lookups may be issued together.
