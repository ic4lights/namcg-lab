# Proposal 129-rc-held-recheck, round 2 (mechanical revision round)

## Result

The three exact string fixes mandated by review-r1 (findings 1-3) are applied to `payload-F.tex`;
no mathematics, no wording beyond those findings, no other byte changed. Corrected payload:
**3,147 B** (was 3,113 B, delta +34 B = −1 +9 +26, itemized below), sha256[:12] = `87a7c2568f72`,
sha1[:12] = `0cf326eb3457` (both prefixes recorded to bridge pin styles). Compile certificate
re-run on the corrected payload: `CERT129 PASS (exit 0, undefined refs/citations = 0)`, 450 pages,
0 undefined refs/citations, 0 multiply-defined; measured splice pre 883,075 B -> post **886,224 B**.
All four verify scripts re-run green. Findings 4-5 (notes) require no action. The routed
mathematics, claim tiers, conditionals and OPEN status are exactly as accepted in review-r1;
nothing here re-opens or alters them.

## Target and status

Problem F (`chapters/appH-microscopic-proofs.tex`, Problem F ledger section): **OPEN, CRITICAL
PATH, PROGRAMME-CONDITIONAL** (ch17 full-GR criterion includes F; read live in r1, chapters/
clean). Unchanged in r2. Payload changes no label. DERIVED (identity-level content) /
PROGRAMME-CONDITIONAL (the operator reduction and the weight input) exactly as tiered in r1.

## Source reading

Targeted reads (+ review-r1.md and the r1 artifacts in full; digest not re-refreshed, no claim
here depends on it). Re-verified live before editing: appH = 883,075 B / 4,146 lines; anchor tail
`On this evidence the sign of \(\hat U\) depends on \(K\).` + blank line occurs exactly once;
boundary `\emph{Scale dependence.}` exactly once; `git status --porcelain -- chapters` empty
(no other chain moved the text since r1). `123`'s `verify_ghost_op_123.py` not run (dispatch
instruction).

## The three payload fixes (exact strings, before -> after)

1. **Finding 1** (P2). Before: `\beta_K\simeq2\cdot5.345/10.68\simeq1.000`
   After:  `\beta_K\simeq2\cdot5.34/10.68\simeq1.000`  (the clause already ended in `\simeq1.000`;
   kept, and with 5.34 the identity 2*5.34/10.68 = 1.000 is exact per the gatekeeper's own
   recomputation and `verify_example_129.py`, tree slope 5.340000). Delta −1 B.
