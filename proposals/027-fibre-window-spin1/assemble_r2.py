"""Assemble proposal-r2.md by inserting block-r2.tex at the placeholder; check the block is verbatim and free of withdrawn phrases."""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
h = open(os.path.join(here, '_p.md'), encoding='utf8').read()
b = open(os.path.join(here, 'block-r2.tex'), encoding='utf8').read().rstrip('\n')
out = h.replace('@@BLOCK@@', b)
open(os.path.join(here, 'proposal-r2.md'), 'w', encoding='utf8', newline='\n').write(out)
os.remove(os.path.join(here, '_p.md'))
print('verbatim:', b in out)
for pat in ['unique continuation', 'domain of dependence', 'Lipschitz', r'\\mathcal J_a', r'\\mathcal J_c', r'function \\\(g', r'\\mathsf J\b']:
    print(pat, len(re.findall(pat, b)))
