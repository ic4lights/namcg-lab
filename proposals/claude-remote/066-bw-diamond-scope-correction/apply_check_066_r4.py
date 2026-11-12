"""Report-only apply check for proposal 066, round 4 (r3 list F0-F9 unchanged plus F10, applied after F9).
Usage: python -I apply_check_066_r4.py <repo_root> <out_dir_outside_repo>
Path A (chain): baseline -> r1 edits (checks r1 result hashes) -> r2 deltas.
Path B (direct): baseline -> final r2 OLD->NEW list (what the integrator applies).
Asserts each OLD occurs exactly once before and each NEW exactly once after, both paths agree,
CRLF only, no BOM. Writes patched copies only to out_dir (asserted outside the repo)."""
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
BASE = {APPH: (624232, "c2dac013f275fed851d53e8086bc3eceef717c5b607b10c09ae7541c43558b5c"),
        BIB: (29781, "28fdd7f8cb62b2ad23da3cc05d819a0b750f7fdec096511fca60ab02135ea64d")}
R3 = {APPH: "fa12e54a83a05061177e2289b83be59c1007118b57f3c799d9e8685049ce29f7",
      BIB: "4315a89553cb97405af89604f1e43c9e5e0237fa5b7be0439431d042677a6060"}
R2 = {APPH: "b8155af307c5d8840405d2bb8e4d3e1b5217316d1fcf555f398839c9ce82394e",
      BIB: "4315a89553cb97405af89604f1e43c9e5e0237fa5b7be0439431d042677a6060"}
R1 = {APPH: "173ab97bc1ffeb14a089f2db2fbefb6f6570727e5d8f5ec885d09083f497e945",
      BIB: "4315a89553cb97405af89604f1e43c9e5e0237fa5b7be0439431d042677a6060"}
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
R1_TAIL = ["is the modular Hamiltonian of the wedge for the free theory, and",
           "of the causal diamond only for its free massless scalar part. The",
           "positive spectral subspace therefore generates the half-sided inclusion",
           "whose modular operator is exactly " + c("H_D") + ". The map",
           MAP + " is a lemma for that massless scalar part",
           "of this sector, defined from"]
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

R1_EDITS = {APPH: [("E1+E6", BASE_L30_34, L(*E1_HEAD, *R1_TAIL)), ("E2", E2_OLD, E2_NEW("R")),
                   ("E3", E3_OLD, E3_NEW("")), ("E4", E4_OLD, E4_NEW), ("E5", E5_OLD, E5_NEW)],
            BIB: [("B1", B1_OLD, B1_NEW)]}
D_EDITS = {APPH: [("D0 (Finding 3, L28)", E0_OLD, E0_NEW), ("D1 (Findings 1-3)", L(E1_HEAD[-1], *R1_TAIL), L(E1_HEAD[-1], *R2_TAIL)),
                  ("D2 (Finding 4, E2 R->ell)", E2_NEW("R"), E2_NEW(ELL)),
                  ("D3 (Finding 5, norm)", E3_NEW(""), E3_NEW(NORM)),
                  ("D4 (Finding 4, E7 display)", E7_OLD, E7_NEW),
                  ("D5 (Finding 6, L37-39)", E8_OLD, E8_NEW)],
           BIB: []}
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
D4_EDITS = {APPH: [("D10 (r3->r4, review-r3 Finding 1)", F10_OLD, F10_NEW)], BIB: []}
D3_EDITS = {APPH: [("D9 (r2->r3, review-r2 Finding 1)", F9_OLD, F9_NEW)], BIB: []}
F_EDITS = {APPH: [("F0", E0_OLD, E0_NEW), ("F1", BASE_L30_34, L(*E1_HEAD, *R2_TAIL)), ("F2", E2_OLD, E2_NEW(ELL)),
                  ("F3", E3_OLD, E3_NEW(NORM)), ("F4", E4_OLD, E4_NEW), ("F5", E5_OLD, E5_NEW),
                  ("F6", E7_OLD, E7_NEW), ("F7", E8_OLD, E8_NEW), ("F9", F9_OLD, F9_NEW), ("F10", F10_OLD, F10_NEW)],
           BIB: [("F8", B1_OLD, B1_NEW)]}

ok = True
def apply(text, edits, tag):
    global ok
    for name, old, new in edits:
        n_old, n_new = text.count(old), text.count(new)
        text = text.replace(old, new, 1)
        n_after = text.count(new)
        good = n_old == 1 and n_new == 0 and n_after == 1
        print(f"  [{tag}] {name}: OLD before={n_old} NEW before={n_new} NEW after={n_after} {'ok' if good else 'FAIL'}")
        ok &= good
    return text

for path in (APPH, BIB):
    raw = open(path, "rb").read(); size, h = BASE[path]
    print(f"{os.path.basename(path)} baseline bytes={len(raw)} sha256={sha(raw)} match={len(raw)==size and sha(raw)==h}")
    ok &= len(raw) == size and sha(raw) == h
    t0 = raw.decode("utf-8")
    t1 = apply(t0, R1_EDITS[path], "r1")
    h1 = sha(t1.encode("utf-8"))
    print(f"  r1 result sha256={h1} matches r1 proposal={h1==R1[path]}")
    ok &= h1 == R1[path]
    t2 = apply(t1, D_EDITS[path], "r1->r2")
    h2 = sha(t2.encode("utf-8"))
    print(f"  r2 result sha256={h2} matches r2 proposal={h2==R2[path]}")
    ok &= h2 == R2[path]
    t3 = apply(t2, D3_EDITS[path], "r2->r3")
    h3 = sha(t3.encode("utf-8"))
    print(f"  r3 result sha256={h3} matches r3 proposal={h3==R3[path]}")
    ok &= h3 == R3[path]
    t2a = apply(t3, D4_EDITS[path], "r3->r4")
    t2b = apply(t0, F_EDITS[path], "direct")
    ok &= t2a == t2b
    d = t2b.encode("utf-8"); crlf, lf = d.count(b"\r\n"), d.count(b"\n")
    print(f"  r4 result bytes={len(d)} sha256={sha(d)} chain==direct={t2a==t2b} "
          f"CRLF={crlf} LF={lf} bareLF={lf-crlf} BOM={d[:3]==bytes([0xef,0xbb,0xbf])}")
    ok &= crlf == lf and d[:3] != bytes([0xef, 0xbb, 0xbf])
    open(os.path.join(out, os.path.basename(path)), "wb").write(d)
print("ALL CHECKS PASS" if ok else "CHECK FAILED")
