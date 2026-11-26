# Proposal 100-g-mi-tau-conditioning-d2, round 1

## Result

For the D=2 complex Wishart edge-block law of the integrated 099 paragraph, the MI carried by
the full spectrum coordinate is decomposed exactly. Writing the spectrum coordinate as the pair
(p2, tau) (trace tau, ratio p2), the chain rule gives I((p2,tau);x) = I(p2;x) + I(tau;x|p2)
identically. Three things are established:

1. **Exact cv-class equality theorem.** In the constant-variance class (g1=g2) each term and the
   total vanish identically for every M: I(tau;x|p2) = 0 exactly (equality, not a limit). This
   is the sharp counterpart of 099's cv statement, now for the second channel.
2. **Exact hetero structure.** For g1 != g2 the exact joint density of (tau,p2,x) is
   prop. to tau^(2M-1) (p2(1-p2))^(M-2) (1-2p2)^2 exp(-tau*Lambda), Lambda = a/2 + w(x-1/2),
   a = (1/g1+1/g2)/sigma^2, w = (1/g1-1/g2)(1-2p2)/sigma^2; hence tau|x,p2 ~ Gamma(2M, rate
   Lambda) and f(tau|p2) prop. to tau^(2M-2)(e^{-L0 tau} - e^{-L1 tau}); and
   I(tau;x|p2) = E_{x|p2} KL(Gamma(2M,Lambda) || f(tau|p2)) > 0 for almost every p2 in (0,1/2)
   (strictness criterion: KL=0 iff Lambda is x-independent iff w=0 iff g1=g2 or p2=1/2).
3. **Triple-validated values** (g=(1,2), sigma=1): I(tau;x|p2) = 0.0390018 (M=2) / 0.0346061
   (M=4); I((p2,tau);x) = 0.0499009 (M=2) / 0.0673135 (M=4), on top of 099's
   I(p2;x) = 0.0108991 / 0.0327074; also I(tau;x|p2) = 0.157269 (M=2) for g=(1,100).
   sigma-invariant and g1<->g2-swap invariant exactly; vanish as g1-g2 -> 0.
   Independent methods agree to <= 4e-9 (gate required <= 1e-5); a 300k-sample Wishart MC
   corroborates the joint law (all z-scores |z| <= 1.8).

Nothing in Problem~G is closed: these are spectrum-side conditioning numbers about a fibre
coordinate; they bound no state-side profile weight and identify no simplex fibre.

## Target and status

- Problem: G (infrared boundary entropy / HBEV). Current labels re-derived from the live
  sources this session: appH-microscopic-proofs.tex L3025-3029 — "Status: OPEN. Priority:
  CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and
  G-external support at most a scope-limited model; G remains OPEN and neither satisfies the
  matrix-derived criterion."; ch17-agenda.tex L475 "CRITICAL PATH; mechanism CLOSED
  CONDITIONALLY, derivation OPEN."; completion item L726-729 (G-derived; "G-model and
  G-external do not meet this item."). No discrepancy found between the two sources.
- Dependency: this item sharpens the integrated 099 spectrum-side paragraph (the preceding
  paragraph in the same section); it does not feed any other critical-path dependency chain.
- Classification of this package: DERIVED as the conditioning sub-lemma/package above (exact
  theorem + numerically-established values); it is PROGRAMME-CONDITIONAL evidence within
  Problem~G and closes nothing. Problem~G stays OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL.
- Frontier register (reports/graph/frontier.yaml L601): the D=2 MI(p,.) value package is
  recorded DONE with "no in-class re-attempt; the live MI sharpening is a DIFFERENT target
  (tau-conditioning, MI((tau,u);x) vs I(u;x))". This package is that sanctioned target; the
  I(p2;x) numbers are recomputed only as a regression check of shared machinery against 099.

## Source reading

