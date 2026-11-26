# Proposal 089-g-profile-pushforward-weight, round 3
Mechanical repair; no new mathematics. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Result
insert-r3.tex = insert-r2.tex minus exactly one byte: in `...dT\=(D-1)!/\Lambda^{D}...`, `\=` becomes `=`. All other bytes identical.

## Incident record
- Integration attempt ordinal 20 failed the build: pdflatex aborted on insert-r2.tex, "Command \= invalid in math mode / Please use \mathaccent" (text-accent macro inside `\( ... \)`); exactly one occurrence, byte offset 1172, 9-byte token -> 8-byte fix.
- Both prior reviews lacked a compile step - the blind spot. A smoke-compile gate is now adopted: s2.py compiles the insert verbatim in an article-class text paragraph; insert-r3 PASS (rc 0), negative control insert-r2 EXPECTED-FAIL with the \= math error. The gate catches this defect class.

## Claim set
No claim, hypothesis class, classification or closer text altered: EXPLICITLY UNCHANGED from round 2; remaining open step unchanged.

## Byte contract
- insert-r2.tex 3,975 B sha256 bba6adc41efd7c6ed244ef2fafc435439c03e36c6aba4f77e9aeff4febba0136 (frozen; defective artifact + control).
- insert-r3.tex 3,974 B sha256 ccb89c9e85eaa59fcee84dd4d152d62ebf726b91ce7ebe8a4fe5a3da5e23a553.
- 1-byte identity: prefix [0,1172) equal; suffixes (r2 1181 / r3 1180 onward) equal; \= count 0; \( / \) 28/28.
- DEAD r2 POST: 752,791 B sha256 e5355e61f99f9b1e5dee0f17c727c478cf22cd0d1fad28fcf175128bfe10f1c8; ONLY reproducible from insert-r2.tex (a4.py); superseded.
- NEW POST: 752,790 B sha256 4b5213160fab6154dbefcdaaf5795501eebed9add432b910660ef2b4e62068d6; live appH 748,814/ecb67a25... + insert-r3 + CRLF at the 356-B PIN; invariants CRLF 3,842, bareLF 0, close-idiom 16, new-header 1, Vacuum-term 2.

## Decisions Taken
- 1-byte deletion over re-anchoring/rewording: smallest change preserving the round-2 accepted argument; rewording reopens verified prose.
- New-file policy continues: r1/r2 artifacts byte-frozen (asserted in h3.py); hygiene rebuild-from-body check inlined on the tex file.
- Scripts build backslash bytes via bytes([92])/chr(92) after an escape-corruption failure mode struck this round (caught by control-byte guards; inserts clean).

## Verification pack (re-run)
python -I scratch/r3b/b1.py -> BUILD OK 3974 ccb89c9e; s2.py -> SMOKE GATE OK; h3.py -> HYGIENE PASS (bs_eq 0, lp=rp=28, accInMath 0; hygiene_089_r3.out); a4.py -> SIMULATION OK POST 752790 (simulate_apply_089_r3.out).

## Gatekeeper instructions
Verify the 1-byte identity independently (prefix/suffix outside the 9->8-byte window); re-run smoke gate AND negative control; reproduce the NEW POST sha; confirm r1/r2 artifacts and chapters/ unchanged. The wrapper isolates the math-mode defect; full build_check is the integrator's step.
