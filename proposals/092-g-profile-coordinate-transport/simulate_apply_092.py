# simulate_apply_092.py - splices insert-r1.tex into a COPY of appH held in memory only,
# asserts PRE pins and its OWN computed POST counts, prints full POST digest. Writes nothing.
# Convention (as integrated for 090/091): insert bytes + one extra CRLF before the anchor line,
# so the new paragraph is followed by a blank line. POST = PRE + len(insert) + 2 bytes.
# Run: python -I proposals/092-g-profile-coordinate-transport/simulate_apply_092.py
import hashlib
A = "chapters/appH-microscopic-proofs.tex"
P = "proposals/092-g-profile-coordinate-transport/insert-r1.tex"
app = open(A, "rb").read()
ins = open(P, "rb").read()
bad = []
def chk(name, cond):
    print(("OK  " if cond else "FAIL") + " " + name)
    if not cond:
        bad.append(name)

# PRE pins
chk("PRE size 760528", len(app) == 760528)
chk("PRE sha256", hashlib.sha256(app).hexdigest() ==
    "46dbfb3f14d444b7e7046883e00e4c58d19847ab4b9ca37bd47a3f97e691811d")
chk("PRE CRLF 3846, bareLF 0", app.count(b"\r\n") == 3846 and app.count(b"\n") == 3846)
tail = (b"the matrix integral of the core action is not evaluated, no state is fixed, the missing "
        b"steps of the Missing step paragraph are unchanged, and they close nothing in Problem~G.")
pin = tail + b"\r\n\r\n" + b"\\emph{Vacuum term.}"
i = app.find(pin)
chk("compound pin found exactly once", app.count(pin) == 1 and i >= 0)

# splice point: immediately before the second Vacuum-term header (the G-side anchor)
anchor = b"\\emph{Vacuum term.}"
j = i + len(pin) - len(anchor)
post = app[:j] + ins + b"\r\n" + app[j:]   # insert bytes + blank-line CRLF before anchor

# POST computed by this script (expectations it asserts, not a contract copy)
newsize = len(app) + len(ins) + 2
chk("POST size = PRE + insert + 2", len(post) == newsize)
chk("POST CRLF 3848, bareLF 0", post.count(b"\r\n") == 3848 and post.count(b"\n") == 3848)
chk("POST noun-idiom 18", post.count(b"close nothing in Problem~G.") == 18)
chk("POST verb-idiom 1", post.count(b"closes nothing in Problem~G.") == 1)
chk("POST Vacuum-term still 2", post.count(b"\\emph{Vacuum term.}") == 2)
chk("POST header count 1", post.count(b"Transport of the profile coordinate") == 1)
chk("POST context: 091 tail, blank, insert line, blank, Vacuum",
    post.count(tail + b"\r\n\r\n" + ins + b"\r\n" + anchor) == 1)
chk("POST byte-identical outside splice window",
    post[:j] == app[:j] and post[j + len(ins) + 2:] == app[j:])
h = hashlib.sha256(post).hexdigest()
print("POST sha256 %s" % h)
print("POST size %d B, CRLF 3848, bareLF 0, noun 18, verb 1, Vacuum 2, header 1" % newsize)
print("insert size %d B, sha8 %s" % (len(ins), hashlib.sha256(ins).hexdigest()[:8]))
print("SIMULATE 092:", "PASS" if not bad else "FAIL " + str(bad))
print("no write performed")
