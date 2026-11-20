# hygiene_093.py -- proposal 093, round 1. Run from repo root:
#   python -I proposals/093-g-orbit-rigidity-vandermonde-walls/hygiene_093.py
import glob, hashlib, re, sys

P = "proposals/093-g-orbit-rigidity-vandermonde-walls/insert-r1.tex"
raw = open(P, "rb").read()
fails = []

def chk(name, cond):
    print("%-46s %s" % (name, "PASS" if cond else "FAIL"))
    if not cond:
        fails.append(name)

content = raw[:-2] if raw.endswith(b"\r\n") else raw
chk("ends with exactly one terminal CRLF", raw.endswith(b"\r\n") and raw.count(b"\n") == 1)
chk("no bare LF inside content", b"\n" not in content and b"\r" not in content)
chk("pure printable ASCII in content", all(0x20 <= b <= 0x7E for b in content))
chk("size <= 5120 bytes", len(raw) <= 5120)
low = [b for b in content if b < 0x20]
chk("no control bytes in content", not low)
chk("exactly one \\emph{", raw.count(b"\\emph{") == 1)
banned = ["status", "priority", "completion", "open", "critical", "programme", "derived"]
hits = {w: len(re.findall(w, content.decode("ascii"), re.I)) for w in banned}
chk("no banned vocab %s" % sorted(k for k, v in hits.items() if v), not any(hits.values()))
for tok in [b"$", b"[", b"]", b"\\cite", b"\\ref{", b"\\eqref", b"\\label", b"%", b"&", b"#", b"\t"]:
    chk("absent token %r" % tok, tok not in raw)
chk("balanced braces", content.count(b"{") == content.count(b"}"))
chk("header phrase once in insert", raw.count(b"Quantitative orbit rigidity") == 1)
chk("ends with noun close-idiom", content.endswith(b"close nothing in Problem~G."))
hdr = b"Quantitative orbit rigidity"
ext = sum(open(f, "rb").read().count(hdr) for f in glob.glob("chapters/*.tex"))
chk("header phrase absent from live chapters/ tree", ext == 0)
proc = [w for w in ["proposal", "researcher", "gatekeeper", "round", "insert", "integration"]
        if re.search(w, content.decode("ascii"), re.I)]
chk("no process vocabulary", not proc)
print("insert bytes:", len(raw), "sha256:", hashlib.sha256(raw).hexdigest())
print("HYGIENE OVERALL:", "PASS" if not fails else "FAIL %s" % fails)
sys.exit(0 if not fails else 1)
