# Proposal 072-d1-heisenberg-wider-linearised, round 3

This is a minimal revision of r2 in response to `review-r2.md`. The review's only required finding is F1 (minor). The
full scan is complete: pass 1 is in `review-r2.md` and passes 2-4 are in `scan-pass-2.md`..`scan-pass-4.md`.

One change is made: the closing sentence of the insert. Everything else is unchanged from r2 and r1: the
mathematics, the scripts s1-s6, the rest of the insert text, the anchors, Edit 2, the target, the avenues and the
scope.

## Result

The result is unchanged from r2 and r1. It is a bounded no-gap result at tree level and linear order, on the null-leg
constant-connection Heisenberg family. Problems D, F and N stay OPEN.

## Target and status

Unchanged from r2:
- Problem D: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (ch17 D1).
- Dependencies: 068 and 071.

## Source reading

Digest + targeted reads. I read `scratch/digest.md` first. `make_digest.py --check` printed `DIGEST STALE (head
changed)`. The appH file hash recorded in the digest (`b98a3a34d2ac`) still matches the live file, so the anchor
region is unchanged.

Targeted reads:
- appH L1640-1647, the 071 closer. It already uses "the algebra \(\mathcal A\)" and the same
  non-identification with `ch:vierbein-emergence`.
- A grep for the label `ch:vierbein-emergence`.

## Research and reasoning

There is no new mathematics. F1 is correct. The non-identification with the emergent metric is not one of the
assumptions listed in the 071 paragraph, so "the assumptions listed in the preceding paragraph" does not cover it.
The r2 closer had dropped it. The F1 text restores it, together with "the algebra \(\mathcal A\)".

## Claim classification

Unchanged from r1 and r2. The closer is a scope statement and makes no claim.

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

There are two edits. Their anchors are identical to r2.

**Edit 1.**
- What is inserted: the block `appH_insert_r3.tex` (CRLF, 14 lines, 6463 bytes, sha256
  `b2fbd741df62cf9865a203f4cc60e1e26b349c2513a5f6ac8716eee5185f3fb9`), followed by one blank CRLF line.
- Where: immediately before the unique line `\section{Problem E: signature}` (live line 1648).
- Effect: the block sits directly after the 071 closing paragraph, which begins "These statements are for
  Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, the Lorentzian
  contraction, left-invariant backgrounds with constant connection".

**Exact diff of the block, r2 -> r3.** Only the last sentence changes. It sits on the last line of the block, in
the final paragraph. `make_insert_r3.py` asserts that this is the only difference; the check
`r2.replace(old, new) == r3` holds.

```diff
-Nothing here shows that the matrix integral selects this class or these backgrounds, so the assumptions listed in the preceding paragraph are not discharged; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
+Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), so the assumptions listed in the preceding paragraph are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

The new closing sentence is the F1 text, verbatim:

```latex
Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), so the assumptions listed in the preceding paragraph are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

**Edit 2.** Unchanged from r2. In the 071 closing paragraph (live line 1646), the unique string

```latex
Family (ii), its extension with \(\chi\neq0\) and the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and
```

becomes

```latex
Family (ii) and its extension with \(\chi\neq0\) are linearised in their Landau sectors in the following paragraph; the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and
```

**Checks on the block.**
- Labels referenced, with their definition counts across `chapters/*.tex`:
  - `eq:Smatrix`: defined once.
  - `ch:vierbein-emergence`: defined exactly once, at `chapters/ch04-vierbein-emergence.tex` line 2.
- The block adds no new labels and no citations. There is no bibliography change.
- The block still contains exactly one status sentence, in its last paragraph.

## Verification scripts

- `make_insert_r3.py` builds `appH_insert_r3.tex` from `appH_insert_r2.tex`, which is kept. It asserts:
  - the r2 sha256 `01b5d27a25bb8c19904ed13f26f29aae6b33d813bd66e11d3d63bbad01a42513`;
  - that the old closer occurs once and ends the block;
  - CRLF line endings and no BOM.

  Output: `make_insert_r3_output.txt`.
- `apply_and_build_r3.py` is `apply_and_build_r2.py` with the r3 file names and the new POST hash. Its anchors and
  Edit 2 are identical. It applies both edits in memory and asserts the pre and post hashes. With `--build` it
  builds in a temporary directory outside the repository (pdflatex, bibtex, pdflatex, pdflatex) and then deletes
  that directory. Output: `apply_and_build_r3_output.txt`.

### Reproduction pack

Command 1:

```
python -I -B make_insert_r3.py
```

Expected output:
- `replaced once: closer (F1)`
- `appH_insert_r3.tex bytes 6463 sha256 b2fbd741df62cf9865a203f4cc60e1e26b349c2513a5f6ac8716eee5185f3fb9 bare LF 0 lines 14`

Command 2:

```
python -I -B apply_and_build_r3.py --build
```

Expected output:
- `pre-hash matches expected: True`. The pre hash is `b98a3a34d2ac71800ceae7369db90d373d8bcdc139fe7fb81e7bad3e552df1c0`, 753095 bytes; it is the live hash.
- `appH post sha256 c8c07938df995ac1e6ebedc4e80bcc4ce43eaec9ec99c45696aad6474554ab52 bytes 759626 bare LF 0`
- `label ch:vierbein-emergence defined 1` and `label eq:Smatrix defined 1`
- `status sentences in block: 1 ; in last paragraph: True`
- Every pdflatex and bibtex step returns rc 0, and the final page count is 416.
- `undefined/multiply-defined warnings: 0` and `BUILD CLEAN`
- `temp copy removed: True`

## Decisions Taken

F1 is adopted verbatim. No other choice arises.

## Milestone assessment

Routine.

## Status-label recommendation

None. D, F and N remain OPEN and PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

Unchanged from r1 and r2.

## Special instructions for the gatekeeper

1. Re-verify the live pre hash `b98a3a34...` and the new post hash `c8c07938...`.
2. Confirm that the r2 -> r3 diff of the block is the single closing sentence above.
3. Confirm that nothing else changed relative to r2.
