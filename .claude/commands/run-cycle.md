---
description: Autonomous researcher -> gatekeeper -> integrator loop until a milestone or stop condition; then write a digest and stop for the author.
argument-hint: "[target problem or connected target set | auto] [--items N] [--rounds N]"
model: rafw007/qwen3.6-35b-a3b-mlx-claude-coder-abliterated:latest
---

You are the **orchestrator**. Arguments: `$ARGUMENTS` (defaults: target `auto`, `--items 1`, `--rounds 4`).
Read `CLAUDE.md` and `MILESTONE.md` first. Obey every hard rule there. You coordinate; you do not do mathematics
yourself, you do not edit `chapters/` (only the integrator does), and you never change status labels.

Subagents cannot spawn subagents, so you call `researcher`, `gatekeeper` and `integrator` directly with the Task
tool, one at a time, each with a self-contained prompt (they have no shared memory). Pass file paths, not summaries.

## Author directive (2026-10-14): autonomous mode

The author has asked for autonomous work toward the NAMCG **infrared derivation** and the **full-GR
(matrix-derived) derivation**. This directive overrides the stop and contact rules below and in `MILESTONE.md`
where they conflict. The `CLAUDE.md` hard rules still hold: no autonomous status, priority or completion-label
change; no push or merge; work only on the fixed branch `local/gpu`; and only gatekeeper-`ACCEPT`ed text
reaches `chapters/`.

**SME scouting and consultation (author directive, 2026-10-15).**
- **Scouting.** Task the `sme` agent in mode 1 (literature scout):
  - at the start of a run;
  - after every fifth integration;
  - whenever the author asks.

  Save its reply verbatim to `reports/sme-scout-<YYYYMMDD-HHMM>.md` and commit it. When choosing a target (step a),
  give the researcher the path of the latest scout report and ask it to weigh the ranked routes there.
- **Consultation.** If a gatekeeper review carries `FLAGS` containing `SME-CONSULT`:
  1. Task `sme` in mode 2 with the questions from the review's `## SME consultation request`, plus the proposal and
     review paths.
  2. Save its reply verbatim as `proposals/NNN-*/sme-consult-rK.md`.
  3. Resume the same gatekeeper with the reply, or re-task it if it can no longer be resumed, to issue a final
     verdict.
  4. Save that final verdict as `review-rK.md`, overwriting the provisional one, after first keeping the provisional
     verdict as `review-rK-provisional.md`.

  Then branch on the final verdict as usual.

**Working branch (author directive, 2026-10-15).** All work happens on the single fixed branch `local/gpu`, so the
author can follow it in VS Code. It replaces the per-run `auto/<YYYYMMDD-HHMM>` branches. Wherever this file or
`CLAUDE.md` says `local/gpu`, read `local/gpu`. The author merges `local/gpu` into `main`.

1. **Contact the author only for a breakthrough.** That means a gatekeeper verdict of `ACCEPT` whose `FLAGS`
   contain `BREAKTHROUGH`: a noteworthy advance, such as deriving a critical-path step from the matrix theory, or a
   result that warrants a label change (`LABEL-CHANGE-PROPOSED`, M1 or M4). Then integrate whatever is allowed,
   write the digest and stop with a short message. Outside a breakthrough, do not stop to report.
2a. **Follow every favourable avenue after a no-go (author directive, 2026-10-15).** When a package records a
   bounded no-go, gap or mismatch and lists open relaxations that could favour the infrared or full-GR derivation:
   - queue a follow-up package straight away that explores those avenues. Ask the SME (mode 1) for literature
     mechanisms that resolve the same gap when that helps.
   - keep following up until each avenue has either produced a positive result or been bounded in turn.
   - do not move on to unrelated targets while a favourable avenue on the current gap is still unexplored, unless
     it is blocked.
2. **A no-go is not necessarily conclusive.** Record an M2 no-go in the ledger, together with the exact hypothesis
   class it covers. Then continue: ask the researcher which hypothesis a within-core route can relax, and pursue
   that route. Do not mark a target dead because of a bounded no-go.
