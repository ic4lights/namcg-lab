import re,glob,os
root=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
def norm(s): return re.sub(r'\s+',' ',s.replace('\r',''))
txt={os.path.basename(f):norm(open(f,encoding='utf-8').read()) for f in glob.glob(root+'/chapters/*.tex')}
allt=' '.join(txt.values())
anchors=[
('appK-endomorphism.tex',r'a_1=\operatorname{tr}(E)-\frac16 R\,\dim.'),
('appK-endomorphism.tex',r'On a Laplace-type operator \(\Delta=-D^\mu D_\mu+E\) the first Seeley--DeWitt coefficient is'),
('appK-endomorphism.tex',r'The first non-vanishing correction linear in the laboratory field appears in \(a_2\) and is proportional to \(F_{\mu\nu}F^{\mu\nu}\).'),
('ch17-agenda.tex',r'function has no propagating Ostrogradsky ghost for \(p<\LUV\), for the values of \(\alpha\) and \(G_{\mathrm{eff}}\) computed in Problem~F, with the region of those values in which it holds stated. The target is no stronger'),
('appH-microscopic-proofs.tex',r'function has no propagating Ostrogradsky ghost for \(p<\LUV\), for the values of \(\alpha\) and \(G_{\mathrm{eff}}\) computed in Problem~F, with the region of those values in which it holds stated. This is the requirement'),
('ch16-falsifiers.tex',r'\ref{ass:laplace} & setup & infrared operator is Laplace type '+'\\'),
('ch16-falsifiers.tex',r'and frame existence is part of Problem~D1. An assumption may remain'),
('ch16-falsifiers.tex',r'The Euclidean curvature coefficient obeys the conditional, truncated heat-kernel identity of Theorem~\ref{thm:Geff}; physical matching requires specified operators, weights, thresholds, continuation, and scheme (Problem~F).'),
]
for f,a in anchors:
    print(txt[f].count(norm(a)),f,a[:60])
for l in ['eq:appA-a1','eq:stelle','eq:W4','ch:ultraviolet','sec:status-N','app:seeley-dewitt','thm:Geff','ass:emergent-op','ass:laplace']:
    print(len(re.findall(re.escape('\label{')+re.escape(l)+r'\}',allt)),l)
