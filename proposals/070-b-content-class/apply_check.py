"""070 apply check (read-only on the repository). Re-run: python proposals/070-b-content-class/apply_check.py"""
import hashlib, re, pathlib, glob
root = pathlib.Path(__file__).resolve().parents[2]
app = (root/'chapters/appH-microscopic-proofs.tex').read_bytes()
print("baseline appH:", len(app), hashlib.sha256(app).hexdigest())
anchor = (b"the Dirac sector or the measure of the matrix integral, and derive no local Lorentz symmetry. "
          b"Problems~B and~D remain open and PROGRAMME-CONDITIONAL.\r\n\r\n\\section{Problem C: conformal mode and Cassini}")
n = app.count(anchor)
print("anchor occurrences:", n)
ins = (pathlib.Path(__file__).parent/'appH_insert.tex').read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
cut = app.index(anchor) + anchor.index(b"\\section{Problem C")
new = app[:cut] + ins + app[cut:]
ok = n == 1
crlf = b"\n" not in new.replace(b"\r\n", b"")
print("CRLF only:", crlf)
ok &= crlf
txt = ins.decode('utf-8')
allsrc = "".join(pathlib.Path(p).read_text(encoding='utf-8', errors='replace') for p in glob.glob(str(root/'chapters/*.tex')))
main = "".join(pathlib.Path(p).read_text(encoding='utf-8', errors='replace')
               for p in glob.glob(str(root/'*.tex')) + glob.glob(str(root/'*.sty')))
bib = (root/'bib/namcg.bib').read_text(encoding='utf-8', errors='replace')
for lab in sorted(set(re.findall(r'\\(?:eq)?ref\{([^}]*)\}', txt))):
    c = allsrc.count('\\label{%s}' % lab)
    print("ref", lab, "labels:", c)
    ok &= c == 1
for key in sorted(set(k.strip() for g in re.findall(r'\\cite\{([^}]*)\}', txt) for k in g.split(','))):
    c = len(re.findall(r'@\w+\{%s,' % re.escape(key), bib))
    print("cite", key, "bib entries:", c)
    ok &= c == 1
print("refs in insert:", re.findall(r'\\(?:eq)?ref\{([^}]*)\}', txt), "; new labels in insert:", re.findall(r'\\label\{([^}]*)\}', txt))
luv = bool(re.search(r'\\LUV\b', main + allsrc.replace(txt, '')))
print("\\LUV used/defined elsewhere:", luv)
ok &= luv
bal = txt.count('{') - txt.count('}')
par = txt.count('\\(') - txt.count('\\)')
br = txt.count('\\[') - txt.count('\\]')
env = txt.count('\\begin{') - txt.count('\\end{')
print("brace/inline/display/env balance:", bal, par, br, env)
ok &= (bal, par, br, env) == (0, 0, 0, 0)
bad = [w for w in ("proposal", "researcher", "gatekeeper", "adversary", "as proposed", "F9", "chain") if w in txt]
print("process words:", bad)
ok &= not bad
inB = app.index(b"\\label{sec:status-B}") < cut < app.index(b"\\label{sec:status-C}")
print("insert lies in sec:status-B:", inB)
ok &= inB
print("insert adds no ledger-label line:", b"Status:" not in ins and b"Priority:" not in ins)
print("result appH:", len(new), hashlib.sha256(new).hexdigest())
print("APPLY CHECK PASS" if ok else "APPLY CHECK FAIL")
