# cert_130.py - verification certificate for proposal 130-margin-tightening.
# Typographic package: preamble emergencystretch line (A) + ch03 tabcolsep
# wrapper (B). Runs the candidate and baseline builds in a scratch mirror and
# scans the logs for Overfull \hbox boxes. Writes NOTHING outside
# scratch/margin-typo/cert/. Run from the repo root:
#     python -I proposals/130-margin-tightening/cert_130.py
# Expected invariant output (final line): CERT130 PASS ... with
# BASE14 CAND1 CH03SITE0 MAX1.215 (see journal-130.md for provenance).
#
# This source contains no backslash literals: every TeX token that needs one
# is built with chr(92), so byte-mangling by a transport layer cannot corrupt
# the patterns (the trap that sank an earlier hand-built mirror in this task).
import os, sys, shutil, hashlib, subprocess

BS = chr(92)
R = os.getcwd()
TOK = "Overfull " + BS + "hbox ("
PT_END = "pt too wide)"
A_STRETCH = (BS + "setstretch{1.12}").encode() + b"\r\n"
A_EMERGE = (BS + "setlength{" + BS + "emergencystretch}{2em}").encode() + b"\r\n"
B_BEGIN = (BS + "begin{tabular}{@{}ll@{}}").encode() + b"\r\n"
B_END = (BS + "end{tabular}").encode() + b"\r\n"
B_INS1 = ("{" + BS + "setlength{" + BS + "tabcolsep}{3pt}").encode() + b"\r\n"
B_INS2 = b"}\r\n"
S = os.path.join(R, "scratch", "margin-typo", "cert")
TRACKED = ["namcg-book7.tex", "chapters/ch03-matrix-action.tex", "namcg-book7.pdf",
           "namcg-book7.log", "namcg-book7.aux", "namcg-book7.bbl",
           "namcg-book7.toc", "namcg-book7.out"]
CHAPTERS = ["ch01-geometrogenesis", "ch02-preliminaries", "ch03-matrix-action",
    "ch04-vierbein-emergence", "ch05-lorentz-decomposition",
    "ch06-entanglement-equilibrium", "ch07-massless-tensor", "ch08-heat-kernel",
    "ch09-ultraviolet", "ch10-lorentz-locking", "ch11-conservation", "ch12-hbev",
    "ch13-cores-galaxies", "ch14-dissipation", "ch15-numerics", "ch16-falsifiers",
    "ch17-agenda", "appA-seeley-dewitt", "appB-modular", "appC-integrator",
    "appD-empirical", "appE-rar-bridge", "appF-field-equation",
    "appG-sector-entropy", "appH-microscopic-proofs", "appI-gaia-wide",
    "appJ-summary", "appK-endomorphism", "appL-coupling", "ch18-epilogue"]
fails = []

def h12(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:12]

def parse_boxes(log_text):
    # string split only (never regex on the hbox token)
    vals = []
    i = 0
    while True:
        j = log_text.find(TOK, i)
        if j < 0:
            return vals
        k = log_text.find(PT_END, j)
        if k < 0 or k - j > 40:
            fails.append("malformed overfull token at " + str(j))
            return vals
        vals.append((float(log_text[j + len(TOK):k]), j))
        i = k

def unwrap(path):
    return open(path, "r", encoding="utf-8", errors="replace").read().replace("\n", "")

def region_of(u, fname, chmark):
    # open trace of the chapter .tex is the path token just before "Chapter N."
    c = u.find(chmark)
    st = u.rfind(fname + ".tex", 0, c)
    return st

def boxes_between(u, lo, hi):
    return [v for (v, j) in parse_boxes(u) if lo <= j < hi]

def owner_of(u, j):
    best, bf = -1, "?"
    for f in CHAPTERS:
        k = u.rfind(f + ".tex", 0, j)
        if k > best:
            best, bf = k, f
    return bf

def build_mirror(name, patchA, patchB):
    M = os.path.join(S, name)
    if os.path.exists(M):
        shutil.rmtree(M)
    os.makedirs(M)
    tex = open(os.path.join(R, "namcg-book7.tex"), "rb").read()
    if patchA:
        assert tex.count(A_STRETCH) == 1, "anchor A not unique"
        tex = tex.replace(A_STRETCH, A_STRETCH + A_EMERGE)
    assert A_EMERGE not in tex or patchA
    open(os.path.join(M, "namcg-book7.tex"), "wb").write(tex)
    shutil.copytree(os.path.join(R, "chapters"), os.path.join(M, "chapters"))
    shutil.copytree(os.path.join(R, "frontmatter"), os.path.join(M, "frontmatter"))
    if patchB:
        p = os.path.join(M, "chapters", "ch03-matrix-action.tex")
        c3 = open(p, "rb").read()
        assert c3.count(B_BEGIN) == 1 and c3.count(B_END) == 1, "anchor B not unique"
        c3 = c3.replace(B_BEGIN, B_INS1 + B_BEGIN).replace(B_END, B_END + B_INS2)
        open(p, "wb").write(c3)
    for ext in (".aux", ".bbl", ".toc", ".out"):
        shutil.copy2(os.path.join(R, "namcg-book7" + ext),
                     os.path.join(M, "namcg-book7" + ext))
    return M

