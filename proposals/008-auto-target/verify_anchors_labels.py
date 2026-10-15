import re,glob,os
root=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
def norm(s): return re.sub(r'\s+',' ',s.replace('\r',''))
txt={os.path.basename(f):norm(open(f,encoding='utf-8').read()) for f in glob.glob(root+'/chapters/*.tex')}
allt=' '.join(txt.values())
anchors=[('appH-microscopic-proofs.tex',r'do not apply; no linearized-diffeomorphism invariance is claimed. Problems~B, C, D and~F remain open. \section{Problem G: HBEV}')]
for f,a in anchors: print(txt[f].count(norm(a)),f,a[:70])
for l in ['thm:Geff','eq:O-eta','ass:emergent-op','ass:dictionary','rem:ch3-moyal-check','rem:ch3-trace-quadratic','rem:ch3-varying-theta','def:composite-metric','eq:g-from-e','eq:vev-is-frame','eq:Smicro','eq:V','ass:EE','sec:status-B','sec:status-D','eq:Smatrix']:
    print(len(re.findall(re.escape('\label{')+re.escape(l)+r'\}',allt)),l)
print('LUV macro:', '\newcommand{\LUV}' in open(root+'/namcg-book7.tex',encoding='utf-8').read() or 'check preamble')
