import hashlib

# READ-ONLY splice preview for item 085. Never writes to the repository.
APPH = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/085-g-moments-uniformity-locus/insert-r1.tex"

b = open(APPH, "rb").read()
ins = open(INS, "rb").read()

h = hashlib.sha256(b).hexdigest()
assert len(b) == 735695, ("PRE size", len(b))
assert h[:8] == "a13240a7", ("PRE sha8", h[:8])
assert b.count(b"\r\n") == 3834, ("PRE CRLF", b.count(b"\r\n"))
assert b.replace(b"\r\n", b"").count(b"\n") == 0, "bare LF present"
print("PRE OK: size %d sha8 %s CRLF %d bareLF 0" % (len(b), h[:8], b.count(b"\r\n")))

pin = (b"These statements tie the variance parameter of the named state class to the "
       b"profile and the frame, they do not fix the state that sets \\(W\\) and \\(g\\), "
       b"leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and "
       b"they close nothing in Problem~G.")
assert b.count(pin) == 1, ("pin count", b.count(pin))
ip = b.find(pin) + len(pin)
anchor = b"\\emph{Vacuum term.}"
assert b.count(anchor) == 2, ("anchor count", b.count(anchor))
ia = b.find(anchor, ip)
gap = b[ip:ia]
assert gap == b"\r\n\r\n", ("gap bytes", gap)
# line-start check: byte before anchor must be CR of a CRLF
assert b[ia - 2:ia] == b"\r\n", "anchor not at line start"

post = b[:ia] + ins + b"\r\n" + b[ia:]
hp = hashlib.sha256(post).hexdigest()
print("POST: size %d sha256 %s sha8 %s CRLF %d bareLF 0"
      % (len(post), hp, hp[:8], post.count(b"\r\n")))
assert len(post) == 735695 + len(ins) + 2
assert post.count(b"\r\n") == 3836, ("POST CRLF", post.count(b"\r\n"))
assert post.replace(b"\r\n", b"").count(b"\n") == 0, "POST bare LF"
idiom = b"close nothing in Problem~G."
print("close-idiom count: PRE %d -> POST %d" % (b.count(idiom), post.count(idiom)))
assert (b.count(idiom), post.count(idiom)) == (12, 13)
hdr = b"Uniformity locus of the profile, the frame and the induced coupling."
assert post.count(hdr) == 1, "new header count"
assert post.count(anchor) == 2, "POST Vacuum term count"
assert b[:ia] == post[:ia], "head unchanged"
assert post[ia + len(ins) + 2:] == b[ia:], "tail unchanged"
print("head unchanged, tail unchanged, header count 1, Vacuum term 2")
print("no write performed")
