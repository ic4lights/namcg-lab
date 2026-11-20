import re, hashlib
from pathlib import Path
INS = Path("proposals/096-g-nonbridge-extension-d3/insert-r1.tex")
APPH = Path("chapters/appH-microscopic-proofs.tex")
ok = 0
def chk(tag, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + tag)
    ok += 0 if cond else 1
raw = INS.read_bytes()
chk("H0.terminal_crlf", raw.endswith(b"\r\n") and raw.count(b"\n") == 1)
body = raw[:-2]
chk("H1.no_inner_newline", b"\n" not in body and b"\r" not in body)
chk("H2.ascii", all(32 <= c < 127 for c in body))
chk("H3.no_dollar_bracket", all(t not in body for t in (b"$", b"[", b"]")))
chk("H4.no_cites", all(t not in body for t in (b"\cite", b"\ref", b"\eqref", b"\label")))
chk("H5.one_emph", body.count(b"\emph{") == 1 and body.startswith(b"\emph{"))
i = body.index(b"}")
chk("H6.header_period", body[i-1:i] == b".")
hdr = body[:i+1]
chk("H7.header_plain", body.count(b"\\", 0, i) == 1 and b"(" not in hdr)
chk("H8.banned_words", re.search(rb"(?i)\b(status|priority|completion|open|critical|programme|derived)\b", body) is None)
idiom = b"close nothing in Problem~G."
chk("H9.idiom_end", body.count(idiom) == 1 and body.endswith(idiom))
chk("H10.verb_vacuum_absent", body.count(b"closes nothing") == 0 and b"Vacuum" not in body)
chk("H11.math_balance", body.count(b"\(") == body.count(b"\)") and body.count(b"\(") > 0)
chk("H12.brace_balance", body.count(b"{") == body.count(b"}"))
apph = APPH.read_bytes()
chk("H13.apph_pre", len(apph) == 776019 and hashlib.sha256(apph).hexdigest() == "600588c1d1087232ace2cea1cdecf13fb38885cf7a2126a72eedfdc1234bfa0d")
chk("H14.idiom_counts_pre", apph.count(idiom) == 21 and apph.count(b"closes nothing") == 1 and apph.count(b"\emph{Vacuum term.}") == 2)
hits = 0
for f in sorted(Path("chapters").glob("*.tex")):
    hits += f.read_bytes().count(hdr)
chk("H15.header_unique_pre", hits == 0)
print("INSERT_SIZE %d INSERT_SHA8 %s" % (len(raw), hashlib.sha256(raw).hexdigest()[:8]))
print("SUMMARY " + ("ALL PASS" if ok == 0 else "FAILURES %d" % ok))
raise SystemExit(0 if ok == 0 else 1)
