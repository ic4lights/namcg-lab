# gen_insert_101.py -- regenerates insert-r1.tex byte-identically (single LaTeX paragraph line +
# terminal CRLF). Run: python -I gen_insert_101.py   then compare sha256 to manifest.md.
import hashlib
LINE = (
    "\\emph{Exact conditional diagonal law at D=3.} Let $\\lambda_{1}>\\lambda_{2}>\\lambda_{3}$, "
    "$\\textstyle\\sum_{i}\\lambda_{i}=1$, be the spectrum of $\\Lambda$ and let $d=(d_{1},d_{2},d_{3})$ "
    "be the diagonal of $U\\Lambda U^{\\dagger}$ for Haar-distributed $U\\in\\mathrm{U}(3)$. Write "
    "$\\varepsilon(w)$ for the signature of $w\\in S_{3}$ and $k(g_{1},g_{2})=\\min(g_{1},g_{1}+g_{2})$ "
    "if $g_{1}>0$ and $g_{1}+g_{2}>0$, and $k=0$ otherwise. Then the conditional density of "
    "$(d_{1},d_{2})$ given $\\Lambda$, with respect to $\\mathrm{d}d_{1}\\,\\mathrm{d}d_{2}$, is "
    "$\\widehat{\\rho}(d_{1},d_{2})=Z(\\lambda)^{-1}\\sum_{w\\in S_{3}}\\varepsilon(w)\\,k\\bigl(\\lambda_{w(1)}-d_{1},\\lambda_{w(2)}-d_{2}\\bigr)$: "
    "supported on the permutahedron $\\{d:\\lambda_{3}\\le d_{i}\\le\\lambda_{1}\\}$ and piecewise linear there. "
    "Exact rational cell-arrangement integration yields $Z=3/200$ at $\\lambda=(0.6,0.3,0.1)$ and "
    "$Z=117/4000$ at $\\lambda=(0.7,0.25,0.05)$, equal to $\\tfrac{1}{2}\\prod_{i<j}(\\lambda_{i}-\\lambda_{j})$ "
    "in both cases, and $\\mathbb{E}\,d_{i}=1/3$ and $\\mathbb{E}\,P_{2}=(1+\\sum_{i}\\lambda_{i}^{2})/4$ "
    "exactly at both spectra. Pushing $\\widehat{\\rho}$ forward by $P_{2}=\\sum_{i}d_{i}^{2}$: with "
    "$u_{i}=d_{i}-1/3$ and eigen-coordinates $a=(u_{1}+u_{2})/\\sqrt{2}$, $b=(u_{1}-u_{2})/\\sqrt{2}$ one "
    "has $P_{2}=1/3+3a^{2}+b^{2}$, and the coarea formula gives "
    "$f_{P_{2}}(P_{2})=(2\\sqrt{3})^{-1}\\int_{0}^{2\\pi}\\widehat{\\rho}\\bigl(\\tfrac{1}{3}+u_{1}(\\theta),\\tfrac{1}{3}+u_{2}(\\theta)\\bigr)\\,\\mathrm{d}\\theta$ "
    "with $u_{1}(\\theta)=(s\\cos\\theta/\\sqrt{3}+s\\sin\\theta)/\\sqrt{2}$, "
    "$u_{2}(\\theta)=(s\\cos\\theta/\\sqrt{3}-s\\sin\\theta)/\\sqrt{2}$, $s^{2}=P_{2}-1/3$; at "
    "$\\lambda=(0.6,0.3,0.1)$ this density is the constant $40\\pi/(3\\sqrt{3})$ for $1/3\le P_{2}\le 67/200$, is "
    "smooth on $(67/200,17/50)$ and $(17/50,23/50)$, and vanishes beyond $P_{2}=23/50=\\sum_{i}\\lambda_{i}^{2}$; "
    "the exact curve agrees with three-million-sample Haar histograms at $|z|\\le2$. The Laplace transform "
    "of $\\widehat{\\rho}\\,\\mathrm{d}d_{1}\\,\\mathrm{d}d_{2}$ equals the Harish--Chandra/Itzykson--Zuber "
    "integral $\\det\\bigl(e^{a_{i}\\lambda_{j}}\\bigr)_{1\\le i,j\\le3}/\\bigl(2\\,\\Delta(a)\\Delta(\\lambda)\\bigr)$ "
    "at $a=(s_{1},s_{2},0)$ to $2\\cdot 10^{-16}$: this is the type-A$_{2}$ case of the "
    "Duistermaat--Heckman--Kostant density formula, whose proof in the literature we have not "
    "independently verified. For $D>3$ the conditional density of $P_{2}$ remains unresolved even for "
    "the uniform fibre law, and under bounded profile-class reweightings of the fibre law only a "
    "bounded-Radon--Nikodym comparison of densities is available, so these exact D=3 numbers are "
    "fibre-side statements that identify no state-side profile weight and close nothing in Problem~G."
)
INS = LINE.encode("ascii") + b"\r\n"
open("insert-r1.tex", "wb").write(INS)
print("insert-r1.tex bytes:", len(INS), "sha256:", hashlib.sha256(INS).hexdigest())
