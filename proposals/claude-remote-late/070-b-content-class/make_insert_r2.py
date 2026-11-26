"""070 r2: build appH_insert_r2.tex from appH_insert.tex by exact, single-occurrence replacements.
Re-run: python proposals/070-b-content-class/make_insert_r2.py"""
import pathlib
here = pathlib.Path(__file__).parent
t = (here/'appH_insert.tex').read_bytes().decode('utf-8').replace('\r\n', '\n')
R = []
# m4: duplicated decomposition sentence -> back-reference
R.append(("m4",
r"The gap of the fixed-state replica has two parts of different origin: the index-weighted coefficient of \(\rho^2X\), which enters the tensor side only, and the excess \(+1\) per Dirac field of the antiperiodic cone value, which enters the area side only. The identification of that gap with \(4\kappa_X\),",
r"The first identity is the decomposition of the paragraph on fermion replica gluing, the weight of \(\rho^2X\) plus the excess \(+1\) per Dirac field. The identification of the fixed-state gap with \(4\kappa_X\),"))
# m1: Donnelly-Wall apposition on the n<1 value only
R.append(("m1",
r"the vector holonomy contact of modulus \(1\), the edge-mode value of~\cite{DonnellyWall2016} for a Maxwell field if the state carries that sector, changes it to \(1\) on \(n<1\) and \(3\) on \(n>1\)",
r"the vector holonomy contact of modulus \(1\) changes it to \(1\) on \(n<1\), the value \(-1\) being that of the edge-mode term of~\cite{DonnellyWall2016} for a Maxwell field if the state carries that sector (an input, not a prescription of this class), and to \(3\) on \(n>1\)"))
# m2: log-order clause
R.append(("m2",
r"The coefficient of \(W\) at logarithmic order has the same pattern, with gaps \(0\), \(2\), \(0\) for the periodic, fixed-state and completed replicas and \(\kappa_C^T=0\); and since \(\mathcal S_4\) is quartic in \(b_\sigma\), the logarithmic coefficient of the induced action stated in the paragraph on the next order has no quadratic form about a constant \(\bar\Theta\).",
r"About a constant self-dual or anti-self-dual \(\bar\Theta\), on the \(n<1\) branch, the coefficient of \(W\) at logarithmic order has the gaps \(0\), \(2\), \(0\) for the periodic, fixed-state and completed replicas, with \(\kappa_C^T=0\); the first two repeat the values of order \(\LUV^2\), and the completed gap has no counterpart of the same form at that order. Since \(\mathcal S_4\) is quartic in \(b_\sigma\), the logarithmic coefficient of the induced action stated in the paragraph on the next order vanishes at quadratic order about a constant \(\bar\Theta\), given the sampled-jet identity of that paragraph."))
# M2: hypotheses of the Tr rho^n identification
R.append(("M2",
r"for the trace of \(\rho^n\) of the paragraph on fermion replica gluing \(1/G_A=\LUV^2/\pi\) while \(1/G_T=0\)",
r"for the fixed-state replica, which is the trace of \(\rho^n\) only under the hypotheses of the paragraph on fermion replica gluing (a quasi-free state of the Poisson-limit fermions with rotational modular flow, the less singular extension and a unique continuation from integer \(n\)), \(1/G_A=\LUV^2/\pi\) while \(1/G_T=0\)"))
# M1, m3: product backgrounds
R.append(("M1/m3",
r"At this content the comparison of \(G_A\) with \(G_T\) is thus not vacuous only in a class with a split spectrum, where it reduces to the two sums \(\mathsf S_n\) and \(\mathsf S_\kappa\). Whether the Kaluza--Klein towers of fuzzy extra dimensions, for which~\cite{Steinacker2023} attributes the Einstein--Hilbert term to a mixed quartic term and not to a mass shift of \(a_1\), give sums of this form is not examined.",
r"For this formal shift the comparison at this content is thus not vacuous only for a split spectrum, where it reduces to the two sums \(\mathsf S_n\) and \(\mathsf S_\kappa\). The product backgrounds \(M\times K\) of the paragraph on product backgrounds in Section~\ref{sec:status-F} are not of this form: there the scalar operator of \(K\) is common to all species, the term that would carry \(\mathsf S_\kappa\) has no two-derivative part, and the comparison is \(c_T=\tfrac16W_R-4W_X\) against \(c_A^{\mathrm{per}}=\tfrac16W_R\), with \(W_X\) from the mixed term, which that paragraph relates to a term of Section~6.2 of~\cite{Steinacker2023}, so that \(W_R\) and \(W_X\) take the places of \(\mathsf S_n\) and \(\mathsf S_\kappa\) and the periodic gap \(4W_X\) is nonzero for a nonzero flux of \(K\); the fixed-state replica there keeps the value \(c_A=2\) of this content for each matrix mode of \(K\) at order \(\LUV^2\), with cutoff-dependent terms whose finite remainders are not computed there. Those statements are for the Poisson limit on \(M\), one loop, the operators of that paragraph, which contain no cubic or mass term on \(K\), a fuzzy space \(K\) that is not constructed and not required to solve the equations of motion, product backgrounds without mixed flux, the orientation-even part of the mixed term and the replicas of this section, and they fix no sign of \(W_R\). The paragraphs that follow it there, on the conjugate-coordinate class times a fuzzy factor, are not used here."))
# closing scope sentence
R.append(("scope",
r"do not treat finite terms, Moyal corrections, more than four matrix coordinates or a Kaluza--Klein tower, use",
r"do not treat finite terms or Moyal corrections, compute no Kaluza--Klein tower and add nothing to the statements quoted from Section~\ref{sec:status-F}, use"))
ok = True
for tag, old, new in R:
    c = t.count(old)
    print(tag, "occurrences of replaced text:", c)
    ok &= c == 1
    t = t.replace(old, new)
(here/'appH_insert_r2.tex').write_bytes(t.encode('utf-8'))
print("r2 insert bytes (LF):", len(t.encode('utf-8')))
print("MAKE R2 PASS" if ok else "MAKE R2 FAIL")
