# Local re-review r1 (remote/claude, 2026-11-18): group B / C / D1

Source reading: digest + targeted reads (no full scan claimed).

## 065-b-ward-measure-insertion-sublemma (appH L506-519)
VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/0
The mathematics is verified: measure identity, null directions, conical-contact formula d S_D = Tr(G1 P G1 B) - 1/2 Tr(G1 B), and the derive_ward_r1.py C1-C4 checks.
Required revisions (all minor):
- m1 (L519, Craps2026): replace "no singlet-sector mechanism accounts for it" with "but the leg-pole transformation relating the target-space tachyon to the singlet-sector collective field does not account for it~\cite{Craps2026}".
- m2 (L519, ArataIsmailLiberati2026): replace "is the Noether charge of a genuine local symmetry \(\delta u^a=f\,a^a\) of the reduced, elliptic gauge-fixed action" with "is, in the static, spherically symmetric, asymptotically AdS sector with \(c_{14}=0\), the charge of a symmetry \(\delta u^a=f\,a^a\) of the reduced action, with \(f\) obeying an elliptic constraint".
- m3 (L511): replace "for Moyal corrections, field redefinitions and the measure of the matrix integral disclaimed in the preceding paragraph" with "for Moyal corrections and the measure of the matrix integral, disclaimed in the preceding paragraph, and for field redefinitions".
- m4 (L513, L519): write "The coefficient \(-4\kappa_X\) required at \(n_D=0\) in the paragraph on the matrix gauge realisation". This bears on local 070, which finds 0 = 0 at the IKKT content (6,2).
- m5 (L517): after "codimension-one hyperplane" add "(for \(P\neq\tfrac12A_1\))".
The negative survey claim ("None of these treats ...") is not independently verified beyond the abstracts.

## 059-d1-lorentz-local-frame (appH L1575, L1578)
VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: RESEARCHER-DECISION | PROGRESS: first | OPEN: 0/3
- M1 (major): the S^2 toy is not in "the class above". The lifts have [xi, D_a] = 0, so they violate the first class relation, and "T_12^2 = cot theta" is the anholonomy of the base frame, not torsion. That contradicts "torsion-free" and local 068's convention (T = 0). RESEARCHER-DECISION:
  - (a) Relabel. Replace the two sentences from "The class data of this connection" through "is not optional." with:
    The horizontal lifts \(\mathbb D_a=e_a-\omega_a\xi\), with \(\xi\) the fundamental vertical field, satisfy exactly \([\mathbb D_1,\mathbb D_2]=-\cot\theta\,\mathbb D_2-\xi\) and \([\lambda\xi,\mathbb D_a]=-(\mathbb D_a\lambda)\xi\) for every real \(\lambda\) on the base. They do not rotate the frame index, \([\xi,\mathbb D_a]=0\), so they satisfy the second class relation but not the first, and \(\lambda\xi\) acts as a circle gauge transformation without the rotation term \(\lambda^c{}_a\mathbb D_c\) of the class; read through the second relation alone, the anholonomy \([e_1,e_2]=-\cot\theta\,e_2\) of the base frame occupies the slot of \(\mathsf T\), \(\mathsf T_{12}{}^2=\cot\theta\), although the Levi-Civita connection is torsion-free, and \(\mathsf R_{12}{}^{12}=-1\) with \(\mathcal S_{12}=\xi\) (the curvature two-form \(\mathrm d\omega^{12}\) evaluates to \(+1\) on \((e_1,e_2)\)), with \(\mathsf F=0\). The \(\xi\)-component of \([\mathbb D_1,\mathbb D_2]\) is nonzero, \(-1\) in the basis \((\mathbb D_a,\xi)\) and \(-\csc^2\theta\) in the basis \((e_a,\xi)\), so the commutator of two horizontal lifts is not in the span of the \(\mathbb D_a\) over the base functions when the curvature is nonzero, and the slot \(\tfrac12\mathsf R_{ab}{}^{cd}\mathcal S_{cd}\) of the class relation is not optional.
    The closing phrase changes to "Abelian in fibre, non-equivariant in the frame index, built on the torsion-free Levi-Civita connection and two-dimensional".
  - (b) Recompute with equivariant lifts. The gatekeeper verified T = 0, S_12 = -xi, R = -1, and prefers (b).
- M2 (major): "the commutator of two first-order operators is not itself first-order" is false. The correct statement is "not in the span of the D_a over base functions"; -csc^2 theta is basis-dependent (-1 in the (D_a, xi) basis).
- M3 (major): the composite paragraph reinterprets ass:frame-lock (a literal VEV), in conflict with ch04 Repair II and ch10. Make it conditional:
  - "on a gauge-invariant reading, which Chapters~\ref{ch:vierbein-emergence} and~\ref{ch:lorentz-locking} do not adopt, the locking of Assumption~\ref{ass:frame-lock} would be represented"
  - "On that reading Assumption~\ref{ass:nondeg} would become"
  - "and the locking would be read as"
  Adopting the reading outright would need a STRUCTURAL package and a full scan.
- m1: define rho_i = eps_ijk x_j d_k.
- m2: replace "This is the finite-size regularization ... of \cite{HattoriSekoTsuchiya2026}" with "Compare the Berezin--Toeplitz finite-size regularization of covariant-derivative configurations, including \(S^2\), of \cite{HattoriSekoTsuchiya2026}".
- m3: after "showed that" insert "for Higgs fields in the fundamental representation".
- m4: add the "(conditional; not closure)" tags.
Verified correct: the fuzzy-sphere inner derivations, the ghost spectrum l(l+1) with multiplicity 2l+1, and the O(hbar_eff) redundancy violation.

## 062 block 1: Problem C "Missing step" (appH L685)
VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1
- M1: the restated target leaves out ch17's phenomenological comparison. After "its pole mass as a derived output," insert "and the phenomenological comparison of Chapter~\ref{ch:agenda}, defining and testing either a sufficiently heavy \(m_\psi\) or the scalar-tensor outcome,".
- m1: replace "three of the inputs it needs are among the things the target is meant to establish" with "three of the inputs it needs are not derived".
- m2: replace "the trace of the tensor fluctuation" with "the trace of the metric fluctuation \(h_{\mu\nu}\)".

## Cross-package
- Local 070's anchor no longer exists (the 065 paragraphs now sit before \section{Problem C}). Re-anchor 070 and reconcile it with 065 m4.
- Local 068's torsion convention contradicts the 059 toy. Fix 059 first.
- Label changes: none. B, C and D remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
