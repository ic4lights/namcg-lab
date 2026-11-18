import hashlib, sys
sys.stdout.reconfigure(errors="replace")
# Corrected splice for 087. The shipped simulate_apply_087.py splices the
# insert immediately AFTER the 085 closer pin, i.e. BEFORE the CRLFCRLF gap:
# the new block then shares physical line L3185 with the 085 paragraph and
# renders INSIDE that LaTeX paragraph (no blank line before it). Every other
# chain-2 entry (081-085) is a blank-line-separated block spliced at the
# line-start of the following entry with "insert + one CRLF" (085 recipe:
# insert-r2 3,399 B + one CRLF = 3,401 added, POST CRLF +2). This script
# splices at the line-start of the G-side Vacuum term instead:
# d[:j] already ends in CRLFCRLF (085 line + blank line L3186), then
# insert (content + terminal CRLF) + one CRLF (blank line) + Vacuum line.
APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/087-g-derivedprofile-selection/insert-r1.tex"
d = open(APP, "rb").read()   # 'rb' only; no writes anywhere in this script
ins = open(INS, "rb").read()
CRLF = bytes([13, 10])
GAP = CRLF + CRLF
def report(name, data):
    h = hashlib.sha256(data).hexdigest()
    crlf = data.count(CRLF)
    bare = data.replace(CRLF, b"").count(bytes([10]))
    print("%s size %d sha256 %s CRLF %d bareLF %d" % (name, len(data), h, crlf, bare))
    return crlf, bare
report("PRE ", d)
assert len(d) == 739096 and \
    hashlib.sha256(d).hexdigest() == \
    "31b345ed5e957910bacd3c02ebae87edfbeb5f0effa77c98149f6eafc2a2679d"
crlf0, bare0 = (d.count(CRLF), d.replace(CRLF, b"").count(bytes([10])))
assert crlf0 == 3836 and bare0 == 0
PIN = (b"they do not fix the state that sets \\(W\\), \\(g\\), \\(s\\) or the "
       b"frame \\(u\\), leave the missing steps (i)-(iv) of the Missing step "
       b"paragraph unchanged, and they close nothing in Problem~G.")
assert d.count(PIN) == 1
assert d.count(b"do not fix the state that sets") == 6
assert d.count(b"sets \\(W\\) and \\(g\\),") == 4
VT = b"\\emph{Vacuum term.}"
assert d.count(VT) == 2
CLOSE = b"they close nothing in Problem~G."
assert d.count(CLOSE) == 13
i = d.find(PIN) + len(PIN)
assert d[i:i + 4] == GAP               # 085 line + blank line L3186
j = d.find(VT, i)                       # line-start of the G-side Vacuum term
assert j == i + 4                       # next VT after the pin is the G-side one
assert ins[0:6] == b"\\emph{" and ins[-2:] == CRLF and ins.count(CRLF) == 1
post = d[:j] + ins + CRLF + d[j:]
report("POST", post)
print("POST size %d = PRE %d + insert %d + 1 CRLF" % (len(post), len(d), len(ins)))
print("POST close-idiom count %d (was 13, +1)" % post.count(CLOSE))
print("POST header count %d"
      % post.count(b"Measure dependence of the frame-averaged decoupling locus"))
print("POST Vacuum-term count %d (unchanged)" % post.count(VT))
a = post[i:i + 4]
print("PIN->next 4 bytes %r (expect CRLFCRLF: 085 paragraph separation kept)" % a)
k = post.find(b"\emph{Measure dependence")
print("before-header 4 bytes %r (expect CRLFCRLF)" % post[k - 4:k])
m = k + 5280
print("after-insert 6 bytes %r (expect CRLFCRLF then Vacuum)" % post[m:m + 6])
print("no write performed")
