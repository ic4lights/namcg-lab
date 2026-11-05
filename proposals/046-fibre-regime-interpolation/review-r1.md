VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The computations reproduce and the no-go is correctly scoped as a fork. Two sentences of the insert overstate what s2 and s4 show (a regime claim "fails for every M", and "close to one" for beta_X), and one scope limit is missing. I accept the insert once the three corrections below are applied. I accept no edit to the 045 paragraph.

## Source reading
- Method: digest plus targeted reads, not a full scan. The integration ordinal is 44, no definition or status is changed, and the dirty tree is the accepted 043-045 integrations, so 3(d) applies.
- Read in full: proposal-r1.md and appH_insert.tex; appH L2340-2405 (conjugate-coordinate class paragraphs, product-backgrounds paragraph, the 045 paragraph); the Problem F and B ledger labels; MILESTONE.md; Steinacker 2303.08012 section 7 ((7.2)-(7.5), (7.12), (7.32)).
- Not read this round: the Chapter 17 B and F passages and the Problem B normalisation paragraph. The proposal relies on them only for labels and the c_A = c_T target, which I checked against the 045 text.
- Unreadable files: none.

## Claim under review
The package computes the fibre spectrum, the Duhamel interpolation between the 045 averaged-frame and fibre-trace readings, and first-order background-torsion corrections, for CP^{1,2} x K at IKKT content. It concludes there is a bounded no-go: no open range of the K scale gives a single Einstein coefficient with c_A = c_T on the five traceless polarisations.

Ledger labels, quoted verbatim from appH:
- Problem F (L1365): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- Problem B (L45): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."

## Checks performed
- Reruns: I re-ran s1, s2, s3 and s4 in the proposal folder, sending output to my scratchpad. s1, s2 and s3 match the saved outputs exactly; s4 matches apart from one extra "(R)" header line. I read the saved s5 and compile_check outputs but did not re-run them.
- s1 (direct verification): E1-E3 hold for both bracket signs; the orbit identity N1 holds to 7e-16; Box(C.t^J) = -3, -8, -15 for J = 1, 2, 3 at two base points to about 1e-16. My own check of J = 2: the -tt part of eta MM gives -6 - 2 = -8.
- s2: the Clebsch-Gordan sums equal 1; the Isserlis moments for the scalar kernel are exact in both signatures; the calibration is 1/4; L1 + L2 = SC2 - SC1 holds at all seven cases; the beta table matches the insert; the half-spread is 4.8308/2 = 2.415, quoted as 2.42; the sum over J >= 1 of (2J+1)/mu_J is >= 1, with the J = 1 term equal to exactly 1.
- s3 and s4: Q1^D = m^4 IX1; span residuals <= 1.3e-11 and the P2 coefficient is -6.000; the LX/Q2hat coefficients lie in -3.30 to -0.32; Q2hat relative to EH has one singlet and two doublets; M* lies in [0.21, 0.67] for L/c = 0 and in [1.1, 29.9] for L/c = 1 and 10. Caveat: at M >= 1e3 the s2 beta_X is not monotone (0.963, then 0.982). This is numerical noise, is not quoted, and does not matter.
- Insert mechanics (my own Python byte check): 10683 bytes, 0 TAB, 0 CR, 0 control or non-ASCII characters. The anchor `\section{Problem G: HBEV}` occurs once, preceded by the 045 closing paragraph and a blank line. The refs sec:status-B, ch:vierbein-emergence and ass:lorentzian each occur once, and the cite Steinacker2023 exists once. Braces and \( \) balance; there is no \label; there is one \paragraph; there is no process language; there is one closing scoped status sentence. compile_check.out.txt shows 325 pages with no undefined references, citations or duplicate labels.
- Not verified: the Clebsch-Gordan closed forms and the Isserlis moments were not rederived beyond their script checks, and the torsion code was not independently rewritten.

## Findings

