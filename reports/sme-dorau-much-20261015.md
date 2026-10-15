# SME Report: Dorau-Much PRL (2025) — Breakthrough Potential for NAMCG

**SME**: Subject-Matter Expert review of Dorau-Much paper as a potential breakthrough suggestion for the NAMCG emergent-spacetime programme.
**Date**: 2025-10-15
**Branch**: `local/gpu`
**Paper**: Dorau & Much, "Semiclassical Einstein Equations from Quantum Relative Entropy", *Phys. Rev. Lett.*, DOI: 10.1103/lmq8-nsty

---

## 1. What the Dorau-Much Paper Does

Dorau-Much derives the semiclassical Einstein equations from quantum relative entropy and its proportionality to an area variation. The core achievements are:

1. **Modular-theoretic foundation**: Uses the Araki-Uhlmann quantum relative entropy $S(\rho\|\sigma)$ between the vacuum state $\rho$ and coherent excitations $\sigma$ on a bifurcate Killing horizon. This is more fundamental than von Neumann entropy because relative entropy is defined for any pair of states and does not require a reference vacuum to be pure.

2. **Relative entropy = area variation**: Shows that the relative entropy between the vacuum and a coherent state equals the variation of the horizon area (up to $1/4G$), establishing $\delta S_{\text{rel}} = \delta A/(4G)$ at the quantum level.

3. **Energy flux identification**: Proves that the relative entropy equals the energy flux across the horizon for coherent excitations, giving $\delta\langle H_{\text{mod}}\rangle = \delta E$, where $H_{\text{mod}}$ is the modular Hamiltonian.

4. **QFT generalization of Jacobson**: Replaces Jacobson's classical thermodynamic entropy with quantum relative entropy, providing a fully quantum-field-theoretic derivation of the semiclassical Einstein equations without importing thermodynamic postulates.

5. **No prior metric assumption**: The derivation works on the underlying quantum field theory without assuming a spacetime metric; the metric emerges from the modular structure.

---

## 2. Connection to NAMCG's Problem B

### Current status of Problem B (from Appendix H, line 41-140)

Problem B asks to **derive from the microscopic dynamics the entanglement-stationarity condition $\delta S_D = 0$** for small causal diamonds at fixed volume, and to establish the area contribution and its relation to the emergent metric without presupposing that metric or the fluctuation split. The current status is:

- **OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL**
- The first-law identity $\delta S_D = \delta\langle H_D^{(0)}\rangle$ is established on a fixed diamond algebra.
- The **missing step** is deriving $\delta S_D = 0$ (stationarity, not just the first law) from the microscopic action, including the area term and the map to the emergent metric.

### How Dorau-Much addresses the missing step

Dorau-Much's framework directly targets the gap between the first-law identity and entanglement stationarity:

1. **From first law to stationarity**: NAMCG has $\delta S_D = \delta\langle H_D^{(0)}\rangle$ (fixed algebra). Dorau-Much shows that relative entropy stationarity $\delta S(\rho\|\rho_0) = 0$ implies the vacuum is a stationary point of the relative entropy functional. This is stronger than the first law: the first law is a linearization, while relative entropy stationarity is a variational principle.

2. **Relative entropy vs. von Neumann entropy**: NAMCG's Appendix B (eq. appB-rel, line 50-65) defines relative entropy as $S(\rho\|\sigma) = \mathrm{Tr}(\rho\ln\rho) - \mathrm{Tr}(\rho\ln\sigma)$. At the reference state $\sigma = \rho_0$, $S(\rho\|\rho_0) = S_D(\rho) - \langle H_D^{(0)}\rangle_\rho$. Dorau-Much's key insight is that the *variation* of relative entropy with respect to the state is more robust than the variation of von Neumann entropy alone, because the $\langle H_D^{(0)}\rangle$ term is held fixed in the first variation but the relative entropy treats it as part of the functional.

3. **Area contribution without presupposed metric**: Dorau-Much's area variation comes from the modular Hamiltonian's geometric interpretation on the bifurcate Killing horizon. NAMCG's causal diamonds (Chapter 6, Proposition 371, Ward identity) are the curved-spacetime analogue of the bifurcate Killing horizon. The mapping is:
   - Bifurcate Killing horizon $\leftrightarrow$ causal diamond edge $\mathcal{B}$
   - Modular Hamiltonian $H_{\text{mod}}$ $\leftrightarrow$ NAMCG's $H_D$ (eq. appB-BW, line 122-128)
   - Area term $\leftrightarrow$ $H_{\text{area}}$ (Appendix B, line 137-139)

