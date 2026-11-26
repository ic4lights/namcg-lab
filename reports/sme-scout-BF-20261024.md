SME-SCOUT: 7 routes | TOP: B:Lambda^2 entropy of rho^2X via Wald/Noether with Solodukhin-type mediator contact (S_BH = S_ent - Q) and Lie-dragged boost-invariant Theta; F:spin-resolved (Nikishov/Hattori-Itakura-Ozaki) m^2 -> m^2 +/- 2f decomposition of the Zeeman vector-mass term at order eps^2; B:constraint-term Noether charge in the Prabhu/Jacobson-Mohd bundle framework | EMERGENCE-RISK: low

Reading mode: digest + targeted reads. In this session I read:
- the Problem B ledger label and missing-step paragraphs;
- the G_T/G_A normalisation paragraph (appH line 174);
- the 036 and 037 blocks (the "Comparator ..." paragraph and the preceding edge/holonomy paragraph);
- grep hits for the Zeeman paragraphs of F;
- the tail of reports/ledger.md (entries 030-037).

I did not re-read the 034 and 032 F blocks in full. Sources are verified by arXiv API record (title, authors, year, journal_ref) unless marked "abstract only" or "not independently verified". I quote no equation numbers.

## 0. Where B and F stand (my reading)

**B.** The Lambda^2 gap is 1/G_A - 1/G_T = 2 Lambda_{UV,v}^2/pi. It is the rho^2 X term of the connection sector. The text says this term is "bounded on the replica cover and contributes no entropy but contributes to the quadratic form". Entries 037 and 036 record that the Noether charge of the composite connection b = G Theta d Theta is formed only under an auxiliary-connection reading, that the charge of the constraint term is not computed, and that no first law at order Lambda^2 is addressed.

**F.** The Zeeman field is F_ab(xi) = xi(J_ab). The mass-linear term has exponential Zeeman growth, and the vector-mass part is called "completeness of the M_str term". The window average of the full Fin(zeta) is untested.

## 1. Problem B routes

### B-R1. Lambda^2-order entropy of rho^2 X as a mediator contact term (genuine breakthrough if it closes; conditional sharpening if it only scopes)

**Known mechanism for this kind of gap.** In induced gravity the entanglement or conical entropy and the Wald/Noether entropy differ by exactly this kind of term. For a non-minimally coupled scalar, the Newton-constant renormalisation contains a term in xi that the conical entropy lacks. The difference is a Noether-charge or contact term, S_BH = S_ent - Q.
- Susskind-Uglum (hep-th/9401070, PRD 50 2700, 1994) and Larsen-Wilczek (hep-th/9506066, NPB 458, 1996) address the renormalisation of G and of the entropy.
- Kabat (hep-th/9503016, NPB 453, 1995) gives the gauge-field contact term.
- Frolov-Fursaev (hep-th/9703178, PRD 56 2212, 1997) show that the Wald entropy of Sakharov induced gravity equals S_ent minus a Noether-charge surface term for non-minimally coupled constituents. Abstract only.
- Casini-Mazzitelli-Testé (1412.6522, PRD 91 104035, 2015) review area terms and the Newton-constant renormalisation with xi. Abstract and search snippet only.
- Solodukhin (1502.03758) is the most relevant. Its abstract (read in full) extends the contact-term discussion to massive vectors, p-forms and gravitons and observes that "contact terms originate from the fields which mediate the interactions". It then proposes "a mechanism by which the Bekenstein-Hawking entropy is identified with entanglement entropy in any theory which includes both matter fields and the mediators of interactions". I read the abstract only and did not check the formulas.
- Jacobson-Satz (1212.6824, PRD 87 084047, 2013; abstract page) split the entropy into a gravitational-action part and a below-cutoff part. The second part generally includes a quantum correction to the Noether charge, and they report complications for identifying the remainder with entanglement.
- Jacobson (gr-qc/9404039) is the original statement that the same fluctuations renormalise the area term and the entanglement term.
- Blommaert-Colin-Ellerin (2405.12276, JHEP 2025; abstract) find a graviton contact term equal to d-2 times Kabat's photon term.

