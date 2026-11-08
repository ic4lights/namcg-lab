## scan-p4.md: full-scan pass 4 of 5 (ordinal-55 CLAUDE.md 3(a) scan), chapters ch01–ch09

**Read-only.** I made no edits and no git writes.

**Pre-checks**
- `git status --short`: ` M chapters/appH-microscopic-proofs.tex`, plus untracked `proposals/057-mass-plane-class/scan-p1.md`, `scan-p2.md`, `scan-p3.md`.
- `git diff --stat -- chapters`: only `chapters/appH-microscopic-proofs.tex` is modified (35 insertions). This matches what was expected.
- I read the whole of `C:\Users\redgi\Projects\namcg-lab\proposals\057-mass-plane-class\appH_insert.tex` (lines 1–10).

**Files and lines read, in full and consecutively** (all under `C:\Users\redgi\Projects\namcg-lab\chapters\`)
- ch01-geometrogenesis.tex, lines 1–385 of 385
- ch02-preliminaries.tex, lines 1–582 of 582
- ch03-matrix-action.tex, lines 1–915 of 915 (read as 1–459 and 460–915)
- ch04-vierbein-emergence.tex, lines 1–441 of 441
- ch05-lorentz-decomposition.tex, lines 1–418 of 418
- ch06-entanglement-equilibrium.tex, lines 1–457 of 457
- ch07-massless-tensor.tex, lines 1–475 of 475
- ch08-heat-kernel.tex, lines 1–410 of 410
- ch09-ultraviolet.tex, lines 1–391 of 391

Supporting greps:
- No label is defined twice within ch01–ch09.
- These cross-file targets exist: `app:status`, `sec:status-E`, `sec:status-I`, `sec:status-J`, `sec:status-N`, `thm:locking`, `prop:B-torsion-free`, `eq:D-both`, `eq:Z-sigma`.
- I grepped every signature statement in ch01–ch09.

**1. Conflicts with the 057 insert or the 053–056 Problem E blocks: none found**
- ch04:313–333 (`ass:lorentzian`, L321–328) says signature is borrowed from η_AB and that its dynamical emergence "is not proved … and is not pretended here". ch04:375 lists "The signature is dynamical" among the results not obtained. This agrees with the 057 closing sentence that the two classes "select no signature" and do not discharge `ass:lorentzian`.
- ch03:172–205 (`def:matrix-coords-ext`) says the Lorentzian signature of the matrix-index form η_IJ "is retained as Assumption ass:lorentzian". This is the same reading as the 057 use of η in S_b.
- Wick rotation and Euclidean forms appear in ch02:276–278 and 289–305, ch06:192–198 and ch08:80 and 151–153. All of these concern the Presentation-B field theory and say the continuation is conditional. None of them asserts anything about the regulated Lorentzian matrix integral, the mass term or the ε→0 limit treated in 057.
- ch09:184–197 says Lorentzian boundedness of the matrix action "is not solved here". This is consistent with 057 leaving the fixed-γ>0 limit undecided.
- Nothing in ch01–ch09 claims Lorentzian signature is derived or emergent.

**2. Status, priority and completion statements: no contradiction with ch17 or Appendix H**
- ch01–ch09 contain no status, priority or completion labels. They only record that problems remain open.
- ch03:445, 596 and 786 each end with "Problems B, C, D, F and G remain open". This is a fixed partial list rather than a pointer to the current criterion, but it is not false. Note.

**3. Labels, references and notation**
- **ch01:321–323, minor.** The text says "Chapter 16 restates the whole derivation… Chapter 17 lists what would falsify". The include order is ch16 = falsifiers and ch17 = agenda, so these hard-coded chapter numbers appear wrong.
- **ch01:325–326, minor.** Two consecutive `\paragraph` headings ("Prerequisites." and "What you need.").
- **ch05:174 and 181, minor.** A stray "." follows `\end{equation}`.
- **Note (clashes with 057 symbols; pre-existing, none blocking).** A reader could confuse 057's symbols with these:
  - Θ^{μν}, the noncommutativity tensor (ch02:580, ch03 throughout, ch04 SW map), against Θ(E) in 057.
  - γ^μ, the Clifford generators (ch01:145, ch03:297, ch05:145 and 173), against the mass parameter γ and γ′.
  - η, used for the drag coefficient (ch01:266, ch06:339) and for the loop fluctuation (ch02:298, ch08:54), against the metric form η in S_b.
  - h, used for the metric perturbation h_{μν} and h^A_μ (ch04:292–299), against the complex symmetric form h in 057.
  - ε_{μν}, the polarization (ch07:353), and ε, the exercise parameter (ch04:402), against the regulator ε.
  - φ does not occur. φ appears only as a generic scalar (ch02, ch03:725–757).

  The 057 insert defines its symbols locally inside Appendix H, so none of these clashes blocks integration.

**4. Overbroad or materially false claims**
All are pre-existing and committed. None is a PRIOR-CLAIM-ERROR (a previously accepted claim found to be wrong) that bears on 057.
- **ch04:330–333, minor.** "What the book does derive, contingent on ass:lorentzian, is the dynamics of the resulting Lorentzian metric" overstates the position: B, C, D, F and N remain open. Suggest "conditionally develops".
- **ch01:64, 257–259 and ch06:47–48, minor.** "theorems inside the framework" and "a Ward identity … forbids m_T²≠0" are stated without qualification. ch06:51–56 and ch07:315–331 correctly downgrade this to a hypothesis and a compatibility statement.
- **ch05:347–349, minor.** It says two TT helicities follow under the "separately established" massless limit (thm:mT). thm:mT is conditional on Hypotheses 4–6.
- **ch05:321–322, 418–419; ch07:19–21; ch08:22; ch09:325, 381, minor.** Each reads off m_T=0 or Einstein gravity without the qualifier "conditional on thm:mT".
- **ch02:582–583, ch03:22–23 and 915–916, note.** "geometry … is an output" leaves out that the signature is an input (`ass:lorentzian`).
- **ch03:838–850, note.** The collected-assumption list leaves out `ass:lorentzian`. That assumption is introduced in ch04, so this is consistent but incomplete.
- **ch04:311, minor.** It says existence of a global Minkowski condensate "is part of ass:nondeg". That assumption only states that det e ≠ 0.
- **ch02:289–290, minor.** "hyperbolic, after Wick rotation" has the direction reversed: a hyperbolic operator becomes elliptic after Wick rotation.
- **ch09:163–164, minor.** The saddle ⟨Φ^I_A⟩=vΛ^A_I has mismatched index placement.
- **ch09:231, minor.** It says "Two distinct properties" but lists three items.
- **ch02:438–440, minor.** The sentence on the additive constant is garbled but harmless.

**5. Chat or process language**
- **ch02:490, minor.** It refers to "Theorem 2 in the ultraviolet note".
- **Note.** References to "the source notes" occur throughout ch03–ch05. They are attributions, not process language. Nothing addresses the reader as "the researcher" or says "as proposed".

**Does anything block integrating the 057 insert?**
No. Nothing in ch01–ch09 blocks integrating the 057 insert. All findings above are minor or notes in committed text and are independent of 057. None needs to be fixed before or as part of the 057 insertion.