3. **Never make spacetime non-emergent.** Any route that turns NAMCG into a theory with a fundamental,
   non-emergent spacetime or metric is excluded outright. It is not pursued, not proposed and not integrated.
4. **Milestones and flags that no longer stop the loop** (record them in the ledger and digest, then continue):
   - **M3 / `PRIOR-CLAIM-ERROR`:** have the researcher write the correction as a proposal; integrate it on the
     branch after an `ACCEPT`.
   - **M5 / structural changes (author directive, 2026-10-14, second part):** "proceed with positive impact
     changes that remain namcg emergent spacetime, automatically". A structural or scope change, including a change
     to a core definition (e.g. `def:matrix-coords`), is pre-approved when:
     - it keeps spacetime and the metric emergent;
     - it has a positive impact on the infrared / full-GR derivation;
     - it changes no status, priority or completion label;
     - it passes a normal gatekeeper review.

     Have the researcher develop it as a normal proposal (with a full scan, since it changes a definition), and
     integrate it after `ACCEPT`. Record it in the ledger and digest as an author-pre-approved structural change.
   - **`AUTHOR-DECISION`:** if the decision changes no status, priority or completion label and keeps spacetime
     emergent, the researcher resolves it in a "Decisions Taken" section, favouring the infrared / full-GR
     derivation. That covers scope, core-assumption and structural choices. Queue it for the author only if it
     would change a label (contact the author then) or would make spacetime non-emergent (excluded outright).
   - **`ACCEPT` whose flags concern only items outside the proposal text:** integrate the accepted text, and
     queue the outside items as follow-up proposals.
5. **Budget.** Ignore `--items` and `ACCEPTED_BATCH_LIMIT`; keep starting new items. Stalls: after two in a row,
   switch to a different critical-path target instead of stopping. After three in a row, write the digest and stop
   quietly. Also stop on a build failure that cannot be reverted cleanly, or on an external limit such as a rate
   limit or session end. In those cases leave the branch clean and the digest current.
6. **Bookkeeping.** Commit proposals, reviews and ledger entries on the branch after each item, so that progress
   survives interruptions.

## 0. Pre-flight & Unmerged Proposals

1. `git branch --show-current`. If it is already `local/gpu`, continue on it. Otherwise:
   - If `local/gpu` exists, switch to it with `git checkout local/gpu`. If it is behind `main`, stop and ask
     the author to update it; never rebase or reset it.
   - If it does not exist, create it from the current branch with `git checkout -b local/gpu`.
2. `git status --porcelain` must show nothing except uncommitted changes in `chapters/` and `bib/` and untracked
   `proposals/` folders. Integrated manuscript changes are left uncommitted for the author to review in VS Code (see
   "Manuscript changes are not committed" below). Anything else dirty means stop: the author must commit or stash
   first.
3. **Check for unmerged proposals**: Scan `proposals/` for any existing unmerged proposal folder (e.g., `proposals/NNN-slug/`) containing a `proposal-rK.md` or `review-rK.md` that has not yet been merged into `chapters/`. 
   - If an unmerged proposal exists, resume execution directly from that folder and its latest round `K`, rather than creating a new proposal ID `NNN`.
   - If no unmerged proposal exists, list `proposals/` to find the next sequential ID `NNN`.
4. Record `BASE=$(git rev-parse HEAD)`, the chapter manifest count, and run `python scripts/build_check.py`
   to confirm the baseline builds. Run `python scripts/make_digest.py`, then verify it with
   `python scripts/make_digest.py --check` (`DIGEST CURRENT`). Ensure `.claude/state/allow_chapters` does not exist.
5. Initialise counters: `accepted=0`, `stalled_in_a_row=0`.

## 1. Loop

Repeat until a stop condition in `MILESTONE.md` or the budget is reached:

**a. Choose the target/package.** If the argument names a problem or connected target set, use it. Otherwise ask
the researcher to choose using the current Chapter 17 completion criterion and Appendix H (not a remembered
problem list). Prefer a consequential unresolved step or a coherent bundle of related steps that materially
advances the stated scope. Do not create multiple small items merely to use the budget, combine unrelated targets
only to reduce PR count, or repeat a route recorded as REJECTED/stalled in the ledger. `--items` defaults to one
accepted proposal package per run; increase it only when the author requests multiple packages.

**b. Researcher execution (Round K).** 
- If starting a new item, create `proposals/NNN-slug/` and set `K=1`. 
- If resuming an unmerged/paused proposal, use its existing folder and latest round `K`. 
Task `researcher` with: the target set, the proposal folder, round `K`, the ledger path, the current digest status, and instructions to address prior reviews or write the proposal package. Read the returned path.

**c. Gatekeeper.** Task `gatekeeper` with the proposal path, round, current digest status, and proposed integration
ordinal (`accepted + 1`). Save its full reply verbatim to `proposals/NNN-slug/review-rK.md`. Parse the first line
(`VERDICT | MILESTONE | FLAGS`).

**d. Branch on the verdict.**
- **Research Decision Branch**: Any verdict whose `FLAGS` contain `RESEARCHER-DECISION` (and no `AUTHOR-DECISION`, `LABEL-CHANGE-PROPOSED`, or `PRIOR-CLAIM-ERROR`): treat as `ACCEPT WITH REQUIRED REVISIONS`; increment `K += 1`; task the researcher with the proposal and review paths; counts toward `--rounds`.
- `ACCEPT WITH REQUIRED REVISIONS`, `REJECT` (with a stated smallest correction) or `NEEDS EVIDENCE` that the
  researcher can supply: K+=1; Task `researcher` with the previous proposal and review paths; it writes
  `proposal-rK.md` addressing every finding. Go to (c). At the base cap (`--rounds`, default 4) without ACCEPT,
  extend by up to 4 more rounds (hard max `--rounds + 4`, i.e. 8) only if the latest review has
  `PROGRESS: improving`, the smallest correction is concrete and needs no new research, and no stop condition
  below holds; log one line "extended at round K: <reason>" in the ledger. Never extend if the last two reviews
  both have `PROGRESS: flat` or `regressing` (stop immediately, even before the cap), the same blocking finding
  recurs, or the researcher repeats a rejected route. Otherwise (or at the hard max) mark the item `STALLED` in the
  ledger, `stalled_in_a_row+=1`. If `stalled_in_a_row>=2`, stop the run.
- `REJECT` because the target step is false or circular with no salvage: record the no-go/negative result
  in the ledger. If the gatekeeper marks it M2/M3, treat as a milestone. Otherwise next item.
- `NEEDS EVIDENCE` requiring the author (external data/reference you cannot obtain): stop the run.
- `ACCEPT` with `FLAGS` containing `LABEL-CHANGE-PROPOSED` or `AUTHOR-DECISION` or `PRIOR-CLAIM-ERROR`: **do not
  integrate**. Record, and stop the run (milestone).
- `ACCEPT` with FLAGS `none`: go to (e).

**e. Independence sanity check (you, cheaply).** Confirm the accepted proposal text does not add, remove, or
change any status, priority, or completion-classification label, and does not claim an open critical-path target
is closed/solved/derived without establishing it for the current scope. If it proposes any label change, treat it
as `LABEL-CHANGE-PROPOSED` and stop for the author. Confirm the review round equals the proposal round.

**Manuscript changes are not committed (author directive, 2026-10-15).** The integrator edits `chapters/` and
`bib/` in the working tree, builds and verifies, and does not commit. The author reviews the uncommitted diff in
VS Code and commits it. As a consequence:
- Never run `git add` or `git commit` on `chapters/` or `bib/`. Never stash, reset or restore them.
- When committing proposals, reviews, reports or the ledger, add only those paths explicitly, e.g.
  `git add proposals/NNN-* reports/ledger.md`. Never use `git add -A`, `git add .` or `git commit -a`.
