import glob

# Round-2 hygiene audit of insert-r2.tex (mirrors the review-r1 hygiene checks).
P = "proposals/085-g-moments-uniformity-locus/insert-r2.tex"
b = open(P, "rb").read()
print("size %d" % len(b))
assert not b.startswith(b"\xef\xbb\xbf"), "BOM present"
b.decode("utf-8")
print("utf-8 decodes, no BOM")
assert b.count(b"\r\n") == 1 and b.endswith(b"\r\n"), "terminal CRLF"
rest = b[:-2]
assert b"\r" not in rest and b"\n" not in rest, "single content line"
print("single content line + terminal CRLF")
assert not [c for c in rest if c < 0x20], "control bytes in content"
print("zero control bytes below 0x20 in content")
for tok in (b"$", b"[", b"]", b"\\cite", b"\\ref", b"\\eqref", b"\\label"):
    assert b.count(tok) == 0, tok
print("counts 0: $ [ ] cite ref eqref label")
assert b.count(b"\\emph") == 1, b.count(b"\\emph")
print("\\emph count 1")
low = b.lower()
for w in (b"status", b"priority", b"completion", b"open", b"critical",
          b"programme", b"derived"):
    assert low.count(w) == 0, w
print("banned seven-word set: 0 hits (case-insensitive)")
assert b.count(b"{") == b.count(b"}"), "brace balance"
print("brace balance 0")
hdr = b"Uniformity locus of the profile, the frame and the induced coupling."
hits = {f: open(f, "rb").read().count(hdr) for f in glob.glob("chapters/*.tex")}
hits = {k: v for k, v in hits.items() if v}
print("header occurrences across chapters/: %s (files: %d touched)"
      % (hits, len(hits)))
assert not hits, "header not unique"
assert b.count(b"slot count") == 2 and b.count(b"row length") == 0
assert b.count(b"at fixed total weight \\(W\\)") == 1
print("F1/F4 edits present: 'slot count' 2, 'row length' 0, "
      "'at fixed total weight (W)' 1")
print("HYGIENE OK")
