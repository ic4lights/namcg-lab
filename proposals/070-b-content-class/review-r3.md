VERDICT: NEEDS EVIDENCE | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0
Gatekeeper r3 confirmation + scan pass 1/4, remote/claude, 2026-11-19. Saved by orchestrator.

r3 confirmation:
- appH_insert_r4 differs from r3 only by m-a and m-c, both verbatim.
- apply_build_r3: pre 5106f993..., post 4ea0ee0f... (702490 B), all 20 checks PASS, 401 pp.
- m-b: the gatekeeper's r2 claim was wrong. In sympy 1.14, nsimplify(non-integer Rational) can return surds. The researcher's wording stands (proposal file only).
- m-a, m-b and m-c are closed.

SCAN-PASS 1/4: CLEAN. appH L1-1750 read in full.
- Consistency checks: the content identities agree with L304-433, the (6,2) ledger with L320-455, the n_D=0 scoping with L489-527, and the mass shift with L352. L437 is the only positional phrase affected.
- Pre-existing minor (no action for 070): the Tr rho^n hypotheses at L307-308 are in tension with L372 and L382. Leave this to a later package.
- Cross-refs unaffected. No duplicate labels or titles.

Disposition: run scan passes 2-4. If clean, plain ACCEPT of appH_insert_r4.tex + L437 companion edit, at post hash 4ea0ee0f....
