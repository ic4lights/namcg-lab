# Proposal 069-f-nonderivative-sector, round 3

This round only changes wording. It adds no mathematics and changes no claim, value or label. Every section that
is not restated below is identical to `proposal-r2.md`: Research and reasoning, Claim classification, the
mathematics of E7, Milestone assessment, Remaining open step and the avenue ranking.

## Result
The result is unchanged from r2. This round folds in the three required wording fixes from the gatekeeper's full scan
(`scan-pass-2.md`). It also adopts the optional wording from `scan-pass-3.md`.

## Target and status
Unchanged from r2. Problem F stays OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL, and so do C and N. No label is
changed.

## Source reading
Digest + targeted reads. `make_digest.py --check` printed `DIGEST CURRENT`. Reads in this round:
- appH L3000 and L3002 (the live text);
- ch03 L136-186 (`eq:Smatrix`, `def:matrix-coords-ext`);
- `scan-pass-1..4.md`;
- `review-r2.md`.

The gatekeeper's full scan (passes 1-4) covers the package.

## Proposed changes (exact diffs from r2)
The target is still `chapters/appH-microscopic-proofs.tex`, in the paragraph "Conjugate-coordinate class times a
fuzzy factor: response of the scale of K to the frame, ..." (live L2949-3005). The pre-image hash is unchanged:
`6a72a326...39a7c`. I re-checked that it is still the live file.

1. **E1, E3 and E4 (scan-pass-2, item 1).** In each replacement string, `(next paragraph)` becomes
   `(paragraph on the Hessian of a tree stabiliser on \(K\) below)`. That phrase matches the title of E7, which
   contains "the Hessian of a tree stabiliser on \(K\)". The old strings are unchanged. The pre-image contains no
   other `(next paragraph)`, and the script checks that the post-image adds none.
2. **New E8 (scan-pass-2, item 2), at L3000.** E8 does not overlap E4, which sits in the same line.
   - old: `\(V\) and \(T\) both scale as \(\chi^2\), so the response of \(\chi\) does not move the condition \(V=T\).`
   - new: `For the operators without a tree stabiliser on \(K\), \(V\) and \(T\) both scale as \(\chi^2\), so the response of \(\chi\) does not move the condition \(V=T\).`
3. **New E9 and withdrawn E5 (scan-pass-2, item 3), at L3002.**
   - E9 old: `The value \(\beta_K=1\) needs a tree term of negative slope at the minimum and,`
   - E9 new: `In the forms with a tree stabiliser above, which omit its Hessian, the value \(\beta_K=1\) needs a tree term of negative slope at the minimum and,`
   - E5 is withdrawn. Its old string `for \(\hat U<0\), where \(q_b^2<0\), it is available at negligible \(Y\).` stays
     unchanged. The r2 suffix (", in the forms with a tree stabiliser above, which omit its Hessian") is now carried
     by the opening clause of E9 in the same sentence. Applying both would state that qualifier twice.
   - The final sentence, applied as one consistent edit, reads in full:

     ```latex
     In the forms with a tree stabiliser above, which omit its Hessian, the value \(\beta_K=1\) needs a tree term of negative slope at the minimum and, for \(\hat U\ge0\), \(Y>4|U_4|+2|U_2|\), which at large \(N\) on \(S^2_N\) is \(\chi^2<(\sqrt{39}-3)\vartheta/4\); for \(\hat U<0\), where \(q_b^2<0\), it is available at negligible \(Y\).
     ```

     The scope now covers both clauses of the sentence, the \(\hat U\ge0\) branch and the \(\hat U<0\) branch. In r2
     it covered only the second. The next sentence ("In each case the relation among the tree data ...") is
     unchanged.
4. **E7 (optional wording from scan-pass-3, adopted).** The file `appH_insert_r3.tex` equals `appH_insert_r2.tex`
   except for one string. In paragraph 3 of the insert:
   - old: `which Equation~\eqref{eq:Smatrix} does not contain;`
   - new: `which the displayed terms of Equation~\eqref{eq:Smatrix} do not contain;`

   Reason: `eq:Smatrix` (ch03 L142-157) contains the unspecified term \(S_{\mathrm{matter}}(\Psi,\hat X^\mu)\). The
   new wording claims only what can be checked, namely the absence of a \(\chi^3\)/\(\chi^2\) term on \(K\) among
   the displayed quartic and cubic terms. It makes no claim about \(S_{\mathrm{matter}}\). This matches r2's own
   wording in "Author decision needed" ("terms that `eq:Smatrix` does not display").
   - sha256 of the LF insert: `07ae105c65514f208b4ff49ba2ecd7243db89c1aea49a5b473d568597245c8a5` (12817 B).