**Map onto NAMCG.**
- The vector sector with Zeeman/Pauli structure plays the role of the mediator.
- The gap 2 Lambda_{UV,v}^2/pi independent of N_s plays the role of the xi-type or Kabat-type surface term.
- The 036 result that endomorphism contacts carry no W coefficient was a log-order statement. The Lambda^2-order statement is the cross term of the a_1-level endomorphism with the delta content, in the 031 bookkeeping.

**Sub-lemma to attempt.**
- Hypotheses: Poisson limit, one loop, alpha = 1, totally geodesic Sigma, first order in 1-n, and the 031 delta content (Theta^12 = 1/f, Theta^34 = 1) on the two delta-rho = 0 modes.
- Result: compute the area-order (Lambda^2) cross term of E_V and E_f with E_delta, and the Dirac and vector holonomy contact. Compare the resulting area coefficient with N_tot Lambda^2/(12 pi) (the G_A side) and with the tensor side (N_tot - 24) Lambda^2/(12 pi).
- Question answered: does a contact of Solodukhin/Kabat type, together with an "S_BH = S_ent - Q" term that is the Noether charge of the rho^2 X term, reproduce 1/G_A - 1/G_T for all N_s and Lambda_{UV,v}? The test is non-vacuous because the gap is independent of N_s.
- NAMCG objects needed: E_V, E_f, a_1, the 031 delta content, the 037 dictionary E(alpha_v, alpha_f), and the normalisation paragraph.

**Risk.** The log-order result shows that the sum of contacts is an equality of vanishing coefficients (N_tot = 0 and the weighted Dynkin index). The Lambda^2 order lacks the topological protection, so a nonzero residue is possible and would be informative either way.

**Feasibility** medium. A positive match would be a real result: it would show that the entropy follows G_T once the Noether term is included, and it would remove the "G_T != G_A" obstruction at this level. A negative result is a reproducible obstruction.

### B-R2. Wald/Noether entropy for a frame-gradient Lagrangian: what Iyer-Wald requires, and the einstein-aether analogy (conditional sharpening, with a no-go constraint)

**Facts verified.**
- Wald (gr-qc/9307038) and Iyer-Wald (gr-qc/9403028, PRD 50 846, 1994) require covariance, and the fields must be Lie-dragged and regular on the bifurcation surface.
- Jacobson-Kang-Myers (gr-qc/9312023, PRD 49 6587) show that the ambiguities vanish on the bifurcation surface only for covariant Lagrangians.
- Foster (gr-qc/0509121, PRD 73 024005): for Einstein-aether theory the Iyer-Wald derivation fails because the unit vector is singular at the bifurcation surface, and no definitive entropy was found. Abstract-level content from search snippets.
- Mohd (1309.0907; abstract and search snippet only) states the Lie-dragged and regular requirement and that it fails for the aether on Killing horizons. Ding-Zhai (2001.06261, CQG 37 185015) use the solution phase-space method and find the Killing-horizon entropy exactly A/4 and a corrected term at universal horizons in 3D. Abstract and snippet only.
- Jacobson's status report (0801.1547, PoS QG-Ph 020, 2007) gives G_N = G/(1 - c_14/2) with c_14 = c_1 + c_4, and states that the entropy and first law are not identified. I read this in the ar5iv text.

**Why it matters.** Einstein-aether is the one case where a fundamental vector with first-derivative terms and a separate metric has two coefficients (G in the action vs G_N). In that case the tensor normalisation (G, spin-2 amplitude) and the Newtonian normalisation differ by c_14, and the horizon entropy is an unresolved problem rather than a given area law.

**My reasoning, not from the literature (flag for the gatekeeper).** A constant Theta that is not boost-invariant on a bifurcation surface would behave like the aether, and Iyer-Wald would fail. The delta-rho = 0 family with Theta^12 = 1/f, Theta^34 = 1 is the normal-plane binormal plus an invariant, so it is boost-invariant and Lie-dragged. This may explain why the replica class works, and it gives a stated hypothesis for B-R1.

**Sub-lemma.**
- State: for L(Theta, dTheta) with emergent G = Theta Theta^T, a Noether charge Q_xi for a Killing field xi exists, and the entropy is 2 pi times the integral of Q over the bifurcation surface, if and only if Theta is Lie-dragged and regular.
- Check: whether this class contains the replica family. Also check that Q_xi from rho^2 X has no momentum-map obstruction, in the 035 sense.
- Hypotheses: bifurcate Killing horizon, Theta Lie-dragged by xi.

