"""050 r2: one-shot application of R1-R27 and the four bib entries, strings read raw from review-r1.md.
Nothing is written unless every check passes. Refuses to run a second time (appH_insert.r1.tex exists, or the
current insert or bib file does not have its r1 hash). Writes appH_insert.r1.tex, appH_insert.tex, new_bib_entries.bib."""
import hashlib
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
P = lambda n: os.path.join(here, n)
R1_INS = "408a9d28fff6308559036268e399c018c0eb98cf383b48171ef449012c024c7c"
R1_BIB = "328d05cd6233c9e3697dda4227038f5248320f2eed4b834a5f897a1093caa869"
R2_INS = "819f40a624e4f7a87c177253be13f23dc97d0861921230bf1835c421ec2987f9"
R2_BIB = "7f05cb9d40570ffc1f57f753476538a280cea26e2924aad3070c67e0ddebb42e"
sha = lambda b: hashlib.sha256(b).hexdigest()


def refuse(msg):
    print("REFUSED, nothing written:", msg)
    sys.exit(1)


if os.path.exists(P("appH_insert.r1.tex")):
    refuse("appH_insert.r1.tex exists, so this has already run")
ins = open(P("appH_insert.tex"), "rb").read()
bib = open(P("new_bib_entries.bib"), "rb").read()
if sha(ins) != R1_INS:
    refuse("insert is not the r1 bytes: " + sha(ins))
if sha(bib) != R1_BIB:
    refuse("bib file is not the r1 bytes: " + sha(bib))

rev = open(P("review-r1.md"), "rb").read()
print("review-r1.md bytes", len(rev), "sha256", sha(rev), "CR", rev.count(b"\r"))
text = rev.decode("utf-8").replace("\r\n", "\n")
pairs = re.findall(r"^\*\*R(\d+)\*\* old: `([^`\n]*)`\nnew: `([^`\n]*)`$", text, flags=re.M)
if [int(p[0]) for p in pairs] != list(range(1, 28)):
    refuse("expected R1..R27 in order, found " + str([p[0] for p in pairs]))

s = ins.decode("ascii")
for n, old, new in pairs:
    c0 = ins.decode("ascii").count(old)
    c = s.count(old)
    if c != 1:
        refuse(f"R{n}: old string occurs {c} times at its turn")
    s = s.replace(old, new)
    print(f"R{n}: old count in r1 bytes {c0}; at its turn {c}; length {len(old)} -> {len(new)}")
out = s.encode("ascii")
print("result bytes", len(out), "sha256", sha(out), "CR", out.count(b"\r"))
if sha(out) != R2_INS or len(out) != 18152:
    refuse("insert result differs from the expected bytes")

m = re.search(r"\*\*New bib entries\.\*\*[^\n]*\n```\n(.*?)\n```\n", text, flags=re.S)
if not m:
    refuse("bib block not found")
block = m.group(1).encode("ascii")
keys = re.findall(rb"@\w+\{([^,]*),", block)
print("bib keys read", [k.decode() for k in keys])
newbib = bib + b"\n" + block + b"\n"
print("bib result bytes", len(newbib), "sha256", sha(newbib), "CR", newbib.count(b"\r"))
if sha(newbib) != R2_BIB or len(newbib) != 2035:
    refuse("bib result differs from the expected bytes")

with open(P("appH_insert.r1.tex"), "xb") as f:
    f.write(ins)
with open(P("appH_insert.tex"), "wb") as f:
    f.write(out)
with open(P("new_bib_entries.bib"), "wb") as f:
    f.write(newbib)
print("WRITTEN: appH_insert.r1.tex (r1 bytes), appH_insert.tex (r2), new_bib_entries.bib (r2)")
