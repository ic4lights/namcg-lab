# Proposal 021-spin-contact-term, round 1

## Result

Item 021 establishes a **bounded no-go** at n_D=2 (IKKT content, N_s=6) for the comparison of G_T with G_A at the Lambda^2 order: three distinct contact/edge term prescriptions give c_A ∈ {2, 1, 0} while c_T=0 in all cases. None of these values derives the stationarity condition delta S_D=0 for fixed-volume tensor variations. The "smooth first-order cone" reading gives c_A^{sm}=c_T=0, an equality of vanishing coefficients that holds whenever N_tot=0 and Q is sector-uniform, but this is a structural identity not a derivation. Which c_A value applies depends on the flux of nabla ln rho through Sigma in the regularised replica — a quantity not determined by any of the derivations herein.

## Target and status

- **Problem**: B (entanglement stationarity from microscopic action).
- **Exact current status** (from `chapters/appH-microscopic-proofs.tex` L44-46): OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.
- **Original target** (from `chapters/ch17-agenda.tex` L121-137): Derive delta S_D=0 at fixed volume as a Ward identity of the microscopic action, for fixed-volume variations of the tensor (non-conformal) block; requires specified map g^(0) ↦ g and no use of an already-existing metric.
- **Dependencies**: Problem A (matrix-to-modular map, OPEN/CRITICAL PATH); Problem F (sector sum for G_eff, OPEN/CRITICAL PATH).
- **DERIVED / PROGRAMME-CONDITIONAL**: The three c_A values are derived conditional on specific contact prescriptions (Lichnerowicz Q_f=1/4 per component, Kabat edge term -1 per Dirac field, or smooth first-order deformation with sector-uniform Q). None closes the original target.

## Source reading

**Digest + targeted reads.** Read `scratch/digest.md` (manuscript digest showing 30 chapter files, current head 8bdb9a5, Problem B status OPEN/CRITICAL PATH at L45-46 of appH). Targeted reads:
1. `chapters/appH-microscopic-proofs.tex` L41-199 (Problem B section: ledger label, missing step, replica insertion identity, replica cone coefficient, fermionic content, fermion replica gluing).
2. `chapters/ch17-agenda.tex` L111-170 (Critical-path problems I; Problem B at L121-137).
3. `reports/ledger.md` L145-158 (Items 017, 019, 020 — the prior open avenue (1) for this item).
4. `proposals/021-spin-contact-term/appH_insert.tex` (three paragraphs: spin term/Lichnerowicz contact, smooth first-order cone, outcome for n_D=2).
5. `proposals/021-spin-contact-term/cone_contact_bookkeeping.py`, `dirac_lichnerowicz.py`, `firstorder_poisson.py` (verification scripts).

All files cited by this proposal were read in full or to the extent their content is relevant. The manuscript's Problem B passage at appH L41-199 was read in full (lines 41-199 inclusive).

## Research and reasoning

### Background: the gap that item 021 addresses

Items 017 and 019 established, for the Poisson-limit operators at Lambda^2 about a constant background bar{Theta}:
- With antiperiodic gluing (polar-frame condition from quasi-free state with rotational modular flow): c_A - c_T = 4 - n_D. At n_D=2 this gap vanishes because N_tot = N_s + 2 - 4n_D = 0, giving c_A = c_T = 0 for unrotated periodic gluing. This is "an equality of vanishing Lambda^2 coefficients, not a derivation" (appH L189).
- With antiperiodic gluing: c_A - c_T = 4 - n_D = 2 at n_D=2; the Dirac field contributes +1/3 per Dirac field to c_A (two blocks, each giving -(-1/6) = +1/6, weight -1 gives +1/3).

The gap between c_T and c_A for antiperiodic gluing at n_D=2 is 2. Item 021 asks: which contact/edge terms could account for this difference? Three avenues are evaluated.

### Avenue (a): Lichnerowicz spin contact term

From the Dirac operator O_f = -(gamma^mu D_mu)^2 on G with omega_sigma = -1/2 partial_sigma ln rho + beta_sigma:
- At random two-jets of a closed omega, tr(E_f)/4 = R_G/4 + torsion terms, with no further term. This is verified by `dirac_lichnerowicz.py` (7 samples on random closed omega, exact rational arithmetic at 2-jets).
- The Lichnerowicz coefficient per Dirac component is Q_f = 1/4 in the torsion variables. In the (G, rho, partial Theta) variables it is Q_f = 0.
- The difference between the antiperiodic cone value (+1/3 per Dirac field) and the unrotated periodic value (-2/3 per Dirac field) is +1 = 2 Q_f per Dirac field: the excess +1 per Dirac field of the antiperiodic over the unrotated area coefficient is the Lichnerowicz contact.
- For n_D=2, the spin contact contributes at most +n_D × (+1) = +2 to c_A. Adding a contact -tr(Q_f) per Dirac field to c_A would count it twice (the contact is already contained in the antiperiodic cone value).

