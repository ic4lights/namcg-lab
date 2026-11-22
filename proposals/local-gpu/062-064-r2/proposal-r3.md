# Proposal local-gpu/062-064-r2, round 3

This is a minimal revision of round 2 that answers `review-r2.md` (verdict AWRR, with 2 major findings and 3 minor
ones, plus 1 optional item). The texts to apply are now `block_C_r3.tex` and `block_F_r3.tex`. The r2 blocks are
kept in the folder for the diff only and are VOID for integration. Everything in `proposal-r2.md` stands except
what is listed below. Its Target and status, Source reading, R1-R6 derivations (with the S7 edits below), Decisions
D1-D6, Milestone assessment, Status-label recommendation and Author decision are unchanged unless this file says
otherwise.

## Result

- Unchanged in substance from r2. In the y^mu y^nu channel, at a background that is stationary at q = 0, there is
  an exact identity: every term that carries sqrt|g| alone drops out of the denominator of the first pole, and so
  does -q_b^2.
- This gives a bounded obstruction. A Yukawa pole needs positive deviations of the profile, `Sum(C_i - T_i)`, and
  these must come from terms that are not computed. Per F2, that list now also includes **the tree non-derivative
  terms of the wave**.
- **Correction (finding 2).** r2 claimed that the sign of the extra first-order part "changes with s_Lambda". That
  claim rested on a sample point, s_Lambda D = 3, which lies outside the truncation's validity. There the
  exact-regulated value is positive. The claim is removed (F4) and replaced by an exact criterion (F3), which I
  verified independently (below).
- Nothing is closed. C, F and N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Target and status

Unchanged from r2. I re-checked that the live appH sha256 is `a7f1492a30c89b52e9ecadcd2550aaab89261796c35266b19bfed0d5b354e842`.

## Source reading

The digest is current (`DIGEST CURRENT`; dirty-chapters: yes). This round used **digest + targeted reads**: appH
L2959-3046, i.e. the definition of `\hat U` at L2959-2962, `m_\chi` at L2982, L2994-2998 and L3039-3043.

The review rules that protocol 3(c) applies to block C. The gatekeeper still owes the full scan. This round makes
no claim to have done one.

## Research and reasoning: response to every finding

**Finding 1 (MAJOR): the tree non-derivative terms were missing from the obstruction list.** I applied F1 and F2
verbatim.
- F1 names the tree potential `\rho_MV_{\mathrm t}/g^2`, the object whose `\rho_M` does not respond at fixed chi.
- F2 adds "the tree non-derivative terms of the wave, which the leading symbol of the tree form drops" to the list
  of terms that do not carry sqrt|g| alone.
- This agrees with appH L2998, which lists the tree non-derivative terms as not computed.

**Finding 2 (MAJOR): the change of sign with s_Lambda.** I applied F3 and F4 verbatim and verified the criterion
myself.
- *Leading form* (the one in the block, valid up to relative order `x = s_Lambda D`). The bracket is
  `B = (15/2) th^2 E_1(x) - th c_J/D`. Since th^2 > 0, it factors as
  `B = (15/2) th^2 [E_1(x) - 2c_J/(15 th D)]`. So B > 0 **exactly** when `E_1(s_Lambda D) > 2c_J/(15 th D)`. This
  holds for either sign of c_J, because only th^2 > 0 is divided out. Check: S7, exact sympy identity.
- *Exact-regulated form.* Differentiating the exact density bracket of S6, I get the bracket
  `B_ex = (15/2) th^2 E_1(x) - th c_J e^{-x}/D`, and `B_ex - B = th c_J x/D + O(x^2)`. The two criteria therefore
  agree to relative order s_Lambda D. That is "within the truncation's validity" in the sense of F3. Check: S7,
  both statements symbolic.
- *Comparison at th = 1, D = 10, c_J = 2* (the r2 sample):

  | x | B | B_ex |
  |---|---|---|
  | 1e-3 | 47.2865 | 47.2867 |
  | 0.1 | 13.4719 | 13.4910 |
  | 3 | -0.1021 | +0.0879 |

  The zero of B is at x = 2.449 and the zero of B_ex is at x = 36.5. Both are far outside x << 1. So the r2 "sign
  change" was an artefact of using the leading form at x = O(1). This confirms the gatekeeper's observation.
- *What the criterion still permits.* Inside the range of validity, E_1(x) is about -gamma - ln x, so a zero with
  x << 1 needs c_J/(th D) >> 1. At 2c_J/(15 th D) = 4 the leading zero is x = 0.01039 and the exact-regulated zero
  is x = 0.01085. Their relative difference is about 4x, as expected (S7).
- So the sign of the bracket is set by the criterion, level by level. Whether it changes with s_Lambda inside the
  range of validity depends on the level data. No numerical claim of a sign change is made anywhere in r3.

*Removed or corrected r2 material:*
- The `verify_r2.py` check "S7 sign of extra part changes with s_Lambda" is replaced in `verify_r3.py` by the
  criterion identity, the exact-regulated comparison and the zero locations. `verify_r2.py` and its output are
  kept unchanged as the round-2 record, and they are superseded.
