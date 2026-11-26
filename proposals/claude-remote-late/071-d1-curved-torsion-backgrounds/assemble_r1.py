"""Assemble proposal-r1.md from its head, the exact insert block and its tail (run once)."""
from pathlib import Path

here = Path(__file__).resolve().parent
head = (here / 'proposal-r1.head.md').read_text(encoding='utf-8')
tail = (here / 'proposal-r1.tail.md').read_text(encoding='utf-8')
ins = (here / 'appH_insert_r1.tex').read_bytes().decode('utf-8').replace('\r\n', '\n')
mid = (
    "\n## Proposed changes\n\n"
    "**File:** `chapters/appH-microscopic-proofs.tex`, section `sec:status-D`. Only this file changes; "
    "there is no bibliography change.\n\n"
    "**Anchor:**\n"
    "- Insert the block below, followed by one blank line, immediately before the unique line "
    "`\\section{Problem E: signature}` (pre-image line 1631).\n"
    "- That puts it directly after the integrated 068 paragraph. The 068 paragraph's last sentence ends "
    "\"..., \\ref{ass:local-lorentz} and~\\ref{ass:EFT-a2} are not discharged; Problems~D, F and~N remain "
    "open and PROGRAMME-CONDITIONAL.\"\n"
    "- Nothing is replaced, and all existing text is kept. The exact CRLF block is `appH_insert_r1.tex`, "
    "applied by `apply_and_build_r1.py`.\n\n"
    "```latex\n" + ins + "```\n"
)
(here / 'proposal-r1.md').write_text(head + mid + tail, encoding='utf-8')
print('written', len(head + mid + tail))