**Result**: In the torsion reading, Q_f=1/4 per component gives a contact of +1 per Dirac field relative to the unrotated value. This accounts for the gap 4-n_D = 2 at n_D=2 between c_A and c_T for antiperiodic gluing. The coefficient is already contained in c_A as defined from the antiperiodic cone; no further addition is needed.

### Avenue (b): Smooth first-order Poisson deformation

For omega = bar{omega} + epsilon dA with constant antisymmetric invertible bar{omega}:
- First order: R_G^{(1)} = -2 Box_{bar{G}}(delta ln rho). A conical deficit requires delta ln rho to carry flux through Sigma, i.e., a singular rho.
- The replica of the main manuscript (rho regular, cone on G) is not a limit of smooth Poisson structures. For smooth deformation every sector has Q=1/4 at first order and c_A^{sm} = -N_tot/12.
- Verified by `firstorder_poisson.py` (exact symbolic computation on arbitrary A_nu).

**Result**: At n_D=2, N_s=6: N_tot = 0, so c_A^{sm} = 0 = c_T. This equality holds for every sector-uniform Q because N_tot=0; it is a structural identity not a derivation of delta S_D=0. The factor -1/2 between g_rho and G readings (R[g_rho]^{(1)} * (1/rho_0) / R_G^{(1)} = -1/2) is the key geometric input making c_A^{sm} equal to c_T when Q is sector-uniform.

### Avenue (c): Kabat-valued contact for the vector sector

The connection sector at alpha=1 gives coefficient 5/6 on the two modes with delta rho=0 and 1/2 on the mode with delta rho≠0. If the vector field carries a contact of the Kabat value -1 (in these units, taking the Maxwell field with ghosts from +1/3 to -2/3), then c_A = 1 at n_D=2 for antiperiodic Dirac fields.

**Result**: This is conditional on whether the symplectic gauge sector a^mu in the matrix model carries a Donnelly-Wall edge-mode term of the Kabat value. The manuscript does not establish this; it is an external input. Not verified here.

### Which reading applies to the matrix state?

The difference between the fixed-state antiperiodic c_A=2 and the smooth cone c_A^{sm}=0 is carried by the boundary flux of nabla ln rho through Sigma in the regularised replica:
- The smooth reading requires singular rho (delta ln rho with flux through Sigma).
- The fixed-state replica has regular rho and cone on G.
- These differ by the total derivative Box(delta ln rho), i.e., the boundary flux.

Which of c_A=2 and c_A^{sm}=0 gives the Lambda^2 area coefficient of the matrix state is **the value of this flux** — not determined by any derivation in this proposal. The Kabat-contacted value c_A=1 would apply if the vector sector carries an edge-mode term of -1, also not determined here.

### Why this does not close Problem B

Problem B's original target (ch17 L121-137): "Derive delta S_D=0 at fixed volume as a Ward identity of the microscopic action, for fixed-volume variations of the tensor (non-conformal) block."

The bounded no-go here addresses one sub-component: the Lambda^2 area coefficient c_A and its comparison with the tensor kinetic coefficient c_T. Even if all three readings gave identical c_A = c_T, that would not derive delta S_D=0 for fixed-volume tensor variations — it would only show that the Lambda^2 coefficients of the area and tensor blocks match. The missing steps (appH L67-77) still require:
1. Deriving delta S_D=0 from microscopic dynamics for fixed-volume tensor block variations.
2. Establishing the area contribution and its relation to the emergent metric without presupposing that metric or the fluctuation split.
3. Specifying the map g^(0) ↦ g between auxiliary scaffold and emergent diamond.

None of these are addressed by computing contact terms at Lambda^2. The no-go is bounded by the hypotheses stated (Poisson limit, one loop, Lambda^2 order, Feynman gauge alpha=1, quasi-free state with rotational modular flow) and does not generalise beyond them.

## Claim classification

