VERDICT: ACCEPT | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0

## Verdict
The r2 insert differs from r1 only by the three requested edits, and its mechanics are clean. The Chen2022 BibTeX is unchanged from the entry I checked in r1, and the ch07 L227 correction stands. All three pieces are accepted.

## Source reading
Digest + targeted reads. `git status` for `chapters/` is clean, so there is no dirty-chapters flag. I did not run a full scan. I did not re-read `proposal-r2.md`, only the insert, the diff and the compile output.

## Checks performed
I ran a character-level diff of `appH_insert_r1.tex` against `appH_insert.tex` (r2) in Python. The only changes are:
- The title tag changes from "(conditional; bounded no-go)" to "(conditional; not closure)". This is finding 3 of my r1 review.
- Finding 2: "so defined" is inserted after "the edge term carried by T^op", followed by ", which restates the definition of \(r=-4\) by agreement on those modes". "the stress, so defined, does not supply it" is also inserted.
- Finding 1: "when that gradient is kept as an independent invariant" is inserted. After "a first-order invariant with no charge on \(\Sigma\)" the following is added: " in that presentation; in the presentation that eliminates it by the identity this part is carried by the charge of \(R_G\) with \(r=-4\), and the density does not select between the two".

These match my corrected snippets from r1 verbatim. Nothing else changed.

Byte check of the r2 insert: 7947 bytes, 0 TAB, 0 CR, 0 non-ASCII, 0 control other than LF. Braces and `\(`/`\)` balance, both 0. There are 0 `\label` commands in the insert.

Anchor: `\section{Problem C: conformal mode and Cassini}` occurs once in `chapters/appH-microscopic-proofs.tex`. "Matrix gauge realisation" occurs 0 times there, so the insert goes immediately before that section line, after the 042 paragraph. The insert is LF and ASCII, so the integrator must write it with CRLF line endings.

The compile output shows exit codes [0,0,0,0], 317 pages, and 0 undefined references, citations and multiply defined labels with the insert, the bib entry and the ch07 fix. I did not re-run the build. `Chen2022` is not yet in `bib/namcg.bib` (grep count 0). The `bib_add.bib` entry begins with `@article{Chen2022`, and I verified its fields against the arXiv API in r1.

The ch07 L227 old string still occurs once in the unchanged working tree. I confirmed this in r1 with `grep -F`; it is not re-confirmed in r2. A Python re-check in this session returned 0, which came from escaping in my one-off script, not from the file.

## Findings
none. My r1 findings 1–3 are closed. Finding 4 was the separate ch07 item, and it stands as a distinct correction.

## Scope of what is established
Unchanged from my r1 review. Nothing is DERIVED. B, D and A remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change is proposed. The insert is a bounded, conditional no-go with the following boundaries:
- It is limited to the Poisson limit, four coordinates, n_D = 0, joint-flow-invariant backgrounds and local charges.
- The 3κ_X attribution rests on the numerical 041 stationary-set identity, and the insert now says it depends on the presentation.
- The Maxwell edge sector is an input, not a derivation.
- It gives no local Lorentz symmetry, so nothing for D1.

The open avenues and their ranking are as in my r1 review. The top two are the modular Hamiltonian and edge sector of the matrix state (A ∩ B), and a class in which the axion is independent of the tensor modes.

This is not a breakthrough.

## Recommended disposition
Integrate as item 41.

## Accepted text
1. The block `proposals/043-gauge-charge-edge-term/appH_insert.tex` (r2, 7947 bytes), inserted immediately before `\section{Problem C: conformal mode and Cassini}` in `chapters/appH-microscopic-proofs.tex`, with one blank line before it, converted to CRLF.
2. The `Chen2022` BibTeX entry in `bib_add.bib`, appended to `bib/namcg.bib` with CRLF if that file uses it.
3. The ch07 L227 correction, as its own item. The old string, which occurs once, is `   \bigl((\ell^2-t^2-r^2)\partial_t^\mu+2t\,x^\mu\bigr)`. The new string is `   \bigl((\ell^2-t^2-r^2)\partial_t^\mu-2t\,x^i\delta^\mu_i\bigr)`. The integrator edits in place and preserves that line's existing ending.
