VERDICT: NEEDS EVIDENCE | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0

Gatekeeper r2 review, remote/claude, 2026-11-21. Saved here by the orchestrator. The gatekeeper's check script is gk069r2.py.

Source reading: digest + targeted reads (appH L1821-1842, L2900-3011; ch17 L400-412). Not a full scan.

## Checks
- s1-s5: outputs byte-identical.
- apply_and_build_r2 run on a scratch copy:
  - pre 6a72a326..., post 120c8aba... (733461 B);
  - E1-E6 each occur once, inside the target paragraph;
  - 410 pp, BUILD CLEAN.
- Re-derived independently (mpmath E_3, own tower code):
  - towers, stability, moments, E_3 expansion;
  - F1 values: 41.0912 and 659.392, with no zero at 0.926;
  - the sign near kappa_3=2 at N=16, matching the narrowed statement;
  - F3: U_2 = +0.5575, slope 9.2047 > 5.34, regulated slope positive at the sampled limits; the counterterm caveat is present;
  - the tree-curve relations;
  - the weights and the no-go (V=T forces r_3 in {0,2}, and 2 is unstable);
  - the exchange formula.
- F2: conditional wording is present.
- F4-F8: closed.
- E1-E6 against the live tree (L2966, L2966, L2980, L3000, L3002, L3004): each is false or under-scoped as written, and each fix is minimal. E6 now states the c_3 = mu = 0 restriction.
- E7: single status sentence.
- IsoKimuraTanakaWakatsuki2001 verified on INSPIRE (full names, NPB 604 (2001) 121-147).

## Findings
All r1 findings closed. Non-blocking observations only.

Open (procedural): the full scan, required under 3(b), 3(c) and 3(d).

## Disposition
- Once the scan is clean: plain ACCEPT of E1-E6, appH_insert_r2.tex and new_bib_entry.bib, post hash 120c8aba....
- M3 / PRIOR-CLAIM-ERROR applies, so the item then goes to the AUTHOR, not to autonomous integration.
- No label change. F, C and N stay OPEN.
- Avenues, ranked: (1) rotating K without a tree Hessian; (2) a SUSY or mass-deformed completion (would be structural); (3) a matrix-derived regulator or counterterms; (4) the W_R first-order response; (5) other choices of K; (6) higher loops.
