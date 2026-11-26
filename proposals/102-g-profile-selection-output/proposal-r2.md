PROPOSAL 102 r2 | G (entropy/stationarity) - G.moments-derivedprofile edge | flat-Dirichlet exact statistics of rho_p | revision round

## Response to review-r1

Finding 1 (BLOCKING) - fix applied verbatim as mandated. `insert-r2.tex` = byte-copy of
`insert-r1.tex` with the single clause `so \(s_{2}\to0\) in \(L^{2}\) at rate \(D^{-3/2}\)`
replaced by `so \(s_{2}-\mathbb{E}\,s_{2}\to0\) in \(L^{2}\) at rate \(D^{-3/2}\)`; the old
clause occurs once in r1 and zero times in r2, the new clause occurs once, and the
replace-back roundtrip is byte-equal to insert-r1.tex (orchestrator-verified byte surgery).
`insert-r1.tex` is retained, superseded, never integrated. Byte-count note for the gatekeeper:
review-r1's "13 bytes / expected insert 3168 B" is a miscount - the two ASCII clause strings
differ by 18 bytes (`-\mathbb{E}\,s_{2}` is 18 ASCII bytes), so insert-r2.tex measures 3173 B
(sha8 86d4b849, one CRLF-terminated line, ASCII, no BOM). The verbatim mandated clause governs
and all byte counts in this round are measured, not predicted; recommend the gatekeeper
re-check this arithmetic at r2.

Finding 2 (MAJOR, record only) - applied. `findings.md` corrected in place at three sites, each
marked inline `[r2 correction per review-r1 Finding 2]` (and one `[r2 correction per review-r1
Finding 1]` for the centred phrasing): the earlier "s3b Var[sigma] line evaluates negative at
small D - impossible" claim is struck as wrong (the s3b Var line is nonnegative for all integer
D >= 1); the correct defect record replaces it - s3b's Check-I/II expectations equal the true
values divided by D, and its gap line is floor - E_true, sign-flipped relative to E - floor; and
the "sigma -> 0 in L2 at rate D^{-3/2}" phrasing is corrected to the centred form
(sigma - E[sigma] -> 0; the uncentred L2 decay of sigma itself is at rate D^{-1}).

Findings 3-4 (MINOR, optional) - DECLINED this round to keep the package minimal. Finding 3
(p-notation word): the context resolves the ambiguity without a new word - subscripts 2,3,4,
the pin clause "at p = 2", and L3177's `p!\,h_{p}(g)/W^{p}` all fix the reading as the integer
index. Finding 4 ("three means" qualifier): the preceding sentence already enumerates
p = 2, 3, 4, so the scope is exact as written.

## Unchanged from r1

All other content of `proposal-r1.md` stands unchanged (TARGET, DERIVATION SUMMARY, rule-6
classification table, EVIDENCE FILES narrative, verdict criteria) and was independently
re-confirmed by the gatekeeper (re-derivations 1-7, script reproduction, splice mechanics,
rule-6 table honesty, no-closure scope against the four governing integrated sentences). The
gatekeeper's observation that the pointwise pin holds for all profiles and all p by the
partition form is stronger than the package's own numerical verification and is NOT further
exploited in this round.

## Byte contract (r2, from simulate_apply_102.out)

```
PRE bytes = 798457
PRE sha256-16 = cfb6af516017367f
PRE CRLF = 3866
PRE bareLF = 0
PIN count in appH bytes = 1
payload bytes (insert + blank-CRLF separator) = 3175
POST bytes = 801632
POST sha256-16 = e37ca5385996df34
POST CRLF = 3868
POST bareLF = 0
POST == PRE + payload bytes = True
SIMULATION PASS
```

Anchor unchanged: pure insertion in `chapters/appH-microscopic-proofs.tex` AFTER the
"Eigenvalue reduction of the edge Gram and the Jacobian origin of the beta factor." paragraph
and BEFORE `\emph{Transport of the profile coordinate`; PIN (complete preceding paragraph line +
its CRLF + the single blank-CRLF separator) occurs exactly once. The byte counts differ from
review-r1's expectation (3168/3170) for a documented reason: the gatekeeper's ASCII clause
length was miscounted (18 bytes, not 13); the verbatim clause governs and the measured
contract is PRE 798457 + payload 3175 = POST 801632. `insert-r2.tex`: 3173 B, sha8 86d4b849,
ASCII, CRLF-terminated single line, no BOM, no \ref/\label/\eqref (HYGIENE PASS, exit 0).

## Evidence-file changes

- `insert-r2.tex` NEW: 3173 B, sha8 86d4b849 (this round's manuscript text).
- `_mk_r2_102.py` transient generator RETAINED as provenance (agent deaths #38/#39 on this
  item; the generator's 18-byte correction note was applied as orchestrator byte surgery and the
  generator run by the orchestrator).
- `insert-r1.tex` retained-superseded (never integrated).
- `findings.md` corrected in place with the r2 markers listed above.
- `hygiene_102.py`/`hygiene_102.out` and `simulate_apply_102.py`/`simulate_apply_102.out`
  retargeted to insert-r2.tex with documented `# r2:` notes (including the 13->18 byte
  correction note); outputs regenerated.
- `s4_dirichlet_rho_direct.*`, `s2_uniform_rho_r2.*`, `s1_frame_identities.*`: unchanged from r1
  and gatekeeper-reproduced at the review.

## Reproduction pack (r2)

Run from repo root:
- `python -I proposals/102-g-profile-selection-output/hygiene_102.py` -> final line
  `HYGIENE PASS`, exit 0; prints insert-r2.tex bytes = 3173, sha8 = 86d4b849, ASCII-only,
  braces balanced, closing idiom count 1.
- `python -I proposals/102-g-profile-selection-output/simulate_apply_102.py` -> final line
  `SIMULATION PASS`, exit 0; prints exactly the quoted PRE/payload/POST/PIN lines above.
- `python -I proposals/102-g-profile-selection-output/s4_dirichlet_rho_direct.py` and
  `python -I proposals/102-g-profile-selection-output/s2_uniform_rho_r2.py`: unchanged from r1
  (final lines `ALL CHECKS PASS` / `ALL EXACT CHECKS PASS`, exit 0).

No status, priority or completion-classification change is proposed or implied.