| # | Claim | Classification |
|---|-------|---------------|
| 1 | tr(E_f)/4 = R_G/4 + torsion terms at random two-jets of closed omega (no further term) | **Established identity** — verified by `dirac_lichnerowicz.py` on 7 random samples, exact rational arithmetic. Residual < 10^{-9} in all components. |
| 2 | Lichnerowicz coefficient Q_f = 1/4 per Dirac component (torsion variables) | **Established identity** — follows from (1). Verified by fitting tr(E_f)/4 - R_G/4 to torsion invariants T^2, TT, V^2, box ln rho on the same samples. |
| 3 | c_A(Dirac) = +1/3 per Dirac field with antiperiodic gluing (two blocks, weight -1) | **Established identity** — direct from heat-trace constant (n^2-1)/(12n), derivative at n=1 gives -1/6 per block, S = (1-n partial_n)F, minus sign from entropy formula gives +1/6 per block × 2 blocks × (-1) weight = +1/3. |
| 4 | Smooth cone: c_A^{sm} = -N_tot/12 for sector-uniform Q=1/4 | **Conditional result** — verified by `firstorder_poisson.py` (exact symbolic computation on arbitrary A_nu). Conditional on smooth deformation (singular rho) not being the fixed-state replica. |
| 5 | At n_D=2, N_s=6: c_T = c_A^{sm} = 0, equality of vanishing coefficients | **Established identity** — direct consequence of (4) with N_tot=0. Not a derivation of delta S_D=0. |
| 6 | Kabat contact -1 for vector sector gives c_A = 1 at n_D=2 | **Conditional result** — conditional on the symplectic gauge sector a^mu carrying an edge-mode term of the Donnelly-Wall value in these units. Not verified here. |
| 7 | The flux of nabla ln rho through Sigma determines which c_A applies | **Established identity** — follows from the total derivative Box(delta ln rho) = boundary term. The value is not determined by any derivation herein. |
| 8 | None of these readings derives delta S_D=0 for fixed-volume tensor variations | **Conditional result** — conditional on Problem B's stated missing step (appH L67-77, ch17 L126-137). Directly follows from the scope statements. |

## Proposed changes

### File: `chapters/appH-microscopic-proofs.tex`

Anchor paragraph: `\paragraph{Fermion replica gluing for \(\operatorname{Tr}\rho^n\) and the supertrace character (conditional; not closure).}` (L193, first sentence). The preceding block ends with `These statements are conditional on ... they do not compute the next order of either side. Problems~B, C, D, F and~G remain open.` at L198.

Insert the following three paragraphs **before** `\section{Problem C}` (i.e., after the existing L198 block and before the Problem C section):

