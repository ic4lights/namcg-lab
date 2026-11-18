import hashlib, sys
sys.stdout.reconfigure(errors="replace")
APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/087-g-derivedprofile-selection/insert-r1.tex"
d = open(APP, "rb").read()   # 'rb' only; no writes anywhere in this script
ins = open(INS, "rb").read()
def report(name, data):
    h = hashlib.sha256(data).hexdigest()
    crlf = data.count(b"\r\n")
    bare = data.replace(b"\r\n", b"").count(b"\n")
    print("%s size %d sha256 %s CRLF %d bareLF %d" % (name, len(data), h, crlf, bare))
    return crlf, bare
report("PRE ", d)
assert len(d) == 739096 and \
    hashlib.sha256(d).hexdigest() == \
    "31b345ed5e957910bacd3c02ebae87edfbeb5f0effa77c98149f6eafc2a2679d"
crlf0, bare0 = (d.count(b"\r\n"), d.replace(b"\r\n", b"").count(b"\n"))
assert crlf0 == 3836 and bare0 == 0
PIN = (b"they do not fix the state that sets \\(W\\), \\(g\\), \\(s\\) or the "
       b"frame \\(u\\), leave the missing steps (i)-(iv) of the Missing step "
       b"paragraph unchanged, and they close nothing in Problem~G.")
assert d.count(PIN) == 1
SHORT = b"do not fix the state that sets"
assert d.count(SHORT) == 6
V2 = b"sets \\(W\\) and \\(g\\),"
assert d.count(V2) == 4
VT = b"\\emph{Vacuum term.}"
assert d.count(VT) == 2
CLOSE = b"they close nothing in Problem~G."
assert d.count(CLOSE) == 13
i = d.find(PIN) + len(PIN)
assert d[i:i + 4] == b"\r\n\r\n" and d[i + 4:i + 4 + len(VT)] == VT
post = d[:i] + ins + d[i:]
report("POST", post)
print("POST size %d = PRE %d + insert %d" % (len(post), len(d), len(ins)))
print("POST close-idiom count %d (was 13, +1)"
      % post.count(CLOSE))
print("POST header count %d"
      % post.count(b"Measure dependence of the frame-averaged decoupling locus"))
print("POST Vacuum-term count %d (unchanged)" % post.count(VT))
print("no write performed")
