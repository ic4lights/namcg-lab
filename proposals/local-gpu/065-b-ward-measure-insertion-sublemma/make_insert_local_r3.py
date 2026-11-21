"""065 local round 3: build insert-local-r3.tex from insert-local-r2.tex.

Every replacement is count-asserted (old string occurs exactly once), so the diff to
insert-local-r2.tex is exactly: e1 (scan-pass-2 edge-modes clause, verbatim) and
o1/o2 (scan-pass-3 optional measure wording, adopted).
Output: CRLF, UTF-8 without BOM, trailing CRLF.
Run:  python -I make_insert_local_r3.py
"""
import hashlib
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "insert-local-r2.tex")
DST = os.path.join(HERE, "insert-local-r3.tex")
SRC_SHA = "c8a2422bed86cb74a983ced0e3f64db25d9c68b578fee24a0a9c8dec8f5c312e"
CR, LF = b"\x0d", b"\x0a"

EDITS = [
    ("e1",
     r"the entanglement of the black 0-brane with its Hawking radiation in the BFSS model~\cite{ChoudhuryLaurenzano2024};",
     r"the entanglement of the black 0-brane with its Hawking radiation in the BFSS model~\cite{ChoudhuryLaurenzano2024}; "
     r"block entanglement with edge modes in matrix quantum mechanics~\cite{FlissFrenkelHartnollSoni2025,Frenkel2023EdgeModes}, applied to a compact fuzzy factor in Section~\ref{sec:status-G};"),
    ("o1",
     r"For the flat Lebesgue matrix measure of Equation~\eqref{eq:Smatrix} the Jacobian term vanishes identically;",
     r"For the flat Lebesgue measure on the matrix entries, with the action of Equation~\eqref{eq:Smatrix}, the Jacobian term vanishes identically;"),
    ("o2",
     r"the flat matrix measure of Equation~\eqref{eq:Smatrix}, Presentation~A",
     r"the flat Lebesgue measure on the matrix entries with the action of Equation~\eqref{eq:Smatrix}, Presentation~A"),
]

raw = io.open(SRC, "rb").read()
assert hashlib.sha256(raw).hexdigest() == SRC_SHA, "insert-local-r2.tex changed"
txt = raw.decode("utf-8")
for tag, old, new in EDITS:
    n = txt.count(old)
    print("%-3s occurrences of old text: %d" % (tag, n))
    assert n == 1, tag
    txt = txt.replace(old, new, 1)
out = txt.encode("utf-8")
assert out.count(LF) == out.count(CR + LF) and out.endswith(CR + LF) and not out.startswith(b"\xef\xbb\xbf")
io.open(DST, "wb").write(out)
print("insert-local-r3.tex bytes=%d sha256=%s" % (len(out), hashlib.sha256(out).hexdigest()))