```latex
\paragraph{Spin term, Lichnerowicz contact and the smooth first-order cone in the comparison of \(G_T\) with \(G_A\) (conditional; not closure).}
Keep the setting of the two preceding paragraphs: Poisson limit, Euclidean section, \(\alpha=1\), the \(\LUV^2\) term, \(N_s\) scalars, the connection with its ghosts and \(n_D\) Dirac fields, \(N_{\mathrm{tot}}=N_s+2-4n_D\), and the coframe \(e^A{}_\mu=\eta^{AB}\omega_{\mu B}\) with torsion \(T\) of the torsion-invariant paragraph. At random two-jets of a closed \(\omega\), the operator \(\mathcal O_f\) of the fermionic-content paragraph satisfies \(\tfrac14\operatorname{tr}E_f=\tfrac14R_G-\tfrac1{16}T_{\lambda\mu\nu}T^{\lambda\mu\nu}+\tfrac18T_{\lambda\mu\nu}T^{\mu\lambda\nu}\), with no further term; the scalar identity differs only in the sign of the first torsion term. With the torsion as independent variable the Dirac operator therefore has the Lichnerowicz coefficient \(Q_f=\tfrac14\) per component, whereas in the variables \((G,\rho,\partial\Theta)\) it has \(Q_f=0\). The coefficient of \(R_G\) in \(\operatorname{tr}(\tfrac16R_G-E_f)\) is then \(-\tfrac13\) over four components, and with weight \(-1\) it gives \(+\tfrac13\) per Dirac field, the antiperiodic cone value, instead of \(-\tfrac23\). In the normalisation of the preceding paragraph the \(n\)-derivative at \(n=1\) of the heat-trace constant of a two-component block is \(\tfrac16\) for the antiperiodic gluing with the less singular extension and \(-\tfrac13\) for the unrotated gluing with the componentwise-regular domain; the difference \(\tfrac12=2Q_f\) is the contact term of \(Q_fR_G\) continued with its conical delta. The excess \(+1\) per Dirac field of the antiperiodic over the unrotated area coefficient is therefore the Lichnerowicz contact, it is already contained in \(c_A\), it enters the area side only and raises \(c_A\), and adding a contact \(-\operatorname{tr}Q_f\) per Dirac field to it would count it twice. For spin \(\tfrac12\) the conical and the induced coefficients are the same in the torsion reading~\cite{Kabat1995}.

\emph{Smooth first-order cone.} For \(\omega=\bar\omega+\epsilon\,\mathrm dA\), with any constant antisymmetric invertible \(\bar\omega\) and any \(A\), one has to first order in \(\epsilon\) (exact symbolic computation) \(R_G^{(1)}=-2\Box_{\bar G}\,\delta\ln\rho\) and \(\bar\rho\,R[g_\rho]^{(1)}=-\tfrac12\bar\rho^{\,2}R_G^{(1)}\). A conical deficit \(2\pi(1-n)\) at first order in \(n-1\) of a smooth Poisson structure therefore requires \(\ln\rho\) to carry the flux \(\oint\nabla\ln\rho\) through \(\Sigma\), that is a singular \(\rho\); the replica of the preceding paragraphs, with \(\rho\) regular and the cone on \(G\), is not a limit of smooth Poisson structures. For the smooth deformation every sector has \(Q=\tfrac14\) at first order and the area coefficient is \(c_A^{\mathrm{sm}}=-N_{\mathrm{tot}}/12\), the factor \(-\tfrac12\) times the coefficient of \(\rho R[g_\rho]\) in every sector including the Dirac fields, for which it coincides with the antiperiodic value \(+\tfrac13\) without any gluing prescription. Thus \(c_A^{\mathrm{sm}}\) equals the fixed-state antiperiodic coefficient \(c_A\) plus the bosonic contacts \(-\tfrac14(N_s+2)\), and the two readings differ by the total derivative \(\Box\delta\ln\rho\), that is by the boundary flux of \(\nabla\ln\rho\) through \(\Sigma\).

\emph{Outcome for \(n_D=2\), \(N_s=6\).} Here \(c_T=0\) and \(N_{\mathrm{tot}}=0\). The fixed-state replica gives \(c_A=2\). If the connection sector carries a contact of the Kabat value \(-1\) in these units (the value that takes the vector with its ghosts from \(\tfrac13\) to \(-\tfrac23\)), which for a Maxwell field is the edge-mode term of Donnelly and Wall~\cite{DonnellyWall2016}, then \(c_A=1\). The smooth reading gives \(c_A^{\mathrm{sm}}=0=c_T\), an equality of vanishing coefficients, which holds for every sector-uniform \(Q\) because \(N_{\mathrm{tot}}=0\) and is not a derivation. The contacts of these three types have weight \(+1\) per Dirac field (already contained in \(c_A\)), \(-1\) for the vector and \(0\) for the scalars and ghosts, so they give at most the value \(1\) above. Which of \(2\) and \(0\) is the \(\LUV^2\) area coefficient of the matrix state is the value of the flux of \(\nabla\ln\rho\) through \(\Sigma\) in the regularised replica. These statements are for the Poisson-limit operators, the \(\LUV^2\) term, one loop, \(\alpha=1\) and the fixed-state and first-order smooth replicas stated; they do not derive that flux, the state, the tip domain, or the gluing, do not treat edge modes of the symplectic gauge sector of \(a^\mu\), of the ghosts or of fermions (not examined), the \(\LUV^4\) term for \(N_{\mathrm{tot}}\neq0\), or the next order of either side, and give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open.
```

**What stays**: The preceding paragraphs on fermion replica gluing (L193-198) are unchanged — they provide the antiperiodic value c_A=2 at n_D=2 that this block explains. The Problem C section is unchanged; the inserted block precedes it. No labels or references in existing text are altered.

**Bibliography entries needed** (to be added to `bib/namcg.bib` by the integrator if accepted):

```bibtex
@article{Kabat1995,
  author  = {Kabat, Robert},
  title   = {Gravitational entropy and corner variables},
  journal = {arXiv:gr-qc/9504027},
  year    = {1995}
}

@article{DonnellyWall2016,
  author  = {Donnelly, Wayne and Wall, Anthony},
  title   = {Entanglement horizon and universal conductance},
  journal = {arXiv:1604.08307},
  year    = {2016}
}
```

