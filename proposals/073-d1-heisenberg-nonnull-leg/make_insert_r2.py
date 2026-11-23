"""Writes appH_insert_r2.tex (UTF-8, no BOM, CRLF) from the text below.  Run: python -I -B make_insert_r2.py
Round 2 relative to round 1: gatekeeper snippets S1-S3 and F4 applied; F6: delta_0 defined, tilt (s, c) renamed
(sin phi, cos phi) (sampled tilts phi = 0 and phi = arcsin 3/5, where the scripts take cos phi >= 0), class shift Lambda renamed varpi (Lambda is the gauge parameter of the class paragraph).
N1: the kernel sentence is narrowed at the tilted point to the oscillator levels <= 5 that S7(a) tests.
The script checks that no r1 symbol survives in the block."""
from pathlib import Path

TEXT = r"""\paragraph{First-order equivariant class on the Heisenberg background: connections with legs off the null direction (conditional; not closure).}
Keep time times the Heisenberg group with the normalisation and the fluctuation of the preceding paragraph. For an angle \(\varphi\) let \(\delta_0^a=(1,0,0,0)\), \(n^a=(1,\sin\varphi,-\cos\varphi,0)\), \(\hat n^a=(0,\sin\varphi,-\cos\varphi,0)\), \(e^a=(0,\cos\varphi,\sin\varphi,0)\), \(f^a=(0,0,0,1)\) and \(k_a=-\eta_{ab}n^b\), write \(X(u,v)^{cd}=u^cv^d-u^dv^c\), and let \(B_n=X(\delta_0,-\hat n)\), \(J_n=X(e,f)\), \(N_e=X(n,e)\) and \(N_f=X(n,f)\); at \(\varphi=0\) these are \(k\), \(B\), \(N\) and \(N'\) of the preceding paragraphs and the rotation of the \(1\)-\(3\) plane. Take
\[
w_a{}^{cd}=k_a(\chi B_n+\vartheta J_n)^{cd}+P_aN_e^{cd}+Q_aN_f^{cd},\qquad P_a=\zeta k_a+\alpha e_a+(\beta+\vartheta)f_a,\quad Q_a=xk_a+\beta e_a+\gamma f_a,
\]
which is the wider family at \(\varphi=\vartheta=\alpha=\beta=\gamma=0\). For all real \(\kappa,\chi,\vartheta,\zeta,x\) the first two brackets hold when
\[
\vartheta^2-2\vartheta\beta-2\beta^2-\alpha^2-\gamma^2+2\chi(\alpha+\gamma)=0
\]
and, if \(\sin\varphi\neq0\), \(\tau:=\chi+\alpha+\gamma=0\); at \(\sin\varphi\neq0\) and generic \(\tau\neq0\) the constraint alone does not suffice. Then \(\mathsf T_{ac}{}^c=\tau k_a\), the third bracket holds, \(\mathsf R_{abcd}\mathsf R^{abcd}=4\kappa^2\cos^2\varphi\,(\vartheta^2-\chi^2)\), which is positive for \(\cos\varphi\neq0\) and \(|\vartheta|>|\chi|\), and every \(w_a\) fixes the null line of \(n\) (exact for symbolic parameters; for the operators on the bundle at a rational Lorentz \(u\), order-zero part included, exact at one point with \(\varphi=0\), \(\tau\neq0\) and one with \(\varphi=\arcsin\tfrac35\)). The form \(\eta^{ab}w_a{}^{cd}w_b{}^{ef}\) is nonzero when one of \(\alpha\), \(\beta\), \(\beta+\vartheta\), \(\gamma\) is, but on vectors \(\eta^{ab}w_aw_b=-\eta^{ab}(P_aP_b+Q_aQ_b)\,n\otimes n^\flat\), whose square is zero (exact). Of the __NCLEAN__ solutions of the survey of the preceding paragraph that converge to residual \(10^{-13}\), __NSTRICT__ pass the tests for this form at tolerances \(10^{-10}\) to \(10^{-9}\), __NLOOSE__ more at \(10^{-8}\) to \(10^{-6}\), and __NOUT__ do not; for all of them \((\eta^{ab}w_aw_b)^2\) vanishes on vectors to \(2\cdot10^{-11}\) (numerical, not a classification).

On this family \(\mathcal Q_b[A]=\mathcal Q_b[A]|_{w=0}-\tau\,k^a\mathsf F_{ab}[A]\) for all \(A\) (exact), so at \(\varphi=0\) the order-zero operator is that of the preceding paragraph with \(\chi\) replaced by \(\tau\), and at \(\sin\varphi\neq0\) it is the operator of the paragraph on left-invariant backgrounds with torsion. For the forty equations, in the sectors \(p=0\), where \(E_1\) and \(E_3\) commute, every characteristic root lies on a cone \((q+\varpi k)^2=0\), and in the Landau sectors every root satisfies
\[
(q_\parallel+\varpi k_\parallel)^2+\kappa p\,l=0,\quad\text{that is}\quad q_0^2-p^2+2\varpi(q_0-p\cos\varphi)+\varpi^2\sin^2\varphi=\kappa p\,l,\qquad k_\parallel=(1,0,\cos\varphi,0),\ l\in\{-1,1,3,\dots\},
\]
with \(\varpi\) in the set
\[
\bigl\{\tfrac{\mathrm i}2\tau,\ \mathrm i(\tfrac\tau2+\chi),\ \mathrm i(\tfrac\tau2+\chi)\pm\vartheta,\ \mathrm i(\tau-\tfrac32\chi)\pm\rho\bigr\},\qquad\rho^2=\tfrac32\vartheta^2-\chi^2+\tfrac14(\tau-3\chi)^2,
\]
whose members carry \(10\), \(2\), \(2\), \(2\), \(2\) and \(2\) of the twenty quadratic factors at \(l\ge3\), and half of these at \(l=\pm1\) (at \(\varphi=0\) and \(l\le5\); at \(\varphi=\arcsin\tfrac35\) only the presence of the predicted roots with \(l\le3\) is checked). So \(\zeta\), \(x\), \(\alpha\), \(\beta\) and \(\gamma\) enter only through \(\tau\) and the constraint, and the levels \(\kappa p\,l\) are not shifted. At \(\varphi=0\), \(\chi=\tfrac14\), \(\vartheta=\tfrac12\), \(\alpha=\gamma=\tfrac34\), \(\beta=-\tfrac14\), where the rotation of the \(1\)-\(3\) plane combined with the oscillator level is conserved, this is exact in rational arithmetic after rational reconstruction, in the sector \(p=0\) at a sampled \(q\), also with \(\zeta,x\neq0\), and in the blocks that on the observed pattern contain all factors with \(l\le5\), at \((\kappa,p)=(1,\tfrac12)\) and \((2,\tfrac14)\). Otherwise it is numerical at sampled points: at \(\varphi=0\) for \(l\le5\) as in the preceding paragraph, and at \(\varphi=\arcsin\tfrac35\), where the solutions are not polynomials times the Landau Gaussian, for the eigenvalues of truncations to \(18\) and \(24\) oscillator levels that agree, all of which are assigned. The kernel at generic \(q_0\) is the ten gauge directions for each level (numerical; at \(\varphi=\arcsin\tfrac35\) among the fluctuations of oscillator level at most \(5\)).

At \(\varphi=0\) the vector \(k_\parallel=k\) is null and no term independent of the momentum enters, as for the wider family, now on backgrounds with \(\mathsf R_{abcd}\mathsf R^{abcd}>0\) and a nonzero leg form; the real parts \(\pm\vartheta\) and \(\pm\operatorname{Re}\rho\) of \(\varpi\) shift the cones along \(k\), as on the null-rotation background of the paragraph on left-invariant backgrounds with torsion, and the imaginary parts are rates. At \(\sin\varphi\neq0\) the null leg has a component along \(E_1\), on which the Landau sectors act by oscillators, \(k_\parallel^2=-\sin^2\varphi\), and the characteristic equation found above contains the momentum-independent term \(\varpi^2\sin^2\varphi\) for every class with \(\varpi\neq0\); the class \(\varpi=\tfrac{\mathrm i}2\tau=0\), which contains \(\mathcal Q\), has none. This term does not give a gap. It is the term \(-\varpi^2k_\parallel^2\) of the square \((q_\parallel+\varpi k_\parallel)^2\), fixed by the coefficient \(\varpi\) of the first-order term \(2\varpi(q_0-p\cos\varphi)\), and it vanishes with \(\sin\varphi\). Given the displayed equation, as \(p\to0\) the roots of a class tend to \(q_0=-\varpi(1\mp\cos\varphi)\), which are not real when \(\varpi\) is not real; for real \(\varpi\neq0\), as at \(\chi=0\), these two limits have the same sign, unlike the pair \(\pm m\) of a mass, and for each \(l\) one of the two roots vanishes at the unique \(p>0\) with \(p^2+(2\varpi\cos\varphi+\kappa l)p=\varpi^2\sin^2\varphi\) (by hand from the displayed equation). So no gauge-invariant gap or mass appears for the Lorentz or torsion modes on this family at this order. No norm is used, so no statement on stability is made.

These statements are for Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, linear order in the fluctuation, the Lorentzian contraction and this family on time times the Heisenberg group with constant connection, in the sectors named. The survey solutions outside the family, a norm, loops, the nonlinear evolution, the regulated trace and the domains of the unbounded operators are not treated. Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), so the assumptions listed in the paragraph on left-invariant backgrounds with curvature and torsion are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
"""

