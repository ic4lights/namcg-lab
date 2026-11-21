VERDICT: ACCEPT | MILESTONE: NONE | FLAGS: NONE | PROGRESS: improving | OPEN: 0/0

## Scope & reads

Digest + targeted reads (full scan still not due; next at ordinal 35). r2 round: re-read `proposal-r2.md` in full; verified `insert-r1.tex` vs `insert-r2.tex` at byte level; verified the three marked correction sites in `findings.md` (L25, L26, L47); inspected `hygiene_102.out`/`simulate_apply_102.out` regeneration; re-checked live appH integrity and my own byte-splice. `s4_dirichlet_rho_direct.*`, `s2_uniform_rho_r2.*`, `s1_frame_identities.*` unchanged from r1 (r1 gatekeeper reproduction stands: s4 sha8 7b293544, s4 .py sha8 69a04377, all re-derived at general D in review-r1). No manuscript text beyond `insert-r2.tex` is proposed for integration; `findings.md` changes are record-only.

## Re-derivations (changed claims only)

1. **Centring correction.** Given (independently re-derived at r1, unchanged) Var(s_2) = 4(D−1)/((D+1)²(D+2)(D+3)) ~ 4/D³, the centred L² norm is ‖s_2 − E s_2‖₂ = sqrt(Var) ~ 2 D^{-3/2}, so "s_2 − E s_2 → 0 in L² at rate D^{-3/2}" is correct, and it is now internally consistent with the preceding clause "D³ Var(s_2) → 4". CONFIRMED.
2. **Byte arithmetic (my r1 note vs r2 record).** The mandated clause strings: old `\(s_{2}\to0\)` = 13 bytes, new `\(s_{2}-\mathbb{E}\,s_{2}\to0\)` = 31 bytes; the inserted substring `-\mathbb{E}\,s_{2}` is 18 ASCII bytes. 3155 + 18 = 3173. RULING: the researcher is right and my r1 "13 added bytes / expected 3168" was a miscount (I wrote the length of the old clause in place of the length of the addition). The verbatim clause governed and must not be resized to hit 3168 — the r2 handling is correct.
3. **Diff minimality.** `insert-r2.tex` equals `insert-r1.tex` with exactly one occurrence of the old clause (count 1 in r1, 0 in r2; new clause count 1 in r2) replaced, the replace-back roundtrip is byte-equal to r1, and r2 == r1.replace(old, new) byte-for-byte. First (and only) difference at byte offset 2137, inside the target sentence. So no other manuscript-relevant text changed. CONFIRMED.
4. **findings.md corrections read as specified.** Site at L25: s3b Var line struck as "nonnegative for every integer D >= 1 — the earlier 'negative at small D' claim was wrong", with the correct defect record (expectations = true values / D; gap line = floor − E_true, sign-flipped) — matches my Finding 2 requirement. Site at L26: centred form with the explicit note that the uncentred decay is at rate D^{-1} — matches Finding 1. Site at L47: same correction in the OPEN list. All three carry `[r2 correction per review-r1 Finding k]` markers. CONFIRMED.

## Findings

1. **MINOR (gatekeeper-side, self-correction; no action required) — Location: review-r1, Corrected snippet section.** My "expected insert bytes 3168 / 13 added bytes" was an arithmetic slip; the correct figure is 3173 / 18 added bytes, as the r2 package states and as I have now re-verified. Recorded so the ledger does not inherit the wrong number from my r1 review.
2. Findings 3-4 (r1 MINOR, optional) declined with reasons: both were explicitly marked "not required" at r1; the stated rationales (context fixes the index reading; the preceding sentence already enumerates p=2,3,4) are acceptable to me. No residual finding.

No open blocking or major findings.

## Script reproduction