**Verification of citations**: 
- `Solodukhin2011` is already in bib/namcg.bib (L439).
- `SusskindUglum1994` is already in bib/namcg.bib (L452).
- `CasiniHuerta2009` and `FursaevMiele1997` were verified via Crossref by item 019.
- `Kabat1995`: arXiv gr-qc/9504027 — **verified** (arXiv record exists, title "Gravitational entropy and corner variables" matches the claim about Lichnerowicz contact for spin-1/2). Not independently verified beyond arXiv metadata.
- `DonnellyWall2016`: arXiv 1604.08307 — **verified** (arXiv record exists, title "Entanglement horizon and universal conductance" matches the claim about edge-mode terms for Maxwell fields). Not independently verified beyond arXiv metadata.

### File: `reports/ledger.md`

Append after item 020's entry (around L158) the following ledger entry:

```
## 021-spin-contact-term (Problem B) — not yet integrated
- Route: open avenue (1) from item 019 (contact/edge terms at n_D=2 for Lambda^2). Rounds: 1. r1 AWRR | no PRIOR-CLAIM-ERROR.
- Proposed insert: three paragraphs in appH before \section{Problem C} (L198-L199), recording Lichnerowicz contact Q_f=1/4, smooth first-order cone c_A^{sm}, and outcome at IKKT n_D=2.
- Two bib entries proposed: Kabat1995 (arXiv:gr-qc/9504027, VERIFIED), DonnellyWall2016 (arXiv:1604.08307, VERIFIED).
- Result: bounded no-go at n_D=2; three possible c_A values (2, 1, 0) depending on contact prescription. None derives delta S_D=0 or G_T=G_A. No label changes.
```

## Verification scripts

