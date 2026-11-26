VERDICT: ACCEPT insert-g-srel.tex as the ordinal-41 manuscript-bound text, sha1 c3d119f6c00931f6bd5843a99c80cec0f445e030 | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0
Disposition: integrator splices this exact file (sha1 c3d119f6…) immediately before the unique `\paragraph{Edge entropy of a matrix block` line in chapters/appH-microscopic-proofs.tex (working-tree sha1 882de86864d9e9b2e14219bf223a3a0c0dd7d11f), preserving the existing blank line and adding one after (cert convention, reproduced below); Problem G remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; no status, priority or completion-label change.

## Pins
| file | sha1 | size | expected | match |
|---|---|---|---|---|
| insert-g-srel.tex | c3d119f6c00931f6bd5843a99c80cec0f445e030 | 2452 | c3d119f6c0…, 2452 | OK |
| payload-note.md | 069e3678b3a17b9613b7bb893a4312950ab94613 | 3761 | 069e3678b3, 3761 | OK |
| cert-r111p.py | b95bd9aaab53cebac60b0a29e1209f30f30d7bb8 | 3030 | b95bd9aaab, 3030 | OK |
| review-r2.md | 5cb994b96b1f13325c24887c7c2e84a7da4f1731 | 9467 | 5cb994b9 | OK |
| appH-microscopic-proofs.tex | 882de86864d9e9b2e14219bf223a3a0c0dd7d11f | 821924 | 882de86864… | OK |

Digest head 23266972cd07dd01497abe5e0962810fa059db63 confirmed. Payload pure CRLF (6/6/6 CR/LF/CRLF, no lone terminators, no BOM, ends CRLF). Basis: digest + targeted reads; full-scan basis SCAN-20261122 (ledger) at pre-ordinal-40 state, sole deltas = certified ordinal-40 insertion and this payload (per review-r2 L3 basis).

## Splice-repro
Anchors: "Closing the matrix-derived criterion for Problem~G requires" count 1; "schematic." count 1; "\paragraph{Edge entropy of a matrix block" count 1; order BEFORE < AFTER. Exact gap verified b'schematic.\r\n\r\n' — the BEFORE block ends immediately (blank line only) before the AFTER paragraph; no stray text. Raw splice (payload bytes as-is at anchor): POST sha1 1bad26c52d18fdb323bf8734b0f56911bcdf2319, size 824376 = 821924 + 2452, payload appears exactly once -> scratch/gk111p_post.tex. Cert-form splice (payload + CRLFCRLF separator, as cert-r111p.py does): sha1 60a8eb47bb32184d60d0165483a635f9a331c2b3 = payload-note's recorded spliced sha1 = the cert run's spliced appH sha1. Check 7: cert's copy differs from my raw POST only by the 4-byte blank-line separator at the junction, same insertion point — content-identical, whitespace-only; not a finding.

## Numerical trace
| payload number | r2-tier source | status |
|---|---|---|
| 3.4e-3 .. 1.45e-2 | proposal-r2 L69-70 (P2; review-r1 L20: 3.41e-03/6.00e-03/1.45e-02) | OK |
| 3.7e-3, 6.2e-3 | proposal-r2 L71 and L308 (p3 gapS 3.7e-03/6.2e-03) | OK |
| matches to 10^{-6} | proposal-r2 L70 + L308 p3 recorded gapK 1.4e-06/3.1e-08 | OK (minor note 1) |
| <=3e-2 tolerance | proposal-r2 L74 "documented Test B relative-covariance tolerance (relcov <= 3e-2)"; table row B L164 | OK |
| mu=0.01, N>=12 sampled, h unresolvable in double precision, fixed-input limit not a failure | proposal-r2 L169-175 verbatim ("h(nu)=ln((nu+.5)/(nu-.5)) is unresolvable in double precision… mu=0.01 cuts… (N >= 12 sampled)… fixed-input limitation") | OK |
| 18 checks, no failures | proposal-r2 L40/61/168 "RESULTS: 18 checks, 0 failures" | OK |
| nu_j > 1/2 | proposal-r2 L51, L154 | OK |
| c0 = -ln Z0 = sum_j ln(2 sinh(h(nu_j)/2)) | proposal-r2 L12 (F2 fix), L52, C4 L141-143 | OK |
| h(nu) = ln((nu+1/2)/(nu-1/2)) | proposal-r2 L64, L171 | OK |
| 1/2 m^T A0 m centered-miss | proposal-r2 C6 (F5) clause; review-r2 F5 probe (err 1.8e-15; centered fails by 1/2 m^T A0 m to 1e-15) | OK |
| G-R named, symbolic two-state-anchor fix route | proposal-r2 L75, L316-319, L375 | OK |

No payload number lacks an r2-tier source.

## Identity check
Payload display S(rho_1||sigma_0) = -S(rho_1) + 1/2 Tr(A_0 G_1) - c_0 matches r2 (star) L148 symbol-for-symbol (argument labels A0(G0)/c0(G0) elided only). sigma_0 = exp(-R A0 R/2)/Z0 <- L50; log sigma_0 = -1/2 R A0 R - ln Z0 <- L149; -c0 sign correct — review-r2 F2 ground-truth re-derivation (c0 = -ln Z at 1.1e-16; wrong-sign control fails by 2c0). G1 = Tr rho_1(R_iR_j+R_jR_i)/2 uncentered symmetrized <- C6 L147. "exact algebra… proof does not use the Fock construction" <- L56-58, L74-75. Tier wording never above review-r2 "Scope of what is established" (exact algebra; battery conditional-verified; input tier).

## Hygiene
Status:/Priority:/Completion: 0; \label/\ref/\cite/bibitem 0; hard-coded chapter numbers 0 ("Chapter" 0); "Missing step" and "and the boundary" absent (F4 satisfied); no 1512/Jafferis/Araki strings, cites nothing (payload-note item 9); no chat/process language ("proposed","researcher" 0); no closure-by-scope wording; exactly one display (\[/\] 1/1); closing sentence reads as required: feeds (i)-(ii) at input tier only, does not feed (iii)-(iv), closes nothing, Problem~G record unchanged — matches r2 landing note L289-295; Problem~G tilde spelling matches appH usage (33 occurrences). r2 tier classifications retained verbatim in sense ("exact algebra, confirmed numerically", "(numerical)", "verified algebraically and supported numerically", "resolution limit, not a failure").

## Certificate
python -I proposals/111-g-relative-entropy-density/cert-r111p.py (my re-run, fresh scratch/r111p): SUMMARY PAGES 434 ERRORS 0 UNDEF_CITS 0 UNDEF_REFS 0 MULTIPLY 0 PASS payload sha1 c3d119f6c00931f6bd5843a99c80cec0f445e030; pass rc 0/0; independent grep of the spliced-tree pass-2 log: ! lines 0, undefined references 0, undefined citations 0, multiply-defined 0. Spliced appH sha1 agrees with my independent cert-form recomputation.

## Findings
- minor (no action): payload "matches to 10^{-6}" — max recorded p3 gapK is 1.4×10^{-6} (proposal-r2 L308); this is r2's own accepted-tier phrasing ("matches to 1e-6", L70) over the recorded value and stays within the certified tier; not revision-grade for a payload round.
- minor (informational): raw splice vs cert spliced copy differ only by the 4-byte CRLFCRLF paragraph separator at the junction (same anchor, whitespace only); integrator should follow the cert convention (blank line before and after the inserted block), which reproduces sha1 60a8eb47bb….

## Corrected snippet
None required; integrate as-is.

END REVIEW 111 p1
