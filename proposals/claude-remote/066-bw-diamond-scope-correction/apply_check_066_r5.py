"""Report-only apply check for proposal 066, round 5.

Direct chain F0-F7, F9, F10 (proposal-r2/r3/r4 lists, byte-identical strings to apply_check_066_r4.py),
then S1 and S2 (review-r4.md, section "Corrected snippet", verbatim), applied to the CURRENT (drifted)
appH baseline; bib edit F8 unchanged. For every edit: OLD must occur exactly once before and NEW
exactly once after. Failures are reported with context, never forced.

The r1/r2/r3 chain hashes are NOT re-derived here: the appH baseline has drifted (new Problem A
paragraph "Explicit Weyl data and per-order error in the flat Abelian class." at L63-109 and hunks
deeper in the file), so the historical chain hashes cannot be reproduced from the new baseline.
The F strings are the same ones the r4 script verified against the r4-era baseline.

Usage: python -I apply_check_066_r5.py <repo_root> <out_dir_outside_repo>
Writes patched copies only to out_dir (asserted outside the repo)."""
import hashlib, os, sys
B = chr(92); NL = "\r\n"; EN = "–"; ELL = B + "ell"
def L(*a): return NL.join(a)
def c(s): return B + "(" + s + B + ")"
def sha(b): return hashlib.sha256(b).hexdigest()

repo, out = sys.argv[1], sys.argv[2]
assert not os.path.abspath(out).lower().startswith(os.path.abspath(repo).lower()), "out_dir must be outside repo"
os.makedirs(out, exist_ok=True)
APPH = os.path.join(repo, "chapters", "appH-microscopic-proofs.tex")
BIB = os.path.join(repo, "bib", "namcg.bib")
# Current baselines (working tree, HEAD f2cafc1, digest CURRENT, 2026-11-12).
BASE = {APPH: (688007, "382389a4345a1c554fd4d7c2a6621c7eca3f0d84e357aefdecf668658bdeed46"),
        BIB: (36133, "bd0d8a80cf616587d06bdfafeed199539c9af75d4f89e102472836e11583cc35")}
# Historical r4-era baselines and results, for the record only (not checked here).
R4_ERA = {APPH: ("baseline c2dac013f275fed851d53e8086bc3eceef717c5b607b10c09ae7541c43558b5c 624232 B",
                 "r4 result c5bf9be4f7c9b51218be4000dcdd5273ebf3cfa3e125d0a5fe90299e443075b3 625774 B"),
          BIB: ("baseline 28fdd7f8cb62b2ad23da3cc05d819a0b750f7fdec096511fca60ab02135ea64d 29781 B",
                "r4 result 4315a89553cb97405af89604f1e43c9e5e0237fa5b7be0439431d042677a6060 30159 B")}

def SQ(r): return "O(" + r + B + "sqrt{" + B + "|" + B + "delta" + B + "Theta" + B + "|})"
TH = c(B + "Theta")
MAP = c("(" + B + "hat X," + B + "Phi)" + B + "mapsto H_D")

E1_HEAD = ["degree " + c(B + "le 2") + "). For a Rindler wedge, the Bisognano--Wichmann",
           "theorem~" + B + "cite{BisognanoWichmann1976} identifies the vacuum modular",
           "Hamiltonian with " + c("2" + B + "pi") + " times the boost generator that fixes the",
           "wedge (Section~" + B + "ref{sec:appB-BW}), for free fields with or without",
           "mass. For a causal diamond (double cone), the identification of the",
           "vacuum modular flow with the conformal Killing flow of the diamond is",
           "established for the free massless scalar field~" + B + "cite{HislopLongo1982},",
           "through conformal covariance. No such geometric identification is",
           "used here for massive free fields, such as the radial mode with the",
           "mass " + c("m_" + B + "sigma") + " of Section~" + B + "ref{sec:ch3-scales}. Hence the charge"]
R2_TAIL = ["is a vacuum modular Hamiltonian only where it coincides with one of",
           "these generators: the wedge boost charge, for the free theory, or the",
           "diamond conformal Killing charge, for its free massless scalar part.",
           "Which of these charges the Weyl symbol of " + c("K_0") + " equals, and for",
           "which " + c("H_{" + B + "mathrm{quad}}") + ", is not derived here. Nor is the statement",
           "that, in the diamond case, the positive spectral subspace generates a",
           "half-sided inclusion whose modular operator is " + c("H_D") + ". Given these",
           "two steps, the map " + MAP + " is a lemma for that",
           "massless scalar part of this sector, defined from"]
BASE_L30_34 = L("degree " + c(B + "le 2") + "). By the Bisognano" + EN + "Wichmann theorem this charge is the",
                "modular Hamiltonian of the causal diamond of the free theory. The",
                "positive spectral subspace therefore generates the half-sided inclusion",
                "whose modular operator is exactly " + c("H_D") + ". The map",
                MAP + " is a lemma in this sector, defined from")
