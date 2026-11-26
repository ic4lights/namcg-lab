import os
here=os.path.dirname(os.path.abspath(__file__))
t=open(os.path.join(here,'block-r1.tex'),encoding='utf8',newline='').read().replace('\r\n','\n')
def rep(a,b):
    global t
    assert t.count(a)==1,a[:60]; t=t.replace(a,b)
rep(r"and the term linear in the masses is \(-M_{\mathrm{str}}\operatorname{Tr}[\chi\,\Phi'(H_X)]\) with",
    r"and the term linear in the masses and without insertions of \(\mathcal Z_{ab}\) is \(+M_{\mathrm{str}}\operatorname{Tr}[\chi\,\Phi'(H_X)]\) (for \(\Phi=e^{-(\cdot)}\) this is \(-M_{\mathrm{str}}\operatorname{Tr}[\chi\,e^{-H_X}]\)) with")
rep(r"At the leading symbol that term is \(-M_{\mathrm{str}}\int\chi\,(\sigma_X-\mathrm i0)^{-1}\) with",
    r"At the leading symbol that term is proportional to \(M_{\mathrm{str}}\int\chi\,(\sigma_X-\mathrm i0)^{-1}\) with")
i=t.index("Its second variation therefore contains"); j=t.index("(iii) A term of Einstein")
new=(r"This leading-symbol term depends on \(A\) only through its first derivatives, so its second variation contains no second derivative of the fluctuation and no term of Einstein--Hilbert form; the next-to-leading symbol, which involves the second jet of \(X\), is not computed. With the Gaussian window of \(\Delta_{3/4}\) the Hessian of the real (principal-value) part of this moment along \(\alpha\), at frozen coefficients and \(\phi=\pi/2\), was evaluated numerically in \(59\) random draws of orbit point and \(q\): it is indefinite in \(40\), positive definite in \(5\) and negative definite in \(14\), and along \(\alpha^a\propto q^a\) it is numerically nonzero in all draws with non-null \(q\). ")
t=t[:i]+new+t[j:]
rep(r"the dependence on \(A\) of the flux enters the leading symbol only through \(F_{ab}(\xi)\to F^0_{ab}(\xi)+\epsilon\,c\,(\xi\cdot Y_q)(q_a\alpha_b-q_b\alpha_a)\), \(c=-s\,y^4\cos\phi\), at the leading order in \(q\), and its Gaussian averages depend on \(q\cdot y\) at fixed \(q\cdot q\)",
    r"at the phase \(\phi=0\), where the first-jet terms vanish, and at the leading order in \(q\), the flux in the leading symbol is shifted as \(F_{ab}(\xi)\to F^0_{ab}(\xi)+\epsilon\,c\,(\xi\cdot Y_q)(q_a\alpha_b-q_b\alpha_a)\), \(c=-s\,y^4\cos\phi\), and at fixed proper time and \(\kappa=\tfrac34\) the Gaussian averages in the integrand depend on \(q\cdot y\) at fixed \(q\cdot q\), through the vector \(y^\mu\) and the window")
rep(r"; this term is not Lorentz invariant, through the vector \(y^\mu\) and the background flux. (iv)",
    r"; its integrand is therefore not Lorentz invariant (the window and the leaf both single out \(y^\mu\), and this diagnostic does not separate them). (iv)")
open(os.path.join(here,'block-r2.tex'),'w',encoding='utf8',newline='').write(t)
print(len(t))
