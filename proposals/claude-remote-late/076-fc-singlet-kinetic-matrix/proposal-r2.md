# Proposal 076-fc-singlet-kinetic-matrix, round 2

Minimal revision round. It answers review-r1.md (AWRR: one major and two minor findings, plus the procedural full
scan). Findings 1-3 are applied verbatim with the texts given in the review. Nothing else is changed in the
manuscript text, the mathematics or the scripts s1/s2. Every section of proposal-r1.md not restated here stands
as written, except the three wording corrections listed under "Result".

## Result

The mathematical content is unchanged from r1, items 1-5. s1 and s2 were re-run with `python -I`, and their
output is byte-identical to the stored r1 outputs (modulo line endings). Three wording corrections carry over to
the r1 summary:
- Item 3: the Yukawa condition depends on the supplied rho_M/g^2 and on the **tree and one-loop** data of K,
  through U'_loop and U_chichi.
- Item 4: whenever the sigma_1 pole is Yukawa (mu + r/2 > 0), the static **form** has exactly one further
  **zero**, at q^2 > 0. At that zero the response to any source not orthogonal to the form's null vector has a
  pole of the tachyonic sign.
- Item 4: a static form **without a zero** at q^2 >= 0 needs the q=0 form to be positive definite.

Each claim keeps its r1 classification. The bounded no-go holds under H_K+ (a positive-definite kinetic matrix of
the singlets), and E1 now states that hypothesis. Nothing closes C, F or N, and no labels change.

## Target and status
As in r1, unchanged: Problem F (OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL), Problem C (same labels) and N (OPEN).
The critical-path set A, B, C, D1, E, F, G-derived and N is OPEN 8/8. The package is PROGRAMME-CONDITIONAL.

## Source reading
Digest + targeted reads. `python scripts/make_digest.py --check` printed DIGEST CURRENT (head 399fcc8,
dirty-chapters: yes). The live appH sha256 is 8aed4519472ef5ec9b1c8a4668e39b02b0882b5e7edb2cf9a9e0b5ba513ae229,
the same as the r1 pre hash; `apply_and_build_r2.py` checked it. In r2 I re-read only the three target sentences
in the r1 insert, in context, and the E1 anchor. **No full scan was done. It is still owed by the gatekeeper
(review-r1 finding 4; protocol 3(c)/(d)).**

## Research and reasoning
There is no new derivation. Each finding was checked against the r1 mathematics:
- **F1 (major).** The r1 E1 text claimed the singlet-sector statement without the positive-definite kinetic-matrix
  hypothesis that the insert's bound needs. The review's text restores it: "for a positive-definite kinetic matrix
  of the singlets". This matches the bounded no-go of the insert (det M(0) = -r(2mu+r) < 0 together with a
  positive-definite Z gives exactly one positive root).
- **F2 (minor).** The objects are zeros of det M(q^2), the static form. The response to a source J has a pole at
  such a zero only if J is not orthogonal to the null vector. The corrected wording says exactly this. The second
  replacement follows the same logic: no zero at q^2 >= 0, together with Z > 0, requires M(0) > 0.
- **F3 (minor).** U'_loop and U_chichi involve the one-loop data of K as well as its tree data, so "tree and
  one-loop data" is the accurate phrase.