1. Major. Insert, "Which regime", last sentence.
   - Finding: it says the condition M*Sum(2J+1)/mu_J << 1 "fails for every M in the Poisson limit".
   - Reason: that is too strong. The proposal's own table has beta_X = 0.065 at M = 0.01, n = 30, and for any given n a small enough M satisfies the condition. What is true is that at fixed M the sum grows as 2 ln n, so the condition fails as n -> infinity.
   - Required action: replace the clause as in snippet (a).

2. Major. Insert, "Consequence".
   - Finding: it says "where the torsion expansion holds, M >> coth^2 tau, the weight beta_X is close to one".
   - Reason: s4 gives beta_X = 0.52 at n = 2 (M* = 5.0 and 29.9, coth^2/M* = 0.55 and 0.09) and 0.90-0.97 at larger n. beta_X -> 1 only as n -> infinity.
   - Required action: say "of order one (it tends to one as n grows)", as in snippet (b).

3. Minor-to-major. Insert, last sentence of "Consequence".
   - Finding: the statement "no open range ... within these computations" does not say that the intermediate range M ~ coth^2 tau is uncomputed. There beta_X >= 0.86 (trace-like), but the first-order torsion parameter coth^2 tau/M is of order one. For L/c = 1 the zeros sit at coth^2/M* of 0.55-2.5, so even those "cancellation" entries are not in a controlled torsion regime.
   - Required action: add the clause in snippet (c).

4. Minor, no change required. mu_J = J(J+2) against Steinacker's 3s.
   - Finding: the exact algebra is settled. The J = 2 value -8 follows from Box(tt) = -6tt + 2 eta MM with eta MM containing -tt, so the discrepancy at J >= 2 is real for this operator. I cannot tell from (7.5) whether the rest is a convention or an operator difference. Steinacker's modes are sections of an equivariant (twisted) bundle, with Box = k.k + m_s^2, where k.k is built from the fibre-point-dependent frame E, and 3s/R^2 is stated without derivation. The insert's value is a frozen-coefficient value of Box on the polynomial C.t^J. The likely source is a difference in what is attributed to k.k and the connection, but I cannot confirm that.
   - The insert's phrasing ("agree at J = 1, exceed it for J >= 2, not reconciled") is accurate. The conclusions hold for both spectra, because the power-law tail holds for both (for 3J the sum diverges faster), and the insert gives both beta tables. No SME consultation is needed for this verdict.

5. Minor, no change required. The beta_X table and the power-law tail.
   - The derivation is sound: a level contributes (2J+1) times the integral of s^-2 tau^K e^{-s mu_J}, about (2J+1) tau_2/mu_J since tau^K ~ tau_2 s^2, which gives a power-law tail, and the J -> J transitions have Delta = 0.
   - beta_X -> 1 as n -> infinity is a statement about the truncation, which is the physical fibre size. The Poisson limit is itself n -> infinity, so the statement is relevant.
   - H11 (commutative Clebsch-Gordan coefficients) fails for J ~ n, but that does not change the leading ln n.
   - The numbers depend on the single-scale model (H13) and on n, and the insert says so.

6. The 045 sentence is not a prior-claim error, so I raise no flag.
   - The merged sentence ("The full trace approaches them when the fibre gaps exceed the scale of K, ... this is an argument and is not computed") is a labelled uncomputed argument whose condition is incomplete, not false. The condition holds when M << 1/Sigma, with Sigma ~ 2 ln n. With n = 30, fibre gap 3 and M = 0.1, the gap exceeds M by a factor of 30 yet beta_X = 0.40, so the sentence is misleading but not false.
   - Decision: do not edit the 045 paragraph. The insert's own sentence ("The argument of the preceding paragraph ... is therefore incomplete: ...") already corrects it, following the merged correction pattern at L2352 and L2361. The optional replacement ("... is computed in the following paragraph") would leave the insert's correction pointing at text that no longer exists. The old string occurs once in the working tree, so the edit is mechanically possible, but I do not accept it. Take only one of the two routes.

