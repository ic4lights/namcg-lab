"""Simulate the proposal-060 insertions on the CURRENT appH bytes (read-only).

r2 rules (review-r1 F1): SINGLE-PASS splice, offsets in ascending order:
    out = src[:235613] + D_crlf + src[235613:269406] + E_crlf + src[269406:]
The D anchor (235613) precedes the E insertion (269406), so no shift is applied
(the r1 script shifted D by len(E_crlf) after inserting E: that was the bug).

Two E variants are simulated:
  (A) r1 E bytes, recovered byte-exactly from the fenced latex block of
      proposal-r1.md (asserted sha256(LF) = 0e7ca8330cfd90ec5cd2bb0c07367178ef764a9ea10252600a4f64331acac548):
      reproduces the gatekeeper's F1 check, expected sha256
      edbf723a2502125fc22243e1e9a58bbf753d29c8e49281e4a80eebf529de975f
      (560706 B, 3331 CRLF, 0 bare LF).
  (B) r2 E bytes (insert-E.tex as now stored, with the review-r1 F2 sentence):
      the true r2 post-state.
No file is modified.
"""
import hashlib
import pathlib
import re

root = pathlib.Path(r"C:\Users\redgi\Projects\namcg-lab@gpu")
src_p = root / "chapters" / "appH-microscopic-proofs.tex"
folder = pathlib.Path(r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\060-rp-n2-invariant-failure")

src = src_p.read_bytes()
tE = (folder / "insert-E.tex").read_bytes()
tD_raw = (folder / "insert-D.tex").read_bytes()
tD = tD_raw[:-1] if tD_raw.endswith(b"\n") else tD_raw

sha = lambda b: hashlib.sha256(b).hexdigest()

md1 = (folder / "proposal-r1.md").read_bytes()
fenced = re.findall(rb"```latex\r?\n(.*?)\r?\n```", md1, re.S)
assert len(fenced) == 2, "expected two fenced latex blocks in proposal-r1.md"
tE_r1 = fenced[0].replace(b"\r\n", b"\n") + b"\n"
tD_r1 = fenced[1].replace(b"\r\n", b"\n") + b"\n"
assert sha(tE_r1) == "0e7ca8330cfd90ec5cd2bb0c07367178ef764a9ea10252600a4f64331acac548", "r1 E block recovered wrong"
assert sha(tD_r1) == "7b9cadaee6e22ee8e121e6de61b1a830755ab5dc1d06c870719b9b24a6baf205", "r1 D block recovered wrong"
print("recovered r1 fenced blocks: E(LF) %d B sha %s ; D(LF) %d B sha %s"
      % (len(tE_r1), sha(tE_r1), len(tD_r1), sha(tD_r1)))

md2_p = folder / "proposal-r2.md"
if md2_p.exists():
    f2 = re.findall(rb"```latex\r?\n(.*?)\r?\n```", md2_p.read_bytes(), re.S)
    assert len(f2) == 2, "expected two fenced latex blocks in proposal-r2.md"
    okE = f2[0].replace(b"\r\n", b"\n") + b"\n" == tE
    okD = f2[1].replace(b"\r\n", b"\n") + b"\n" == tD_raw
    print("proposal-r2 fenced E == insert-E.tex:", okE)
    print("proposal-r2 fenced D == insert-D.tex:", okD)
    assert okE and okD
else:
    print("proposal-r2.md not present yet")

SENT_NEW = (b"Any unital \\(*\\)-subalgebra closed under \\(\\theta\\) on which "
            b"\\(\\langle\\cdot,\\cdot\\rangle_\\theta\\) is nonnegative contains no nonzero "
            b"\\(\\theta\\)-odd element, since such an element would have negative square, so every "
            b"\\(\\theta\\)-stable reflection-positive test algebra for these measures lies in the "
            b"\\(\\theta\\)-even invariant algebra, and every invariant mixing time and space under "
            b"\\(\\theta\\) is excluded from any reconstruction from these measures.")
assert tE.count(SENT_NEW) == 1, "corrected F2 sentence not found once in insert-E.tex"
print("corrected F2 sentence bytes:", len(SENT_NEW), "sha", sha(SENT_NEW))

for name, t in (("E(r2)", tE), ("E(r1-from-fence)", tE_r1), ("D", tD_raw)):
    assert t.count(b"\r") == 0
    print("block %s: LF bytes=%d CR=%d LF=%d sha256(LF)=%s"
          % (name, len(t), t.count(b"\r"), t.count(b"\n"), sha(t)))

tE_crlf = tE.replace(b"\n", b"\r\n")
tE1_crlf = tE_r1.replace(b"\n", b"\r\n")
tD_crlf = tD.replace(b"\n", b"\r\n")
print("block E(r2) CRLF: bytes=%d CR=%d sha256=%s" % (len(tE_crlf), tE_crlf.count(b"\r"), sha(tE_crlf)))
print("block E(r1-fence) CRLF: bytes=%d CR=%d sha256=%s" % (len(tE1_crlf), tE1_crlf.count(b"\r"), sha(tE1_crlf)))
print("block D CRLF(applied form, trailing newline stripped): bytes=%d CR=%d sha256=%s"
      % (len(tD_crlf), tD_crlf.count(b"\r"), sha(tD_crlf)))

A_E = (b"PROGRAMME-CONDITIONAL.\r\n\r\n\r\n\r\n\r\n\paragraph{Status.}\r\n"
       b"Remains Assumption~\\ref{ass:lorentzian}.")
P_E = b"PROGRAMME-CONDITIONAL.\r\n\r\n"
A_D = (b"and the diagonal elements, so Assumption~\\ref{ass:lorentzian} is not discharged.")

nE = src.count(A_E)
nD = src.count(A_D)
print("count A_E:", nE, " offset:", src.find(A_E))
print("count A_D:", nD, " offset:", src.find(A_D), " end:", src.find(A_D) + len(A_D))
assert nE == 1 and nD == 1

iinsE = src.find(A_E) + len(P_E)     # 269406
iinsD = src.find(A_D) + len(A_D)     # 235613
assert iinsD < iinsE, "D must precede E for the single-pass rule"
print("single-pass insert offsets: D at", iinsD, " E at", iinsE)
print("context E:", src[iinsE - 30:iinsE + 60])
print("context D:", src[iinsD:iinsD + 40])

def stats(out):
    assert b"\r" not in out.replace(b"\r\n", b""), "bare LF present"
    return ("bytes=%d CRLF=%d bareLF=%d sha256=%s"
            % (len(out), out.count(b"\r\n"), out.count(b"\n") - out.count(b"\r\n"), sha(out)))

outA = src[:iinsD] + tD_crlf + src[iinsD:iinsE] + tE1_crlf + src[iinsE:]
outB = src[:iinsD] + tD_crlf + src[iinsD:iinsE] + tE_crlf + src[iinsE:]

print("original: bytes", len(src), "CRLF", src.count(b"\r\n"), "sha256", sha(src))
print("(A) r1-E + F1 fix :", stats(outA))
print("(B) r2-E (F2 text):", stats(outB))
print("delta bytes r2:", len(outB) - len(src))
print("change-1-only r2 :", len(src) + len(tE_crlf))

target = "edbf723a2502125fc22243e1e9a58bbf753d29c8e49281e4a80eebf529de975f"
okA = sha(outA) == target and len(outA) == 560706 and outA.count(b"\r\n") == 3331
print("GATEKEEPER_F1_CHECK_REPRODUCED:", okA)
targetB = "fe02de8970b7dee8b0df8cad9a84ca557b1ecf41bc9d2b4984135a50b8faab8d"
okB = sha(outB) == targetB and len(outB) == 560743 and outB.count(b"\r\n") == 3326
print("R2_POST_STATE_MATCHES_DECLARATION:", okB)

for key in ("OsterwalderSchrader1973", "OsterwalderSchrader1975",
            "ChouNishimuraTripathi2025", "sec:status-D", "sec:status-E",
            "eq:Smatrix", "ass:lorentzian"):
    print("src occurrences of", key, ":", src.count(key.encode()))
print("no new \\label introduced:", tE.count(b"\\label") + tD.count(b"\\label"))
print("SIMULATION_OK")
