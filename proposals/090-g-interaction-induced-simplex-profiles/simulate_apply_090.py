import hashlib
# Splice rehearsal for proposal 090 r1 (v2: v1 inserted an extra CRLFCRLF before Vacuum term,
# creating a triple blank line; v2 inserts the paragraph directly before the original gap).
# READ-ONLY on the repository.
appH = r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appH-microscopic-proofs.tex"
ins = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\090-g-interaction-induced-simplex-profiles\insert-r1.tex"
d = open(appH, "rb").read()
para = open(ins, "rb").read()
assert para.endswith(b"\r\n"), "insert must end with CRLF"
para = para[:-2]
assert b"\r\n" not in para, "insert must be exactly one paragraph (no internal CRLF)"
assert b"\n" not in para
PIN = b"close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}"
checks = [
    ("size", len(d), 752790),
    ("sha256", hashlib.sha256(d).hexdigest(), "4b5213160fab6154dbefcdaaf5795501eebed9add432b910660ef2b4e62068d6"),
    ("crlf_count", d.count(b"\r\n"), 3842),
    ("pin_count", d.count(PIN), 1),
    ("vac_after_pin", d.count(PIN + b" The abstract"), 1),
]
ok = True
for name, got, want in checks:
    s = str(got) == str(want)
    ok = ok and s
    print(("PASS " if s else "FAIL ") + name + ": " + str(got))
assert ok
new = PIN[:27] + b"\r\n\r\n" + para + PIN[27:]
i = d.find(PIN)
post = d[:i] + new + d[i + len(PIN):]
assert (post[:i] == d[:i]) and (post[i + len(new):] == d[i + len(PIN):])
print("outside-window identity: True")
print("POST size:", len(post), " delta:", len(post) - len(d))
print("POST sha256:", hashlib.sha256(post).hexdigest())
print("POST crlf:", post.count(b"\r\n"), " POST lone-LF:", post.count(b"\n") - post.count(b"\r\n"))
print("089 paragraph line:", d[:i].count(b"\n") + 1, " new paragraph line:", d[:i].count(b"\n") + 1 + 2)
print("SIMULATE OK")