import re
here = Path(__file__).resolve().parent
t = (here / "s3_survey_structure_output.txt").read_text(encoding="utf-8")
m1 = re.search(r"residual below 1e-13 after polishing (\d+)", t)
m2 = re.search(r"\): (\d+) at tolerances 1e-10, 1e-9, 1e-9; (\d+) more at 1e-8, 1e-6, 1e-6; (\d+) not", t)
m3 = re.search(r"largest defects: .*?\|L\^2\| ([0-9.e+-]+)", t)
nclean = int(m1.group(1)); ns, nl, no = map(int, m2.groups())
assert ns + nl + no == nclean and float(m3.group(1)) < 2e-11
txt = (TEXT.replace("__NCLEAN__", str(nclean)).replace("__NSTRICT__", str(ns)).replace("__NLOOSE__", str(nl))
       .replace("__NOUT__", {1: "one", 2: "two", 3: "three"}.get(no, str(no))))
assert "__" not in txt
# r1 symbols that must not survive: the class shift \Lambda and the tilt pair (s, c) as math symbols
math = " ".join(re.findall(r"\\\((.*?)\\\)", txt, flags=re.S) + re.findall(r"\\\[(.*?)\\\]", txt, flags=re.S))
assert "\\Lambda" not in txt, "Lambda survives"
stray = re.findall(r"(?<![\\A-Za-z^_{])[sc](?![A-Za-z])", math)  # index positions ^c, _{ac} excluded
assert not stray, ("stray s/c symbols", stray)
for s in ("\\(\\delta_0^a=(1,0,0,0)\\)",
          "positive for \\(\\cos\\varphi\\neq0\\) and \\(|\\vartheta|>|\\chi|\\)",
          "This term does not give a gap.",
          "(numerical; at \\(\\varphi=\\arcsin\\tfrac35\\) among the fluctuations of oscillator level at most \\(5\\)).",
          "and half of these at \\(l=\\pm1\\) (at \\(\\varphi=0\\) and \\(l\\le5\\); at \\(\\varphi=\\arcsin\\tfrac35\\) only the presence of the predicted roots with \\(l\\le3\\) is checked).",
          "\\(k_\\parallel^2=-\\sin^2\\varphi\\), and the characteristic equation found above contains",
          "So no gauge-invariant gap or mass appears for the Lorentz or torsion modes on this family at this order. No norm is used, so no statement on stability is made."):
    assert txt.count(s) == 1, s
assert "This term is not a mass" not in txt and "so the characteristic equation contains" not in txt
data = txt.replace("\r\n", "\n").replace("\n", "\r\n").encode("utf-8")
(here / "appH_insert_r2.tex").write_bytes(data)
print("survey: clean %d, strict %d, loose %d, outside %d" % (nclean, ns, nl, no))
print("symbol checks: no \\Lambda, no stray s/c in math mode; S1, S2, S3, F4, F6 strings present once: True")
print("wrote appH_insert_r2.tex: bytes", len(data), "CRLF lines", data.count(b"\r\n"),
      "bare LF", data.count(b"\n") - data.count(b"\r\n"))