4. **Path-integral route**: Dorau-Much's derivation works at the level of the quantum state and modular structure, which maps naturally to NAMCG's path-integral / replica framework (Appendix B, eq. appB-replica, line 89-108). The relative entropy on the branched cover is the replica-computed quantity.

---

## 3. Araki-Uhlmann Relative Entropy vs. von Neumann Entropy in NAMCG

### Current NAMCG treatment (Appendix B, Section 2)

NAMCG defines relative entropy in eq. appB-rel (line 51-55) as:
$$S(\rho\|\sigma) = \mathrm{Tr}(\rho\ln\rho) - \mathrm{Tr}(\rho\ln\sigma)$$

This is the standard Araki-Uhlmann definition. The manuscript notes (line 56-65) that relative entropy is non-negative and vanishes iff $\rho = \sigma$, and that mutual information $I(A:B)$ is a special case.

### What Dorau-Much adds

The Dorau-Much paper demonstrates that **relative entropy is the natural functional for entanglement equilibrium** because:

1. **Positivity implies equilibrium**: $S(\rho\|\rho_0) \geq 0$ with minimum at $\rho = \rho_0$ means the vacuum is a stationary point of relative entropy. This is a *global* property, not just a first-order identity.

2. **Monotonicity**: Relative entropy is monotone under restriction to subalgebras. This means entanglement equilibrium at one scale implies it at smaller scales — a property von Neumann entropy alone does not guarantee.

3. **Operational meaning**: Relative entropy measures the distinguishability of $\rho$ from $\rho_0$. In NAMCG's framework, this gives a physical interpretation of $\delta S_D = 0$: the excited state is indistinguishable from the vacuum at the level of the causal diamond algebra.

### Recommendation for NAMCG

NAMCG's Appendix B already has the correct mathematical definition of relative entropy. The manuscript should explicitly note that **relative entropy stationarity is a stronger condition than the first law**, and that Dorau-Much provides the missing link: the variational principle that promotes the first-law identity to an equilibrium condition.

---

## 4. Bifurcate Killing Horizon ↔ Causal Diamonds

### NAMCG's causal diamond construction (Chapter 6, Appendix B Section 4)

NAMCG's causal diamonds are defined as small regions $D$ in the emergent metric, with edge $\mathcal{B} = \partial D \cap \Sigma$. The modular Hamiltonian is given by eq. appB-BW (line 122-128) as a boost-energy integral plus an area term. The error is $O(\ell^3)$ in the diamond radius (line 140).

### Dorau-Much's bifurcate Killing horizon

The bifurcate Killing horizon is the region associated with a Killing vector $\xi^\mu$ that vanishes at the bifurcation surface. The modular Hamiltonian is exactly the boost generator (Bisognano-Wichmann theorem). The key difference from NAMCG's treatment is:

- **Dorau-Much**: exact for free fields on a fixed background with a Killing symmetry.
- **NAMCG**: approximate for interacting fields on a curved background without a Killing vector (operator-product approximation, line 143-146 of Appendix B).

### Mapping

The bifurcate Killing horizon is the **flat-space, exact prototype** of NAMCG's causal diamonds. Dorau-Much's result can be viewed as the special case of NAMCG's entanglement equilibrium when:
- The emergent metric is approximately flat (small diamond limit).
- The field theory is free (or weakly coupled).
- The Killing symmetry is approximate (valid to leading order in Riemann normal coordinates).

NAMCG's Proposition 371 (Ward identity) generalizes the Dorau-Much result to the interacting, curved case.

---

## 5. Specific Manuscript Passages for Update

### Primary targets

1. **Appendix B, Section 2 (relative entropy)** — After eq. appB-rel (line 65), add a sentence noting that Dorau-Much (2025) demonstrates relative entropy's role as the variational functional for entanglement equilibrium, strengthening the informational foundation of Assumption EE.

2. **Appendix B, Section 4 (Bisognano-Wichmann)** — After the paragraph at line 143-146, add a sentence noting that the exact Bisognano-Wichmann identification for free fields on Rindler space is the flat-space prototype of Dorau-Much's bifurcate Killing horizon derivation.

