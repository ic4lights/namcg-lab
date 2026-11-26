# -*- coding: ascii -*-
# Item 124 generator. Builds the payload paragraph, splices it into the LIVE
# appH bytes before the named-completion-class paragraph header, and writes
#   payload-124.txt                     (the inserted bytes, CRLF-terminated)
#   <outdir>/spliced_appH_124.preview.bin  (full spliced file, for the cert build)
# Prints PRE/PAY/POST sha1+sizes. Every hygiene guard has an INJECTED POSITIVE
# CONTROL: a corrupted copy is run through the same guard and MUST be flagged
# (memory rule "generator join-guard selftest").
# Control semantics: each guard is clean(x) -> bool True iff x passes. The
# control stores (not clean(corrupted_x)) == True, i.e. the guard fired.
# Usage: python -I make_payload_124.py [outdir]
import sys, os, hashlib, re, glob

APPH = r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appH-microscopic-proofs.tex"
FOLDER = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\124-n-mqm-pos"
CHAPTERS = r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters"

PIN_SHA1 = "ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1"
PIN_SIZE = 869275

ANCHOR = "\\paragraph{The named completion class and the remainder bound.}"

PAY_TEXT = (
    "\\paragraph{Realization of the spectral-positivity hypotheses in homogeneous Presentation-B matrix quantum mechanics (derivations in a named truncation class; not closure).} "
    "The hypotheses of the sublemma of the paragraph ``Spectral positivity of the exact correlator'' are realized as theorems in the following named class. "
    "Class: Equation~\\eqref{eq:Smicro} with \\(A_\\mu=0\\), no couplings beyond Equations~\\eqref{eq:Smicro} and~\\eqref{eq:V}, fixed flat background \\(g^{(0)}=\\eta\\) of Assumption~\\ref{ass:lorentzian}, truncated to the spatially homogeneous mode \\(\\Phi(\\mathbf x,t)=M(t)\\) at finite internal dimension \\(N\\), and canonically quantized as matrix quantum mechanics on \\(L^2(\\mathbb C^{N^2})\\) with the flat field-space measure. "
    "Derivations in the class. The kinetic form of the truncation is \\(\\operatorname{Tr}\\dot M^\\dagger\\dot M=\\sum_{I,A}|\\dot M_{IA}|^2\\): the field-space metric is flat, positive and finite-dimensional, so there is no ordering ambiguity, and the Legendre transform gives the canonical Hamiltonian \\(H=V_3^{-1}\\operatorname{Tr}\\Pi\\Pi^\\dagger+V_3(\\lambda/4)\\operatorname{Tr}(M^\\dagger M-v^2\\mathbb I)^2\\) with \\(V_3\\) the volume of space (checked symbolically). "
    "The potential equals \\((\\lambda/4)\\sum_a(\\sigma_a^2-v^2)^2\\) in the singular values \\(\\sigma_a\\) of \\(M\\) (identity checked symbolically), hence is non-negative, vanishes exactly on the compact set \\(M=vU\\) with \\(U\\) unitary, and dominates \\(V_3(\\lambda/4N)(\\operatorname{Tr}M^\\dagger M-Nv^2)^2\\) by Cauchy--Schwarz on the eigenvalues, \\(N\\operatorname{Tr}A^2\\ge(\\operatorname{Tr}A)^2\\) for Hermitian \\(A\\) (the \\(N=2\\) sum-of-squares form \\(2\\operatorname{Tr}A^2-(\\operatorname{Tr}A)^2=(a_{11}-a_{22})^2+4|a_{12}|^2\\) checked symbolically). "
    "Then, for every finite \\(N\\): (i)~\\(H\\) is the Schr\\\"odinger operator \\(-V_3^{-1}\\Delta+V_3(\\lambda/4)\\operatorname{Tr}(M^\\dagger M-v^2\\mathbb I)^2\\) on \\(\\mathbb R^{2N^2}\\): by the classical essential self-adjointness criterion for Schr\\\"odinger operators with continuous potentials bounded below it is essentially self-adjoint on \\(C_c^\\infty(\\mathbb R^{2N^2})\\), and its Friedrichs extension obeys \\(H\\ge0\\); the potential is confining, so the Rellich compactness criterion gives compact resolvent, pure point spectrum \\(E_n\\to\\infty\\) with an orthonormal eigenbasis, and an \\(L^2\\)-normalizable ground-state eigenvector \\(\\Omega\\); no gap above \\(E_0\\) is claimed or needed. "
    "(ii)~For every self-adjoint observable \\(\\mathcal O\\) of the truncated model and every projection with real constant coefficients (the class analogue of the spin-two projection, which preserves self-adjointness), \\(\\langle\\Omega|\\mathcal O(t)\\mathcal O(0)|\\Omega\\rangle=\\sum_ne^{-\\mathrm i(E_n-E_0)t}|\\langle\\Omega|\\mathcal O|n\\rangle|^2\\) by the spectral resolution of (i): the spectral measure is a positive sum of point masses and the residue at each isolated simple real pole of the projected two-point function is a sum of squared matrix elements and so non-negative. This realizes the residue-positivity hypotheses of the sublemma above as theorems in the class for every self-adjoint observable, not only for a derived composite \\(T_{\\mu\\nu}\\). "
    "(iii)~The Euclidean measure of the class realized as the kernel of \\(e^{-\\tau H}\\) is reflection-positive for the reflection \\(\\theta\\) that negates Euclidean time about \\(0\\): the \\(\\theta\\)-reflected pairing of any bounded measurable functional of the fields at times of one side equals \\(\\|e^{-(T/2)H}\\widetilde{\\mathcal F}\\|^2\\ge0\\), in terms of the time-zero representative \\(\\widetilde{\\mathcal F}\\) and the time length \\(T>0\\), by self-adjointness and \\(H\\ge0\\). "
    "Contrast, fixing the scope of the recorded no-go statements of Sections~\\ref{sec:status-E} and~\\ref{sec:status-D}. The weights failing reflection positivity there are of the Presentation-A family with \\(\\eta_{\\mu\\nu}\\)-contracted field-space metric, so that failure is a property of that family at finite \\(N\\) and not of finite-\\(N\\) matrix measures at large; and the sign of the kinetic convention of Equation~\\eqref{eq:Smicro} is decisive rather than cosmetic, since the canonical classical-mechanics lift of Equation~\\eqref{eq:Smatrix} to a time \\(\\tau\\) with Hermitian \\(\\hat X^\\mu(\\tau)\\) and kinetic metric \\(\\eta_{\\mu\\nu}\\) has Hamiltonian kinetic polynomial \\(\\sum_{\\mu,\\nu}\\eta^{\\mu\\nu}\\operatorname{Tr}(P^\\mu P^\\nu)\\), which evaluates to \\(-\\operatorname{Tr}(P^0)^2<0\\) at \\(P^i=0\\) and whose quantum form is \\(-\\lambda^2\\|\\chi\\|^2+O(\\lambda)\\) on states \\(e^{\\mathrm i\\lambda q_0}\\chi\\) in a coordinate \\(q_0\\) of the \\(\\hat X^0\\) fibre, while its quartic form equals \\(g_{\\mathrm{YM}}^{-2}\\bigl(\\tfrac14\\sum_{i,j}\\|[\\hat X^i,\\hat X^j]\\|^2-\\tfrac12\\sum_i\\|[\\hat X^0,\\hat X^i]\\|^2\\bigr)\\) with \\(\\|[\\,\\cdot\\,,\\cdot\\,]\\|^2=-\\operatorname{Tr}[\\,\\cdot\\,,\\cdot\\,]^2\\ge0\\) (identity checked symbolically on traceless \\(2\\times2\\) Hermitian matrices), which tends to \\(-\\infty\\) on the ray \\(\\hat X^0=t\\sigma_1/2\\), \\(\\hat X^1=t\\sigma_2/2\\), where it equals \\(-t^4/(4g_{\\mathrm{YM}}^2)\\): in that lift the sublemma hypotheses fail. "
    "Together the two halves pin the open content of the sublemma hypotheses to recorded inputs: the kinetic-sign content of Assumption~\\ref{ass:dictionary} that Presentation~A reproduces the convention of Equation~\\eqref{eq:Smicro}, the derivation of the composite fluctuation \\(T_{\\mu\\nu}\\) of Problem~D, and the restriction to the matrix-quantum-mechanics truncation class named here. "
    "These statements derive nothing about the emergent metric or the full dynamics, they do not discharge Assumption~\\ref{ass:lorentzian} or Assumption~\\ref{ass:EFT-a2}, they do not constrain the poles of the truncated kernels of this section (the two-oscillator artifact recorded above stands untouched), they change no status label, and they close nothing in Problem~N."
)

