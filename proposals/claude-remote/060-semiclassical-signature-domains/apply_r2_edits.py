"""060 r2: apply review-r1 R1-R9 verbatim (plus optional item 10) to the r1 bytes.
Checks the r1 hashes, that each old string occurs exactly once before replacement, and that each new
string occurs exactly once afterwards. Raw strings; backslashes are literal."""
import hashlib
H_INS = 'f2a08fbcd9e5ec46db6a79e43eff0324701e5fef973fd4a97a3c2525069994ee'
H_BIB = 'e142c5c0a4e2ce8cd628ec3759b6d83a514186ac0255d731993547f592cbdaf7'
ins = open('appH_insert.r1.tex', 'rb').read()
bib = open('bib_entries.r1.bib', 'rb').read()
assert hashlib.sha256(ins).hexdigest() == H_INS, 'insert r1 hash'
assert hashlib.sha256(bib).hexdigest() == H_BIB, 'bib r1 hash'
s = ins.decode('ascii')

# R2: locate the span by its first and last words
start = r"A representation of \(\mathfrak{so}(4,2)\) by Hermitian"
end = r"exists only for \(N\to\infty\)."
assert s.count(start) == 1 and s.count(end) == 1
i = s.index(start); j = s.index(end) + len(end)
old_R2 = s[i:j]
new_R2 = (r"The \(T^a\) and their commutators span the subalgebra on the five indices \(a\) and \(c_0\), which is "
          r"\(\mathfrak{so}(4,1)\) for the class above. A representation of a non-compact simple Lie algebra by "
          r"Hermitian \(N\times N\) matrices is trivial, since its image would be a compact Lie algebra isomorphic "
          r"to it, with negative definite Killing form, whereas the Killing form of a non-compact simple Lie algebra "
          r"is indefinite; \(\mathfrak{so}(5)\subset\mathfrak{so}(6)\) has such representations. Within this family, "
          r"a non-zero solution at finite \(N\) therefore has \(\eta\) definite on these five indices and a positive "
          r"definite kinetic tensor, and the Lorentzian member exists only for \(N\to\infty\).")

reps = [
    # R1
    (r"the kinetic tensor is \(\gamma^{\mu\nu}=(h_0)_{ab}E^{a\mu}E^{b\nu}\)",
     r"the kinetic tensor is \(\mathsf K^{\mu\nu}=(h_0)_{ab}E^{a\mu}E^{b\nu}\), that of Definition~\ref{def:matrix-coords-ext} with \(h_0\) in place of \(\eta_{IJ}\)"),
    (r"then \(\gamma\) is a Gram matrix", r"then \(\mathsf K\) is a Gram matrix"),
    (r"point, \(\gamma\) has, by Sylvester's", r"point, \(\mathsf K\) has, by Sylvester's"),  # review text read "four, ..."; actual r1 text is "point, ..."
    (r"then \(\gamma=m^2\eta^{-1}H\eta^{-1}\)", r"then \(\mathsf K=m^2\eta^{-1}H\eta^{-1}\)"),
    (r"and \(\gamma=0\) where \(m=0\)", r"and \(\mathsf K=0\) where \(m=0\)"),
    (r"\(\rho^2=\rho_M|\det\gamma^{\mu\nu}|^{1/2}\)",
     r"\(\rho^2=\rho_M|\det\mathsf K^{\mu\nu}|^{1/2}\), with \(\mathsf K\) the tensor written \(\gamma^{\mu\nu}\) there,"),
    # R2
    (old_R2, new_R2),
    # R3
    (r"\(m=M^{45}\) and \(\ell^2=-y_ay^a\)", r"\(m=M^{45}\) and \(y_\mu y^\mu=-\ell^2-m^2\)"),
    # R4
    (r"The criterion therefore fails, as stated in~\cite{Steinacker2026Weak} for commutative backgrounds.",
     r"The Euclidean criterion therefore fails, as stated in~\cite{Steinacker2026Weak} for commutative backgrounds; for \(\eta\) the window \(|t'-t|<\Delta_T\) then contains no \(t'\neq t\), and the states below give a ratio that grows like \(\sigma^{-2}\) as their width \(\sigma\to0\)."),
    (r", so that \(\Delta_T=\sigma\),",
     r", with its uncertainty \(\sigma\) in place of \(\Delta_T\), since no quasi-coherent state exists,"),
    # R5
    (r"; the weight \(w\) used for this class in Section~\ref{sec:status-D} supplies such a width and is not derived.",
     r"; the weight \(w\) used for this class in Section~\ref{sec:status-D} is likewise a supplied momentum scale, and no width is derived."),
    # R6
    (r"the criterion as \(g_{\mathrm{YM}}/\sqrt2\) at late \(\tau\)", r"the criterion as of order \(g_{\mathrm{YM}}\) at late \(\tau\)"),
    # R7
    (r"the identity with \(c_0=5\) gives \(\gamma=-3c\),",
     r"the identity with \(c_0=5\) gives \(\gamma=-3c\), with \(c>0\) for \(h_0\) of signature \((9,1)\) as above,"),
    # R8
    (r"therefore do not apply to these backgrounds", r"therefore do not apply to the conjugate-coordinate backgrounds"),
    # optional item 10 (adopted)
    (r"It is the mechanism of~\cite{Steinacker2018BB}, where,",
     r"The same mechanism, averaging over the fibre, gives the signature change of~\cite{Steinacker2018BB}, where,"),
]
for a, b in reps:
    assert s.count(a) == 1, ('old', a[:80])
    s = s.replace(a, b)
    assert s.count(b) == 1, ('new', b[:80])
open('appH_insert.tex', 'w', encoding='ascii', newline='\n').write(s)

# R9
bs = bib.decode('ascii')
a = "  year    = {2026},\n  eprint  = {2605.13294},"
b = "  year    = {2026},\n  note    = {Version 2; the equation numbers cited refer to it},\n  eprint  = {2605.13294},"
assert bs.count(a) == 1
bs = bs.replace(a, b)
assert bs.count(b) == 1
open('bib_entries.bib', 'w', encoding='ascii', newline='\n').write(bs)

for fn in ['appH_insert.tex', 'bib_entries.bib']:
    d = open(fn, 'rb').read()
    print(fn, len(d), hashlib.sha256(d).hexdigest(), 'CR', d.count(b'\r'))
import re
rest = re.findall(r"\\gamma[^_a-zA-Z]", s)
print('remaining \\gamma occurrences (mass parameter, or "written gamma there"):', len(rest))
for m in re.finditer(r".{40}\\gamma.{30}", s):
    print('   ', m.group(0))
