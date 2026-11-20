# simulate_apply_099.py -- read-only simulation of the 099 insert into appH (NO WRITE).
# Insertion: POST = d[:755141] + insert-r1.tex bytes + CRLF(blank line) + d[755141:]  (before \emph{Vacuum term.})
# Run from repo root:  python -I proposals/099-g-mi-p-d-d2/simulate_apply_099.py
import hashlib
APP = "chapters/appH-microscopic-proofs.tex"
d = open(APP, "rb").read()
ins = open("proposals/099-g-mi-p-d-d2/insert-r1.tex", "rb").read()
assert len(d) == 791958 and len(ins) == 1556, "unexpected pre sizes"
POST = d[:755141] + ins + b"\r\n" + d[755141:]
s = POST.decode("utf-8")
print("PRE  bytes=%d sha256=%s" % (len(d), hashlib.sha256(d).hexdigest()))
print("POST bytes=%d sha256=%s" % (len(POST), hashlib.sha256(POST).hexdigest()))
print("POST CRLF=%d bareLF=%d" % (POST.count(b"\r\n"), POST.count(b"\n") - POST.count(b"\r\n")))
print("POST idiom(they close nothing in Problem~G.)=%d" % s.count("they close nothing in Problem~G."))
print("POST verb(closes nothing)=%d" % s.count("closes nothing"))
print("POST emph{Vacuum term.}=%d" % s.count("\\emph{Vacuum term.}"))
hdr = ins[:ins.index(b"}") + 1]
print("POST header-count=%d" % POST.count(hdr))
p098 = d.rfind(b"\\emph{Exact fibre interval")
le = d.find(b"\r\n", p098)
tail = d[le - 620:le]
print("adjacent 098tail+CRLF*2+ins = %d" % POST.count(tail + b"\r\n\r\n" + ins))
print("adjacent ins+CRLF+Vacuum    = %d" % POST.count(ins + b"\r\n\\emph{Vacuum term.}"))
print("old probe 098tail+CRLF*2+Vacuum = %d (must be 0)" % POST.count(tail + b"\r\n\r\n\\emph{Vacuum term.}"))
print("expected: POST bytes=793516 CRLF=3862 bareLF=0 idiom=25 verb=1 vac=2 hdr=1 adj1=1 adj2=1 old=0")
print("no write performed")