E2_OLD = TH + ", with error " + c(SQ("R")) + " under fluctuations."
def E2_NEW(r): return L(TH + ". Its error under fluctuations of " + TH + " is not derived",
                        "here; the scaling " + c(SQ(r)) + ", with " + c(r) + " the",
                        "diamond radius, is an unproved estimate.")
E3_OLD = L("terms and is not a routine specialisation of the free-field result. The", "bound", B + "[")
def E3_NEW(extra): return L("terms and is not a routine specialisation of the free-field result. The",
                            "estimate, which is not derived here" + extra + ",", B + "[")
E4_OLD = L("controls the difference from the free modular flow (itself identified",
           "with the diamond only in the constant-" + TH + " quadratic sector); it", "does not control")
E4_NEW = L("would control the difference from the free modular flow (itself",
           "identified with the diamond only in the constant-" + TH + " quadratic",
           "sector, and there only for its free massless scalar part); it would", "not control")
E5_OLD = L("of the general theory. The error bound therefore controls the",
           "difference from an unproven candidate, not from the diamond modular")
E5_NEW = L("of the general theory. Even if derived, the estimate would therefore",
           "control only the difference from an unproven candidate, not from the", "diamond modular")
E7_OLD = ("=O" + B + "bigl(R" + B + "sqrt{" + B + "|" + B + "delta" + B + "Theta" + B + "|}+"
          + B + "|H_{" + B + "mathrm{int}}" + B + "|" + B + "bigr)")
E7_NEW = E7_OLD.replace("bigl(R", "bigl(" + ELL)
E8_OLD = L("Mutual information follows from the Araki formula. This makes explicit",
           "the conditional free/Poisson content already noted above; it remains",
           "dependent on the free-field theorem.")
E8_NEW = L("Mutual information follows from the Araki formula. This records the",
           "conditional free/Poisson content of Problem~A; it remains dependent on",
           "the free-field theorems cited above and on the two steps not derived",
           "here.")
NORM = " (in a norm not specified here)"
E0_OLD = "has Weyl symbol equal to the classical boost/diamond Noether charge"
E0_NEW = L("is taken here to have Weyl symbol equal to the classical boost/diamond", "Noether charge")
B1_OLD = L("@article{BisognanoWichmann1976,", "  author  = {Bisognano, J. J. and Wichmann, E. H.},",
           "  title   = {On the Duality Condition for Quantum Fields},",
           "  journal = {Journal of Mathematical Physics},", "  volume  = {17},", "  pages   = {303},",
           "  year    = {1976}", "}") + NL
B1_NEW = B1_OLD + NL + L("@article{HislopLongo1982,", "  author  = {Hislop, Peter D. and Longo, Roberto},",
           "  title   = {Modular Structure of the Local Algebras Associated with",
           "             the Free Massless Scalar Field Theory},",
           "  journal = {Communications in Mathematical Physics},", "  volume  = {84},", "  number  = {1},",
           "  pages   = {71--85},", "  year    = {1982},", "  doi     = {10.1007/BF01208372}", "}") + NL
F9_OLD = L(TH.replace("Theta", "Theta=" + B + "Theta_0+" + B + "delta" + B + "Theta") + ", the same algebraic construction yields",
           "a well-defined modular operator of a half-sided inclusion from matrix",
           "data alone. That operator is a candidate modular Hamiltonian. It is the")
F9_NEW = L(TH.replace("Theta", "Theta=" + B + "Theta_0+" + B + "delta" + B + "Theta") + ", the same algebraic construction would",
           "yield, if it generates a half-sided inclusion (a step not derived here,",
           "as in the free case) and given a cyclic and separating state, a",
           "modular operator built from matrix data. That operator would be a",
           "candidate modular Hamiltonian. It is the")
F10_OLD = L("candidate modular Hamiltonian. It is the",
            "modular Hamiltonian of a causal diamond if and only if the",
            "semi-classical symbol of " + c("K_0") + " is shown to recover the geometric",
            "boost/diamond vector field of the emergent geometry. That matching has")
F10_NEW = L("candidate modular Hamiltonian. It would be the modular Hamiltonian of",
            "a causal diamond if the semi-classical symbol of " + c("K_0") + " were shown to",
            "recover the geometric boost/diamond vector field of the emergent",
            "geometry, in a sector whose diamond modular flow is known to be",
            "geometric (for free fields, the massless scalar part cited above);",
            "elsewhere that recovery is not known to suffice. That matching has")
# S1 and S2: review-r4.md "Corrected snippet", verbatim, applied after the F chain.
S1_OLD = L("mass " + c("m_" + B + "sigma") + " of Section~" + B + "ref{sec:ch3-scales}. Hence the charge",
           "is a vacuum modular Hamiltonian only where it coincides with one of")