**Feasibility** medium. Value: it gives the hypotheses under which "contributes no entropy" can hold, and states a no-go outside them.

### B-R3. Constraint-term charge for the composite connection in the principal-bundle framework (conditional sharpening)

**Facts verified.** Prabhu (1511.00388, CQG 34 035011, 2017; abstract and search summary) recasts tetrad theories on a principal bundle with bundle automorphisms, so a Noether charge and a perturbed-entropy formula exist for fields with internal gauge freedom. Jacobson-Mohd (1507.01054, PRD 92 124010) give the Lorentz-diffeomorphism Noether charge. Chatterjee-Ghosh (1511.01709, EPJC 78, 2018; metadata only) use the Lorentz-Lie derivative. Vollick (0710.1859, PRD 76 124001; abstract) and Faraoni's review (1005.2327; metadata) do Palatini-f(R) with an independent connection. Heisenberg-Kuhn-Walleghem (2203.13914) do coincident GR. Hammad-Dijamco-Torres-Rivas-Berube (1912.08811, PRD 100 124040) do TEGR and find entropy of GR form. Beltran Jimenez-Koivisto (2111.04716) review Noether charges in the geometrical trinity; metadata only.

**Gap in the literature.** I found no paper treating the charge of a multiplier term for a composite connection b = F[Theta], with the connection tied to the frame by a Lagrange multiplier. The Palatini result is the closest: with the independent connection on shell, the entropy in the first-order and metric formalisms agrees. Vollick finds an area law with a non-1/4 coefficient for non-conformal matter, which is also a G_A versus G_T type statement.

**Sub-lemma.**
- Hypotheses: Lagrangian L(Theta, omega, lambda) = L_0(Theta, Omega[omega]) + lambda(omega - F[Theta]); Lie-dragged Theta; bundle automorphism generated by the horizon Killing field together with the compensating internal rotation.
- Result: Q_xi = Q_diff + Q_Lorentz + Q_constraint, evaluated on the bifurcation surface. The constraint term vanishes if lambda is fixed in terms of D(dL/dOmega) and omega - F[Theta] = 0 holds on shell, apart from the terms that are not tensorial under non-diagonal rotations. State that residue.
- This closes the 037 open item (the charge of the constraint term), or turns it into a stated residue.

**Feasibility** medium to high for a computation, since the structure is quadratic. Value is modest: it removes an explicit hypothesis from 037.

### B-R4. Completed replica from modular flow, n > 1 (lower priority)
The Dirac replica is not analytic at n = 1 in the 037 ledger. Casini-Huerta-Myers and Dong-Camps-type arguments choose the replica by modular flow. I did not verify a specific paper for this point, so I give no citation. Dong (1310.5713, JHEP 1401:044) is verified and relevant for the cone and extrinsic-curvature terms.

## 2. Problem F routes

### F-R1. Spin-resolved decomposition with m^2 -> m^2 +/- 2f (conditional sharpening, may be a clean closure of the Zeeman term at the Poisson-limit constant-field order)

**Verified literature.**
- Nikishov (hep-th/0104019, JETP 93 197, 2001; abstract): W boson (g = 2) in a constant electromagnetic field. For the spin along (against) the magnetic field the Bogoliubov coefficients and the contributions to the imaginary part of the one-loop Lagrangian follow from the scalar expressions with m^2 -> m^2 + 2eH (m^2 -> m^2 - 2eH). With only an electric field the coefficients are polarisation-independent.
- Hattori-Itakura-Ozaki (2001.06131; abstract): identification of Landau levels and Zeeman energies in proper-time Heisenberg-Euler actions for scalar and spinor QED and QCD; tachyonic ground state and cancellation of longitudinal gluon and ghost.
- Bastianelli-Fecit-Miccichè (2507.15943): worldline one-loop effective Lagrangian for a constant field from a massive charged vector, with vacuum instability and pair-production rate. Abstract only.
- Reuter-Schmidt-Schubert (hep-th/9610191, Ann. Phys. 259 313, 1997): one-loop gluon loop in constant fields for spin 0, 1/2, 1; abstract only.
- Dunne's review (hep-th/0406216) for the Heisenberg-Euler background.
- Heat-kernel coefficients for Proca (Toms and Ananthanarayan 0808.2781 for non-minimal operators; metadata only for the latter) do not treat a magnetic Zeeman term.

