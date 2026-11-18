# simulate_apply_088_r2.py -- computes POST bytes of appH from LIVE chapters bytes for
# insert-r2.tex, WITHOUT writing to chapters/. Read-only. Run: python -I simulate_apply_088_r2.py
import hashlib, sys
sys.stdout.reconfigure(errors="replace")
SRC = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/088-g-moments-stationarity-functional/insert-r2.tex"
pre = open(SRC, "rb").read()
ins = open(INS, "rb").read()          # content line + terminal CRLF
pin = b"they classify the locus over frame laws rather than selecting the profile"  # NEVER pin "Vacuum term." (2x) or short suffixes
# --- r2 PRE re-pin (live; recheck at integration time) ---
assert len(pre) == 744476, "PRE size drift: %d" % len(pre)
h = hashlib.sha256(pre).hexdigest()
assert h == "e7736a56230f80eff3c3325c519eda797d2f3b7a1a77c4f785451d51b79df75b", "PRE sha drift: " + h
assert pre.count(b"\r\n") == 3838 and pre.count(b"\n") - pre.count(b"\r\n") == 0
assert pre.count(pin) == 1, "pin not unique"
j = pre.find(b"\r\n\r\n\emph{Vacuum term.}", pre.find(pin))
assert j != -1, "gap not found"
assert pre[j:j+6] == b"\r\n\r\n\e"  # gap PIN -> next line-start is exactly CRLFCRLF
splice = j + 4
added = ins + b"\r\n"
post = pre[:splice] + added + pre[splice:]
def stats(bb):
    crlf = bb.count(b"\r\n")
    return dict(size=len(bb), sha256=hashlib.sha256(bb).hexdigest(),
                sha8=hashlib.sha256(bb).hexdigest()[:8], crlf=crlf,
                barelf=bb.count(b"\n") - crlf)
ps, qs, ins_s = stats(pre), stats(post), stats(ins)
print("PRE  size=%d sha8=%s crlf=%d barelf=%d" % (ps["size"], ps["sha8"], ps["crlf"], ps["barelf"]))
print("     sha256=%s" % ps["sha256"])
print("INS  size=%d sha8=%s crlf=%d barelf=%d" % (ins_s["size"], ins_s["sha8"], ins_s["crlf"], ins_s["barelf"]))
print("POST size=%d sha8=%s crlf=%d barelf=%d" % (qs["size"], qs["sha8"], qs["crlf"], qs["barelf"]))
print("     sha256=%s" % qs["sha256"])
# invariants
assert post.count(b"\n") - post.count(b"\r\n") == 0
idiom = b"they close nothing in Problem~G."
assert pre.count(idiom) == 14 and post.count(idiom) == 15, "close-idiom %d->%d" % (pre.count(idiom), post.count(idiom))
nvt = pre.count(b"emph{Vacuum term.}")
assert post.count(b"emph{Vacuum term.}") == nvt == 2
assert post.count(b"Variational rigidity of the frame-averaged decoupling locus") == 1
assert qs["size"] == ps["size"] + len(added)
assert pre[:splice] == post[:splice] and pre[splice:] == post[splice + len(added):]
print("INVARIANTS OK: close-idiom 14->15, new header 1, single splice, prefix/suffix identity, no bare LF, CRLF delta=%d"
      % (qs["crlf"] - ps["crlf"]))
print("NOTE: r1 POST contract (748405/a03ba415) is DEAD; the POST above is for insert-r2 bytes only")
print("SIMULATE APPLY PASS (no file was written outside the proposal folder)")