def run_build(name):
    M = os.path.join(S, name)
    O = os.path.join(S, "out-" + name)
    if os.path.exists(O):
        shutil.rmtree(O)
    os.makedirs(os.path.join(O, "chapters"))
    os.makedirs(os.path.join(O, "frontmatter"))
    for ext in (".aux", ".bbl", ".toc", ".out"):
        shutil.copy2(os.path.join(R, "namcg-book7" + ext),
                     os.path.join(O, "namcg-book7" + ext))
    env = dict(os.environ)
    env["TEXINPUTS"] = M.replace(os.sep, "/") + "/;;"
    passes = 2 if name == "cand" else 1
    rc = None
    for _ in range(passes):
        r = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-file-line-error",
             "-output-directory", O, os.path.join(M, "namcg-book7.tex")],
            cwd=R, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        rc = r.returncode
    log = os.path.join(O, "namcg-book7.log")
    return rc, log

# --- 0. tracked-tree before hashes
pre = {p: h12(os.path.join(R, p)) for p in TRACKED}

# --- 1. parser positive control (must find exactly 1 box at 9.99)
fake = ("some junk " + TOK + "9.99pt too wide) in paragraph at lines 1--2"
        " tail junk " + "Overfull " + BS + "hbox no paren decoy 9.99")
ctl = parse_boxes(fake)
ctl = [v for (v, j) in ctl if "in paragraph at lines 1--2" in fake[j:j + 120]]
print("CTL-PARSER boxes:", len(ctl), "values:", ctl)
if len(ctl) != 1 or abs(ctl[0] - 9.99) > 1e-9:
    fails.append("parser positive control did not fire")

# --- 2. region scanner positive control
fake2 = ("(C:/m/chapters/ch03-matrix-action.tex Chapter 3. "
         + TOK + "5.00pt too wide) in paragraph at lines 802--813 "
         "C:/m/chapters/ch04-vierbein-emergence.tex Chapter 4. "
         + TOK + "1.00pt too wide) elsewhere")
st = region_of(fake2, "ch03-matrix-action", "Chapter 3.")
en = region_of(fake2, "ch04-vierbein-emergence", "Chapter 4.")
inr = boxes_between(fake2, st, en)
outr = [v for (v, j) in parse_boxes(fake2) if not (st <= j < en)]
print("CTL-REGION in-region:", inr, "outside:", outr)
if len(inr) != 1 or len(outr) != 1:
    fails.append("region scanner positive control failed")

# --- 3. baseline mirror: reproduce the 14-box audit (site-existence control)
build_mirror("base", False, False)
rc_b, log_b = run_build("base")
ub = unwrap(log_b)
bb = parse_boxes(ub)
b3 = boxes_between(ub, region_of(ub, "ch03-matrix-action", "Chapter 3."),
                   region_of(ub, "ch04-vierbein-emergence", "Chapter 4."))
print("BASE rc:", rc_b, "total:", len(bb), "ch03-region:", [round(v, 5) for v in b3])
if rc_b != 0:
    fails.append("base rc nonzero")
if len(bb) != 14 or len(b3) != 1 or abs(b3[0] - 5.04942) > 1e-3:
    fails.append("base did not reproduce 14 boxes / ch03 site 5.04942")

# --- 4. candidate mirror (A+B)
build_mirror("cand", True, True)
rc_c, log_c = run_build("cand")
uc = unwrap(log_c)
cb = parse_boxes(uc)
vals = [v for (v, j) in cb]
c3 = boxes_between(uc, region_of(uc, "ch03-matrix-action", "Chapter 3."),
                   region_of(uc, "ch04-vierbein-emergence", "Chapter 4."))
mirror_trace = "margin-typo/cert/cand/chapters/ch03-matrix-action.tex" in uc
owners = [owner_of(uc, j) for (v, j) in cb]
pg = uc[uc.find("Output written"): uc.find("Output written") + 200]
print("CAND rc:", rc_c, "total:", len(vals), "max:", max(vals) if vals else 0.0)
print("CAND sizes:", [round(v, 5) for v in vals], "owners:", owners)
print("CAND ch03-region:", len(c3), "mirror trace:", mirror_trace)
print("CAND page line:", pg[:120])
if rc_c != 0:
    fails.append("cand rc nonzero")
if any(L.startswith("!") for L in open(log_c, encoding="utf-8", errors="replace")):
    fails.append("cand log has error lines")
if not (1 <= len(vals) <= 2):
    fails.append("cand total not <= 2")
if vals and max(vals) > 1.25:
    fails.append("cand max > 1.25pt")
if len(c3) != 0 or any(5.00 <= v <= 5.10 for v in vals):
    fails.append("ch03 site not gone")
if not mirror_trace:
    fails.append("candidate did not read the mirrored ch03")

# --- 5. tracked tree untouched
post = {p: h12(os.path.join(R, p)) for p in TRACKED}
for p in TRACKED:
    if pre[p] != post[p]:
        fails.append("tracked file changed: " + p + " " + pre[p] + "->" + post[p])
print("TRACKED hashes unchanged:", all(pre[p] == post[p] for p in TRACKED))

mx = max(vals) if vals else 0.0
summary = "BASE%d CAND%d CH03SITE%d MAX%.3f" % (len(bb), len(vals), len(c3), mx)
if fails:
    for f in fails:
        print("FAIL:", f)
    print("CERT130 FAIL", summary)
    sys.exit(1)
print("CERT130 PASS", summary)
