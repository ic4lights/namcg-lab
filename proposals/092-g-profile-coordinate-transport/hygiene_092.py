# hygiene_092.py - full audit of insert-r1.tex and live-appH pin sweep for item 092. Read-only.
# Run: python -I proposals/092-g-profile-coordinate-transport/hygiene_092.py
import hashlib, glob
P = "proposals/092-g-profile-coordinate-transport/insert-r1.tex"
A = "chapters/appH-microscopic-proofs.tex"
raw = open(P, "rb").read()
bad = []
def chk(name, cond):
    print(("OK  " if cond else "FAIL") + " " + name)
    if not cond:
        bad.append(name)

# --- insert structural checks
chk("single CRLF-terminated line", raw.count(b"\r\n") == 1 and raw.count(b"\n") == 1 and raw[-2:] == b"\r\n")
chk("no control bytes <0x20 before terminal CRLF", all(c >= 0x20 for c in raw[:-2]))
try:
    raw.decode("ascii"); ok = True
except UnicodeDecodeError:
    ok = False
chk("ascii-only", ok)
low = raw.decode().lower()
for w in ["status", "priority", "completion", "open", "critical", "programme", "derived"]:
    chk("no-banned '" + w + "' (substring, lowercase)", low.count(w) == 0)
chk("emph count == 1", raw.count(b"\\emph") == 1)
chk("no-$", raw.count(b"$") == 0)
chk("no square brackets", raw.count(b"[") == 0 and raw.count(b"]") == 0)
for c in [b"\\cite", b"\\ref{", b"\\eqref", b"\\label", b"\\ "]:
    chk("no-" + c.decode(), raw.count(c) == 0)
chk("math parens balanced", raw.count(b"\\(") == raw.count(b"\\)") and raw.count(b"\\(") > 0)
print("   counts: \\( = %d, \\) = %d" % (raw.count(b"\\("), raw.count(b"\\)")))
chk("close-idiom noun form once, at end", raw.count(b"close nothing in Problem~G.") == 1
    and raw.endswith(b"and they close nothing in Problem~G.\r\n"))
chk("no verb-form idiom in insert", raw.count(b"closes nothing") == 0)
hdr = b"Transport of the profile coordinate along the pushforward family and its moment coordinates.}"
chk("header present once, period-terminated", raw.count(hdr) == 1)
chk("header at start of line", raw.startswith(b"\\emph{" + hdr[:-1]))

# --- live appH PRE-state sweep
app = open(A, "rb").read()
chk("appH size 760528", len(app) == 760528)
h = hashlib.sha256(app).hexdigest()
chk("appH sha256 46dbfb3f...", h.startswith("46dbfb3f"))
print("   appH sha256 full: %s" % h)
chk("appH CRLF 3846 and no bare LF", app.count(b"\r\n") == 3846 and app.count(b"\n") == 3846)
chk("appH noun-idiom 17", app.count(b"close nothing in Problem~G.") == 17)
chk("appH verb-idiom 1", app.count(b"closes nothing in Problem~G.") == 1)
chk("appH Vacuum-term 2", app.count(b"\\emph{Vacuum term.}") == 2)
tail = (b"the matrix integral of the core action is not evaluated, no state is fixed, the missing "
        b"steps of the Missing step paragraph are unchanged, and they close nothing in Problem~G.")
pin = tail + b"\r\n\r\n" + b"\\emph{Vacuum term.}"
chk("compound splice pin count 1", app.count(pin) == 1)
chk("091 tail-pin alone count 1", app.count(tail) == 1)

# --- header uniqueness sweep across all chapters
hits = 0
for f in glob.glob("chapters/*.tex"):
    hits += open(f, "rb").read().count(b"Transport of the profile coordinate")
chk("header phrase occurs 0 times in all chapters", hits == 0)
# insert-phrase collision sweep: no insert content already in appH (would signal stale text)
for probe in [b"single transport orbit of the flat member",
              b"inverted Girard recursion",
              b"strictly decreasing from \\(1/2\\) at \\(L=1\\)",
              b"normalised diagonal of the Gram matrix"]:
    chk("probe absent from appH (novelty): " + probe[:28].decode(), app.count(probe) == 0)
    chk("probe present once in insert: " + probe[:28].decode(), raw.count(probe) == 1)

# --- referenced-anchor sanity (paragraph references must point at real text)
for probe, cnt in [(b"Pushforward weights on the profile simplex", 1),
                   (b"Charge-to-edge moment identification", 1),
                   (b"Induced coupling of the imaginary-part and slot data", 1),
                   (b"Eigenvalue reduction of the edge Gram", 1)]:
    chk("anchor exists once in appH: " + probe[:30].decode(), app.count(probe) == 1)
chk("Missing step paragraph exists", app.count(b"\\paragraph{Missing step.}") >= 1)
chk("missing-steps idiom in appH", app.count(b"missing steps (i)-(iv) of the Missing step paragraph") >= 3)

print("HYGIENE 092:", "PASS" if not bad else "FAIL " + str(bad))
