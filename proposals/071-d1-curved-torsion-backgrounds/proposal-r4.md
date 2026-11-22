# Proposal 071-d1-curved-torsion-backgrounds, round 4

## Result

Round 4 is a minimal revision. It addresses the one required finding of `review-r3.md` (finding 1, minor). No mathematics changed. Every r3 file is kept unchanged, including `appH_insert_r3.tex` (sha256 `c0ff0f79...a19dc`, re-verified). The results, scripts, classification and scope of `proposal-r3.md` (and through it `proposal-r2.md`) stand as recorded there.

- **Finding 1 (minor, REQUIRED).** The phrase `and no value \(q^2=-m^2\) with \(m\neq0\) is isolated` used `m`, which is also the connection vector of family (i). It is replaced verbatim by `and no nonzero value of \(q^2\) is isolated`. The phrase occurred once, and `make_insert_r4.py` asserts this.
- **Finding 2 (informational).** No change. The insert defines its own `k=(1,0,1,0)`, as the review notes.

The new wording is still true, and slightly stronger. The preceding clause already states that the set of values of `q^2` on the cone is invariant under multiplication by every positive number. So any nonzero value `v` in the set comes with the whole open ray `{t v : t > 0}`, and `v` is not isolated. This holds for either sign of `v`. The old phrase covered only `v = -m^2 < 0`. The conclusion drawn from it ("do not produce a mass") is unchanged.

D, F and N remain OPEN and PROGRAMME-CONDITIONAL.

## Target and status

Unchanged from r3. Problem D (D1 route) is OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL, and the item attacked is "torsion or propagating modes". D1 supplies operators to F, and F gates N. No discrepancy was found.

## Source reading

- **Mode:** digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT`, and `scratch/digest.md` was read first.
- **Full scan:** the gatekeeper has completed it (pass 1 in `review-r3.md`, passes 2-4 in `scan-pass-2..4.md`). This round changes one phrase of the insert and no definition, assumption, scope statement or status passage.
- **Live appH sha256:** `d8d8b678fa0ceabe03f3f9c2f56cc60dbe140aa845658beddb0c206ba26c9180`. This was verified with `sha256sum` and by the apply script (`pre-hash matches expected: True`).

## Research and reasoning

See the argument under Result. No other reasoning changed.

## Claim classification

Unchanged from r3. The changed sentence is part of the established derivation that family (i) has no mass shell. It follows from the stated invariance of the cone under `q -> e^{±θ} Λ_θ q`.

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`.

- **Anchors:** identical to r3.
  - **Insert.** `appH_insert_r4.tex` is inserted, plus one blank CRLF line, immediately before the unique line `\section{Problem E: signature}` (L1631). The insert follows the 068 paragraph that ends "Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL."
  - **Edit E (L1623).** In the paragraph beginning "The null-rotation algebra solves the equation", the unique string `has the same torsion for \(\vartheta=-\tfrac12\), with` becomes `has the same torsion for \(\vartheta=\tfrac12\), with`.
- **What is kept:** all other text.

The exact diff of the insert, r3 to r4, is one line (insert line 14) and one phrase:

```diff
-... under multiplication by every positive number, and no value \(q^2=-m^2\) with \(m\neq0\) is isolated. So on family (i) ...
+... under multiplication by every positive number, and no nonzero value of \(q^2\) is isolated. So on family (i) ...
```

The full sentence after the change reads:

```latex
invariant under \(q\mapsto\mathrm e^{\pm\theta}\Lambda_\theta q\), with \(\Lambda_\theta\) the boost and the sign fixed by the action on covectors, so the set of values of \(q^2\) on it is invariant under multiplication by every positive number, and no nonzero value of \(q^2\) is isolated.
```

The insert has no other change: `make_insert_r4.py` prints `differs from appH_insert_r3.tex only by Q: True`. Edit E is unchanged from r3.

- **Labels and citations:** no label or citation is added or changed, and no bibliography change is needed.
- **Status sentences:** the insert has one, in its last paragraph, as in r3.

## Verification scripts

| command (from this folder) | checks | expected invariant output |
|---|---|---|
| `python -I make_insert_r4.py` | builds the r4 insert: r2 plus H, SC2 and Q | `replacement H applied once`; `replacement SC2 applied once`; `replacement Q applied once`; `old parameter-a patterns remaining: 0`; `\chi occurrences in insert: 8`; `q^2=-m^2 occurrences remaining: 0`; `differs from appH_insert_r3.tex only by Q: True`; `appH_insert_r4.tex bytes 9302 sha256 75da43f08edf2dac999876732beceaf052c6f1c425cb1475229d086f102b502b bare LF 0` (`make_insert_r4_output.txt`) |
| `python -I apply_and_build_r4.py --build` | applies the change to a temp copy outside the repo, then builds it | `pre-hash matches expected: True`; `anchor unique: True; offset 277558 line 1631`; `E anchor unique: True; line 1623`; block sha `75da43f0...502b`, 9302 bytes; `appH post sha256 b98a3a34d2ac71800ceae7369db90d373d8bcdc139fe7fb81e7bad3e552df1c0 bytes 753095 bare LF 0`; 7 labels each defined once; pdflatex 399 → bibtex → 414 → 414 pages; `undefined/multiply-defined warnings: 0`; `BUILD CLEAN`; `temp copy removed: True` (`apply_and_build_r4_output.txt`) |

`apply_and_build_r4.py` is `apply_and_build_r3.py` with only these changes: the insert file name, the pinned POST hash, the temp-directory prefix and the docstring. The anchors and the edit-E strings are identical. The other scripts are unaffected and were not re-run.

## Decisions Taken

None new. Finding 1's snippet was applied verbatim.

## Milestone assessment

Routine.

## Status-label recommendation

None. D, F and N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

Unchanged from r3 (see `proposal-r3.md`, "Remaining open step", and its ranked avenues).

## Special instructions for the gatekeeper

- **Diff.** Confirm that the insert differs from r3 only by finding 1's phrase.
- **Hashes.**
  - Pre: `d8d8b678…9180`, which is live.
  - Block: `75da43f0…502b`.
  - Post: `b98a3a34d2ac71800ceae7369db90d373d8bcdc139fe7fb81e7bad3e552df1c0` (753095 bytes).
- **Unchanged.** Edit E and all anchors are unchanged.
- **Scope of changes.** No file outside this folder was changed. The build ran in a temp directory outside the repository, which was removed afterwards.