7. No-go scoping (your item d) is adequate once finding 3 is applied.
   - The hypothesis fork (H1-H13, inert amplitudes set to zero, level-one graviton, leading symbol) and the relaxation table are present.
   - Exact, numerical and power-counting statements are labelled consistently with the insert.
   - The tuned-point statement is correctly "not excluded", and the insert states what a tuned point would still need (the L1 coefficient vanishing and the cone matching).

## Scope of what is established
- Exact (algebraic): the Lie-Poisson spectrum mu_J = J(J+2) for the frozen-coefficient loop operator on the fibre; the J-diagonal cross term; the Duhamel weights, the scalar-kernel calibration 1/4 and L1 + L2 = SC2 - SC1 at seven points; the power-law tail.
- Numerical or model-conditional: the beta_X table and the half-spread 2.42 beta_X (H13, n = 30); the span structure and lambda range (residual < 1e-11 at seven points, not proved); the M* ranges (free L/c, first-order torsion, J = 0 only).
- Open: the fibre-flux S^2-M part (power counting only); torsion beyond first order; the cone at torsion order; elimination of the inert amplitudes; the trace polarisation; K itself; G_eff. Problems B and F stay OPEN and PROGRAMME-CONDITIONAL; nothing is DERIVED.
- No-go class: rank-6 CP^{1,2} x K, level-one graviton, IKKT content supplied, frozen leading symbol, inert amplitudes zero, product background without mixed flux, cross term dropped.
- Open avenues, ranked by promise:
  1. Exact Gaussian resummation of the background torsion together with the cone at the same order. This would decide the intermediate range M ~ coth^2 tau (uncomputed) and the tuned points (not excluded), and is the most promising route.
  2. Schur elimination of the inert and J = 2 amplitudes (relaxes "inert = 0").
  3. The S^2-M fibre-flux part with the cross term kept.
  4. Equivariant K with mixed M-K flux (relaxes the product background and could suppress the tail).
  5. A J = 2 or hs-mode graviton.
  6. Other presentations (M^{A5}, non-product).
  7. Reconciling J(J+2) with 3s to fix the fibre-level normalisation; the findings do not depend on it.

## Milestone
- M2 is not met: this is a bounded no-go that leaves the tuned points, the intermediate range and several avenues open.
- M3 is not met: the 045 sentence is an incomplete labelled argument, not a false claim.
- M1, M4 and M5 do not apply.
- No breakthrough, because nothing is derived for a critical-path step. I propose no label change.

## Recommended disposition
Revise the insert per findings 1-3, then integrate it. Do not edit the 045 paragraph. The stale-statement check is clean: 045 already lists "the interpolation between the two regimes ... or the fibre spectrum" as uncomputed, and the insert supplements it; 044's "first term has no two-derivative part" stays scoped to the four-coordinate class.

Accepted text: the whole appH_insert.tex (anchor and mechanics verified) with exactly the three replacements below, and nothing else.

## Corrected snippets (wording only, no new physics)

(a) In "Which regime", replace
`which fails for every \(M\) in the Poisson limit.`
with
`which, at fixed \(M\), fails as \(n\to\infty\), since the sum grows as \(2\ln n\).`

(b) In "Consequence", replace
`the weight \(\beta_X\) is close to one and the fibre trace of the preceding paragraph applies.`
with
`the weight \(\beta_X\) is of order one (it tends to one as \(n\) grows) and the fibre trace of the preceding paragraph is the leading reading.`

(c) In the last sentence of "Consequence", replace
`Within these computations no open range of the scale of \(K\) gives a single Einstein coefficient on the five traceless polarisations with \(c_A=c_T\); isolated values`
with
`Within these computations no open range of the scale of \(K\) gives a single Einstein coefficient on the five traceless polarisations with \(c_A=c_T\); the range \(M\sim\coth^2\tau\), where the first-order torsion parameter is of order one, is not computed, and isolated values`

## Note for the proposal file
The proposal's milestone assessment agrees with mine (none, not a breakthrough). Its soft PRIOR-CLAIM-ERROR should read "incomplete labelled argument, corrected in the new paragraph".
