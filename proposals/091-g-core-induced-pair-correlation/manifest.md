# Manifest, proposal 091-g-core-induced-pair-correlation, round 1

All scripts run with `python -I` from the repo root, e.g.
`python -I proposals/091-g-core-induced-pair-correlation/<script>`. `.out` files are shipped.

## Manuscript payload
| file | bytes | sha8 | role |
|---|---|---|---|
| insert-r1.tex | 3773 | 3e471d12 | the single insert paragraph (single line, CRLF-terminated) |

Insert integration contract (verified live by simulate_apply_091.py on the current tree):
PRE appH 756,686 B, sha256 068ce3f21139911ee7beccd6086b85a4ad18b19df683918ee4beb67b2963df38, CRLF 3844, bareLF 0;
compound PIN `closes nothing in Problem~G.\r\n\r\n\emph{Vacuum term.}` count 1, the `\emph{Vacuum term.}`
side at line start; splice = insert + one CRLF after the `closes nothing...` paragraph break.
POST: 760,461 B, CRLF 3846, bareLF 0, sha256 784cb0a8351d7bf51d62315b9fca9718df419aef133ebd2f68921e6be82f35a1.
Close idiom surface form used: `they close nothing in Problem~G.` (noun/plural form).
Expected POST counts: `close nothing in Problem~G.` 16 -> 17; `closes nothing in Problem~G.` stays 1;
`\emph{Vacuum term.}` stays 2; new header `Eigenvalue reduction of the edge Gram` 0 -> 1.

## Contract scripts
| file | bytes | sha8 | result |
|---|---|---|---|
| hygiene_091.py / .out | 1693/559 | bdcf1a56/fb623710 | PASS (all 24 checks) |
| smoke_compile_091.py / .out | 1671/107 | c7bf62ab/04063dfb | PASS (POS rc0, NEG rc1 undefined control sequence) |
| simulate_apply_091.py / .out | 2138/454 | ec5cf934/c5bd2eaa | PASS (PRE contract, PIN 1, POST invariants; read-only) |

## Derivation / verification scripts (active)
| file | bytes | sha8 | content and key invariant |
|---|---|---|---|
| s2_exact_d2.py / .out | 2138/141 | ec4d62ca/6f7c2448 | tau-separation ratio joint*|jac| / [tau^(2a+1) e^-tau u^2 (1-u^2)^(a-1)] constant in (tau,u); ratio 2/4^a = 2^(1-2a) |
| s2b_exact_d2_stats_v2.py / .out | 1637/536 | 13297eb9/d6ac0eb3 | exact D=2 beta=2 stats: mode u*=1/sqrt(a); E[u]=2*Gamma(a+3/2)/(sqrt(pi)*Gamma(a+2)), lim sqrt(a)E[u]=2/sqrt(pi); P(u<eps)=eps^3 at a=1; Var(p1)=3/(8a+12) at a=1 -> 3/20 vs 1/12; Dirichlet-tail identities |
| s2c_chart_check.py / .out | 1507/185 | 84a4fbb6/a2141613 | exact 2x2 Hermitian chart: det J == (1/2)(y1-y2)^2 sin(2 theta) at 6 rational points, max err ~1e-30 |
| s2d_numeric_id_v2.py / .out | 1712/282 | a013c95b/33ed1be3 | Var(p1)==3/(8a+12) for 8 values of a; direct fibre integral == 089 integrated D=2 slot-pushforward density 1/(g1 g2 (x/g1+(1-x)/g2))^2 at 8 points |
| s2e_d3_jacobian_num.py / .out | 2166/158 | c6750b9c/fc669557 | D=3 finite-difference det J: pairwise coincidence slopes 1.990-1.998 (5 trials), triple-collision slope 6.000 (3 trials) |
| s2f_dirichlet_var.py / .out | 783/96 | b3061f3c/312ec0d0 | exact Dirichlet(a,a) D=2 variance = 1/(4(2a+1)) (the beta=0 comparator) |
| s3_mc_checks_v3.py / .out | 2407/508 | b3733746/65822d0d | MC 1.5e6: u-CDF exponent 2.986 (iid), 3.092 (heterogeneous column variances); E[u^2] flat 0.332-0.334 across 12 tau-deciles (= 3/(2a+3), a=3); rank-one flat-Dirichlet moments 0.3340/0.1672/0.0836 (expect 1/3, 1/6, 1/12) |
| s3b_tau_exponent.py / _v2.out | 1210/207 | 01e93d33/5d0382ec | MC tau-CDF fit 5.23 = UNRESOLVABLE-window artifact (recorded honestly; see s3c), E[u^2] flat 0.332-0.335 over rescaled tau-deciles |
| s3c_tau_exponent_exact.py / .out | 1303/320 | a9b13ea4/b2109e3e | EXACT: int_0^1 x^2(1-x)^2(1-2x)^2 = 1/210; int_0^tau (lam(tau-lam))^2(tau-2lam)^2 dlam = tau^7/210; Gamma(8) CDF leading term t^8/40320 (explains the s3b artifact) |

## Superseded first attempts (kept for provenance, no shipped .out or partial .out)
| file | bytes | sha8 | why superseded |
|---|---|---|---|
| s2b_exact_d2_stats.py | 2743 | 7f830193 | wrong substitution in check (4d); fixed in v2 |
| s2d_numeric_id.out | 320 | ae75eabc | crash output of v1 (BooleanAtom addition); fixed in s2d_numeric_id_v2.py |
| s3_mc_checks.py | 3133 | c7efd5ad | garbled (1b)/(1c) expressions; crashed (shape); fixed chain v2->v3 |
| s3_mc_checks_v2.py / .out | 2245/961 | 696c894c/fe3c9d34 | shape fix but histogram-window artifacts ((1a) 1.611, (1b) crash on empty bins); superseded by v3 |
| s3b_tau_exponent.out | 742 | bfdfb69e | artifact of a flattened heredoc run backgrounded by the harness (stdin echo only); replaced by s3b_tau_exponent.py + s3b_tau_exponent_v2.out and s3c_tau_exponent_exact |

## Quarantined dead-pass WIP (from the previous, context-overflowed pass; untrusted)
| file | bytes | sha8 | disposition |
|---|---|---|---|
| s1_jacobian_v4.py | 3318 | a3ea74ff | NOT relied upon. Independently re-derived by s2c/s2b_v2/s2/s2e. Its check (2) asserted the separation ratio equals 1; the true constant is 2^(1-2a) (s2_exact_d2). |
| s1_jacobian_v4.out | 735 | 1a133e86 | output of the above, consistent with s2c/s2b_v2 on the D=2 chart and E[u] limit; kept for provenance only |

## Literature record status
- Kumar-Sambasivam-Anand, "Smallest eigenvalue density for regular or fixed-trace complex
  Wishart-Laguerre ensemble and entanglement in coupled kicked tops", arXiv:1701.07402 -
  independently verified via the arXiv abs page (fixed-trace complex Wishart-Laguerre ensemble;
  smallest-eigenvalue marginals). Supports that the fixed-trace complex WL ensemble is standard.
- Forrester "Log-gases and Random matrices" (Cambridge) and Muirhead "Aspects of Multivariate
  Statistical Theory" (Wiley) - standard references for the Wishart/Vandermonde Jacobian;
  NOT independently verified (no arXiv record checked; a scout-supplied arXiv id 1301.6213 was
  checked and found to point to an unrelated paper - the id was wrong and is discarded).
