import os
here = os.path.dirname(os.path.abspath(__file__))
blk = open(os.path.join(here, 'block-r2.tex'), 'rb').read().decode('utf8').replace('\r\n', '\n')
F = '`' * 3
tpl = open(os.path.join(here, 'proposal-r2.template.md'), encoding='utf8').read()
open(os.path.join(here, 'proposal-r2.md'), 'w', encoding='utf8').write(tpl.replace('@@BLOCK@@', F + 'latex\n' + blk + F))
