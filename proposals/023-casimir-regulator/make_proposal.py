import os
here = os.path.dirname(os.path.abspath(__file__))
blk = open(os.path.join(here, 'block-r1.tex'), encoding='utf8').read().replace('\r\n', '\n')
tpl = open(os.path.join(here, 'proposal-r1.template.md'), encoding='utf8').read()
open(os.path.join(here, 'proposal-r1.md'), 'w', encoding='utf8').write(tpl.replace('@@BLOCK@@', blk.rstrip('\n') + '\n'))
