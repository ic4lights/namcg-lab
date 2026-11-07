# Proposal 057 r2, script 5: apply the CORRECTED insert (patched appH_insert.tex)
# to an out-of-repo copy of chapters/appH-microscopic-proofs.tex.
# Usage: python -I apply_in_build_r2.py <path-to-appH-copy-in-tmp-build>
# Rule: src.replace(anchor, CRLF+CRLF + T_CRLF + anchor, 1). Asserts anchor count 1
# and decoy count 1 before and after. Writes ONLY the appH copy given as argv[1].
import hashlib, sys
src_path = sys.argv[1]
INS = "appH_insert.tex"
anchor = (b"\r\n") * 4 + b"\\paragraph{Status.}" + b"\r\n" + b"Remains Assumption~\\ref{ass:lorentzian}."
decoy = b"Remains Assumption~\\ref{ass:EFT-a2}."
sha = lambda b: hashlib.sha256(b).hexdigest()
src = open(src_path, "rb").read()
T = open(INS, "rb").read()
T_CRLF = T.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
assert src.count(anchor) == 1, "anchor count != 1: %d" % src.count(anchor)
assert src.count(decoy) == 1, "decoy count != 1"
out = src.replace(anchor, b"\r\n\r\n" + T_CRLF + anchor, 1)
assert out.count(anchor) == 1 and out.count(decoy) == 1
open(src_path, "wb").write(out)
print("src size", len(src), "sha256", sha(src))
print("T LF size", len(T), "sha256", sha(T))
print("T CRLF size", len(T_CRLF), "sha256", sha(T_CRLF))
print("applied size", len(out), "sha256", sha(out))
print("applied CRLF count", out.count(b"\r\n"), "bare LF count", out.count(b"\n") - out.count(b"\r\n"))
print("applied anchor count", out.count(anchor), "decoy count", out.count(decoy))
