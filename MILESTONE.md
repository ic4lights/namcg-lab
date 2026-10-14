# Milestone triggers and stop conditions

The autonomous loop (`/run-cycle`) keeps going through routine accepted items. It **stops and writes a digest for
the author** when any of the following occurs.

## Milestone triggers (significant progress)

A gatekeeper-accepted item counts as a milestone if it does at least one of:

1. Derives (not assumes) one of the "remaining steps" listed in the Appendix H ledger for B, C, D, F or G, for
   example: a matrix-to-frame map for D, a derived local Lorentz transformation law, connection dynamics, a
   resolution of the D↔F circularity, the scaffold-to-emergent-metric map for B, a derived boundary-to-bulk
   conversion factor for G, or the full coupled gauge-fixed scalar–tensor operator for C.
2. Establishes a new **no-go result** that rules out a class of routes the manuscript currently keeps open.
3. Finds that an **already merged or accepted claim is wrong** (error in a merged paragraph, a sign/factor error,
   a false implication). This stops the loop immediately, regardless of other progress.
4. Proposes a **status-label change** for any of B, C, D, F, G (never applied autonomously).
5. Proposes a **structural change to the NAMCG core** or a scope change that makes a critical-path dependency
   optional (needs an author decision on alternatives).

Routine items that are NOT milestones: consistency checks, toy-model calculations, restatements with sharper
scope, dimensional or sign corrections to non-load-bearing text, bookkeeping.

## Stop conditions (non-milestone)

- `ACCEPTED_BATCH_LIMIT` accepted-and-integrated items since the run began (default 5).
- `MAX_ROUNDS` researcher/gatekeeper revision rounds on one item without `ACCEPT` (default 4). Record the
  item as stalled; if two consecutive items stall, stop.
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
5. Current status of B, C, D, F, G (must still read OPEN unless the author changes it).
6. Items stalled or rejected, with the gatekeeper's smallest-correction notes.
7. Build result (page count, undefined references = 0, `git diff --check` clean).
8. What the author should do: review the branch diff, merge or discard, and the suggested next target.