S1_NEW = L("mass " + c("m_" + B + "sigma") + " of Section~" + B + "ref{sec:ch3-scales}. Hence the charge",
           "is known to be a vacuum modular Hamiltonian only where it coincides",
           "with one of")
S2_OLD = L("elsewhere that recovery is not known to suffice. That matching has",
           "not been performed for higher-order, interacting, or fluctuating-" + TH,
           "terms and is not a routine specialisation of the free-field result. The")
S2_NEW = L("elsewhere that recovery is not known to suffice. That matching has",
           "not been performed, even in the quadratic sector, where the Weyl-symbol",
           "identification above is not derived; for higher-order, interacting, or",
           "fluctuating-" + TH + " terms it would not be a routine specialisation of",
           "the free-field case. The")

# Sanity: S1 OLD is the junction of F1 NEW lines; S2 OLD is F10 NEW last line + baseline lines.
assert S1_OLD == NL.join([E1_HEAD[-1], R2_TAIL[0]])
assert S2_OLD == NL.join([F10_NEW.split(NL)[-1],
                          "not been performed for higher-order, interacting, or fluctuating-" + TH,
                          "terms and is not a routine specialisation of the free-field result. The"])

F_EDITS = {APPH: [("F0", E0_OLD, E0_NEW), ("F1", BASE_L30_34, L(*E1_HEAD, *R2_TAIL)), ("F2", E2_OLD, E2_NEW(ELL)),
                  ("F3", E3_OLD, E3_NEW(NORM)), ("F4", E4_OLD, E4_NEW), ("F5", E5_OLD, E5_NEW),
                  ("F6", E7_OLD, E7_NEW), ("F7", E8_OLD, E8_NEW), ("F9", F9_OLD, F9_NEW), ("F10", F10_OLD, F10_NEW),
                  ("S1 (review-r4)", S1_OLD, S1_NEW), ("S2 (review-r4)", S2_OLD, S2_NEW)],
           BIB: [("F8", B1_OLD, B1_NEW)]}

ok = True
def lineno(text, pos): return text.count("\n", 0, pos) + 1
def apply(text, edits, tag):
    global ok
    for name, old, new in edits:
        n_old, n_new = text.count(old), text.count(new)
        if n_old == 1:
            at = lineno(text, text.find(old))
            loc = f"OLD at line {at}"
        elif n_old > 1:
            poss = []; i = text.find(old)
            while i >= 0 and len(poss) < 10:
                poss.append(lineno(text, i)); i = text.find(old, i + 1)
            loc = "OLD occurrences at lines " + ",".join(map(str, poss))
        else:
            head = old.split(NL)[0]
            probe = text.find(head)
            loc = "OLD NOT FOUND; first line of OLD" + (f" occurs at line {lineno(text, probe)}" if probe >= 0 else " does not occur at all")
        text = text.replace(old, new, 1)
        n_after = text.count(new)
        good = n_old == 1 and n_new == 0 and n_after == 1
        print(f"  [{tag}] {name}: OLD before={n_old} NEW before={n_new} NEW after={n_after} | {loc} | {'ok' if good else 'FAIL'}")
        if not good:
            print(f"    OLD bytes: {old!r}")
            print(f"    NEW bytes: {new!r}")
        ok &= good
    return text

for path in (APPH, BIB):
    raw = open(path, "rb").read(); size, h = BASE[path]
    print(f"{os.path.basename(path)} baseline bytes={len(raw)} sha256={sha(raw)} match_current_baseline={len(raw)==size and sha(raw)==h}")
    print(f"  r4-era for the record: {R4_ERA[path][0]}; {R4_ERA[path][1]}")
    ok &= len(raw) == size and sha(raw) == h
    t = apply(raw.decode("utf-8"), F_EDITS[path], "direct")
    d = t.encode("utf-8"); crlf, lf = d.count(b"\r\n"), d.count(b"\n")
    print(f"  r5 result bytes={len(d)} sha256={sha(d)} CRLF={crlf} LF={lf} bareLF={lf-crlf} "
          f"BOM={d[:3]==bytes([0xef,0xbb,0xbf])}")
    ok &= crlf == lf and lf == t.count("\r\n") and d[:3] != bytes([0xef, 0xbb, 0xbf])
    if path == APPH:
        for key in ("HislopLongo1982", "BisognanoWichmann1976"):
            print(f"  cite count {key} = {t.count('{'+key+'}')}")
        ok &= t.count("{HislopLongo1982}") == 1 and t.count("{BisognanoWichmann1976}") == 1
    open(os.path.join(out, os.path.basename(path)), "wb").write(d)
print("ALL CHECKS PASS" if ok else "CHECK FAILED")