digest + targeted reads. Digest was CURRENT at task start. Read in full: the 099 paragraph at
appH L3211 (the paragraph being sharpened, including its final sentence used as the byte pin)
and the Vacuum-term passage at L3213; the Problem~G ledger block L3022-3040 (quoted above);
ch17 L474-477 and L666-668 and L726-729 (quoted above); frontier.yaml L601 entry. All prior
rounds/reviews checked: this folder has no earlier proposal round; predecessor context deaths
are recorded in err100.txt / err100p.txt and lineage scripts (see manifest.md).

## Research and reasoning

**Setup (input from the integrated 099 paragraph, not re-derived).** D=2 edge-block law for the
2x2 block: density prop. to det(G)^(M-D) exp(-sum_j G_jj/(sigma^2 g_j)), g_j the column-profile
weights, Wishart shape M. Coordinates: G = tau * [[x, c],[c*, 1-x]]-type fibre parametrisation of
099; the joint (tau, p2, x) is a bijection of the spectrum coordinate for p2 in (0,1/2).

**Derivation (established here).** Jacobian + determinant: det(G) = tau^2 x(1-x)(1 - |c|^2/(x(1-x)))
maps, with the 099 p2 variable, to the measure factor tau^(2M-1) (p2(1-p2))^(M-2) (1-2p2)^2 dp2 dx dtau
(the (1-2p2)^2 from the p2-fibre Jacobian at D=2; the exponent 2M-1 on tau is the D=2 trace
Jacobian: Gamma(2M) shape). The exponent is linear: sum G_jj/(sigma^2 g_j) = tau*Lambda with
Lambda = a/2 + w(x - 1/2), w = beta(1-2p2), beta = (1/g1 - 1/g2)/sigma^2. Hence:
(i) x | tau,p2 prop. exp(-w tau x) on (0,1) (099's rho = w tau) — reproduced;
(ii) tau | x,p2 ~ Gamma(2M, rate Lambda);
(iii) marginalising x: f(tau|p2) prop. tau^(2M-1) e^{-a tau/2} * (e^{-w tau/2} - e^{w tau/2})/(-w tau)
     = tau^(2M-2) (e^{-L0 tau} - e^{-L1 tau}) * const, L0,1 = a/2 -/+ |w|/2. The 1/|w| in
     int_0^1 e^{-w tau x} dx CANCELS into the p2-marginal normalisation, so the exponent is
     2M-2, NOT 2M-1. This corrects the pre-compaction lineage claim (fix_100.py, kept as
     lineage); sympy check B in verify_anchors.py verifies int_0^inf tau^(2M-2)(e^{-L0 tau} -
     e^{-L1 tau}) dtau = Gamma(2M-1)(L0^{1-2M} - L1^{1-2M}) and the consistency of the joint
     marginalisation (check C), so N_q = Gamma(2M-1)(L0^{1-2M}-L1^{1-2M}) is the exact
     normaliser with no 1/|w|.

**Chain rule and cv theorem.** I((p2,tau);x) = I(p2;x) + I(tau;x|p2) is the exact chain rule for
the bijection (p2,tau) <-> spectrum coordinate. cv: w = 0 makes x | (p2,tau) uniform and
independent of (p2,tau) AND of p2, so all three MI terms are exactly zero for every M (route-A
print: Itau = 0). This is the strict-vs-equal contrast 099 left implicit: the cv limit is
attained exactly, and by the strictness criterion below the hetero value is strictly positive a.e., so the limit is
genuinely a boundary value.

**Strictness.** I(tau;x|p2) = E_{x|p2}[KL(Gamma(2M,Lambda(x)) || f(tau|p2))] (route B; the KL
representation follows from E[-ln f(tau|p2)] = h(tau|p2) by marginalising the chain rule).
KL(conditional || marginal-mixture) = 0 iff Lambda(x) is a.s. constant iff w tau-dependence
trivialises iff w = 0 iff g1 = g2 or p2 = 1/2. For g1 != g2 this fails on a set of p2 of full
measure: strict positivity a.e. established (equality at p2 = 1/2 only, a null point).

**Three representations, three codes (validation design).** Route A: I = h(x|p2) - E_{p2} h(rho)
with h the truncated-exponential entropy h(r) = -ln r + ln(1-e^{-r}) + 1 - r e^{-r}/(1-e^{-r})
(series -r^2/24 + r^4/960; sympy check E). Route B: the KL form above. Route A': mpmath dps-30,
I = h(tau|p2) - E_{x|p2} H_Gamma(Lambda), fully independent code path (no shared quadrature,
no scipy). Pipeline A-vs-B agree 5-8e-14; grid-refine drift <= 1e-13; numpy-vs-mpmath agree
<= 4e-9; shared machinery reproduces 099's published I(p2;x) to 2.9e-8 / 1.4e-8 (regression
gate). Direct Wishart MC (300k samples, mc100s.py): E[h(rho)] -0.223903/-0.419796 vs quadrature
refs -0.223877/-0.419234 (z = -0.07/-1.04); conditional means E[x|p2-bin] and E[tau|cell] match
the closed forms of (i)/(ii) (all |z| <= 1.79). Last quoted digit stable at <= 2e-8.

