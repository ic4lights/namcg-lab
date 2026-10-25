# Proposal 043-gauge-charge-edge-term, round 2

This round applies the three edits in the "Corrected snippet" section of `review-r1.md` and nothing else.

## Files

- **`appH_insert_r1.tex`**: a copy of the round 1 insert, unchanged.
- **`appH_insert.tex`**: the round 2 insert.
  - Each old string was confirmed to occur exactly once before it was replaced.
  - Edit (1) touches two sentences, so it was applied as two unique replacements.
  - No other text changed.
- **`bib_add.bib`**: unchanged from round 1. It holds the Chen2022 entry.
- **`compile_check.py`**: now also applies the accepted ch07 L227 correction in the scratch build.

## Findings and how each was addressed

**Finding 1 (major): the "no charge" attribution of the 3 kappa_X part depends on the presentation.**
- Applied as edit (2). The clause is now scoped to the presentation that keeps the gradient of vartheta as an independent invariant. It also states that the presentation which eliminates that gradient by the identity puts this part in the charge of R_G with r = -4, and that the density does not select between the two.
- **Correction to proposal-r1.** The r1 Result table entry "non-edge in every local reading examined" is withdrawn as not established. It restates the r-ambiguity. The correct statement is narrower:
  - The 3 kappa_X part has no charge in the presentation that keeps the vartheta gradient independent.
  - It is an R_G edge term (r = -4) in the presentation that eliminates the gradient.
  - The density does not select between these.
  - The conjecture about a class in which vartheta is independent stays outside the insert, as in round 1.

**Finding 2 (minor): T^op carries r = -4 by definition, not by derivation.**
- Applied as edit (1). The text now says the r = -4 edge term holds for T^op "so defined" and restates the on-mode definition of r = -4. It also says "the stress, so defined, does not supply it".

**Finding 3 (minor): the title tag.**
- Applied as edit (3). The tag "(conditional; bounded no-go)" is now "(conditional; not closure)".

**Finding 4 (PRIOR-CLAIM-ERROR, ch07 Eq. (xi-RNC)).**
- This is accepted separately, as written. It is not part of this insert. It is included only in the scratch compile.

## Exact final strings

**Edit (1), "Superpotential of the stress":**

`... so the edge term carried by \(T^{\mathrm{op}}_{\mu\nu}\) so defined is that of \(r=-4\), which restates the definition of \(r=-4\) by agreement on those modes. With the area coefficient \(c_A=c_W(0)\) of the fixed-state replica, the requirement \(G_A=G_T\) of the paragraph on the normalisation then needs the further term \(-4\kappa_X\) from the modular Hamiltonian of the state; the stress, so defined, does not supply it.`

**Edit (2), "Edge terms of the fluctuation Lagrangians", final clause:**

`... and \(3\kappa_X\) remains: the part that the stationary-set identity of the paragraph on Moser variables assigns to the gradient of \(\vartheta\) when that gradient is kept as an independent invariant, a first-order invariant with no charge on \(\Sigma\) in that presentation; in the presentation that eliminates it by the identity this part is carried by the charge of \(R_G\) with \(r=-4\), and the density does not select between the two.`

**Edit (3), title tag:** `(conditional; not closure)`

## Byte check of the round 2 insert

| Check | Result |
|---|---|
| Size | 7947 bytes |
| Tabs | 0 |
| CR characters | 0 |
| Non-ASCII bytes | 0 |
| Control characters other than LF | 0 |
| Brace balance | 0 |
| `\(` / `\)` balance | 0 |
| Final LF | present |

## Scratch compile

The current tree was built outside the repository, with the insert, the Chen2022 bib entry and the ch07 L227 correction applied. The output is in `compile_check.out.txt`.

| Build | Pages | Exit codes (pdflatex, bibtex, pdflatex, pdflatex) | Undefined refs | Undefined citations | Multiply defined labels |
|---|---|---|---|---|---|
| Baseline | 315 | [0,0,0,0] | 0 | 0 | 0 |
| With the changes | 317 | [0,0,0,0] | 0 | 0 | 0 |

CRLF line endings were preserved, and the scratch directory was removed.

## Unchanged

- No labels change. Problems B, D and A stay OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL.
- The milestone assessment is routine.
- No author decision is needed.
