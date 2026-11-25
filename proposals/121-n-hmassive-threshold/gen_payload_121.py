# gen_payload_121.py - generates insert-n-hmassive-threshold.tex (CRLF) and
# verifies splice hygiene against the LIVE appH file. Deterministic.
# Run: python -I gen_payload_121.py    (prints <= 20 lines, ends GEN121 OK)
import hashlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
APP = os.path.join(REPO, 'chapters', 'appH-microscopic-proofs.tex')

PAYLOAD = r'''\paragraph{Mass-resummed thresholds in the spin-two factor
(conditional; not closure).}
Assume the hypotheses of the recorded block bookkeeping paragraph of
Section~\ref{sec:status-F}: sixteen decoupled real components of
\(\mathcal O_H=-\nabla^2+E\) with \(E=m^2+Q R_E\),
\(m^2=\lambda v^2\) from Equations~\eqref{eq:Smicro} and~\eqref{eq:V},
constant \(Q\). From Equations~\eqref{eq:appA-a1}--\eqref{eq:appA-a2}
the per-component curvature-squared coefficients are \(1/120\) for
\(C^2\) and \(\tfrac12(1/6-Q)^2\) for \(R^2\), and the
curvature-linear part of \(a_2\) is \(-m^2(1/6-Q)R\), consistently
with the recorded block data; the \(C^2\) coefficient is independent
of \(m^2\) and \(Q\). At curvature-squared order the
proper-time windows of Equation~\eqref{eq:appA-Wexp} replace
\(L=\ln(\LUV^2/\mu^2)\) in the block coefficients \(c_W\), \(c_R\) by
\(L_m:=E_1(m^2/\LUV^2)-E_1(m^2/\mu^2)\), with \(E_1\) the
exponential integral defined in Section~\ref{sec:status-F}, and the
curvature \(a_1\) window is \((1/6-Q)J(m^2;\LUV^{-2},\mu^{-2})\) with
the recorded threshold \(J\). Write \(y:=m^2/\LUV^2\). Then, for one
block with \(Q=0\) and \(\mu\ll m\),
\(\Upsilon=\mathcal A_1/(2\mathcal W_C)\) becomes
\(\Upsilon_H=10[e^{-y}-yE_1(y)]\): the recorded \(\Upsilon=10\)
universality of minimally coupled massless scalars is the \(y\to0\)
limit; \(\Upsilon_H\) decreases monotonically to zero as \(y\) grows;
and at \(Q=1/6\) the curvature \(a_1\) and \(R^2\) windows of this
block vanish, so its windowed contribution to \(1/G_{\mathrm{eff}}\) and to
the \(a_1\)-numerator of \(\Upsilon\) is zero at this order, while its
\(C^2\) coefficient remains in \(\mathcal W_C\). The fixed-window spin-two
pole estimate
\(|m_2|^2=\Upsilon_H\LUV^2/L_m\) (the recorded
\(-\Upsilon\LUV^2/L\) with windows) satisfies, for \(\mu\ll m\),
\(|m_2|^2/\LUV^2=10[e^{-y}/E_1(y)-y]\), which increases
monotonically from \(0\) and equals \(1\) at
\(y=e^{-(10+\gamma_{\mathrm E})}(1+O(10^{-2}))\): the estimate lies
below \(\LUV\) only in that narrow band. The momentum-dependent
window \(\ell(x;y):=\int_0^1\mathrm{d}\tau\,
E_1(y+\tau(1-\tau)x)\), whose \(\mu\)-window term is negligible for
\(\mu\ll m,k\), replaces \(\ln(1/x)+\delta_W\) in the spin-two
factor: at \(y\to0\) it reproduces the recorded model value
\(\ln(1/x)+2-\gamma_{\mathrm E}\), while for \(\mu\ll k\ll m\) it is
\(\ln(\LUV^2/m^2)-\gamma_{\mathrm E}+O(k^2/m^2)\), so this block's
contribution to the running freezes between \(\mu\) and \(m\). For
every \(y>0\) the window \(\ell(\cdot;y)\) has a branch cut on the
negative real axis starting at \(x=-4y\), across which its boundary
values differ and toward whose endpoint it grows logarithmically;
the boundary remainder-bound argument of the two preceding paragraphs
therefore does not apply on the full slit-disc boundary once
\(m>0\), and the recorded zero-free-window statements are statements
of the massless sector. Hypotheses and limits: the Presentation~B
operator and \(Q\) assignment, one block without the other sectors,
weights, gauge fixing or the ghosts, the leading-logarithmic
fixed-window class of this ledger entry, \(\mu\ll m,k\ll\LUV\), and
window substitutions not derived from the matrix path integral; the
local finite counterterm of Theorem~\ref{thm:Geff} is not fixed here,
the fixed-window pole estimate is not shown to coincide with a zero
of the momentum-dependent factor, no \(\mathcal W_C\),
\(\mathcal A_1\), \(G_{\mathrm{eff}}\) or \(\delta_W\) is computed
for the locked block, no zero-free region or ghost-freedom statement
is made for any massive sector, and no status label is changed; the
ledger entries of Problems~F and~N are unchanged and both stay OPEN.
'''

