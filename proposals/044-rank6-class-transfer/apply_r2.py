"""apply_r2.py (044): apply exactly the gatekeeper's r1 corrected snippets to appH_insert.tex (r1 saved as appH_insert_r1.tex)."""
p='appH_insert.tex'
s=open(p,encoding='utf-8').read()
R=[
(r"(conditional; bounded no-go)", r"(conditional; not closure)"),
(r"and for the fixed-state replica a cutoff-dependent term of order \(\LUV^2\) plus the finite part \(2W_X\): for \(W_X\neq0\) the periodic gap does not vanish and the smooth one vanishes only for \(W_R=16W_X\), a condition on \(K\).",
 r"and for the fixed-state replica cutoff-dependent terms from the first term (the order \(\LUV^2\) term and a logarithmic term proportional to the trace of \(H_0^K\), whose finite remainders are not computed) plus the part \(2W_X\) from the mixed term. For \(W_X\neq0\) the periodic gap does not vanish, and the smooth gap vanishes only if \(W_R=16W_X\), a condition on \(K\)."),
(r"The finite part \(2W_X\) of the fixed-state gap is the axial-torsion part of the Dirac index density on the tensor modes;",
 r"The part \(2W_X\) of the fixed-state gap that comes from the mixed term is the axial-torsion part of the Dirac index density on the tensor modes;"),
(r"the finite gap would vanish for tensor modes that source neither the axial nor the vector torsion at first order.",
 r"the mixed-term part of the gap would vanish for tensor modes that source neither the axial nor the vector torsion at first order. This is the case for the dressed density of the paragraph on local frame rotations (an input of Assumption~\ref{ass:local-lorentz}, not derived), which sets \(S=0\) and gives \(c_T^{\mathrm{ext}}=\tfrac16W_R-2W_X\), equal to the mixed-term part of the fixed-state \(c_A\)."),
(r"(p\cdot g^{-1}p)(p\cdot Kp)", r"(p\cdot g^{-1}p)(p\cdot\mathsf Kp)"),
(r"The two forms are not proportional, so for a nonzero flux of \(K\) no single \(G_T\) covers the transverse polarisations at the frozen-coefficient leading symbol.",
 r"The fourth-order term is the product of the symbol \(p\cdot g^{-1}p\) of the induced d'Alembertian and the tree-level kinetic symbol \(p\cdot\mathsf K p\) of \(\phi\), with \(\mathsf K=\theta^{T}g\theta\) the kinetic tensor; at this order it can be moved by a local redefinition of \(\phi\) and vanishes on the tree-level mass shell. The part of second order in \(p\), which is nonzero in the same check, is not compared with the Einstein--Hilbert form of \(\hat g\), so a common \(G_T\) on the transverse polarisations is neither established nor excluded."),
(r"The coefficient that~\cite{Steinacker2023} identifies with the inverse Newton constant corresponds to its part \(-2W_X\);",
 r"The coefficient that~\cite{Steinacker2023} identifies with the inverse Newton constant corresponds structurally to its part \(-2W_X\) (the same mixed term; the normalisations and the sign convention are not compared, and there the axial torsion is the axion);"),
(r"that is \(T^a\) and \(y^\mu\) here up to normalisation;",
 r"the bundle structure and the generator definitions agree with those of the conjugate-coordinate class here up to normalisation, the assignment of the two families to the matrices and the base functions following Section~7 of~\cite{Steinacker2023};"),
(r"the axial part of the torsion is also nonzero on the on-shell null mode with \(\delta\rho=0\) of the Lorentzian section.",
 r"the axial part of the torsion is also nonzero as a tensor on the on-shell null mode with \(\delta\rho=0\) of the Lorentzian section, although its quadratic invariants vanish on a single null wave."),
(r"the content stated,", r"the content stated, a fuzzy space \(K\) that is not required to solve the equations of motion,"),
(r"and, for the transverse modes, frozen coefficients.", r"and, for the transverse-mode check, frozen coefficients at one background point."),
]
for a,b in R:
    n=s.count(a); assert n==1,(n,a[:70]); s=s.replace(a,b)
open(p,'w',newline='\n',encoding='utf-8').write(s)
b=s.encode()
print('bytes',len(b),'TAB',b.count(b'\t'),'CR',b.count(b'\r'),'nonASCII',sum(c>127 for c in b),'ctrl',sum((c<32 and c!=10) for c in b))
print('braces',s.count('{')-s.count('}'),'inline',s.count('\(')-s.count('\)'),'display',s.count('\[')-s.count('\]'))
