"""060: replace the equation numbers of 2605.13294 by those of the arXiv v2 PDF ((88), (89), (100))."""
p = 'appH_insert.tex'
s = open(p, encoding='utf-8').read()
reps = [
    (r"and coupling \(g_{\mathrm{YM}}^2=1/\rho^2\) of~\cite{Steinacker2026Weak}, the coupling",
     r"and coupling \(g_{\mathrm{YM}}^2=1/\rho^2\) of~\cite{Steinacker2026Weak} (its Eqs.~(88) and~(89)), the coupling"),
    (r"the dependence \(1/\sinh^3\tau\) of its Eq.~(104), now", r"the dependence \(1/\sinh^3\tau\) of its Eq.~(89), now"),
    (r"at late \(\tau\) (its Eq.~(115))", r"at late \(\tau\) (its Eq.~(100))"),
]
for a, b in reps:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print(len(s.encode('utf-8')))