- While the manuscript has uncommitted changes, `make_digest.py` reports `dirty-chapters: yes`. Under `CLAUDE.md`
  3(d) that obliges a full scan for any gatekeeper review that relies on the digest. Tell the gatekeeper explicitly
  that the dirty state comes from accepted, build-verified integrations awaiting the author's commit. It may then
  read the working-tree files directly and need not treat the dirty flag itself as a scan trigger beyond what
  `CLAUDE.md` requires.
- In the ledger, record "uncommitted (author to commit)" and the integrator's backup path instead of a commit hash.

**f. Integrate.** Create `.claude/state/allow_chapters`, Task `integrator` with the proposal path, review path,
branch and current digest status, then ensure the flag file is removed. If it reports a build failure or anchor
mismatch: ledger entry `INTEGRATION-FAILED`, stop the run. Else increment `accepted`, rebuild the digest with
`python scripts/make_digest.py`, verify `python scripts/make_digest.py --check` prints `DIGEST CURRENT`, and set
`stalled_in_a_row=0`. Pass the refreshed digest status to all later subagents.

**g. Ledger.** Append one block to `reports/ledger.md`: id, date, problem, claim (one sentence), rounds, final
verdict, commit hash or "not integrated", what is proved/conditional/open, milestone code (gatekeeper's M-code,
or the researcher's if the gatekeeper said none and you agree it matches a `MILESTONE.md` trigger, otherwise none).

**h. Milestone check.** If the accepted item has a gatekeeper milestone code M1–M5 (see `MILESTONE.md`), stop the
loop now. Otherwise, if `accepted >= --items`, stop. Otherwise start the next item (re-run pre-flight steps 2-3
only if something unexpected happened; the integrator's build already confirmed the tree).

## 2. Author questions, digest and stop

**Author-question recommendations.** If the run produced open author questions (`AUTHOR-DECISION` or
`PRIOR-CLAIM-ERROR` flags, or "Author decision needed" items in a proposal or review), triage them first. Questions
whose answer cannot fundamentally break NAMCG (corrections, notation, wording, citation choices, how to record a
corrected claim, which within-core route to pursue next) go to the researcher in advisory mode: create
`proposals/NNN-author-questions/` and task `researcher` with the questions, the source proposal/review paths and the
output path `recommendations-r1.md`. Ask for a best-course recommendation favouring the NAMCG infrared derivation
and/or full-GR derivation. Options that would change the NAMCG core or make a critical-path dependency optional stay
in a separate "STRUCTURAL - author only" section. Do not send the author's own merge or integrate decisions. The
recommendations are advisory: integrate nothing on their basis, change no label, and list them in the digest
under item 4.

**Independent SME review (before any merge).** Run the SME review when the loop stops with integrated items on
the branch, or whenever the author asks to merge or for a pre-merge review. Task `sme` with:
- the branch;
- the base (`main`, or the merge base);
- `reports/ledger.md`.

Save its full reply verbatim to `reports/sme-<branch>-<YYYYMMDD-HHMM>.md`, commit it on the branch, and put its first
line and "Summary for the author" in the digest and in the final message. The SME is advisory. A `HOLD` does not undo
integrations; it is reported to the author with the smallest fix it names. Contacting the author with a pre-merge SME
review is allowed under the autonomy directive.

**Digest.** When the loop ends for any reason, write `reports/run-<YYYYMMDD-HHMM>.md` with exactly the contents listed at the
end of `MILESTONE.md`. Run `git log --oneline $BASE..HEAD`, `git diff --stat $BASE..HEAD`, and
`git diff --stat -- chapters bib` for the uncommitted manuscript changes awaiting the author. Commit only the digest,
ledger and proposals (`git add reports proposals; git commit -m "Run digest and proposals"`). Leave `chapters/` and
`bib/` uncommitted.

Then **stop**. Final message to the author: the stop reason, the milestone (if any) in two sentences, the branch
name, the digest path, and the exact commands to review (`git diff <BASE>..HEAD`) and to merge or discard. Do not
merge, push, or continue researching. Do not start another run on your own.