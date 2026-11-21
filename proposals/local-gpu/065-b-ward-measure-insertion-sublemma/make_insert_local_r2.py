"""065 local round 2: build insert-local-r2.tex from the gpu-accepted insert-r2.tex.

Every replacement is count-asserted (each old string must occur exactly once), so the
diff to insert-r2.tex is exactly the listed edits m1-m5 plus the survey softening (s1).
Output: insert-local-r2.tex with CRLF line endings, UTF-8 without BOM, trailing CRLF.
Run:  python -I make_insert_local_r2.py
"""
import hashlib
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "insert-r2.tex")
DST = os.path.join(HERE, "insert-local-r2.tex")
SRC_SHA = "7db417b6"  # prefix of the LF-normalised accepted text recorded in review-r2
CR, LF = b"\x0d", b"\x0a"

EDITS = [
    ("m3",
     r"for Moyal corrections, field redefinitions and the measure of the matrix integral disclaimed in the preceding paragraph it must be retained",
     r"for Moyal corrections and the measure of the matrix integral, disclaimed in the preceding paragraph, and for field redefinitions it must be retained"),
    ("m4a",
     r"The coefficient \(-4\kappa_X\) required in the paragraph on the matrix gauge realisation cannot",
     r"The coefficient \(-4\kappa_X\) required at \(n_D=0\) in the paragraph on the matrix gauge realisation cannot"),
    ("m5",
     r"which is nonzero for a generic block deformation \(B\) and vanishes only on the codimension-one hyperplane",
     r"which, for \(P\neq\tfrac12A_1\), is nonzero for a generic block deformation \(B\) and vanishes only on the codimension-one hyperplane"),
    ("m1",
     r"but no singlet-sector mechanism accounts for it~\cite{Craps2026}",
     r"but the leg-pole transformation relating the target-space tachyon to the singlet-sector collective field does not account for it~\cite{Craps2026}"),
    ("s1",
     r"None of these treats fixed-volume variations of a non-conformal block, and none supplies the missing step of Problem~B.",
     r"None of these is stated to treat fixed-volume variations of a non-conformal block or the matrix data of Equation~\eqref{eq:Smatrix}, and none supplies the missing step of Problem~B."),
    ("m2",
     r"is the Noether charge of a genuine local symmetry \(\delta u^a=f\,a^a\) of the reduced, elliptic gauge-fixed action~\cite{ArataIsmailLiberati2026}",
     r"is, in the static, spherically symmetric, asymptotically AdS sector with \(c_{14}=0\), the charge of a symmetry \(\delta u^a=f\,a^a\) of the reduced action, with \(f\) obeying an elliptic constraint~\cite{ArataIsmailLiberati2026}"),
    ("m4b",
     r"and no local symmetry of the matrix data carries the coefficient \(-4\kappa_X\);",
     r"and no local symmetry of the matrix data carries the coefficient \(-4\kappa_X\) required at \(n_D=0\) in the paragraph on the matrix gauge realisation;"),
]

raw = io.open(SRC, "rb").read().replace(CR + LF, LF)
print("src (LF-normalised) sha256:", hashlib.sha256(raw).hexdigest())
assert hashlib.sha256(raw).hexdigest().startswith(SRC_SHA), "insert-r2.tex is not the accepted gpu text"
txt = raw.decode("utf-8")
for tag, old, new in EDITS:
    n = txt.count(old)
    assert n == 1, "%s: old string occurs %d times" % (tag, n)
    txt = txt.replace(old, new, 1)
    print("%-4s applied (1 occurrence)" % tag)
txt = txt.rstrip("\n") + "\n"
out = txt.encode("utf-8").replace(LF, CR + LF)
io.open(DST, "wb").write(out)
crlf = out.count(CR + LF)
print("dst bytes=%d CRLF=%d bareLF=%d sha256=%s" % (len(out), crlf, out.count(LF) - crlf, hashlib.sha256(out).hexdigest()))
for k in ("\\label", "\\ref{", "Status:", "Priority:"):
    print("occurrences of %-9s: %d" % (k, txt.count(k)))
print("closing status sentences 'remain open and PROGRAMME-CONDITIONAL':", txt.count("remain open and PROGRAMME-CONDITIONAL"))
print("MAKE INSERT PASS")
