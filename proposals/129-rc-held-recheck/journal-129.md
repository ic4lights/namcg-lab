# Journal 129-rc-held-recheck

## Start (block order A first)

Reads so far (in full): scratch/digest.md (DIGEST CURRENT per dispatch; appH pin dee9a4174b81,
4146 lines); reports/rc-import-review-2026-11-25.md; reports/rc-parallel-apph-blocks-2026-11-25.md
(headers at lines 5,11,63,151,162,248,253,258; blocks 42,48,49,50,51 read in full);
proposals/claude-remote-late/README.md (verdict table).

Working plan: F-area first (blocks 48, 49/50/51, 42), then D1/E (27, 28), block 22 verification
expected SUPERSEDED.

## Block 48/49/50/51 (F-area q=0): context check against our appH

(next: read our appH Problem F region L3000-3230 to verify the "preceding paragraph" referents
exist in our reviewed text, and check bib keys IsoKimuraTanakaWakatsuki2001, Bertotti2003)

## Block 22 (Problem C "Missing step.") -- SUPERSEDED, verified

Our appH L762 = "The full target of Problem~C is the gauge-fixed quadratic scalar operator on
the locked vacuum in a constructed frame: ... (i) A frame ... (ii) G_eff ... (iii) constraint
structure ... bounded obstruction recorded in the Problem F entry." Held block 22 = OLDER
variant: "full quadratic scalar operator", includes "or a ratio m_\psi/v", Cassini-clause and
ch:agenda phenomenological-comparison clause that our gatekeeper-edited text dropped, and lacks
(i)-(iii) and the F-obstruction cross-reference. Verified against reports/...blocks L5ff.
No payload for block 22. (Item 070 content-class candidate result NOT payloaded this round:
needs re-read of Axiom (H)/Theorem (S) definitions; logged as future package candidate.)

## Block 48 paragraph 1 (Hessian of tree stabiliser on K) -- re-derivation results

Angular-momentum structure hand-derived: H = chi^2(L^2 - kappa3 S.L), kappa3 = 2 - c3/chi gives
branches chi^2(l(l+1)-kappa3 l) [mult 2l+3, j=l+1], chi^2(l(l+1)+kappa3) [2l+1, j=l],
chi^2(l(l+1)+kappa3(l+1)) [2l-1, j=l-1]; S.L eigenvalues l, -1, -(l+1) by CG algebra.
Adjoints carry l=1..N-1 only (no l=0): no negative mode iff -1<=kappa3<=2 exactly
(j=l-1 at l=1 binds at -1; j=l+1 at l=1 binds at 2). kappa3=-2 gives l=1,j=0 eigenvalue -2chi^2.
kappa3=2 reproduces OUR integrated c3=0 spectrum l(l-1), l(l+1)+2, (l+1)(l+2) at L3194.
Multiplicities sum 3(N^2-1). Numerical check vs explicit matrix Hessian: script verify_hessian_129.py.
CORRECTION (see below, session 2): my earlier note here claimed sum(S.L)^2 = N^4-N != held
factor; that hand sum was WRONG. sympy (verify_weights_129.py) proves sum = N^2(N^2-1),
exactly the held factor. Full held weighted identity stays conditional (spinor/ghost sector
not reverified); downstream regulated-mathcalU sign claims still NOT payloaded.
Algebra (kappa3^2-4)chi^4 = c3^2 chi^2 - 4 c3 chi^3 holds exactly; vanishing at kappa3=2 matches
our c3=0 index-part agreement statement.

## Block 48 tree curve + scale exchange -- algebra verified

