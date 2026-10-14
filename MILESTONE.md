# Milestone triggers and stop conditions

The autonomous loop (`/run-cycle`) keeps going through routine accepted items. It **stops and writes a digest for
the author** when any of the following occurs.

## Milestone triggers (significant progress)

A gatekeeper-accepted item counts as a milestone if it does at least one of:

1. Derives (not assumes) an important remaining step for a problem required by the current Chapter 17 completion
   criterion and recorded in Appendix H, for example: the matrix-to-dictionary map (A), fixed-volume
   tensor-block stationarity (B), the scalar–tensor operator (C), matrix-derived local Lorentz/frame dynamics
   (D1), Lorentzian signature (E), specified heat-kernel coefficients (F), matrix-derived entropy/stationarity
   (G-derived), or effective-expansion/low-energy pole control (N). Re-read the current agenda and ledger; this
   list is illustrative, not exhaustive or permanent.
2. Establishes a new **no-go result** that rules out a class of routes the manuscript currently keeps open.
3. Finds that an **already merged or accepted claim is wrong** (error in a merged paragraph, a sign/factor error,
   a false implication). This stops the loop immediately, regardless of other progress.
4. Proposes any **status, priority, or completion-classification change** in the agenda or ledger (never applied
   autonomously; includes adding a new tracked problem or changing the current critical-path set).
5. Proposes a **structural change to the NAMCG core** or a scope change that makes a critical-path dependency
   optional (needs an author decision on alternatives).

Routine items that are NOT milestones: consistency checks, toy-model calculations, restatements with sharper
scope, dimensional or sign corrections to non-load-bearing text, bookkeeping.

## Stop conditions (non-milestone)

- `ACCEPTED_BATCH_LIMIT` accepted-and-integrated proposal packages since the run began (default 1, matching
  `/run-cycle`; increase only when the author requests multiple packages).
- `MAX_ROUNDS` researcher/gatekeeper revision rounds on one item without `ACCEPT` (default 4), extendable by up to 4
  more rounds (hard max 8) only while the gatekeeper's `PROGRESS` is `improving` (see `/run-cycle` step d); stop
  early after two consecutive `flat`/`regressing` reviews. Record the extension reason and rounds used per item in
  the ledger and digest. Record the item as stalled when the cap is reached; if two consecutive items stall, stop.
- The gatekeeper returns `NEEDS EVIDENCE` that needs the author (data, an external reference you must supply).
- A choice among materially different designs where the author's preference matters.
- Pre-flight failures: dirty `chapters/`, on `main`, build already broken, tools missing.
- Build fails after an integration (revert the integration commit on the branch, report, stop).
- Wall-clock / turn budget exhausted.

## What the digest must contain (`reports/run-<timestamp>.md`)

1. Branch name, base commit, final commit, `git log --oneline` of the run.
2. For each item: target problem, claim, verdict history, what is proved, what is conditional, what remains.
3. Milestone triggered (which trigger and why) or the stop reason.
4. Any proposed status-label change, clearly separated, with the evidence that would justify it.
5. Current status, priority and completion classification of every problem in the current Chapter 17 completion
   criterion, cross-checked against Appendix H. Do not substitute a fixed historical list.
6. Items stalled or rejected, with the gatekeeper's smallest-correction notes.
7. Build result (page count, undefined references = 0, `git diff --check` clean).
8. What the author should do: review the branch diff, merge or discard, and the suggested next target.
