VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0 (one minor wording defect)

## Verdict
All r1 required corrections are applied correctly and nothing else changed. One sentence, the CP^{1,2} one, is now ungrammatical (a comma splice created by my r1 snippet 6), so a one-character fix is required before ACCEPT.

## Source reading
Targeted reads, not a full scan. I compared `appH_insert_r1.tex` with `appH_insert.tex` (r2) sentence by sentence. The r1 review covered the full mathematical verification; the r2 changes are wording and scope only. I re-read the current chapters/ working tree for the anchor and for `ass:local-lorentz`.

## Claim under review
Unchanged from r1. Problems B and F (PROGRAMME-CONDITIONAL, OPEN, CRITICAL PATH) are untouched; no label change.

## Checks performed
**Diff r1 vs r2.** Eleven sentence-level changes, all matching the r1 snippets:
- Heading is now "(conditional; not closure)".
- Null-mode sentence: now "nonzero as a tensor … although its quadratic invariants vanish on a single null wave".
- Steinacker sentence: now "corresponds structurally … (the same mixed term; the normalisations and the sign convention are not compared, and there the axial torsion is the axion)".
- Fixed-state gap: now "cutoff-dependent terms from the first term (the order Λ² term and a logarithmic term proportional to the trace of H_0^K, whose finite remainders are not computed) plus the part 2W_X from the mixed term". Periodic and smooth are now phrased as conditions ("vanishes only if W_R=16W_X").
- The "finite part" sentence is now "The part 2W_X of the fixed-state gap that comes from the mixed term …".
- The criterion sentence now reads "the mixed-term part of the gap would vanish …". It is followed by the added dressed-density sentence, with `\ref{ass:local-lorentz}` and c_T^ext = W_R/6 − 2W_X.
- Brane sentence: the "no single G_T" claim is replaced by "neither established nor excluded", with the factor-of-symbols explanation.
- Closing scope sentence: now includes "a fuzzy space K that is not required to solve the equations of motion" and "for the transverse-mode check, frozen coefficients at one background point".
- No other change.

**K notation.** `\mathsf K` occurs exactly three times, all for the kinetic tensor θ^Tgθ: the brane sentence (twice) and the definition. Every other K in the block is the fuzzy space.

**Bytes (Python).** 11763 bytes, 0 CR, 0 TAB, 0 non-ASCII, 0 control characters other than LF. Braces balanced. `\(`/`\)` is 175/175. `\[`/`\]` is 2/2. One `\paragraph`, no `\label`.

**Refs and anchor.**
- `ass:local-lorentz` is defined once, in ch10-lorentz-locking.tex L56.
- `sec:status-B`, `ch:vierbein-emergence` and the three cite keys were verified as unique in r1; r2 adds no new ones.
- The anchor `\section{Problem G: HBEV}` occurs once in the working tree, directly after the 041 Casimir paragraph. The 043 block before Problem C does not affect it.

**Build.** The saved compile_check reports 317 → 321 pages and 0 undefined references. I did not re-run it.

## Findings
1. **Minor (required). CP^{1,2} sentence.** It now reads "… of~\cite{SperlingSteinacker2019}, the bundle structure and the generator definitions agree with those of the conjugate-coordinate class here up to normalisation, the assignment … following Section~7 of~\cite{Steinacker2023}; there the mixed term is …". The comma after `\cite{SperlingSteinacker2019}` makes the sentence ungrammatical, and "there" is now ambiguous.
   - Replace `of~\cite{SperlingSteinacker2019}, the bundle structure` with `of~\cite{SperlingSteinacker2019}; the bundle structure`.
   - Replace `following Section~7 of~\cite{Steinacker2023}; there the mixed term is` with `following Section~7 of~\cite{Steinacker2023}. In that construction the mixed term is`.
   - Each old string occurs once.

   Without these changes the sentence is ungrammatical; the content is correct.

## Scope of what is established
Unchanged from the r1 review: conditional bookkeeping and exact algebra; nothing DERIVED; B and F remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; no brane no-go; no milestone and no breakthrough. M2 does not fire (see the r1 review).

## Recommended disposition
Apply the finding 1 fix and integrate. On that edit alone the block is acceptable.

**What is accepted:** exactly `appH_insert.tex` (r2, 11763 bytes) with the finding-1 replacement. It is inserted as one paragraph, with CRLF endings, immediately before `\section{Problem G: HBEV}`. If the researcher resubmits with that change only, no further review of the mathematics is needed.

## Corrected snippet
As given under finding 1. No new physics or assumptions.
