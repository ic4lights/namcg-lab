"""Build appH_insert_r2.tex from appH_insert_r1.tex by the exact replacements of
review-r1 (m2, m3, m4) and the optional o1, o2.  Each old string must occur exactly
once (o2: exactly four times).  Output CRLF, UTF-8 without BOM.
Run: python -I make_insert_r2.py
"""
import hashlib
from pathlib import Path

here = Path(__file__).resolve().parent
r1 = (here / "appH_insert_r1.tex").read_bytes().decode("utf-8")
assert "\r\n" in r1
t = r1.replace("\r\n", "\n")

EL_OLD = (r"On flat space and on the null-rotation background, moreover, every constant matrix \(G\) for which \(G\) "
          r"times the forty linearised equations is formally self-adjoint vanishes on the frame equations (numerical), "
          r"so no constant recombination of these equations is the Euler--Lagrange system of a quadratic Lagrangian in "
          r"\(h\) and \(\omega\) with constant coefficients.")
EL_NEW = (r"On flat space and on the null-rotation background in the gauge with constant frame below, moreover, every "
          r"constant matrix \(G\) for which \(G\) times the forty linearised equations is formally self-adjoint vanishes "
          r"on the frame equations (numerical), so no constant recombination of these equations is the Euler--Lagrange "
          r"system of a quadratic Lagrangian in \(h\) and \(\omega\) with constant coefficients; the ten Maxwell "
          r"equations of the paragraph on the pairing of the action are in variables that contain \(y\) explicitly.")
REPL = [
    ("m2", r"The Heisenberg algebra \([E_3,E_1]=\kappa E_2\), with \(E_0\) and \(E_2\) central,",
           r"The Heisenberg algebra \([E_3,E_1]=\kappa E_2\), with \(\kappa>0\) and with \(E_0\) and \(E_2\) central,", 1),
    ("m3a", r"\omega_a{}^{12}=\kappa k_a", r"\omega_a{}^{12}=\vartheta k_a", 1),
    ("m3b", r"for \(\kappa=-\tfrac12\)", r"for \(\vartheta=-\tfrac12\)", 1),
    ("m3c", r"\((q+j\kappa k)^2=0\)", r"\((q+j\vartheta k)^2=0\)", 1),
    ("m3d", r"roots numerical at \(\kappa=\tfrac12,1,2\)", r"roots numerical at \(\vartheta=-\tfrac12,\tfrac12,1,2\)", 1),
    ("m3e", r"for \(\kappa=1\)", r"for \(\vartheta=1\)", 1),
    ("m4", EL_OLD, EL_NEW, 1),
    ("o1", r"acquire no term beyond those of a gauge field that keeps its gauge parameter, and at generic characters the kernel",
           r"obey the gauge-invariant equation \(\mathcal Q\); no term breaking \(A_b\to A_b+E_b\Lambda\) appears. At generic characters the kernel", 1),
    ("o2", r"\mathsf A", r"\mathsf L", 4),
]
for name, old, new, cnt in REPL:
    c = t.count(old)
    print(name, "occurrences", c)
    assert c == cnt, name
    t = t.replace(old, new)
# sanity: the null-rotation sentences no longer use kappa; Heisenberg ones still do
nr = t[t.index("The null-rotation algebra solves"):t.index("The Heisenberg algebra")]
print("kappa left in null-rotation sentences:", nr.count(r"\kappa"))
assert nr.count(r"\kappa") == 0 and nr.count(r"\vartheta") == 5
print("mathsf A left:", t.count(r"\mathsf A"), "; status sentences ('remain open'):", t.count("remain open"))
assert t.count(r"\mathsf A") == 0 and t.count("remain open") == 1
assert t.count("PROGRAMME-CONDITIONAL") == 1
out = t.replace("\n", "\r\n").encode("utf-8")
(here / "appH_insert_r2.tex").write_bytes(out)
print("appH_insert_r2.tex bytes", len(out), "sha256", hashlib.sha256(out).hexdigest(),
      "bare LF", out.count(b"\n") - out.count(b"\r\n"))