V_t = abar(chi^4 - 2/3 c3 chi^3): d/dlnchi = 4Utilde(1-r3) => 1-r3 = -U'_loop/(4Utilde) [exact].
d2/dlnchi2 tree = 4Utilde(4-3r3); + delta*4Utilde => beta_K = 2U'/(4Utilde(4-3r3+delta)) =
2(r3-1)/(4-3r3+delta) given beta_K = 2U'/U_chichi; beta_K=1 => r3=(6+delta)/5; V/T=(1-r3)^2
[their weight claim, conditional] => (1+delta)^2/25; beta_K(r3=2)=2/(delta-2). All reproduce.
q_*^2|_chi = -beta_K U' L/(8 m^4) = -L U'^2/(4 m^4 U_chichi) <= 0 at U_chichi>0 [derived; note
holds at ANY stationary-convex point, not only minima]. Example: x=3/10, quartic 7.935, cubic
-12.36 => c3/chi = 1.5*12.36/7.935 = 2.3366 => r3=1.1683, kappa3=-0.3366, V/T=(1-r3)^2=0.0282,
varrho=(V+2T)/3V = 23.97; ratio beta_K U'/(4 U4) q_b^2 with U'=4*7.935*0.1683=5.345/(4*-0.09)
= -14.85 ~ held -14.8. Scripts: verify_treecurve_129.py (sympy), verify_example_129.py.
Variance: earlier hand-check of eliminated quadratic part: min -U'^2 sigma1^2/(2 U_chichi)
= -(1/4)beta_K U' sigma1^2 -- held coefficient CORRECT (my earlier factor doubt was wrong).

## Held items NOT payloaded (recorded for later packages)

- Block 48 para2 (tadpole/theta): channel y^mu y^nu + sigma1 reparam invariance duplicates our
  newer integrated L3220/L3222 (pure-trace channel); no new derivation-grade input. SUPERSEDED
  in our presentation except "sigma1 -> sigma1 + a sigma1^2 reparam invariance" observation --
  not payloaded (our L3220 already states the profile normalisation).
- Block 48 para3 / blocks 49-51 (tree non-derivative, singlet sector): localisation identity
  2fL(fA)-f^2L(A)-L(f^2A) = 2(Df.Df)A - 2Df(Df.A) verified for L=-box (script
  verify_localize_129.py); eigenvalue pattern 6/-2/-2 + trace bookkeeping consistent by hand
  but explicit 4x4 realisation and C_tree = (rho_M/4g^2)(l^2+m^2) coefficient NOT reproduced ->
  conditional, NOT payloaded. Our L3212 "not computed" sentence stays.
- Block 42 (TT dispersion multline): v^2, mu^2 are inputs in the held text; Z matches our c_T^TT
  entry structure but rho_M->dark energy needs G_N connection. NOT-FOR-MANUSCRIPT.
- Blocks 27/28 (D1/E Heisenberg, reflection positivity): pending read; E thimble + C.operator
  under author HOLD; payload must not touch.

## Session 2 (post-compaction): Hessian shift identity ESTABLISHED; scripts PASS

verify_hessian_129.py REWRITTEN, now PASS. Key new result: the GAUGE-FREE shift identity
2(G(c)-G(0)) = (c3/chi) chi^2 SO, SO_{ij} = -eps_{kij} i ad_{J^k} (real form), residual <1e-13
for N=2..5 and seven (chi,c) points. So the cubic term changes ONLY the spin-orbit coefficient,
2 S.L -> kappa3 S.L, independent of any gauge fixing; combined with OUR integrated L3194 c=0
anchor (flux operator, Lambda^i=J^i spectrum l(l-1), l(l+1)+2, (l+1)(l+2)), the held operator
identity H_V^K = chi^2(L^2-kappa3 S.L) is now CONDITIONAL ONLY ON THAT INTEGRATED ANCHOR, not
on prior art. SO spectrum on su content = {l,-1,-(l+1)}^(mult) + 3 trace zeros (verified N=2..4).
Earlier flux-free full-spectrum mismatch explained: L3194 anchor is the FLUX operator; a
flux-free Hessian has kernel {0x8,2x3,6} at N=2 and cannot test the anchored c=0 spectrum.
no-negative-mode iff -1<=kappa3<=2 (exact formula scan), kappa3=-2 -> -2 chi^2 (l=1,j=0),
multiplicities 3(N^2-1): all PASS.