2. **Finding 2** (P1). Before: `checked at \(N\le5\) with residual below \(10^{-13}\)`
   After:  `checked at \(N\le5\) with residual below \(1.5\times10^{-13}\)`
   (the pack's own observed maximum is 1.421e-13 at N=4, inside the quoted set). Delta +9 B.
3. **Finding 3** (P1 opening). Before: `supplied there as \(C_{ijk}=\mathrm i c_3\epsilon_{ijk}/g^2\)`
   After:  `specialised there to \(C_{ijk}=\mathrm i c_3\epsilon_{ijk}/g^2\) on the flux directions`
   (the epsilon-tensor specialization is the held derivation's ansatz, consistent with the one
   supplied constant, not verbatim supplied). Delta +26 B.

Total delta +34 B: 3,113 -> 3,147 B, matching the byte counts above.

**Proof that no other byte changed:** `edit_payload_r2_129.py` asserts each old string occurs
exactly once and replaces once; the post-hoc inversion test run this session re-applies the three
inverses to the corrected file and recovers exactly the pre-edit r1 bytes: size 3,113,
sha256[:12] `bcace605a53b`, sha1[:12] `af564f3bf0b9` (both hashed directly before editing). Hence
the r2 payload differs from the reviewed r1 payload in exactly these three regions. Re-running
the edit script is idempotent-safe (prints `EDIT129 ALREADY-APPLIED` + hashes; guards fire on any
partial state).

**Hygiene (check_payload_129.py):** payload 3,147 B, 3 CRLF, 0 bare LF, ASCII, ends CRLF; old
strings (`5.345`, `supplied there as`, `below \(10^{-13}\)`) absent; each new string exactly once;
`\eqref{eq:Smatrix}` once; no `\cite`/`\ref{`/`\label{`. **Positive control (item-117 lesson):**
four in-memory doctored copies (injected bare LF; re-injected `5.345`; appended 0xE9 byte;
stripped trailing CRLF) - each caught by its expected guard, 4/4, printed by the script before
`CHK129 PASS`.

## Expected POST splice size (independent computation)

The splice in `cert_129.py` L26 is `txt.replace(anchor, anchor + payload + b'\r\n', 1)`, so the
delta is exactly len(payload) + 2 (the extra `b'\r\n'` join; the payload itself ends CRLF, so its
last line and the join consume no anchor bytes). Independent prediction: 883,075 + 3,147 + 2 =
**886,224 B**. Measured by the r2 cert run: `splice: pre 883075 B -> post 886224 B (payload 3147 B
+ join)`. Agreement. (Splice form here is insert-after-anchor, not `replace(anchor, payload +
anchor)`, so the memory note's blank-line-cost warning does not apply; the +2 join is the whole
overhead, as in the r1 gatekeeper run: 883,075 + 3,113 + 2 = 886,190.)

## Non-payload text fixes (proposal prose only; no manuscript text involved)

- `verify_example_129.py` L41 note: `tree-slope size 5.345` -> `tree-slope size 5.34` (the printed
  polynomial value is 5.3400; with 5.34 the "coincides" note is exact; note is non-load-bearing;
  the near() check already targeted 5.34). Script still ends `EXAMPLE_129 PASS`.
- `proposal-r1.md` (round file, prose + embedded quote only; 8 replacements, each count-checked):
  L27 `exactly \(2\cdot5.345/10.68\)` -> `\(2\cdot5.34/10.68\)`; L83 `-5.345\Rightarrow\beta_K=
  2\cdot5.345/10.68=1.0000` -> `-5.34\Rightarrow\beta_K=2\cdot5.34/10.68=1.0000`; L173
  `tree slope 5.345` -> `tree slope 5.3400`; L174 `\beta_K=2\cdot5.345/10.68=1.0000` -> `5.34`;
  the embedded payload-quote block updated by the same three payload replacements, and its size
  line `CRLF+ASCII, 3113 B` -> `3147 B` with a note that the quote now equals the r2 payload
  byte-for-byte (r1 as-submitted values remain recorded in review-r1.md). Post-edit grep: zero
  occurrences of `5.345` and `supplied there as` left in `proposal-r1.md`.

## Claim classification

Unchanged from r1 (gatekeeper accepted the tiering; no mathematics touched). The three fixes
change an unsourced number to the recomputed exact one (established), a false bound to a true one
(established, pack-measured), and an overstatement of what is supplied to an ansatz statement
(tiering fix, finding 3).

## Verification scripts (reproduction pack, r2 state)

Run from repo root with `python -I`:
- `proposals/129-rc-held-recheck/edit_payload_r2_129.py` -> `EDIT129 ALREADY-APPLIED size=3147
  sha256_12=87a7c2568f72 sha1_12=0cf326eb3457` (first-run output `EDIT129 APPLIED ... 3113 -> 3147 B (delta +34 B)` recorded here).
- `proposals/129-rc-held-recheck/check_payload_129.py` -> last line `CHK129 PASS`; invariants:
  payload 3,147 B / 3 CRLF / ASCII / ends-CRLF; appH 883,075 B pin; expected POST 886,224 B;
  4/4 positive controls caught (bare-lf, old-string 5.345, non-ASCII, trailing-CRLF).
- `verify_hessian_129.py` -> `HESSIAN_129 PASS` (a3/a4=-0.666667; residuals 3e-15..1.421e-13;
  window iff -1<=kappa_3<=2; kappa3=-2 min -2.000; kappa3=2 anchor; mult 3(N^2-1)) - unchanged.
- `verify_treecurve_129.py` -> `TREECURVE_129 PASS` - unchanged.
- `verify_example_129.py` -> `EXAMPLE_129 PASS` (r3=1.168242, kappa_3=-0.336484, V/T=0.028305,
  tree slope 5.340000, beta_K=1.000000; note line now reads "coincides with the tree-slope size
  5.34"; printed polynomial 5.3400).
- `verify_weights_129.py` -> `WEIGHTS_129 PASS (...)` - unchanged.
- `cert_129.py` -> full out-of-repo copy + splice + pdflatex/bibtex/pdflatex x2, `-halt-on-error`;
  expected: `splice: pre 883075 B -> post 886224 B (payload 3147 B + join)`, `pdflatex exit 0/0,
  pages = 450, undefined refs/citations = 0, multiply-defined = 0`, last line `CERT129 PASS`.
  r2 run output saved at `proposals/129-rc-held-recheck/cert-r2-output.txt` (scratch dir deleted
  by the script).

## Decisions Taken

- **Updated the embedded quote and expected-output lines in proposal-r1.md** (proposal prose only)
  so every quoted copy of the payload matches the corrected on-disk bytes, honoring the
  gatekeeper's "proposal prose ... should not repeat the number". Rejected alternative: leaving
  r1 untouched - it would leave a byte-size and quote drift contradicting the file the integrator
  splices, and re-assert 5.345 as a pack invariant that no script emits. The r1 as-submitted text
  is preserved in review-r1.md (gatekeeper's record), so no evidence is lost.
- Did not reflow/normalize proposal-r1.md's pre-existing .md line endings (not a manuscript .tex
  file; my replacements added zero newline bytes; a normalization edit would bloat the r1 diff).
- Kept the `\simeq1.000` clause (the gatekeeper's corrected snippet shows it and it is now exact).
- Recorded both sha256[:12] and sha1[:12] to bridge the pin-style mismatch (finding 5).

## Milestone assessment

Routine (mechanical revision of an already-accepted package; no trigger fires).

## Status-label recommendation

None. Problem F stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (live read unchanged).

## Author decision needed

None new. (r1's OPTIONAL unused BibTeX entry stands as before - payload cites nothing.)

## Remaining open step

Unchanged from r1: F is closed only by deriving the fluctuation-operator reduction on the cubic
branch from the matrix model (constructing, not conditionalizing, the "same reduction"), the
large-N weight ratio, and the one-loop delta - none supplied by this package.

## Special instructions for the gatekeeper

Re-run (not re-derive - math untouched): edit script (idempotent), check_payload_129.py (must show
4/4 controls + POST 886,224), the four verify scripts, cert_129.py (expect `CERT129 PASS`, 450 pp,
0 undefined, post 886,224 B). Verify the payload diff vs. review-r1 text is exactly the three
mandated regions (inversion proof above; payload on disk: sha256[:12] 87a7c2568f72). Verify no
`5.345` remains in payload-F.tex, verify scripts, or proposal-r1.md (only in review-r1.md and
this r2 note as the corrected-from record). Do not integrate r1's payload bytes; r2 payload
(3,147 B) is the splice target. Accept the payload as-is only if cert and byte pins reproduce; the
claim tiers and OPEN 0/2 of r1 carry unchanged.