def to_bytes(txt):
    return txt.replace('\r\n', '\n').replace('\n', '\r\n').encode('ascii')

def hygiene_ok(b):
    if not b.endswith(b'\r\n'): return 'no-final-CRLF'
    if b'\n' in b.replace(b'\r\n', b''): return 'bare-LF'
    if b'$' in b: return 'dollar'
    for tok in (b'\\label', b'\\cite', b'\\begin', b'\\end{'):
        if tok in b: return 'tok:' + tok.decode()
    if b.decode('ascii', 'ignore') != b.decode('latin-1'): return 'nonascii'
    import re
    BS = chr(92).encode()
    toks = re.findall(BS + BS + b'(?:eq)?ref' + BS + b'{([^}]*)}', b)
    toks += re.findall(BS + BS + b'autoref' + BS + b'{([^}]*)}', b)
    wl = {b'thm:Geff', b'eq:appA-a1', b'eq:appA-a2', b'eq:appA-scalar',
          b'eq:appA-Wexp', b'eq:O-eta', b'eq:V', b'eq:Smicro',
          b'ass:emergent-op', b'sec:status-N', b'sec:status-F', b'eq:LUV-def'}
    for t in toks:
        if t not in wl: return 'ref:' + t.decode()
    if b'ref' not in b: return 'norefs'
    return None

def main():
    pb = to_bytes(PAYLOAD)
    fail = hygiene_ok(pb)
    print('hygiene payload:', 'OK' if fail is None else fail)
    if fail: raise SystemExit('HYGIENE-FAIL ' + str(fail))
    # positive controls: guards must FIRE on injected defects (item-117 lesson)
    controls = [pb.replace(b'Upsilon_H', b'\\label{x}Upsilon_H', 1),
                pb.replace(b'\\LUV', b'$\\LUV$', 1),
                (pb[:-2] if pb.endswith(b'\r\n') else pb),
                pb.replace(b'\\paragraph', b'\\begin{x}', 1),
                pb.replace(b'sec:status-F', b'sec:nope-Z', 1)]
    fired = [hygiene_ok(c) is not None for c in controls]
    print('controls fired:', fired)
    if not all(fired): raise SystemExit('CONTROL-FAIL')
    p = os.path.join(HERE, 'insert-n-hmassive-threshold.tex')
    open(p, 'wb').write(pb)
    print('payload bytes:', len(pb), 'sha1:', hashlib.sha1(pb).hexdigest()[:12])
    # splice against live appH (memory only)
    t = open(APP, 'rb').read()
    anchor = b'Problems~F and~N remain open.'
    n = t.count(anchor)
    print('anchor count:', n)
    if n != 1: raise SystemExit('ANCHOR-COUNT ' + str(n))
    old = len(t)
    new = t.replace(anchor + b'\r\n\r\n', anchor + b'\r\n\r\n' + pb + b'\r\n', 1)
    print('PRE bytes:', old, 'POST bytes:', len(new),
          'delta:', len(new) - old, '=', len(pb) + 2, ':',
          len(new) - old == len(pb) + 2)
    sp = os.path.join(HERE, 'appH-spliced-preview.tex')
    open(sp, 'wb').write(new)
    print('sha1 spliced:', hashlib.sha1(new).hexdigest()[:12])
    print('GEN121 OK')

main()