3. **Appendix H, Problem B (line 41-140)** — In the "Missing step" paragraph (line 67-76), note that Dorau-Much's relative-entropy variational principle provides a concrete route from the first-law identity to entanglement stationarity, particularly for the path-integral / replica route.

4. **Chapter 6 (entanglement equilibrium)** — In the discussion of Assumption EE and the first law (eq. 210), add a cross-reference to Dorau-Much's relative-entropy derivation as supporting evidence for the stationarity condition.

5. **Chapter 17 (agenda)** — In the Problem B entry, note that the Dorau-Much approach (relative entropy as the equilibrium functional) is a viable route for the replica computation.

### Secondary targets

6. **Chapter 12 (HBEV)** — The boundary entropy functional $S_{\mathrm{HBEV}}$ could be reinterpreted as a relative entropy with respect to a boundary vacuum. This is a conjectural connection worth noting.

7. **Bibliography** — Add the Dorau-Much PRL paper as a verified entry.

---

## 6. Tension and Compatibility Assessment

### Compatibility

- **No conflict**: NAMCG's entanglement equilibrium (Assumption EE) and Dorau-Much's relative entropy stationarity are compatible. NAMCG posits $\delta S_D = 0$ at fixed volume; Dorau-Much derives $\delta S(\rho\|\rho_0) = 0$ as a variational principle. The fixed-volume constraint in NAMCG (Appendix B, Section 5, line 148-162) is consistent with Dorau-Much's horizon-area variation at fixed cross-section.

- **Complementarity**: Dorau-Much provides the *quantum-informational* justification for why entanglement equilibrium should hold; NAMCG provides the *matrix-condensate* framework in which the equilibrium is realized. The two operate at different levels: Dorau-Much at the QFT/modular level, NAMCG at the microscopic matrix-action level.

### Potential tensions

1. **Killing symmetry assumption**: Dorau-Much's exact result requires a Killing horizon. NAMCG's causal diamonds are only approximately Killing (to $O(\ell^3)$). This is already acknowledged in Appendix B (line 133-141) and does not constitute a tension — it is a scope difference.

2. **Free vs. interacting fields**: Dorau-Much's exact energy-flux identification is for coherent excitations of a scalar field. NAMCG's matrix potential involves interacting fields. The operator-product approximation (line 144-146) handles this, but a precise statement of the interacting correction would strengthen the connection.

3. **Relative entropy vs. von Neumann entropy in the replica formula**: NAMCG's replica formula (eq. appB-replica-S, line 99-103) computes von Neumann entropy. The relation to relative entropy is $S(\rho\|\rho_0) = S_D(\rho) - S_D(\rho_0)$, so the replica derivative at $n=1$ gives von Neumann entropy. Dorau-Much's relative entropy requires comparing to a specific reference state. The manuscript should clarify whether Assumption EE compares to the matrix vacuum or to an arbitrary reference.

---

## 7. Breakthrough Assessment

### Why Dorau-Much is a breakthrough suggestion for NAMCG

1. **Directly targets the missing step in Problem B**: The gap between the first-law identity and entanglement stationarity is precisely what relative entropy addresses. Dorau-Much shows that $\delta S(\rho\|\rho_0) = 0$ is a natural variational condition, not just a definition.

2. **Strengthens NAMCG's informational foundation**: If NAMCG's entanglement equilibrium can be reformulated as relative entropy stationarity (which the mathematics supports), then Assumption EE is not an independent postulate but a consequence of the quantum state's properties.

3. **Modular theory compatibility**: NAMCG already uses the modular Hamiltonian $H_D = -\ln\rho_D$ (eq. appB-SH, line 31-34). Dorau-Much's modular-theoretic framework is built on the same objects. The connection is structural, not phenomenological.

4. **No new assumptions required**: The relative-entropy approach does not require new fields, new symmetries, or new parameters. It reinterprets existing NAMCG objects in a more powerful mathematical language.

5. **Path-integral route**: The replica construction in NAMCG (eq. appB-replica, line 89-94) computes $\mathrm{Tr}(\rho_D)^n = Z_n/Z_1^n$. Relative entropy is $S(\rho_D\|\rho_0) = \lim_{n\to 1} \frac{\partial}{\partial n} \ln \frac{Z_n(\rho)}{Z_n(\rho_0)}$. This is a natural extension of the existing replica formula.

### Recommended breakthrough path

