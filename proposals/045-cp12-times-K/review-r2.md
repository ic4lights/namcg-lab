VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
Applying R1–R8 verbatim to `appH_insert_r1.tex` reproduces `appH_insert.tex` (r2) exactly, with no other change. The r1 findings are closed, and the r2 insert is accepted.

## Source reading
Targeted re-review. I did not repeat the r1 mathematical verification (r1 review, s1–s3 re-runs, Steinacker check). I re-read the anchor region of the working-tree `chapters/appH-microscopic-proofs.tex`. I did not re-run `compile_check`; I relied on its saved output. That output reports 321 → 323 pages, 0 undefined references, 0 undefined citations and 0 multiply defined labels.

## Claim under review
Unchanged from r1. Problem F and Problem B stay "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." No label change.

## Checks performed
- **Diff r1 vs r2.** Both files were read CR-stripped. Each R1–R8 old string occurs exactly once in r1 (R5 was matched with the short anchor `or covariant (exact linear algebra`). Applying the ten replacements to r1 gives a string identical to r2: `True`. R6 consists of three replacements. Nothing else changed.
- **Byte check on `appH_insert.tex` (Python).**
  - 8485 bytes, 0 CR, 0 TAB, 0 non-ASCII, 0 control characters other than LF.
  - Braces, `\(` `\)` and `\[` `\]` are all balanced.
  - One `\paragraph`, no `\label`.
- **Anchor.** `\section{Problem G: HBEV}` occurs once, at L2393. L2391 is the 044 closing paragraph ("These statements are for the Poisson limit on \(M\), one loop…"), followed by a blank line at L2392. The insert ends "…Problems~B and~F remain open and PROGRAMME-CONDITIONAL."
- **r1 findings.**
  - Findings 1–4 are closed by R1–R8 as specified.
  - Finding 5 is a proposal and ledger wording item only. The insert contains no Problem C attribution, and I did not re-read proposal-r2.md for it.
  - No new defects.
- **PRIOR-CLAIM-ERROR.** None.

## Findings
None.

## Scope of what is established
Unchanged from r1.
- The paragraph is a conditional, bounded result.
- Averaged-frame reading: c_T = W_R/6 − 2W_X on the five traceless polarisations, so c_A − c_T = 0 for the finite parts of the fixed-state replica. This is labelled as the averaged-frame reading, not the fibre trace. It inherits the non-derived cone-value equality and the carried-over index-density identification.
- Fibre-trace reading: no single G_T for the six or the five, under stated hypotheses. These are inert amplitudes set to zero, Lorentz covariance at the frozen point without the background vector, and the hybrid treatment with the 044 cone values.
- The regime argument, the fibre-flux part, the Λ²/log parts, K, the sign of W_R and the interpolation are uncomputed.
- No milestone and no breakthrough. B and F remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.
- Open avenues and their ranking are as in the r1 review.

## Recommended disposition
Integrate as-is.

**Accepted text:** exactly `proposals/045-cp12-times-K/appH_insert.tex` (r2, 8485 bytes, LF). Convert to CRLF on integration, as the repository convention requires.

**Insertion point:** as one paragraph in `chapters/appH-microscopic-proofs.tex`.
- Place it immediately after the 044 paragraph, which ends "…Problems~B and~F remain open and PROGRAMME-CONDITIONAL." (L2391).
- Leave one blank line between them.
- Place it immediately before the unique line `\section{Problem G: HBEV}` (L2393), again with one blank line before the anchor.
- Replace nothing, and leave the 044 paragraph unchanged.

## Corrected snippet
None needed.
