VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/1

(Gatekeeper r2 review, remote/claude, 2026-11-19. Saved here by the orchestrator. The gatekeeper's check scripts are copied in as gk_hc_r2.py, gk_approx_r2.py and gk_sign_r2.py.)

Source reading: digest + targeted reads (appH L2886-2932; ch17 L474-495, L700-730; gpu backup L3153-3175; local 067 appH_insert_r2.tex and review-r2; ch12 L139, L185). The full scan is owed under 3(c) and 3(d) and is deferred to scan-only passes.

## Checks
Reproduced:
- d1-d3: byte-identical.
- 10 inherited scripts: identical.
- apply_build_r2.py:
  - pre and post hashes match;
  - R1-R3 anchors are each unique;
  - 394 pp, 0 undefined.

Re-derived by hand:
- the direct-sum algebra;
- the pair formula;
- E1 against the arXiv:2311.10131 PDF: CONFIRMED. The paper uses the block partition, from [44,45], not the diagonal partition of [37].
- E3: confirmed.
- the hook-content identities, checked in rational arithmetic;
- the pencil and 078 content;
- the 067 interplay: 067 is a plain ACCEPT r2; insert it before \section{Problem H}; anchors unique.

## Findings
- M1, major. Replace "at fixed fractions the residual grows as \(q_1q_2\log N\) (numerical)" with "at equal row fractions \(u_1=u_2\), as at the symmetric saddle, the residual grows as \(q_1q_2\log N\), while at the unequal fractions tested it stays bounded in \(N\) (numerical)".
  - Reason: the residual is bounded at the unequal fractions tested, because the hook product telescopes when l1-l2 ~ N.
- m1 (R2). Replace "the median relative distance of the spectrum from it is \(0.086\) at block rank \(50\) and \(0.023\) at rank \(800\), decaying as about the inverse square root of the rank, and the norm of each edge row then also includes its entries in the block of the other summand (numerical)" with "at \(M_1=M_2\) and \(s_1=s_2\) the median relative distance of the spectrum from the union of the two pairs formed with the full edge rows, whose norms then also include their entries in the block of the other summand, is \(0.086\) at block rank \(50\) and \(0.023\) at rank \(800\), decaying as about the inverse square root of the rank (numerical)".
  - Reason: at unequal scales the distances are smaller and fall roughly as 1/rank.
- m2 (R3). Replace "is derived for the block cut of~\cite{FlissFrenkelHartnollSoni2025} on the fuzzy sphere" with "is derived for the block partition of the matrix degrees of freedom, the cut of the subsystem of~\cite{FlissFrenkelHartnollSoni2025} above, on the fuzzy sphere".
- m3 (R4). Replace "on its \(M_f\ge2\) largest eigenvalues in summand \(f\)" with "on its \(M_f\) largest eigenvalues in summand \(f\), \(2\le M_f<N\)".
- m4 (R5). Replace "the charge is \(\bigoplus_f\mathbf 1_{q_f}\otimes Q_f\) and the stacked diagram \((\ell_1^{q_1},\ell_2^{q_2})\) is read (exact)" with "the charge is \(\bigoplus_f\mathbf 1_{q_f}\otimes Q_f\) (exact), so the stacked diagram \((\ell_1^{q_1},\ell_2^{q_2})\) is read".
- m5 (R6, PRIOR-CLAIM-ERROR, scoping).
  - In Bearing (ii) (appH L2926), replace "up to a correction of the order of a logarithm (numerical)" with "up to a correction of the order of \(\ell_1^2/M_1+\ell_2^2/M_2\) and of a logarithm (numerical)".
  - In the block, replace "(the approximate form holds for \(\ell_f\ll M_f\))" with "(the approximate form holds at leading order for \(\ell_f\ll M_f\))".

## Previous findings (group5-G1)
- 072 BLOCKING: resolved (direct sum; product handed to 067).
- 073-080: all resolved, 077 absorbed.
- Group-wide: resolved.
- 078 compression: acceptable.

## Disposition
- Researcher r3 applies R1-R6, then re-review with a full scan (in passes).
- Note for 081 r2: drop "diagonal-cut convention" (E1).
- No label change; Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- Open avenues, ranked:
  (1) a spacetime-block subsystem of a non-compact or Lorentzian leaf (relax H1);
  (2) a split algebra with edge group U(M1)xU(M2) (relax H3);
  (3) derive rows-from-moments;
  (4) a within-core state / OS reconstruction;
  (5) two-sided diagrams;
  (6) depth-cancelling combinations.
