# Local re-review r1 (remote/claude, 2026-11-18): group G1 (061, 072-080)

Group verdict: AWRR | FLAGS: RESEARCHER-DECISION | OPEN: 1/5
Source reading: digest + targeted reads (appH L3022-3196, ch17 G passages). No full scan claimed. The full scans owed from ordinal 65 are not discharged by this review.
Scripts reproduced except 077 s2-s6, which were not run or still running and are not used as evidence.

## 061: AWRR (OPEN 0/1)
- MAJOR (L3096-3099). Replace "\((s_1(2N)-s_1(N))/\ln 2=0.31022,0.30788,0.30065\) approaching the central-charge value \(c/3=\tfrac13\) for the two cuts of the interval at \(c=1\);" with "\((s_1(2N)-s_1(N))/\ln 2=0.31022,0.30788,0.30065,0.27337\) for \(N=256,512,1024,2048\), below the central-charge value \(c/3=\tfrac13\) for the two cuts of the interval at \(c=1\) and decreasing with \(N\) at this regulator, so these slopes do not resolve the coefficient \(\tfrac13\);"
- minor (L3110-3111). Replace "one half of the logarithmic term" with "one half of the two-cut slab density".
- minor (L3053-3055). Replace "the non-factorization of region algebras in matrix models is established independently in the BFSS setting in~\cite{Anous2020}" with "that the BFSS matrix model is ordinary quantum mechanics without spatial subsystems is noted independently in~\cite{Anous2020}".

## 072: AWRR, BLOCKING, RESEARCHER-DECISION (OPEN 1/0)
- BLOCKING (L3153-3155). The edge data are those of Theta1 (x) Theta2: rank M1M2, one connected edge. The diagram, defect and selection reading are for U(M1+M2) with one row per disconnected component. The two belong to different blocks, and the text contradicts the accepted local 067.
  - Options: (a) re-anchor to two band-separated caps of one axis, which needs m1+m2<1; (b) a direct-sum background X1 (+) X2, which keeps the numbers but needs to be defined (preferred); (c) keep Theta1 (x) Theta2 with U(M1M2) and the 067 multi-row reading.
  - Minimal selection sentence: replace "for the block of the union it suggests a two-row diagram whose row lengths follow the factor edge data up to the \(O(1/N)\) corner admixture above." with "for a block that is the union of two disconnected components, such as the two band-separated caps of one axis of the Row length paragraph, whose charge spectrum is exactly the union of the two single-cap pairs, it suggests a two-row diagram of \(U(M_1+M_2)\) with rows fixed by the single-cap edge data; the block \(\Theta_1\otimes\Theta_2\) above has rank \(M_1M_2\) and a connected edge, so this reading does not apply to it."
- minor. Replace "\(M_2=N/3\) (numerical)" with "\(M_2=N/3\), \(k_1=k_2\) (numerical)".
- minor. Define Theta = Theta1 (x) Theta2 and E (or cite 067).
- minor. Append "(the approximate form holds for \(\ell_f\ll M_f\))" to Bearing (ii).

## 073: AWRR (inherited). Replace "two-row hook-content defect of the product testbed within" with "two-row hook-content defect, a function of the ranks and rows alone, within". Optional: point to the derived bound in 079.
## 074: AWRR (inherited). Replace "stacked-row hook-content defect of the product testbed within" with "stacked-row hook-content defect within".
## 075: AWRR, RESEARCHER-DECISION (follows 072).
- Independent averaging of the two axes, and the corner sentence (0.9423-2.4484), presuppose two factors.
- Replace "the sphere mean of the edge-length fraction" with "the sphere mean of the squared edge-length fraction".
- Replace "reproducing the integrated isotropic values at the round frame" with "reproducing the isotropic values of the stacked-rows paragraph at the round frame".
## 076: AWRR (inherited).
- The product-testbed comparison sentence has to be revised or deleted per the 072 decision.
- Replace "\(w_f=k_fm_f(1-m_f)\), with ... \(k_f\) the edge-length coefficient of the factor" with "\(w_f=k\,m_f(1-m_f)\), with \(k\) the edge-length coefficient of the factor", and "\(k_f=1\)" with "\(k=1\)".
## 077: AWRR (minor). Replace "(symbolic and numerical; no such reduction is established for \(q>2\))" with "(symbolic and numerical; the general-\(q\) form under exact equalization is given in the next paragraph)".
## 078: ACCEPT.
## 079: AWRR (minor).
- Replace "and this content is now established with explicit constants rather than verified numerically" with "and this bound is established with explicit constants".
- Replace "previously verified numerically on frames with N up to 3200," with "verified numerically there on frames with N up to 3200,".
- Replace the sentence from "A sampled frame scan confirms" through "(numerical, sampled frame grids)." with "A sampled frame scan checks the inequality: at N=3200 with symmetric block ranks and saddle parameter one, over 150 sampled frames the worst residual is 7.1 for two rows and 54.9 at depth three, against values of the row-dependent form of the bound between 8.6 and 9.0 and between 74.8 and 80.2 (8.8 and 77.0 at the round frame), with no violation at N=400, 1600 and 3200 (numerical, sampled frame grids)."
## 080: AWRR (minor). Replace "with \(n_f\) in place of \(w_f\): \(9/17\) at \(p=1\)" with "with \(n_f\) in place of \(w_f\), with excess \(9/17\) at \(p=1\)".

## Group-wide
- Repeated "close(s) nothing in Problem~G" clauses (072, 074-080) should be removed in one editorial cleanup.
- The L3193 scope sentence is stale: it no longer covers the product, frame-average and copy paragraphs.
- Local 067: 072 duplicates its closed forms and conflicts with its block rank and row reading. 067 can still be inserted directly after L3193, before \section{Problem H}; its anchor occurs exactly once, and its expected size/hash must be recomputed. Do not insert it mid-block. The revised 072 should then cite 067.
- Label changes: none. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## 077 addendum
The background scripts s1, s3, s4b, s5 and s6 have all finished, and all pass. Their values match the text, so the verdict stays AWRR with the one minor fix. s2 and s2b were not run.
