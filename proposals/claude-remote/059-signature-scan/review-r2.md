VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The r2 insert is the r1 insert with exactly the three replacements I required as F1–F3, byte for byte. F4 is recorded in the proposal, nothing else changed, and the round-1 mathematics, which I re-derived then, still stands.

## Source reading
- **Mode:** digest + targeted reads. No full scan is claimed.
- **Digest:** `make_digest.py --check` printed DIGEST CURRENT at HEAD d27650d. The working tree is unchanged from round 1: appH has 055–057; ch13, ch16, appE and appI have 058, which I checked in round 1 to be unrelated to Problem E.
- **Read this round:**
  - `appH_insert.tex` (r2) against `appH_insert.r1.tex`, by `diff` and by an exact string-replacement check;
  - `proposal-r2.md`, for F4 and the status, ordinal and label lines;
  - `apply_check.py` and `apply_check.txt`;
  - `bib_entries.bib`, by hash.
- **Read in full in round 1 and unchanged since:** appH L1482–1581, ch17 L392–400 and L690–752, ch04 L313–333, ch03 L130–204.
- **Scan ruling (same as round 1).**
  - 3(c) is not triggered. This is a new conditional paragraph with no change to any definition, assumption, status or label. The F1 wording narrows the scope sentence further.
  - 3(b) is not triggered. M2 is non-stopping.
  - 3(d) is met by the full reads of the dirty Problem E passages. Coverage is the ordinal-55 full scan plus these deltas, and the next 5th-item scan is due at 60.

## Claim under review
The claims are unchanged from round 1:
- the rigidity lemma;
- real points of cl 𝔆 are exactly t ∈ {0, 1, 9, 10};
- path and single-contour reality, and non-integrability, for 2 ≤ t ≤ 8;
- MW iff s−t ≡ 0 mod 8 (cited);
- under P1 ∧ P2, h₀ = ±TᵀηT, for the target contraction only.

Target: Problem E. From Appendix H L1486–1489, verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."

## Checks performed
- **Verbatim edits.** I applied the three exact replacement strings from review-r1 to `appH_insert.r1.tex`. Each source string occurs exactly once, and the result is byte-identical to the r2 `appH_insert.tex` (`scratchpad\v2.py`: "r2 == r1 + F1-F3 verbatim: True"). The r1 file hashes to ac95c669…9680, the r1 value I verified in round 1, so the base is authentic. `diff` shows changes only in paragraphs (i), (iii) and the closing paragraph, at exactly those three spots.
- **F1, the composite-metric sentence.** It now reads "With \(h_0\) in place of \(\eta_{IJ}\), the induced tensor of Definition~\ref{def:matrix-coords-ext} is its pull-back … Neither its signature nor that of the composite metric is derived here." This matches `def:matrix-coords-ext` (ch03 L177–196, η_IJ) and the manuscript's use of "composite metric" (appF L30). Resolved.
- **F2, the Kontsevich–Segal differences.** The text now says "Three differences matter", with the boundary position of positive-definite forms and the Euclidean contours h = e^{iπ/4}TᵀT. Both facts are already established in 055 (no real form in 𝔆) and 056 (i). Resolved.
- **F3, e_j.** It is now defined as "the basis vectors of the negative entries". Resolved.
- **F4.** Recorded at proposal-r2 L10 and L133: the negatives −𝓡_u and −e^{iθ}𝟙 show that p ≥ 2 is needed, since det(−h|_E) = det(h|_E). Correct; it affects the record only. Resolved.
- **F5.** The colour-mixing material is still outside the insert, which still says "no statement about linear maps that also mix the colour components". Unchanged.
- **apply_check, re-run in report mode.** Output:
  - appH baseline: 569524 B, 9443341b…7bcd, CRLF 3266, bare LF 0; matches.
  - Anchor: count 1 at L1575.
  - Insert: LF 10213 B, ae4e617f…2845; CRLF 10225 B, 607acf36…756b.
  - Result: 579751 B, b6c505ad16fcc689f32b3bc9975d78049f2bfc2679585149d56209154a7e5a8a, CRLF 3279, bare LF 0.

  All of these match the claimed values. The stored `apply_check.txt` also has three bib lines that the script does not print in my run. I checked the bib independently instead:
  - `bib_entries.bib` is unchanged: 625 B, cf79b6c0…91d7.
  - In round 1 I computed the appended bib at 26627 B, acbee1ce…738f.
- **LaTeX.** No new labels or citations. `\ref{def:matrix-coords-ext}`, `\eqref{eq:Smatrix}` and `\ref{ass:lorentzian}` are each unique. No process language. There is one scoped closing sentence, unchanged from r1. No status or label change.
- **Proposal-quote repair.** The researcher's byte-level repair of one `\ref` in proposal-r2.md's quoted change list does not affect integration, because the integrator uses `appH_insert.tex`, which is verified above.
- **Not re-run this round:** `rigidity_checks.py`, my own `gk059.py` and the colour checks. The mathematics is unchanged and all of them passed in round 1. A scratch LaTeX build was not run either; the integrator's `build_check.py` remains required.

## Findings
None. All round-1 findings are resolved, as itemised under Checks performed.

## Scope of what is established
Unchanged from round 1.

**Proved, exactly and at every N:**
- the rigidity lemma and its clopen corollary;
- real points of cl 𝔆 are t ∈ {0, 1, 9, 10};
- for 2 ≤ t ≤ 8, linear colour-blind paths with Re iS_b ≤ 0 keep h real, for any regulator and mass term;
- single contours with Re M > 0 and P⁻¹h₀ = ±c have real h;
- on these contours there is no damping, the integrand at ε = 0 is non-integrable, and the domination used in 053 is unavailable.

**Cited and verified:** the MW condition and the IKKT content.

**Conditional (PROGRAMME-CONDITIONAL):** h₀ = ±TᵀηT under P1 (imposed) and P2 (supplied). This concerns the target contraction only. Neither the induced tensor's signature nor the composite metric's is derived, and `ass:lorentzian` is not discharged. Problem E stays OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL, with no label change.

**Exact hypothesis class of the no-go:**
- linear contours that do not mix colour;
- Re iS_b ≤ 0 along the path, or Re M > 0 with P⁻¹h₀ = ±c;
- a damped-contour representation of the limit;
- ε → 0 at fixed N.

**Open avenues, ranked:**
1. Signature of the induced or composite metric on a selected background (scout R2, D1/E).
2. Existence of lim_{ε→0} for 2 ≤ t ≤ 8 at N = 2 without domination (H9/H3).
3. Colour-mixing linear maps beyond first order (H2).
4. Non-linear contours or thimbles (H1).
5. Alternatives to P2, and N → ∞ taken first.

**Milestone:** M2, a bounded no-go, non-stopping. Not M1, M3, M4 or M5, and not a breakthrough.

## Recommended disposition
Integrate as-is:
- `proposals/059-signature-scan/appH_insert.tex`, converted to CRLF, immediately before the unique `\paragraph{Status.}` anchor of Problem E (appH L1575), followed by one blank line. The resulting appH must hash to b6c505ad…5a8a.
- The three entries of `bib_entries.bib`, appended to `bib/namcg.bib` after a CRLF blank line, with CRLF endings. The result must be 26627 B, acbee1ce…738f.
- Then run `python scripts/build_check.py`.

## Corrected snippet
None needed.

VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0
