# simulate_apply_088.py -- computes the POST bytes of appH from LIVE chapters bytes,
# WITHOUT writing to chapters/. Insert spliced at the start of the "\emph{Vacuum term.}"
# line, i.e. after the 087 paragraph, as one content line + blank line.
# Run: python -I simulate_apply_088.py
import hashlib, sys
sys.stdout.reconfigure(errors="replace")
SRC = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/088-g-moments-stationarity-functional/insert-r1.tex"
pre = open(SRC, "rb").read()
ins = open(INS, "rb").read()          # content line + terminal CRLF
pin = b"they classify the locus over frame laws rather than selecting the profile"
assert pre.count(pin) == 1, "pin not unique"
j = pre.find(b"\r\n\r\n\\emph{Vacuum term.}", pre.find(pin))
assert j != -1, "gap not found"
splice = j + 4                        # start of the Vacuum term line
added = ins + b"\r\n"                 # insert line, then the blank-line separator
post = pre[:splice] + added + pre[splice:]
def stats(b):
    crlf = b.count(b"\r\n")
    return dict(size=len(b), sha256=hashlib.sha256(b).hexdigest(),
                sha8=hashlib.sha256(b).hexdigest()[:8], crlf=crlf,
                barelf=b.count(b"\n") - crlf)
ps, qs, ins_s = stats(pre), stats(post), stats(ins)
print("PRE  size=%d sha8=%s crlf=%d barelf=%d" % (ps["size"], ps["sha8"], ps["crlf"], ps["barelf"]))
print("     sha256=%s" % ps["sha256"])
print("INS  size=%d sha8=%s crlf=%d barelf=%d" % (ins_s["size"], ins_s["sha8"], ins_s["crlf"], ins_s["barelf"]))
print("POST size=%d sha8=%s crlf=%d barelf=%d" % (qs["size"], qs["sha8"], qs["crlf"], qs["barelf"]))
print("     sha256=%s" % qs["sha256"])
# invariants
assert post.count(b"\n") - post.count(b"\r\n") == 0
nvt = pre.count("emph{Vacuum term.}".encode())  # twice in appH; splice pinned by 087 tail
assert post.count("emph{Vacuum term.}".encode()) == nvt == 2
assert post.count(b"Variational rigidity of the frame-averaged decoupling locus") == 1
assert qs["size"] == ps["size"] + len(added)
ctx = post[splice - 80: splice + len(added) + 60]
assert pre[:splice] == post[:splice] and pre[splice:] == post[splice + len(added):]
print("INVARIANTS OK: single splice, suffix/prefix identity, no bare LF, CRLF delta=%d"
      % (qs["crlf"] - ps["crlf"]))
print("context (escaped):", ctx[:120], "...", ctx[-90:])
print("NOTE: Vacuum term header occurs", nvt, "times in appH; splice chosen as first gap after the unique 087 pin")
print("SIMULATE APPLY PASS (no file was written outside the proposal folder)")