**Map onto NAMCG.**
- The leaf has a real pair +/- a and an imaginary pair +/- ib (the Lorentzian centre flux), i.e. crossed electric-like and magnetic-like parts. The vector Zeeman operator then has spectrum lambda +/- 2i f_e-type shifts (the 032/034 "spectral vector sector" avenue).
- Take the mass-linear term to order eps^2 of the vector mass. Diagonalise the Zeeman matrix of the spin factor, giving eigenvalues of J_ab acting on the vector index. Each spin eigenvalue shifts the exponent of the scalar-type kernel by the Nikishov substitution. Expand in the mass to second order for each branch.
- Resum the per-branch mass-dependent pieces with the contour already established in the 032 block. The unbounded e^{+2sf} branch is the Nielsen-Olesen type mode, and the analytic-continuation prescription fixes its treatment.

**Sub-lemma.**
- Statement: for a constant central flux, a constant Zeeman field and mu^2 = -3, the order-eps^2 vector-mass term is a sum over spin eigenvalues s_k of g(a, b; m^2 -> m^2 + 2 s_k f), with the same i-eps contour.
- Test: compare the sum with the 034 engine at sampled points. If it matches, it supersedes the mu^2(chi_V - 4) exponential-growth term with a closed form.
- NAMCG objects: the 032 function g(a, b) = pi[b S(b/a) + i a S(a/b)], the 034 double-Duhamel engine, the supertrace weights.

