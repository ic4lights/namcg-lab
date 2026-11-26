"""Builds appH_insert.tex (r2) from appH_insert_r1.tex by applying review snippets A-G verbatim; asserts each OLD string occurs once."""
s = open('appH_insert_r1.tex', encoding='utf-8').read()


def rep(s, a, b):
    assert s.count(a) == 1, (s.count(a), a[:70])
    return s.replace(a, b)


def span(s, start, end, new):
    assert s.count(start) == 1 and s.count(end) == 1, (s.count(start), s.count(end), start[:50])
    i = s.index(start)
    j = s.index(end) + len(end)
    assert j > i
    return s[:i] + new + s[j:]


lines = s.split('\n')
assert all(l.startswith('%%') for l in lines[:4])
s = '\n'.join(lines[4:]).lstrip('\n')

A = r"""That Hessian equals \(2\mathsf M_G+b\,\mathsf E\) at six sampled rational points, in exact arithmetic and for both signatures (not proved for general \(\omega\)): \(\mathsf M_G\) is the quadratic form \(\rho\,G^{\mu\rho}G^{\nu\sigma}F_{\mu\nu}F_{\rho\sigma}\), \(\mathsf E\) the quadratic form \(2\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\) with \(\epsilon^{0123}=1\), and \(b=-\operatorname{sgn}(\operatorname{Pf}\Theta)\,\eta_{ac}\eta_{bd}\Theta^{ab}\Theta^{cd}/8\), so that the quadratic action is \(\rho\,G^{\mu\rho}G^{\nu\sigma}F_{\mu\nu}F_{\rho\sigma}+b\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\) up to the term proportional to \(\mathfrak J\). Apart from that term, the connection sector is a Maxwell field of the metric \(G\) with weight \(\rho\), coupled to the pseudoscalar \(\vartheta=\rho b\) through \(b\,\epsilon FF\); the variables \((G,\rho,\vartheta)\) are not the variables \((G,\rho,b)\) of the paragraph on the order \(\Lambda^2\), and the axial torsion is not the dual of \(\partial\vartheta\) (tested, residual \(0.3\)-\(1.0\));"""
s = span(s, r'That Hessian is, exactly', r'through \(b\,\epsilon FF\);', A)

B = r"""At sampled jets with \(\mathfrak J=0\) and \(\partial\mathfrak J=0\) (numerical: six draws, both signatures, first-order coefficients to \(10^{-15}\), both vanishing at zeroth order) the operator \(S\mathcal O_vS^{-1}\), \((Sa)_\nu=a^\mu\omega_{\mu\nu}\), has the same principal, first-order and zeroth-order coefficients as the Maxwell--axion operator in the \(\rho\)-weighted Lorenz gauge; along a one-parameter family leaving \(\mathfrak J=0\) the first- and zeroth-order differences grow linearly with the parameter."""
s = span(s, r'At points with \(\mathfrak J=0\) and \(\partial\mathfrak J=0\) the operator', r'the mismatch is linear in \(\mathfrak J\) and \(\partial\mathfrak J\).', B)

C = r"""About the sampled generic constant \(\bar\omega\) (twelve draws, both signatures) the only first-order rotation that keeps \(\eta_{AB}e^B{}_\mu\) antisymmetric, a necessary condition for \(e\) to come from a two-form, is \(\lambda=0\); the Goldstone-extremised rotation of the preceding paragraph therefore does not satisfy this condition at those backgrounds. This was not tested for (anti-)self-dual \(\bar\omega\)."""
s = span(s, r'About a generic constant \(\bar\omega\)', r'(twelve draws, both signatures).', C)

s = rep(s, r'This is a covariance under diffeomorphisms of the chart acting on \((G,\rho,\vartheta)\); it is not a local Lorentz symmetry of the matrix index.',
        r'This is covariance of the operator under changes of the coordinates \(y\) when \(G\), \(\rho\) and \(\vartheta\) are treated as tensor fields. These fields are built from \(\omega\) with the constant \(\eta\) contracted with the matrix index, which is the coordinate index, so it is not a symmetry of the matrix action under independent chart diffeomorphisms, and it is not a local Lorentz symmetry of the matrix index.')

s = rep(s, r'For the Maxwell--axion operator, \(a_1=\operatorname{tr}(E+R_G/6)\) is',
        r'For the Maxwell--axion operator the coefficient \(a_1\), in the normalisation in which \(\sqrt{\lvert G\rvert}\,a_1(\mathcal O_v)=\tfrac46\rho R[g_\rho]+\rho^2X\), is')

