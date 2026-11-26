r"""Round-3 (Item 7 removed; ch03 anchor added): verify each anchor occurs exactly once (whitespace-normalised, CRLF-safe) and each \ref/\eqref
label used in the proposed text is defined exactly once; the new labels must be defined zero times now."""
import re, glob, sys
root = r'C:/Users/redgi/Projects/namcg-lab/chapters/'
def norm(s): return re.sub(r'\s+', ' ', s.replace('\r', ''))
anchors = {
 'appH-microscopic-proofs.tex': [r'\section{Problem G: HBEV}'],
 'ch08-heat-kernel.tex': [
   r'The justification is the derivative expansion:',
   r'\begin{proposition}[Scaffold replacement]',
   r'Self-consistently substituting the emergent metric is therefore valid through the order of this conditional truncated identity. \end{proposition}',
   r'Integrate \(\eta\) at one loop on a slowly varying emergent background \(g_{\mu\nu}\), using Presentation~B.',
   r'\item \textbf{Scaffold error.} Expand Proposition~\ref{prop:scaffold} to first order in \(h_{\mu\nu}\) on a flat scaffold and list the operators produced. Which of them renormalize \(\Geff\), and which renormalize higher-curvature couplings?'],
 'ch04-vierbein-emergence.tex': [r'Write one sentence stating when it is legitimate to replace \(g^{(0)}\) by \(g\) inside a heat kernel, and what error term that replacement drops. The full answer is Chapter~8; the sentence is due now.'],
 'appG-sector-entropy.tex': [r'For a Laplace-type fluctuation operator the heat-kernel expansion on the cone produces the area term'],
 'appB-modular.tex': [r'In Presentation~B the cover is a branched cover of the auxiliary manifold, later identified with the emergent spacetime by Proposition~\ref{prop:scaffold}. In Presentation~A the same construction requires Problem~A of Chapter~17.'],
 'ch05-lorentz-decomposition.tex': [r'On a Minkowski condensate the mixing terms that survive after gauge fixing are of the form \(\psi\,\partial\partial T\) and \(A\,\partial T\). They are the usual linearized scalar--tensor and vector--tensor mixings.'],
 'ch03-matrix-action.tex': [r'The auxiliary metric is a scaffold for writing derivatives and heat kernels. Chapter~8 uses this scaffold.'],
}
bad = 0
for f, lst in anchors.items():
    t = norm(open(root + f, encoding='utf-8', newline='').read())
    for a in lst:
        n = t.count(norm(a))
        print(f'{n}  {f}: {a[:70]}...')
        bad += n != 1
alltxt = ''.join(open(p, encoding='utf-8', newline='').read() for p in glob.glob(root + '*.tex'))
labels = """eq:Smicro eq:V ass:aux-metric eq:W-again eq:s-limits eq:appA-a0 eq:appA-a2 eq:universal-R eq:repairII-trace
eq:Z-sigma lem:msigma eq:D-both eq:g-from-e eq:vev-is-frame eq:FP-gauge eq:FP thm:mT sec:status-D sec:status-F eq:O-eta
thm:Geff eq:Geff-structure app:status ch:vierbein-emergence ch:heat-kernel ch:agenda eq:W-expand sec:ch8-which-g
rem:ch3-varying-theta""".split()
for l in labels:
    n = len(re.findall(r'\\label\{' + re.escape(l) + r'\}', alltxt))
    print(n, l); bad += n != 1
for l in ['ass:emergent-op', 'rem:ch8-scaffold-vs-emergent']:
    n = len(re.findall(r'\\label\{' + re.escape(l) + r'\}', alltxt))
    print(n, l, '(new; must be 0 now)'); bad += n != 0
print('PROBLEMS:', bad)
