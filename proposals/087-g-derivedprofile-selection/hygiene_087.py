import glob, re, sys
sys.stdout.reconfigure(errors="replace")
P = "proposals/087-g-derivedprofile-selection/insert-r1.tex"
d = open(P, "rb").read()
ok = True
def chk(name, cond, extra=""):
    global ok
    print("%-42s %s %s" % (name, "OK" if cond else "FAIL", extra))
    ok = ok and cond
t = d.decode("utf-8")
chk("single content line + terminal CRLF", d.endswith(b"\r\n") and
    d.replace(b"\r\n", b"").count(b"\n") == 0 and d.count(b"\r\n") == 1)
chk("no control bytes < 0x20 except terminal",
    sum(1 for b in d[:-2] if b < 0x20) == 0)
chk("no BOM, valid UTF-8", d[:3] != b"\xef\xbb\xbf")
for m in [b"$", b"[", b"]", b"\\cite", b"\\ref", b"\\eqref", b"\\label"]:
    chk("absent " + m.decode(), d.count(m) == 0)
for f in ["status", "priority", "completion", "open", "critical",
          "programme", "derived"]:
    chk("word absent: " + f, t.lower().count(f) == 0)
chk("exactly one \\emph{ header", d.count(b"\\emph{") == 1)
h = "Measure dependence of the frame-averaged decoupling locus"
hits = sum(open(f, encoding="utf-8", errors="replace").read().count(h)
           for f in glob.glob("chapters/**/*.tex", recursive=True))
chk("header unique across chapters", hits == 0)
chk("brace balance", d.count(b"{") - d.count(b"}") == 0)
chk("paren balance", d.count(b"(") - d.count(b")") == 0)
chk("ends with close idiom",
    d.endswith(b"they close nothing in Problem~G.\r\n"))
nums = sorted(set(re.findall(r"(?<![A-Za-z_])\d+", t)))
print("numerals present:", nums)
allowed = {"2", "3", "4", "5", "6", "8", "9", "10", "12", "13", "16", "24",
           "25", "30", "34", "36", "40", "45", "48", "66", "72", "109",
           "144", "160", "16", "18", "299", "323", "338", "1488", "23017",
           "1", "0"}
extra = [x for x in nums if x not in allowed]
chk("numerals within derivable allowlist", not extra, extra)
print("insert bytes", len(d), "| overall", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
