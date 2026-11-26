# Proposal 086-g-081-momentlabel-correction, round 1

CORRECTION package (not new research). Fixes the gatekeeper-confirmed prior-claim error F2 of
`proposals/085-g-moments-uniformity-locus/review-r1.md` in the integrated 081 paragraph at
`chapters/appH-microscopic-proofs.tex` L3177.

## Result
The integrated 081 sentence simultaneously asserts that the proxy fourth-moment excess equals
\(1/D_{\mathrm{eff}}\) exactly and quotes \(4.0\times10^{-3}\to2.6\times10^{-4}\) as "the fourth-moment
excess". Exact rational arithmetic on 081's own profile convention (\(g_l=l/2\) with multiplicity
\(2l+1\), \(l=1..l_c\); \(D_{\mathrm{eff}}=(\sum g)^2/\sum g^2\)) gives the true fourth-moment excesses
\(\rho_2-1 = 1/D_{\mathrm{eff}} = 6.7204\times10^{-4}\) (\(l_c=40\)) and \(4.3446\times10^{-5}\)
(\(l_c=160\)), while the quoted numerals are \(6/D_{\mathrm{eff}}\) (4.0323e-3 / 2.6068e-4) and match the
exact eighth-moment excesses \(\rho_4-1\) (4.0375e-3 / 2.6070e-4) to 2 s.f. — i.e. \(p=4\) (eighth-moment)
values mislabeled "fourth-moment". The package replaces the two numerals by their true fourth-moment values
(6.7e-4 / 4.3e-5, 2 s.f.), removing the internal contradiction with the same paragraph's exact
\(\rho_2-1=1/D_{\mathrm{eff}}\) clause. My verification (`s1_moment_values.py`) reproduces every gatekeeper
numeral exactly, by two independent exact-arithmetic routes per moment (complete-homogeneous recursion and
partition-form closed forms).

## Target and status
- Affected problem: Problem G (HBEV). appH L3026-3029 verbatim: "Status: OPEN. Priority: CRITICAL PATH.
  Completion: PROGRAMME-CONDITIONAL." Unchanged by this package — the edit is purely numerical (moment-label
  of two quoted values) and touches no status, priority or completion language. G stays OPEN / CRITICAL PATH /
  PROGRAMME-CONDITIONAL; nothing is closed or reopened.
- Provenance: REVIEW-085-r1 finding F2 (PRIOR-CLAIM-ERROR, M3 recorded in the ledger per author directive 4);
  ledger sequencing entry: "item 086 = correction proposal to appH L3177 ... gatekeeper review, integrate as
  ordinal 16; then 085 round 2".

## Source reading
digest + targeted reads. `scratch/digest.md` head 384dfc1, DIGEST CURRENT, dirty-chapters yes (expected
uncommitted 081-084 integrations); reviewed the working tree, not HEAD. Read in full: appH L3020-3034 (G
section head + Ledger label block) and the complete live L3177 line (dumped as raw bytes); the 085 review
in full (F2, Checks performed/claim-7 arithmetic, Corrected snippet); `proposals/081-g-edge-moments/`
folder listing and `s3_profile_concentration_r2.py` in full (profile convention, \(\rho_p\) definition,
\(D_{\mathrm{eff}}\) table); ledger tail (REVIEW-085-r1, INTEGRATION-15, DISPATCH/ORCHESTRATION-085).

## Research and reasoning
1. Convention fixity. The 081 paragraph fixes everything needed to disambiguate the two readings:
   \(D_{\mathrm{eff}}=(\sum g)^2/\sum g^2\), \(\rho_p(g)=p!\,h_p(g)/(\sum g)^p\), "the averaged \(2p\)-th
   moment equals the edge-data single-scale prediction multiplied by \(\rho_p(g\))", "\(\rho_2-1\) equals
   \(1/D_{\mathrm{eff}}\) at \(p=2\)", and the clause "fails at the fourth by exactly \(1/D_{\mathrm{eff}}\)".
   Within this convention the fourth-moment excess is by definition \(\rho_2-1\), so the quoted
   \(4.0\times10^{-3}/2.6\times10^{-4}\) cannot be fourth-moment excesses unless \(D_{\mathrm{eff}}\approx250\)
   / \(3850\), contradicting the same sentence's quoted \(D_{\mathrm{eff}}=1488\to23017\).
