VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: regressing | OPEN: 1/1

Gatekeeper r2 review, remote/claude, 2026-11-19. The orchestrator saved it here because the gatekeeper is read-only.

Source reading: digest + targeted reads. The whole Problem G section (appH L2886-2966) was read in full. The full scan is pending.

## Checks
- v1-v3 re-run: identical, PASS.
- apply_build_r2: pre 779bfcac... / post c541fb20... match, 394 pp, 0 undefined, anchors unique.
- Re-derived:
  - slot law: entries independent and circular, a independent of r, Gamma = 0, at most l_c-1 slots, rho2-1 >= 1/(l_c-1), all exact;
  - moment map; Isserlis coupled-slot identities; frame-law locus; 086 now moot.
- Proxy adjudication: the 1488 "proxy" is a separately supplied mode-count profile, not the Row length slot law, so the researcher was right to drop it. The group6 M1 consolidation carried it as if it described the state, which was a reviewer error.
- Independent profile computation (tridiagonal Casimir per offset, cross-checked against a dense computation and exact CG at N=12). At N=400, M=200:
  - l_c=40, f=l/2: W_block 27.856, g_u/W 0.0230, D_eff 37.96, 6N(W-g_u)/l_c^3 = 1.0206.
  - l_c=20: g_u/W 0.0441, D_eff 18.68, 1.0414.
  - f=l(l+1)/4: D_eff 38.07, 1.069.
- v3 diagnosis: its tensors are not orthonormal at N=400 (<T40,3,T38,3> = 0.97), and it reports W_block 413.3, which exceeds the full-row sum of 56.4.

## Findings
1. BLOCKING: D_eff = 29.5 (and the g_u/W shares 0.0085/0.042) come from the broken v3. Correct values: 38.0; 0.0441 (l_c=20), 0.0230 (l_c=40).
   - Fix with (a).
   - Rebuild v3 with a stable construction (tridiagonal Casimir) and assert the full-row sum at the N used.
   - Correct the proposal record.
2. MAJOR, PRIOR-CLAIM-ERROR in integrated text (appH L2922, Row length paragraph). W is defined as the full block-row sum, but the paragraph's numbers (1.021, 1.041, 1.07) are 4s^2(W-g_u). Fix with (d), folded into this package.
3. minor: the pseudo-covariance needs nonzero charges of one sign. Fix with (b).
4. minor: the second-moment match holds at a=0. Fix with (c).
5. minor, no action: W is defined locally in each paragraph.
6. procedural: the full scan is pending (3(c)).

All else verified: placement, the clause extension (status sentence once), no "diagonal-cut" wording, the scoping of paragraph 2, and the 087/088 no-go.

## Corrected snippets
(a) Replace `\(D_{\mathrm{eff}}=29.5\) at \(N=400\), \(M=N/2\), \(l_c=40\) and \(f=\nu l/2\) (numerical)` with `\(D_{\mathrm{eff}}=38.0\) at \(N=400\), \(M=N/2\), \(l_c=40\) and \(f=\nu l/2\) (numerical)`

(b) Replace `since distinct entries carry distinct charges under that rotation;` with `since the entries carry distinct nonzero charges of one sign under that rotation;`

(c) Replace `The reading of the rows from the edge data in the transplanted selection rule therefore matches the averaged charge moments exactly at the second moment,` with `The reading of the rows from the edge data in the transplanted selection rule therefore matches the averaged charge moments at \(a=0\) exactly at the second moment,`

(d) In appH L2922, replace `with \(W\) the sum over the boundary row inside the block.` with `with \(W\) the sum over the boundary row inside the block without its entry at \(u\), while \(\tfrac12\langle\operatorname{Tr}Q^{2}\rangle\) is \(4s^{2}\) times the full sum (exact).`

## Disposition
- Researcher r3 applies (a)-(d), fixes v3 and regenerates the hashes. Then the full scan in passes.
- No label change. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- Open avenues:
  (1) a core-produced state;
  (2) typical moments or the l_c -> infinity limit;
  (3) the non-compact/Lorentzian spacetime-block and split-algebra routes.