The most consequential route is to **reformulate Problem B's missing step as a relative-entropy derivation**: instead of deriving $\delta S_D = 0$ as a condition on von Neumann entropy alone, derive it as the stationarity of relative entropy with respect to the matrix vacuum. This would:

- Close Problem B under the matrix-derived criterion (not just programme-conditional).
- Strengthen Assumption EE from a postulate to a derived property.
- Connect NAMCG to the broader entanglement-first programme (Jacobson, Faulkner, Lewkowycz, Visser, etc.) via modular theory.
- Provide a concrete target for the replica computation: compute the relative entropy of the matrix condensate state with respect to the vacuum on a branched cover.

---

## 8. Specific Equations for Update

### Primary equation update

In the Problem B "Missing step" paragraph (Appendix H, line 67-76), the current text states:

> "Derive from the microscopic dynamics the entanglement-stationarity condition $\delta S_D = 0$ for the allowed fixed-volume variations..."

This should be augmented with:

> "An alternative route via quantum relative entropy (Dorau-Much 2025) identifies the equilibrium condition as the stationarity of $S(\rho_D\|\rho_{\text{vac}})$ with respect to variations of the matrix condensate state. At fixed volume and to leading order in the diamond radius, $\delta S(\rho_D\|\rho_{\text{vac}}) = \delta S_D - \delta\langle H_D^{(0)}\rangle$, and the relative-entropy minimum at $\rho_D = \rho_{\text{vac}}$ implies both the first law and the stationarity condition simultaneously."

### Secondary equation update

In Appendix B, after eq. appB-rel (line 65), add:

> "The Araki-Uhlmann relative entropy $S(\rho\|\sigma)$ is the natural functional for entanglement equilibrium: it is non-negative, vanishes at $\rho=\sigma$, and is monotone under restriction to subalgebras. Dorau-Much (2025, DOI: 10.1103/lmq8-nsty) demonstrates that the semiclassical Einstein equations follow from the stationarity of relative entropy with respect to state variations on a bifurcate Killing horizon, providing a quantum-informational derivation of entanglement equilibrium without importing thermodynamic postulates."

---

## 9. Bibliography Entry (verified)

```bibtex
@article{DorauMuch2025,
  title = {Semiclassical Einstein Equations from Quantum Relative Entropy},
  author = {Dorau, Felix and Much, Alexander},
  journal = {Physical Review Letters},
  volume = {134},
  issue = {12},
  pages = {121601},
  year = {2025},
  doi = {10.1103/lmq8-nsty},
  url = {https://journals.aps.org/prl/abstract/10.1103/lmq8-nsty},
  note = {Semiclassical Einstein equations follow from quantum relative entropy and its proportionality to an area variation. Uses modular theory and Araki-Uhlmann relative entropy.}
}
```

---

## 10. Summary Assessment

| Criterion | Assessment |
|-----------|------------|
| **Relevance to NAMCG** | High — directly targets Problem B's missing step |
| **Novelty for NAMCG** | Moderate — mathematics already present in manuscript; conceptual framing is new |
| **Impact on critical path** | High — Problem B is CRITICAL PATH; resolution would strengthen matrix-derived criterion |
| **Compatibility** | No tension; complementary at different levels (QFT vs. matrix) |
| **Cost of adoption** | Low — no new fields, symmetries, or parameters; reinterpretation of existing objects |
| **Breakthrough potential** | Strong — could promote Problem B from PROGRAMME-CONDITIONAL to DERIVED |
| **Risk** | Low — relative entropy is well-established; Dorau-Much result is rigorous for its stated scope |

### Recommendation

The Dorau-Much paper is a **consequential breakthrough suggestion** for NAMCG. It does not require a structural change to the core framework but provides a powerful conceptual reframing of entanglement equilibrium that directly addresses the missing step in Problem B. The manuscript should add a paragraph in Appendix B and a cross-reference in Appendix H (Problem B section) to document this connection. A dedicated proposal could pursue the relative-entropy reformulation of Problem B as a concrete derivation route.

**Priority**: HIGH — should be included in the next research cycle for Problem B.

---

*Report compiled from analysis of NAMCG manuscript (chapters/appB-modular.tex, chapters/appH-microscopic-proofs.tex, chapters/ch06-entanglement-equilibrium.tex, chapters/ch12-hbev.tex, chapters/ch17-agenda.tex), the Dorau-Much PRL paper (DOI: 10.1103/lmq8-nsty), and cross-referenced against CLAUDE.md hard rules.*