## Claim classification
Unchanged from r1. The tachyonic-partner row now reads "the static form has one further zero at q^2 > 0, with a
tachyonic-sign pole of the response to any source not orthogonal to its null vector; established for these forms
under (K+) (bounded no-go)". The Yukawa-vs-chi row now reads "depends on supplied rho_M/g^2 and the tree and
one-loop data of K".

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`.
- Pre sha256: 8aed4519472ef5ec9b1c8a4668e39b02b0882b5e7edb2cf9a9e0b5ba513ae229 (live, verified).
- **Post sha256: 2b8f46a62f3b4480152f93801170029b589a08618ec1cf5504b8aea04eb85a4d** (794350 bytes, 3771 lines,
  CRLF, 0 bare LF). This replaces the r1 post hash deec6c35...7a69.

**E1** (L3138, tadpole paragraph; the anchor occurs once and lies inside the intended paragraph). Replace
`(on two other realisations of this channel the tree terms supply no positive constant; paragraph on the tree non-derivative terms below)`
with (review-r1 finding 1, verbatim):
```latex
(on two other realisations of this channel the tree terms supply no positive constant, and on the singlet sector, for a positive-definite kinetic matrix of the singlets, they supply one only together with a static pole of the tachyonic sign in the neutral singlet; paragraphs on the tree non-derivative terms and on the kinetic matrix of the static scalar singlets below)
```
Diff against the r1 E1 text: insert `, for a positive-definite kinetic matrix of the singlets,` after
`and on the singlet sector`.

**E2** (L3159): unchanged from r1. The anchor occurs once and lies inside the intended paragraph.

**E3.** Insert `appH_insert_r2.tex` (LF in the folder, CRLF on insertion; 8306 bytes; sha256(LF)
1345e9401c93f0331a6424b1c5e4e452317c4f3b9b05a1501a1c49c4aaeedbe1; 6 blocks) immediately before the unique line
`\section{Problem G: HBEV}`. The placement is as in r1. `appH_insert_r1.tex` is kept. The r2 file differs from r1
by exactly three replacements, each of which occurs once in r1 and zero times in r2 before replacement. All three
are in the paragraph "Selected combination ..." and the paragraph "The pole of the neutral singlet":

1. Finding 2a. Replace
   `the static response has exactly one further pole, at \(q^2>0\), of the tachyonic sign`
   with
   `the static form has exactly one further zero, at \(q^2>0\), at which the response to any source not orthogonal to its null vector has a pole of the tachyonic sign`
2. Finding 2b. Replace
   `a static response without a pole at \(q^2\ge0\) needs`
   with
   `a static form without a zero at \(q^2\ge0\) needs`
3. Finding 3. Replace
   `through \(U'_{\mathrm{loop}}\) and \(U_{\chi\chi}\), the tree data of \(K\)`
   with
   `through \(U'_{\mathrm{loop}}\) and \(U_{\chi\chi}\), the tree and one-loop data of \(K\)`

Nothing else changes: no labels, no citations, no bibliography entries, one status sentence (at the end of the
insert).

## Verification scripts
Run from `proposals/076-fc-singlet-kinetic-matrix/`:
- `python -I s1_singlet_symbol.py`. Unchanged. Re-run in r2, and the output is identical to
  `s1_singlet_symbol_output.txt` (`diff --strip-trailing-cr` is empty; ends "all checks passed").
- `python -I s2_static_singlet_response.py`. Unchanged. Re-run in r2, and the output is identical to
  `s2_static_singlet_response_output.txt` (empty diff; the invariants are as listed in r1).
- `python -I apply_and_build_r2.py [--build]`. It differs from r1 only in the E1 replacement string, the insert
  file name, the temp prefix and POST. Expected output, recorded in `apply_and_build_r2_output.txt`:
  - pre-hash matches expected: True;
  - E1 at line 3138 and E2 at line 3159, each occurring 1x and inside the intended paragraph True;
  - insert LF 8306 bytes, sha256(LF) 1345e940...dbe1, inserted at line 3165, followed by
    `\section{Problem G: HBEV}`;
  - post 2b8f46a6...5a4d, matches expected True, bare LF 0;
  - label ch:vierbein-emergence defined 1;
  - one status sentence at the end;
  - no label words or process language, balanced delimiters;
  - with --build: pdflatex rc 0 with 426 pages, 0 undefined/multiply-defined, BUILD CLEAN, temp copy removed
    (the build runs in a temporary copy outside the repository).

## Decisions Taken
- Findings 1-3 were applied verbatim, with no rewording. Finding 4 (the full scan) belongs to the gatekeeper.
- The proposal summary (Result, items 3-4) carries the same three corrections, so that it matches the
  manuscript text.

## Milestone assessment
Routine. This is a wording revision only.

## Status-label recommendation
None. All 8 critical-path problems remain OPEN.

## Author decision needed
None.

## Remaining open step
Unchanged from r1. The first-ranked avenue is the one-loop induced kinetic matrix of the singlets, which decides
H_K+ (review avenue 1). Then come the yy loop entries (mu), a non-frozen profile, general b and nu, and a derived
beta_K.

## Special instructions for the gatekeeper
- The full scan is still owed (review-r1 finding 4).
- Check that the three insert replacements and the E1 text match review-r1.md character for character, and that
  `apply_and_build_r2.py` reproduces post 2b8f46a62f3b4480152f93801170029b589a08618ec1cf5504b8aea04eb85a4d.
- The r1 "must not be asserted" list stands.