**Invariances.** sigma enters only through 1/sigma^2 in a and w, i.e. Lambda -> Lambda/sigma^2:
the Gamma rate rescaling is absorbed by tau -> tau*sigma^2 (Jacobian 2M-power cancels against
Lambda^{2M} normalisers), so I(tau;x|p2) is exactly sigma-invariant (verified numerically
identical rows at sigma=2). g1<->g2 swaps w -> -w, Lambda0 <-> Lambda1 and leaves x|p2 and the
KL invariant (exact). Weak-hetero g=(1,100): I(tau;x|p2) = 0.157269 > 0 (M=2) — the channel is
large when the profile contrast is large, as the strictness criterion predicts; both channels -> 0 as beta -> 0 by
the cv theorem plus continuity of MI in the law.

**Comparison with the original target (i)-(iii).** (i) equality theorem: closed exactly.
(ii) exact 1-D integral representations given (routes A, A', B are all single/two-dimensional
exact integrals; no closed form beyond the anchors is claimed); values at M=2,4 + weak case;
sigma/swap statements: given; numerics marked "numerically established" with error estimates.
(iii) scope sentence in the insert matches 099's phrasing family.

## Claim classification

- Bijection (p2,tau) <-> spectrum coordinate; chain-rule identity: established identity.
- Exact joint density of (tau,p2,x), Gamma(2M,Lambda) conditional, f(tau|p2) prop.
  tau^(2M-2)(e^{-L0 tau}-e^{-L1 tau}), N_q = Gamma(2M-1)(L0^{1-2M}-L1^{1-2M}): established
  derivation, checked symbolically (verify_anchors A,C) and by MC conditional means.
- h(r) truncated-exponential entropy formula + series: established (sympy check E).
- cv equality theorem (all three terms exactly 0 for every M): established (conditional
  independence from the explicit density).
- Strict positivity a.e. via the KL criterion: established, conditional on the stated law.
- MI values 0.0390018/0.0499009/0.0346061/0.0673135/0.157269 and 099-regression: numerically
  established (two independent quadrature paths to 4e-9; MC corroboration |z|<=1.8; error on
  quoted digits <= 2e-8).
- sigma-invariance and g-swap: established exactly from the density; verified numerically.
- "vanish as g1-g2 -> 0": established (cv theorem + continuity); the g=(1,100) row is a
  large-contrast data point, not a small-beta limit (disclosed deviation (d)).
- Input (not re-derived here): the D=2 edge-block law itself and the 099 fibre parametrisation
  — these are the integrated 097/099 spectrum-side inputs of the same paragraph.
- No claim made about: state-side profile weights, simplex fibres, S_ent^(IR), stationarity,
  Lambda_eff, or any other Problem~G target component.

## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`. One paragraph appended inside the Problem~G
section (sec:status-G), immediately after the integrated 099 spectrum-side paragraph and
before the vacuum-term paragraph. Nothing is removed, reworded, or reordered; no equation of
the existing text is touched; the 099 paragraph's final sentence and the vacuum-term opening
line both stay verbatim.

Anchor (verified unique in the live PRE): the paragraph boundary is the byte sequence
`and they close nothing in Problem~G.` + CRLF CRLF + line-initial `\emph{Vacuum term.}`
(pin 162 B at byte 756633, count 1; compound count 1; cut position 756799). The insert file
`insert-r1.tex` (1989 B, sha256 511ddc60..., single line, one terminal CRLF) is applied as
PRE[:756799] + insert + CRLF + PRE[756799:]. Quote of the inserted text (exactly the file
bytes, rendered; the file itself is one line — regenerate only via gen_insert_100.py):

```latex
\emph{Full-spectrum conditioning of the fibre coordinate at \(D=2\).} Sharpening the preceding paragraph, decompose the spectrum coordinate into the trace \(\tau\) and the ratio \(p_{2}\), so that conditioning on the spectrum is conditioning on the pair \((p_{2},\tau)\) and the chain rule gives \(I((p_{2},\tau);x)=I(p_{2};x)+I(\tau;x\mid p_{2})\) exactly. In the constant-variance class the two terms and the full mutual information vanish identically for every \(M\): equality, not merely a limit. In the column-profile class with \(g_{1}\neq g_{2}\) the exact joint density of \((\tau,p_{2},x)\) is proportional to \(\tau^{2M-1}(p_{2}(1-p_{2}))^{M-2}(1-2p_{2})^{2}e^{-\tau\Lambda}\) with \(\Lambda=(g_{1}^{-1}+g_{2}^{-1})/(2\sigma^{2})+(g_{1}^{-1}-g_{2}^{-1})(1-2p_{2})(x-\tfrac{1}{2})/\sigma^{2}\), so that \(\tau\mid x,p_{2}\) is \(\mathrm{Gamma}(2M)\) with rate \(\Lambda\), while \(f(\tau\mid p_{2})\) is proportional to \(\tau^{2M-2}(e^{-\Lambda_{0}\tau}-e^{-\Lambda_{1}\tau})\) with \(\Lambda_{0,1}\) the endpoints of the \(x\)-range of \(\Lambda\); the second term equals \(E_{x\mid p_{2}}\mathrm{KL}(\mathrm{Gamma}(2M,\Lambda)\,\|\,f(\tau\mid p_{2}))\) and is strictly positive for almost every \(p_{2}\in(0,\tfrac{1}{2})\), since \(\Lambda\) depends on \(x\) unless \(g_{1}=g_{2}\) or \(p_{2}=\tfrac{1}{2}\). Nested quadrature and an independent high-precision path give \(I(\tau;x\mid p_{2})=0.0390018\) and \(I((p_{2},\tau);x)=0.0499009\) at \(M=2\), and \(0.0346061\) and \(0.0673135\) at \(M=4\), for \(g=(1,2)\), on top of the preceding \(I(p_{2};x)=0.0108991\) and \(0.0327074\); these conditioning numbers are exactly independent of \(\sigma\), invariant under \(g_{1}\leftrightarrow g_{2}\), and vanish as \(g_{1}-g_{2}\to 0\), with \(I(\tau;x\mid p_{2})=0.157269\) at \(M=2\) for \(g=(1,100)\). These are spectrum-side conditioning numbers about a fibre coordinate: they bound no state-side profile weight, identify no simplex fibre, and close nothing in Problem~G.
```

