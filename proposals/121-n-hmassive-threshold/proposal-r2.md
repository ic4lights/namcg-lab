# Proposal 121-n-hmassive-threshold, round 2

## Result
Round-1 payload corrected by exactly the three replacements required by
review-r1 (ACCEPT WITH REQUIRED REVISIONS), applied verbatim; no other text
change. New payload 3754 B / sha1[:12] 84dcba179198. Compile certificate
re-issued on the corrected bytes: PRE 854131 f5a761c55396 -> POST 857887
cf3139fbedb076a6d7f68278a0945756a49efdbf, two pdflatex passes rc 0, exclam 0,
undefrefs 0, multidef 0 (48 pre-existing undefined citations, informational),
temp tree removed. Verifier 12/12 PASS on the corrected payload, twice.
Mathematics, claim tiers, hypothesis list and status dispositions are
unchanged from round 1; Problem N stays OPEN, CRITICAL PATH,
PROGRAMME-CONDITIONAL and Problem F stays OPEN.

## (a) The three before/after diffs (payload lines, CRLF; content of each
replacement equals the review-r1 "Corrected snippet" verbatim)

Replacement 1 (blocking: undefined \Lambda^2_{\mathrm W} -> recorded \LUV;
gatekeeper Finding 1):
```
- \(|m_2|^2=\Upsilon_H\Lambda^2_{\mathrm W}/L_m\) (the recorded
+ \(|m_2|^2=\Upsilon_H\LUV^2/L_m\) (the recorded
```

Replacement 2 (blocking: Q=1/6 clause scoped to the a1/R^2 windows; the C^2
coefficient 1/120 remains in \mathcal W_C, so \Upsilon is still shifted
through the W_C denominator; gatekeeper Finding 2). Old three lines:
```
- and at \(Q=1/6\) the curvature window of this block vanishes, so this
- block shifts neither \(1/G_{\mathrm{eff}}\) nor \(\Upsilon\) at this
- order. The fixed-window spin-two pole estimate
```
New five lines (the last line-break before "pole estimate" is whitespace-only
reflow; content equals the corrected snippet exactly, verified modulo wrapping
by scratch/121/diffcheck121.py -> EXACT-THREE-REPLACEMENTS True):
```
+ and at \(Q=1/6\) the curvature \(a_1\) and \(R^2\) windows of this
+ block vanish, so its windowed contribution to \(1/G_{\mathrm{eff}}\) and to
+ the \(a_1\)-numerator of \(\Upsilon\) is zero at this order, while its
+ \(C^2\) coefficient remains in \(\mathcal W_C\). The fixed-window spin-two
+ pole estimate
```

Replacement 3 (minor: paragraph anaphora at the splice site; gatekeeper
Finding 3):
```
- the boundary remainder-bound argument of the preceding paragraph
+ the boundary remainder-bound argument of the two preceding paragraphs
```

## (b) No other changes
diffcheck121.py reconstructs the new payload from the old one by applying
exactly these three replacements (modulo CRLF wrapping) and asserts equality:
EXACT-THREE-REPLACEMENTS True. Hence claim tiers, all numerals (Upsilon_H
= 10[e^{-y}-yE1(y)], pole ratio 10[e^{-y}/E1(y)-y], crossing
y=e^{-(10+gamma_E)}(1+O(10^{-2})), branch cut (-inf,-4y], freeze value,
hypotheses list, closer "both stay OPEN"), the 7 whitelisted \ref targets and
the zero-\label/zero-\cite hygiene are unchanged from the round-1 payload the
gatekeeper fully accepted. New tokens \(a_1\), \(R^2\), \(\mathcal W_C\),
\LUV, \(C^2\), \(1/G_{\mathrm{eff}}\) are all plain ASCII in the payload and
all pre-existing in the manuscript's notation; no new \ref/\cite targets.

## (c) Attribution
Change 1 = review-r1 blocking finding "undefined \Lambda_W";
change 2 = review-r1 blocking finding "Q=1/6 overclaim" (scoped wording taken
verbatim from the Corrected snippet, including its internal line breaks);
change 3 = review-r1 minor finding "off-by-one paragraph anaphora".
Generator controls: five whole-function rejection controls fired [True x5] in
both regeneration runs; verify121-r2.py S11 hygiene + six injected-defect
controls + len(names)>=8 intact and PASS.

## Reproduction pack
- `python -I gen_payload_121.py` (twice) -> hygiene OK, controls fired
  [True,True,True,True,True], payload bytes 3754 sha1[:12] 84dcba179198,
  anchor count 1, PRE 854131 POST 857887 delta 3756 = 3756 True, sha1 spliced
  cf3139fbedb0, GEN121 OK (capture: out-gen121-r3.txt).
- `python -I splice121r2.py` -> POST 857887 cf3139fbedb0 (full sha1
  cf3139fbedb076a6d7f68278a0945756a49efdbf), POST-matches-expected True,
  wrong-zone-hash guard True, same-bytecount-as-wrongzone True, SPLICE2 OK.
- `python -I verify121-r2.py` (twice) -> TOTAL 12/12 PASS, ALL CHECKS DONE 121
  (capture: out-verify121-r6.txt).
- `python -I diffcheck121.py` -> EXACT-THREE-REPLACEMENTS True, new-size 3754.
- `python -I scratch/121/cert-r121q.py` -> CERT PASS (capture:
  scratch/121/out-cert-r121q-r1.txt).

## Deviation from dispatch wording (one, recorded)
verify121.py contains no payload hash/size pin, so the default was "reuse
verify121.py unchanged"; however its S11 selects `cands[0]` of files matching
`insert*.tex`, and the instructed superseded-evidence copy
`insert-n-hmassive-threshold-r1-superseded.tex` sorts lexicographically BEFORE
the live payload (byte '-' < '.'), so an unmodified re-run would silently
verify the old bytes. Minimal fix: verify121-r2.py = verify121.py with ONE
added selection filter (`and 'superseded' not in f`); all check logic, the six
S11 controls and the len(names)>=8 condition byte-identical. verify121.py left
unmodified at d04bf3101e0c/10728.

## Decisions Taken
Kept the instructed superseded-copy filenames (evidence bytes preserved per
the pinned-file-supersession rule) and routed around the glob collision via
the verifier copy above, rather than renaming the evidence files or editing
verify121.py in place; this preserves both the evidence trail and a verifier
that provably targets the live payload.

## Milestone assessment
Routine: mechanical correction round on an already-accepted package; no
milestone trigger. (Candidate status for integration at ordinal 49 per the
gatekeeper's recommended disposition, pending their r2 ACCEPT.)

## Status-label recommendation
None. N: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL unchanged. F: OPEN
unchanged.

## Author decision needed
None.

## Remaining open step
Unchanged from round 1: derivation of the h-massive threshold windows (and the
block-level W_C, A1, G_eff, delta_W data) from the matrix path integral for the
Problem-F values; nothing here closes N or F.

## Label changes: None.
