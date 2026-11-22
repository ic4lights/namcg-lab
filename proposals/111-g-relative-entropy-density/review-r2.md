VERDICT: ACCEPT proposal 111 round 2, proposal-r2.md sha1 f3d9ee751e1a1114c75de19d4e680acde2027191 with battery inputs at pinned shas, cleared for integration as ordinal 41 at input tier; Problem C/G remain OPEN with G CRITICAL PATH, PROGRAMME-CONDITIONAL; this package recorded as conditional derivation-grade input to Problem G missing steps (i)-(ii) | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

Basis: digest + targeted reads + review-r1 + scan reports (full 30-file split scan completed 2026-11-22, reports/ledger.md SCAN-20261122, at pre-ordinal-40 state; sole delta = certified ordinal-40 insertion at appH L732-740; no re-scan required for a record-level revision round). Digest re-verified this pass: `DIGEST CURRENT` at head 23266972cd07dd01497abe5e0962810fa059db63.

## Verdict
All five r1 findings are verifiably closed by independent re-checks (not changelog trust), the diff is exactly the six claimed record lines, the corrected c0 convention is confirmed against ground truth at 1e-16, and the (star) uncentered-moment clause is confirmed at 1e-15; ACCEPT with the integrator pinning only the table-1 full shas below.

## Source reading
digest + targeted reads (basis above). Read in full: proposal-r2.md (all 396 display lines), r1_to_r2.diff, manifest.md, review-r1.md, run_modular.out, _common.py, check_modular.py; targeted: appH L3195-3202 (Missing-step quote), L3099-3112 (G ledger label), L529-536 (C ledger label), ch17 L475; p1_symbolic_a0.py L11 (F6 comment). No unreadable files.

## Claim under review
Record-level r2 of a verified building block for Problem G missing steps (i)-(ii) at input tier: exact identity (star) S(rho1||sigma0) = -S(rho1) + 1/2 Tr(A0 G1) - c0 with c0 = -ln Z0 = sum_j ln(2 sinh(h(nu_j)/2)), G1 the uncentered symmetrized second moment per H2; 18-check battery fixed input; gap G-R named. No new mathematics. Original target: `Status: OPEN. Priority: CRITICAL PATH.` — appH L3102-3106 read live this pass: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a scope-limited model; G remains OPEN and neither satisfies the matrix-derived criterion." r2 quotes it verbatim. Problem C live (L532-536): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL..." — consumed by nothing here (r2 Dependencies); both remain OPEN, not normalized or altered by this package.

## Pins (re-hashed from disk this pass; all 25 manifest rows + full shas match)
| file | sha1 (full for integrator inputs) | manifest match |
|---|---|---|
| proposal-r2.md | f3d9ee751e1a1114c75de19d4e680acde2027191 (27143 B) | f3d9ee751e ✓ |
| r1_to_r2.diff | b50734e91a0edb06b2edf2e5c7c43421a1da8f2a (6284 B) | b50734e91a ✓ |
| _common.py | 52497c0c45683561078e1ec23e2c89b907beec15 | ✓ (FROZEN) |
| check_modular.py | cd982322f9052bc48096fd44303683820e5f1e62 | ✓ (FROZEN) |
| run_modular.out / rerun.out | 7247af5bf4590b3f3e3f856b9b70b9b74b940427 / identical | ✓ |
| p1_symbolic_a0.py | 8d2bd3624d0cd04a612c229b734a615b4f094885 | ✓ (FROZEN; false comment still at L11, deferred per F6) |
| p2_fock_srel.py | b6bac2a036398994d7b2f848ee99914eeab532da (1565 B) | ✓ (supersedes stale 0904f2f7d8; manifest now pins exactly this) |
| p3_fock_srel_cold.py | 819d478da6fe6c4faec8adec96039023e1b4b8ce | ✓ |
| surg_r2.py | 7bc53cbdd2d4e5ae723dda3b0554c92fe6f96c78 | ✓ |
| review-r1.md / proposal-r1.md / manifest.md | 48118920cf8cad4f… / 7aee411e3f03452c… / 51e2cdc50db939cf… | ✓ |
| stab probes/runs, diag/probe/deadpass | all 10 prefixes match manifest rows | ✓ |

## Diff-audit result
The diff file is LF-encoded with a doubled newline after every record; after normalizing empty lines, I applied it to proposal-r1.md bytes with a hand-written patcher asserting every context and minus line against the actual r1 bytes: 5 hunks, **exactly 6 minus lines** (title; F2a Result ¶1; F4 quotation; F2b C4; F5 C6; F3 Test A), 36 plus lines, and the result is **byte-identical to proposal-r2.md (27143 = 27143, MATCH True)**. Consequently every claim of scope is proven, not asserted: the (star) equation line is untouched (context line); the only battery-table change is the Test A row, and a token-level diff of that row shows the sole change `1.5e-07` → `9.7e-07`; the C6/(star) sentence gains only the F5 clause; everything else is the changelog block and title.