verify_treecurve_129.py PASS (sympy): r3:=c3/2chi is the UNIQUE defn making dV_t/dlnchi =
4U(1-r3) and d2/dlnchi2 = 4U(4-3r3); beta_K=2(r3-1)/(4-3r3+delta); beta_K=1 <=> r3=(6+delta)/5,
V/T=(1+delta)^2/25; beta_K(r3=2)=2/(delta-2); V=T iff r3 in {0,2}; (1-r3)^2 = kappa3^2/4;
q_*^2|_chi = -beta_K U' L/(8m^4) = -L U'^2/(4m^4 U_chichi); eliminated quadratic =
(U4 - (1/4)beta_K U'_loop) sigma1^2 (held coefficient). Bounded no-go: c3!=0 + no negative mode
forces 0<r3<=3/2, disjoint from {r3=2}; r3=0 excluded by c3!=0 => NO point has V=T with no
negative mode; beta_K=1 & V=T needs r3=2 (negative mode) or r3=0,delta=-6 (outside one-loop
validity). Conditional on the held beta_K relation (its W_R-response caveat quoted at L203).

verify_example_129.py PASS: r3=1.1682, kappa3=-0.3365, V/T=0.0283, varrho=23.89, tree slope
5.34, slope ratio 0.1682, beta_K = 2*5.345/10.68 = 1.0000, ratio beta_K U'/(4U4) = -14.83
(held -14.8); also U_chichi consistency: 4U~(4-3r3+delta)=10.68 exactly at delta=5r3-6.

verify_weights_129.py PASS: sum(S.L)^2 vector content = N^2(N^2-1) EXACTLY = held factor
(corrects session-1 error); per-l cross term vanishes; (k3^2-4)chi^4 = c3^2 chi^2-4c3 chi^3
holds, vanishes at k3=2. FULL sum w lambda^2 identity (held report L183) uses spinor/ghost
supertrace bookkeeping -> CONDITIONAL, not payloaded; mathcalU negativity claim NOT payloaded.

Payload-F plan FINAL: (i) cubic-branch Hessian paragraph: shift identity (established here),
branch spectrum/multiplicities/no-negative iff -1<=k3<=2, k3=-2 mode, anchor k3=2 (= our L3194),
stationary chi=c3/2 point; (ii) tree-curve + scale-exchange paragraph incl. bounded no-go and
q_*^2<=0 (with L>=0 condition stated); (iii) example re-analysis: the held text's own admission
(block L203/L209: example NOT stationary with cubic term without counterterms; ratios -1, -0.32,
one-loop slope 9.2 > 5.34 tree) is the derivation-grade correction to OUR L3194 "beta_K=1 is
attained at a local minimum" sentence -> qualifier sentence. IKTW bib entry supplied (verified
arXiv hep-th/0101102 / DOI 10.1016/S0550-3213(01)00173-0) - KEY MISSING from bib/namcg.bib,
flag to author; no \cite until key added.

## Work order B (blocks 27, 28) -- classification

Block 27 (30.4 kB, items 068/071/075 region): 'Bearing on sec:status-E and the relaxations' +
compact SO(2) toy + locked-frame-composite diverged drafts. The relaxations (i)-(iv) are
hedged conditionals that ADD NO derivation-grade input to a named missing step: they conclude
'Assumptions not discharged, Problems D,E,F,N remain open', consistent with our current text.
Citations HoKawaiSteinacker2025, Chatzistavrakidis2011, IsonoTomino2010, Liao2026 NOT verified
here, likely absent from bib/namcg.bib (rule 7). Compact-toy paragraph duplicates our reviewed
compact-toy text in diverged form (import review sec.3/4). -> NOT-FOR-MANUSCRIPT (prior art;
would need a dedicated E-relaxations package with independently verified refs).

Block 28 (23.7 kB, items 072/073): Heisenberg background with curvature, characteristic cones
(q-alpha k)^2 = 0 with listed complex alpha, boost-dilation non-isolation argument, 'no
gauge-invariant gap at this order'. Internally coherent bounded E/D1-adjacent no-go, but its
reproduction pack depends on their 'family (i)' definitions embedded in the diverged drafts
(24x24/40x40 numerical matrices, sampled q) NOT reconstructible from our manuscript; no
contradiction with our OPEN E/D1 status. -> NOT-FOR-MANUSCRIPT this round; recorded as future
candidate package 'reproduce Heisenberg characteristic cones + gap statement', ranked BELOW
F-area follow-ups (it is a same-conclusion extension unless a gap appears in their numerics).

