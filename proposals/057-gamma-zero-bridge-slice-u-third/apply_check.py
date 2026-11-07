# Proposal 057 r1, script 3 (report mode only): anchor and insert arithmetic for
# chapters/appH-microscopic-proofs.tex. Writes NOTHING outside this folder.
# Byte patterns are built with chr(92) to dodge heredoc backslash corruption.
import hashlib
BS = chr(92).encode()          # single backslash byte
CRLF = bytes([13, 10])
APPH = r"C:/Users/redgi/Projects/namcg-lab@gpu/chapters/appH-microscopic-proofs.tex"
INS = "appH_insert.tex"
anchor = CRLF * 4 + BS + b"paragraph{Status.}" + CRLF + b"Remains Assumption~" + BS + b"ref{ass:lorentzian}."
decoy = b"Remains Assumption~" + BS + b"ref{ass:EFT-a2}."
src = open(APPH, "rb").read()
ins_lf = open(INS, "rb").read()
ins_crlf = ins_lf.replace(CRLF, b"\n").replace(b"\n", CRLF)
sha = lambda b: hashlib.sha256(b).hexdigest()
print("appH size", len(src), "sha256", sha(src))
print("appH CRLF count", src.count(CRLF), "bare LF count", src.count(b"\n") - src.count(CRLF))
n = src.count(anchor)
print("anchor count (must be 1):", n)
assert n == 1, n
print("anchor offset:", src.find(anchor))
print("decoy count (must stay untouched):", src.count(decoy))
print("insert LF size", len(ins_lf), "sha256", sha(ins_lf))
print("insert CRLF size", len(ins_crlf), "sha256", sha(ins_crlf))
nonascii = sum(1 for c in ins_lf if c > 127)
print("insert non-ASCII bytes:", nonascii)
print("insert dollar-sign count:", ins_lf.count(b"$"))
refc = ins_lf.count(BS + b"ref") + ins_lf.count(BS + b"cite") + ins_lf.count(BS + b"label")
print("insert ref/cite/label count:", refc)
s = ins_lf.count(b"Problem~E remains open and PROGRAMME-CONDITIONAL.")
print("insert status sentences:", s)
assert s == 1
assert nonascii == 0
assert ins_lf.count(b"$") == 0
new = src.replace(anchor, CRLF * 2 + ins_crlf + anchor, 1)
print("post-apply size", len(new), "delta", len(new) - len(src), "sha256", sha(new))
print("post-apply CRLF count", new.count(CRLF), "bare LF count", new.count(b"\n") - new.count(CRLF))
print("post-apply anchor count", new.count(anchor))
print("DONE")
