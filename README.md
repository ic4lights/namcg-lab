# namcg-lab

Official repository for **Non-Abelian Matrix-Condensate Geometrogenesis (NAMCG)**.

NAMCG is a research programme that attempts to derive an emergent Lorentzian metric, massless transverse-traceless spin-2 modes, and a covariantly conserved entropic stress from a microscopic matrix-valued order parameter \(\Phi^I_A\). The composite metric is defined by
$$
e^A_\mu \equiv \langle \partial_\mu \Phi^I_A \rangle, \qquad
g_{\mu\nu} = \eta_{AB}\, e^A_\mu e^B_\nu.
$$
The programme is organised as a single derivation chain; many steps remain open (see Appendix H of the monograph).

> **Read the monograph:** [NAMCG monograph (namcg-book7.pdf)](namcg-book7.pdf)

## Repository contents

- Complete monograph (PDF)
- Python laboratory for the reduced Newtonian inspiral model of Chapter 15
- Coefficient-level consistency checks for SPARC rotation curves (Appendix D) and Gaia DR3 wide binaries (Appendix I)
- Supporting visualisation scripts for metric emergence and deprojections

## Reproducing Appendix D and Appendix I

From the repository root, with Python 3.12:

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
python -m pip install -r requirements.txt

python appD-sparc-rar.py
python appI-gaia-dr3-msmm.py