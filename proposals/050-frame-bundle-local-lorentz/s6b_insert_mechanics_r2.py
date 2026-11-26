"""050 s6b (r2): mechanics of the r2 insert and bib file at byte level. Prints only."""
import hashlib
import os
import re

here = os.path.dirname(os.path.abspath(__file__))
sha = lambda b: hashlib.sha256(b).hexdigest()
raw = open(os.path.join(here, "appH_insert.tex"), "rb").read()
r1 = open(os.path.join(here, "appH_insert.r1.tex"), "rb").read()
bibb = open(os.path.join(here, "new_bib_entries.bib"), "rb").read()
print("insert bytes", len(raw), "sha256", sha(raw))
print("r1 copy bytes", len(r1), "sha256", sha(r1))
print("bib bytes", len(bibb), "sha256", sha(bibb), "CR", bibb.count(b"\r"))
print("ASCII", all(b < 128 for b in raw), "CR", raw.count(b"\r"), "BOM", raw[:3] == b"\xef\xbb\xbf", "ends with blank line", raw.endswith(b"\n\n"))
s = raw.decode("ascii")
print("paragraph blocks", len([p for p in s.split("\n\n") if p.strip()]))
print("new labels", re.findall(r"\\label\{([^}]*)\}", s))
print("status sentence count", s.count("remain open and PROGRAMME-CONDITIONAL"))
words = ["we ", "proposal", "gatekeeper", "researcher", "as proposed", "this package", "round ", "avenue", "script"]
hits = {w: [s[max(0, m.start() - 12):m.end() + 8] for m in re.finditer(re.escape(w), s, flags=re.I)] for w in words}
print("process-word scan with context", {k: v for k, v in hits.items() if v})
print("residual forms:", {t: s.count(t) for t in [r"\Phi", r"\sigma\ell", r"\eta\cdot", r"\varsigma", r"\mathsf F", r"\tilde\zeta"]})
refs = sorted(set(re.findall(r"\\(?:ref|eqref)\{([^}]*)\}", s)))
cites = sorted(set(c.strip() for g in re.findall(r"\\cite\{([^}]*)\}", s) for c in g.split(",")))
repo = here
while not os.path.isfile(os.path.join(repo, "namcg-book7.tex")):
    repo = os.path.dirname(repo)
all_tex = b"".join(open(os.path.join(repo, "chapters", f), "rb").read() for f in sorted(os.listdir(os.path.join(repo, "chapters"))) if f.endswith(".tex"))
apph = open(os.path.join(repo, "chapters", "appH-microscopic-proofs.tex"), "rb").read()
a = rb"\section{Problem E: signature}"
print("anchor + CRLF count", apph.count(a + b"\r\n"), "; anchor + bare LF count", apph.count(a + b"\n"), "; anchor count", apph.count(a))
i = apph.find(a + b"\r\n")
line = apph[:i].count(b"\n") + 1
print("anchor at line", line, "; preceding bytes", apph[max(0, i - 60):i])
for r in refs:
    print("  label", r, all_tex.count(("\\label{" + r + "}").encode()))
bib = open(os.path.join(repo, "bib", "namcg.bib"), "rb").read()
newkeys = re.findall(rb"@\w+\{([^,]*),", bibb)
print("keys in new_bib_entries.bib:", [k.decode() for k in newkeys])
for k in newkeys:
    print("  key absent from bib/namcg.bib:", k.decode(), bib.count(b"{" + k + b","))
for c in cites:
    print("  cite", c, "in namcg.bib", bib.count(("{" + c + ",").encode()), "in new file", bibb.count(("{" + c + ",").encode()))