D2 = r"""(the Hodge operator with the dilaton term \(V\) and the axion term; the dilaton part is derived analytically, and the axion term is checked at generic jets, ratio \(1\) to six digits, both signatures). On fourteen random jets per signature with \(\mathfrak J=\partial\mathfrak J=0\) it equals \(a_1(\mathcal O_v)\) to \(3\times10^{-11}\), and \(\sqrt{\lvert G\rvert}\,a_1(\mathcal O_v)=\tfrac46\rho R[g_\rho]+\rho^2X\). With \(\rho R[g_\rho]=\rho^2(R_G+3\Box_G\ln\rho-\tfrac32\lvert V\rvert_G^2)\) this gives, on those jets,"""
s = span(s, r'(the Hodge operator with the dilaton term', r'this gives, on the stationary set,', D2)

s = rep(s, r'On the same jets the invariants satisfy exactly one linear relation (rank five of six),',
        r'On the same jets the six invariants satisfy one linear relation to numerical accuracy (rank five of six),')
s = rep(s, r'(residual \(6\times10^{-12}\)), so that on the stationary set also \(X=-4R_G+6\lvert V\rvert_G^2-10\Box_G\ln\rho\).',
        r'(residual \(6\times10^{-12}\); numerical, not proved), so that on those jets also \(X=-4R_G+6\lvert V\rvert_G^2-10\Box_G\ln\rho\).')

s = rep(s, r'whose operator \(\gamma^AD_A\) is the frame derivative \(\gamma^Ae_A{}^\nu\partial_\nu\) without spin connection and is not shown to have a covariant form',
        r'whose Dirac operator \(\gamma^\mu D_\mu\), the Poisson limit of \(\Gamma^\mu[\hat X_\mu,\Psi]\), is a frame derivative without a spin-connection term and is not shown to have a covariant form')
s = rep(s, 'They do not cover the Dirac sector', 'The Hessian, operator and stationary-set identities are numerical at the sampled points stated. They do not cover the Dirac sector')

G = r"""Let \(C_{31}^{\mathrm{tot}}\) be as above and let \(H_V^{0}=H_V-\mu^2\) denote the operator without the mass term. The exact relation of the paragraph on the Casimir of \(\mathfrak{so}(4,2)\), \(H_V=C_G-C_{41}-C_\Sigma+\mu^2\), with \(C_G=C_{31}^{\mathrm{tot}}\) and \(C_\Sigma=C_V=-3\), reads \(H_V^{0}=-C_{41}+C_{31}^{\mathrm{tot}}+3\) (re-checked on random polynomial fields; the other sign of \(R^{ab}\) and the opposite sign of the Zeeman term give no such identity)."""
s = span(s, 'In exact polynomial arithmetic (random polynomial fields)', 'giving no such identity.', G)
s = rep(s, r'on \(y^\mu\) is not the absence of a connection.', r'on \(y^\mu\) is not the absence of a connection, but the dependence of the induced form on the base point.')
s = rep(s, r'and they are the points where the preceding paragraphs find \(f_1=f_2\).', r'and they are the points where the preceding paragraphs find \(f_1=f_2\) in that case.')

open('appH_insert.tex', 'w', encoding='utf-8', newline='\n').write(s)
b = s.encode()
body = '\n'.join(l for l in s.split('\n') if not l.startswith('%'))
print('bytes', len(b), 'TAB', b.count(b'\t'), 'CR', b.count(b'\r'), 'nonascii', sum(x > 127 for x in b), 'ctrl', sum(1 for x in b if x < 32 and x != 10))
print('braces net', body.count('{') - body.count('}'), 'paren net', body.count('\\(') - body.count('\\)'), 'bracket', body.count('\\['), body.count('\\]'))
print('comment lines left:', [l for l in s.split('\n') if l.startswith('%')])
c = open('../../chapters/appH-microscopic-proofs.tex', encoding='utf-8').read().replace('\r\n', '\n')
old = "It stays undetermined until the frame is dragged by a flow whose internal part is a local symmetry, that is until the question of local frame rotations (Problem~D) is settled."
print('OLD(a) count', c.count(old), 'anchors', c.count('\\section{Problem C: conformal mode and Cassini}'), c.count('\\section{Problem G: HBEV}'))