2. Independent re-derivation (script `s1_moment_values.py`, exact `fractions.Fraction`, run `python -I`):
   profile \(g_l=l/2\) with multiplicity \(2l+1\), \(l=1..l_c\) — the exact-rational limit of 081 s3_r2's
   `Fraction(int(f(l)*1000),1000)` which for \(f=l/2\) equals \(l/2\) exactly (500l/1000), so 081's shipped
   \(D_{\mathrm{eff}}\) values are the exact-rational ones. Computed \(D_{\mathrm{eff}}\), \(\rho_2-1\),
   \(\rho_4-1\) by the generic complete-homogeneous recursion (081's `hcf`) AND by partition-form closed
   forms \(\rho_2-1=s_2/S_1^2\) and \(\rho_4-1=(6S_1^2s_2+3s_2^2+8S_1s_3+6s_4)/S_1^4\); the two routes agree
   exactly (asserted). Results: \(D_{\mathrm{eff}}=1488.002400\) / \(23016.894112\);
   \(\rho_2-1=1/D_{\mathrm{eff}}=6.7204\times10^{-4}\) / \(4.3446\times10^{-5}\) (exact identity
   \(\rho_2-1=1/D_{\mathrm{eff}}\) asserted as a Fraction equality); \(6/D_{\mathrm{eff}}=4.0323\times10^{-3}\) /
   \(2.6068\times10^{-4}\); \(\rho_4-1=4.0375\times10^{-3}\) / \(2.6070\times10^{-4}\). These reproduce the
   gatekeeper's claim-7 numerals digit for digit; the mislabel (factor-6, \(p=2\) label on \(p=4\) values) is
   confirmed by my own arithmetic.
3. Why replace the numerals rather than the label (option (a) over (b)): see Decisions Taken.
4. Consistency of the corrected sentence. After the fix, "grows ... from \(1488\) ... to \(23017\) ... while
   the fourth-moment excess drops from \(6.7\times10^{-4}\) to \(4.3\times10^{-5}\)" equals exactly
   \(1/D_{\mathrm{eff}}\) of the quoted (rounded) dimensions to 2 s.f., matches the exact
   \(1/D_{\mathrm{eff}}\) clause three clauses earlier, keeps the monotone "drops", and keeps the trailing
   caveat "(numerical, on the exact rational profiles)" accurate (the values are the numerical 2-s.f.
   readings of exact-rational quantities on the profiles, as before).
5. Literature: none required; this is internal arithmetic against the repository's own convention. Nothing
   cited, nothing imported; emergence untouched.

## Claim classification
- The corrected numerals 6.7e-4 / 4.3e-5: established — exact-derivation values (2 s.f. roundings of
  \(1/D_{\mathrm{eff}}\) for the stated exact rational profiles) under 081's own stated convention; verified
  twice per quantity by exact arithmetic (this package and the 085 gatekeeper check, independently).
- The diagnosis (quoted 4.0e-3 / 2.6e-4 are \(p=4\) eighth-moment values, \(\approx6/D_{\mathrm{eff}}\)):
  established — exact arithmetic, two independent routes each side.
- This package's change: correction of a mislabeled numerical statement in accepted text; no new physics, no
  new premise, no status change.

## Proposed changes
File: `chapters/appH-microscopic-proofs.tex` — ONE in-place clause replacement inside the existing 081
paragraph at L3177. No new paragraph, no new `\emph` header, no insertion, nothing else in the file changes.
All surrounding sentences and the whole rest of the line are kept verbatim.

BEFORE substring (verbatim from the live file; occurs EXACTLY once, count asserted by
`simulate_apply_086.py`; single backslashes as in the file's `\(...\)` inline-math style):

```
the fourth-moment excess drops from \(4.0\times10^{-3}\) to \(2.6\times10^{-4}\)
```

AFTER substring:

```
the fourth-moment excess drops from \(6.7\times10^{-4}\) to \(4.3\times10^{-5}\)
```

Context (unchanged, for the gatekeeper): the clause sits in "... the effective dimension grows with the
cutoff, from \(1488\) at \(l_c=40\) to \(23017\) at \(l_c=160\), while the fourth-moment excess drops from
... to ... (numerical, on the exact rational profiles)." The parenthetical, the label words
"fourth-moment excess", and the exact clause "fails at the fourth by exactly \(1/D_{\mathrm{eff}}\)" earlier
in the same sentence are all KEPT; only the two numerals change.

Stale passage elsewhere: none created by this edit. Note for the orchestrator (not a manuscript change here):
085 r2 must withdraw its claim-7 and recompute its byte contract against the POST of this pass, per the 085
review's sequencing instruction.

## Decisions Taken
RESEARCHER-DECISION (from REVIEW-085-r1 F2), resolved for option (a) — replace the numerals, keep the label:
1. Option (a) keeps the paragraph's own load-bearing exact identity "\(\rho_2-1\) ... equals
   \(1/D_{\mathrm{eff}}\) at \(p=2\)" and the clause "fails at the fourth by exactly
   \(1/D_{\mathrm{eff}}\)" as the operative statement, and makes the quoted numerals agree with it. Option
   (b) (relabel "fourth-moment" -> "eighth-moment", keep 4.0e-3 / 2.6e-4) would require quoting the exact
   eighth-moment excesses or re-adding a "approximately" hedge, since the exact \(\rho_4-1\) values
   (4.0375e-3 / 2.6070e-4) equal the quoted numerals only to 2 s.f. and not the \(6/D_{\mathrm{eff}}\)
   leading form exactly; it also shifts the sentence's narrative off the \(p=2\) obstruction that the
   paragraph (and the 085 insert, and Problem G's proxy-recovery datum) is built on.
2. Textual minimality: option (a) changes 6 characters at 0 net byte length (both numerals keep the same
   token shape `X.Y\times10^{-Z}`); option (b) would add a word and perturb grammar.
3. Rejected alternatives: (b) relabel (above); (c) delete the clause (loses the recovery-direction datum);
   (d) quote more digits (unnecessary precision change beyond the correction's scope; rule: smallest text
   that removes the contradiction).
Routine choice: 2 s.f. display ("6.7", "4.3") matches both the paragraph's existing display style (its other
proxy numerals are 2 s.f. / rounded integers) and the gatekeeper's supplied correction in the 085 review
"Corrected snippet" ("the verified replacements are 6.7e-4 and 4.3e-5").

## Verification scripts (reproduction pack)
All under `proposals/086-g-081-momentlabel-correction/`, run from the repo root with `python -I`; shipped
`.out` files are byte-identical to the runs recorded here.
1. `s1_moment_values.py` (+ `s1_moment_values.out`) — exact-Fraction computation of
   \(D_{\mathrm{eff}}\), \(\rho_2-1\), \(\rho_4-1\) on the two proxy profiles, each by two independent
   routes, with range asserts that pin the 2 s.f. manuscript numerals.
   Re-run: `python -I proposals/086-g-081-momentlabel-correction/s1_moment_values.py`
   Expected invariants: `PASS s1_086` as final line; printed values
   D_eff = 1488.002400 / 23016.894112; 1/D_eff = 6.720419270e-04 / 4.344634837e-05;
   6/D_eff = 4.032251562e-03 / 2.606780902e-04; rho4-1 = 4.037466334e-03 / 2.606998651e-04.
2. `simulate_apply_086.py` (+ `simulate_apply_086.out`) — read-only splice simulation.
   Re-run: `python -I proposals/086-g-081-momentlabel-correction/simulate_apply_086.py`
   Expected invariants: asserts PRE 735,695 B / sha256 a13240a7f7a197ff7cffc26297fe1a6afbdeab749a4de57d6152828c573945ea
   / CRLF 3,834 / bareLF 0; BEFORE count 1; byte delta 0; then prints
   `POST size: 735695`, `POST sha256: b8bd51f6a82d4edebc44f870ff3f07249e723f3302d871243b227ba0b22ca777`,
   `POST CRLF: 3834; bareLF: 0; close-idiom count: 12`, and `no write performed`.
Tool output is a check, not a proof; the proof-level content is the exact-rational identity
\(\rho_2-1=s_2/S_1^2=S_1^{-2}\!\cdot\!\sum g^2=1/D_{\mathrm{eff}}\) (elementary, from
\(h_2=(p_1^2+p_2)/2\)) and the partition form of \(\rho_4\) quoted in the 081 paragraph itself, both
asserted symbolically in the script for the actual profiles.

## Compliance notes
- Rule 7 (no unsourced numerals): every introduced numeral (6.7e-4, 4.3e-5) traces to
  `s1_moment_values.py`/`.out` in this folder AND independently to the 085 review's "Corrected snippet"
  (gatekeeper-verified 6.720e-4 / 4.345e-5); my re-derivation agrees digit for digit.
- Rule 6 (no silent strengthening): the corrected sentence claims no more than the paragraph already claimed;
  the "(numerical, on the exact rational profiles)" caveat is retained.
- Rule 2 (labels): no status/priority/completion word or sentence is touched; the replacement region contains
  only digits and the unchanged words "the fourth-moment excess drops from ... to ...". Banned-word set
  {status, priority, completion, open, critical, programme, derived}: replacement adds ZERO hits (pure
  digit/exponent change).
- Rule 3 (no closure by scope): nothing is closed; the correction strengthens internal consistency of a
  negative datum (proxies off-exactness at finite \(D_{\mathrm{eff}}\)) that argues AGAINST closure.
- Token hygiene: zero new `$`, `[`, `]`, `\cite`, `\ref`, `\eqref`, `\label` tokens (the two `\(`/`\)` pairs
  are identical in BEFORE and AFTER); close-idiom "close nothing in Problem~G." count stays 12; the line
  stays one physical line; CRLF 3,834 preserved; UTF-8 no BOM; byte delta 0.
- Emergence: untouched (pure arithmetic of a classical moment map; no external import).

## Milestone assessment
Routine (a correction pass executing the M3 already recorded under REVIEW-085-r1). I propose no new
milestone; the M3 event belongs to the 085 review. If the gatekeeper classifies the integrated correction
itself under M3 wording ("finds that an already merged claim is wrong"), note that the finding was already
made and recorded by the 085 gatekeeper; this package is the fix, not a new finding.

## Status-label recommendation
Current critical-path set re-derived from the digest + targeted reads of appH Ledger-label blocks and the
ledger tail: A, B, C, D1, E, F, G-derived, N OPEN / CRITICAL PATH (per current full-GR / matrix-derived
scope; H, I, J optional in their scopes). All labels UNCHANGED by this package; Problem G's block at
L3026-3029 quoted verbatim above and not edited. No label change proposed.

## Author decision needed
None. (The F2 wording choice was flagged RESEARCHER-DECISION and is resolved to option (a) in Decisions
Taken, per the autonomous-mode directive.)

## Remaining open step
Nothing in this package advances or closes any Appendix H problem. After integration: (1) 085 r2 (F1 insert
clause, F3/F4/F5 fixes, claim-7 withdrawal) must be recomputed against this pass's POST (735,695 B /
b8bd51f6a82d4edebc44f870ff3f07249e723f3302d871243b227ba0b22ca777) — note this pass has byte delta 0, so the
PRE size is unchanged but the hash moves; (2) Problem G and `G.moments-derivedprofile` remain exactly as
recorded in the 085 review's "Scope of what is established".

## Special instructions for the gatekeeper
- Verify BEFORE occurs exactly once in the live file and matches the shipped `simulate_apply_086.py`
  constants byte-for-byte; re-run both scripts with `python -I` and diff against the shipped `.out`.
- Re-derive the fourth-moment excess yourself (the identity \(\rho_2-1=1/D_{\mathrm{eff}}\) is elementary;
  the profile convention is in `proposals/081-g-edge-moments/s3_profile_concentration_r2.py`).
- Confirm the corrected sentence is internally consistent (exact \(1/D_{\mathrm{eff}}\) clause vs the two
  2 s.f. numerals vs the quoted rounded \(D_{\mathrm{eff}}\) values 1488 / 23017).
- This package must NOT be expanded: no new text beyond the clause swap; assert byte delta 0 and that no
  banned word, macro or idiom count moved.
- Scope limit: the only manuscript change is the clause above in `chapters/appH-microscopic-proofs.tex`;
  `proposals/` files here are records, not integration inputs except the snippet constants.
