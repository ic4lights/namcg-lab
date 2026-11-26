import re, shutil
d = r"C:\Users\redgi\Projects\namcg-lab\proposals\039-lorentz-locking-noether"
src = d + r"\appH_insert.tex"
shutil.copyfile(src, d + r"\appH_insert_r1.tex")
s = open(src, encoding="utf-8", newline="").read()
subs = [
 ("F5", r"\(V_\mu=\partial_\mu\ln\rho\), \(\mathcal T=",
        r"\(V_\mu=G^{\lambda\nu}T_{\lambda\mu\nu}\), equal to \(\partial_\mu\ln\rho\) on the Poisson class, \(\mathcal T="),
 ("F2", r"then shows that the whole non-invariance of \(\kappa_X\rho^2X\) is the axial term \(\tfrac32\kappa_X\rho^2S^2\); on generic",
        r"then shows that, with \(V_\mu V^\mu\) replaced by its class value \(\lvert\partial\ln\rho\rvert^2\), the non-invariance of \(\kappa_X\rho^2X\) is the axial term \(\tfrac32\kappa_X\rho^2S^2\) (the difference \(2(V_\mu V^\mu-\lvert\partial\ln\rho\rvert^2)\) vanishes on the class but is not invariant); on generic"),
 ("F4", r"\emph{Dressed density.} Let \(e\to\Lambda e\) with the Stueckelberg field of Equation~\eqref{eq:dressed-omega}; rotations are then a symmetry of the dressed density, and \(\Lambda\) is fixed by its own stationarity.",
        r"\emph{Dressed density.} Let the Stueckelberg field \(\Lambda\) of Equation~\eqref{eq:dressed-omega} act on the coframe, \(e\to\Lambda e\), with the density \(\kappa_X\rho^2X[\Lambda e]\); this is an input of Assumption~\ref{ass:local-lorentz} and is not derived. The density is then invariant under \(e\to\Lambda'e\), \(\Lambda\to\Lambda\Lambda'^{-1}\) of the pair, and \(\Lambda\) is treated as a field fixed by its own stationarity at the \(\Theta\)-built frame \(e\). In the unitary gauge \(\Lambda=\mathbb I\) with \(e\) that frame the density is the undressed one and \(r\) stays undetermined, as in the preceding paragraph."),
 ("F6", r"The Hessian over the six rotation amplitudes", r"The Hessian over the twelve real rotation amplitudes"),
 ("F3", r"On the stationary set the density depends on \(e\) only through \(G\) and \(\rho\), and",
        r"At the stationary points above, where \(S=0\) and \(V_\mu=\partial_\mu\ln\rho\), the density depends on \(e\) only through \(G\) and \(\rho\), and"),
 ("F1", r"half of the value \(4-n_D\) before the dressing;",
        r"smaller by \(2\kappa_X\) than the value \(4-n_D\) before the dressing, that is half of it at \(n_D=0\) and unchanged at \(n_D=2\);"),
]
for name, old, new in subs:
    print(name, "occurrences of old:", s.count(old))
    assert s.count(old) == 1
    s = s.replace(old, new)
open(src, "w", encoding="utf-8", newline="").write(s)
b = s.encode("utf-8")
print("bytes", len(b), "TAB", b.count(b"\t"), "CR", b.count(b"\r"),
      "bad", sum(1 for c in b if c > 126 or (c < 32 and c != 10)))
print("braces", s.count("{") - s.count("}"), "\\(", s.count("\\("), "\\)", s.count("\\)"))
print("refs", re.findall(r"\\(?:ref|eqref)\{([^}]*)\}", s))