Closing sentence deliberately ends "and close nothing in Problem~G." (not 099's exact "and
they close nothing in Problem~G.") so the old-seam pattern "and they close nothing in
Problem~G.\r\n\r\n\emph{Vacuum term.}" has count 0 after application; the hygiene check
enforces this. No \ref/\cite/labels are added (no label verification needed); no duplicate
header string (hdr count 1 after apply). No stale passages elsewhere: the only other text
quoting 099's numbers is untouched; the idiom "close nothing in Problem~G." goes 25 -> 26,
"closes nothing" stays 1, "\emph{Vacuum term.}" stays 2.

Byte contract for the integrator (all confirmed by simulate_apply_100.py, read-only):
PRE 793616 B / sha 7cd6e208...; POST 795607 B / crlf 3864 / bareLF 0 / sha256
3f1b030cf81dff1b39a0fc96be87331d92ca2ed5c33bc592bb794b66670e3202; idiom 26, closesverb 1,
vacuum 2, hdr 1, adjacency 1, oldseam 0. STOP on any pin mismatch.

## Verification scripts

All in this folder (see manifest.md for lineage). Reproduction pack — run from the repository
root; each command is traceback-free and the listed invariant output must match (scripts
locate their siblings via __file__, need no cwd assumption; fix_* and gen_* rewrite their
targets idempotently to the same sha):

1. `python -I proposals/100-g-mi-tau-conditioning-d2/verify_anchors.py` -> last line
   `PASS verify_anchors` (sympy checks A-G: f(tau|p2) exponent 2M-2 and N_q (B,C); truncated-
   exponential entropy formula + series (E); cv anchors (A,G)).
2. `python -I proposals/100-g-mi-tau-conditioning-d2/mi_tau_100q.py` -> invariants as in
   mi_tau_100q.out: M=2 I(p2;x)=0.0108991 I((p2,tau);x)=0.0499009 I(tau;x|p2)=0.0390018
   (route A) rB=0.0390018 Eh=-0.223877 refine+A/B <= 1e-12; M=4: 0.0327074/0.0673135/
   0.0346061/-0.419234; 099 regression rows agree <= 3e-8; sigma=2 and swap rows identical;
   cv row Itau=0; weak g=(1,100) Itau=0.1572689. (A RuntimeWarning at one division is benign:
   the d=0 branch is selected by np.where; output is traceback-free.)
3. `python -I proposals/100-g-mi-tau-conditioning-d2/rederive_100.py` (mpmath dps-30,
   independent path, ~minutes) -> I(tau;x|p2)=0.0390018457, I((p2,tau);x)=0.0499009171,
   I(p2;x)=0.0108990714 (M=2); 0.0346060516/0.0673134655/0.0327074139 (M=4); weak
   0.1572688891 — matching (2) to <= 4e-9.
4. `python -I proposals/100-g-mi-tau-conditioning-d2/mc100s.py` (300k-sample Wishart MC,
   corroboration only) -> E[h(rho)] sim -0.223903/-0.419796 vs refs -0.223877/-0.419234;
   all |z| <= 1.8 (mc100s.out).
5. `python -I proposals/100-g-mi-tau-conditioning-d2/gen_insert_100.py` ->
   `insert-r1.tex bytes=1989 sha256=511ddc60...` (sole byte authority; hygiene self-checks
   bail on violation before writing).
6. `python -I proposals/100-g-mi-tau-conditioning-d2/hygiene_100.py` -> `SUMMARY ALL PASS`.
7. `python -I proposals/100-g-mi-tau-conditioning-d2/simulate_apply_100.py` -> POST bytes
   795607, crlf 3864, bareLF 0, sha256 3f1b030c..., idiom=26 closesverb=1 vacuum=2 hdr=1
   adjacency=1 oldseam=0; last line `no write performed` (READ-ONLY).

## Decisions Taken

- Re-derived f(tau|p2) from scratch instead of trusting the pre-compaction fix_100.py: the
  prior claim (exponent 2M-1, 1/|w| kept) is wrong; the correct exponent is 2M-2 with the
  1/|w| absorbed into the p2-marginal normalisation (sympy checks B,C). Rejected alternative:
  importing the pre-compaction formula.
- Orchestrator-suggested anchor h(3)=0.3068970 is numerically wrong; the computed value is
  h(3) = -0.3068685591 (used as internal anchor only, not quoted in the insert). The 2-ln 6
  expression is not an item-100 anchor: the x-channel cv anchor here is exactly 0. Neither
  appears in manuscript text.
- The MC path is corroboration only; the validation gate is the two independent quadrature
  paths (agreement 4e-9 << gate 1e-5).
- fix9 adopted: requiring adjacency with TWO CRLFs is the only satisfiable reading of the
  contract layout under the double-CRLF paragraph seam; the predecessor single-CRLF pattern
  admits no insert at all.
- Insert tail reworded ("...and close nothing in Problem~G.") to keep oldseam=0 while staying
  in 099's phrasing family; routine wording choice, no label or scope effect.
- Notation p_{2} and \( \) delimiters kept to match the integrated 099 paragraph; square-
  bracket exponent notation dropped (hygiene bans square brackets).
- The q-file print label "weak g=(1,100) both ->0 as b->0" is misleading (g=(1,100) has
  b=0.99, not small); the b->0 test is the cv run. Numbers correct; script kept as-is
  (lineage), deviation disclosed.
- Predecessor artifacts (wrong v1 pipeline variants, dead mc100r, pre-compaction fix) kept
  unreadable-as-evidence but on disk as lineage, registered in manifest.md.

## Milestone assessment

Routine. A sharpening sub-lemma package on the spectrum-side layer of Problem~G; triggers no
milestone in MILESTONE.md; closes nothing on the critical path.

## Status-label recommendation

Current critical-path list re-derived from ch17 (A, B, C, D1, E, F, G-derived, N). Labels
affected by this package: NONE. Problem~G stays Status: OPEN / Priority: CRITICAL PATH /
Completion: PROGRAMME-CONDITIONAL; the G-derived completion item (ch17 L726-729) remains
unmet. No label change is proposed.

## Author decision needed

none

## Remaining open step

The original Problem~G target is untouched: derive S_ent^(IR) and boundary stationarity from
the matrix theory and obtain the Lambda_eff scaling or value (ch17 L666-668, L726-729). This
package supplies only spectrum-side conditioning numbers and the exact cv equality theorem for
the fibre coordinate. Spectrum-side variants still open (frontier register): zero-entry
profiles and the M < N-M row variant. The state-side profile-weight edge and the simplex-
fibre identification edge are untouched.

## Special instructions for the gatekeeper

- Highest-value re-derivation: the 2M-2 exponent / 1-|w|-cancellation in f(tau|p2) (the
  package's one correction of lineage mathematics); do it independently of verify_anchors.py.
- Check the strictness iff-chain against the actual x|p2 law (full support on (0,1) for
  finite |w|tau, so a.s.-constancy of Lambda <=> w=0 <=> g1=g2 or p2=1/2).
- No closed form for I(tau;x|p2) is asserted, so do not mark its absence as a gap; "1-D
  integral representations" in the Result section means the exact route-A/A'/B integrals, and
  route A/B are 1-D / expectation forms, route B nested — stated as such.
- The insert must be verified byte-identical to insert-r1.tex and the contract numbers above;
  do not accept a hand-retyped paragraph.
- Must NOT be asserted from this package: any closure of Problem~G or of the G-derived item;
  any state-side/profile-weight or simplex-fibre consequence; any S_ent^(IR) implication.
- Lineage files with known-wrong content (fix_100.py, mi_tau_100p.py defects listed in
  manifest.md, mc100r.py, mi_tau_100q v1, hygiene v1, rederive v1) must not be used as
  evidence; the final-version shas in manifest.md identify what to run.
- Disclosed deviations to re-check rather than rediscover: (a) p-file h() branch algebra wrong
  in both branches (superseded); (b) orchestrator h(3) anchor wrong, computed value used;
  (c) 2-ln-6 not an anchor here; (d) weak-g print label misleading; (e) mc100s needed six
  fix rounds (predecessor-written pieces deeply wrong); (f) hygiene v1 adjacency bug;
  (g) insert tail rewording for oldseam.
