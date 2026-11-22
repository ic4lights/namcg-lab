# Proposal local-gpu/062-064-r2, round 4

This is a minimal wording revision of round 3. It applies review-r3 finding 1 and scan-pass-4 findings 1 and 2
verbatim. The texts to apply are now `block_C_r4.tex` and `block_F_r4.tex`. The r3 and r2 blocks are VOID for
integration. Everything in `proposal-r3.md` (and in `proposal-r2.md`, as amended by r3) stands except the three
replacements below. Nothing else changed: no mathematics, no anchors, no labels, no status lines.

## Result

Unchanged from r3. The y^mu y^nu identity and the bounded obstruction are as accepted in r3. Nothing is closed.
C, F and N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Target and status

Unchanged from r3. The live appH sha256 was re-checked this round:
`a7f1492a30c89b52e9ecadcd2550aaab89261796c35266b19bfed0d5b354e842` (733675 bytes, 3628 CRLF, 0 bare LF).

## Source reading

Digest + targeted reads: ch17-agenda.tex L140-156 (the Problem C criterion), review-r3.md and scan-pass-4.md. The
full scan was done by the gatekeeper in scan passes 1-4. This round makes no claim to have done one.

## Research and reasoning: exact diffs

**R3-1 (review-r3 finding 1, required), block_F.** This fixes the parenthesisation.
- old: `\(E_1(s_\Lambda\mathcal D)>2c_J/15\vartheta\mathcal D\)`
- new: `\(E_1(s_\Lambda\mathcal D)>2c_J/(15\vartheta\mathcal D)\)`
- Check: the bracket is `(15/2)ϑ^2 E_1 - ϑ c_J/D`. For ϑ>0 it is positive iff `E_1 > 2 c_J/(15 ϑ D)`. The new text
  states that criterion. The math is unchanged; only the notation was ambiguous.

**S4-1 (scan-pass-4 finding 1, required), block_C.** This matches the ch17 wording at L145-146.
- old: `including the induced Einstein--Hilbert term,`
- new: `including the induced Einstein--Hilbert contribution,`

**S4-2 (scan-pass-4 finding 2, optional, adopted), block_C.** This follows the ch17 wording at L149-151.
- old: `and its pole mass, or a ratio \(m_\psi/v\), as a derived output,`
- new: `and its pole mass, or a ratio \(m_\psi/v\), as a derived output, together with the coupling that can be compared with Cassini bounds,`

*Grammar and duplication check (requested).* The resulting list is: kinetic coefficient, mixing, non-minimal
coupling, matter coupling, and pole mass/ratio as a derived output, together with the Cassini-comparable coupling,
and the phenomenological comparison of Chapter~\ref{ch:agenda}, ... The sentence is grammatical.

There is no literal duplication. Two items overlap in meaning:
- "its matter coupling" is the operator coefficient, and "the coupling that can be compared with Cassini bounds"
  is the derived output.
- "compared with Cassini bounds" names the comparable quantity, and "the phenomenological comparison" names the
  test itself.

Chapter 17 L144-155 contains exactly this pair of overlaps: "its matter coupling", then "the coupling that can be
compared with Cassini bounds", then "phenomenological comparison". So the overlap follows the criterion being
quoted and is not new redundancy. I keep the wording verbatim as instructed.

If the gatekeeper prefers a tighter form, the smallest coherent alternative changes only the inserted clause, to
`together with the scalar coupling to be compared with Cassini bounds,`. This alternative is NOT applied.

## Claim classification

Unchanged from r3. All three edits are wording only.

## Proposed changes

Same two anchors and insertion points as r3, with `block_C_r4.tex` and `block_F_r4.tex` substituted. There is no
other change to `chapters/`.

Final block C sentence (first sentence of the inserted paragraph, in full):

```latex
\paragraph{Missing step.} The full target of Problem~C is the full quadratic scalar operator on the locked vacuum in a constructed frame: the canonically normalised kinetic coefficient of the pure-trace scalar, including the induced Einstein--Hilbert contribution, its mixing with \(T_{\mu\nu}\), its non-minimal curvature coupling, its matter coupling, and its pole mass, or a ratio \(m_\psi/v\), as a derived output, together with the coupling that can be compared with Cassini bounds, and the phenomenological comparison of Chapter~\ref{ch:agenda}, defining and testing either a sufficiently heavy \(m_\psi\) or the scalar-tensor outcome, with Assumption~\ref{ass:gap-psi} discharged.
```

## Verification scripts

- `make_snippets_r4.py` builds the r4 blocks from the r3 blocks by the three replacements. Each old string occurs
  exactly once. The script checks that the output is CRLF, has no trailing newline, and that the length delta is
  exact. Output: `make_snippets_r4_output.txt`.
- `apply_and_build_r4.py` is `apply_and_build_r3.py` with the r4 block names and the r4 build directory, plus an
  assertion that the post hash differs from the r2 and r3 hashes. It uses the same PRE_SHA and the same anchors.
  Output: `apply_and_build_r4_output.txt`.
- `verify_r3.py` was re-run unchanged with `python -I`. Its output, `verify_r3_rerun_r4_output.txt`, is
  byte-identical to `verify_r3_output.txt` (`diff` is empty) and ends with `ALL CHECKS PASS: True`.

Reproduction pack:

```
python -I make_snippets_r4.py
#  block_C_r4.tex 2690 bytes sha e7e7a028d898dc5bb5cebcb6f3845a4cfd2f7f065841ebfbcbb44c990b777d52
#  block_F_r4.tex 7419 bytes sha fff2c45ab433aa2745762acab49b397aaf28863288aac4448484dfe197b618d7
python -I apply_and_build_r4.py <repo_root> <scratch_dir_outside_repo>
#  pre  sha a7f1492a30c89b52e9ecadcd2550aaab89261796c35266b19bfed0d5b354e842 (733675 B)
#  post sha d8d8b678fa0ceabe03f3f9c2f56cc60dbe140aa845658beddb0c206ba26c9180 (743792 B, CRLF 3647, bareLF 0)
#  11 labels each 1; 2 pdflatex passes rc 0; undefined 0; multiply defined 0; errors 0; copy removed
python -I verify_r3.py   # identical to verify_r3_output.txt; ALL CHECKS PASS: True
```

Byte check: the post size is 743792 = 743713 (r3 post) + 77 (block C: +8 for "contribution" in place of "term",
+69 for the Cassini clause) + 2 (block F: the parentheses).

## Decisions Taken

- I adopted the optional S4-2 so that block C follows the ch17 criterion wording. I rejected omitting it: the
  Cassini-comparable coupling is an explicit ch17 output and should appear in the missing-step statement.

## Milestone assessment

Routine.

## Status-label recommendation

None. The labels are unchanged.

## Author decision needed

None.

## Remaining open step

Unchanged from r3.

## Special instructions for the gatekeeper

- Confirm that the r4 blocks differ from r3 only by the three listed replacements:
  `diff <(tr -d '\r' < block_C_r3.tex) <(tr -d '\r' < block_C_r4.tex)`, and likewise for block F.
- Confirm the new post hash `d8d8b678...`.
