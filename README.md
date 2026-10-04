# namcg-lab
Official repository for Non-Abelian Matrix-Condensate Geometrogenesis (NAMCG). Includes the complete monograph PDF, Python code for Chapter 15, Appendices D &amp; F, and visualization scripts for metric emergence and Gaia DR3 deprojections.

## Reproducing Appendix D and F

Run these commands from the repository root with Python 3.12 installed. Install the project dependencies first in a virtual environment:

```bash
python -m pip install -r requirements.txt
```

Then run the scripts that produce the Appendix D and Appendix F results:

```bash
python appD-sparc-rar.py
python appF-gaia-dr3.py
```

Appendix D reads the SPARC rotation-curve files from `sparc/rotmod` and writes its summary to `sparc_namcg_vs_summary.csv`. Appendix F reads `gaia_dr3_wide_binaries.csv` and prints the Monte Carlo deprojection and model-comparison results. Keep the input data in the repository's expected locations when running the scripts.

## Licensing
* **Source Code:** Licensed under the [Apache 2.0 License](LICENSE).
* **Monograph & Documentation:** Licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