## Per-finding closure
- **F1 (blocking) CLOSED.** Manifest restated from disk; all 25 rows re-hashed by me and match; p2 full sha1 confirmed; SUPERSEDED r1 table preserved with the STALE-PIN annotation and the probe_34x absence correction.
- **F2 (major) CLOSED.** See ground-truth re-derivation below. Zero occurrences of the wrong label "c0 = ln Z" in r2; all 8 `ln Z` occurrences are correct-convention uses or the disclosed Test A content note.
- **F3 (minor) CLOSED.** run_modular.out L2 observed dSfock = 9.66e-07 at (17,0.70,1); r2 Test A reads `&lt;= 9.7e-07`; changelog's three values 9.66/1.47/1.02e-07 match run_modular.out L2-4; tol 5e-3 unchanged.
- **F4 (minor) CLOSED with non-blocking note.** Live appH L3199 reads "...boundary cut and \(\partial M\) under which"; the r2 quotation now carries the source symbol (r1's required action). Note: r2 renders it as the apposition "and the boundary \(\partial M\) under which" — the words "the boundary" are a gloss absent from the source; the changelog discloses the rendered string, so provenance is auditable. Non-blocking here, but that gloss must not be imported into manuscript text as a verbatim quotation of L3199.
- **F5 (minor) CLOSED.** r2 C6 clause matches H2/battery `cov_from_rho` (symmetrized uncentered products). Fresh probe (displaced single-mode thermal, nu = 0.7, alpha = 0.8, dim 81): direct S(rho1||sigma0) vs (star) with uncentered G1: err = 1.8e-15; with centered covariance: err = 1.1467260603059555 = 1/2 m^T A0 m = 1.1467260603059541 to 1e-15. The centered form fails by exactly the claimed amount; the uncentered form is exact.
- **F6 deferral CORRECTLY TAKEN.** Changelog L26-30 and manifest L30 both record it; p1_symbolic_a0.py unmodified (8d2bd3624d, false comment still at L11 exactly as described); no claim depends on the comment (r1 hand-derived the encoded Kf_term).

## F2 ground-truth re-derivation (fresh scratch)
Single-mode thermal, nu = 0.7: battery `A_of_G(nu I)` returns A0 = h I (offdiag 0); with Z = Tr exp(-h(a†a + 1/2)) computed independently via expm (dim 41): c0_from_nus = 0.7135581778200729, -ln Z = 0.713558177820073 (diff 1.1e-16), ln(2 sinh(h/2)) and c0_from_G_alt identical. First law S0 = 1/2 Tr(A0 G0) - c0: err 8.9e-16 vs spectrum entropy; wrong-sign control (+c0) fails by 2·c0 = 1.427 (non-tautological). r2's Result ¶1, C4 (`c0(G) = -ln Z(G)`, both closed forms), C6 proof (`Z0 = exp(-c0)`, `+ ln Z0` step), and (star)'s `- c0` are mutually consistent and match the battery's dZ = |ln Z + c0| (check_modular.py L43).

## Checks performed
Pins and full shas (direct); diff byte-application (direct); battery re-run from scratch copy with the documented `__file__`-injected exec one-liner: `python -I -c "...exec(open('check_modular.py').read(), g)"`, 18 checks 0 failures, output byte-identical to run_modular.out (7247af5bf4, 2250 B) — r1's negative controls stand and were not redone (record-level round; stated skip); F2 and F5 probes (direct, fresh); appH L3199, L3102-3106, L529-536, ch17 L475 verbatim quotes (direct); anchor "Edge entropy of a matrix block" unique (count 1) in the live tree post-ordinal-40; ledger SCAN-20261122 and R111-STABILIZED present. Not verified: JLMS arXiv record (r1 fetched live; r2 imports nothing from it and keeps the mischaracterization flag unsoftened — unchanged from r1); Araki-Yamagami remains marked not independently verified with nothing imported.

## Hygiene results
No status/priority/completion wording added; explicit "no label changes" and "Nothing is closed; Problem G remains exactly as recorded"; steps (iii),(iv) NOT fed; rule-6 classifications retained; new numerics all traceable (9.66/1.47/1.02e-07 and 5e-3 ← run_modular.out; rest are disclosed hashes); quarantined files named only in the non-citation declaration (r2 L41); no closure-by-scope language; emergence intact (L339-340: no fundamental metric). Proposal-file mixed EOLs: `proposals/` is not manuscript; the .tex CRLF rule is unaffected.

## Findings
none blocking/major. One non-blocking note (F4 appositional gloss, above) for the integrator's awareness at insert time.

## Scope of what is established
Unchanged from review-r1's determination: (star) proved exact algebra (faithful Gaussian reference; uncentered symmetrized second moment); n=1 positivity exact; battery conditional-verified on the certified grid; G-R localization interpretation-tier; steps (i)-(ii) fed at input tier only. DERIVED: none of Problem G. PROGRAMME-CONDITIONAL input. Problem G remains OPEN / CRITICAL PATH; Problem C remains OPEN / CRITICAL PATH; nothing in this round changes any status.

## Recommended disposition
Integrate as ordinal 41, input tier, integrating proposal-r2.md at sha1 f3d9ee751e1a1114c75de19d4e680acde2027191 and pinning only the full shas in the pins table; the integrator re-verifies the appH insertion anchors against the then-current working tree and the F4-gloss note above.

## Corrected snippet
None needed; no new physics; no extra assumptions.

END REVIEW 111 r2
