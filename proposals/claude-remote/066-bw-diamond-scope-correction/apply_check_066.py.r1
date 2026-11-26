"""Report-only apply check for proposal 066.
Usage: python apply_check_066.py <repo_root> <out_dir_outside_repo>
Reads appH and bib from the repo (read-only), applies the OLD->NEW replacements,
verifies baseline hashes, uniqueness, CRLF and no BOM, writes patched copies to out_dir only."""
import hashlib, os, sys

B = chr(92)          # backslash
NL = "\r\n"

def L(*lines):
    return NL.join(lines)

repo, out = sys.argv[1], sys.argv[2]
assert not os.path.abspath(out).lower().startswith(os.path.abspath(repo).lower()), "out_dir must be outside repo"
os.makedirs(out, exist_ok=True)

APPH = os.path.join(repo, "chapters", "appH-microscopic-proofs.tex")
BIB = os.path.join(repo, "bib", "namcg.bib")
BASE = {APPH: (624232, "c2dac013f275fed851d53e8086bc3eceef717c5b607b10c09ae7541c43558b5c"),
        BIB: (29781, "28fdd7f8cb62b2ad23da3cc05d819a0b750f7fdec096511fca60ab02135ea64d")}

def c(s):  # inline math \( \)
    return B + "(" + s + B + ")"

E1_OLD = L("degree " + c(B + "le 2") + "). By the Bisognano\u2013Wichmann theorem this charge is the",
           "modular Hamiltonian of the causal diamond of the free theory. The")
E1_NEW = L("degree " + c(B + "le 2") + "). For a Rindler wedge, the Bisognano--Wichmann",
           "theorem~" + B + "cite{BisognanoWichmann1976} identifies the vacuum modular",
           "Hamiltonian with " + c("2" + B + "pi") + " times the boost generator that fixes the",
           "wedge (Section~" + B + "ref{sec:appB-BW}), for free fields with or without",
           "mass. For a causal diamond (double cone), the identification of the",
           "vacuum modular flow with the conformal Killing flow of the diamond is",
           "established for the free massless scalar field~" + B + "cite{HislopLongo1982},",
           "through conformal covariance. No such geometric identification is",
           "used here for massive free fields, such as the radial mode with the",
           "mass " + c("m_" + B + "sigma") + " of Section~" + B + "ref{sec:ch3-scales}. Hence the charge",
           "is the modular Hamiltonian of the wedge for the free theory, and",
           "of the causal diamond only for its free massless scalar part. The")

E2_OLD = c(B + "Theta") + ", with error " + c("O(R" + B + "sqrt{" + B + "|" + B + "delta" + B + "Theta" + B + "|})") + " under fluctuations."
E2_NEW = L(c(B + "Theta") + ". Its error under fluctuations of " + c(B + "Theta") + " is not derived",
           "here; the scaling " + c("O(R" + B + "sqrt{" + B + "|" + B + "delta" + B + "Theta" + B + "|})") + ", with " + c("R") + " the",
           "diamond radius, is an unproved estimate.")

E3_OLD = L("terms and is not a routine specialisation of the free-field result. The",
           "bound",
           B + "[")
E3_NEW = L("terms and is not a routine specialisation of the free-field result. The",
           "estimate, which is not derived here,",
           B + "[")

E4_OLD = L("controls the difference from the free modular flow (itself identified",
           "with the diamond only in the constant-" + c(B + "Theta") + " quadratic sector); it",
           "does not control")
E4_NEW = L("would control the difference from the free modular flow (itself",
           "identified with the diamond only in the constant-" + c(B + "Theta") + " quadratic",
           "sector, and there only for its free massless scalar part); it would",
           "not control")

E5_OLD = L("of the general theory. The error bound therefore controls the",
           "difference from an unproven candidate, not from the diamond modular")
E5_NEW = L("of the general theory. Even if derived, the estimate would therefore",
           "control only the difference from an unproven candidate, not from the",
           "diamond modular")

B1_OLD = L("@article{BisognanoWichmann1976,",
           "  author  = {Bisognano, J. J. and Wichmann, E. H.},",
           "  title   = {On the Duality Condition for Quantum Fields},",
           "  journal = {Journal of Mathematical Physics},",
           "  volume  = {17},",
           "  pages   = {303},",
           "  year    = {1976}",
           "}") + NL
B1_NEW = B1_OLD + NL + L("@article{HislopLongo1982,",
           "  author  = {Hislop, Peter D. and Longo, Roberto},",
           "  title   = {Modular Structure of the Local Algebras Associated with",
           "             the Free Massless Scalar Field Theory},",
           "  journal = {Communications in Mathematical Physics},",
           "  volume  = {84},",
           "  number  = {1},",
           "  pages   = {71--85},",
           "  year    = {1982},",
           "  doi     = {10.1007/BF01208372}",
           "}") + NL

E6_OLD = c("(" + B + "hat X," + B + "Phi)" + B + "mapsto H_D") + " is a lemma in this sector, defined from"
E6_NEW = L(c("(" + B + "hat X," + B + "Phi)" + B + "mapsto H_D") + " is a lemma for that massless scalar part",
           "of this sector, defined from")

EDITS = {APPH: [("E1", E1_OLD, E1_NEW), ("E2", E2_OLD, E2_NEW), ("E3", E3_OLD, E3_NEW),
                 ("E4", E4_OLD, E4_NEW), ("E5", E5_OLD, E5_NEW), ("E6", E6_OLD, E6_NEW)],
         BIB: [("B1", B1_OLD, B1_NEW)]}

ok = True
for path, edits in EDITS.items():
    raw = open(path, "rb").read()
    size, sha = BASE[path]
    h0 = hashlib.sha256(raw).hexdigest()
    print(f"{os.path.basename(path)} baseline bytes={len(raw)} sha256={h0} match={len(raw)==size and h0==sha}")
    ok &= (len(raw) == size and h0 == sha)
    text = raw.decode("utf-8")
    for name, old, new in edits:
        n = text.count(old)
        print(f"  {name}: OLD occurrences={n}; NEW occurrences before={text.count(new)}")
        ok &= (n == 1)
        text = text.replace(old, new, 1)
    data = text.encode("utf-8")
    crlf, lf = data.count(b"\r\n"), data.count(b"\n")
    print(f"  result bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()} CRLF={crlf} LF={lf} bareLF={lf-crlf} BOM={data[:3]==bytes([0xef,0xbb,0xbf])}")
    ok &= (crlf == lf) and data[:3] != bytes([0xef, 0xbb, 0xbf])
    for name, old, new in edits:
        ok &= text.count(new) == 1 if name != "B1" else text.count("@article{HislopLongo1982,") == 1
    open(os.path.join(out, os.path.basename(path)), "wb").write(data)
print("ALL CHECKS PASS" if ok else "CHECK FAILED")