Item 075 (cubic/Hessian, NEEDS-EVIDENCE there) = block 48 P1 issue, resolved here by the
gauge-free shift identity: our evidence is stronger than their numerical Hessian claim because
ours pins the c=0 anchor as our OWN integrated text.

## Session 3: payload-F written, compile certificate PASS, proposal-r1.md written

Anchor re-verified live: tail "On this evidence the sign of \(\hat U\) depends on \(K\)." once (L3194);
"\emph{Scale dependence.}" once (L3196); c_3 only at L1720-1738 (payload disambiguates); r_3/kappa_3 free.
Payload = 2 paragraphs, 3113 B, CRLF ASCII, no \cite (bib key IsoKimuraTanakaWakatsuki2001 missing from
bib/namcg.bib -> author note + BibTeX in proposal). cert_129.py: out-of-repo splice + pdflatex/bibtex/pdflatex^2,
CERT129 PASS, exit 0, 450 pages, 0 undefined refs/citations, 0 multiply-defined, post 886190 B (= 883075+3113+2 join),
scratch deleted by script. IKTW re-verified via arXiv abs: Iso-Kimura-Tanaka-Wakatsuki, NPB B604 (2001) 121-147,
DOI 10.1016/S0550-3213(01)00173-0 (arXiv journal ref; Elsevier landing not fetched). All four verify scripts re-run
green (HESSIAN/TREECURVE/EXAMPLE/WEIGHTS PASS). proposal-r1.md written: per-block disposition table
(22 SUPERSEDED; 48p1 ADOPT-MODIFY->payload; 48p2 SUPERSEDED; 48p3+49-51 conditional/not payloaded; 42,27,28
NOT-FOR-MANUSCRIPT), claim classification, reproduction pack, ranked open avenues (1 weights from exact spectra,
2 sigma1 coupling, 3 supertrace, 4 C_tree, 5 Heisenberg cones, 6 E-relaxations). Item 128 / E.thimble / C.operator
untouched. No files outside proposals/129-rc-held-recheck changed.


## Round 2 (mechanical revision per review-r1 ACCEPT WITH REQUIRED REVISIONS)

Verdict r1: sound math, OPEN 0/2, three exact string fixes required (findings 1-3; 4-5 notes, no
action). Live pre-checks: appH 883,075 B / 4,146 lines, anchor+blank and boundary unique,
chapters/ porcelain-clean. edit_payload_r2_129.py applied the 3 mandated replacements (each
count==1 asserted): 5.345 to 5.34 (-1 B); 10^{-13} to 1.5x10^{-13} (+9 B); 'supplied there as'
to 'specialised there to ... on the flux directions' (+26 B). Payload 3,113 -> 3,147 B,
sha256_12=87a7c2568f72 sha1_12=0cf326eb3457; old r1 pins bcace605a53b/af564f3bf0b9 recovered
byte-exactly by inversion test (proof: only the 3 regions differ). check_payload_129.py:
pure-CRLF/ASCII/ends-CRLF, old strings absent, new once, eqref once, no cite/ref/label, expected
POST 883075+3147+2=886224 B; positive controls 4/4 fired (bare-lf, 5.345 reinjection, 0xE9,
stripped CRLF). Fixed verify_example_129.py L41 note 5.345->5.34 and 8 count-checked prose/quote
lines in proposal-r1.md (embedded quote now byte-matches r2 payload; zero 5.345 left outside
review-r1.md). Reproduction pack re-run: HESSIAN/TREECURVE/EXAMPLE/WEIGHTS all PASS (values
unchanged; tree slope 5.340000, beta_K=1.000000). cert_129.py on corrected payload: splice
883,075->886,224 B (= payload 3,147 + 2 B join, matches independent prediction), bibtex 0,
pdflatex exit 0/0, 450 pages, 0 undefined refs/citations, 0 multiply-defined, CERT129 PASS;
output saved cert-r2-output.txt, scratch deleted by script. proposal-r2.md written. F stays
OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL, no label touched. No files outside
proposals/129-rc-held-recheck changed.