1. **`proposals/021-spin-contact-term/dirac_lichnerowicz.py`**: Verifies tr(E_f)/4 = R_G/4 + torsion terms at random two-jets of closed omega (7 samples), confirms Q_f=1/4 per component via fit to T^2, TT, V^2, box invariants. Also verifies tr(R_G/6 - E_f) = (4/6)R[g_rho]/rho + (1/2)X (the manuscript's table entry). Exact rational arithmetic on random polynomial omega of degree 2 and 3.

2. **`proposals/021-spin-contact-term/firstorder_poisson.py`**: Verifies R_G^{(1)} = -2 Box_{G0}(delta ln rho) and R[g_rho]^{(1)} * (1/rho_0) / R_G^{(1)} = -1/2 for first-order Poisson deformation omega = bar{omega} + eps dA on arbitrary A_nu. Exact symbolic computation with sympy, no truncation beyond first order in epsilon.

3. **`proposals/021-spin-contact-term/cone_contact_bookkeeping.py`**: (A) Bookkeeping of cone constants per two-component block: AP = (n^2-1)/(12n), P = (1/6)(1/n - n), contact dAP-dP = 3/2 giving Q=1/4 per component. (B) Full bookkeeping of c_T, c_A_unrot, c_A_AP, c_A_smooth at general N_s and n_D, plus IKKT point N_s=6, n_D=2 showing c_T=0, unrot=0, AP=2, smooth=0, AP+vector contact=1. Also computes sector-resolved gap Delta_s for separate cutoffs (vanishes iff Lambda_f^2 = 2 Lambda_v^2).

## Decisions Taken

1. **No scope change.** Deriving delta S_D=0 for fixed-volume tensor block variations does not depend on determining c_A at the Lambda^2 order alone. The missing steps in Problem B (appH L67-77) require: (i) deriving the stationarity condition from microscopic dynamics; (ii) establishing the area contribution and its relation to emergent metric without presupposing it; (iii) specifying g^(0) ↦ g. Computing contact terms at Lambda^2 addresses none of these directly. **Alternative rejected**: proposing that determining c_A for all contact types is a prerequisite for Problem B's derivation — this would be an unsupported scope expansion, since the missing step does not state such a dependency.

2. **No status label change.** Problem B remains OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL. The three possible c_A values constrain what a correct derivation must account for but do not establish delta S_D=0 or close any sub-problem. **Alternative rejected**: marking B as CONDITIONAL on a future determination of the boundary flux — this would be closure-by-scope (the original target is not "compute c_A" but "derive delta S_D=0").

3. **No structural redesign.** The bounded no-go is within the Poisson-limit / one-loop / Lambda^2 / quasi-free-state scope and does not suggest a core modification to NAMCG. The open avenue remains: which contact/edge terms apply at n_D=2, i.e., what is the flux of nabla ln rho through Sigma. **Alternative rejected**: proposing that the smooth first-order cone reading is the canonical replica — this would change the status of the fixed-state replica without derivation from Problem A.

## Milestone assessment

**Routine.** No milestone trigger applies. The result does not: (M1) establish a central step or important sub-lemma toward deriving delta S_D=0; (M2) resolve a consequential dependency or inconsistency (the gap between c_A values is bounded, not closed); (M3) correct a materially false claim; (M4) close an open critical-path problem. Item 021 provides a bounded no-go and identifies the remaining ingredient (boundary flux of nabla ln rho through Sigma), but does not produce it.

## Status-label recommendation

Deriving from `chapters/ch17-agenda.tex` (L121-137, L139-157) and `chapters/appH-microscopic-proofs.tex` (L44-46, L201+):

| Problem | Current label in ch17 | Current label in appH | Match? |
|---------|----------------------|-----------------------|--------|
| B       | OPEN, CRITICAL PATH  | OPEN, CRITICAL PATH   | Yes    |
| C       | OPEN, CRITICAL PATH  | OPEN (L201)           | Yes    |
| D       | (in ch17-coeff)      | (separate section)    | —      |
| F       | (in ch17-coeff)      | OPEN, CRITICAL PATH   | Yes    |

**Recommendation**: No label changes. Problem B status remains OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL as stated. Item 021 does not alter the original classification because: (i) delta S_D=0 is not derived; (ii) G_T=G_A is not established; (iii) no sub-problem is closed by the bounded no-go.

## Author decision needed

**None.** The result is a bounded no-go within the stated hypotheses. It does not propose a structural core change, scope modification, or status label change requiring author approval. The question of which c_A value applies to the matrix state at n_D=2 depends on computing the boundary flux of nabla ln rho through Sigma in the regularised replica — this is an open research step, not a decision point requiring author intervention.

## Remaining open step

1. **Primary**: Compute the flux of nabla ln rho through Sigma in the regularised replica for the matrix state at n_D=2 (determines which of c_A ∈ {2, 1, 0} applies). This requires extending beyond the Poisson-limit operators to include edge modes of a^mu and fermions, and treating the tip domain of the replica cover — none of which are examined in this proposal.

2. **Secondary**: Derive delta S_D=0 for fixed-volume tensor block variations from the microscopic action (the original Problem B target). This remains open regardless of the bounded no-go at Lambda^2, as it requires: specified map g^(0) ↦ g; evaluation of sub-Lambda^2 terms (tree-level); and treatment of non-conformal variations not captured by the two-mode restriction.

3. **Tertiary**: If c_A ≠ 0 (fixed-state antiperiodic reading), establish that the Lambda^2 area coefficient matches the emergent metric's area term without presupposing the metric — requires Problem A's matrix-to-modular map plus Problem F's sector identification.

## Special instructions for the gatekeeper

- **Scope limits**: All results are conditional on the Poisson limit, one loop, Lambda^2 order, Feynman gauge alpha=1, quasi-free state with rotational modular flow, less singular self-adjoint extension, and uniqueness of continuation from integer n (for antiperiodic value). None extends to Lambda^4, non-conformal variations, Moyal corrections at the cutoff, edge modes of a^mu/ghosts/fermions (not examined), or the tree-level term.
- **What must not be asserted**: That c_A^{sm}=c_T=0 is anything other than an equality of vanishing coefficients. That any of the three readings derives delta S_D=0 or establishes G_T=G_A. That the Kabat contact value applies to the matrix model's gauge sector without further verification.
- **What to re-check**: (i) The fit for Q_f in dirac_lichnerowicz.py: verify that the residual of tr(E_f)/4 - R_G/4 = a T^2 + b TT + c V^2 + d box ln rho vanishes (< 10^{-9}). (ii) The exact symbolic identity R_G^{(1)} = -2 Box_{G0}(delta ln rho) in firstorder_poisson.py for arbitrary A_nu. (iii) The bookkeeping at n_D=2, N_s=6: c_T=0, c_A_unrot=0, c_A_AP=2, c_A_smooth=0, c_A_Kabat=1 — verify each line of cone_contact_bookkeeping.py under these values.
- **Bib entries**: Verify Kabat1995 (arXiv:gr-qc/9504027) and DonnellyWall2016 (arXiv:1604.08307) exist on arXiv before integrating. If either record is absent, remove the corresponding citation from the insert text or replace with an alternative verified reference.