All from repo root:
- `python -I proposals/102-g-profile-selection-output/hygiene_102.py` — exit 0, final line `HYGIENE PASS`; `insert-r2.tex bytes = 3173`, `sha8 = 86d4b849`, ASCII-only, CRLF 1/bareLF 0, braces 71/71, no \ref/\label/\eqref, closing idiom count 1.
- `python -I proposals/102-g-profile-selection-output/simulate_apply_102.py` — exit 0, final line `SIMULATION PASS`; PRE 798457 / `cfb6af516017367f` / CRLF 3866 / bareLF 0 / no BOM; `PIN count in appH bytes = 1`; payload 3175; POST 801632 / sha16 `e37ca5385996df34` / CRLF 3868 / bareLF 0; POST == PRE + payload = True; PIN still 1 in POST.
- Independent gatekeeper byte surgery (my own, not the researcher's script): live appH 798457 / cfb6af516017367f / CRLF 3866 / bareLF 0 — untouched; the PIN (full eigenvalue-reduction paragraph line + CRLF + blank CRLF) occurs exactly once; bytes after the pin are `\emph{Transport of the profile coordinate`; manual splice = live + insert-r2 (3173, 86d4b849, CRLF-terminated) + blank CRLF gives 801632 / `e37ca5385996df34` / CRLF 3868, and `scratch/102_sim_post.tex` is byte-identical to it; the corrected clause occurs exactly once in POST; paragraph separations on both boundaries are exactly one blank CRLF line.
- s4 / s2_uniform_rho_r2 unchanged from r1 (r1 reproduction: exit 0, `ALL CHECKS PASS` / `ALL EXACT CHECKS PASS`).

## Verdict rationale

The single blocking finding (uncentred L² rate claim) is fixed with the exact mandated clause, verified at byte level and mathematically re-derived; the record-only Finding 2 is corrected in place at all three sites with the specified content; the byte-count discrepancy resolved in the researcher's favour and against my r1 note (recorded as a self-correction). The central mathematical content — the closed-form E[rho_p], the s_2 moments and positivity, the floor-gap factorizations, the pointwise pin, and the honest rule-6 classification with full no-closure scoping — was independently re-derived at r1 and is untouched. Problem G remains `Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL` with missing steps (i)-(iv) explicitly unchanged; nothing here alters any label, so this remains a non-milestone exact-statistics supplement upgrading the integrated D=3 numerical confirmation to closed symbolic forms.

## Integration spec (final)

- File: `chapters/appH-microscopic-proofs.tex`, pure insertion only; payload text = `proposals/102-g-profile-selection-output/insert-r2.tex` (3173 B, sha8 `86d4b849`, single CRLF-terminated line, ASCII, no BOM) + one blank-CRLF separator = 3175 B payload.
- Anchor PIN (assert count == 1 before write): the complete current line 3195 (`\emph{Eigenvalue reduction of the edge Gram and the Jacobian origin of the beta factor.}` paragraph line) + its CRLF + the following blank-CRLF line; insert lands immediately after that separator and immediately before `\emph{Transport of the profile coordinate along the pushforward family and its moment coordinates.}`.
- PRE: 798457 B / sha256-16 `cfb6af516017367f` / CRLF 3866 / bareLF 0 / no BOM (re-verify against the live tree at integration time per the serialization rule).
- POST (assert): 801632 B / sha256-16 `e37ca5385996df34` / CRLF 3868 / bareLF 0 / PIN still count 1; then `python scripts/build_check.py` (expect build OK; the known ledger-CRLF diff-check EOL artifact, if it appears on appended ledger lines, is not a manuscript failure) and digest refresh; integration ordinal 33. Do not integrate `insert-r1.tex` (retained-superseded).

## Recommended disposition

Integrate as-is per the spec above. Scope established: exact flat-Dirichlet statistics of rho_p at p=2,3,4 and of s_2 = 1/D_eff at general D (in-folder exact, gatekeeper-re-verified), including centred L² concentration at rate D^{-3/2}; they characterize the named a=1, β=0 family member, evaluate no matrix integral, select no profile, supply no state, leave missing steps (i)-(iv) unchanged, and close nothing in Problem G.