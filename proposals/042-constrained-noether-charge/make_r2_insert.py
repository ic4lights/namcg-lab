"""Apply the six verbatim replacements of review-r1.md to appH_insert.tex (r1 saved as appH_insert_r1.tex)."""
import os, shutil
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, 'appH_insert.tex')
r1 = os.path.join(here, 'appH_insert_r1.tex')
if not os.path.exists(r1):
    shutil.copy(p, r1)
s = open(r1, encoding='utf-8').read()
reps = [
(r"The shift of the charge on \(\Sigma\) is therefore the boost charge of the shift of \(T_\eta\) on the Cauchy surface of the wedge, and the relation of~\cite{IyerWald1994} between the charge on \(\Sigma\) and the boost charge of \(T_\eta\) holds for every \(r\). In the variables \((X^a,\omega)\) the same freedom is the ambiguity",
 r"By Stokes' theorem on the Cauchy surface of the wedge, the boost charge of the shift of \(T_\eta\) equals the shift of the charge on \(\Sigma\) minus the flux of \(Q^{ab}\) at spatial infinity. For variations of \(f\) of compact support the first-order change of the charge on \(\Sigma\) is therefore the boost charge of the change of \(T_\eta\), and the relation of~\cite{IyerWald1994} between the charge on \(\Sigma\) and the boost charge of \(T_\eta\), with its term at infinity, holds for every \(r\); for constant \(f\) the improvement vanishes and the charge on \(\Sigma\) is carried by that term. In the variables \((X^a,\omega)\) this freedom corresponds to the ambiguity"),
(r"Within these hypotheses the first law does not select \(r\).",
 r"Within these hypotheses the Iyer--Wald identity for the induced density does not select \(r\); the response \(T_\eta\) to \(\gamma\) is not identified here with \(T^{\mathrm{op}}_{\mu\nu}\) of Equation~\eqref{eq:first-law}."),
(r"For \(n_D=0\) the equality \(c_A=c_T\) is the statement that the edge term that accompanies the fixed-state replica is that of \(r=-4\), that is \(-4\kappa_X\) in units of \(c\) relative to \(L_0\).",
 r"For \(n_D=0\) the fixed-state replica has \(c_A-c_T=4\kappa_X\), so the requirement \(G_A=G_T\) of the paragraph on the normalisation holds if and only if the edge term that accompanies the replica contributes the coefficient of \(r=-4\), that is \(-4\kappa_X\) in units of \(c\) relative to \(L_0\)."),
(r"A multiplier term for the constraint \(b=F[\Theta]\) depends on first derivatives of \((\gamma,\omega)\) only and has no charge on \(\Sigma\).",
 r"For the constraint \(b=F[\Theta]\), with \(F\) the covariantised composite built from the first jets of \((\gamma,\omega)\), a multiplier term depends on first derivatives of \((\gamma,\omega)\) only and has no charge on \(\Sigma\); this is the charge that the paragraphs on the comparator and on the order \(\Lambda^2\) list as not computed, and it is computed only in this setting."),
(r"and the torsion of \(e\) taken with the Levi-Civita connection of \(\gamma\).",
 r"and the torsion of \(e\) taken with the Levi-Civita connection of \(\gamma\). Densities carry the factor \(\sqrt{\lvert\gamma\rvert}\), which is \(1\) in the matrix chart, so that \(\sqrt G=\rho^2\sqrt{\lvert\gamma\rvert}\)."),
(r"They do not determine the edge term, the modular Hamiltonian, the replica or the Dirac sector,",
 r"They do not determine the edge term, the modular Hamiltonian, the replica or the Dirac sector, do not identify \(T_\eta\) with \(T^{\mathrm{op}}_{\mu\nu}\) of Equation~\eqref{eq:first-law},"),
]
for i, (a, b) in enumerate(reps, 1):
    n = s.count(a)
    print(f'replacement {i}: old occurs {n} time(s)')
    assert n == 1
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
bb = open(p, 'rb').read()
ctrl = sum(1 for c in bb if (c < 32 and c != 10) or c == 127)
print('bytes', len(bb), 'CR', bb.count(b'\r'), 'TAB', bb.count(b'\t'), 'nonASCII', sum(1 for c in bb if c > 127), 'other control', ctrl)
print('braces net', s.count('{') - s.count('}'), r'\( \) net', s.count('\\(') - s.count('\\)'), r'\[', s.count('\\['), r'\]', s.count('\\]'))
import glob, re
labs = [f for f in glob.glob(r'C:\Users\redgi\Projects\namcg-lab\chapters\*.tex') for _ in range(open(f, encoding='utf-8').read().count('\\label{eq:first-law}'))]
print('label eq:first-law definitions:', len(labs), labs)