- The following r2 statements are withdrawn:
  - Result item 5, "numerical sign change at s_Λ D ≈ 3";
  - R5, "so its sign depends on s_Λ";
  - Claim 11, "its regulator-dependent sign … the sign change is numerical";
  - the reproduction-pack line "S7 bracket list ends (3.0, -0.1021...)".

**Finding 3 (minor): the sigma_1 coefficients.** I applied F5 verbatim, in both places. In F3 I applied
`p\,U_2\sigma_1`. In verify, "extra" is the coefficient of sigma_1 (S7 and S8 differentiate in sigma at 0), so the
change is consistent.

**Finding 4 (minor): q^2 below m_chi^2.** I applied F6 verbatim. `m_\chi^2=U_{\chi\chi}/Z_\chi` is defined at appH
L2982, before the insertion point. `apply_and_build_r3.py` asserts that ordering.

**Finding 5 (minor): wording of C1.** I applied C1 verbatim in both places ("full quadratic scalar operator"; "its
pole mass, or a ratio \(m_\psi/v\), as a derived output").

**Finding 6 (optional).** I adopted half of it; see Decisions Taken, R3-D1.

**Finding 7 (PRIOR-CLAIM-ERROR on gpu 062 block 2).** This round needs no action. That text is already VOID for
integration in r2, and neither r3 block carries it.

## Claim classification

This is the r2 table with these changes:
- **11 (replaced).** The extra first-order part under hypothesis 9, and its sign criterion `E_1(s_Lambda D) > 2c_J/(15 th D)` level by level, are
  **conditional** on 9 and on the level form; the criterion is an exact identity of the leading form, and agrees with the exact-regulated form to relative
  order s_Lambda D. No claim is made of a sign change.
- **7 (amended).** The list of terms that are not computed now includes the tree non-derivative terms of the wave.
  The claim is still conditional and a bounded obstruction. The clause "for either sign of \(\hat U\)" is part of
  the same conditional claim: with the listed terms set to zero, the right-hand side is
  `q^2 + q_*^2|_chi`, and `q_*^2|_chi = -L U'^2/(4m^4 U_chichi) < 0` for either sign of U_4 (S4).

## Proposed changes

These are pure insertions into `chapters/appH-microscopic-proofs.tex` at the same two anchors as r2 (each asserted
unique):
- C: after `tensor operator or the remaining scalar couplings.`, before `Problems~B, C, D, F and~G remain open.`;
- F: after `Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.`, before `\section{Problem G: HBEV}`.

The block texts are the files `block_C_r3.tex` (2613 bytes, sha256 `c86d0ba1…6a5e22`) and `block_F_r3.tex` (7417
bytes, sha256 `2c364025…9c9946`). They are CRLF, UTF-8 without a BOM, and add no `\label`. The labels are unchanged
from r2, and all 11 resolve once.

### Exact diffs from r2 (old -> new; each old string occurs once in the r2 block, as asserted by `make_snippets_r3.py`)

block_C:
- C1a: `the gauge-fixed quadratic scalar operator` -> `the full quadratic scalar operator`
- C1b: `and its pole mass as a derived output,` -> `and its pole mass, or a ratio \(m_\psi/v\), as a derived output,`

block_F:
- F1: `and the tree term carries \(\rho_M\), which does not respond at fixed \(\chi\).` -> `and the tree potential \(\rho_MV_{\mathrm t}/g^2\) carries \(\rho_M\), which does not respond at fixed \(\chi\).`
- F2: `…of the fibre-constant part of the first term, and the part of the first term with the fibre flux, at first and at second order, none of which is computed.` -> `…of the fibre-constant part of the first term, the part of the first term with the fibre flux, at first and at second order, and the tree non-derivative terms of the wave, which the leading symbol of the tree form drops, none of which is computed.`
- item 6 (adopted part): `With them set to zero the pole of this term has the tachyonic sign.` -> `With them set to zero the pole of this term has the tachyonic sign for either sign of \(\hat U\), so at a stationary background the sign of \(\hat U\) does not decide it.`
- F3: `, whose value and sign depend on \(s_\Lambda\), and that of \(U_2\) exceeds it by \(p\,U_2\);` -> `, whose value depends on \(s_\Lambda\) through \(E_1\), the bracket at each level being positive exactly when \(E_1(s_\Lambda\mathcal D)>2c_J/15\vartheta\mathcal D\), and that of \(U_2\) exceeds it by \(p\,U_2\sigma_1\);`
- F4: `The identity at a stationary background is exact for these forms, the density of the first term is exact for the level form at the stated limit, and the change of sign with \(s_\Lambda\) is numerical at sampled values.` -> `The identity at a stationary background is exact for these forms, and the density of the first term is exact for the level form at the stated limit.`
- F5a: `exceeds the profile of \(\sqrt{|g|}\) by \(-p\,(` -> `exceeds the profile of \(\sqrt{|g|}\) by \(\sigma_1\) times \(-p\,(`
- F5b: `the response of \(Y\) is finite, with the summand` -> `the coefficient of \(\sigma_1\) in the response of \(Y\) is finite, with the summand`
- F6: `With the exchange of \(\chi\) of the preceding paragraph, the denominator` -> `With the exchange of \(\chi\) of the preceding paragraph, for \(q^2\) below \(m_\chi^2\), the denominator`

The block contains no other change. The size changes are +19 bytes for C and +371 bytes for F.

## Verification scripts

All the scripts are in `proposals/local-gpu/062-064-r2/`:
- `make_snippets_r3.py` builds the r3 blocks from the r2 blocks by the replacements above. It asserts that each old
  string occurs once and that the output is CRLF. Output: `make_snippets_r3_output.txt`.
- `verify_r3.py` is `verify_r2.py` with the S7 sign check replaced. It checks:
  - the criterion identity;
  - the exact-regulated extra part and its O(x) difference from the leading part;
  - the comparison table and the zero locations.

  Output: `verify_r3_output.txt`.
- `apply_and_build_r3.py <repo> <scratch>` does the following:
  - it applies the r2 checks (pre-hash, unique anchors, CRLF, post-size, refs);
  - it asserts that the post hash differs from the r2 post hash;
  - it asserts that `m_\chi^2=U_{\chi\chi}/Z_\chi` occurs once and before block F;
  - it asserts that the scratch directory lies outside the repository;
  - it builds twice on a copy and deletes the copy.

  Output: `apply_and_build_r3_output.txt`.

**Reproduction pack** (run from the folder; the scratch directory must be outside the repository):
```
python -I make_snippets_r3.py   -> every "old occurs 1"; block_C_r3.tex 2613 c86d0ba1...; block_F_r3.tex 7417 2c364025...
python -I verify_r3.py          -> "ALL CHECKS PASS: True"; S7 table row 3.0: -0.10213... (leading), +0.08790... (exact);
                                   zeros x = 2.4486 (leading), 36.525 (exact); at 2c/(15 th D)=4: 0.010391, 0.010854
python -I apply_and_build_r3.py C:/Users/redgi/Projects/namcg-lab <outside dir>
                                -> pre a7f1492a30c89b52...; post 743713 B sha fef011270d31b932...; CRLF 3647 bareLF 0;
                                   both pdflatex rc 0; undefined 0; multiply defined 0; copy removed
```
The new post hash is `fef011270d31b93239845581a8826059ea6011b8bafd0899c5a9328346b79aa7` (743713 bytes). The r2
post hash was 112b485c… (743323 bytes), and the difference of 390 bytes equals 19 + 371.

## Decisions Taken

- **R3-D1 (optional item 6).**
  - *Adopted:* the stationarity note, as one clause appended to the sentence on the tachyonic sign. It is clearly
    better because appH L2998 states, at an uncancelled tadpole, "for \(\hat U>0\) the static scalar pole has the
    tachyonic sign unless …, and for \(\hat U<0\) … it is a Yukawa pole". Without the note, a reader could carry
    that sign-of-Û reading over to the stationary background. There it does not hold, because U_4 drops out and
    `q_*^2|_chi < 0` for either sign (S3, S4).
  - *Not adopted:* the phrase "vartheta-dependent coefficients". The review gives no anchor, and the block already
    says that vartheta enters U_2 and the first term through the loop-momentum average, and that it is held there at
    first order. Adding the phrase at a guessed location is not clearly better.
- **R3-D2 (F3 notation).** I kept `2c_J/15\vartheta\mathcal D` verbatim, as instructed. It is to be read as
  2c_J/(15 vartheta D), the inline convention used elsewhere in appH, e.g. `\tfrac{15}{4}\vartheta^2F\sqrt{|g|}/16\pi^2`.
  If the gatekeeper prefers `2c_J/(15\vartheta\mathcal D)` for clarity, that is a verbatim fix, and I have no
  objection to it.

## Milestone assessment

Routine.

## Status-label recommendation

Unchanged from r2. The critical-path set is A, B, C, D1, E, F, G-derived and N. C, F and N stay OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL. No label change is proposed.

## Author decision needed

None.

## Remaining open step

This is as in r2, with the avenue order taken from the review:
1. the tree non-derivative terms of the wave;
2. the fibre-level and flux response in the yy channel;
3. the second-order parts of U_2 and of the first term;
4. V != T (the W_R term);
5. q_b^2 in the third term;
6. fixing p, which is last and does not enter the pole of the reduced form.

F is still gated by D1. Per the review, no further edges are to be spawned ahead of D1.

## Special instructions for the gatekeeper

- Protocol 3(c) applies (your ruling). The full scan is still to be done.
- Re-check that F3 holds exactly for the leading form and to relative order s_Lambda D for the exact-regulated one.
  Also check that no r3 text or output asserts a numerical sign change.
- Check the adopted item-6 clause against S3/S4 and appH L2998.
- Must not be asserted: any value or sign of p; any sign of the static scalar pole beyond the conditional statement
  with the listed terms set to zero; a Cassini or Newtonian statement; any label change.