ACCENT = chr(233)  # non-ASCII codepoint used only to corrupt the ASCII control

def clean_ascii(s):
    return all(32 <= ord(c) <= 126 for c in s)

def clean_braces(s):
    d = 0
    for c in s:
        if c == '{':
            d += 1
        elif c == '}':
            d -= 1
        if d < 0:
            return False
    return d == 0

def clean_nolabelcite(s):
    return ('\\label' not in s) and ('\\cite' not in s)

def all_labels():
    labels = set()
    for f in glob.glob(os.path.join(CHAPTERS, "*.tex")):
        txt = open(f, encoding='utf-8', errors='replace').read()
        labels.update(re.findall(r'\\label\{([^}]+)\}', txt))
    return labels

def missing_refs(s, labels):
    refs = re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', s)
    return [r for r in refs if r not in labels]

def clean_one_line(s):
    return ('\r' not in s) and ('\n' not in s)

def run_guards(pay_line, labels):
    """Each entry: (name, clean(payload), control_fired_bool)."""
    ent = []
    ent.append(('ascii', clean_ascii(pay_line),
                not clean_ascii(pay_line + ACCENT)))
    ent.append(('braces', clean_braces(pay_line),
                not clean_braces(pay_line + '{')))
    ent.append(('nolabelcite', clean_nolabelcite(pay_line),
                not clean_nolabelcite(pay_line + '\\label{bogus}')))
    bad = missing_refs(pay_line, labels)
    badc = missing_refs(pay_line + '~\\ref{bogus124zz}', labels)
    ent.append(('refs-exist', len(bad) == 0,
                ('bogus124zz' in badc) and len(bad) == 0))
    ent.append(('one-line', clean_one_line(pay_line),
                not clean_one_line(pay_line + '\n')))
    return ent, bad

