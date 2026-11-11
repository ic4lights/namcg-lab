# simulate_apply.py -- proposal 067, round 2. READ-ONLY.
# Predicts the byte-exact post-state of chapters/appH-microscopic-proofs.tex if the
# proposal is integrated: (a) insert insert-r2.tex (two \paragraph blocks) between the
# zero-location paragraph and the caveat paragraph of the Problem N block; (b) replace the
# first sentence of the caveat paragraph. Marker-string anchored; every marker must occur
# exactly once. Writes nothing into the repository.
# Run from the repository root: python -I proposals/067-n-positivity-remainder-sublemma/simulate_apply.py
import hashlib

APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/067-n-positivity-remainder-sublemma/insert-r2.tex"

data = open(APP, "rb").read()
print("appH current size:", len(data))
print("appH current sha256:", hashlib.sha256(data).hexdigest())
crlf = data.count(b"\r\n")
print("appH CRLF:", crlf, "bare LF:", data.count(b"\n") - crlf)

insert_lf = open(INS, "rb").read()
assert b"\r" not in insert_lf, "insert file must be LF-only"
insert = insert_lf.replace(b"\n", b"\r\n")

# marker A: end of the zero-location paragraph + blank line, immediately before the
# caveat paragraph.
marker_a = (b"are a complex-conjugate pair with \\(|k^2|\\approx3.9\\LUV^2\\).\r\n"
            b"\r\nThese statements are conditional on the truncated identity, the\r\n")
assert data.count(marker_a) == 1, "marker A not unique"

# marker B: the caveat first sentence (5 source lines), to be replaced.
old_c = (b"These statements are conditional on the truncated identity, the\r\n"
         b"continuation and common limits stated, massless sectors (massive\r\n"
         b"sectors require the threshold functions of Problem~F), and the use of\r\n"
         b"the leading-logarithmic form factor up to \\(|k^2|\\sim\\LUV^2\\), where\r\n"
         b"the derivative expansion is not controlled.")
assert data.count(old_c) == 1, "marker B not unique"

new_c = (b"These statements are conditional on the truncated identity or, for\r\n"
         b"the zero-location statements, on the remainder bound of the preceding\r\n"
         b"paragraph, on the continuation and common limits stated, on massless\r\n"
         b"sectors (massive sectors require the threshold functions of Problem~F),\r\n"
         b"and on the use of the leading-logarithmic form factor up to\r\n"
         b"\\(|k^2|\\sim\\LUV^2\\), where the derivative expansion is not\r\n"
         b"controlled.")

head = (b"are a complex-conjugate pair with \\(|k^2|\\approx3.9\\LUV^2\\).\r\n\r\n")
out = data.replace(marker_a, head + insert + b"\r\n\r\n"
                   + b"These statements are conditional on the truncated identity, the\r\n", 1)
out = out.replace(old_c, new_c, 1)

print()
print("PREDICTED post-integration appH:")
print("  size:", len(out))
print("  sha256:", hashlib.sha256(out).hexdigest())
c2 = out.count(b"\r\n")
print("  CRLF:", c2, "bare LF:", out.count(b"\n") - c2)

# unchanged-region checks anchored at the edited spans
pos_a = data.index(marker_a)
print("head before insertion byte-identical:", data[:pos_a] == out[:pos_a])
b0 = data.index(old_c) + len(old_c)
b1 = out.index(new_c) + len(new_c)
print("tail after replaced caveat byte-identical:", data[b0:] == out[b1:])
print("bib unchanged: no bib keys are added by this proposal.")
print("DONE")
