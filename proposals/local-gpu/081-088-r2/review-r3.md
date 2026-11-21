VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

Gatekeeper r3 review, remote/claude, 2026-11-19, saved here by the orchestrator. Source reading: digest + targeted reads (Problem G, appH L2886-2966). Live appH sha is 779bfcac....

## Checks
- (a)-(c): applying them to insert_r2 gives insert_r3 byte for byte (sha 8dfc3ac0..., 5236 B).
- (d): applied verbatim. The anchor is unique at L2922.
- Re-derived:
  - Tr Q^2 = 16a^2 + 8r;
  - <l^2> = 4s^2(W_block - g_u), exact without neglecting Im alpha;
  - 1/2<Tr Q^2> = 4s^2 W_block.
- (b) and (c): verified.
- v1, v2 and v3_r3 all PASS. v3_r3 is stable and reproduces the table.
- Independent sympy Wigner-3j cross-check at N=400 reproduces all values. The symmetric local exponents (2.981 / 3.936) come out for W - g_u, confirming that the integrated numbers are W - g_u quantities.
- apply_build_r3: pre and post hashes match (b71bb0ac..., 682008 B). 394 pp, 0 undefined.
- No "29.5" left in chapters/.
- Flag (ii), the nu-dependence of the normaliser: it holds for every nu>0 (W(nu) = nu W(1); s^2 = nu^2 M(N-M)/2). No edit needed.

## Findings
1. minor, required (flag (i)). In rowlen line 2, replace
   `with \(W\) the sum over the boundary row inside the block without its entry at \(u\), while \(\tfrac12\langle\operatorname{Tr}Q^{2}\rangle\) is \(4s^{2}\) times the full sum (exact).`
   with
   `with \(W\) the sum over the boundary row inside the block without its entry at \(u\), while \(\tfrac12\langle\operatorname{Tr}Q^{2}\rangle\) is \(4s^{2}\) times the full sum over the boundary row inside the block (exact).`
   Regenerate the post hash afterwards.
2. minor, no action: "with Im alpha neglected" is now redundant but not false.
3. minor, no action: the local-exponent stencil is not stated; the values agree with symmetric differences.
4. procedural: the full scan is pending.

All r2 findings are closed.

## Disposition
r4 with finding 1 only. Then the full scan in passes. If the scan is clean, a plain ACCEPT is expected.

No label change. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