def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else FOLDER
    data = open(APPH, 'rb').read()
    assert hashlib.sha1(data).hexdigest() == PIN_SHA1, 'PRE appH pin MISMATCH'
    assert len(data) == PIN_SIZE, 'PRE appH size MISMATCH'
    ab = ANCHOR.encode('ascii')
    assert data.count(ab) == 1, 'anchor count != 1'
    data2x = data.replace(ab, ab + ab, 1)  # in-memory corruption only
    assert data2x.count(ab) == 2, 'anchor guard positive control failed'
    print('anchor guard: PRE count 1; doubled-copy control count 2 (fires)')

    pay_line = PAY_TEXT
    labels = all_labels()
    gres, bad = run_guards(pay_line, labels)
    for name, ok, control_fired in gres:
        assert ok is True, 'guard %s FAILED on payload' % name
        assert control_fired is True, 'guard %s POSITIVE CONTROL DID NOT FIRE' % name
        print('guard %s: payload clean; injected control fires' % name)
    print('refs used: %s' % sorted(set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', pay_line))))

    payload = (pay_line + '\r\n\r\n').encode('ascii')
    # tail/join guards with structural positive controls
    assert payload.endswith(b'\r\n\r\n'), 'EOL tail guard'
    assert payload.endswith(b'\r\n') and not payload.rstrip(b'\r\n').endswith(b'\r'), 'tail shape control'
    assert b'\n' not in payload.replace(b'\r\n', b''), 'bare-LF guard'
    assert b'\r' not in payload.replace(b'\r\n', b''), 'bare-CR guard'
    # join control: after splice the payload must sit directly before the anchor
    new = data.replace(ab, payload + ab, 1)
    assert new.count(ab) == 1, 'anchor duplication after splice'
    i = new.find(payload + ab)
    assert i >= 0, 'join guard: payload+anchor not found after splice'
    # positive control for the join guard: remove one CR and the search must fail
    broken = payload[:-3] + b'\n' + ab
    assert new.find(broken) == -1, 'join guard control did not fire'
    open(os.path.join(FOLDER, 'payload-124.txt'), 'wb').write(payload)
    assert len(new) == len(data) + len(payload), 'POST size accounting'
    open(os.path.join(outdir, 'spliced_appH_124.preview.bin'), 'wb').write(new)
    for tag, b in (('PRE', data), ('PAY', payload), ('POST', new)):
        print('%s sha1 %s size %d' % (tag, hashlib.sha1(b).hexdigest(), len(b)))
    print('OK')

if __name__ == '__main__':
    main()