5. **E2 and E6** are unchanged from r2. **Bibliography:** `new_bib_entry.bib` (`IsoKimuraTanakaWakatsuki2001`) is
   unchanged. The key is still absent from the live `bib/namcg.bib`.

The edits are applied in this order: E1, E2, E3, E8, E4, E9, E6, then the E7 insert before the unique line
`\section{Problem G: HBEV}`. Each old string occurs exactly once and lies inside the target paragraph (script
output).

**Post-image sha256:** `a7f1492a30c89b52e9ecadcd2550aaab89261796c35266b19bfed0d5b354e842` (733675 B, 3628 lines,
CRLF, no bare LF). The r2 post-image `120c8aba...` no longer applies.

## Verification scripts
- `apply_and_build_r3.py` is generated from r2. The only differences are the edit list above, the checks for the
  E5 string and the final E9 sentence, the check that no new `(next paragraph)` appears, and the file names. It
  checks:
  - the pre hash;
  - that every anchor is unique and inside the target paragraph;
  - CRLF line endings;
  - labels (`eq:Smatrix`, `def:matrix-coords-ext`, `ch:vierbein-emergence`, `ass:gap-psi`, `ass:lorentzian`, each
    defined once);
  - the citation;
  - a single status sentence;
  - no process language and balanced delimiters;
  - the post hash.

  With `--build` it builds a copy in a temporary directory outside the repository and then deletes it.
- `s5_exact_regulated.py` was re-run under `python -I`. Its output is byte-identical to
  `s5_exact_regulated_output.txt` (sha256 `899951d7...072b2b`).

Reproduction pack (from the repository root):
- `python -I proposals/069-f-nonderivative-sector/apply_and_build_r3.py --build`. Expected output:
  - `pre-hash matches expected: True`;
  - E1, E2, E3, E8, E4, E9 and E6 each `occurs 1x ... inside target paragraph True`;
  - `E5 old string kept once; final E9 sentence present once; ...`;
  - `post-hash matches expected: True` (a7f1492a...);
  - 410 pages, `undefined/multiply-defined warnings: 0`, `BUILD CLEAN`, `temp copy removed: True`.

  The saved output is in `apply_and_build_r3_output.txt`.
- `python -I proposals/069-f-nonderivative-sector/s5_exact_regulated.py | cmp - proposals/069-f-nonderivative-sector/s5_exact_regulated_output.txt`. Expected result: no difference.

## Decisions Taken
- **Optional pass-3 wording: adopted.** It is more accurate because `eq:Smatrix` contains an unspecified
  \(S_{\mathrm{matter}}\). The rejected alternative was to keep the r2 wording, which implicitly makes a claim about
  \(S_{\mathrm{matter}}\).
- **E5: withdrawn rather than kept as a no-op.** Its old string is retained verbatim, and the script asserts that.
  The rejected alternative was to keep both the E5 suffix and the E9 prefix, which would state the qualifier twice in
  one sentence.

## Milestone assessment
Unchanged from r2. M3 / PRIOR-CLAIM-ERROR (correction of the cubic and mass branches) applies, so the item goes to
the author after a plain ACCEPT.

## Status-label recommendation
None. The labels of F, C and N are unchanged.

## Author decision needed
None. This is unchanged from r2: the r2 information item on a supersymmetric completion still stands, and it is not
a decision request.

## Remaining open step
Unchanged from r2.

## Special instructions for the gatekeeper
- Verify only the diffs listed above against `scan-pass-2.md` and `scan-pass-3.md`. Then re-run the reproduction
  pack.
- Confirm that the final L3002 sentence above is exactly what the post-image contains.
- No mathematics changed. The values and statements of E7 are those of r2, apart from the one optional phrase.