**Constraints.** The unstable branch has a known imaginary part (Nielsen-Olesen; Leutwyler-type zero-mode treatments and Kondo's functional-RG claim, 1309.2337, are contested resolutions; I read only search summaries). Do not take "removal of the imaginary part" as a result. The researcher must state the continuation prescription. Zeeman growth is a feature of the physical vector and not of the leaf only.

**Feasibility** medium to high. The structure is the W-boson problem with a different spin matrix.

### F-R2. Covariant window average through the magnetic Weyl calculus (conditional sharpening)

**Facts verified.** Mantoiu-Purice (math-ph/0401043, J. Math. Phys. 45 1394, 2004; abstract): a gauge-covariant symbolic calculus defined from the magnetic canonical commutation relations, with a Moyal deformation fixed by the flux across triangles. Quadratic-operator semigroup technology: Hitrik-Pravda-Starov-Viola (1510.02072; metadata only), Pravda-Starov (0809.0186; metadata only), Hormander's general Mehler formulas (Math. Z. 219, 1995; not independently verified).

**Relation to NAMCG.** This addresses the 030/032 open item "gauge/diffeo-covariant window". The window average of the finite parts then has a covariant definition. The 034 result that Fin is finite per centre variable is the input.

**Sub-lemma.** Define the window by a magnetic-covariant symbol. Show that the average of Fin over the window is independent of the base point of the cone (frame dependence), or give the obstruction. I found no paper that does this for a Landau-type resummed heat kernel on a symplectic leaf, so the route is a method suggestion, not a known result.

**Feasibility** low to medium. If it works it removes the frame dependence of the finite remainder, but not the sign of G_eff.

### F-R3. Steinacker's recent induced-gravity literature as a consistency check (cross-check only)
- Steinacker (2110.03936, PLB 827 136946, 2022): the EH action from the one-loop action of the IKKT model with a fuzzy extra space. Abstract only.
- Steinacker (2601.08031, Jan 2026): modified gravity at large scales, extra non-Ricci-flat modes with a non-standard dispersion relation. Abstract only.
- Steinacker (2605.13294v2, May 2026): quantum fluctuations negligible at weak coupling. Abstract only.
- Steinacker (2609.08955, Sep 2026): review of the framework. Abstract only.
- Ho-Kawai-Steinacker (2509.06646, Sep 2025): diffeomorphism invariance and unitarity of the IIB matrix model through bilocal fields. Abstract only.
- Manta-Steinacker (2509.24753): fuzzy extra dimensions as a classical solution. Abstract only.

I found no paper in this list that computes the Zeeman vector-mass term or a conical entropy. NAMCG's direction (explicit B and F calculations with stated hypotheses) is not duplicated, so the field is not ahead on these two items. NAMCG should record that the 2601.08031 extra-mode dispersion statement and the 034 leaf-dependent roots are of the same family (the appH text already says so).

## 3. Ranking

1. B-R1 (Lambda^2 contact and Noether term for rho^2 X).
2. F-R1 (spin-resolved Nikishov decomposition).
3. B-R3 (constraint-term charge in the bundle framework).
4. B-R2 (Iyer-Wald hypotheses and the boost-invariance observation). Cheap, and it should be done together with B-R1 as the hypothesis section.
5. F-R2 (magnetic Weyl calculus window).
6. B-R4.
7. F-R3, cross-check only.

## 4. Concerns and constraints for the researcher
- Einstein-aether is a published warning: a fundamental vector with a separate metric makes the entropy unresolved, not automatic. State the Lie-dragging and regularity hypotheses.
- Solodukhin-type cancellation (contacts of mediators) at log order was already an equality of vanishing coefficients (031); do not present a Lambda^2 match as new unless the residue is nonzero before the contact is added.
- Spacetime stays emergent in all routes: Theta is the fundamental bivector, the metric is G = Theta Theta^T, and no fundamental metric enters. Risk: low. Watch for B-R3, where the Lagrange multiplier must not be defined with a background metric.
- Classification: the routes above give conditional results unless the researcher derives the replica holonomy and the continuation in n from the matrix state. Do not call a match closure. This is advice and not a label change.

## 5. Literature checked (verified by arXiv API record, plus abstract or ar5iv text where noted)
- Solodukhin, 1502.03758 (abstract read in full).
- Casini, Mazzitelli, Teste, 1412.6522, PRD 91 104035 (2015).
- Frolov, Fursaev, hep-th/9703178, PRD 56 2212 (1997).
- Donnelly, Wall, 1206.5831, PRD 86 064042 (2012); 1412.1895, PRL 114 111603 (2015).
- Kabat, hep-th/9503016; Susskind, Uglum, hep-th/9401070; Larsen, Wilczek, hep-th/9506066; Jacobson, gr-qc/9404039.
- Jacobson, Satz, 1212.6824 (abstract page read).
- Jacobson, Mohd, 1507.01054; Prabhu, 1511.00388; Chatterjee, Ghosh, 1511.01709.
- Wald, gr-qc/9307038; Iyer, Wald, gr-qc/9403028; Jacobson, Kang, Myers, gr-qc/9312023.
- Foster, gr-qc/0509121; Mohd, 1309.0907; Eling, Jacobson, gr-qc/0604088 (record only); Ding, Zhai, 2001.06261; Jacobson, 0801.1547 (text read for G_N and the entropy statement).
- Hammad et al., 1912.08811; Heisenberg, Kuhn, Walleghem, 2203.13914 (a search snippet gave the wrong third author; the API record says Walleghem); Beltran Jimenez, Koivisto, 2111.04716; Vollick, 0710.1859; Faraoni, 1005.2327.
- Solodukhin living review, 1104.3712; Dong, 1310.5713; Blommaert, Colin-Ellerin, 2405.12276 (abstract read).
- F: Nikishov, hep-th/0104019 (abstract read); Hattori, Itakura, Ozaki, 2001.06131 (abstract read); Bastianelli, Fecit, Miccichè, 2507.15943 (abstract read); Reuter, Schmidt, Schubert, hep-th/9610191; Dunne, hep-th/0406216; Ananthanarayan, 0808.2781; Mantoiu, Purice, math-ph/0401043; Hitrik, Pravda-Starov, Viola, 1510.02072; Pravda-Starov, 0809.0186.
- Steinacker and collaborators: 2110.03936, 2601.08031, 2605.13294, 2609.08955, 2509.06646, 2509.24753 (abstracts only).
- Not independently verified: Hormander, Math. Z. 219 (1995); Kondo, 1309.2337 (search summary only); Nielsen-Olesen 1978 and Leutwyler zero-mode papers (cited via search summaries only); Hitrik-Pravda-Starov Math. Ann. 344 (2009).
- Literature search found nothing that computes (i) the entropy of a first-derivative frame term at the Lambda^2 order with an emergent metric, (ii) a heat kernel with a Zeeman-type vector mass on a symplectic leaf, or (iii) the charge of a multiplier term for a composite connection.
